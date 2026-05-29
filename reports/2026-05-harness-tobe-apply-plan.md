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
| **(A) 1차 PR — 이관** | tobe-temp 에 *파일로 존재하는 것* 을 운영 경로로 옮기고 경로만 수정 | **Phase 0~6** (아래) |
| **(A+) 1차 PR — 실전 적용 보강** | 본인이 *이번 PR로 실제 개발에 적용*하므로, (B) 중 *체인 작동에 꼭 필요한 항목*을 1차 PR로 승격 + 기존 문서 정합화 | **Phase 7~8** (아래) |
| **(B) 후속 — TO-BE 전체 구현** | tobe-temp 에도 없어 *새로 저작* 해야 하는 나머지 TO-BE 강제 항목 | **§ 후속 PR 백로그** (하단) |
| **(C) 개발자 가이드(교과서)** | TO-BE 의 개발자 가이드 본문을 운영 레포 교과서로 신설 | **Phase 9** ✅ 완료 (`document/dev-process-guide.md`) |

> **원칙**: (B) 는 *한꺼번에 만들지 않는다* (TO-BE §2.3 ② "필요한 시점에 작게 추가"). 다만 본인이 *이번 PR로 실제 개발에 적용*하므로, (B) 중 *체인이 실제로 작동하려면 꼭 필요한 최소 항목*(IP 입력 확인 등)은 Phase 7로 승격한다. 나머지 (B) 는 백로그에 *누락 없이* 적어 두고 하나씩 별도 PR 로 진행한다.
> **실행 순서**: Phase 0~6(이관) → **Phase 7(실전 보강) ✅** → **Phase 8(문서 정합화) ✅** → **Phase 9(개발자 가이드) ✅** → **Phase 10(push & PR)**.

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

- `.claude-hooks-proposal.json` **실제 활성화** → 개인 PC 로컬 (견본·가이드·`.gitignore`는 Phase 6에서 포함, 백로그 B-5)
- 백로그 B-4/B-6/B-7 → 별도 PR. ※ **B-2(2-Track 재구성)·B-3(CCB 변경관리 문서화+`munto-spec-change` 스킬)는 본 PR로 완료** (백로그 참조)

> 개발자 가이드(교과서)는 **본 PR 포함**(Phase 9)으로 변경됨 — 집필 착수 전 목차·범위만 사용자와 확정.

---

## Phase 0 — 준비 (로컬, 커밋 없음)

- [x] `main` 최신화 (`git fetch origin` → `git checkout main` → `git pull origin main`)
- [x] feature 브랜치 생성 (`git checkout -b feat/agentic-dev-chain-tobe`)
- [x] 이관 소스 위치 확인: `munto-dev-assistant-report/munto-dev-assistant-tobe-temp/` (2026-05-29 확인 — 14개 파일)
- [x] tobe-temp SKILL 상단 `<!-- ... -->` 기획 주석 제거 방침 확인 (skills/README §3 — 제거 맞음)

> **확인 결과 — Phase 3에서 처리할 것**:
> - `munto-spec-writer` · `munto-spec-review`: 상단 `<!-- -->` 블록(1~10줄) 제거 + **프론트매터 정규화 필요**. 주석만 지우면 프론트매터가 한 줄로 뭉친 무효 형태로 남음 → 운영 형식(여러 줄 YAML, `name`/`description`만)으로 복원. `metadata`/`revision` 포함 여부는 결정 필요(기존 운영 본문엔 없음).
> - `dev-chain-implementation-plan`: `<!-- -->` 주석은 없으나 `status: "PROPOSAL …"` 프론트매터 필드 제거 + `revision`의 "검토안 선택지 B 전제" 문구 정리.

```bash
cd /Users/gracegyu/Documents/GitMunto/munto-dev-assistant
git fetch origin
git checkout main && git pull origin main
git checkout -b feat/agentic-dev-chain-tobe
```

---

## Phase 1 — 표준 문서 (`document/`)

**커밋 예시:** `docs: IP·Spec 표준 및 작성 가이드 추가`

- [x] `ip-standard.md` → `document/ip-standard.md` **(위치 결정: `document/`)** (2026-05-29)
- [x] `spec-standard.md` → `document/spec-standard.md` (**덮어쓰기** — 540줄 → 2065줄, PR 설명에 강조) (2026-05-29)
- [x] `spec-philosophy.md` → `document/spec-philosophy.md` (2026-05-29)
- [x] `spec-writing-tips.md` → `document/spec-writing-tips.md` (2026-05-29)
- [x] `munto-spec-*` 스킬이 참조하는 `document/spec-standard.md` 경로가 유효한지 확인 (spec-writer·spec-review 모두 유효)
- [x] `ip-standard.md` 내부 상대링크를 `document/` 기준으로 수정 — 11번 `../.agents/skills/common/docs/dev-chain-implementation-plan/SKILL.md`, 553번 `../projects/...` 3개 (2026-05-29)

> **결정 — `ip-standard.md` 는 `document/` 에 둔다.** TO-BE §IP-1 등은 단일 진실 공급원을 **`munto-dev-assistant/ip-standard.md`(레포 루트)** 로 표기하므로, 이 결정에 맞춰 **TO-BE 문서·tobe-temp IP 스킬·projects 템플릿의 경로 표기를 모두 `document/ip-standard.md` 로 수정**해야 한다.
> - TO-BE 문서 수정은 (B) 백로그 항목으로 추적 (하단 § 후속 PR 백로그).
> - 1차 PR 안에서 고쳐야 할 경로(IP 스킬 내부 참조·projects 템플릿)는 Phase 2·Phase 3-② 의 "경로 수정" 체크 항목에 포함.

---

## Phase 2 — `projects/` 견본·인덱스 (신규 폴더)

**커밋 예시:** `feat: projects 템플릿 및 활성 프로젝트 인덱스 추가`

- [x] `projects/README.md` → `projects/README.md` (2026-05-29)
- [x] `projects/_template/ImplementationPlan.md` → `projects/_template/ImplementationPlan.md` (2026-05-29)
- [x] `projects/_template/README.md` → `projects/_template/README.md` (2026-05-29)
- [x] 내부 상대 경로를 운영 레포 기준으로 수정 — `../skills/...`·`../../skills/...` → `.agents/skills/common/docs/...`, `ip-standard.md`·`spec-standard.md` 참조 → `document/...` (총 9곳: README 4 / _template README 3 / ImplementationPlan 2)
- [x] 비운영(`-report/`·"적용 대기") 본문 참조를 운영 기준으로 재작성 — `_template/README.md` 60·62번, `document/ip-standard.md` 188·189번 (스킬은 `.agents/...`, Hook은 별도 PR 트랙 명시). 변경이력(changelog) 행은 historical로 유지

---

## Phase 3 — 스킬 본문 (`.agents/`)

**커밋 예시 ①:** `feat(skills): spec-writer·spec-review TO-BE 세션·baseline 반영`

- [x] `skills/munto-spec-writer/SKILL.md` → `.agents/skills/common/docs/munto-spec-writer/SKILL.md` (2026-05-29)
- [x] `skills/munto-spec-review/SKILL.md` → `.agents/skills/common/docs/munto-spec-review/SKILL.md` (2026-05-29)
- [x] 위 2개: 상단 `<!-- -->` 기획 주석 제거 + **프론트매터를 운영 형식(여러 줄 YAML, `name`/`description`)으로 복원** 완료 (metadata/revision은 기존 운영 컨벤션대로 미포함)

**커밋 예시 ②:** `feat(skills): dev-chain-implementation-plan 신규`

- [x] `skills/dev-chain-implementation-plan/SKILL.md` → `.agents/skills/common/docs/dev-chain-implementation-plan/SKILL.md` (2026-05-29)
- [x] 스킬 내부 `ip-standard.md`·`dev-chain-design-update-proposal.md` 참조를 운영 기준(`document/...`, 루트 상대)으로 수정 (26·40·210번)
- [x] 프론트매터 `metadata`/`status: "PROPOSAL …"` 제거 → `name`/`description`만 유지
- [x] `dev-chain-design` Step 5 `### 다음 단계`에 IP 단계(`dev-chain-implementation-plan`)를 개발 스킬 *앞에* 추가 — Phase 3/4에서 IP를 별도 스킬+서브에이전트로 만든 것 자체가 선택지 B 채택이므로 본 PR에서 체인 연결 완료 (B-2의 본문 대개편과 분리)

> **위치 결정**: tobe README는 `backend/docs` 후보도 제시하나, `dev-chain-design`·`dev-chain-wbs`와 일관되게 **`common/docs`** 권장.

---

## Phase 4 — 서브에이전트 

`dev-chain-implementation-plan` 이 `Task(subagent_type=ip-writer)` 를 호출하므로, 없으면 스킬이 반쪽이 된다.

- [x] `spec-reviewer.md`/`swagger-writer.md` 패턴 기반 → `.agents/agents/ip-writer.md` 작성 (writer, Read/Write/Glob/Grep)
- [x] `.agents/agents/ip-reviewer.md` 작성 (생성-검증 페어, read-only Read/Grep, IP-8 7가지 질문 점검)
- [x] `.claude/agents/ip-writer.md` / `ip-reviewer.md` 래퍼 생성
- [x] `.codex/agents/ip-writer.md`(worker) / `ip-reviewer.md`(explorer) 어댑터 생성

**커밋 예시:** `feat(agents): ip-writer·ip-reviewer 서브에이전트 추가`

> proposal은 "별도 PR"도 허용. 1차 PR 완성도를 위해 같은 PR 포함 권장. 분리한다면 Phase 3-② 스킬도 함께 2차 PR로 미룬다.

---

## Phase 5 — 어댑터·목록

**커밋 예시:** `chore: Claude·Codex 스킬 어댑터 및 AGENTS.md 갱신`

- [x] `.claude/skills/dev-chain-implementation-plan/SKILL.md` 얇은 래퍼 생성
- [x] `.codex/skills/dev-chain-implementation-plan/SKILL.md` (`source:` + `codex_type: skill` 선언) 생성
- [x] `AGENTS.md` 활성 스킬 목록 + Development Chain 다이어그램(1-1 단계)에 `dev-chain-implementation-plan` 추가
- [x] (선택) `munto-skills` SKILL 목록 common/docs 표에 IP 행 추가 (※ design/verify/wbs는 기존부터 미등재 — 본 PR 범위 밖이라 유지)
- [x] `bash scripts/check-adapters.sh` 실행 → 137개 참조 검증, 깨진 링크 0건

```bash
bash scripts/check-adapters.sh
```

---

## Phase 6 — 검토안 이관 & Hook 견본 보존

**커밋 예시:** `docs: dev-chain-design 검토안 이관 + Claude Hook 견본 보존`

- [x] `dev-chain-design-update-proposal.md` → `document/dev-chain-design-update-proposal.md` 이관 (**필수**: ip-standard.md·IP 스킬이 이 경로를 참조 → 미이관 시 깨진 링크). 깨진 상대경로 운영 기준 수정 + "제안만/별도 PR" 문구를 구현 완료 상태로 갱신 + 결정 1~3 해소 표기
- [x] `.claude-hooks-proposal.json` 처리 — **B+ 채택**: 견본을 레포 루트에 커밋용으로 이관(참고 템플릿, 자동 로드 안 됨) + 잘못된 적용 위치(`hooks.json`→실제 `settings.json`) 운영 기준 수정 + 루트 `.gitignore`에 출력물(`projects/**/sessions/spec-hook-turn-*.md`) 등록 + `_template/README.md` (c) 트랙 가이드 정정. 실제 활성화는 개발자별 로컬 `~/.claude/settings.json`(백로그 B-5)
  - 근거: Claude Code는 standalone `.claude/hooks.json` 미로드(플러그인 전용), `.claude/settings.json`은 본 레포 `.gitignore`가 무시(팀 정책) → 공유 커밋형 활성화는 정책 변경 전까지 불가

---

## Phase 7 — 개발 체인 실전 적용 보강 (백로그 승격) [본 PR]

> 본인이 *이번 PR로 실제 개발에 적용*하므로, 백로그(B) 중 **체인이 실제로 작동하려면 꼭 필요한 항목**을 1차 PR로 승격한다.

**커밋 예시:** `feat: 개발 체인 실전 적용 보강 (IP 입력 확인 + Spec 품질 강제)`

### Task 7-1 (필수, TO-BE §4.4) — PHASE 2 구현 스킬에 "IP 입력 확인" 연결 ✅ 완료

- [x] `dev-chain-backend` · `dev-chain-mobile` · `dev-chain-frontend` 시작부에 *IP(`projects/{프로젝트}/ImplementationPlan.md`) 존재·참조 확인* 안내(`## 권장 입력 — IP(구현계획서) 확인` 섹션) 추가 + PM 역할표·`입력 확인`에 IP 행 추가 (2026-05-29)
- [x] IP 없을 때 안내: "IP가 없습니다. `dev-chain-implementation-plan`을 먼저 호출할까요? (강제 아님 — 작은 변경은 IP 없이 진행 가능)" (TO-BE §4.4) — 3개 스킬 모두 명시
- [x] 위임 호출 패턴 prompt에 `(선택) ip=<경로>` 추가 + `backend/mobile/frontend-expert` 입력부에 IP 소비 정의 추가 → *체인이 실제로 IP를 입력으로 소비*하도록 연결
- [x] `bash scripts/check-adapters.sh` 통과(137개, 깨진 링크 0)

> **왜 필수인가**: Phase 3~5에서 만든 `dev-chain-design → dev-chain-implementation-plan → 개발` 체인을, *PHASE 2 스킬이 실제로 IP를 입력으로 소비*하게 만드는 마지막 연결 고리. 이게 없으면 IP를 만들어도 개발 스킬이 무시 → 체인이 끊긴 채 적용된다.

### Task 7-2 (권장, TO-BE §4.7.1) — Spec 작성 4팁(작성 지침) + 리뷰 TBD 검출 ✅ 완료

> **레이어 분리(중요)**: 4팁은 *작성 시점*엔 모두 유용하지만, *리뷰 검출*은 TBD만 기계적으로 가능하다. 비목표·Decision Log의 *부재*는 리뷰어가 알 수 없으므로 작성자 가이드로만 유도한다.

- [x] **(작성)** `munto-spec-writer` 가 `document/spec-writing-tips.md` §4.1~4.4 4팁을 *작성 지침*으로 로드·적용: ① 미결정은 빈칸 대신 `TBD: 사유+담당+기한` ② N/A(적용 자체가 불가, 예: v1.0의 하위호환성) vs None(적용 대상이나 이번엔 없음·안 함) 구분 ③ Will Not Do(비목표) 명시 ④ Decision Log — A안·B안 의논 시 과정·채택/기각 사유 기록 — `### 비결정·미정 항목 4팁` 섹션 신설 + 시작 전 준비에 tips 로드 추가 (2026-05-29)
- [x] **(리뷰)** `munto-spec-review`·`spec-reviewer` 는 *검출 가능한 것만*: TBD 잔존·회피문구("추후 결정" 등) → 결함(하드), 빈칸·`-`·"없음" → 권고(소프트). **비목표·Decision Log 부재는 자동 검출 대상 아님** — `H. TBD 및 미정 표기 처리`로 보강 + `spec-reviewer` 자체검증에 부재 오검출 방지 가드 추가 (2026-05-29)
- [x] `bash scripts/check-adapters.sh` 통과(137개, 깨진 링크 0)

### Task 7-3 (권장, TO-BE §4.7.2) — 용어·약어 정의 의무화 (SRS §1.4 Terms and Abbreviations)

- [x] `munto-spec-writer` 가 SRS 작성 시 *비표준 용어 중 등록 판정 통과분* 을 **§1.4 Terms and Abbreviations** 에 자동 등록 (별도 §10 Glossary 부록 신설 X) — SRS 핵심 규칙·자체검증 체크리스트 + 신규 `### 용어·약어(§1.4) 등록` 절 추가 (등록 판정은 `spec-standard.md §"용어·약어(1.4) 작성 원칙"` 5질문 참조) (2026-05-29)
- [x] `munto-spec-review` 가 **§1.4 누락 용어** 를 검출 — `B. 기호·수식·용어 선행 정의(§1.4)` 로 확장, 누락 의심 용어 🟡(소프트, 모두 아는 용어·사내 용어집 링크 제외) (2026-05-29)
- [x] One Pager 템플릿에 *Terms and Abbreviations* 항목 신설 → writer/review 스킬의 OnePager 고정 항목 **8개→9개** 동기화 (구조·작성규칙·출력형식·자체검증 모두 반영) (2026-05-29)
- [x] `bash scripts/check-adapters.sh` 통과(137개)

### Task 7-4 (권장, TO-BE §4.7.3) — 대안 검토 박스 의무화 ✅ 완료

- [x] `munto-spec-writer`(§2.2 핵심 아키텍처 결정) · `dbml-writer`(핵심 엔티티 구조 결정) · `swagger-writer`(핵심 계약 패턴 결정) 가 **대안 검토 박스**(고려한 대안 2+ / 채택·기각 사유 / 재검토 조건) 자동 생성 — **선별 원칙 명시**
- [x] `munto-spec-review`(§J) · `dbml-reviewer`(S5) 가 *핵심 결정으로 보이는데 대안 흔적 없으면* 🟡 질문으로 보강 요청 (소프트) — `spec-reviewer` 자체검증에 *부재 자동결함 단정 금지* 가드 추가
- [x] **선별 적용**: 모든 결정 X, 핵심 아키텍처만. 버그수정·소규모·기존 표준 답습 면제, **박스 0개도 정상**. 억지 대안 강요 금지
- [x] **설계 결정**: `design-consistency-reviewer`는 *산출물 간 정합성 전용*이라 단일 산출물 결정-근거 검출은 범위 밖 → 제외 (TO-BE §4.7.3 강제 문구도 동기화)
- 변경: `munto-spec-writer/SKILL.md`(대안 박스 작성 지침 §) · `munto-spec-review/SKILL.md`(§J + A~J 갱신) · `dbml-writer.md` · `swagger-writer.md` · `dbml-reviewer.md`(S5) · `spec-reviewer.md`(A~J + 가드) · TO-BE §4.7.3(선별 원칙·강제 문구)

### Task 7-5 (필수, TO-BE §4.9 / 가이드 ch.3) — IP 번호 기반 구현 지시(디스패치) 가이드 ✅ 완료

> 사용자가 `"Task 1.2 구현"`, `"Phase 1 구현"`, `"Phase 1-3 구현"`, `"IP 기준으로 구현"` 처럼 *IP 번호로* 지시하는 경로가 가이드·스킬 어디에도 없었다. 이를 **PHASE 2 오케스트레이션의 유인(수동) 디스패치**로 정의해 메인이 IP를 읽어 책임 도메인·DAG 순서로 분배하도록 박았다.

- [x] `document/dev-process-guide.md` ch.3 PHASE 2에 **「IP 기준 구현 지시(디스패치)」** 서브섹션 추가 — Task/Phase/범위별 매핑 표 + DAG 위상 순서 + 도메인 책임 원칙 + IP 부재 안내
- [x] ch.8 치트시트에 IP 번호 지시 행 추가
- [x] `dev-chain-backend·mobile·frontend` 3개 스킬 IP 섹션에 **「IP Task/Phase 번호로 호출된 경우(디스패치)」** 4단계 처리 추가 (IP 조회 → 대상 Task 선별[자기 도메인만, 타 도메인은 안내] → DAG 위상 순서 → expert 위임). 다중 도메인·다중 Phase는 메인 오케스트레이션 위임 명시
- [x] `AGENTS.md` 에이전트 행동 원칙 6번 **「IP 번호 지시 = 메인이 디스패치」** 신설 (라우팅 발견성 확보)
- [x] `bash scripts/check-adapters.sh` 통과(139개)

> **왜 필수인가**: 7-1이 *IP를 입력으로 소비*하게 만든 연결이라면, 7-5는 *IP의 Task/Phase 번호로 직접 지시*하는 진입점을 연다. 이게 없으면 사용자는 매번 도메인명으로만 호출해야 하고 IP의 DAG·Task 단위 실행이 사람 머릿속에만 남는다. (전체 자동 순회 무인 모드는 TO-BE §4.9, 본 PR은 유인 디스패치까지)

> **범위 판단**: 7-1·7-5는 *체인 작동 필수*. 7-2~7-4는 *Spec 품질 직결(P1)* 이라 실전 적용 시 처음부터 높이는 게 유리해 권장 포함. 작업량이 크면 7-2~7-4만 분리 PR 가능 — **실행 시 사용자와 의논**.

---

## Phase 8 — 기존 문서 정합화 [본 PR · 마지막 작업] ✅ 완료

> 새 구조(dev-chain 스킬군, IP, `projects/`, `document/` 표준, 서브에이전트, `.codex/` 어댑터)와 기존 안내 문서가 어긋나 있다. **모든 변경을 마친 뒤** 문서를 새 구조에 맞춘다.

**커밋 예시:** `docs: README·AGENTS 등 기존 문서를 신규 구조에 맞게 갱신`

### Task 8-1 — `README.md` 전면 갱신 ✅ 완료

- [x] 구조 개요 도식에 `.codex/`, `document/`, `projects/`, `.agents/agents/`(서브에이전트), `scripts/` 추가
- [x] common/docs 스킬표에 `dev-chain-wbs`·`dev-chain-design`·`dev-chain-implementation-plan`·`dev-chain-verify`·`munto-humanize` 추가 + ops에 `munto-create-pr`·`munto-read-db`·`qa-tcl-writer` 추가
- [x] backend/mobile/frontend `dev-chain-*` 개발 스킬군 + `muntorial-mobile` 추가
- [x] 잘못 분류된 "### frontend" 헤더의 `spec-writing`(규칙) 정정 → `dev-chain-frontend`는 스킬, 규칙은 `nextjs`만으로 통합 규칙표 재구성
- [x] **Development Chain 프로세스 섹션 신설** (AGENTS.md와 동기화 — 5 PHASE + IP 단계)
- [x] `document/` 표준 문서(`ip-standard`·`spec-standard`·`spec-philosophy`·`spec-writing-tips`·`spec-templates`) + `projects/` 안내 추가
- [x] (추가) 어댑터 예시 경로를 `SKILL.md` 폴더 컨벤션으로 정정 · "시작하기 #2"의 옛 슬래시 커맨드 예시를 자연어 스킬 호출로 정정 · 기여 가이드 스킬 추가 예시 갱신 · spec-review 체크리스트 A~I→A~J

### Task 8-2 — `AGENTS.md` 최종 점검 ✅ 완료

- [x] **서브에이전트 목록 섹션 신설** (13종: 설계 5 / 구현 3 / 문서·계획 3[`ip-writer`·`ip-reviewer` 포함] / 분석 2)
- [x] 디렉토리 구조에 `projects/` 추가 · common/ops 스킬에 `qa-tcl-writer` · common/docs에 `munto-humanize` 추가
- [x] frontend 스킬 섹션 신설(`dev-chain-frontend` 규칙→스킬 정정) · common/ops 규칙에 `jira` 추가
- [x] **표준 문서(`document/`) 섹션 신설** (ip/spec 표준 + `projects/README.md`)

### Task 8-3 — 기타 문서 상호참조 점검 ✅ 완료

- [x] `document/` 표준 문서·`projects/README.md` 링크 정합성 확인 (이미 최신 — 변경 불요)
- [x] **`munto-skills` 목록 백필** — stale `*-acli`(NEW)/`Deprecated: MCP` 항목 제거, 실제 폴더 기준 재작성 + design/verify/wbs/humanize/qa-tcl-writer/create-pr/read-db/dev-chain-backend·frontend·mobile/muntorial 등 누락분 전부 추가 + 서브에이전트 안내 추가
- [x] `.claude/agents/spec-reviewer.md` 래퍼의 A~I→A~J 동기화 (Codex 래퍼는 source 참조형이라 불요)
- [x] check-adapters 137개 참조 통과

---

## Phase 9 — 개발자 프로세스 가이드(교과서) 신설 [본 PR] ✅ 완료

> **현황(조사 결과)**: 운영 레포에 *개발자가 프로세스를 교과서처럼 배우는 가이드는 없다*. `AGENTS.md`=에이전트/하네스용, `README.md`=레포 구조 설명, `document/`=표준(ip/spec)뿐. **TO-BE(§1~4, §6)가 사실상 개발자 가이드 본문**이나 `-report` 레포에만 존재 → 운영 레포로 가져와 교과서화 필요.
> **목표 독자**: 사람 개발자(에이전트 아님). *언제·어떤 PHASE에서·어떤 지시를 주는지* 를 순서대로 익히는 문서.
> **실행 원칙**: **본 PR 포함.** 단 집필 착수 전 Task 9-1·9-2(현황·위치·목차)를 **사용자와 확정**한 뒤 집필한다.

**위치 확정:** `document/dev-process-guide.md` (단일 파일). 사유: 8장 규모는 처음부터 끝까지 읽는 교과서형 → 단일 파일이 Ctrl+F·진입 링크·mermaid 렌더에 유리. ~800줄 초과 또는 챕터별 오너 분화 시 `document/guide/`로 분할.

### Task 9-1 — 현황·격차 확정 + 위치/형식 결정 [사용자 확정] ✅ 완료

- [x] 기존 가이드 부재 결론 확정 + 위치 = **단일 파일 `document/dev-process-guide.md`**
- [x] TO-BE(`-report`/Notion) ↔ 운영 가이드 관계 정의 — **positioning: self-contained**. 가이드는 핵심 규범까지 본문에 담아 단독으로 읽히고, *깊은 근거*만 `TO-BE §X`로 링크. 규범 정본은 TO-BE/AGENTS/`document/` 표준 유지(드리프트 시 정본 우선)

### Task 9-2 — 목차 설계 (TO-BE 챕터 매핑) [사용자 확정] ✅ 완료 (8장 확정·집필됨)

- [x] 1) 큰 그림 — Agentic Dev Chain이란 / 5 PHASE + **마스터 mermaid `flowchart`** + 범례 (TO-BE §1, §3.0, §3.1)
- [x] 2) 핵심 원칙 8개 (TO-BE §2.3)
- [x] 3) **PHASE별 사용법** (TO-BE §3.2~3.6, §4.1~4.5) ← 교과서 핵심. PHASE 0/1/CCB/루프 **mermaid 서브다이어그램** 포함
- [x] 4) 사람 개입 체크리스트 (TO-BE §4.6 + 분석 아키텍트)
- [x] 5) AI에게 지시하는 법 — 가이드 4종·Review·4팁·§1.4 용어·대안 박스 (TO-BE §4.7)
- [x] 6) 베이스라인·인수·변경관리 — CCB mermaid (TO-BE §2.2, §4.8)
- [x] 7) 무인/유인 모드 — 오케스트레이션 루프 mermaid (TO-BE §4.9)
- [x] 8) 빠른 참조 — 스킬·서브에이전트·표준문서 치트시트

### Task 9-3 — 챕터별 집필 ✅ 완료

- [x] `document/dev-process-guide.md` 단일 파일로 8장 집필 (self-contained, 깊은 근거만 TO-BE §X 링크). 깨진 참조·경로는 운영 레포 기준 정합
- [x] **mermaid 4종 작성** — 마스터 흐름(ch.1) + PHASE 0·PHASE 1 서브(ch.3) + CCB(ch.6) + 무인 루프(ch.7)

### Task 9-4 — 진입 링크 연결 ✅ 완료

- [x] `AGENTS.md`(Development Chain 섹션 상단 + 표준 문서 목록)·`README.md`(Development Chain 섹션 + 표준 문서 표)에 가이드 진입 링크 추가. check-adapters 137개 통과

---

## Phase 10 — push & PR [본 PR 마지막]

- [ ] `git push -u origin feat/agentic-dev-chain-tobe`
- [ ] `gh pr create` (또는 GitHub UI)로 PR 생성

```bash
git push -u origin feat/agentic-dev-chain-tobe
gh pr create --title "feat: Agentic Dev Chain TO-BE 하네스 적용" --body "..."
```

### PR 본문 체크

- [ ] Notion TO-BE / brief 링크 첨부
- [ ] 변경 요약 (표준 / projects / 스킬 / 서브에이전트 / IP 입력 확인 + 번호 디스패치 / dev-chain-design 2-Track / munto-spec-change / 개발자 가이드 / 문서 정합화)
- [ ] `bash scripts/check-adapters.sh` 통과 명시
- [ ] 리뷰어 체크 포인트: `{author-id}` 1회 질문 / `MUNTO_AUTHOR_ID`(Hook 별도) / `spec-baseline-handoff` BLOCKER
- [ ] 변경 요약에 **개발자 프로세스 가이드(Phase 9)** 포함
- [ ] 의도적 제외 명시: Hook 실제 활성화(견본만 포함), 무인 자동 순회(B-5/§4.9 — 본 PR은 유인 디스패치까지), 백로그 B-4/B-6/B-7

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
| 7 | `docs: design-update-proposal 이관 + Hook 견본 보존` | Phase 6 |
| 8 | `feat: dev 스킬 IP 입력 확인·번호 디스패치 + Spec 품질 강제` | Phase 7 (7-2~7-4는 분리 가능, 7-5 디스패치 포함) |
| 9 | `docs: README·AGENTS 신규 구조 갱신` | Phase 8 |
| 10 | `docs: 개발자 프로세스 가이드(교과서) 신설` | Phase 9 |

> 스쿼시는 머지 시 GitHub에서 수행 가능. 리뷰 중에는 분리 커밋 유지가 낫다.

---

## PR 이후 (운영)

- [ ] 리뷰·CI·`check-adapters.sh` 통과 → merge
- [ ] 팀에 brief / Notion 안내
- [ ] `munto-dev-assistant-tobe-temp` **삭제(폐기)** — 모든 콘텐츠가 운영 레포로 이관 완료된 임시 스테이징이므로 머지 후 폐기 (이관 누락 0건 최종 확인 후)
- [ ] 후속(별도 PR): Hook 로컬 활성화(B-5), 나머지 백로그(B-4/6/7). ※ B-2(2-Track 재구성)·B-3(CCB 문서화)는 **본 PR로 완료**

---

## 후속 PR 백로그 — (B) TO-BE 전체 구현

> **이 섹션의 목적**: tobe-temp 에 없어 1차 PR(A)에서 빠지는 TO-BE 강제 항목을 *누락 없이* 추적한다. 각 항목은 *별도 PR* 로 하나씩 진행한다. 완료 시 `[x]` 체크 + "완료 PR" 칸에 PR 번호를 적는다.
>
> 우선순위: **P1** = Spec 품질 직결(빠를수록 좋음) / **P2** = IP·검증 강화 / **P3** = 신규 영역·대형 개편.
>
> **본 PR로 승격/완료되어 정리된 항목**: Spec 작성 4팁·용어·약어 정의(§1.4)·대안 검토 박스 → **Phase 7-2~7-4**, IP 입력 확인 → **Phase 7-1**(승격). ip-writer/ip-reviewer는 **Phase 4**, Hook 견본·`.gitignore` 등록은 **Phase 6**에 이미 기록되어 백로그 중복분 제거. 남은 항목을 아래 **B-1~B-7**로 순차 재번호함. **추가 편입(2026-05-29)**: B-2(dev-chain-design 2-Track 재구성)·B-3(CCB 변경관리 문서화)도 본 PR로 완료 — 가이드 ch.3/ch.6와의 정합을 위해 함께 처리. **남은 순수 후속 PR = B-4·B-5·B-6·B-7.**

### B-1. TO-BE 문서 경로 동기화 — ip-standard.md 위치 결정 반영 (P2) ✅ 완료

- [x] `reports/2026-05-harness-TO-BE.md` §IP-1(861줄)의 `munto-dev-assistant/ip-standard.md`(루트) 표기를 **`munto-dev-assistant/document/ip-standard.md`** 로 수정 (2026-05-29 완료. 나머지 언급은 경로 없는 파일명·과거 이력이라 위치 비종속 → 유지)
- ~~tobe-temp 측 잔여 표기 정리~~ → **불요**: tobe-temp 는 머지 후 **삭제(폐기)** 예정이라 내부 경로 정리 가치 없음 (`PR 이후` 참조)
- 완료 PR: (본 PR)

### B-2. dev-chain-design 본문 보강 — 2-Track 재구성 (P3) ✅ 완료

> IP 단계 연결(선택지 B의 "최소 변경" = Step 5 다음 단계 안내)은 **본 PR에서 완료**됐다(Phase 3 항목 참조). 남은 본문 대개편도 **본 PR에서 완료**.

- [x] `dev-chain-design-update-proposal.md` 의 **결정(선택지 A/B/C)** — *B 채택* 상태로 본 PR에서 본문 반영(추인). (의사결정 기록 문서는 보존)
- [x] §3.4 **2-Track 병렬 + Unit TCL 후속** 구조를 `dev-chain-design` 본문에 반영 — 기존 "3종 동시 팬아웃" 폐기. Track 1(DBML 확정→Swagger, 순차) / Track 2(UI, 사람 주도) / Track 3(Unit TCL, 두 트랙 후속) + 트랙별 👤 사람 리뷰 게이트(D3·S3·U2·T5) + 종합 Peer Review 게이트(베이스라인 v1.0)로 재작성. Swagger 사람 리뷰에 **BE 생산자 + FE/App 소비자 입회** 명시.
- [x] **필수 부수 변경**: `design-consistency-reviewer` 에 *모드 A(DBML↔Swagger 부분 정합성, TCL 미작성 단계)* 추가 — 기존 "3종 필수, 누락 시 거부"가 1A-5 단계(TCL 전)를 막았기 때문. Claude/Codex 어댑터의 거부 문구도 동기화.
- 완료 PR: (본 PR)

### B-3. 변경 관리(CCB) 절차 — §4.8 (P3) ✅ 문서화 + 운영 스킬 (본 PR)

- [x] CCB(규모별 가변 의사결정) · AI 1차 영향도 분석 · 베이스라인 버저닝(v1.x / v2.0) 을 **`document/dev-process-guide.md` ch.6**에 self-contained 문서화 (CCB 흐름도 Mermaid + 규모별 구성 + 버저닝 규칙 + Decision Log).
- [x] **운영 스킬 신설 `munto-spec-change`** (common/docs, self-contained) — 베이스라인 이후 Spec/요구사항 변경의 *영향 평가*를 운영. 변경 5대 원칙(신속함>완벽함·설득 도구·기록 보존 등) + 절차(CCB 미강제) + 영향 체크리스트(비즈니스·기술) + 변경 요청서 템플릿 + AI 1차 영향도 보고서 템플릿 + 버저닝. **CCB 미강제, 영향 평가 의무.** Claude/Codex 어댑터 + AGENTS/README/munto-skills 등록 + TO-BE §4.8·가이드 ch.6·ch.8 치트시트 링크.
- [ ] (선택·후속) CCB *의사결정 강제*·별도 규칙화가 필요하면 별도 PR. 현재는 영향 평가 의무 + 결정은 사람(분석 아키텍트/리드) 권한으로 운영.
- 완료 PR: (본 PR — 가이드 ch.6 + `munto-spec-change` 스킬)

### B-4. `munto-doc-review-helper` 신규 스킬 — §5.1 (P3)

- [ ] 비표준 문서(분석 보고서·OnePager·외부 기획서) 핵심 파악·대화식 리뷰 보조 스킬 신설 (가칭 확정 포함)
- 완료 PR: ____

### B-5. Claude Code Hook 트랙 — §4.7.4 (5)(c) (P3, 개인 PC)

> 견본 커밋 + 출력물 `.gitignore` + 적용 가이드는 **본 PR에서 완료**(Phase 6 기록). 남은 것은 *개발자별 로컬 실제 활성화*뿐.

- [ ] (개발자별) 견본 `hooks` 객체를 `~/.claude/settings.json` 또는 `.claude/settings.local.json`에 병합 + `MUNTO_AUTHOR_ID` 환경변수 설정 (로컬 작업, PR 아님)
- [ ] (팀 결정 시) `.gitignore`의 `.claude/settings.json` 무시 해제 → 공유 커밋형 활성화 여부
- 완료 PR: ____ (견본·가이드는 Phase 6에서 완료)

### B-6. 팀 멤버 식별자 인덱스 — §4.7.4 (4) (P3, 선택)

- [ ] `munto-dev-assistant/team/members.yml` 로 `{author-id}` 합의·오타 검출 인프라 (별도 트랙)
- 완료 PR: ____

### B-7. `munto-find-session` 디스커버리 도구 — §IP-9.7 (P3, 백로그)

- [ ] `~/.claude/projects/*` · `~/.cursor/projects/*` 스캔 → 세션 메타 검색·재개 스킬/스크립트
- 완료 PR: ____

---

## 변경 이력

| 일자 | 내용 |
| --- | --- |
| 2026-05-29 | 신규 작성 — TO-BE 운영 적용 단계별 계획(Phase 0~7) + 체크박스 |
| 2026-05-29 | 적용 범위 (A)이관/(B)전체 구분 박스 추가 · `ip-standard.md` 위치 `document/` 결정 명시(TO-BE 경로 수정 필요 표시) · **후속 PR 백로그(B-1~B-12)** 섹션 신설 |
| 2026-05-29 | Phase 4 완료(`ip-writer`·`ip-reviewer` + Claude/Codex 어댑터) → **B-4 완료 처리** · `dev-chain-design` Step 5에 IP 단계 연결(선택지 B 최소 변경)을 본 PR에서 처리 → **B-6을 2-Track 재구성만 남기도록 축소** |
| 2026-05-29 | Phase 5 완료(IP 스킬 Claude/Codex 어댑터 + AGENTS.md + munto-skills, check-adapters 통과) · Phase 6 완료(`dev-chain-design-update-proposal.md`→`document/` 이관[필수: 참조 깨짐 방지] · Hook 견본 B+ 처리: 커밋용 견본+출력물 .gitignore+가이드 정정, 실제 활성화는 B-10 로컬 트랙) |
| 2026-05-29 | **실전 적용용 재설계** — 백로그 중 체인 작동 필수분을 **Phase 7(실전 보강: B-7 필수 + B-1/2/3 권장)** 로 승격, **Phase 8(기존 문서 정합화: README·AGENTS 등)** 신설, push&PR을 **Phase 9**로 재번호, **Phase 10(개발자 프로세스 가이드 교과서 — 설계만 본 PR, 집필 별도)** 신설. 상단 적용범위 박스·커밋 분리표·PR이후·백로그(B-1/2/3/7 승격 표기) 동기화 |
| 2026-05-29 | **개발자 가이드를 본 PR로 포함 + 순서 이동** — Phase 10(개발자 가이드)을 push&PR 앞으로 옮겨 **Phase 9(개발자 가이드 — 본 PR, 집필 전 목차·범위 사용자 확정)**, push&PR을 **Phase 10**으로 재번호. Task 10-3(분해)→9-3(집필)로 전환. 상단 박스·제외·커밋표(행 10 추가)·PR이후 동기화 |
| 2026-05-29 | **백로그 정리** — 본 PR로 승격된 B-1·B-2·B-3(→Phase 7-2~7-4)·B-7(→Phase 7-1)을 백로그에서 제거(결번 처리, 도입부에 추적 노트). 남은 백로그 = B-4(완료 기록)·B-5·B-6·B-8·B-9·B-10·B-11·B-12 |
| 2026-05-29 | **백로그 순차 재번호** — 결번을 없애고 남은 8항목을 B-1~B-8로 재정리(옛→새: B-4→B-1, B-5→B-2, B-6→B-3, B-8→B-4, B-9→B-5, B-10→B-6, B-11→B-7, B-12→B-8). 전방 참조(적용범위 박스·Phase 6·PR 본문)와 Task 7 출처 라벨(제거된 옛 B-번호 → TO-BE §4.4/§4.7.1~3)도 동기화 |
| 2026-05-29 | **tobe-temp 폐기 방침 반영** — tobe-temp는 운영 레포 이관 완료 후 *삭제(폐기)* 결정(아카이브 아님). `PR 이후`의 아카이브 줄을 삭제 절차로 변경 + B-1의 "tobe-temp 잔여 표기 정리"(321)는 *삭제 대상이라 불요*로 종결 → B-1 ✅ 완료 처리 |
| 2026-05-29 | **Phase 7-2 완료** — 레이어 분리 확정(작성=4팁 전부 / 리뷰=TBD만 검출). `munto-spec-writer`에 `### 비결정·미정 항목 4팁`(TBD·N/A vs None·Will Not Do·Decision Log) 작성 지침 + `spec-writing-tips.md` 로드 추가. `munto-spec-review` `H. TBD 및 미정 표기 처리` 보강(TBD 잔존 하드/빈칸 소프트), 비목표·Decision Log *부재*는 비검출 명시. `spec-reviewer` 자체검증에 부재 오검출 방지 가드. check-adapters 137개 통과 |
| 2026-05-29 | **Phase 7-1 완료** — `dev-chain-backend·mobile·frontend` 3종에 `## 권장 입력 — IP(구현계획서) 확인` 섹션 + PM 역할표·`입력 확인`·위임 prompt(`(선택) ip=`)에 IP 연결. `backend/mobile/frontend-expert` 입력부에 IP 소비 정의 추가(체인이 IP를 실입력으로 소비). IP는 비블로커 명시(TO-BE §4.4). check-adapters 137개 통과 |
| 2026-05-29 | **Glossary → SRS §1.4 Terms and Abbreviations 로 정정** — Munto SRS 표준은 별도 §10 Glossary가 아니라 §1.4에 용어를 적음. Task 7-3 제목·항목을 §1.4 기준으로 수정(별도 부록 신설 X) + One Pager용 항목 안내 추가. TO-BE §4.7.2 본문·자기점검·질문강제 절차 §1.4로 일괄 동기화. `OnePager_v1.0_template.md`에 *Terms and Abbreviations* 항목 신설. `spec-standard.md §1.4`는 이미 정확하여 유지 |
| 2026-05-29 | **Task 7-3 완료** — `munto-spec-writer`에 §1.4 용어·약어 등록 지침(SRS 핵심규칙·자체검증·전용 절) + OnePager 8→9개 항목 동기화. `munto-spec-review` `B. 기호·수식·용어 선행 정의(§1.4)` 확장(누락 의심 용어 🟡) + OnePager 9개 검증. `spec-standard.md §"용어·약어(1.4) 작성 원칙"` 5질문 재사용(중복 정의 회피). check-adapters 137개 통과. **brief(team-developer-brief.md)도 Glossary→§1.4 + N/A·None 표현 동기화** |
| 2026-05-29 | **Task 7-3 보강 — §1.4 선별 원칙 명시** — "모든 용어·약어 나열 X, 문서 성격·독자(신입 개발자·직원·타 직군) 기준 모르거나 혼동·애매할 만한 것만 선별, 다 적으면 낭비"를 `munto-spec-writer` 전용 절 맨 앞 *선별 원칙* 박스 + SRS 핵심규칙·자체검증(누락/과잉 양방향)에 반영. `munto-spec-review` §B에 *과잉 나열 정리 제안(🟢)* 소프트 체크 추가. (Book SRS §1.4·`spec-standard.md §1.4` 원칙과 일치) |
| 2026-05-29 | **Phase 9 완료 — 개발자 프로세스 가이드 신설** — 사용자 확정(단일 파일 / 8장 전체 / self-contained)에 따라 `document/dev-process-guide.md` 집필. 8장(큰그림+마스터 mermaid·8원칙·PHASE별 사용법·사람 게이트·지시법(4팁·§1.4·대안박스)·베이스라인/CCB·무인모드·치트시트), mermaid 4종(마스터·PHASE0·PHASE1·CCB·루프). positioning=self-contained(핵심 규범 본문 + 깊은 근거만 TO-BE §X 링크, 정본 우선 명시). `AGENTS.md`·`README.md`에 진입 링크+표준문서 등재. check-adapters 137개 통과 |
| 2026-05-29 | **Phase 8 완료 — 기존 문서 정합화** — `AGENTS.md`(서브에이전트 13종 목록·`document/` 표준 섹션·`projects/` 구조·`qa-tcl-writer`·`munto-humanize`·frontend 스킬·`jira` 규칙 신설/정정), `README.md`(구조 도식·통합 스킬/규칙표·Development Chain·표준 문서·서브에이전트·옛 커맨드/경로 예시 정정·A~J), `munto-skills/SKILL.md`(stale `*-acli`/Deprecated 제거 후 실제 인벤토리로 전면 백필 + 서브에이전트 안내), `.claude/agents/spec-reviewer.md`(A~I→A~J). check-adapters 137개 통과 |
| 2026-05-29 | **Task 7-4 완료 — 대안 검토 박스(선별 적용)** — 목적=AI 아키텍처 무지성 수용 차단. `munto-spec-writer`(§2.2 핵심 결정)·`dbml-writer`(핵심 엔티티 구조)·`swagger-writer`(핵심 계약 패턴)에 *선별 원칙 박스*+작성 지침 추가(**모든 결정 X, 핵심 아키텍처만, 버그수정·소규모·기존 표준 답습 면제, 박스 0개도 정상**). 리뷰는 `munto-spec-review`(§J 신설, A~J 갱신)·`dbml-reviewer`(S5)에 *소프트 질문*으로만(부재 자동결함 금지), `spec-reviewer`에 A~J·부재 오검출 방지 가드. **`design-consistency-reviewer`는 정합성 전용이라 제외**(단일 책임 보존). TO-BE §4.7.3 강제 문구도 선별 원칙으로 동기화. check-adapters 137개 통과 |
| 2026-05-29 | **N/A vs None 정의 오해 소지 수정** — "있어야 하지만 없음"이 "있어야 하는데 빠짐(누락)"으로 오독되는 문제 해소. `N/A`=적용 자체가 불가(예: v1.0 하위호환성) / `None`=적용 대상이나 이번엔 없음·안 함(예: v2.0 하위호환 미지원, 실무에선 "지원하지 않음+사유")로 통일. 수정: TO-BE.md 4팁 표, 본 계획서 Task 7-2, `munto-spec-writer`/`munto-spec-review` 스킬, `spec-writing-tips.md §4.2`. `spec-standard.md §해당 없는 항목 처리`는 이미 정확하여 유지 |
| 2026-05-29 | **백로그 중복분 제거** — Phase에 이미 기록된 완료 항목 정리: ip-writer/ip-reviewer(전부 Phase 4 기록) 항목 삭제, Hook 견본·`.gitignore`(Phase 6 기록) 중복 `[x]` 줄 삭제. 남은 7항목 B-1~B-7로 재번호(옛→새: B-2→B-1, B-3→B-2, B-4→B-3, B-5→B-4, B-6→B-5, B-7→B-6, B-8→B-7) + 전방 참조 동기화. (B-1 TO-BE 경로 동기화의 완료 체크는 Phase 비종속 백로그 작업이라 유지) |
| 2026-05-29 | **B-2 완료 — dev-chain-design 2-Track 재구성(본 PR 편입)** — 사용자 결정에 따라 `dev-chain-design/SKILL.md` 본문을 TO-BE §3.4 2-Track으로 전면 재작성. 기존 "3종 동시 팬아웃(순차 호출 금지)" 폐기 → Step 2(Track1 DBML 작성·AI리뷰·👤BE 확정)/Step 3(Track1 Swagger·정합성·👤BE+FE/App 입회)/Step 4(Track2 UI 확인+Track3 Unit TCL·👤도메인)/Step 5(종합 게이트→베이스라인 v1.0). 헤더 도식·PM표(5종, 트랙 칼럼)·금지사항(순차/후속/게이트 자동통과 금지)·metadata 동기화. **필수 부수**: `design-consistency-reviewer`에 *모드 A(DBML↔Swagger, TCL 미작성 단계)* 추가(기존 3종 필수 거부가 1A-5를 막음) + Claude/Codex 어댑터 거부 문구 동기화. *방금 작성한 가이드 ch.3·AGENTS 다이어그램(2-Track) ↔ 실제 스킬(3종 병렬)의 드리프트 해소.* check-adapters 137개 통과 |
| 2026-05-29 | **B-3 종결 — CCB 변경관리 문서화 충족(본 PR)** — `document/dev-process-guide.md` ch.6에 CCB(규모별 가변)·AI 1차 영향도·베이스라인 버저닝(v1.x/v2.0)·Decision Log를 self-contained로 문서화 완료. 별도 표준 파일/규칙 강제력은 필요 시 후속 PR(선택). |
| 2026-05-29 | **B-3 보강 — `munto-spec-change` 운영 스킬 신설(본 PR)** — 사용자 제공 *책 변경관리* 내용을 정제해 영향 평가 운영 스킬을 신설. 5대 원칙(신속함>완벽함·설득 도구·기록 보존)·절차(CCB 미강제)·영향 체크리스트(비즈니스 8 + 기술 9)·변경 요청서 템플릿·AI 1차 영향도 보고서 템플릿·버저닝. Claude/Codex 어댑터 + AGENTS/README/munto-skills 등록 + TO-BE §4.8·가이드 ch.6/ch.8 링크. check-adapters 139개. |
| 2026-05-29 | **Task 7-5 추가·완료 — IP 번호 기반 구현 지시(디스패치)** — `"Task 1.2/Phase 1/Phase 1-3/IP 기준 구현"` 진입점 부재 해소. PHASE 2 오케스트레이션의 *유인 디스패치*로 정의: `dev-process-guide` ch.3 디스패치 절 + ch.8 치트시트, `dev-chain-backend·mobile·frontend` 3종 IP 섹션에 *Task/Phase 번호 호출 시 IP 조회→자기 도메인 Task 선별→DAG 위상 순서→expert 위임* 4단계, `AGENTS.md` 행동 원칙 6번(메인 디스패치 라우팅) 신설. 상단 *이번 PR 제외* 박스의 B-2 잔여 표기 정정(B-2 완료 반영) + Phase 10 변경요약·의도적 제외·커밋표(행 8) 동기화. check-adapters 139개. |
