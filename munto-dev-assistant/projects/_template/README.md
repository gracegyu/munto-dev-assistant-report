# `_template` — IP (Implementation Plan) 견본 폴더

> 본 폴더는 *복사용 견본* 입니다. 실제 프로젝트가 *아닙니다*.
> 새 프로젝트 시작 시 이 폴더 전체를 복사해 사용하세요.

---

## 1. 새 프로젝트 시작 방법

```bash
# 1. 견본 폴더 복사 (워크스페이스 루트에서)
cp -R munto-dev-assistant/projects/_template munto-dev-assistant/projects/{프로젝트명}

# 2. ImplementationPlan.md 의 모든 {프로젝트명} · {플레이스홀더} 치환
#    (가이드 주석은 작성 완료 후 삭제)

# 3. projects/README.md 인덱스 표에 새 행 추가

# 4. 워크스페이스 파일 생성 (멀티 프로젝트 동시 운영 시 — §IP-9)
#    munto-dev-assistant/workspace/{프로젝트명}.code-workspace
```

`{프로젝트명}` 규칙: kebab-case 영문, 50 자 이내, 메이저 버전(v2) 만 폴더명에 표기. 예: `paid-socialing-v2`.

---

## 2. 폴더 구조 — 필수 1 + 옵션 5

```
projects/{프로젝트명}/
├── ImplementationPlan.md   # 필수 — IP 본문 (단일 진실 공급원)
├── README.md               # 옵션 — 프로젝트 현재 상태·Slack 채널·세션 인덱스·다음 작업자
├── sessions/               # 옵션 — 무인 모드 세션 로그·일일 요약·BLOCKER 기록
│   ├── YYYY-MM-DD-daily-summary.md
│   └── YYYY-MM-DD-blocker-{id}.md
├── decisions/              # 옵션 — 대안 검토 박스 누적본 (Decision Log)
├── attachments/            # 옵션 — Figma 캡처·아키텍처 다이어그램·외부 자료
└── spec-stubs/             # 옵션 — ③ 별도 repo Spec 방식의 STUB·임시 사본
```

> **무인 모드를 안 쓰는 작은 프로젝트는 `ImplementationPlan.md` 하나만 두면 된다.**
> 옵션 서브폴더는 *실제로 사용할 때만* 생성. 빈 폴더 사전 생성 금지.

---

## 3. 옵션 폴더별 생성 시점

| 폴더 | 생성 시점 |
|------|----------|
| `README.md` | 인계자가 *현재 활성 세션 ID · 다음 작업자 · 다음 Task ID* 를 기록할 필요가 생기면 |
| `sessions/` | **PHASE 0~1 (Spec 작성) 자동 (a)**: `spec-session-{date}.md` 와 `spec-review-{date}-{doc}.md` 는 `munto-spec-writer`·`munto-spec-review` 스킬 호출 시 *자동* 박힘. `spec-handover-*.md` 는 사람 인계 시 *수동*. **`spec-baseline-handoff.md` = PHASE 1 GATE 통과 시 Owner 사람 작성 *의무*** (없으면 IP 작성 단계가 *컨텍스트 결손* 으로 진입). **PHASE 2 (구현 운영) 자동 의무 3 종**: `daily-summary`·`phase-{n}-summary`·`blocker-{id}` 는 무인 모드 진입 시 오케스트레이터가 자동 생성, 유인 모드는 *선택*. 인계용 `handover-*.md` 는 *수동 의무*. 자동/수동 매트릭스·Git 커밋 정책 상세는 [`../../ip-standard.md` §세션 파일 저장 정책](../../ip-standard.md#세션-파일-sessions-저장-정책-요약) 및 *TO-BE §4.7.4 / §4.9.7* 참조 |
| `decisions/` | 큰 대안 검토 (스펙 단계 1 안 vs 2 안)를 *결정 이력* 으로 보존하고 싶을 때 |
| `attachments/` | Figma 캡처·시퀀스 다이어그램·외부 자료 등 *바이너리 / 비텍스트 자료* 가 생길 때 |
| `spec-stubs/` | ③ 별도 repo Spec 방식 사용 시 (임시 STUB 보관, `T-MIGRATE-SPEC-FINAL` 완료 시 정리) |

> **AI 도구 raw 세션 (Claude Code JSONL · Cursor 채팅) 은 `~/.claude/`·`~/.cursor/` 에 *개인 로컬* 자동 저장된다.** `sessions/` 폴더는 *그것과 별개* 인 *팀 공유 영구 기록* 이다 — 둘을 혼동하지 말 것.
>
> **PHASE 0~1 자동 (a) 트랙**: `munto-spec-writer`·`munto-spec-review` 스킬이 *호출 시점에* `sessions/spec-session-*.md`·`spec-review-*.md` 를 자동 박는다. 운영 레포 적용 대기 본문은 `-report/munto-dev-assistant/skills/munto-spec-{writer,review}/SKILL.md` 참조.
>
> **PHASE 0~1 자동 (c) 트랙** *(옵션)*: Claude Code `Stop` Hook 이 *매 turn 자동* 으로 `sessions/spec-hook-turn-{date}.md` append. *작성자 본인 디버그용* — `.gitignore` 권장. 견본은 `-report/munto-dev-assistant/.claude-hooks-proposal.json` 참조 (별도 PR 로 적용).

---

## 4. 견본 파일 목록

| 파일 | 용도 |
|------|------|
| `ImplementationPlan.md` | IP 본문 견본 — 8 섹션 / 9 필드 Task 카드 / 7 가지 자동 점검 / 완료 체크리스트 포함 |
| `README.md` (본 파일) | 견본 폴더 사용법 안내 |

> **이 `_template` 폴더 자체는 인덱스(`projects/README.md`)에 등록하지 않습니다.**
> 인덱스에 등록되는 것은 *실제 프로젝트 폴더* 뿐.

---

## 5. 표준 문서 참조

- [`../../ip-standard.md`](../../ip-standard.md) — 8 섹션 / 9 필드 / 5 Task 단위 기준 / 4 요소 spec_refs / DoD 3 요건 상세
- [`../../skills/dev-chain-implementation-plan/SKILL.md`](../../skills/dev-chain-implementation-plan/SKILL.md) — ip-writer/ip-reviewer 자동 생성 절차
- [`../../../reports/2026-05-harness-TO-BE.md`](../../../reports/2026-05-harness-TO-BE.md) §4.3 IP-0 ~ IP-9 — 정책 원본

---

## 변경 이력

| 일자 | 내용 |
|------|------|
| 2026-05-27 | 신규 작성 — IP 견본 폴더 (ip-standard.md L469 *추후 제공 예정* 자리 채움) |
| 2026-05-27 | §3 옵션 폴더별 생성 시점 표의 `sessions/` 행 보강 — 자동/수동 매트릭스 (무인 모드 3 종 자동 의무 / 유인 모드 선택 / 인계용 수동 의무) 및 AI 도구 raw 세션과의 구분 박스 추가. 상세 정책 cross-link (`ip-standard.md` §세션 파일 저장 정책 + TO-BE §4.9.7). TO-BE §4.9.7 신설에 동기화 |
| 2026-05-27 | **§3 sessions/ 행에 *PHASE 0~1 Spec 작성 세션 4 종* 추가 + raw 세션 구분 박스 확장** *(TO-BE §4.7.4 신설에 동기화)* — ① 표 셀 *PHASE 2 무인 모드 자동 의무 3 종* 본문 앞에 *PHASE 0~1 (Spec 작성) 자동 (a)* 4 종 (`spec-session-*.md`·`spec-review-*.md`·`spec-handover-*.md`·**`spec-baseline-handoff.md` = Owner 사람 의무**) 통합 설명. 두 PHASE 가 *대칭 구조* 임을 명시. ② 박스에 *PHASE 0~1 (a) 자동 트랙* (운영 레포 적용 대기 본문 `-report/.../skills/munto-spec-{writer,review}/SKILL.md` 위치) + *(c) Hook 트랙* (옵션, `.claude-hooks-proposal.json` 견본) 안내 추가. ③ 적용 시점 명시 — 운영 레포 일괄 이관 시점에 활성 |
