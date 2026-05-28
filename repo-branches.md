# Munto GitHub 레포 — 브랜치 현황 분석 및 통일안

**작성 목적**: Munto-dev 조직 레포의 `development` / `production` / `main` / `master` 혼재 상태를 정리하고, 팀 공통 브랜치 규칙·정리 우선순위를 제안한다.  
**조사 일자**: 2026-05-28  
**조사 방법**: GitHub REST API — **`git/ref/heads/{브랜치}`로 실존 여부 확인** (아래 §1.1 주의)  
**조사 범위**: Munto-dev 조직 **45개 레포 전체** (private 포함)  
**원본 데이터**: `.branch-inventory.json` (재조사·검증용)

> **범례**: ✅ = 브랜치 **실존** (`refs/heads/…` 확인) / ❌ = 없음 / 🔒 = branch protection

---

## 1. 요약 (Executive Summary)

| 항목 | 현황 (45레포) |
|------|----------------|
| **조직 레포 수** | **45개** |
| **default branch** | `development` **27** · `main` **15** · `master` **3** |
| **`production` 존재** | **13개** |
| **실질 표준 패턴** | `development` + `production` — **12개** (mobile 포함) |
| **`master` 실존** | **5개만** — backoffice-v1, munto_front, muntorial, munto_scheduler, munto_admin_flutter |
| **`main` 2nd long-lived (dev 레포)** | dating-backend/mobile, mobile-core, lambda_image_resizer, bigquery-sync 등 |
| **권장 방향** | 서비스 = **`development` + `production`**. diverged `main`/`master`는 **prod 통합 또는 삭제** |
| **`master` → `main` 통일?** | **No** — **`production` 통일**이 우선 |

### 1.1 조사 방법 주의 — API alias 오탐 (2026-05-28 수정)

초판 보고서는 `GET /repos/.../branches/master`가 200이면 master가 있다고 잘못 집계했다.  
**munto-backend에는 `master` 브랜치가 없다** — 사용자 지적이 맞다.

| 확인 방법 | munto-backend `master` | 실제 |
|-----------|------------------------|------|
| `GET /branches/master` | HTTP 200 (응답 `name`: **development**) | **alias** — 예전 default 이름이 현재 default로 리다이렉트 |
| `GET /git/ref/heads/master` | HTTP **404** | **브랜치 없음** |
| Branches UI | 목록에 없음 | **브랜치 없음** |

과거에 default가 `master`였다가 **`development`로 rename**된 레포에서 GitHub API가 옛 이름을 default로 **alias**해 준다.  
**별도 브랜치가 생긴 것이 아니다.** 이후 조사는 `git/ref/heads/{name}` 200일 때만 ✅ 처리한다.

---

## 2. 조직 전체 통계

### 2.1 default branch 분포

| default | 개수 | 비고 |
|---------|:----:|------|
| `development` | 27 | 서비스·인프라 주류 |
| `main` | 15 | 문서·포크·구형 단일 브랜치 레포 |
| `master` | 3 | muntorial, munto_scheduler, munto_admin_flutter |

### 2.2 long-lived 브랜치 **실존** (45레포)

| 브랜ch | 존재 레포 수 |
|--------|:-----------:|
| `development` | 28 |
| `production` | 13 |
| `main` | 20 |
| `master` | **5** |

### 2.3 패턴 분류 (운영 관점)

| 패턴 | 개수 | 설명 |
|------|:----:|------|
| **표준** dev+prod | 12 | production으로 배포 |
| dev+prod+**main 잔존** | 1 | munto-mobile (stale `main`) |
| dev+**main**, prod 없음 | 5 | dating-backend/mobile, mobile-core, lambda_image_resizer, bigquery-sync |
| dev+**master**, prod 없음 | 2 | backoffice-v1, munto_front |
| dev-only | 7 | backoffice-backend, management, grafana, *-document 등 |
| **단일** main/master (dev 없음) | 18 | 문서·포크·구형 레포 |

---

## 3. 서비스·인프라 레포 상세 (28개)

| 레포 | default | development | production | main | master | 패턴 |
|------|:-------:|:-----------:|:----------:|:----:|:------:|------|
| **munto-backend** | development | ✅ | ✅ | ❌ | ❌ | **표준** |
| **munto-frontend** | development | ✅ | ✅ | ❌ | ❌ | **표준** |
| **munto-backoffice-v2** | development | ✅ | ✅ | ❌ | ❌ | **표준** |
| **munto-notification** | development | ✅ | ✅ | ❌ | ❌ | **표준** |
| **munto-mobile** | development | ✅ | ✅ | ✅ | ❌ | dev+prod+**main잔존** |
| **munto-log-streaming** | development | ✅ | ✅ | ❌ | ❌ | **표준** |
| **munto-model-serving** | development | ✅ | ✅ | ❌ | ❌ | **표준** |
| **munto_be_lambda_action_history** | development | ✅ | ✅ | ❌ | ❌ | **표준** |
| **munto_be_scheduler** | development | ✅ | ✅ | ❌ | ❌ | **표준** |
| **munto_bird** | development | ✅ | ✅ | ❌ | ❌ | **표준** |
| **munto_server** | development | ✅ | ✅ | ❌ | ❌ | **표준** |
| **munto_serverless** | development | ✅ | ✅ | ❌ | ❌ | **표준** |
| **aws-cdk-infra** | development | ✅ | ✅ | ❌ | ❌ | **표준** |
| **dating-backend** | development | ✅ | ❌ | ✅ | ❌ | dev+**main**, prod 없음 |
| **dating-mobile** | development | ✅ | ❌ | ✅ | ❌ | dev+**main**, prod 없음 |
| **munto-mobile-core** | development | ✅ | ❌ | ✅ | ❌ | dev+**main**, prod 없음 |
| **munto_be_lambda_image_resizer** | development | ✅ | ❌ | ✅ | ❌ | dev+**main**, prod 없음 |
| **bigquery-sync** | development | ✅ | ❌ | ✅ | ❌ | dev+**main**, prod 없음 |
| **munto-backoffice-v1** | development | ✅ | ❌ | ❌ | ✅ | dev+**master**, prod 없음 |
| **munto_front** | development | ✅ | ❌ | ❌ | ✅ | dev+**master**, prod 없음 |
| **backoffice-backend** | development | ✅ | ❌ | ❌ | ❌ | dev-only |
| **management** | development | ✅ | ❌ | ❌ | ❌ | dev-only |
| **munto-grafana-sql-query** | development | ✅ | ❌ | ❌ | ❌ | dev-only |
| **munto-chat-backend** | main | ❌ | ❌ | ✅ | ❌ | 단일 main |
| **munto-chat-frontend** | main | ❌ | ❌ | ❌ | ❌ | 단일 main |
| **munto-chat-mobile** | main | ❌ | ❌ | ✅ | ❌ | 단일 main |
| **munto-slack-bot** | main | ❌ | ❌ | ✅ | ❌ | 단일 main |
| **aws-iam** | main | ❌ | ❌ | ✅ | ❌ | 단일 main |

---

## 4. 문서·패키지·포크 레포 (17개, 요약)

| 레포 | default | development | production | main | master |
|------|:-------:|:-----------:|:----------:|:----:|:------:|
| ai_generation_shuffling | main | ❌ | ❌ | ✅ | ❌ |
| muntorial-web | main | ❌ | ❌ | ✅ | ❌ |
| munto-dev-assistant | main | ❌ | ❌ | ✅ | ❌ |
| munto-dev-assistant-tobe-temp | main | ❌ | ❌ | ✅ | ❌ |
| munto-fullstack-docker-starter | main | ❌ | ❌ | ✅ | ❌ |
| munto_server_boilerplate | main | ❌ | ❌ | ✅ | ❌ |
| munto_jenkins | main | ❌ | ❌ | ✅ | ❌ |
| munto-assets-picker | main | ❌ | ❌ | ✅ 🔒 | ❌ |
| munto-social-share | main | ❌ | ❌ | ✅ | ❌ |
| zulip-flutter | main | ❌ | ❌ | ✅ | ❌ |
| backoffice-document | development | ✅ | ❌ | ❌ | ❌ |
| chat-document | development | ✅ | ❌ | ❌ | ❌ |
| dating-document | development | ✅ | ❌ | ❌ | ❌ |
| tips-bert-model | development | ✅ | ❌ | ❌ | ❌ |
| muntorial | master | ❌ | ❌ | ❌ | ✅ |
| munto_scheduler | master | ❌ | ❌ | ❌ | ✅ |
| munto_admin_flutter | master | ❌ | ❌ | ❌ | ✅ 🔒 |

---

## 5. 문제점 진단

### 5.1 운영 브랜치 이름 3종 (`production` / `main` / `master`)

| 운영 추정 | 레포 | 문제 |
|-----------|------|------|
| `production` | 13개 | **표준** |
| `main` (2nd long-lived) | dating-*, mobile-core, lambda_image_resizer, bigquery-sync, mobile(main 잔존) | **`production` 없음** — 배포 대상 불명확 |
| `master` (실존) | backoffice-v1, munto_front + default master 3개 | v1은 v2(`production`)와 **불일치** |
| default `main` only | chat-*, slack-bot, 문서류 | dev+prod **미적용** (별도 정책) |

### 5.2 diverged `main`/`master` (정리 대상)

| 레포 | 브랜치 | 상태 | 위험 |
|------|--------|------|------|
| munto-mobile | main | development 대비 **크게 뒤처짐** | **방치** — prod는 정상 |
| dating-backend | main | dev와 **양방향 diverged** | prod 없음 — **운영 후보** |
| dating-mobile | main | development보다 **뒤처짐** | prod 없음 |
| munto-mobile-core | main | development보다 **뒤처짐** | prod 없음 |
| munto_be_lambda_image_resizer | main | development보다 **뒤처짐** | prod 없음 |
| munto-backoffice-v1 | master | dev와 **약간 diverged** | v2와 운영 브랜치명 불일치 |
| munto_front | master | dev와 **동일 commit** | **중복 브랜치** |

### 5.3 default = `development`는 서비스 레포 주류

- development default **27/45** — 조직 신규 레포 설정과 일치.
- 문서·포크 **18개**는 default `main`/`master` — **레포 유형별 예외** 규칙 필요.

### 5.4 API 한계 (🔒)

- branch protection은 토큰 권한에 따라 API 미반환 가능.
- **`/branches/{옛이름}` alias** — 존재 여부 판단에 **사용 금지**.

---

## 6. `master`를 `main`으로 통일할 필요가 있는가?

**서비스 레포 — No.** 필요한 건 **`production` 통일**.

| 작업 | 효과 |
|------|------|
| `master` → `main` rename | GitHub 관례. **운영 통일과 무관** |
| diverged `master`/`main` → **`production`** | **실제 배포 이름 통일** |
| 중복 `master`/`main` **삭제** | munto_front 등 — CI 확인 후 |

---

## 7. 권장 통일안 (TO-BE)

### 7.1 브랜치 역할 (서비스 레포)

```
feature/* | fix/* | feat/*
        ↓ PR
   development  ← GitHub default
        ↓ PR (릴리즈·hotfix)
   production   ← 운영 배포
```

### 7.2 우선순위 TO-BE 액션

| 우선순위 | 레포 | 액션 |
|:--------:|------|------|
| P0 | dating-backend, dating-mobile | **`main`이 운영인지 확인** → **`production` rename** |
| P0 | munto-backoffice-v1 | **`master`→`production`** (v2 정렬) 또는 freeze |
| P1 | munto-mobile | stale **`main` 삭제** |
| P1 | mobile-core, lambda_image_resizer | prod 도입 또는 main 역할 확정 |
| P2 | munto_front | **`master` 삭제** (dev와 동일 commit) |
| P3 | chat-*, slack-bot | dev+prod 도입 여부 별도 결정 |
| — | 표준 12개 | **none** |

---

## 8. 정리 로드맵

### Phase 0 — 합의 (1주)

- [ ] **운영 = `production`** (서비스) 확정
- [ ] **`master`→`main` 통일 안 함**
- [ ] 문서/포크 default 예외 확정

### Phase 1 — Inventory ✅

- [x] Munto-dev 45레포 (`git/ref` 기준 재조사)
- [ ] CI/CD·배포 파이프라인 브랜치명 grep

### Phase 2 — 레거시 정리

- [ ] diverged `main`/`master` → prod rename 또는 삭제
- [ ] 배포 문서 동기화

---

## 9. FAQ

**Q. default를 `main`으로 바꿔야 하나?**  
A. **서비스 레포는 아니다.** 문서/포크만 `main`.

**Q. API는 master가 있는데 UI에는 없다?**  
A. **`GET /branches/master` alias** 때문. **`git/ref/heads/master`가 404면 브랜치 없음.** 과거 default rename 잔재이지, 별도 master가 있는 것이 아니다.

**Q. `production`과 `development` commit이 어긋나도 되나?**  
A. hotfix가 prod에만 merge되면 **일시적으로** 어긋날 수 있다. 다만 inventory 표에는 넣지 않는다(시점마다 변함). **prod→dev back-merge** 정책은 별도 문서화.

---

## 10. 다음 액션

1. **P0** — dating-backend/mobile, backoffice-v1: 운영 배포 브랜치 1줄 확인  
2. **CI 스캔** — workflow yaml에서 `master`/`main` 참조 grep  
3. **Jira** — 브랜치 네이밍 표준 티켓

---

## 변경 이력

| 일자 | 내용 |
|------|------|
| 2026-05-27 | GitHub Branches 스크린샷 8레포 기준 초안 |
| 2026-05-28 | GitHub API 45레포 조사 (1차) |
| 2026-05-28 | **수정**: `/branches/{name}` alias 오탐 제거 · `git/ref/heads` 기준 재집계 · `(=dev)` 표기 삭제 · munto-backend 등 **master ❌** 로 정정 |
| 2026-05-28 | inventory 표에서 `(Nb/Ma)` behind/ahead 표기 제거 (브랜치 **존재·역할** 중심으로 단순화) |
