# `projects/` — 활성 Implementation Plan 인덱스

> 본 폴더는 **Munto 의 모든 활성 프로젝트의 Implementation Plan (구현계획서, IP) 단일 진입점** 입니다.
> 각 프로젝트는 *1 폴더 = 1 IP* 구조를 따릅니다.

---

## 목차

- [1. 폴더 구조](#1-폴더-구조)
- [2. 활성 프로젝트 (Active)](#2-활성-프로젝트-active)
- [3. 보류·중단 (Paused)](#3-보류중단-paused)
- [4. 아카이브 (Archived)](#4-아카이브-archived)
- [5. 새 프로젝트 등록 방법](#5-새-프로젝트-등록-방법)
- [6. 컬럼 정의](#6-컬럼-정의)
- [7. 표준 문서 참조](#7-표준-문서-참조)
- [변경 이력](#변경-이력)

---

## 1. 폴더 구조

```
projects/
├── README.md                            # 본 파일 (활성 프로젝트 인덱스)
├── _template/                           # IP 견본 폴더 (인덱스 등록 X)
│   ├── ImplementationPlan.md
│   └── README.md
├── _archive/                            # 종료 프로젝트 아카이브 (옵션, 생성 시점에 만듦)
│   └── {YYYY}/
│       └── {프로젝트명}/
└── {프로젝트명}/                          # 활성 프로젝트 1 개당 1 폴더
    ├── ImplementationPlan.md
    └── (옵션) README.md · sessions/ · decisions/ · attachments/ · spec-stubs/
```

> 상세 폴더 구조와 옵션 서브폴더 생성 시점은 [`_template/README.md`](./_template/README.md) 참조.

---

## 2. 활성 프로젝트 (Active)

| 프로젝트명 | Owner | 현재 버전 | Operating Mode | 관련 Repo | Slack 채널 | 마지막 갱신 | 비고 |
|----------|-------|-----------|----------------|----------|------------|------------|------|
| <!-- 예시 행 (실제 프로젝트 등록 시 이 줄 삭제 후 추가): --> |
| paid-socialing-v2 | @grace.gyu | v1.0 (2026-05-25) | 유인 → P3 부터 무인 | munto-backend, munto-frontend, dating-mobile | #dev-paid-socialing | 2026-05-25 | TO-BE §4.3 IP-7 ③ 방식 사용 (T-MIGRATE-SPEC-FINAL 포함) |

> *(현재 활성 프로젝트 없음 — `_template/` 복사 후 위 표에 추가)*

---

## 3. 보류·중단 (Paused)

> 일시 보류 중인 프로젝트. 재개 시 *활성* 으로 이동.

| 프로젝트명 | Owner | 보류 일자 | 보류 사유 | 재개 예정 |
|----------|-------|----------|----------|----------|
| <!-- 해당 없을 시 본 표는 비워둠 --> |

---

## 4. 아카이브 (Archived)

> 종료된 프로젝트. 3 개월 이상 비활성이면 `_archive/{YYYY}/{프로젝트명}/` 로 이동 (Git 히스토리 보존).

| 프로젝트명 | Owner | 종료 일자 | 최종 버전 | 아카이브 경로 |
|----------|-------|----------|----------|--------------|
| <!-- 해당 없을 시 본 표는 비워둠 --> |

---

## 5. 새 프로젝트 등록 방법

```bash
# 1. 견본 폴더 복사
cp -R munto-dev-assistant/projects/_template munto-dev-assistant/projects/{프로젝트명}

# 2. ImplementationPlan.md 작성 (8 섹션 / 9 필드 Task 카드)

# 3. 본 README.md 의 §2 "활성 프로젝트" 표에 새 행 추가

# 4. 워크스페이스 파일 생성 (멀티 프로젝트 동시 운영 시 — §IP-9)
#    munto-dev-assistant/workspace/{프로젝트명}.code-workspace
```

> 상세 절차·자동 검증·사람 리뷰 7 가지 질문은 [`../ip-standard.md`](../ip-standard.md) 와 [`../skills/dev-chain-implementation-plan/SKILL.md`](../skills/dev-chain-implementation-plan/SKILL.md) 참조.

---

## 6. 컬럼 정의

| 컬럼 | 의미 | 기록 형식 | 누가 갱신 |
|------|------|----------|----------|
| **프로젝트명** | IP 폴더 이름 = 프로젝트 식별자 | kebab-case 영문 50 자 이내. 메이저 버전(v2) 만 표기 | IP 작성 시 (1 회) |
| **Owner** | 본 IP 의 작성·유지 책임자 (분석 아키텍트와 별도일 수 있음) | `@{author-id}` *(Munto 권장 = Slack 멘션 핸들 — 예: `@gyuhyeon.jeon`)* | Owner 변경 시 |
| **현재 버전** | IP 의 현재 baseline 버전 + 동결 일자 | `v{X.Y} ({YYYY-MM-DD})` | §8 Change History 갱신 시 |
| **Operating Mode** | 본 프로젝트의 현재 운영 모드 | `유인` \| `무인` \| `유인 → P{N} 부터 무인` | §7 Operating Mode 변경 시 |
| **관련 Repo** | 본 IP 가 건드리는 모든 Repo (쉼표 구분) | `munto-backend, munto-frontend, dating-mobile` 등 | Repo 추가/제거 시 |
| **Slack 채널** | 본 프로젝트 전용 채널 (BLOCKER·일일 요약·세션 인계 알림) | `#{channel-name}` | 채널 신설/이동 시 |
| **마지막 갱신** | 본 행이 마지막으로 수정된 날짜 | `YYYY-MM-DD` | 본 행 갱신 시마다 |
| **비고** | 특이 사항 (③ 방식 사용 여부·외부 의존·연관 프로젝트 등) | 1~2 문장 | 자유 |

---

## 7. 표준 문서 참조

- [`../ip-standard.md`](../ip-standard.md) — IP 작성 표준 (8 섹션 / 9 필드 / 5 Task 단위 기준 / 4 요소 spec_refs / DoD 3 요건 / IP-9 동시 프로젝트 운영)
- [`../spec-standard.md`](../spec-standard.md) — Spec (SRS · One Pager) 작성 표준
- [`../skills/dev-chain-implementation-plan/SKILL.md`](../skills/dev-chain-implementation-plan/SKILL.md) — ip-writer/ip-reviewer 자동 생성 스킬
- [`./_template/README.md`](./_template/README.md) — IP 견본 폴더 사용법
- 정책 원본: [TO-BE 프로세스 가이드 (Notion)](https://www.notion.so/Agentic-Dev-Chain-Munto-TO-BE-36de2bc7639d8052b13fc49575c10e56) §4.3 IP-0 ~ IP-9

---

## 변경 이력

| 일자 | 내용 |
|------|------|
| 2026-05-27 | 신규 작성 — `projects/` 인덱스 양식 (ip-standard.md §"저장 위치와 파일명 규약" 의 `projects/README.md` 인덱스 의무 조항 자리 채움). 활성/보류/아카이브 3 단계 분리, 8 개 컬럼 정의, 새 프로젝트 등록 절차 포함 |
