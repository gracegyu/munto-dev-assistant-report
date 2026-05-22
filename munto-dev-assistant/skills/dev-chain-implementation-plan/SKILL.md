---
name: "dev-chain-implementation-plan"
description: "Generates an Implementation Plan (구현계획서, IP) from baselined Spec artifacts. Converts Spec into an AI-executable single document with Phase/Task breakdown, Spec reference paths (4-element), Dependency DAG, and DoD mapping. PHASE 1 의 *마지막 활동*. PHASE 2 (유인/무인 모드) 의 *유일한 입력* 을 만든다. Triggers: \"IP 만들어줘\", \"구현계획서 작성\", \"Implementation Plan\", \"Task 분해해줘\", \"무인 실행 입력 준비\"."
metadata:
  last_modified: "2026-05-22"
  revision: "신규 작성 — TO-BE §4.3 (IP-0 ~ IP-8) 과 ip-standard.md 에 기반한 스킬 정의 초안. 검토안(dev-chain-design-update-proposal.md) 의 선택지 B 채택을 전제로 한다."
status: "PROPOSAL — 검토 후 본 레포 .agents/skills/common/docs/dev-chain-implementation-plan/SKILL.md 로 이전 예정"
---

# Dev Chain — Implementation Plan (구현계획서, IP) 생성 단계

**위치**: Development Chain 의 **PHASE 1 마지막 활동** *(별도 PHASE 번호 없음)*
**이전 단계**: `dev-chain-design` (DBML + Swagger + Unit TCL 베이스라인 v1.0 통과 후)
**다음 단계**: `dev-chain-backend`, `dev-chain-mobile`, `dev-chain-frontend` (IP 가 *유일한 실행 입력* 이 된다)

```
dev-chain-design 완료 (Spec 베이스라인 v1.0)
   ↓
[이 스킬: 메인은 PM 역할]
   ↓
IP 1 차 초안 → ip-reviewer 자동 점검 → 사람 리뷰 (7 가지 질문) → IP 베이스라인 v1.0
   ↓
PHASE 2 (유인/무인 모드) — IP 가 유일한 입력
```

**참조 표준**: [`ip-standard.md`](../../../ip-standard.md) *(상대 경로는 본 검토 폴더 구조 기준 — 본 레포 이전 시 경로 갱신)*

---

## ⚠️ 메인 에이전트의 역할 (PM 모드)

**메인 에이전트는 직접 IP 본문을 작성하지 않는다.**
대신 다음 2 개 서브에이전트에 Task 툴로 위임하고, 결과를 모아 사용자에게 보고하는 **PM(조율자) 역할**만 수행한다.

| 서브에이전트 | 역할 | 패턴 |
|---|---|---|
| `ip-writer` | IP 1 차 초안 생성 (8 섹션) | 전문가 풀 |
| `ip-reviewer` | `ip-standard.md` 의 7 가지 질문 + 완료 체크리스트 자동 점검 (read-only) | 생성-검증 페어 |

> ⚠️ *두 서브에이전트는 본 검토안과 함께 신설 제안 단계*. 실제 추가는 [`dev-chain-design-update-proposal.md`](../../dev-chain-design-update-proposal.md) 의 *결정 2* 에 따른다.

**금지 사항**:
- ❌ 메인이 직접 IP 본문 작성
- ❌ writer 단독 호출 (반드시 reviewer 와 페어로)
- ❌ ip-reviewer 자동 PASS 만으로 사용자 통과 안내 — *사람 리뷰 7 가지 질문 안내가 의무*

---

## 입력 확인

시작 전 다음을 모두 확인합니다.

### 필수 입력 (모두 있어야 진행)

1. **Spec 베이스라인 v1.0 4 종 산출물 경로**
   - SRS (예: `munto-backend/docs/specs/.../SRS.md`)
   - DBML (예: `munto-backend/docs/specs/.../DBML.dbml`)
   - Swagger (예: `munto-backend/docs/specs/.../swagger.yaml`)
   - Unit TCL (예: `munto-backend/docs/specs/.../tcl.md`)
2. **참여 Repo 목록** — BE / FE / APP 중 어느 것이 참여하는지
3. **프로젝트명** — 영문 소문자·하이픈만, 50 자 이내 (예: `paid-socialing-v2`)
4. **Spec 베이스라인 동결 SHA** — 각 참여 Repo 의 동결 시점 git SHA

### 권장 입력 (없으면 사용자에게 질문)

- 프로젝트 Owner (Slack 핸들)
- 무인 모드 / 유인 모드 선호 (기본: 유인)
- Slack 알림 채널명
- *Spec 작성 방식* — ① 기존 Spec 수정 / ② Sub스펙 누적 / ③ 별도 repo Spec (③ 인 경우 *통합 마감 Task* 자동 포함)

### 입력 누락 시

위 *필수 입력* 중 하나라도 누락되면, **반드시 사용자에게 질문 후 받아낸 다음 진행한다.** 누락한 채로 자동 추측 금지.

특히 *Spec 베이스라인 동결 여부* 가 확인되지 않으면, *"Spec 베이스라인이 동결되지 않았습니다. `dev-chain-design` 의 Step 5 완료 보고를 통과한 상태인지 확인하세요. 베이스라인 미동결 상태에서 IP 를 작성하면 SHA 가 흔들려 무인 루프가 작동하지 못합니다."* 라고 안내하고 진행을 *중단*.

---

## Step 1: 입력 확정 (메인이 직접 수행)

위 *입력 확인* 의 모든 정보를 사용자와 함께 표로 정리합니다.

```markdown
| 항목 | 값 |
|------|------|
| 프로젝트명 | paid-socialing-v2 |
| Owner | @grace.gyu |
| 참여 Repo | munto-backend (sha a1b2c3d), munto-frontend (sha e4f5g6h) |
| Spec 4 종 경로 | (위 4 종 경로) |
| 운영 모드 | 유인 디폴트 (P1·P2 완료 후 무인 전환 검토) |
| Slack 채널 | #dev-paid-socialing |
| Spec 작성 방식 | ② Sub스펙 누적 |
```

→ 서브에이전트에게 전달할 *입력 명세서* 가 된다.

---

## Step 2: 팬아웃 — `ip-writer` 단일 호출

> ⚠️ Step 2 는 *단일 writer* 만 호출하므로 *진정한 팬아웃은 아님*. `dev-chain-design` 의 *3 writer 병렬* 패턴과 차이가 있다 (IP 는 *단일 문서*이므로 분할 작성 시 정합성이 깨짐).

```
Task(subagent_type=ip-writer,
     prompt="입력 명세서=<Step 1 결과>,
             산출물=IP 마크다운 텍스트 반환,
             섹션=8 개 고정 (Project Header / Spec Index / Phase / Task Cards / DAG / DoD / Operating Mode / Change History),
             표준=ip-standard.md")
```

- writer 는 Spec 4 종을 자기 컨텍스트에서 직접 읽는다. *메인은 Spec 본문을 끝까지 읽지 않는다.*
- writer 의 출력은 *1 차 초안* 이며, *DAG 의 정확도·DoD 의 기계 판정 가능성*은 아직 검증되지 않은 상태.

writer 응답이 도착하면 메인은 다음 경로에 임시 저장:

```
munto-dev-assistant/projects/{프로젝트명}.ip.md
```

> ⚠️ *위 경로는 절대 변경 금지*. `ip-standard.md` §저장 위치와 파일명 규약 참조.

---

## Step 3: 팬인 — `ip-reviewer` 단일 호출

```
Task(subagent_type=ip-reviewer,
     prompt="IP 초안=<munto-dev-assistant/projects/{프로젝트명}.ip.md>,
             표준=ip-standard.md,
             자동 점검 7 가지 질문 + 완료 체크리스트")
```

reviewer 는 read-only다. 출력:

- **BLOCKER**: 필수 필드 누락 / 순환 의존 / SHA 가 동결 SHA 아님 / `T-MIGRATE-SPEC-FINAL` 누락 (③ 방식인데 없음) / TCL ID 누락
- **WARNING**: Task 단위 너무 큼 (estimate > 4h, outputs > 3) / DoD 가 모두 자동인데 *Phase 모두 무인 모드 안전 기본값 미정* / Operating Mode 의 Kill Switch 미명시
- **SUGGESTION**: 병렬 가능한 Task 가 *직렬로 표기됨* / *Phase 단위 서브그래프 분할 권장* (DAG 노드 10 개 초과 시)

---

## Step 4: 이슈 처리

### Case 1: reviewer PASS (BLOCKER 0 개) → Step 5 로 진행

### Case 2: BLOCKER 발견 → `ip-writer` 재호출
- BLOCKER 에서 reviewer 가 제시한 *수정 가이드* 를 사용자에게 확인
- 결정된 방향으로 writer 를 재호출 (Task 단발, 변경 부분만)
- 다시 Step 3 로 돌아가 reviewer 재실행

### Case 3: WARNING 만 있음 → 사용자에게 보고 후 진행 여부 확인
- *Task 단위가 큰 것* 은 의도된 단위일 수 있으므로 사용자 판단
- 진행 결정 시 Step 5 로

> **루프 제한**: 같은 BLOCKER 에 대해 writer 재호출 2 회 이상 시 사용자에게 *수동 검토 요청*. 무한 루프 방지.

---

## Step 5: 완료 검증 및 사람 리뷰 안내

완료 보고 전 다음을 반드시 확인합니다.

```
✅ 자동 검증 체크리스트 (메인이 확인)
- [ ] IP 파일이 munto-dev-assistant/projects/{프로젝트명}.ip.md 에 저장됨
- [ ] 8 개 섹션 모두 존재
- [ ] ip-reviewer 판정: PASS (BLOCKER 0)
- [ ] projects/README.md 인덱스에 추가됨 (메인이 자동 추가)
```

위 4 가지 모두 통과 시 사용자에게 다음 안내를 **반드시** 보냅니다.

```markdown
## Implementation Plan (구현계획서, IP) 1 차 초안 생성 완료

| 항목 | 값 |
|------|------|
| 저장 위치 | munto-dev-assistant/projects/{프로젝트명}.ip.md |
| 자동 점검 | ip-reviewer PASS |
| 현재 상태 | **v0.1 (초안)** — 사람 리뷰 미통과 |

### ⚠️ 다음 단계 — 사람의 IP 리뷰 (의무)

IP 는 *PHASE 2 의 유일한 입력* 이므로, *사람 리뷰 통과* 없이 PHASE 2 (특히 무인 모드) 로 진입하면 위험합니다.
아래 7 가지 질문을 모두 *예* 로 통과시킨 후, Change History 에 *인수자* 를 기록하고 v1.0 으로 변경하세요.

> 1. Task Card 9 필드 모두 채워졌는가? (`TBD` 0 개)
> 2. Spec Index 의 모든 SHA 가 *동결 SHA* 인가? (`HEAD` 가 아닌 fixed SHA)
> 3. Task 카드 spec_refs[] 가 모두 Spec Index ID 를 가리키는가? (4 요소 표기 검증)
> 4. depends_on[] 에 순환 의존이 없는가? (DAG 가 실제로 DAG 인가)
> 5. 모든 Task 의 dod[] 가 TCL 케이스 ID 를 1 개 이상 가지는가? (모호한 표현 0 개)
> 6. ③ 별도 repo Spec 방식이라면, T-MIGRATE-SPEC-FINAL Task 가 포함되어 있는가?
> 7. Operating Mode 의 무인 모드 안전 기본값과 Kill Switch 가 명시되어 있는가?

7 가지 중 단 1 개라도 *아니오 / 모름* 이면 **통과 보류**. 보강 후 재리뷰.

### 다음 단계 (사람 리뷰 통과 후)
- 백엔드 구현: `dev-chain-backend` 스킬 적용 — IP 의 BE 도메인 Task 를 *DAG 위상 정렬 순* 으로 진행
- 모바일 구현: `dev-chain-mobile` 스킬 적용
- 프론트엔드 구현: `dev-chain-frontend` 스킬 적용
- 무인 모드 진입 (해당 시): TO-BE §4.9 PHASE 2 무인 실행 모드 절차 참조
```

미완료 항목이 있으면 완료 보고하지 않고 해당 Step 으로 돌아갑니다.

---

## IP 작성 컨벤션 (서브에이전트와 메인이 모두 참조하는 source of truth)

> 본 절은 *최소한의 핵심* 만 적습니다. 상세 양식·예시·사람 리뷰 7 가지 질문은 [`ip-standard.md`](../../../ip-standard.md) 를 단일 진실 공급원으로 합니다.

### 저장 위치·파일명

- 위치: `munto-dev-assistant/projects/{프로젝트명}.ip.md` (절대 변경 금지)
- 파일명: 영문 소문자·하이픈, 50 자 이내, 메이저 버전만 표기 (`paid-socialing-v2.ip.md`)
- 인덱스: `munto-dev-assistant/projects/README.md` 에 자동 추가

### 8 섹션 고정 구조 (번호·제목 변경 금지)

1. Project Header
2. Spec Index (4 요소 표기)
3. Phase Breakdown
4. Task Cards (9 필드 고정)
5. Dependency DAG
6. DoD Mapping
7. Operating Mode
8. Change History

### Task Card 9 필드 (변경·삭제 금지)

`id` / `title` / `repo` / `spec_refs[]` / `depends_on[]` / `outputs[]` / `dod[]` / `estimate` / `risk`

### Spec 참조 4 요소

```
{repo}/{path}#{anchor}@{baseline-sha}
```

Task 카드에서는 *Spec Index ID + anchor* 로 줄여 표기 (예: `S-BE-1 §4.2.3`). SHA 는 Spec Index 행에 한 번만 기록.

### Task 단위 5 기준 (모두 만족해야 적정)

PR 크기 100~300 줄 / 단일 책임 / LLM 30 분~2 시간 / 외부 의존 분리 / 1 git revert 로 롤백 가능.

→ `estimate > 4h` 또는 `outputs > 3` 이면 *쪼갤 신호*.

### Spec 작성 3 방식과의 매핑

| 방식 | Spec Index 표기 | 강제 조건 |
|------|----------------|----------|
| ① 기존 Spec 수정 | 기존 파일 + 새 SHA | 없음 |
| ② Sub스펙 누적 | 신규 파일 SHA + 모스펙 연결 표기 | 모스펙 ↔ Sub스펙 연결 표기 의무 |
| ③ 별도 repo Spec | 임시 SHA | **`T-MIGRATE-SPEC-FINAL` Task 가 반드시 포함**. 누락 시 reviewer BLOCKER |

### 단일 세션 vs 세션 분리

Project Header 에서 4 기준 (Repo 개수 / Task 개수 / 예상 기간 / 참여 인원) 평가 후 결정. *디폴트 없음*.

---

## 본 스킬을 호출하지 *말아야 할* 경우

다음 중 하나에 해당하면 본 스킬을 호출하지 않습니다.

- **Spec 베이스라인 v1.0 이 동결되지 않음** — `dev-chain-design` 의 Step 5 완료 보고 미통과 상태. *베이스라인 미동결 IP* 는 의미 없음.
- **변경 범위가 매우 작음** (1 개 파일 수정·버그 픽스 수준) — IP 작성 비용이 효과보다 큼. 직접 `dev-chain-backend` 등 호출.
- **Spec 자체가 없음** (정찰성 시제 구현·POC) — IP 의 Spec 참조 4 요소가 채워질 수 없음. 그냥 직접 작성.

위에 해당하면 사용자에게 *"본 스킬은 PHASE 1 (Spec 베이스라인 v1.0) 통과 후 의미가 있습니다. 현재는 적용 불필요"* 라고 안내하고 종료.

---

## 다음 단계

> **주의**: 다음 단계 (`dev-chain-backend`, `dev-chain-mobile`, `dev-chain-frontend`) 는 *IP 사람 리뷰 통과* 후에만 시작합니다.
> 사용자가 *IP 사람 리뷰 통과* 없이 PHASE 2 로 진입을 요청하면, "IP 사람 리뷰 7 가지 질문 통과 여부를 먼저 확인해주세요. 통과 없이 진입하면 무인 모드 안전성을 보장할 수 없습니다." 라고 안내합니다.

특히 **무인 모드 (PHASE 2 무인)** 진입은 *IP 사람 리뷰 통과 + Operating Mode 의 Kill Switch 명시 + Slack 알림 정책 확정* 3 가지 모두 통과해야만 허용. 자세한 절차는 `reports/2026-05-harness-TO-BE.md` §4.9 참조.

---

## 변경 이력

| 일자 | 내용 |
|------|------|
| 2026-05-22 | 신규 작성 — TO-BE §4.3 (IP-0 ~ IP-8) 과 `ip-standard.md` 에 기반. 검토안 (`dev-chain-design-update-proposal.md`) 의 선택지 B 채택을 전제. 본 레포 이전 시 상위 폴더 경로 (`../../../ip-standard.md`) 를 본 레포 구조에 맞게 갱신 필요 |
