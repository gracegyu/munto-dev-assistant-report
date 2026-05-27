<!--
⚠️ 본 파일은 *적용 대기 본문* 입니다.

- 운영 레포 위치 (실제 적용 대상): /Users/gracegyu/Documents/GitMunto/munto-dev-assistant/.agents/skills/common/docs/munto-spec-review/SKILL.md
- 본 파일 위치 (기획 미러, 적용 대기):    munto-dev-assistant-report/munto-dev-assistant/skills/munto-spec-review/SKILL.md

원본 대비 *세션 저장 단계 (§"리뷰 결과 세션 저장 — 자동 (a)")* + *baseline-handoff 자동 점검 단계 (§"baseline 동결 점검")* 만 신설했습니다. 그 외 본문은 동일.
적용 시점은 ip-standard.md / TO-BE §4.7.4 정책이 운영 레포에 일괄 이관되는 시점입니다.
변경 근거: TO-BE §4.7.4 (1)(2)(5) — (a) 스킬 호출 자동 저장 + baseline-handoff 누락 시 BLOCKER 처리.
-->

---
name: "munto-spec-review"
description: "Reviews Munto spec docs (SRS, Engineering One Pager) against the internal standard (spec-standard.md). Supports Notion URL or local markdown. Actual checklist application is delegated to the spec-reviewer subagent (PM mode). Triggers: \"리뷰\", \"검토\", \"review\", \"스펙 리뷰\", \"SRS 리뷰\", \"원페이저 리뷰\", \"문서 리뷰\", \"문서 검토\"."
metadata:
  last_modified: "2026-05-27"
  revision: "세션 저장 단계 신설 — (a) 스킬 호출 자동 저장 + baseline-handoff 자동 점검 BLOCKER. PM 모드 도입 (2026-04-30) 위에 추가. 작성자별 파일 분리 정책 (옵션 α): cwd 가 projects/{프로젝트명}/ 이면 sessions/spec-review-{date}-{doc}-{slack-handle}.md 자동 생성. {slack-handle} 자동 추출 = 명시 인자 → git config user.email → $USER → 1 회 질문. baseline 통과 신호 시 spec-baseline-handoff.md 존재 여부 자동 점검. TO-BE §2.3 ⑧ + §4.7.4 (1)(2)(4)(5) 정책 반영."
---

# 스펙 문서 리뷰

## ⚠️ 메인 에이전트의 역할 (PM 모드)

**메인 에이전트는 직접 스펙 본문을 읽으며 체크리스트를 적용하지 않는다.**
실제 리뷰는 `spec-reviewer` 서브에이전트에 Task 툴로 위임한다.

| 작업 | 누가 |
|---|---|
| 문서 가져오기 (Notion fetch 또는 파일 Read) | **메인** — 짧은 작업 |
| 문서 유형 판별 (SRS / One Pager) | **메인** |
| 로컬 임시 파일로 저장 (Notion인 경우) | **메인** |
| **체크리스트 A~I (SRS) / A~G (One Pager) 전체 적용** | `spec-reviewer`에 위임 |
| **BLOCKER/WARNING/SUGGESTION 분류 + 영역별 커버리지 산출** | `spec-reviewer`가 자체 처리 |
| **세션 저장 (sessions/spec-review-*.md)** | **메인** — `spec-reviewer` 응답 수신 후 |
| **baseline 동결 점검 (spec-baseline-handoff.md 존재 여부)** | **메인** — 사용자가 baseline 통과 신호 시 |
| 결과 사용자에게 전달 + 후속 질문 응대 | **메인** |

### 위임 호출 패턴

```
사용자: "이 SRS 리뷰해줘 [Notion URL]"
   ↓
[메인]
1. Notion에서 문서 가져오기 (notion-fetch) 또는 파일 Read
2. 문서 유형 판별 (SRS / One Pager)
3. 임시 경로에 저장 (예: /tmp/spec-review-target.md) — 서브에이전트가 Read 가능하도록
4. cwd 점검 (세션 저장 활성 여부) — 아래 §"세션 저장" 참조
5. Task(subagent_type=spec-reviewer,
        prompt="
          스펙 경로=/tmp/spec-review-target.md,
          문서 종류=SRS,
          (선택) 관련 Jira=...,
        ")
6. spec-reviewer가 자체 컨텍스트에서:
   - munto-spec-review SKILL.md + spec-writing.md Read
   - 스펙 본문 전체(수천 줄) Read
   - 체크리스트 적용
   - BLOCKER/WARNING/SUGGESTION 리포트 반환
7. 메인이 결과를 사용자에게 보고
8. 메인이 세션 저장 활성 시 sessions/spec-review-{date}-{doc}.md 자동 생성 (§"세션 저장" 참조)
9. 사용자가 *baseline 통과 신호* 시 메인이 spec-baseline-handoff.md 점검 (§"baseline 동결 점검" 참조)
```

### PM 모드의 이점

- 메인 컨텍스트가 스펙 본문 수천 줄로 오염되지 않음
- 후속 사용자 질문(특정 BLOCKER 추가 설명 등)에 메인이 깨끗한 컨텍스트로 응답 가능
- 같은 패턴으로 여러 스펙을 *순차 리뷰*해도 메인 컨텍스트 누적 없음

### 예외 — 메인이 직접 처리하는 경우

- 사용자가 *특정 섹션 한 군데만* 리뷰 요청 (전체 체크리스트 불필요)
- 짧은 One Pager (수십 줄) — 위임 오버헤드가 더 큼

---

## 시작 전 준비 (메인이 수행)

1. `document/spec-standard.md`를 읽어 리뷰 기준을 로드합니다
2. 대상 문서를 가져옵니다
3. **cwd 점검 (세션 저장 활성 여부 결정)**:
   - cwd 가 `munto-dev-assistant/projects/{프로젝트명}/` 인지 검사
   - 맞으면: *세션 저장 활성* (아래 §"세션 저장" 단계 자동 수행)
   - 아니면: 1 회 경고 출력 후 작업 계속. 메시지:
     > *"세션 저장이 비활성입니다. cwd 가 `munto-dev-assistant/projects/{프로젝트명}/` 일 때만 자동 저장됩니다."*

4. **`{slack-handle}` 추출 (세션 저장 활성 시만)** — `munto-spec-writer` 와 동일 우선순위. 명시 인자 → `git config user.email` 의 `@` 앞 → `$USER` → 사용자 1 회 질문. 결과는 kebab-case slugify. *상세는 `munto-spec-writer` SKILL.md §"시작 전 준비" 4 참조 (TO-BE §4.7.4 (4))*

## 문서 가져오기

### Notion URL인 경우
Notion MCP `notion-fetch` 도구를 사용합니다.

### 로컬 마크다운 파일인 경우
해당 파일을 읽습니다.

### 입력이 없는 경우
현재 에디터에 열린 파일을 대상으로 합니다.

## 문서 유형 판별

문서 내용을 기반으로 자동 판별합니다:

- **SRS**: `1. Introduction`, `2. Overall Description`, `7. Functional Requirements` 등 챕터 번호 체계가 있으면 SRS
- **One Pager**: `Project Name`, `Business and Marketing Justification`, `Technical Description` 등 고정 항목이 있으면 One Pager

판별이 안 되면 사용자에게 질문합니다.

## 리뷰 실행

문서 유형에 따라 아래 체크리스트를 적용합니다.

---

### SRS 리뷰 체크리스트

#### A. 항목 구조 완전성
- [ ] 1장~7장의 모든 고정 항목이 존재하는가
- [ ] 해당 없는 항목에 `None`, `N/A`, `N/A(기존과 동일)` 처리가 되어 있는가
- [ ] 상위 항목이 `N/A`로 처리된 경우, 하위 항목 전체가 해당 없음으로 간주 (하위 항목 누락으로 판단하지 않음)
- [ ] 항목이 임의로 추가/삭제/번호 변경되지 않았는가
- [ ] 6.3.5 Remaining Attributes 아래에 Testability 등 서브섹션 추가는 정상 (항목 임의 추가로 판단하지 않음)

#### B. 기호·수식 선행 정의
- [ ] 문서에서 수학 기호·변수가 처음 등장하는 위치에서 설명 또는 `(1.4 참조)`가 있는가
- [ ] 1.4 용어표에 문서 내 모든 기호·변수가 정의되어 있는가

#### C. 1.2 Product Scope
- [ ] 비즈니스 배경(현재 문제점 + 목표 + 기대효과)이 서술되어 있는가
- [ ] In/Out of Scope 나열식이 아닌 서술형으로 작성되어 있는가
- [ ] 개별 요구사항을 열거하지 않고 핵심 역할과 경계만 서술했는가

#### D. 섹션 간 일관성
- [ ] 2.4 Product Functions ↔ 7장 대분류가 1:1 매핑되는가
- [ ] 1.3에서 정의한 P1/P2/P3 기준이 7장 전체에 일관되게 적용되었는가
- [ ] 2.7 Phase별 분류가 P1/P2/P3와 일치하는가
- [ ] 7장에서 "6.x 참조"로 표시한 섹션이 실제 6장에 존재하는가

#### E. DB 스키마 완전성
- [ ] 신규 테이블에 Prisma 모델 수준의 정의가 있는가 (컬럼명, 타입, 기본값, nullable, 인덱스, relation)
- [ ] 기존 테이블 변경 시 타입·기본값·nullable·마이그레이션 전략이 명시되어 있는가
- [ ] ERD 링크(PostgreSQL 형식)가 4.1 또는 6.4에 포함되어 있는가

#### F. API 스키마 완전성
- [ ] 모든 API에 request/response JSON 스키마가 있는가
- [ ] 상태 코드(200, 400, 401, 403, 404, 500 등)가 정의되어 있는가
- [ ] 에러 코드 + 메시지 키가 정의되어 있는가
- [ ] Swagger(OpenAPI) 형식 링크가 4.1에 포함되어 있는가

#### G. 측정 가능성
- [ ] 모호한 표현이 없는가 (빠르게, 적절히, 충분히, 상당히, 효율적으로, 안정적으로)
- [ ] 주체가 불명확한 수동태가 없는가 ("처리된다", "저장된다")
- [ ] 성능 수치가 구체적인가 (예: "95%의 요청이 300ms 이내")

#### H. TBD 처리
- [ ] TBD 항목에 담당자, 결정 시점, 관련 이슈 링크가 모두 있는가

#### I. 외부 링크
- [ ] Figma, Notion, GitHub, Jira 링크가 존재하고 형식이 올바른가

---

### One Pager 리뷰 체크리스트

#### A. 항목 구조 완전성
- [ ] 8개 고정 항목이 모두 존재하는가 (Project Name, Date, Submitter Info, Project Description, Business and Marketing Justification, Risk Assessment, Resource and Scheduling Details, Technical Description)
- [ ] 항목이 임의로 추가/삭제/변경되지 않았는가

#### B. Project Description
- [ ] 2~3문장으로 간결하게 요약되어 있는가
- [ ] 기술적 상세 없이 비즈니스 언어로 작성되었는가

#### C. Business and Marketing Justification
- [ ] 비즈니스 목표가 명시되어 있는가
- [ ] 기대 효과가 구체적인가 (모호한 표현 없이)

#### D. Risk Assessment
- [ ] 기술적 리스크가 식별되어 있는가
- [ ] 일정 리스크가 식별되어 있는가
- [ ] 각 리스크에 대응 방안이 있는가

#### E. Resource and Scheduling Details
- [ ] 필요 인력(역할/인원)이 명시되어 있는가
- [ ] 예상 일정(시작~종료)이 있는가
- [ ] 마일스톤이 정의되어 있는가

#### F. Technical Description
- [ ] 기술 스택이 명시되어 있는가
- [ ] 아키텍처 개요가 있는가
- [ ] API(Swagger 형식) 링크가 포함되어 있는가
- [ ] ERD(PostgreSQL 형식) 링크가 포함되어 있는가

#### G. 측정 가능성
- [ ] 모호한 표현이 없는가 (빠르게, 적절히, 충분히, 상당히, 효율적으로, 안정적으로)
- [ ] 주체가 불명확한 수동태가 없는가

## 리포트 출력 형식

```markdown
# [SRS/One Pager] 리뷰 리포트

**문서**: [문서명 또는 URL]
**유형**: SRS / One Pager
**리뷰 기준**: spec-standard.md
**리뷰 일시**: YYYY-MM-DD

## 요약
- 🔴 Critical: N건
- 🟡 Warning: N건
- 🟢 Info: N건

## 상세 결과

### 🔴 Critical
#### [C-001] 제목
- **위치**: 섹션/항목명
- **문제**: 설명
- **기준**: spec-standard.md 규칙 참조
- **수정 제안**: 구체적 수정안

### 🟡 Warning
...

### 🟢 Info
...

## 체크리스트 결과
| 카테고리 | 통과 | 이슈 |
|----------|------|------|
| ... | ✅/❌ | N건 |
```

## 심각도 기준

| 심각도 | 기준 | 예시 |
|--------|------|------|
| 🔴 Critical | 구현/QA/승인 불가 수준 | 항목 누락, DB 스키마 미정의, API 스키마 없음, 섹션 간 불일치 |
| 🟡 Warning | 품질 저하 우려 | 모호한 표현, TBD 불완전, 링크 누락, 1.2 나열식 작성 |
| 🟢 Info | 개선하면 좋은 수준 | 더 나은 표현 제안, 용어 통일, 스타일 개선 |

## 모호한 표현 탐지 패턴

### 모호한 형용사/부사
| 탐지 표현 | 대체 예시 |
|-----------|-----------|
| 빠르게 | 300ms 이내에 |
| 적절히 | [구체적 기준 명시] |
| 충분히 | [수치 명시] |
| 상당히 | [비율/수치 명시] |
| 효율적으로 | CPU 사용률 N% 이하로 |
| 안정적으로 | 가용성 99.9%로 |
| 대량의 | 10만 건 이상의 |
| 다수의 | N명 이상의 |
| 가능한 한 | [구체적 조건 명시] |

### 주체 불명확 수동태
| 탐지 표현 | 대체 예시 |
|-----------|-----------|
| 처리된다 | 서버에서 처리한다 |
| 저장된다 | PostgreSQL에 저장한다 |
| 전송된다 | FCM을 통해 전송한다 |
| 표시된다 | 클라이언트 앱에서 표시한다 |
| 검증된다 | NestJS ValidationPipe로 검증한다 |

## DB/API 스키마 판단 기준

### DB Critical
- 테이블명만 언급하고 컬럼 정의가 없는 경우
- 컬럼명은 있으나 타입이 없는 경우
- 신규 테이블에 Prisma 모델/DDL이 없는 경우
- 기존 테이블에 컬럼 추가하면서 nullable/기본값이 없는 경우

### API Critical
- API URL만 나열하고 request/response가 없는 경우
- "구현 완료"라고 표시했으나 스키마가 문서에 없는 경우
- 상태 코드 정의가 없는 경우

---

## 세션 저장 — 자동 (a) *[2026-05-27 신설 — TO-BE §2.3 ⑧ + §4.7.4]*

> `spec-reviewer` 응답 수신 후 메인이 *팀 공유 영구 기록* 으로 `sessions/spec-review-{YYYY-MM-DD}-{문서명}-{slack-handle}.md` 자동 생성.
> *시작 전 준비 3* 에서 *세션 저장 활성* 으로 판정된 경우에만 수행.
> **작성자별 파일 분리 정책 (옵션 α)** — 같은 문서를 *다른 리뷰어* 가 같은 날 리뷰해도 *다른 파일* 에 박힘. `{slack-handle}` 은 *시작 전 준비 4* 의 추출 결과 사용.

### 자동 박을 내용 (최소 양식 — TO-BE §4.7.4 (2))

```markdown
# Spec 리뷰 — {YYYY-MM-DD} — {문서명} — @{slack-handle}

| 항목 | 값 |
|------|------|
| 리뷰어 Slack 핸들 | {slack-handle} *(파일명과 동일)* |
| 대상 문서 경로 | {예: munto-backend/docs/specs/{기능명}/SRS.md} |
| 문서 유형 | SRS \| One Pager |
| 리뷰 일시 | {YYYY-MM-DD HH:MM} |
| spec-reviewer 자동 점검 결과 | 🔴 Critical N / 🟡 Warning N / 🟢 Info N |
| 반영 결정 항목 ID | {예: C-001, C-003, W-002 — 사용자가 *반영* 선택한 것만} |
| 반영 보류·기각 항목 + 사유 | {예: C-002 (기각: 의도된 동작), W-005 (보류: 다음 sprint)} |
| 다음 리뷰 시 우선 점검 항목 | {위 보류 항목 추적용} |
| (선택) 인계 사항 | {다른 사람에게 이어주는 사람이 있다면 한 줄 메모} |
```

### 박을 위치

- 활성 시: `{cwd}/sessions/spec-review-{YYYY-MM-DD}-{문서명-slug}-{slack-handle}.md`
  - 같은 사람이 같은 날 같은 문서 *재리뷰* 시 파일 끝에 `## 재리뷰 {N}회차` 섹션 *append*
  - 같은 날 *다른 리뷰어* 의 같은 문서 리뷰는 *별도 파일* (`spec-review-{date}-{doc}-{다른-handle}.md`) — race condition·merge conflict 0
- `{문서명-slug}` 은 대상 문서 파일명에서 확장자 제외한 부분 (kebab-case)

### 자동 박지 *않는* 케이스

- ❌ 리뷰가 *시작만* 되고 spec-reviewer 응답을 못 받은 경우 (BLOCKER 발생) → 박지 않음
- ❌ 사용자가 *특정 섹션 한 군데만* 리뷰 요청한 *짧은 케이스* (PM 모드 예외) → 박지 않음

---

## baseline 동결 점검 *[2026-05-27 신설 — TO-BE §4.7.4]*

사용자가 다음 신호를 발신하면 메인이 `spec-baseline-handoff.md` 존재 여부 점검:

- *"baseline 잡자"* / *"v1.0 동결"* / *"PHASE 1 GATE 통과"* / *"이제 IP 작성 단계로"*
- 또는 본 호출의 spec-reviewer 결과가 *🔴 Critical = 0 + 🟡 Warning ≤ N (낮음)* + 사용자가 *"통과"* 의사 표명

### 점검 동작

1. `{cwd}/sessions/spec-baseline-handoff.md` 파일 존재 여부 확인
2. 존재 + 8 개 필수 항목 모두 채워짐 (TO-BE §4.7.4 (2) `spec-baseline-handoff.md` 행 참조):
   - baseline v1.0 동결 일자
   - 문서 경로 4 종 (SRS·DBML·Swagger·UI/TCL)
   - 각 문서의 동결 SHA
   - 핵심 아키텍처 결정 3~5 개 (대안 검토 박스 요약)
   - 미해결 TBD 잔여 목록
   - PHASE 2 진입 시 ip-writer 가 우선 참조해야 할 5 가지 컨텍스트
   - Owner 사인
   - 분석 아키텍트 사인

### 미존재·미충족 시 → **🔴 BLOCKER 리포트**

```
🔴 BLOCKER — Spec baseline 동결 차단

projects/{프로젝트명}/sessions/spec-baseline-handoff.md 가 {없음 | 필수 항목 N개 누락} 입니다.

본 파일은 *PHASE 2 의 ip-writer 가 IP 초안 생성 시 우선 참조* 하는 단일 컨텍스트입니다 (TO-BE §4.7.4 (2)(6)).
파일이 없거나 미완성이면 다음 단계 (dev-chain-implementation-plan) 가 *왜* 를 모르고 IP 를 작성하게 됩니다.

다음 중 하나를 선택하세요:
  (i) 본 파일을 Owner 가 직접 작성·인수자 사인 후 재호출
  (ii) baseline 동결 보류 — 사용자가 *명시적으로* "spec-baseline-handoff.md 없이 진행" 선택 시에만 통과 (권장 안 함)
```

### 자동 작성하지 않는 이유

§4.7.4 (1) 매트릭스의 *spec-baseline-handoff.md* 는 *유일하게 수동 의무* — *Owner 의 사람 책임* 으로 박혀 있어야 다음 단계가 신뢰할 수 있다. 자동 작성하면 *형식적 통과* 가 되어 본 정책의 목적 (PHASE 1 → PHASE 2 *왜* 인계) 이 무력화됨.

---

## 주의사항

- 리뷰 기준은 반드시 `document/spec-standard.md`에서 가져옵니다. 기준을 임의로 추가하지 않습니다
- 문서의 항목 구조(섹션 번호, 항목명)가 변경되었는지 여부는 가장 먼저 확인합니다
- **상위 항목이 `N/A`로 처리된 경우, 하위 항목 전체가 해당 없음으로 간주합니다. 이를 하위 항목 누락으로 판단하지 않습니다** (예: `3.1 Operating Environment: N/A`이면 3.1.1, 3.1.2를 개별 기재하지 않아도 됨)
- **6.3.5 Remaining Attributes**는 6.3.1~6.3.4에서 다루지 않은 나머지 품질 특성(Correctness, Efficiency, Flexibility, Interoperability, Reusability, Testability, Usability 등)을 **선택적으로** 기술하는 항목이다. 작성자가 Testability 등을 6.3.5 아래에 서브섹션으로 추가하는 것은 정상이며, 항목 임의 추가나 번호 변경으로 판단하지 않는다
- 모호한 표현 탐지 시 대체 표현을 반드시 제안합니다
- DB/API가 표에만 나열되고 스키마가 없는 경우 Critical로 분류합니다
- **세션 저장은 *자동 동작* 입니다** — 사용자가 별도 요청하지 않아도 *시작 전 준비 3* 에서 활성 판정 시 수행
- **baseline 동결 점검은 *자동 트리거* 입니다** — 사용자의 baseline 통과 신호 발신 시 무조건 점검. 누락 시 🔴 BLOCKER. *Owner 의 사람 작성* 으로만 해소 가능
