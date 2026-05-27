# `dev-chain-design` 스킬 보강 검토안 — IP 1 차 초안 자동 생성 단계 신설

> **목적**: 기존 `dev-chain-design` 스킬에 **Implementation Plan (구현계획서, IP)** 의 *1 차 초안을 자동 생성하는 단계*를 추가하는 검토안.
> **본 문서의 위치**: 검토안 단계의 *제안* 이며, *구현 결정* 이 아닙니다. 팀 검토 후 본 레포 (`munto-dev-assistant`) 의 `.agents/skills/common/docs/dev-chain-design/SKILL.md` 본문에 반영하거나, *별도 후속 스킬 (`dev-chain-implementation-plan`) 로 분리* 할지 결정합니다.

**관련 문서**

- 상위 표준: [`ip-standard.md`](./ip-standard.md) — IP 작성 표준
- 신규 스킬 초안: [`skills/dev-chain-implementation-plan/SKILL.md`](./skills/dev-chain-implementation-plan/SKILL.md) — 본 검토안과 대안 관계
- 기존 스킬: 본 레포 `.agents/skills/common/docs/dev-chain-design/SKILL.md` (검토 시점 그대로 두고, 본 문서는 *제안만* 함)
- TO-BE: [TO-BE 프로세스 가이드 (Notion)](https://www.notion.so/Agentic-Dev-Chain-Munto-TO-BE-36de2bc7639d8052b13fc49575c10e56) §4.3 (IP-0 ~ IP-8) / §4.9 (PHASE 2 무인 모드)

---

## 목차

- [배경 — 왜 보강이 필요한가](#배경--왜-보강이-필요한가)
- [선택지 3 가지](#선택지-3-가지)
- [추천 — 선택지 B (별도 후속 스킬 분리)](#추천--선택지-b-별도-후속-스킬-분리)
- [선택지 A 의 상세 — `dev-chain-design` 내부 확장](#선택지-a-의-상세--dev-chain-design-내부-확장)
- [선택지 B 의 상세 — 후속 스킬 분리](#선택지-b-의-상세--후속-스킬-분리)
- [선택지 C 의 상세 — 현행 유지 + 매뉴얼 IP](#선택지-c-의-상세--현행-유지--매뉴얼-ip)
- [공통 — 신규 서브에이전트 필요성](#공통--신규-서브에이전트-필요성)
- [의사 결정 체크리스트](#의사-결정-체크리스트)
- [팀 리뷰 포인트](#팀-리뷰-포인트)

---

## 배경 — 왜 보강이 필요한가

기존 `dev-chain-design` 스킬은 *DBML + Swagger + Unit TCL* 3 종 산출물 생성과 정합성 검증까지만 다룹니다. 그러나 **그 직후 단계 — Spec 을 AI 실행 가능한 형태로 변환하는 IP 작성 — 가 자동화되어 있지 않습니다.**

- 현재: Spec 베이스라인 v1.0 → *(사람이 매번 컨텍스트 재구성하며 dev-chain-backend/mobile/frontend 호출)* → 구현
- 보강 후: Spec 베이스라인 v1.0 → **IP 1 차 초안 자동 생성** → *사람이 IP 검토·확정* → dev-chain-backend/mobile/frontend 호출 (IP 가 유일한 입력)

> **핵심 효과**: PHASE 1 ~ PHASE 2 사이의 *컨텍스트 재구성 비용을 IP 가 1 회 자동 생성으로 흡수* — TO-BE §4.3 IP 절의 *입력 → 출력* 사슬을 완성합니다.

---

## 선택지 3 가지

| 선택지 | 설명 | 장점 | 단점 |
|--------|------|------|------|
| **A. `dev-chain-design` 내부 확장** | 기존 5 Step 뒤에 *Step 6: IP 1 차 초안 생성* 을 추가 | *입출력 일체화* (Spec 만들고 바로 IP 까지) · 단일 스킬 호출로 끝남 | 스킬이 비대해짐 · 책임 경계 모호 · *Spec ↔ IP 의 사람 리뷰 게이트가 1 개* 로 합쳐져 *IP 통과 = 인수* 원칙 약화 |
| **B. 별도 후속 스킬 분리** *(추천)* | `dev-chain-implementation-plan` 신규 스킬을 만들어 *dev-chain-design 완료 직후* 호출 | *책임 경계 명확* (설계 vs 구현 계획) · *IP 사람 리뷰 게이트* 가 독립적으로 작동 · 향후 IP-only 재실행 가능 | 스킬 호출 1 회 추가 · *dev-chain-design 완료 → 다음 스킬* 의 *연결 강제* 가 필요 |
| **C. 현행 유지 + 매뉴얼 IP** | 스킬 변경 없음. IP 는 `ip-standard.md` 만 두고 사람이 직접 작성 | 변경 최소 · IP 표준 정착 단계에서 시행착오 수용 | *자동화 효과 없음* · *Spec → 구현 사이 컨텍스트 재구성 비용 문제 (AS-IS §4.15)* 가 해결 안 됨 |

---

## 추천 — 선택지 B (별도 후속 스킬 분리)

### 추천 사유

1. **책임 경계가 분명**: `dev-chain-design` = *Spec 산출* / `dev-chain-implementation-plan` = *Spec → 실행 명세 변환*. 각각 다른 입력·서브에이전트·정합성 기준.
2. **사람 리뷰 게이트가 독립**: Spec 베이스라인 v1.0 통과 ≠ IP 베이스라인 v1.0 통과. *통과 = 인수* 원칙을 두 번 적용해야 안전 (TO-BE §3.2 / `ip-standard.md` §11).
3. **IP-only 재실행 가능**: Spec 변경 없이 *Task 분할만 다시 한 번* 의 경우 IP 스킬만 다시 돌릴 수 있음 — *불필요한 Spec 재검증 회피*.
4. **무인 루프 (§4.9) 의 직접 입력 명세**가 별도 스킬로 *분리되어 명문화*되는 효과 — 운영 책임이 분명.
5. **향후 진화 여지**: IP 생성 로직이 복잡해질 가능성 (DAG 추론, 의존성 자동 도출 등) — *별도 스킬* 이 *내부 확장* 보다 발전 여지 큼.

### 두 스킬의 인터페이스

```
dev-chain-design (기존)
   ↓ 출력: DBML + Swagger + Unit TCL (+ 정합성 PASS)
   ↓ 사용자 안내: "Spec 베이스라인 v1.0 통과 후 dev-chain-implementation-plan 호출 권장"
dev-chain-implementation-plan (신규)
   ↓ 입력: Spec 베이스라인 v1.0 4 종 산출물 + Spec Index 후보
   ↓ 출력: IP 1 차 초안 (munto-dev-assistant/projects/{프로젝트명}/ImplementationPlan.md)
   ↓ 사용자 안내: "IP 사람 리뷰 7 가지 질문 통과 후 무인/유인 PHASE 2 진입"
```

### `dev-chain-design` 측 *최소 변경* (선택지 B 채택 시)

- Step 5 *완료 보고* 마지막에 **다음 단계 안내** 한 줄 추가:

  > "다음 단계: Implementation Plan (구현계획서) 작성 — `dev-chain-implementation-plan` 스킬을 호출하세요. *Spec 만으로 dev-chain-backend/mobile/frontend 를 호출하면 컨텍스트 재구성 비용이 Task 수만큼 폭증합니다.*"

- 그 외 기존 5 Step 본문은 변경하지 않음.

---

## 선택지 A 의 상세 — `dev-chain-design` 내부 확장

> 추천은 아니지만, 팀이 *단일 스킬 호출* 을 선호할 경우의 상세 설계입니다.

### 추가될 Step 6 (제안)

```
## Step 6: IP 1 차 초안 자동 생성

### 전제 조건
- Step 5 의 두 reviewer 모두 PASS
- 사용자 결정: 별도 `dev-chain-implementation-plan` 스킬을 호출할 것인가, 본 스킬에서 IP 까지 같이 만들 것인가
- 사용자가 *본 스킬에서 같이* 를 선택한 경우에만 본 Step 진입

### 신규 서브에이전트 호출

[병렬 호출]
├─ Task(subagent_type=ip-writer,
│       prompt="Spec=<3종 경로>, Repos=<참여 repo 목록>, Project=<프로젝트명>")
└─ Task(subagent_type=ip-reviewer,
        prompt="IP 초안=<경로>, ip-standard.md 7 가지 질문 자동 검증")

### 산출물
- munto-dev-assistant/projects/{프로젝트명}/ImplementationPlan.md (프로젝트 폴더 안 고정 파일명)
- ip-reviewer 의 자동 점검 결과 보고

### 사람 리뷰 게이트
- ip-reviewer 가 PASS 한 *1 차 초안* 이라도, *사람의 IP 7 가지 질문 통과* 까지가 베이스라인 v1.0
```

### 단점 재확인

- 단일 스킬이 Spec 과 IP 두 가지 책임을 모두 짊
- 사용자가 *"IP 까지 같이"* 옵션을 선택해야 하므로 *조건 분기* 가 늘어남
- *IP 사람 리뷰* 가 Spec 사람 리뷰와 한 회기에 묶이면 *피로 누적으로 IP 검토가 형식화* 될 위험

---

## 선택지 B 의 상세 — 후속 스킬 분리

### 신규 스킬: `dev-chain-implementation-plan`

자세한 명세는 [`skills/dev-chain-implementation-plan/SKILL.md`](./skills/dev-chain-implementation-plan/SKILL.md) 참조.

요약:

| 항목 | 값 |
|------|------|
| **트리거** | "IP 만들어줘", "구현계획서 작성", "Implementation Plan", "dev-chain-implementation-plan" |
| **위치** | Development Chain 의 *PHASE 1 마지막 활동* (`dev-chain-design` 다음, `dev-chain-backend/mobile/frontend` 이전) |
| **입력** | Spec 베이스라인 v1.0 4 종 + 참여 Repo 목록 + 프로젝트명 + (선택) 운영 모드 선호도 |
| **출력** | `munto-dev-assistant/projects/{프로젝트명}/ImplementationPlan.md` (1 차 초안. 프로젝트 폴더 + 고정 파일명) |
| **서브에이전트** | `ip-writer` (신규) + `ip-reviewer` (신규) — 아래 [공통 — 신규 서브에이전트 필요성](#공통--신규-서브에이전트-필요성) 참조 |
| **완료 조건** | ip-reviewer 자동 PASS + 사용자에게 *사람 리뷰 7 가지 질문* 명시적 안내 |

### `dev-chain-design` 측 변경

- Step 5 의 *다음 단계* 표에 1 행 추가만 하면 됨 — 본 문서 [추천 사유 § 두 스킬의 인터페이스](#두-스킬의-인터페이스) 참조.

### *PHASE 2 측* 변경 (별도 검토 필요)

- `dev-chain-backend/mobile/frontend` 의 *입력 확인* 단계에 *"IP 가 존재하고 사람 리뷰가 통과되었는가"* 질문 추가
- IP 없이 호출하면: *"IP 가 없습니다. `dev-chain-implementation-plan` 을 먼저 호출하시겠습니까? (강제 아님 — 작은 변경은 IP 없이 진행 가능)"* 안내
- IP 가 있으면: Task 카드 *순회 모드* (DAG 위상 정렬 순)로 자동 진행 가능

> ⚠️ *PHASE 2 측 변경* 은 본 검토안의 범위 밖. *IP 신규 스킬 도입 후* 별도 PR 로 진행 권장.

---

## 선택지 C 의 상세 — 현행 유지 + 매뉴얼 IP

- 스킬 변경 0.
- `ip-standard.md` 만 두고 사람이 *Spec 베이스라인 v1.0 통과 후 매번 IP 를 직접 작성*.
- *IP 표준 정착 단계 (3 ~ 6 개월)* 의 시범 운영안으로 적합.
- 단점: TO-BE §4.3 의 자동화 효과가 *전혀 실현되지 않음*. *AS-IS §4.15 (IP 부재) 의 본질적 문제*가 해결되지 않음.

### C 를 선택해야 하는 경우

- IP 표준 자체가 *팀에 처음 도입* 되는 초기 (양식 안정화가 우선)
- 자동화 도구 (ip-writer 서브에이전트) 의 출력 품질이 *불확실* 한 시기
- *팀이 매뉴얼로 작성한 IP 사례* 를 충분히 모아 *자동화 학습 데이터* 로 활용하고자 할 때

---

## 공통 — 신규 서브에이전트 필요성

선택지 A·B 모두 *신규 서브에이전트 2 종*이 필요합니다.

### `ip-writer` (신규 제안)

| 항목 | 값 |
|------|------|
| 역할 | Spec 4 종을 읽고 IP 1 차 초안 생성 |
| 입력 | Spec 4 종 경로 + 참여 Repo 목록 + 프로젝트명 |
| 출력 | IP 마크다운 (8 섹션) |
| 권한 | read-only (Spec 읽기) + 단일 파일 쓰기 (`projects/{프로젝트명}/ImplementationPlan.md`) |
| 패턴 | 전문가 풀 (단독 호출) |

### `ip-reviewer` (신규 제안)

| 항목 | 값 |
|------|------|
| 역할 | IP 초안을 `ip-standard.md` 의 7 가지 질문 + 완료 체크리스트로 자동 점검 |
| 입력 | IP 초안 경로 + `ip-standard.md` 참조 |
| 출력 | BLOCKER / WARNING / SUGGESTION 리포트 |
| 권한 | read-only |
| 패턴 | 생성-검증 페어 (ip-writer 의 짝꿍) |

> ⚠️ *주의*: 본 두 서브에이전트의 정의는 *제안만* 입니다. 실제 추가는 별도 PR 로 진행. *서브에이전트 정의는 본 검토안에 포함하지 않음.*

---

## 의사 결정 체크리스트

팀 리뷰 시 아래 5 가지를 결정한 후 본 검토안을 닫습니다.

- [ ] **결정 1**: 선택지 A / B / C 중 어느 것을 채택할 것인가? (추천: B)
- [ ] **결정 2**: 신규 서브에이전트 (`ip-writer`, `ip-reviewer`) 를 실제로 만들 것인가? 만든다면 본 PR 과 분리할 것인가?
- [ ] **결정 3**: `munto-dev-assistant/projects/` 폴더와 `projects/README.md` 인덱스를 본 PR 에 포함할 것인가, 별도 PR 로 할 것인가?
- [ ] **결정 4**: 선택지 B 채택 시, *PHASE 2 측 스킬* (`dev-chain-backend/mobile/frontend`) 의 *IP 입력 확인* 안내 추가는 *후속 PR* 로 할 것인가?
- [ ] **결정 5**: 시범 운영 기간 (예: 2 개 프로젝트 시범) 동안 *매뉴얼 IP* (선택지 C 와 병행) 로 양식 안정화 후 자동화 도입을 단계화할 것인가?

---

## 팀 리뷰 포인트

| 항목 | 토론 포인트 |
|------|------------|
| **자동 생성 품질** | ip-writer 가 Spec 만 보고 *Task 의존성·DoD·DAG* 를 얼마나 정확히 추론할 수 있는가? *초안 후 사람이 보강* 이 현실적인가? |
| **사람 리뷰 부담** | IP 사람 리뷰 7 가지 질문이 *Spec 리뷰 5 가지 질문* (spec-standard.md §AI 작성물 검증) 과 겹치지 않는가? 합칠 수 있는가? |
| **저장 위치 트래픽** | `munto-dev-assistant/projects/` 가 *모든 프로젝트의 IP* 가 모이는 곳이 됨. 너무 비대해지면 *연도별 폴더 (`projects/2026/`)* 로 분할할 것인가? |
| **수정 빈도** | IP 가 *PHASE 2 중 자주 갱신* 될 가능성. *minor 변경 (v1.x)* 의 정도와 *사람 재리뷰 강도* 를 어떻게 균형 잡을 것인가? (`ip-standard.md` §변경 관리·버전) |
| **무인 루프 의존** | IP 가 *무인 루프의 유일한 입력* 이라는 강한 의존성. 무인 루프를 *당분간 도입하지 않음* 으로 결정하면 IP 자체의 필요성이 약화되는가? *(답: 약화되지 않음 — 유인 모드에서도 IP 가 컨텍스트 재구성 비용을 흡수)* |

---

## 변경 이력

| 일자 | 내용 |
|------|------|
| 2026-05-22 | 신규 작성 — 선택지 A·B·C 비교, B 추천, 신규 서브에이전트 제안 |
| 2026-05-27 | **IP 저장 단위 *단일 파일 → 프로젝트 폴더* 전환 동기화** — 본문 4 곳 경로 갱신 (`{프로젝트명}.ip.md` → `{프로젝트명}/ImplementationPlan.md`): ① §두 스킬의 인터페이스 다이어그램, ② 선택지 A 의 Step 6 산출물 목록, ③ 선택지 B 요약 표의 *출력* 셀, ④ §공통 — 신규 서브에이전트(ip-writer 권한 셀). 표준은 TO-BE §4.3 IP-0 / `ip-standard.md` §저장 위치와 파일명 규약 |
