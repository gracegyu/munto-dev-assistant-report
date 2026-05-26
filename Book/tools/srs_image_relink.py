#!/usr/bin/env python3
"""
SRS.md 의 이미지 참조 (reference-style) 를 인라인 이미지 (inline) 로 변환한다.

처리 동작:
    1. 본문의  ![alt][imageN]  →  ![alt](image/파일명)  (인라인 직접 삽입)
       - 파일명에 공백이 있으면 <image/파일명> 형태로 angle bracket 처리 (CommonMark 표준)
    2. 정의 영역의 [imageN]: <data:image/...;base64,...>  또는 [imageN]: image/...  줄을 삭제
    3. 매핑되지 않은 라벨은 *건드리지 않음* (안전 우선)

사용법:
    python3 srs_image_relink.py [--dry-run] [--mapping PATH] [--srs PATH]

옵션:
    --dry-run  실제 파일 수정 없이 변경 예정만 출력
    --mapping  매핑 JSON 경로 (기본: 스크립트 옆 image_mapping.json)
    --srs      SRS.md 경로 (기본: ../SRS.md)

원칙:
    - 매핑된 파일이 실제로 Book/image/ 에 존재하지 않으면 WARNING 출력 후 *건너뜀* (해당 라벨은 그대로 둠)
    - 한 번 실행 후 다시 실행해도 안전 (idempotent): 이미 인라인으로 바뀐 본문은 패턴이 안 맞아 건너뜀
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# ---- 패턴 ----
# 본문의 reference-style 이미지 참조: ![alt text][imageN]
#   alt text 는 공백/한글 가능, 비어도 됨. 라벨은 image+숫자.
INLINE_REF_PATTERN = re.compile(r"!\[([^\]]*)\]\[image(\d+)\]")

# 정의 영역 줄: [imageN]: <data:image/...>  또는  [imageN]: image/...  또는 [imageN]: <...>
DEF_LINE_PATTERN = re.compile(r"^\[image(\d+)\]:\s*")


def parse_args() -> argparse.Namespace:
    """CLI 인자 파싱."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    script_dir = Path(__file__).resolve().parent
    parser.add_argument("--dry-run", action="store_true", help="실제 수정 없이 변경 예정만 출력")
    parser.add_argument("--mapping", type=Path, default=script_dir / "image_mapping.json", help="매핑 JSON 경로")
    parser.add_argument("--srs", type=Path, default=script_dir.parent / "SRS.md", help="SRS.md 경로")
    return parser.parse_args()


def load_mapping(path: Path) -> dict[str, str]:
    """매핑 JSON 로드. '_' 로 시작하는 키는 메타 정보로 무시."""
    with path.open("r", encoding="utf-8") as f:
        raw = json.load(f)
    return {k: v for k, v in raw.items() if not k.startswith("_")}


def format_inline_path(rel_path: str) -> str:
    """
    인라인 이미지의 경로 문자열을 만든다.
    공백 등이 포함된 경우 CommonMark 의 angle bracket 형식 (<...>) 으로 감싼다.
    그 외에는 그대로 사용한다.
    """
    if any(c in rel_path for c in [" ", "(", ")"]):
        return f"<{rel_path}>"
    return rel_path


def transform(lines: list[str], mapping: dict[str, str], image_dir: Path) -> tuple[list[str], dict]:
    """
    SRS.md 의 라인 리스트를 인라인 변환 + 정의 삭제 처리한다.

    Returns:
        (new_lines, stats)
        stats: {
            "body_changes":  [(line_no, label, new_inline_text), ...],
            "def_removals":  [(line_no, label, removed_kb), ...],
            "warnings":      [warning_text, ...],
        }
    """
    body_changes: list[tuple[int, str, str]] = []
    def_removals: list[tuple[int, str, int]] = []
    warnings: list[str] = []
    new_lines: list[str] = []

    for line_no, line in enumerate(lines, start=1):
        # 1) 정의 영역 줄인가? — 매핑된 라벨이면 *줄 자체 삭제*
        m_def = DEF_LINE_PATTERN.match(line)
        if m_def:
            label_num = m_def.group(1)
            if label_num in mapping:
                # 실제 파일 존재 확인
                target_rel = mapping[label_num]
                target_filename = Path(target_rel).name
                if not (image_dir / target_filename).exists():
                    warnings.append(
                        f"  L{line_no} image{label_num} → '{target_rel}' 실제 파일 없음, 정의 줄 유지"
                    )
                    new_lines.append(line)
                    continue
                # 매핑됐고 파일 존재 → 줄 자체 삭제 (new_lines 에 추가하지 않음)
                kb = len(line) // 1024
                def_removals.append((line_no, label_num, kb))
                continue
            # 매핑 안 된 라벨 — 그대로 유지
            new_lines.append(line)
            continue

        # 2) 본문의 reference-style 참조를 인라인으로 변환
        def _sub(m: re.Match) -> str:
            alt = m.group(1)
            label = m.group(2)
            target_rel = mapping.get(label)
            if target_rel is None:
                # 매핑 안 됨 — 그대로 둠
                return m.group(0)
            target_filename = Path(target_rel).name
            if not (image_dir / target_filename).exists():
                # 파일이 실제로 없음 — 변환하지 않음 (warning 은 정의 줄 쪽에서 출력)
                return m.group(0)
            inline_path = format_inline_path(target_rel)
            new_text = f"![{alt}]({inline_path})"
            body_changes.append((line_no, label, new_text))
            return new_text

        new_line = INLINE_REF_PATTERN.sub(_sub, line)
        new_lines.append(new_line)

    return new_lines, {
        "body_changes": body_changes,
        "def_removals": def_removals,
        "warnings": warnings,
    }


def main() -> int:
    """엔트리 포인트."""
    args = parse_args()

    if not args.mapping.exists():
        print(f"[ERROR] 매핑 파일이 없습니다: {args.mapping}", file=sys.stderr)
        return 2
    if not args.srs.exists():
        print(f"[ERROR] SRS.md 가 없습니다: {args.srs}", file=sys.stderr)
        return 2

    mapping = load_mapping(args.mapping)
    image_dir = args.srs.parent / "image"

    print(f"[INFO] 매핑 항목: {len(mapping)} 개  /  SRS.md: {args.srs}")

    with args.srs.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    old_size_mb = args.srs.stat().st_size / (1024 * 1024)

    new_lines, stats = transform(lines, mapping, image_dir)

    if stats["warnings"]:
        print(f"\n[WARNING] 건너뛴 매핑 ({len(stats['warnings'])} 건):")
        for w in stats["warnings"]:
            print(w)

    if stats["body_changes"]:
        print(f"\n[INFO] 본문 인라인 변환 ({len(stats['body_changes'])} 건):")
        for line_no, label, new_text in stats["body_changes"]:
            preview = new_text if len(new_text) <= 100 else new_text[:97] + "..."
            print(f"  L{line_no}  image{label}  →  {preview}")

    if stats["def_removals"]:
        print(f"\n[INFO] 정의 영역 줄 삭제 ({len(stats['def_removals'])} 건):")
        total_kb = sum(kb for _, _, kb in stats["def_removals"])
        for line_no, label, kb in stats["def_removals"]:
            print(f"  L{line_no}  image{label}  ({kb} KB 삭제)")
        print(f"  → 정의 영역 절감 합계: {total_kb} KB")

    if not stats["body_changes"] and not stats["def_removals"]:
        print("\n[INFO] 변경 사항 없음.")
        return 0

    if args.dry_run:
        print("\n[INFO] --dry-run 모드 — 실제 파일은 수정하지 않았습니다.")
        return 0

    tmp_path = args.srs.with_suffix(".md.tmp")
    with tmp_path.open("w", encoding="utf-8") as f:
        f.writelines(new_lines)
    tmp_path.replace(args.srs)

    new_size_mb = args.srs.stat().st_size / (1024 * 1024)
    delta_kb = (old_size_mb - new_size_mb) * 1024
    print(f"\n[INFO] 적용 완료. 크기 변화: {old_size_mb:.2f} MB → {new_size_mb:.2f} MB  (Δ −{delta_kb:.1f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
