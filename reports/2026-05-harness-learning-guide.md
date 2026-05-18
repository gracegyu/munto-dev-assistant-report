# Munto Dev Assistant 하네스 — 학습 가이드

> **이 문서의 범위**: `munto-dev-assistant` 하네스를 **스스로 이해·분석**하려는 사람을 위한 **학습 로드맵과 실습 안내**.
> 하네스의 현재 상태 분석은 [2026-05-harness-AS-IS.md](./2026-05-harness-AS-IS.md), 개선 프로세스는 [2026-05-harness-TO-BE.md](./2026-05-harness-TO-BE.md) 참고.

---

## 1. 학습 로드맵 (개인 기준)

| 순서 | 할 일 |
|------|--------|
| 1 | `AGENTS.md` 정독 (진입점·금지·체인·에이전트별 차이). |
| 2 | 구조 목록은 `README.md`보다 `AGENTS.md` 우선(README는 설치·워크스페이스 빠른 참고용). |
| 3 | `AGENTS.md` 언급과 실제 `.agents/skills/`·`commands/` 트리 대조. |
| 4 | (선택) `check-adapters.sh` 실행 — 래퍼 검증 원리만 이해하면 됨, 학습 **선행 필수 아님**. |
| 5 | `dev-chain-design`, 본인 도메인 `dev-chain-*`, `harness-diagnostics` 등 대표 스킬 정독. |
| 6 | 본인 스택 규칙 `.agents/rules/...` + `.cursor/rules/*.mdc` 대응 관계 확인. |
| 7 | Codex 사용자: `.codex/README.md` 및 worker/explorer 패턴. |

**실습 아이디어**: 가상 기능에 대해 WBS 스킵·설계 입력만 적고 어떤 서브에이전트에 무엇을 줄지 글로만 연습.

---

## 2. 준비도 평가 관점 (트렌드·메타 학습용)

하네스의 성숙도를 평가할 때 쓸 수 있는 두 축:

1. **`harness-diagnostics`의 12원칙**(진입점, 불변식, 관측 가능성 등).
2. **업계 흐름**: MCP·멀티에이전트·스킬 패키징·회귀/평가 자동화.

### 현재 하네스의 강점

- `AGENTS.md` 진입점, 어댑터 패턴, Development Chain 스킬화.
- `dev-chain-design`의 PM·병렬 writer·reviewer 패턴.
- 서브에이전트 계약, 실무 MCP·CLI 연동.

### 현재 하네스의 갭

- Cursor 패리티(서브에이전트 없음).
- 래퍼 **CI 미부착**(로컬만).
- 텍스트 룰의 런타임 강제 한계.
- 골든 시나리오 등 회귀 체계 부재.

> 각 항목의 상세 분석은 [AS-IS 분석](./2026-05-harness-AS-IS.md) §4 비판 참고.

---

## 3. 관련 문서 안내

| 문서 | 쓰임 |
|------|------|
| [AS-IS 분석](./2026-05-harness-AS-IS.md) | `munto-dev-assistant`의 **현재 상태** 분석과 비판. |
| [TO-BE 프로세스 가이드](./2026-05-harness-TO-BE.md) | AS-IS 비판을 바탕으로 한 **개선 프로세스·다이어그램·단계별 사용법**. |
| [팀 개발자 브리핑](../2026-05-harness-team-developer-brief.md) | **문제·개선 로드맵·교육/온보딩** 공유. |

---

## 변경 이력

| 일자 | 내용 |
|------|------|
| 2026-05-18 | AS-IS 분석 문서에서 학습 로드맵·준비도 평가를 분리하여 신규 작성 |
