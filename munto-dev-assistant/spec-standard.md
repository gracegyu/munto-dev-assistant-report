# 문토 스펙 문서 작성 표준

> 문토 개발팀이 사용하는 두 가지 스펙 문서 형식의 작성 지침입니다.
> 각 문서의 항목 구조는 절대 변경, 추가, 삭제할 수 없습니다.

---

## 목차

- [문서 종류](#문서-종류)
- [SRS (Software Requirements Specification)](#srs-software-requirements-specification)
- [Engineering One Pager](#engineering-one-pager)
- [공통 작성 규칙](#공통-작성-규칙)

---

## 문서 종류

| 문서 | 템플릿 | 사용 시점 |
|------|--------|-----------|
| **SRS** | [SRS Template v3.3](https://www.notion.so/munto/SRS-Template-v3-3-1a1e2bc7639d8016b09fdf35efd25257) | 신규 기능/서비스 개발 시 상세 요구사항 명세 |
| **Engineering One Pager** | [One Pager Template v1.0](https://www.notion.so/munto/Engineering-One-Pager-Template-v1-0-1d9e2bc7639d8004af14f464edc7b98f) | 프로젝트 착수 전 경영진/이해관계자 승인용 요약 문서 |

---

## SRS (Software Requirements Specification)

### 항목 구조

아래는 SRS Template v3.3의 **고정 항목**입니다. 항목의 추가, 삭제, 번호 변경은 불가합니다.

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
   7.3 대분류 기능3
   ...
```

### 섹션별 작성 지침

#### 1장 Introduction

| 섹션 | 작성 포인트 |
|------|------------|
| **1.1 Purpose** | 문서 목적과 대상 독자, 제품의 revision/release 번호 명시 |
| **1.2 Product Scope** | 아래 "1.2 작성 가이드" 참조 |
| **1.3 Document Conventions** | 우선순위(P1/P2/P3) 정의, 하위 요구사항 우선순위 상속 여부 명시. **수식/기호가 예시로 등장하는 경우 해당 위치에서 간략 설명하거나 1.4 참조를 명시** |
| **1.4 Terms and Abbreviations** | **이 섹션은 문서의 Glossary(용어집) 부록 역할을 한다.** 본문에 처음 등장하는 **식별자 일체**를 정의한다 — 약어 / 사내 도메인 용어·외래어 / 도메인 코드(상태값·enum) / 수학 기호·변수 등. *(예: `MSA` / `큐레이션`, `센터` / `DRAFT`, `SUBMITTED`, `APPROVED` / `α₀`, `β₀`, `k`, `n`)*. 작성 규칙은 공통 작성 규칙 §"Glossary(용어집) 작성 의무" 참조 |
| **1.5 Related Documents** | Notion 정책문서, Figma, GitHub(API/ERD), Jira 이슈 링크 포함 |
| **1.6 Intended Audience** | 개발자 / 기획자&디자이너 / 운영팀 / 마케팅팀 별 읽기 포인트 제시 |
| **1.7.1 Output Format** | 제품/라이브러리/툴 구분, 플랫폼(앱/백엔드/SDK) 명시 |
| **1.7.2 Output Name and Version** | 산출물명(가칭), 레포지토리명, 초기 버전 명시 |
| **1.7.3 Patent Information** | 특허 출원 가능 아이디어 여부. 해당 없으면 `None` |

**1.2 Product Scope 작성 가이드:**

경영진 요약(executive-level summary) 수준으로 **"왜 이 소프트웨어가 필요한지"**를 중심으로 작성합니다.

1. **비즈니스 배경 (1문단)**: 현재 방식의 문제점과 이번 소프트웨어가 해결하려는 비즈니스 목표·기대 효과를 서술합니다. 기획 문서나 Jira에 이미 배경·기대효과가 정리되어 있으면 핵심만 요약하고 해당 문서를 참조 링크로 첨부합니다
2. **소프트웨어의 핵심 역할과 경계 (1문단)**: 이 소프트웨어가 하는 것과 하지 않는 것을 한두 문단으로 서술합니다. In/Out of Scope를 나열식으로 쓰지 않습니다
3. **In Scope 항목 전체 나열 금지**: 개별 요구사항은 이후 섹션(2장, 7장)에서 상세히 다루므로, 여기서는 전체 목록을 열거하지 않습니다

**Why–What–How 균형 원칙 (모든 섹션 공통, 1.2 에 특히 강하게 적용):**

| 비중 | 위치 | 내용 |
|------|------|------|
| **Why ~30%** | 1.2, 2.1, 7.x 각 기능 도입부 | 왜 만드는가 — 비즈니스 목표·문제·기대 효과 |
| **What ~50%** | 2장, 7장 본문 | 무엇을 만드는가 — 외부에서 본 동작·입출력 |
| **How ~20%** | 4장, 6.6, 7.x 구현 노트 | 어떻게 만드는가 — 핵심 제약·결정 사항만 (상세 구현은 설계 문서 영역) |

- *정확함 ≠ 자세함*: 1.2 는 분량이 적어도 Why 가 누락되면 불완전합니다. 반대로 What/How 가 5 페이지여도 Why 가 1 줄이면 1.2 의 목적을 달성하지 못한 것입니다.
- 1.2 에서 핵심 아키텍처 방향(예: *"베이지안 점수 체계로 전환"*, *"MSA 로 분리"*, *"결제 게이트웨이를 외부 PG 로 위탁"*, *"채팅을 Socket.IO 로 통일"*)을 한 문장이라도 언급하면, **공통 작성 규칙 §"핵심 결정 — 대안 검토 박스"** 에 따라 별도 박스를 추가합니다.

> *아래 예시 도메인: 추천 알고리즘 시스템 (가상)* — 다른 도메인(채팅·결제·이메일 등) 에서도 동일한 *Why → 핵심 역할·경계* 구조로 작성합니다.

```markdown
<!-- ❌ 나쁜 예: In/Out of Scope 나열에 그침 -->
## 1.2 Product Scope
**In Scope:**
- 베이지안 점수 계산
- 사용자 분류
- 추천 큐 관리
- ...

**Out of Scope:**
- 채팅 기능
- 결제 기능

<!-- ✅ 좋은 예: 비즈니스 목표 + 핵심 역할·경계 -->
## 1.2 Product Scope
기존 가중합 방식은 행동 지표 간 변별력이 낮아 좋아요 전환율과의
상관관계가 약하다는 문제가 있다. 본 프로젝트는 베이지안 기반
점수 체계로 전환하여, 추천 정확도를 높이고 좋아요 전환율을
개선하는 것을 목표로 한다. (상세 배경: [Jira PROJ-000] / [기획 문서])

이 소프트웨어는 사용자 행동 데이터를 수집·분석하여 베이지안
점수를 산출하고, 점수 기반으로 추천 후보를 선별·정렬하는
역할을 한다. 채팅, 결제, 프로필 편집 등 기존 서비스 기능은
본 프로젝트의 범위에 포함하지 않는다.
```

#### 2장 Overall Description

| 섹션 | 작성 포인트 |
|------|------------|
| **2.1 Product Perspective** | 기존 제품과의 관계 및 컨텍스트 다이어그램(Mermaid 또는 이미지) |
| **2.2 Overall System Configuration** | 내부 관점의 주요 컴포넌트와 연결 관계 구성도 |
| **2.3 Overall Operation** | 전체 시스템 구성도 기준 동작 원리, 주요 사용자 시나리오 |
| **2.4 Product Functions** | **7장 섹션 제목과 1:1 매핑 필수**. 고수준 요약만 기술 |
| **2.5 User Classes** | 사용자 유형별 특성, 사용 빈도, 기술 수준, 권한 수준 |
| **2.6 Assumptions and Dependencies** | 전제 조건, 선행 프로젝트, 외부 의존성 명시 |
| **2.7 Apportioning of Requirements** | Phase별 기능 분류. P1/P2/P3와 Phase 매핑 |
| **2.8 Backward Compatibility** | 신규 개발이 아닌 경우 마이그레이션 전략 기술. 신규이면 `N/A` |

#### 3장 Environment

기존 문토 환경과 동일한 항목은 `N/A(기존과 동일)` 또는 해당 문서 링크로 대체 가능합니다.

| 섹션 | 작성 포인트 |
|------|------------|
| **3.1.1 Hardware Environment** | 서버 사양, 스토리지, 캐시 서버 등 |
| **3.1.2 Software Environment** | OS, 프레임워크, DB, 언어 버전 등 |
| **3.2 Installation and Configuration** | 설치 과정 요구사항, 기본 설정 요소 |
| **3.3 Distribution Environment** | 배포 방식(CD/웹/앱스토어 등), 패치/업데이트 방법 |
| **3.4 Development Environment** | 개발 환경 하드웨어/소프트웨어 |
| **3.5 Test Environment** | 테스트 환경 하드웨어/소프트웨어 |
| **3.6.1 Location of Outputs** | GitHub 레포지토리 URL |
| **3.6.2 Build Environment** | Node.js 버전, 패키지 매니저(pnpm) 버전 등 |
| **3.7 Bugtrack System** | Jira 프로젝트 키 명시 |

#### 4장 External Interface Requirements

| 섹션 | 작성 포인트 |
|------|------------|
| **4.1 System Interfaces** | 기존에 회사에서 사용하는 외부 시스템과의 연동. **API는 Swagger(OpenAPI) 형식**으로 작성하고 GitHub 레포지토리(`*-docs`) 링크를 포함. **ERD는 PostgreSQL 형식**(`*-docs` 레포지토리)으로 작성하고 링크를 포함 |
| **4.2 User Interface** | Figma 링크. UI 상세는 별도 Figma 문서로 관리 |
| **4.3 Hardware Interface** | 연동하는 하드웨어 기기가 없으면 `None` |
| **4.4 Software Interface** | 연동하는 외부 소프트웨어(SDK, DB, 라이브러리) 명시. **DB 테이블/API를 다루는 경우 아래 "DB 스키마 완전성 규칙"과 "API 스키마 완전성 규칙"을 반드시 준수** |
| **4.5 Communication Interface** | 통신 프로토콜(REST, Socket.IO 등), 보안(TLS), 데이터 형식 |
| **4.6 Other Interface** | 위 항목에 해당하지 않는 기타 인터페이스 |

**4.1 작성 필수 포함 항목:**

```markdown
## 4.1 System Interfaces (시스템 인터페이스)

- API: [swagger.yaml](https://github.com/Munto-dev/{레포명}-docs/blob/main/api/swagger.yaml)
- ERD: [erd.md](https://github.com/Munto-dev/{레포명}-docs/blob/main/database/erd.md)
```

- **API (Swagger/OpenAPI 형식)**: 모든 엔드포인트는 `swagger.yaml` 또는 Swagger UI로 관리합니다. NestJS의 `@ApiProperty`, `@ApiOperation` 데코레이터를 통해 자동 생성하며, `*-docs` 레포지토리에 YAML 파일을 커밋합니다
- **ERD (PostgreSQL 형식)**: 테이블 정의는 PostgreSQL DDL 또는 Mermaid `erDiagram` 형식으로 작성합니다. `*-docs` 레포지토리의 `database/` 디렉터리에 관리합니다

#### 5장 Performance Requirements

전체 기능에 공통 적용되는 성능 요구사항만 기술합니다. 특정 기능의 성능은 7장에 기술합니다.

모든 수치는 구체적으로 측정 가능하게 작성합니다.
- ❌ `사용자가 기다리지 않아야 한다`
- ✅ `95%의 요청이 300ms 이내에 처리되어야 한다`

#### 6장 Non-Functional Requirements

| 섹션 | 작성 포인트 |
|------|------------|
| **6.1 Safety** | 데이터 손실, 결제 안전성, 사용자 보호 관련 요구사항 |
| **6.2 Security** | 인증(JWT), 암호화(TLS), 접근 제어, 보안 인증 |
| **6.3.1 Availability** | 가용성 목표(예: 24/7, 99.9%), 장애 복구 방식 |
| **6.3.2 Maintainability** | 모듈화, 코드 컨벤션, API 문서 자동화 방식 |
| **6.3.3 Portability** | 다른 환경(OS, 플랫폼)으로의 이식 가능성 |
| **6.3.4 Reliability** | MTBF 요구사항, 재시도 메커니즘 |
| **6.3.5 Remaining Attributes** | 6.3.1~6.3.4에서 다루지 않은 나머지 품질 특성 중 해당 프로젝트에 관련 있는 것을 **선택하여** 기술. 후보: Correctness(정확성), Efficiency(효율성), Flexibility(유연성), Interoperability(상호운용성), Reusability(재사용성), Testability(테스트 용이성), Usability(사용성). 관련 없으면 `None` |
| **6.4 Database Requirements** | **PostgreSQL 형식의 ERD** 링크(`*-docs` 레포지토리), 무결성 제약, 데이터 보존 기간 |
| **6.5 Business Rules** | 역할별 수행 가능 기능, 재화 규칙, 매칭 규칙 등 비즈니스 정책 |
| **6.6.1 Standards Compliance** | 준수해야 할 외부 표준/규정 |
| **6.6.2 Other Constraints** | 사용 기술 스택, 코딩 컨벤션, 언어/프레임워크 제약 |
| **6.7 Memory Constraints** | 메모리 제한 사항. 없으면 `None` |
| **6.8 Operations** | 백업/복구 운영 방식, 점검 일정 등 |
| **6.9 Site Adaptation** | 특정 사이트별 초기화 데이터, 환경 설정 |
| **6.10 Internationalization** | 지원 언어 목록 (한국어/영어/일본어 등) |
| **6.11 Unicode Support** | UTF-8 지원 여부, 이모지 처리 여부 |
| **6.12 64bit Support** | 64비트 지원 여부 |
| **6.13 Certification** | 외부 인증 필요 여부 (없으면 `None`) |
| **6.14 Field Test** | 필드 테스트 필요 여부 (없으면 `None`) |
| **6.15 Other Requirements** | 법적 요구사항, 기타 |

#### 7장 Functional Requirements

2장에서 설명한 주요 기능을 **상세하게** 분류합니다.

- 7장의 대분류 제목은 **2.4 Product Functions의 항목과 1:1 매핑**되어야 합니다
- 각 기능 항목은 작업량이 **1~2일** 정도로 산정 가능한 수준으로 세분화합니다
- 기능 번호 체계: `7.1` → `7.1.1` → `7.1.1.1` → `7.1.1.1.1` → `7.1.1.1.1.1`
- 각 기능에 우선순위 `(P1)`, `(P2)`, `(P3)` 표시

---

## Engineering One Pager

### 항목 구조

아래는 Engineering One Pager Template v1.0의 **고정 항목**입니다. 항목의 추가, 삭제, 변경은 불가합니다.

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

### 항목별 작성 지침

| 항목 | 작성 포인트 |
|------|------------|
| **Project Name** | 프로젝트 공식 명칭 (가칭 포함 가능) |
| **Date** | 문서 작성일 (YYYY-MM-DD) |
| **Submitter Info** | 작성자 이름, 소속 팀, 연락처 |
| **Project Description** | 무엇을 만드는지 2~3문장으로 요약. 기술적 상세 없이 비즈니스 언어로 |
| **Business and Marketing Justification** | 왜 이 프로젝트가 필요한지. 비즈니스 목표, 기대 효과, 시장 기회 |
| **Risk Assessment** | 주요 리스크와 대응 방안. 기술적 리스크, 일정 리스크, 외부 의존 리스크 |
| **Resource and Scheduling Details** | 필요 인력(역할/인원), 예상 일정(시작~종료), 마일스톤 |
| **Technical Description** | 기술 스택, 아키텍처 개요, 주요 기술적 결정 사항. **API(Swagger 형식)와 ERD(PostgreSQL 형식) 링크를 이 항목에 반드시 포함** |

**Technical Description 작성 예시 (ERD/API 포함):**

```
Technical Description:

기술 스택: NestJS / PostgreSQL / Redis / Flutter
아키텍처: MSA — 별도 레포지토리(chat-backend)로 독립 운영

API
- Swagger: https://github.com/Munto-dev/{레포명}-docs/blob/main/api/swagger.yaml

ERD
- PostgreSQL DDL: https://github.com/Munto-dev/{레포명}-docs/blob/main/database/erd.md

주요 기술적 결정:
- Socket.IO Redis Adapter를 통한 다중 서버 메시지 동기화
- 통합 JWT Payload로 문토/데이팅 서비스 인증 통합
```

---

## 공통 작성 규칙

### 측정 가능성 원칙

모든 요구사항은 검증 가능해야 합니다.

| ❌ 불명확 표현 | ✅ 명확 표현 |
|--------------|------------|
| 빠르게 처리해야 한다 | 300ms 이내에 응답해야 한다 |
| 적절한 오류 메시지를 표시한다 | 오류 발생 시 오류 코드와 재시도 방법을 한국어로 안내한다 |
| 충분한 보안을 적용한다 | JWT 검증, HTTPS(TLS 1.2+), SQL Injection 방어를 적용한다 |
| 안정적으로 운영한다 | 가용성 99.9% (월 다운타임 43분 이하)를 목표로 한다 |

### 기호·수식 선행 정의 원칙

문서에 수학 기호·수식이 등장하는 SRS(통계·확률·랭킹·머신러닝 관련 도메인)는 **독자가 해당 기호를 처음 만나는 시점에서 의미를 알 수 있어야** 합니다.

> 본 절은 수식이 등장하는 도메인에 한정 — 채팅·결제·이메일 등 *수식이 없는 도메인은 N/A*. 다만 **본문에 처음 등장하는 모든 식별자(약어·상태값·외래어)의 선행 정의 원칙은 §"Glossary(용어집) 작성 의무"** 가 전 도메인 공통입니다.

- 1.3 등 이른 섹션에서 수식 예시로 기호가 등장하면, **해당 위치에서 간략 설명**하거나 `(1.4 참조)` 링크를 명시
- **1.4 용어표에 모든 기호를 정의**: 약어뿐 아니라 수학 변수도 포함
- 7장 등 후반 섹션에서만 상세 정의가 나오는 경우, 1.4 용어표에 간략 정의 + 상세 섹션 참조를 병기

> *아래 예시 도메인: 추천 알고리즘 시스템 (가상)* — 결제 도메인이라면 `α₀, β₀` 대신 `수수료율 r, 할인율 d` 식으로 치환됩니다.

```markdown
<!-- ❌ 나쁜 예: 1.3에서 기호가 설명 없이 등장 -->
우선순위 점수 = α₀ × k + β₀ × n

<!-- ✅ 좋은 예: 기호 등장 시 즉시 설명 또는 참조 -->
우선순위 점수 = α₀ × k + β₀ × n (각 기호 정의는 1.4 참조)

<!-- ✅ 1.4 용어표 -->
| 기호 | 정의 | 상세 |
|------|------|------|
| α₀ | 초기 가중치 (기본값: 0.5) | 7.2.3 참조 |
| β₀ | 보정 계수 (기본값: 0.3) | 7.2.3 참조 |
| k | 활성 사용자 수 | 7.2.3 참조 |
| n | 샘플 크기 | 7.2.3 참조 |
```

### DB 스키마 완전성 규칙

SRS에서 신규 테이블이나 기존 테이블 변경을 언급하는 경우, **다른 개발자가 바로 마이그레이션을 작성할 수 있는 수준**으로 정의해야 합니다.

**신규 테이블 필수 정의 항목:**

| 항목 | 필수 | 설명 |
|------|------|------|
| 컬럼명 | ✅ | camelCase (Prisma 컨벤션) |
| 타입 | ✅ | Prisma 타입 (`String`, `Int`, `DateTime`, `Boolean`, `Enum` 등) |
| 기본값 | ✅ | `@default(...)` 또는 "없음" 명시 |
| nullable 여부 | ✅ | `?` 붙이는지 여부 |
| 제약조건 | ✅ | `@unique`, `@id`, `@relation` 등 |
| 인덱스 | ✅ | `@@index([...])`, `@@unique([...])` |
| relation | ✅ | 다른 모델과의 관계 (`@relation`) |

**기존 테이블 변경 시 필수 정의 항목:**

| 항목 | 필수 | 설명 |
|------|------|------|
| 추가/변경 컬럼명 | ✅ | |
| 타입 | ✅ | |
| 기본값 | ✅ | 기존 데이터 마이그레이션 영향 명시 |
| nullable 여부 | ✅ | |
| 마이그레이션 전략 | ✅ | 기존 row 처리 방법 (예: "기존 row는 `null`로 유지") |

> *아래 예시 도메인: 추천 알고리즘 시스템 (가상)* — 결제 도메인이라면 `PaymentLog`, 채팅이라면 `ChatMessage` 등으로 치환됩니다. 핵심은 *어떤 도메인이든 컬럼·타입·기본값·nullable·인덱스·relation 7 종이 모두 명시*되는 것입니다.

```prisma
// ✅ 좋은 예: 바로 마이그레이션 작성 가능한 수준
model UserAlgorithmScore {
  id        Int      @id @default(autoincrement())
  userId    Int      @unique
  score     Float    @default(0.0)
  updatedAt DateTime @updatedAt
  user      User     @relation(fields: [userId], references: [id])

  @@index([userId])
}

// ❌ 나쁜 예: 표에 컬럼명만 나열
// | 테이블명 | 설명 |
// | UserAlgorithmScore | 사용자 알고리즘 점수 |
```

### API 스키마 완전성 규칙

SRS에서 API(신규 또는 기존)를 언급하는 경우, **구현자와 QA가 바로 작업할 수 있는 수준**으로 정의해야 합니다.

**API 정의 필수 항목:**

| 항목 | 필수 | 설명 |
|------|------|------|
| HTTP Method + URL | ✅ | `POST /api/v1/impressions` |
| Request Body/Query | ✅ | 필드명, 타입, 필수 여부, 제약조건 |
| Response Body | ✅ | 성공 시 JSON 스키마 (필드명, 타입) |
| 상태 코드 | ✅ | 200, 201, 400, 401, 403, 404, 409, 500 등 |
| 에러 코드 | ✅ | 커스텀 에러 코드 + 메시지 키 |
| 인증 | ✅ | `Bearer JWT` 필수 여부 |

> *아래 예시 도메인: 추천 시스템의 노출 기록(impression) API (가상)* — 결제 도메인이라면 `POST /payments`, 채팅이라면 `POST /messages` 등으로 치환됩니다. 핵심은 *어떤 도메인이든 method+URL / request / response / 상태 코드 / 에러 코드 / 인증 6 종이 모두 명시*되는 것입니다.

```yaml
# ✅ 좋은 예: Swagger/OpenAPI 수준
POST /api/v1/impressions:
  summary: 노출 기록 생성
  security:
    - BearerAuth: []
  requestBody:
    required: true
    content:
      application/json:
        schema:
          type: object
          required: [targetUserId, type]
          properties:
            targetUserId:
              type: integer
            type:
              type: string
              enum: [CARD, PROFILE, RECOMMENDATION]
  responses:
    201:
      description: 생성 성공
      content:
        application/json:
          schema:
            type: object
            properties:
              id: { type: integer }
              createdAt: { type: integer, description: "Unix timestamp (ms)" }
    400:
      description: 잘못된 요청
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    401:
      description: 인증 실패

# ❌ 나쁜 예: 표에 URL만 나열
# | API | 설명 | 상태 |
# | POST /api/v1/impressions | 노출 기록 | 구현 완료 (WEBB-1143) |
```

> **"구현 완료"라고 표시된 API도 문서에 스키마가 없으면 불완전합니다.** 구현 완료 여부와 문서 완전성은 별개입니다.

### 금지 표현

아래 표현이 포함된 요구사항은 반드시 구체화해야 합니다.

- **모호한 형용사/부사**: 빠르게, 적절히, 충분히, 상당히, 효율적으로, 안정적으로
- **주체 불명확**: "처리된다", "저장된다" → "서버에서 처리한다", "PostgreSQL에 저장한다"

### TBD 처리 규칙

> **원칙**: TBD 는 "**언제·누가·왜·무엇에 영향**" 4 가지를 모두 명시할 때만 허용한다.
> 4 가지를 다 적을 수 없으면 TBD 가 아니라 **결정 미루기**일 뿐이며, 베이스라인 통과가 불가하다.

| 필수 항목 | 설명 |
|----------|------|
| **미결 이유** | 왜 지금 결정할 수 없는가 (정보 부족 / 외부 의존 / 운영 데이터 필요 등) |
| **결정 책임자** | 최종 결정을 내릴 사람 (`@이름`) |
| **결정 마감 시점** | 절대 시점("2026-07-01") 또는 상대 시점("런칭 후 4 주") |
| **영향 받는 섹션** | 이 결정이 확정되면 본 문서의 어떤 섹션·하위 산출물(DBML·Swagger·UI)이 갱신되어야 하는가 |

```markdown
<!-- ✅ 허용: 4 항목 전부 명시 -->
- **스팸 방지 정책** (TBD)
  - 미결 이유: 런칭 후 실사용 패턴(IP/디바이스/속도) 데이터가 필요하다
  - 결정 책임자: @홍길동 (백엔드 리드)
  - 결정 마감 시점: 런칭 후 4 주
  - 영향 받는 섹션: 6.2 Security / 7.3 신고·차단 / Swagger `POST /reports`
  - 관련 이슈: DEVT-000

<!-- ❌ 불허용 (이유·책임자·시점·영향 누락) -->
- 스팸 방지 기능이 필요하다고 생각하지만 구체적인 방안이 마련되지 않음

<!-- ❌ 불허용 ("나중에 정함" 류) -->
- 인증 방식: TBD
```

- 베이스라인(v1.0) 통과 시점에 **TBD 항목 목록**을 별도 표로 정리하여 변경 이력에 첨부합니다.
- TBD 가 결정되면 본문을 수정하고, 변경 이력에 "TBD → 결정" 한 줄을 기록합니다.

### 우선순위 정의 (1.3에서 반드시 정의)

| 우선순위 | 정의 |
|----------|------|
| **P1** | 반드시 포함. 제외 시 릴리스 불가 |
| **P2** | 중요하나 일정에 따라 조정 가능 |
| **P3** | 추가되면 좋으나 필수 아님. 다음 Phase |

### 해당 없는 항목 처리 — `None` vs `N/A` 구분

항목은 삭제할 수 없습니다. 내용이 없는 경우 아래 표기를 **정확히 구분**해서 사용합니다.

| 표기 | 의미 | 사용 예 |
|------|------|--------|
| `None` | 항목은 적용 대상이지만 **이번 프로젝트에서 해당되는 내용이 없다** | 1.7.3 Patent — 특허 출원 가능 아이디어가 실제로 없음 |
| `N/A` | **항목 자체가 본 프로젝트에 적용되지 않는다** (검토 자체가 무의미) | 백엔드 전용 프로젝트의 4.2 User Interface |
| `N/A(기존과 동일)` | 기존 문토 환경과 완전히 동일하여 별도 정의가 필요 없음 | 3.1 Operating Environment |
| `N/A(기존 배포 환경과 동일)` | 기존 배포 환경과 완전히 동일 | 3.3 Distribution Environment |

> **`None` 과 `N/A` 의 의미가 다릅니다.** `None` 은 "확인했고 없다", `N/A` 는 "확인 자체가 무관하다" 입니다. 잘못 쓰면 리뷰어가 누락 여부를 판단할 수 없습니다.

> 항목을 **삭제하면** 독자가 "누락된 것인지, 해당 없는 것인지" 판단할 수 없습니다. 삭제 금지.

**상위 항목 축약 규칙**: 하위 항목이 **전부** `None` 또는 `N/A` 계열인 경우, 하위 항목을 개별 기재하지 않고 **상위 항목에 `N/A`를 한 번만 기재**해도 됩니다. 이 경우 하위 항목이 모두 해당 없음으로 간주됩니다.

```markdown
<!-- ✅ 축약 가능: 하위 항목 전부 N/A -->
### 3.1 Operating Environment
N/A

<!-- ❌ 축약 불가: 하위 항목 중 일부만 N/A -->
### 3.1 Operating Environment
#### 3.1.1 Hardware Environment
N/A(기존과 동일)
#### 3.1.2 Software Environment
Node.js 18.15.0, PostgreSQL 15
```

### 용어 표기

- 기술 용어는 **영어 원문** 표기, 최초 등장 시 한글 병기: `Socket.IO(웹소켓)`
- 약어는 최초 등장 시 전체 용어 병기: `MSA(Microservice Architecture)`
- 시간 형식: Unix Timestamp (밀리초)
- 필드명: camelCase

### 비목표(Will Not Do) 표기 규약

**"하지 않는다"는 결정은 "한다"는 결정만큼 중요합니다.** 비목표를 명시하지 않으면 리뷰어·구현자·QA 가 각자 추정해서 일하게 됩니다.

비목표는 **누락 위험이 높은 두 위치**에 명시합니다.

| 위치 | 무엇을 적는가 |
|------|--------------|
| **1.2 Product Scope 마지막 1 문단** | 프로젝트 전체 차원의 비목표 (예: "본 프로젝트는 채팅·결제 기능을 다루지 않는다") |
| **7.x 각 기능 끝** | 해당 기능 차원의 비목표 (예: "이 추천 알고리즘은 신규 사용자(가입 7 일 미만)는 대상으로 하지 않는다") |

```markdown
<!-- ✅ 좋은 예 -->
### 7.2 추천 알고리즘 (P1)
...본문...

**비목표 (Will Not Do):**
- 신규 사용자(가입 7 일 미만)는 본 알고리즘의 대상이 아니다. 별도 콜드 스타트 정책(7.5)을 따른다.
- 비활성 사용자(30 일 이상 미접속)는 후보군에서 제외하며, 본 알고리즘으로 점수를 재계산하지 않는다.

<!-- ❌ 나쁜 예: 비목표 절 자체가 없음 → 구현자가 "신규/비활성 처리"를 임의 결정 -->
```

- 비목표는 **부정형으로 명확히** 작성합니다. "~ 고려하지 않는다", "~ 대상이 아니다", "~ 본 프로젝트 범위 밖이다".
- 단순 누락(쓰지 않음)과 비목표(의도적으로 제외)는 다릅니다. 의도적으로 제외한 것은 반드시 비목표로 명시합니다.

### 논의 기록 (Decision Log) — 핵심 결정의 근거 보존

**"왜 이렇게 결정했는가"가 사라지면, 6 개월 뒤 같은 논의를 반복합니다.**
SRS 본문은 결론만 적고, 그 결론에 도달한 과정을 별도 **Decision Log** 에 보존합니다.

**기록 대상**: 다음 중 하나라도 해당하면 Decision Log 에 1 줄을 추가합니다.

1. 1.2 / 2.x / 6.x / 7.x 에서 **여러 안 중 하나를 선택한 결정** (예: "JWT vs 서버 세션 → JWT 채택")
2. 외부 시스템·라이브러리·프로토콜 선택 (예: "WebSocket vs Socket.IO → Socket.IO")
3. 비기능 요구사항의 수치 근거 (예: "응답 시간 300 ms 채택 근거")
4. 비목표(Will Not Do) 로 옮긴 항목 (왜 빼기로 했는가)

**위치**: SRS 본문 끝(7장 뒤)에 부록 `Appendix A. Decision Log` 로 추가합니다.

```markdown
## Appendix A. Decision Log

| 일시 | 결정 사항 | 채택안 | 비교 대안 | 채택 이유 | 결정자 | 관련 섹션 |
|------|----------|--------|----------|-----------|--------|----------|
| 2026-05-12 | 인증 방식 | JWT (Access 1 h + Refresh 14 d) | 서버 세션 / OAuth 위임 | MSA 구조에서 무상태 검증 필요 | @홍길동 | 6.2 |
| 2026-05-13 | 메시지 동기화 | Socket.IO + Redis Adapter | 순수 WebSocket / SSE | 재연결·룸 관리 비용 절감 | @김민지 | 4.5, 7.4 |
| 2026-05-14 | 채팅 기능 비포함 | Will Not Do | — | 본 프로젝트 범위 초과, 별도 chat-backend 진행 | @홍길동 | 1.2 |
```

- 결정이 **번복**되면 새 줄을 추가하고, 이전 결정 줄에는 `(2026-06-01 번복, A.5 참조)` 와 같이 주석을 답니다. 이전 줄을 지우지 않습니다.
- 베이스라인 v1.0 통과 시점의 Decision Log 항목 수를 기록하면, 변경 관리(CCB) 추적이 쉬워집니다.

### 핵심 결정 — 대안 검토 박스 의무화

**AI 가 처음 제안한 안을 그대로 통과시키지 않기 위한 강제 장치입니다.**
다음에 해당하는 "핵심 결정" 에는 본문 안에 **대안 검토 박스**를 반드시 포함합니다.

**대안 검토 박스 의무 대상**:

- 인증·세션·암호화 방식
- 통신 프로토콜 (REST/gRPC/WebSocket/Socket.IO 등)
- 데이터 동기화 전략 (Polling/SSE/Push 등)
- DB 모델링의 분기점 (정규화 vs 비정규화, 단일 테이블 상속 vs 분리)
- 외부 시스템·SDK 선택
- 비기능 요구사항의 수치 결정 (응답 시간·동시 세션·가용성 등)

```markdown
> **🔍 대안 검토 — 인증 방식**
>
> - **채택안**: JWT (Access 1 h + Refresh 14 d)
>   - 장점: MSA 무상태 검증, 모바일/웹 통합 용이
>   - 단점: 토큰 강제 무효화 비용, 로테이션 복잡도
> - **대안 1**: 서버 세션 (Redis 기반)
>   - 장점: 즉시 무효화, 단순한 멘탈 모델
>   - 단점: MSA 전 노드가 동일 Redis 의존 → 단일 장애점
> - **대안 2**: 외부 OAuth 위임 (Auth0)
>   - 장점: 보안 운영 부담 위임
>   - 단점: 월 비용·종속성, 신원 검증 정책 외부화
> - **선정 이유**: 본 프로젝트는 MSA 구조이며 자체 정책(닉네임·연령 검증)이 필요. 운영 비용 최소화 우선.
> - **재검토 조건**: 동시 접속 5 만 초과 시 / 외부 SSO 도입 요구 발생 시
```

- 최소 **대안 2 개**를 비교합니다 ("대안 없음 — 표준이므로" 식의 한 줄 통과 금지).
- 장점·단점·운영 비용·재검토 조건을 모두 포함합니다.
- 박스 내용은 **Appendix A. Decision Log** 의 해당 줄과 1:1 로 연결되어야 합니다.

### AI 작성물 검증 책임 — "통과 = 인수" 원칙

**AI 가 작성한 산출물이라도, 사람이 한 번 통과시키면 그 시점부터 책임은 통과시킨 사람에게 있습니다.**

| 행동 | 책임 소재 |
|------|----------|
| AI 가 SRS·DBML·Swagger·UI·TCL 초안을 생성 | (AI 출력은 가설일 뿐) |
| 사람이 PR/리뷰에서 ✅ 또는 LGTM 표기 | **그 사람이 인수자(reviewer-of-record)** |
| 베이스라인 v1.0 설정 | 인수자 명단·일시가 변경 이력에 기록됨 |

**리뷰어 자기점검 — 통과 직전 5 가지 질문 (모든 사람 리뷰에 적용)**

> 1. 이 문서/산출물 전체를 **처음부터 끝까지** 읽었는가? (스크롤만 내리지 않았는가)
> 2. 본문에 등장하는 **모든 비표준 용어**의 뜻을 알고 있는가? 모르면 1.4 / Glossary 에서 확인했는가?
> 3. **Why** 가 명시되어 있는가? (단순히 What 만 적혀 있는 게 아닌가)
> 4. **누락된 케이스가 있는가?** (에러·경계값·동시성·권한·롤백)
> 5. **다른 합리적 대안**이 있는데, 채택안의 우위 근거가 명확한가? 없다면 대안 검토 박스를 요청했는가?

- 5 가지 중 단 1 개라도 "아니오 / 모름" 이 있으면 **통과 보류**합니다.
- 모르는 용어를 발견하면, 통과 전에 작성자에게 **질문하는 것이 의무**입니다. "AI 가 썼으니 맞겠지" 식의 묵시적 통과는 명백한 책임 위반입니다.
- AI 가 1 안만 제시한 경우, "왜 이게 최선인가" 와 "어떤 안과 비교했는가" 를 작성자에게 요청합니다. 답이 없으면 통과 보류합니다.

### Glossary(용어집) 작성 의무

§1.4 (Terms and Abbreviations) 는 SRS 의 **Glossary 부록** 역할을 합니다.
아래 5 종은 본문에 등장하는 즉시 1.4 에 의무 등록합니다.

| 등록 대상 | 예 (도메인별) |
|----------|---|
| **사내 용어·외래어** | `큐레이션`, `센터`, `오픈 채팅` (소셜링) / `호스트`, `참가자` (이벤트) / `리워드`, `포인트` (결제) |
| **약어** | `MSA`, `JWT`, `PG`, `RPO`, `RTO`, `P95`, `DAU`, `MAU` (도메인 무관) |
| **도메인 코드 (상태값·enum)** | `DRAFT`, `SUBMITTED`, `APPROVED`, `REJECTED` (워크플로) / `PENDING`, `PAID`, `REFUNDED` (결제) / `READ`, `UNREAD` (알림) |
| **수학 기호·변수** *(통계·랭킹·ML 도메인에 한정)* | `α₀`, `β₀`, `k`, `n` (추천 알고리즘) / `r`, `d` (수수료율·할인율, 결제) / `λ`, `μ` (대기열 이론) |
| **AI 가 제안했는데 출처가 불분명한 용어** | 의심되면 즉시 등록 + 출처/근거 확인 (도메인 무관) |

```markdown
<!-- ✅ 좋은 예: 1.4 표 한 행 -->
| 큐레이션 | 운영자가 후보 사용자 중 일부를 수동 선별해 추천 풀에 올리는 행위 | 7.2.4 참조 |
| SUBMITTED | 신청서가 사용자에 의해 제출되었으나 운영자 검토 전 상태 | 7.3.1 참조 |

<!-- ❌ 나쁜 예 -->
- 본문에서 "큐레이션" 을 7 번 사용했으나 1.4 에 정의 없음
- 1.4 에 "MSA" 만 정의되어 있고, 본문의 "EDA(이벤트 기반 아키텍처)" 는 누락
- enum 값 `SUBMITTED`, `APPROVED` 가 본문/Swagger/DBML 에 등장하는데 1.4 미정의 → 리뷰어가 의미·전이 규칙 추정해야 함
```

- **빈 Glossary 금지**: 본문이 3 페이지를 넘는 SRS 인데 1.4 가 비어 있으면 리뷰어는 통과시키지 않습니다.
- AI 작성 시: 본문 작성 후 비표준 용어 자동 수집 → 1.4 초안 자동 등록 → 리뷰어 최종 확인.

### 섹션 간 일관성 체크

문서 작성 완료 후 아래 항목을 반드시 확인합니다.

- [ ] **2.4 ↔ 7장**: Product Functions 항목이 7장 대분류와 1:1 매핑되는가
- [ ] **1.3 ↔ 7장**: 정의한 P1/P2/P3 기준이 7장 전체에 일관되게 적용되었는가
- [ ] **2.7 ↔ 7장**: Phase별 분류가 P1/P2/P3와 일치하는가
- [ ] **6장 ↔ 7장**: 7장에서 "6.x 참조"로 표시한 섹션이 실제 6장에 존재하는가
- [ ] **외부 링크**: Figma, Notion, GitHub, Jira 링크가 접근 가능한가
- [ ] **SRS 4.1**: Swagger(OpenAPI) 형식의 API 링크가 포함되어 있는가
- [ ] **SRS 4.1 / 6.4**: PostgreSQL 형식의 ERD 링크가 포함되어 있는가
- [ ] **One Pager Technical Description**: API(Swagger) + ERD(PostgreSQL) 링크가 포함되어 있는가
- [ ] **1.3 → 1.4**: 1.3 등 이른 섹션에서 등장하는 수학 기호·변수가 1.4 용어표에 모두 정의되어 있는가
- [ ] **4.4 DB 스키마**: 신규 테이블은 Prisma 모델 수준으로 정의되어 있는가 (컬럼명, 타입, 기본값, nullable, 인덱스, relation)
- [ ] **4.4 DB 변경**: 기존 테이블 변경 시 타입·기본값·nullable·마이그레이션 전략이 명시되어 있는가
- [ ] **4.4 API 스키마**: 모든 API가 request/response JSON 스키마, 상태 코드, 에러 코드를 포함하는가
- [ ] **1.2 균형**: Why–What–How 균형 원칙(30/50/20)이 지켜졌는가. 1.2 에 Why 가 1 문단 이상 있는가
- [ ] **1.2 / 7.x 비목표**: Will Not Do 가 명시되었는가
- [ ] **1.4 Glossary**: 본문 비표준 용어(사내 약어·수학 기호·외부 모호 용어)가 모두 1.4 에 등록되어 있는가. 1.4 가 비어 있지 않은가
- [ ] **TBD 4 항목**: 모든 TBD 에 미결 이유 / 책임자 / 마감 시점 / 영향 섹션이 명시되어 있는가
- [ ] **None vs N/A**: 두 표기가 정확히 구분되어 사용되었는가
- [ ] **대안 검토 박스**: 의무 대상 결정(인증·통신·DB 분기점·외부 SDK·NFR 수치 등)에 대안 검토 박스(최소 2 안 비교)가 있는가
- [ ] **Decision Log**: Appendix A 가 존재하며, 핵심 결정·번복이 누적 기록되는가
- [ ] **리뷰어 자기점검 5 질문**: 리뷰어가 통과 직전 5 가지 질문을 모두 통과했는가 (모르는 용어 0 개, 누락 케이스 확인 등)
- [ ] **AI 작성물 책임 인수**: PR/리뷰 통과 시 인수자 실명·일시가 변경 이력에 기록되는가

---

## 변경 이력

| 일시 | 변경 사항 | 작성자 |
|------|----------|--------|
| 2026-05-18 | 초안 작성 (DEVT-107) | — |
| 2026-05-20 | Agentic Dev Chain TO-BE 반영 — Why-What-How 균형 / Glossary 의무화 / TBD 4 항목 / None vs N/A 구분 / Will Not Do / Decision Log / 대안 검토 박스 / AI 작성물 책임 인수 / 자기점검 5 질문 신설 (검토용, 본 사본은 `munto-dev-assistant-report` 안에만 반영) | — |
| 2026-05-20 | 도메인 편향 제거 — *수학 기호·변수* 가 1.4 등록 대상의 *부분 집합* 임을 명확화. ① §1.4 가이드 행: 식별자 4 종 카테고리(약어 / 외래어·도메인 용어 / 도메인 코드(상태값) / 수학 기호) 로 일반화 + 복수 도메인 예시 병기. ② §"기호·수식 선행 정의 원칙": *수식이 있는 도메인 한정* 임을 명시 + 결제 도메인 치환 예. ③ §"Glossary 작성 의무" 표: 5 행으로 확장 (도메인 코드 행 신설 + 사내 용어/약어 분리 + 수학 기호 행 다중 도메인 예). ④ §1.2 / §"기호·수식" / §DB 스키마 / §API 스키마의 예시 코드 블록 위에 *"예시 도메인: 추천 알고리즘 시스템 (가상)"* 라벨 추가 — 비-알고리즘 도메인 작성자(채팅·결제·이메일 등) 가 *치환해서 적용* 함을 명확화 | — |

---

*관련 이슈: [DEVT-107](https://munto.atlassian.net/browse/DEVT-107)*
