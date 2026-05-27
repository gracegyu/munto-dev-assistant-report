<!--
⚠️ 본 파일은 *적용 대기 본문* 입니다.

- 운영 레포 위치 (실제 적용 대상): /Users/gracegyu/Documents/GitMunto/munto-dev-assistant/.agents/skills/common/docs/munto-spec-writer/SKILL.md
- 본 파일 위치 (기획 미러, 적용 대기):    munto-dev-assistant-report/munto-dev-assistant/skills/munto-spec-writer/SKILL.md

원본 대비 *세션 저장 단계 (§"세션 저장 — 자동 (a)")*만 신설했습니다. 그 외 본문은 동일.
적용 시점은 ip-standard.md / TO-BE §4.7.4 정책이 운영 레포에 일괄 이관되는 시점입니다.
변경 근거: TO-BE §4.7.4 (1)(2)(5) — (a) 스킬 호출 자동 저장.
-->

---
name: "munto-spec-writer"
description: "Writes Munto spec docs (SRS, Engineering One Pager) following the internal standard (spec-standard.md). Triggers: \"작성\", \"쓰기\", \"write\", \"스펙 작성\", \"SRS 작성\", \"원페이저 작성\", \"문서 작성\", \"SRS 써줘\", \"원페이저 써줘\", \"스펙 써줘\"."
metadata:
  last_modified: "2026-05-27"
  revision: "세션 저장 단계 신설 — (a) 스킬 호출 자동 저장. 작성자별 파일 분리 정책 (옵션 α): cwd 가 projects/{프로젝트명}/ 이면 sessions/spec-session-{date}-{author-id}.md 에 자동 append. {author-id} 입력 = 호출 시 명시 인자 우선, 미명시 시 세션 첫 호출에 1 회 질문 + 캐싱 (자동 추출 폐기 — git config 가 회사 이메일이 아닌 케이스 다수로 검증 실패). TO-BE §2.3 ⑧ + §4.7.4 (1)(2)(4)(5) 정책 반영."
---

# 스펙 문서 작성

## 시작 전 준비

1. `document/spec-standard.md`를 읽어 작성 기준을 로드합니다
2. 문서 유형에 따라 해당 템플릿을 로드합니다:
   - SRS → `document/spec-templates/SRS_v3.3_template.md`
   - One Pager → `document/spec-templates/OnePager_v1.0_template.md`
3. **cwd 점검 (세션 저장 활성 여부 결정)**:
   - cwd 가 `munto-dev-assistant/projects/{프로젝트명}/` 인지 검사
   - 맞으면: `sessions/` 폴더 자동 생성, *세션 저장 활성* (이후 §"세션 저장" 단계 자동 수행)
   - 아니면: 사용자에게 1 회 경고 후 작업 계속. 메시지:
     > *"세션 저장이 비활성입니다. cwd 가 `munto-dev-assistant/projects/{프로젝트명}/` 일 때만 자동 저장됩니다. 활성화하려면: (i) cwd 이동 후 재호출 (ii) `프로젝트명=…` 인자 명시 (iii) 그대로 진행 (세션 저장 안 함)"*
   - 사용자가 (ii) 를 선택했고 `projects/{프로젝트명}/` 폴더가 *존재* 하면 절대 경로로 박기 활성

4. **`{author-id}` 입력 (세션 저장 활성 시만)** — *팀이 합의한 작성자 식별 문자열*. Munto 권장 = Slack 멘션 핸들 (`@gyuhyeon.jeon` 의 `gyuhyeon.jeon`). 입력 정책 2 단계:
   - (1) **호출 인자에 `author=gyuhyeon.jeon` 명시** → 그대로 사용. **권장 디폴트**
   - (2) (미명시 시) 세션 첫 호출에 *1 회만* 질문: *"본 세션의 `{author-id}` 를 입력하세요 (예: `gyuhyeon.jeon`). 팀 합의 포맷은 Munto Slack 핸들"*. **답한 값을 본 세션 동안 캐싱** — 같은 세션 내 재질문 금지
   - **자동 추출 (`git config user.email`·`$USER`) 폐기 사유**: 다중 회사 이메일 잔존·오픈소스용 별도 계정·PC 계정명 불일치 등으로 *사용자 의도와 어긋날 확률이 높음* (TO-BE §4.7.4 (4))
   - 결과 검증: *사용자 입력 그대로 박음 — slugify 안 함* (팀 합의 포맷 보존). 권장 패턴 `^[a-z0-9._-]+$`
   - 빈 값 입력 시 *세션 저장 자체 스킵 + 경고 1 회* (익명 산출물은 인계 가치 0). `unknown` 으로 박지 않음

## 문서 유형 판별

사용자 요청에서 유형을 판별합니다:

- **SRS**: "SRS", "상세 스펙", "요구사항 명세" 등의 키워드
- **One Pager**: "원페이저", "one pager", "요약", "착수 문서" 등의 키워드

판별이 안 되면 사용자에게 질문합니다.

## 정보 수집

### Notion URL이 제공된 경우
Notion MCP `notion-fetch`로 내용을 가져와 정보를 추출합니다.

### 로컬 파일이 제공된 경우
해당 파일을 읽어 정보를 추출합니다.

### 텍스트 설명이 제공된 경우
설명에서 필요한 정보를 추출하고, 부족한 부분을 질문합니다.

### 입력이 부족한 경우
필수 정보를 대화형으로 수집합니다.

## 작성 실행

문서 유형에 따라 아래 항목 구조와 규칙을 적용합니다.

---

### SRS 작성

#### 항목 구조 (변경 금지)

```
1. Introduction (개요)
   1.1 Purpose (목표)
   1.2 Product Scope (범위)
   1.3 Document Conventions (문서규칙)
   1.4 Terms and Abbreviations (정의 및 약어)
   1.5 Related Documents (관련문서)
   1.6 Intended Audience and Reading Suggestions (대상 및 읽는 방법)
   1.7 Project Output (프로젝트 산출물)
       1.7.1 Output Format (산출물 형태)
       1.7.2 Output Name and Version (산출물명(가칭) 및 버전)
       1.7.3 Patent Information (특허 출원 유무 및 내용)

2. Overall Description (전체 설명)
   2.1 Product Perspective (제품 조망)
   2.2 Overall System Configuration (전체 시스템 구성)
   2.3 Overall Operation (전체 동작방식)
   2.4 Product Functions (제품 주요 기능)
   2.5 User Classes and Characteristics (사용자 계층과 특징)
   2.6 Assumptions and Dependencies (가정과 종속 관계)
   2.7 Apportioning of Requirements (단계별 요구사항)
   2.8 Backward compatibility (하위 호환성)

3. Environment (환경)
   3.1 Operating Environment (운영 환경)
       3.1.1 Hardware Environment (하드웨어 환경)
       3.1.2 Software Environment (소프트웨어 환경)
   3.2 Product Installation and Configuration (제품 설치 및 설정)
   3.3 Distribution Environment (배포 환경)
       3.3.1 Master Configuration (마스터 구성)
       3.3.2 Distribution Method (배포 방법)
       3.3.3 Patch/Update Method (패치와 업데이트 방법)
   3.4 Development Environment (개발 환경)
       3.4.1 Hardware Environment (하드웨어 환경)
       3.4.2 Software Environment (소프트웨어 환경)
   3.5 Test Environment (테스트 환경)
       3.5.1 Hardware Environment (하드웨어 환경)
       3.5.2 Software Environment (소프트웨어 환경)
   3.6 Configuration Management (형상관리)
       3.6.1 Location of Outputs (산출물 위치)
       3.6.2 Build Environment (빌드 환경)
   3.7 Bugtrack System (버그트래킹)
   3.8 Other Environment (기타 환경)

4. External Interface Requirements (외부 인터페이스 요구사항)
   4.1 System Interfaces (시스템 인터페이스)
   4.2 User Interface (사용자 인터페이스)
   4.3 Hardware Interface (하드웨어 인터페이스)
   4.4 Software Interface (소프트웨어 인터페이스)
   4.5 Communication Interface (통신 인터페이스)
   4.6 Other Interface (기타 인터페이스)

5. Performance requirements (성능 요구사항)
   5.1 Throughput (작업처리량)
   5.2 Concurrent Session (동시 세션)
   5.3 Response Time (대응시간)
   5.4 Performance Dependency (성능 종속 관계)
   5.5 Other Performance Requirements (기타 성능 요구사항)

6. Non-Functional Requirements (기능 이외의 요구사항)
   6.1 Safety requirements (안전성 요구사항)
   6.2 Security Requirements (보안 요구사항)
   6.3 Software System Attributes (소프트웨어 시스템 특성)
       6.3.1 Availability (가용성)
       6.3.2 Maintainability (유지보수성)
       6.3.3 Portability (이식성)
       6.3.4 Reliability (신뢰성)
       6.3.5 Remaining Attributes (나머지 특성)
   6.4 Logical Database Requirements (데이터베이스 요구사항)
   6.5 Business Rules (비즈니스 규칙)
   6.6 Design and Implementation Constraints (설계와 구현 제한사항)
       6.6.1 Standards Compliance (표준준수)
       6.6.2 Other Constraints (기타 제한 사항)
   6.7 Memory Constraints (메모리 제한 사항)
   6.8 Operations (운영 요구사항)
   6.9 Site Adaptation Requirements (사이트 적용 요구사항)
   6.10 Internationalization Requirements (다국어 지원 요구사항)
   6.11 Unicode Support (유니코드 지원)
   6.12 64bit Support (64비트 지원)
   6.13 Certification (제품 인증)
   6.14 Field Test (필드 테스트)
   6.15 Other Requirements (기타 요구 사항)

7. Functional Requirements (기능요구사항)
   7.1 대분류 기능1
       7.1.1 ...
       7.1.1.1 ...
   7.2 대분류 기능2
   ...
```

#### SRS 핵심 작성 규칙

- **1.2 Product Scope**: 서술형 작성. In/Out of Scope 나열식 금지
- **2.4 ↔ 7장 매핑**: 2.4 Product Functions 항목과 7장 대분류가 1:1 매핑 필수
- **7장 세분화**: `7.1` → `7.1.1` → `7.1.1.1`, 각 항목은 1~2일 작업량, 우선순위 `(P1)/(P2)/(P3)` 표시
- **해당 없는 항목**: `None` / `N/A` / `N/A(기존과 동일)` 처리 (삭제 금지)
- **상위 `N/A`**: 하위 항목 전체를 개별 기재하지 않아도 됨
- **기호·수식**: 1.4 용어표에 모두 정의 필수

#### SRS 자체 검증 체크리스트

- [ ] 1장~7장의 모든 고정 항목이 존재하는가
- [ ] 해당 없는 항목에 `None`/`N/A`/`N/A(기존과 동일)` 처리가 되어 있는가
- [ ] 1.2가 서술형이며 In/Out of Scope 나열식이 아닌가
- [ ] 2.4 Product Functions ↔ 7장 대분류가 1:1 매핑되는가
- [ ] 1.3에서 정의한 P1/P2/P3 기준이 7장 전체에 적용되었는가
- [ ] 수학 기호가 1.4 용어표에 모두 정의되어 있는가
- [ ] 신규 테이블에 Prisma 모델 수준의 정의가 있는가
- [ ] API에 request/response 스키마, 상태 코드, 에러 코드가 있는가
- [ ] 4.1에 Swagger/ERD 링크가 포함되어 있는가

---

### One Pager 작성

#### 항목 구조 (변경 금지) — 8개 고정

```
Project Name
Date
Submitter Info
Project Description
Business and Marketing Justification
Risk Assessment
Resource and Scheduling Details
Technical Description
```

#### 항목별 작성 규칙

| 항목 | 작성 규칙 |
|------|-----------|
| **Project Name** | 프로젝트 공식 명칭 (가칭 포함 가능) |
| **Date** | 문서 작성일 (YYYY-MM-DD) |
| **Submitter Info** | 작성자 이름, 소속 팀, 연락처 |
| **Project Description** | 2~3문장 요약. 기술적 상세 없이 비즈니스 언어로 작성 |
| **Business and Marketing Justification** | 비즈니스 목표, 기대 효과, 시장 기회를 구체적으로 |
| **Risk Assessment** | 기술적·일정·외부 의존 리스크와 각 대응 방안 |
| **Resource and Scheduling Details** | 필요 인력(역할/인원), 예상 일정(시작~종료), 마일스톤 |
| **Technical Description** | 기술 스택, 아키텍처 개요, 주요 기술적 결정. **API(Swagger 형식)와 ERD(PostgreSQL 형식) 링크 필수** |

#### One Pager 출력 형식

```markdown
# Engineering One Pager Template v1.0

create by: 전규현

Project Name : [프로젝트명]
Date : YYYY-MM-DD
Submitter Info : [작성자 정보]
Project Description : [2~3문장 요약]
Business and Marketing Justification : [비즈니스 정당성]
Risk Assessment : [리스크 및 대응 방안]
Resource and Scheduling Details : [인력/일정/마일스톤]
Technical Description : [기술 스택, 아키텍처, API/ERD 링크]
```

#### One Pager 자체 검증 체크리스트

- [ ] 8개 고정 항목이 모두 존재하는가
- [ ] Project Description이 비즈니스 언어 2~3문장인가
- [ ] Technical Description에 API(Swagger) 링크가 있는가
- [ ] Technical Description에 ERD(PostgreSQL) 링크가 있는가
- [ ] Risk Assessment에 리스크별 대응 방안이 있는가
- [ ] Resource and Scheduling Details에 마일스톤이 있는가

## 절대 불변 규칙

### 항목 구조 보존
- 템플릿의 항목 구조는 **절대 변경 불가**
- 항목 추가, 삭제, 이름 변경, 번호 변경 금지
- 해당 없는 항목은 삭제하지 않고 `None`, `N/A`, `N/A(기존과 동일)` 처리

### One Pager 고정 항목 (8개)
```
Project Name
Date
Submitter Info
Project Description
Business and Marketing Justification
Risk Assessment
Resource and Scheduling Details
Technical Description
```

### SRS 고정 항목 (1장~7장)
```
1. Introduction (개요)
   1.1 ~ 1.7 (1.7.1 ~ 1.7.3 포함)
2. Overall Description (전체 설명)
   2.1 ~ 2.8
3. Environment (환경)
   3.1 ~ 3.8 (하위 항목 포함)
4. External Interface Requirements (외부 인터페이스 요구사항)
   4.1 ~ 4.6
5. Performance requirements (성능 요구사항)
   5.1 ~ 5.5
6. Non-Functional Requirements (기능 이외의 요구사항)
   6.1 ~ 6.15 (하위 항목 포함)
7. Functional Requirements (기능요구사항)
   7.1 ~ (프로젝트에 따라 확장)
```

## 작성 품질 기준

### 금지 표현
| 금지 표현 | 대체 방법 |
|-----------|-----------|
| 빠르게 | 300ms 이내에 |
| 적절히, 충분히 | 구체적 수치 명시 |
| 효율적으로 | CPU 사용률 N% 이하로 |
| 안정적으로 | 가용성 99.9%로 |
| 처리된다 | 서버에서 처리한다 |
| 저장된다 | PostgreSQL에 저장한다 |

### DB 스키마
신규 테이블은 Prisma 모델 수준으로 정의합니다 (컬럼명, 타입, 기본값, nullable, 인덱스, relation).

### API 스키마
모든 API는 Swagger/OpenAPI 수준으로 정의합니다 (HTTP Method+URL, Request/Response, 상태 코드, 에러 코드).

**날짜/시간 타입 컨벤션**:

| 규칙 | 설명 |
|------|------|
| 모든 datetime 필드 | ISO 8601 문자열 ❌ → **Unix Timestamp milliseconds** (`number`) 사용 |
| Swagger 타입 정의 | `type: integer`, `format: unixTimestamp`, example: `1737354000000` |
| nullable 시간 필드 | `nullable: true`, `type: integer` |
| **초 단위 금지** | `Math.floor(date.getTime() / 1000)` ❌ — 반드시 ms (`date.getTime()`) 사용 |

**커서 기반 페이지네이션 컨벤션**:

목록 API는 오프셋이 아닌 커서 기반 페이지네이션을 사용합니다.

| 구분 | 필드 | 타입 | 설명 |
|------|------|------|------|
| Query | `count` | `integer` | 조회 개수, 기본값 20 |
| Query | `after` | `string` (optional) | 다음 페이지 커서 (`nextCursor` 값) |
| Query | `before` | `string` (optional) | 이전 페이지 커서 (`prevCursor` 값) |
| Response | `data` | `T[]` | 데이터 배열 (없으면 빈 배열 `[]`) |
| Response | `meta.nextCursor` | `string \| null` | 마지막 페이지면 `null` |
| Response | `meta.prevCursor` | `string \| null` | 데이터 없으면 `null` |

**HTTP 상태 코드 컨벤션** (munto-backend / dating-backend 공통):

| 상황 | 상태 코드 |
|------|----------|
| 본인 리소스가 없음 (미설정) | `404` — 예: 인증 정보 미설정, 프로필 미작성 |
| 타인 리소스를 조회했는데 없음 | `404` — 예: 존재하지 않는 소셜링 ID |
| soft delete된 리소스 조회 | `404` |
| 존재하지만 비어있는 목록 | `200` + 빈 배열 |
| 리소스 존재 여부 표현 | `404` 사용, `200 + boolean` 플래그 금지 |

### TBD
담당자 + 결정 시점 + 이슈 링크가 모두 있어야 허용합니다.

## 자체 검증

작성 완료 후 `document/spec-standard.md`의 "섹션 간 일관성 체크" 항목을 실행합니다:

- 2.4 ↔ 7장 매핑 확인 (SRS)
- P1/P2/P3 일관성 확인 (SRS)
- API/ERD 링크 포함 확인
- 모호한 표현 탐지
- 항목 구조 완전성 확인

---

## 세션 저장 — 자동 (a) *[2026-05-27 신설 — TO-BE §2.3 ⑧ + §4.7.4]*

> 작성 작업이 끝나면 *팀 공유 영구 기록* 으로 `sessions/spec-session-{YYYY-MM-DD}-{author-id}.md` 에 자동 append.
> *시작 전 준비 3* 에서 *세션 저장 활성* 으로 판정된 경우에만 수행. 비활성이면 본 단계 *스킵* (사용자에게 별도 안내 없음).
> **작성자별 파일 분리 정책 (옵션 α)** — 멀티 작성자 동시 작업 시 race condition·git merge conflict 0. `{author-id}` 은 *시작 전 준비 4* 의 추출 결과 사용.

### 자동 박을 내용 (최소 양식 — TO-BE §4.7.4 (2))

```markdown
## {HH:MM} — munto-spec-writer 호출 {N}회차

| 항목 | 값 |
|------|------|
| 작성자 ID (`{author-id}`) | {author-id} *(파일명과 동일 — 메타 헤더에 명시. Munto 권장 = Slack 멘션 핸들)* |
| 문서 유형 | SRS \| One Pager |
| 작업 대상 | {Notion URL or 로컬 파일 경로} |
| 결과 산출물 경로 | {예: munto-backend/docs/specs/{기능명}/SRS.md} |
| 이번 세션 *추가·수정한 섹션 ID* | {예: 1.2, 2.4, 7.1.1 — 변경된 섹션만} |
| 제기된 의문·미해결 TBD | {목록 — 없으면 "없음"} |
| 다음 세션 첫 질문 | {다음 세션 시작 시 사용자에게 물을 1 문장} |
| 자체 검증 결과 | {SRS 9 가지 또는 One Pager 6 가지 통과 N개 / 미통과 N개} |
| (선택) 대안 검토 발생 | {§4.7.3 대안 검토 박스를 추가한 항목 ID — 없으면 생략} |
```

### 박을 위치

- 활성 시: `{cwd}/sessions/spec-session-{YYYY-MM-DD}-{author-id}.md`
  - 같은 날 *같은 사람* 의 같은 파일이 *이미 있으면* 파일 끝에 새 섹션 *append*
  - 같은 날 *같은 사람* 의 파일이 *없으면* 신규 생성. 파일 헤더:
    ```markdown
    # Spec 작성 세션 — {YYYY-MM-DD} — @{author-id}

    > 본 파일은 `munto-spec-writer` 가 자동 박은 *팀 공유 영구 기록* 입니다 (TO-BE §2.3 ⑧ + §4.7.4 (1)(2)).
    > AI 도구 raw 세션 (`~/.claude/`) 과 다릅니다 — 본 파일은 *팀이 다음 단계에서 참조* 합니다.
    > **작성자별 분리 정책** — 다른 사람의 같은 날 작업은 `spec-session-{date}-{다른-handle}.md` 에 따로 박힙니다. 시간순 통합이 필요하면 `cat sessions/spec-session-{date}-*.md | sort`.

    ```
- 호출자 (`프로젝트명=` 인자 명시) 가 *절대 경로* 를 지정한 경우: 해당 경로 사용

### 자동 박지 *않는* 케이스 (안티 패턴 차단)

- ❌ 문서 작성을 *시작만* 하고 *작성 결과* 가 없는 경우 (사용자가 입력만 주고 작성 미실행) → 박지 않음 (노이즈)
- ❌ 사용자가 *명시적으로* "이번 호출 세션 저장 스킵" 요청 → 박지 않음
- ❌ cwd 가 *프로젝트 폴더가 아니고* 사용자가 `프로젝트명=` 인자도 안 준 경우 → 박지 않음 (이미 *시작 전 준비 3* 에서 경고했음)

### baseline 동결 시점의 *별도 산출물 안내*

작성 완료 후 *Spec baseline v1.0 동결이 임박했다고 판단되면* (= 사용자가 "이제 baseline 잡자" / "v1.0 동결" / "PHASE 1 GATE 통과" 같은 의사 표현) 다음 메시지를 *반드시* 출력:

```
⚠️ Spec baseline v1.0 동결 직전입니다.
다음 단계로 진입하기 전에 다음 파일을 *Owner 가 직접* 작성해주세요:
  → projects/{프로젝트명}/sessions/spec-baseline-handoff.md

본 파일은 *ip-writer (dev-chain-implementation-plan 스킬) 가 IP 초안 생성 시 우선 참조* 합니다.
최소 양식: TO-BE §4.7.4 (2) 의 spec-baseline-handoff.md 행 참조.
```

> **이 파일은 자동 생성하지 않는다** — TO-BE §4.7.4 (1) 매트릭스에서 *유일하게 수동 의무* 인 산출물. *Owner 의 사람 책임* 으로 박혀 있어야 다음 단계 ip-writer 가 신뢰할 수 있다.

## 주의사항

- 작성 기준은 반드시 `document/spec-standard.md`에서 가져옵니다. 기준을 임의로 추가하지 않습니다
- 템플릿의 가이드 텍스트(영어 설명문)는 최종 문서에 포함하지 않습니다
- 상위 항목이 `N/A`이면 하위 항목 전체를 해당 없음으로 처리합니다
- 6.3.5 Remaining Attributes 아래에 Testability 등 서브섹션 추가는 허용합니다
- **세션 저장은 *자동 동작* 입니다** — 사용자가 별도 요청하지 않아도 *시작 전 준비 3* 에서 활성 판정 시 수행. 비활성 시 *경고 1 회만* 출력하고 작업 계속.
