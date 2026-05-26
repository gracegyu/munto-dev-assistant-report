#!/usr/bin/env python3
"""
SRS.md 본문의 ![][imageN] 컨텍스트와 Book/image/ 파일명을 fuzzy 매칭하여
*확신도 높은 매핑만* 제안한다.

알고리즘 (4 가지 신호의 가중 합계):
    1. 출처 URL path segment ↔ 파일명 단어 직접 일치  (+100, 매우 강함)
    2. 본문 영문 단어 (3자 이상) ↔ 파일명 단어 직접 일치  (+80)
    3. 한국어 캡션 명사 ↔ 한국어 파일명 직접 일치        (+90)
    4. difflib.SequenceMatcher (캡션 전체 ↔ 파일명)       (보조, 0~40)

사용법:
    python3 srs_image_suggest.py [--threshold N] [--show-all]

옵션:
    --threshold N    이 점수 이상만 제안 (기본 60)
    --show-all       임계값 미달도 함께 출력 (디버깅용)
    --apply          *확신도 매우 높은 (90 이상)* 항목을 image_mapping.json 에 자동 추가
                     (이미 매핑된 라벨은 덮어쓰지 않음 — 안전)

출력:
    - 콘솔: 제안 매핑 표 (라벨 / 점수 / 파일 / 근거)
    - image_mapping.suggested.json: 점수·근거 포함 전체 제안 (사용자 검증용)
"""

from __future__ import annotations

import argparse
import json
import re
from collections import OrderedDict
from difflib import SequenceMatcher
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
BOOK_DIR = SCRIPT_DIR.parent
SRS_PATH = BOOK_DIR / "SRS.md"
IMAGE_DIR = BOOK_DIR / "image"
MAPPING_PATH = SCRIPT_DIR / "image_mapping.json"
SUGGESTED_PATH = SCRIPT_DIR / "image_mapping.suggested.json"

REF_PATTERN = re.compile(r"!\[\]\[image(\d+)\]")
URL_PATTERN = re.compile(r"https?://[^\s\)\]]+", re.IGNORECASE)
CAPTION_PATTERN = re.compile(r"^\s*\(([^)]+)\)")  # 줄 시작 (캡션)
ENG_WORD_PATTERN = re.compile(r"[A-Za-z][A-Za-z0-9]{2,}")
HANGUL_PATTERN = re.compile(r"[가-힣]{2,}")

# 매칭에서 무시할 너무 흔한 영문 단어
ENG_STOPWORDS = {
    "the", "and", "for", "with", "from", "into", "this", "that",
    "image", "img", "fig", "figure", "png", "jpg", "jpeg",
    "com", "kr", "www", "html", "http", "https",
}
# 매칭에서 무시할 너무 흔한 한글 단어 (캡션 노이즈)
KOR_STOPWORDS = {"삽화", "그림", "예시", "예제", "스펙", "프로젝트", "소프트웨어"}


def parse_args() -> argparse.Namespace:
    """CLI 인자."""
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    p.add_argument("--threshold", type=int, default=60, help="제안 임계 점수 (기본 60)")
    p.add_argument("--show-all", action="store_true", help="임계값 미달도 함께 출력")
    p.add_argument("--apply", action="store_true", help="점수 90 이상만 image_mapping.json 에 자동 추가")
    return p.parse_args()


def tokenize_filename(name: str) -> list[str]:
    """파일명을 키워드 리스트로 분해. 확장자 제외, 단어/CamelCase 분리, 소문자화."""
    stem = Path(name).stem
    # 언더스코어·하이픈·공백 분리
    parts = re.split(r"[_\-\s]+", stem)
    tokens: list[str] = []
    for part in parts:
        # CamelCase 분리 (영문)
        sub = re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)|\d+|[가-힣]+", part)
        for s in sub:
            if not s:
                continue
            tokens.append(s.lower() if s[0].isascii() else s)
    return tokens


def collect_context(lines: list[str], line_no: int, window: int = 6) -> str:
    """imageN 직후 N 줄 컨텍스트 텍스트 (캡션·출처 URL 포함)."""
    end = min(line_no + window, len(lines))
    return "\n".join(lines[line_no:end])


def extract_signals(context: str) -> tuple[str, list[str], list[str], list[str]]:
    """
    컨텍스트에서 4 가지 매칭 신호 추출.

    Returns:
        (caption_text, url_segments, eng_words, kor_words)
    """
    # 캡션: 직후 첫 (X) 패턴. 단 (http..) 출처 URL 은 제외.
    caption_text = ""
    for line in context.split("\n"):
        m = CAPTION_PATTERN.match(line)
        if m:
            inner = m.group(1).strip()
            if not inner.lower().startswith(("http://", "https://", "[http")):
                caption_text = inner
                break

    # URL path segments (출처 URL 의 마지막 path 부분)
    url_segments: list[str] = []
    for url_match in URL_PATTERN.finditer(context):
        url = url_match.group(0)
        # URL 의 path 마지막 segment 만 추출
        path_part = re.sub(r"^https?://[^/]+/", "", url).rstrip("/")
        if path_part:
            last_seg = path_part.split("/")[-1]
            # %XX 디코딩 (UTF-8 한글 등)
            try:
                from urllib.parse import unquote
                last_seg = unquote(last_seg)
            except Exception:
                pass
            # 토큰화
            for token in re.split(r"[_\-]+", last_seg):
                token = token.strip().lower()
                if len(token) >= 3 and token not in ENG_STOPWORDS:
                    url_segments.append(token)

    # 영문 단어 (캡션 + 직후 컨텍스트)
    eng_words = [w.lower() for w in ENG_WORD_PATTERN.findall(caption_text)]
    eng_words = [w for w in eng_words if w not in ENG_STOPWORDS]

    # 한국어 명사 (캡션)
    kor_words = [w for w in HANGUL_PATTERN.findall(caption_text) if w not in KOR_STOPWORDS]

    return caption_text, url_segments, eng_words, kor_words


def score_candidate(
    filename: str,
    caption: str,
    url_segs: list[str],
    eng_words: list[str],
    kor_words: list[str],
) -> tuple[int, list[str]]:
    """파일명 후보에 대해 점수 + 근거 키워드 반환."""
    file_tokens = tokenize_filename(filename)
    file_token_set_lower = set(file_tokens)
    score = 0
    reasons: list[str] = []

    # 1. URL segment 매칭 (가장 강한 신호)
    # 단, 파일 토큰이 3 자 미만이거나 숫자만으로 구성되면 가짜 매칭 위험 → 제외
    for seg in url_segs:
        if seg.isdigit() or len(seg) < 4:
            continue
        for ft in file_token_set_lower:
            if len(ft) < 3 or ft.isdigit():
                continue
            if seg == ft or (len(seg) >= 5 and (seg in ft or ft in seg)):
                score += 100
                reasons.append(f"url:'{seg}'↔'{ft}'")
                break

    # 2. 영문 단어 직접 매칭 (파일 토큰도 3 자 이상이어야 의미 있음)
    matched_eng = set()
    for word in eng_words:
        if word in matched_eng or len(word) < 3:
            continue
        for ft in file_token_set_lower:
            if len(ft) < 3 or ft.isdigit():
                continue
            if word == ft:
                score += 80
                reasons.append(f"eng:'{word}'")
                matched_eng.add(word)
                break
            elif len(word) >= 4 and len(ft) >= 4 and word in ft:
                score += 40
                reasons.append(f"eng~:'{word}'⊂'{ft}'")
                matched_eng.add(word)
                break

    # 3. 한국어 단어 직접 매칭 (한국어 파일명에만 의미)
    for word in kor_words:
        if word in file_token_set_lower:
            score += 90
            reasons.append(f"kor:'{word}'")

    # 4. SequenceMatcher 보조 (캡션 vs 파일명 stem 전체 단어 조인)
    if caption:
        file_stem = " ".join(file_tokens)
        ratio = SequenceMatcher(None, caption.lower(), file_stem).ratio()
        bonus = int(ratio * 40)
        if bonus > 0:
            score += bonus
            if bonus >= 15:
                reasons.append(f"seq:{ratio:.2f}")

    return score, reasons


def build_suggestions(
    srs_path: Path,
    image_dir: Path,
    existing_mapping: dict[str, str],
) -> list[dict]:
    """모든 imageN 라벨에 대해 최고 점수 후보 + 차상위 후보 반환."""
    text = srs_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    file_list = [
        p.name for p in image_dir.iterdir()
        if p.is_file() and p.suffix.lower() in {".png", ".jpg", ".jpeg", ".bmp", ".gif"}
    ]
    file_list.sort()

    suggestions: list[dict] = []
    # ![][imageN] 위치 찾기 (라벨별 첫 등장만)
    seen: dict[str, int] = {}
    for i, line in enumerate(lines):
        m = REF_PATTERN.search(line)
        if m:
            label = m.group(1)
            if label not in seen:
                seen[label] = i

    for label, line_no in sorted(seen.items(), key=lambda kv: int(kv[0])):
        if label in existing_mapping:
            # 이미 매핑된 라벨은 건너뜀
            continue
        context = collect_context(lines, line_no + 1, window=6)
        caption, urls, eng, kor = extract_signals(context)

        scored = []
        for fname in file_list:
            score, reasons = score_candidate(fname, caption, urls, eng, kor)
            if score > 0:
                scored.append((score, fname, reasons))
        scored.sort(key=lambda x: x[0], reverse=True)

        top = scored[0] if scored else None
        runner = scored[1] if len(scored) >= 2 else None

        suggestions.append({
            "label": label,
            "line_no": line_no + 1,
            "caption": caption,
            "top": {
                "score": top[0] if top else 0,
                "file": f"image/{top[1]}" if top else None,
                "reasons": top[2] if top else [],
            },
            "runner_up": {
                "score": runner[0] if runner else 0,
                "file": f"image/{runner[1]}" if runner else None,
            } if runner else None,
        })

    return suggestions


def main() -> int:
    """엔트리 포인트."""
    args = parse_args()

    if not SRS_PATH.exists() or not IMAGE_DIR.exists() or not MAPPING_PATH.exists():
        print("[ERROR] SRS.md / image / mapping 중 하나가 없습니다.")
        return 2

    mapping_raw = json.loads(MAPPING_PATH.read_text(encoding="utf-8"))
    existing = {k: v for k, v in mapping_raw.items() if not k.startswith("_")}

    suggestions = build_suggestions(SRS_PATH, IMAGE_DIR, existing)

    # 임계값 이상만 카운트
    above = [s for s in suggestions if s["top"]["score"] >= args.threshold]
    high = [s for s in suggestions if s["top"]["score"] >= 90]

    print(f"[INFO] 미매핑 라벨 {len(suggestions)} 개 / 임계값({args.threshold}) 이상 {len(above)} 개 / 90 점 이상 {len(high)} 개")
    print()

    # 제안 표 출력 (검증용 — 캡션 포함)
    target = suggestions if args.show_all else above
    for s in target:
        top = s["top"]
        marker = "★" if top["score"] >= 90 else " "
        caption = s["caption"][:60] if s["caption"] else "(캡션 없음)"
        reasons_str = ", ".join(top["reasons"][:3])
        runner = s.get("runner_up")
        runner_str = ""
        if runner and runner["file"] and runner["score"] >= args.threshold * 0.7:
            runner_str = f"   (2위: {runner['file']} {runner['score']})"
        print(f"{marker} image{s['label']:>3}  [{top['score']:>4}점]  → {top['file']}{runner_str}")
        print(f"        캡션: {caption}")
        print(f"        근거: {reasons_str}")
        print()

    # suggested.json 저장 (검증용)
    SUGGESTED_PATH.write_text(
        json.dumps(
            OrderedDict([
                ("_comment", "자동 제안 매핑. 사용자 검증 후 image_mapping.json 으로 promote."),
                ("_threshold_used", args.threshold),
                ("_total", len(suggestions)),
                ("_above_threshold", len(above)),
                ("_high_confidence_90plus", len(high)),
                ("suggestions", suggestions),
            ]),
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"\n[INFO] 상세 결과 저장: {SUGGESTED_PATH.name}")

    # --apply: 90 점 이상만 매핑에 자동 추가
    if args.apply:
        added = 0
        for s in high:
            if s["label"] not in existing:
                existing[s["label"]] = s["top"]["file"]
                added += 1
        # 메타 갱신 + 저장
        merged = OrderedDict()
        merged["_comment"] = mapping_raw.get("_comment", "")
        merged["_file_count_total"] = mapping_raw.get("_file_count_total", 124)
        merged["_mapped_count"] = len(existing)
        merged["_unmapped_count"] = 124 - len(existing)
        # 라벨 숫자 순 정렬
        for k in sorted(existing.keys(), key=int):
            merged[k] = existing[k]
        MAPPING_PATH.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\n[INFO] --apply: 90 점 이상 {added} 개를 image_mapping.json 에 추가했습니다.")
        print("       (다음 단계: python3 srs_image_relink.py --dry-run 으로 변경 미리보기)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
