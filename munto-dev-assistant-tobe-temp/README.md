# munto-dev-assistant-tobe-temp

> ⚠️ **임시 레포 — 리뷰 전용**. 적용 후 본 레포는 아카이브 또는 삭제됩니다.

## 본 레포의 목적

`Agentic Dev Chain` TO-BE 정책의 *변경 예정 본* 을 담습니다. 정책 본문 (AS-IS / TO-BE / brief) 의 *합의가 끝나면* 본 레포 내용을 운영 레포 `munto-dev-assistant` 로 *일괄 이관* 합니다.

본 레포는 *원칙·방향* 이 아니라 *실물 (Skill 갱신본·IP 견본·Spec 작성 표준 등)* 이 본인 도메인에 *어떻게 박힐지* 를 검토하는 자료입니다. *원칙·방향 합의* 는 아래 Notion 3 종을 참고하세요.

## 함께 보세요 (Notion)

- **AS-IS — 현재 하네스 진단**: <https://www.notion.so/Munto-Dev-Assistant-AS-IS-36de2bc7639d808d9cedd2252484fd92>
- **TO-BE — 프로세스·정책 원천**: <https://www.notion.so/Agentic-Dev-Chain-Munto-TO-BE-36de2bc7639d8052b13fc49575c10e56>
- **팀 개발자 브리핑 (요약본)**: <https://www.notion.so/Agentic-Dev-Chain-TO-BE-36de2bc7639d8093abbbe41b623252d7>

> 본 레포는 위 brief 의 §12 (함께 보면 좋은 문서) 에서 *적용 대기본 실물* 의 위치로 참조됩니다.

## 리뷰 가이드

- **기한**: YYYY-MM-DD HH:MM
- **코멘트 채널**: 본 레포 *PR 또는 Issue* 우선. 보조로 Slack `#agentic-dev-chain` *(채널명 확인 필요)*
- **의제 3 가지**:
  1. 본 폴더의 *적용 대기본 실물* 이 본인 도메인 (BE/FE/App/하네스) 에 맞는가
  2. Notion 의 *원칙 합의* 와 본 *실물* 사이 정합성에 깨짐은 없는가
  3. 적용 직후 *놀라움 요소* (예: `munto-spec-writer` 호출 시 *세션 첫 1 회 질문* 추가, `MUNTO_AUTHOR_ID` 환경변수 설정 요구 등) 가 본인 워크플로우와 충돌하는가

## 적용 절차

1. 본 레포 리뷰 PASS (위 기한 내)
2. 하네스 담당이 *적용 PR* 작성 — 본 레포 내용 → 운영 레포 `munto-dev-assistant`
3. 운영 적용 후 본 레포 *아카이브 (read-only)* 또는 *삭제*

## 폴더 안내

> **경로 텍스트 해석 안내**: 본 폴더 내 파일들이 본문에서 참조하는 `reports/2026-05-harness-*.md` 경로 텍스트는 위 *함께 보세요 (Notion)* 의 AS-IS / TO-BE 페이지와 *동일 내용*. 본 임시 GitHub 레포에서는 해당 경로가 *클릭되지 않으며*, 운영 레포 `munto-dev-assistant` 적용 후에야 상대경로로 동작합니다. 적용 전에는 위 Notion 링크를 사용하세요.

### 핵심 표준

| 파일 | 무엇 |
| --- | --- |
| `ip-standard.md` | **IP 표준** — TO-BE §4.3 IP-x 의 실물. *IP 작성 책임자 필독* |
| `spec-philosophy.md` | Spec 작성 철학 (`spec-standard.md` 에서 분리) |
| `spec-writing-tips.md` | Spec 작성 실무 팁 (`spec-standard.md` 에서 분리) |
| `spec-standard.md` | **Spec 작성 표준 (대형 — 발췌 정독 권장)**. 전체 정독 의무 아님 |

### IP 견본

| 파일 | 무엇 |
| --- | --- |
| `projects/_template/ImplementationPlan.md` | IP 본문 견본 — *실제 IP 가 어떻게 박힐지* |
| `projects/_template/README.md` | 견본 사용법 (`cp -R _template/ {프로젝트명}/` 절차) |
| `projects/README.md` | 활성 프로젝트 인덱스 양식 |

### 스킬 갱신본

| 파일 | 무엇 |
| --- | --- |
| `skills/README.md` | **본 폴더 안내 — 반드시 먼저 정독**. 적용 대기본의 *목적·이관 절차·변경 이력* |
| `skills/munto-spec-writer/SKILL.md` | spec-writer 갱신 — *세션 자동 저장 + `{author-id}` 1 회 질문* |
| `skills/munto-spec-review/SKILL.md` | spec-review 갱신 — *baseline-handoff 자동 점검 BLOCKER* |
| `skills/dev-chain-implementation-plan/SKILL.md` | IP 작성 스킬 |

### 옵션·부분 독립 트랙 *(본 리뷰의 *주의제 아님*)*

| 파일 | 무엇 | 트랙 |
| --- | --- | --- |
| `.claude-hooks-proposal.json` | Claude Code Stop Hook 견본. 매 turn 자동 캡처. *각 개발자 PC 적용* | *옵션 — 본인 디버그용*. `MUNTO_AUTHOR_ID` 환경변수 1 회 설정 필요 |
| `dev-chain-design-update-proposal.md` | `dev-chain-design` 스킬 갱신 제안 | *부분 독립 — 별도 PR 트랙* |

## 적용 후 본 레포는 어떻게 되나

- 적용 PR 머지 직후 *아카이브* (read-only) 권장 — *6 개월간* 참조용 보존
- 보존 기간 종료 후 *삭제*. 모든 내용은 운영 레포 `munto-dev-assistant` 의 *변경 이력* 으로 추적 가능
