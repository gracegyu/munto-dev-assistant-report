# Agentic Dev Chain TO-BE — 운영 적용 단계별 계획

> **목적**: `munto-dev-assistant-tobe-temp/` 의 검토 완료본을 운영 레포 `munto-dev-assistant` 로 일괄 이관한다.
> **방식**: 브랜치 생성 → 여러 커밋으로 분리 → push → GitHub PR.
> **커밋 주체**: 코드 준비는 에이전트, **commit·push·PR 생성은 본인이 직접 수행**한다.
> **체크박스 사용법**: 완료한 항목은 `[ ]` → `[x]` 로 바꿔 진행 상황을 추적한다.

---

## 적용 범위 — 두 단계로 나눠 진행

`munto-dev-assistant-tobe-temp/` 는 TO-BE 문서의 **부분집합만 실물화**해 둔 상태다. 따라서 적용을 두 범위로 분리한다.

| 범위 | 내용 | 본 문서에서의 위치 |
| --- | --- | --- |
| **(A) 1차 PR — 이관** | tobe-temp 에 *파일로 존재하는 것* 을 운영 경로로 옮기고 경로만 수정 | **Phase 0~7** (아래) |
| **(B) 후속 — TO-BE 전체 구현** | tobe-temp 에도 없어 *새로 저작* 해야 하는 TO-BE 강제 항목 | **§ 후속 PR 백로그** (하단) |

> **원칙**: (B) 는 *한꺼번에 만들지 않는다* (TO-BE §2.3 ② "필요한 시점에 작게 추가"). 1차 PR 은 (A) 로 한정하고, (B) 는 백로그에 *누락 없이* 적어 두고 하나씩 별도 PR 로 진행한다.

---

## 0. 절차 요약

| 질문 | 답 |
| --- | --- |
| 브랜치를 먼저 만드나? | **예.** `main` 최신화 후 feature 브랜치 생성 |
| 커밋을 여러 번 나눠도 되나? | **예, 권장.** 리뷰·롤백·이력 추적에 유리 |
| push 후 PR? | **예.** `git push -u origin <branch>` → `gh pr create` (또는 GitHub UI) |
| PR 개수 | **1개 권장.** 표준 + projects + 스킬 + 어댑터가 한 덩어리로 동작 |

### 브랜치명

이 레포는 이미 `feat/DEVT-136/add-backend-review-hotfix-skills` 처럼 **`feat/{Jira키}/{설명}`** 컨벤션을 사용한다.

| 형태 | 예시 |
| --- | --- |
| Jira 키 있을 때 (권장) | `feat/DEVT-XXX/agentic-dev-chain-tobe` |
| Jira 키 없을 때 | `feat/agentic-dev-chain-tobe` |

### 이번 PR에서 제외 (별도 트랙)

- `.claude-hooks-proposal.json` → 개인 PC / 별도 PR
- `dev-chain-design-update-proposal.md` 본문 대규모 반영 → 팀 결정 후 (검토안만 참고로 포함 가능)

---

## Phase 0 — 준비 (로컬, 커밋 없음)

- [x] `main` 최신화 (`git fetch origin` → `git checkout main` → `git pull origin main`)
- [x] feature 브랜치 생성 (`git checkout -b feat/agentic-dev-chain-tobe`)
- [ ] 이관 소스 위치 확인: `munto-dev-assistant-report/munto-dev-assistant-tobe-temp/`
- [ ] tobe-temp SKILL 상단 `<!-- ... -->` 기획 주석 제거 방침 확인 (skills/README §3)

```bash
cd /Users/gracegyu/Documents/GitMunto/munto-dev-assistant
git fetch origin
git checkout main && git pull origin main
git checkout -b feat/agentic-dev-chain-tobe
```

---

## Phase 1 — 표준 문서 (`document/`)

**커밋 예시:** `docs: IP·Spec 표준 및 작성 가이드 추가`

- [ ] `ip-standard.md` → `document/ip-standard.md` **(위치 결정: `document/`)**
- [ ] `spec-standard.md` → `document/spec-standard.md` (**덮어쓰기** — diff 크므로 PR 설명에 강조)
- [ ] `spec-philosophy.md` → `document/spec-philosophy.md`
- [ ] `spec-writing-tips.md` → `document/spec-writing-tips.md`
- [ ] `munto-spec-*` 스킬이 참조하는 `document/spec-standard.md` 경로가 유효한지 확인

> **결정 — `ip-standard.md` 는 `document/` 에 둔다.** TO-BE §IP-1 등은 단일 진실 공급원을 **`munto-dev-assistant/ip-standard.md`(레포 루트)** 로 표기하므로, 이 결정에 맞춰 **TO-BE 문서·tobe-temp IP 스킬·projects 템플릿의 경로 표기를 모두 `document/ip-standard.md` 로 수정**해야 한다.
> - TO-BE 문서 수정은 (B) 백로그 항목으로 추적 (하단 § 후속 PR 백로그).
> - 1차 PR 안에서 고쳐야 할 경로(IP 스킬 내부 참조·projects 템플릿)는 Phase 2·Phase 3-② 의 "경로 수정" 체크 항목에 포함.

---

## Phase 2 — `projects/` 견본·인덱스 (신규 폴더)

**커밋 예시:** `feat: projects 템플릿 및 활성 프로젝트 인덱스 추가`

- [ ] `projects/README.md` → `projects/README.md`
- [ ] `projects/_template/ImplementationPlan.md` → `projects/_template/ImplementationPlan.md`
- [ ] `projects/_template/README.md` → `projects/_template/README.md`
- [ ] 내부 상대 경로를 운영 레포 기준으로 수정 (`../../skills/...` → `.agents/skills/...`, `ip-standard.md` 참조 → `document/ip-standard.md` 등)

---

## Phase 3 — 스킬 본문 (`.agents/`)

**커밋 예시 ①:** `feat(skills): spec-writer·spec-review TO-BE 세션·baseline 반영`

- [ ] `skills/munto-spec-writer/SKILL.md` → `.agents/skills/common/docs/munto-spec-writer/SKILL.md`
- [ ] `skills/munto-spec-review/SKILL.md` → `.agents/skills/common/docs/munto-spec-review/SKILL.md`

**커밋 예시 ②:** `feat(skills): dev-chain-implementation-plan 신규`

- [ ] `skills/dev-chain-implementation-plan/SKILL.md` → `.agents/skills/common/docs/dev-chain-implementation-plan/SKILL.md`
- [ ] 스킬 내부 `ip-standard.md` 참조를 **`document/ip-standard.md`** 로 수정 (tobe-temp 의 `../../../ip-standard.md` → 운영 경로)
- [ ] (선택) `dev-chain-design` Step 5 마지막에 "다음: `dev-chain-implementation-plan`" 한 줄 안내 추가

> **위치 결정**: tobe README는 `backend/docs` 후보도 제시하나, `dev-chain-design`·`dev-chain-wbs`와 일관되게 **`common/docs`** 권장.

---

## Phase 4 — 서브에이전트 (권장: Phase 3과 같은 PR)

`dev-chain-implementation-plan` 이 `Task(subagent_type=ip-writer)` 를 호출하므로, 없으면 스킬이 반쪽이 된다.

- [ ] `spec-reviewer.md` 패턴 복사 → `.agents/agents/ip-writer.md` 작성
- [ ] `.agents/agents/ip-reviewer.md` 작성 (생성-검증 페어)
- [ ] `.claude/agents/ip-writer.md` / `ip-reviewer.md` 래퍼 생성
- [ ] (Codex 사용 시) `.codex/agents/` 어댑터 생성

**커밋 예시:** `feat(agents): ip-writer·ip-reviewer 서브에이전트 추가`

> proposal은 "별도 PR"도 허용. 1차 PR 완성도를 위해 같은 PR 포함 권장. 분리한다면 Phase 3-② 스킬도 함께 2차 PR로 미룬다.

---

## Phase 5 — 어댑터·목록

**커밋 예시:** `chore: Claude·Codex 스킬 어댑터 및 AGENTS.md 갱신`

- [ ] `.claude/skills/dev-chain-implementation-plan/SKILL.md` 얇은 래퍼 생성
- [ ] `.codex/skills/dev-chain-implementation-plan/SKILL.md` (`source:` 선언) 생성
- [ ] `AGENTS.md` 활성 스킬 목록에 `dev-chain-implementation-plan` 추가
- [ ] (선택) `munto-skills` SKILL 목록 동기화
- [ ] `bash scripts/check-adapters.sh` 실행 → 깨진 참조 0건 확인

```bash
bash scripts/check-adapters.sh
```

---

## Phase 6 — 검토안·제외물 (선택)

**커밋 예시:** `docs: dev-chain-design IP 단계 검토안 추가`

- [ ] (선택) `dev-chain-design-update-proposal.md` → `document/dev-chain-design-update-proposal.md` (참고용)
- [ ] `.claude-hooks-proposal.json` 은 PR에 **포함하지 않음** 확인

---

## Phase 7 — push & PR

- [ ] `git push -u origin feat/agentic-dev-chain-tobe`
- [ ] `gh pr create` (또는 GitHub UI)로 PR 생성

```bash
git push -u origin feat/agentic-dev-chain-tobe
gh pr create --title "feat: Agentic Dev Chain TO-BE 하네스 적용" --body "..."
```

### PR 본문 체크

- [ ] Notion TO-BE / brief 링크 첨부
- [ ] 변경 요약 (표준 / projects / 스킬 / 에이전트)
- [ ] `bash scripts/check-adapters.sh` 통과 명시
- [ ] 리뷰어 체크 포인트: `{author-id}` 1회 질문 / `MUNTO_AUTHOR_ID`(Hook 별도) / `spec-baseline-handoff` BLOCKER
- [ ] 의도적 제외 명시: Hooks, design 스킬 본문 대개편

---

## 커밋 분리 권장 순서

| # | 커밋 메시지(예) | 비고 |
| --- | --- | --- |
| 1 | `docs: IP·Spec 표준` | Phase 1 |
| 2 | `feat: projects/` | Phase 2 |
| 3 | `feat(skills): spec-writer, spec-review` | Phase 3-① |
| 4 | `feat(skills): dev-chain-implementation-plan` | Phase 3-② (+경로 수정) |
| 5 | `feat(agents): ip-writer, ip-reviewer` | Phase 4 (4와 합쳐도 됨) |
| 6 | `chore: adapters + AGENTS.md` | Phase 5 |
| 7 | (선택) `docs: design-update-proposal` | Phase 6 |

> 스쿼시는 머지 시 GitHub에서 수행 가능. 리뷰 중에는 분리 커밋 유지가 낫다.

---

## PR 이후 (운영)

- [ ] 리뷰·CI·`check-adapters.sh` 통과 → merge
- [ ] 팀에 brief / Notion 안내
- [ ] `munto-dev-assistant-tobe-temp` 아카이브 (README 30일 절차)
- [ ] 후속(별도 PR): Hook, `dev-chain-backend` 등 "IP 입력 확인" 안내, design 스킬 본문 확장

---

## 후속 PR 백로그 — (B) TO-BE 전체 구현

> **이 섹션의 목적**: tobe-temp 에 없어 1차 PR(A)에서 빠지는 TO-BE 강제 항목을 *누락 없이* 추적한다. 각 항목은 *별도 PR* 로 하나씩 진행한다. 완료 시 `[x]` 체크 + "완료 PR" 칸에 PR 번호를 적는다.
>
> 우선순위: **P1** = Spec 품질 직결(빠를수록 좋음) / **P2** = IP·검증 강화 / **P3** = 신규 영역·대형 개편.

### B-1. Spec 작성 4 팁 강제 — §4.7.1 (P1)

- [ ] `munto-spec-writer` 본문에 **TBD / N/A vs None / Will Not Do / 논의 기록(Decision Log)** 4 팁을 체크리스트로 박기 (AI 가 비결정 항목을 추측 대신 `TBD:` 로 명시 + 사람 질문)
- [ ] `munto-spec-review` · `spec-reviewer` 가 4 표기의 **부재(빈칸·`-`·"없음")** 를 결함으로 잡도록 보강
- [ ] `dbml-writer` · `swagger-writer` · `dbml-reviewer` 도 동일 규약 반영
- 완료 PR: ____

### B-2. Glossary(용어집) 의무화 — §4.7.2 (P1)

- [ ] `munto-spec-writer` 가 SRS 작성 시 본문의 *비표준 용어* 를 Glossary 부록에 자동 등록 (정의는 사람/AI 1차)
- [ ] `munto-spec-review` 가 **Glossary 누락 용어** 를 결함으로 잡기 (최소 5개 도출 유도)
- [ ] DBML 상단 주석 · Swagger `components/schemas` description 에도 용어 정의 위치 반영
- 완료 PR: ____

### B-3. 대안 검토 박스 의무화 — §4.7.3 (P1)

- [ ] `munto-spec-writer` 가 *핵심 아키텍처 결정* 발견 시 **대안 검토 박스**(고려한 대안 2+ / 채택·기각 사유 / 재검토 조건) 자동 생성
- [ ] `dbml-writer` · `swagger-writer` 가 *주요 엔티티·계약 패턴* 에 동일 박스 자동 첨부
- [ ] `munto-spec-review` · `dbml-reviewer` · `design-consistency-reviewer` 가 *핵심 결정에 박스 없으면 결함* 으로 잡기
- 완료 PR: ____

### B-4. ip-writer / ip-reviewer 서브에이전트 — IP §IP-8 / §4.7.4 (6) (P2)

> **주의**: 1차 PR(Phase 4)에서 이미 저작하기로 했다면 본 항목은 *완료 처리*. 1차 PR 에서 미뤘다면(스킬도 함께 2차 PR) 여기서 추적.

- [ ] `.agents/agents/ip-writer.md` (Spec 4종 → IP 8섹션 초안, `spec-baseline-handoff.md` 우선 참조)
- [ ] `.agents/agents/ip-reviewer.md` (`ip-standard.md` 7가지 질문 + 완료 체크리스트 자동 점검)
- [ ] `.claude/agents/` · (필요 시) `.codex/agents/` 어댑터
- 완료 PR: ____

### B-5. TO-BE 문서 경로 동기화 — ip-standard.md 위치 결정 반영 (P2)

- [x] `reports/2026-05-harness-TO-BE.md` §IP-1(861줄)의 `munto-dev-assistant/ip-standard.md`(루트) 표기를 **`munto-dev-assistant/document/ip-standard.md`** 로 수정 (2026-05-29 완료. 나머지 언급은 경로 없는 파일명·과거 이력이라 위치 비종속 → 유지)
- [ ] tobe-temp 측 잔여 표기(README·skills·proposal)도 동일 정리(아카이브 전 1회)
- 완료 PR: ____

### B-6. dev-chain-design 본문 보강 — IP 단계 연결 + 2-Track 재구성 (P3)

- [ ] `dev-chain-design-update-proposal.md` 의 **결정(선택지 A/B/C)** 을 팀이 확정
- [ ] 확정안에 따라 `dev-chain-design` 본문에 *IP 단계 연결* 반영 (선택지 B = 완료 보고 끝에 `dev-chain-implementation-plan` 안내)
- [ ] (해당 시) §3.4 **2-Track 병렬 + Unit TCL 후속** 구조를 `dev-chain-design` 본문에 반영 (DBML 확정 → Swagger, BE+FE 입회 리뷰)
- 완료 PR: ____

### B-7. PHASE 2 구현 스킬에 "IP 입력 확인" 안내 — §4.4 / IP (P2)

- [ ] `dev-chain-backend` · `dev-chain-mobile` · `dev-chain-frontend` 시작부에 *IP(`ImplementationPlan.md`) 존재·참조 확인* 안내 한 줄 추가
- 완료 PR: ____

### B-8. 변경 관리(CCB) 절차 — §4.8 (P3)

- [ ] CCB(규모별 가변 의사결정) · AI 1차 영향도 분석 템플릿 · 베이스라인 버저닝(v1.x / v2.0) 을 문서 또는 규칙으로 박기
- 완료 PR: ____

### B-9. `munto-doc-review-helper` 신규 스킬 — §5.1 (P3)

- [ ] 비표준 문서(분석 보고서·OnePager·외부 기획서) 핵심 파악·대화식 리뷰 보조 스킬 신설 (가칭 확정 포함)
- 완료 PR: ____

### B-10. Claude Code Hook 트랙 — §4.7.4 (5)(c) (P3, 개인 PC)

- [ ] `.claude-hooks-proposal.json` 기반 Stop Hook 적용(매 turn `spec-hook-turn-*.md` 캡처, `.gitignore`)
- [ ] `MUNTO_AUTHOR_ID` 환경변수 안내
- 완료 PR: ____

### B-11. 팀 멤버 식별자 인덱스 — §4.7.4 (4) (P3, 선택)

- [ ] `munto-dev-assistant/team/members.yml` 로 `{author-id}` 합의·오타 검출 인프라 (별도 트랙)
- 완료 PR: ____

### B-12. `munto-find-session` 디스커버리 도구 — §IP-9.7 (P3, 백로그)

- [ ] `~/.claude/projects/*` · `~/.cursor/projects/*` 스캔 → 세션 메타 검색·재개 스킬/스크립트
- 완료 PR: ____

---

## 변경 이력

| 일자 | 내용 |
| --- | --- |
| 2026-05-29 | 신규 작성 — TO-BE 운영 적용 단계별 계획(Phase 0~7) + 체크박스 |
| 2026-05-29 | 적용 범위 (A)이관/(B)전체 구분 박스 추가 · `ip-standard.md` 위치 `document/` 결정 명시(TO-BE 경로 수정 필요 표시) · **후속 PR 백로그(B-1~B-12)** 섹션 신설 |
