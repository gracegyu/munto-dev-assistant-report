# `-report/munto-dev-assistant/skills/` — *적용 대기 본문* 미러

본 폴더는 **운영 레포 (`/Users/gracegyu/Documents/GitMunto/munto-dev-assistant/.agents/skills/common/docs/`) 의 스킬 본문 *교체 대기본***을 임시 보관하는 *기획 미러* 입니다.

## 1. 보관 원칙

- *현재 운영 중인 스킬은 직접 수정하지 않는다* — 정책 검증·합의 미완료 시 운영 영향 차단
- *수정 결과만* 본 폴더에 박고, 정책 일괄 이관 시점에 *cp -R 한 번* 으로 운영 반영
- 운영 레포 폴더 구조와 *동일 패턴* (skill name 하위 폴더)

## 2. 현재 보관 중인 본문

| 폴더 | 운영 레포 적용 위치 | 핵심 변경 | 정책 근거 |
|------|---------------------|-----------|----------|
| `dev-chain-implementation-plan/` | `.agents/skills/backend/docs/dev-chain-implementation-plan/` *(또는 common/docs 위치 — 운영 이관 시 결정)* | 신규 스킬 (IP 작성) | TO-BE §4.3 IP-0 ~ IP-9 |
| `munto-spec-writer/` | `.agents/skills/common/docs/munto-spec-writer/` | *세션 저장 단계* 신설 (a 자동 저장) | TO-BE §4.7.4 (1)(2)(5) |
| `munto-spec-review/` | `.agents/skills/common/docs/munto-spec-review/` | *세션 저장 단계* + *baseline-handoff 자동 점검 BLOCKER* 신설 | TO-BE §4.7.4 (1)(2)(5) |

## 3. 운영 이관 절차 (정책 합의 후)

```bash
# 1) 백업 (만일에 대비)
cp -R /Users/gracegyu/Documents/GitMunto/munto-dev-assistant/.agents/skills/common/docs/munto-spec-writer \
      /tmp/munto-spec-writer.bak.$(date +%Y%m%d-%H%M)
cp -R /Users/gracegyu/Documents/GitMunto/munto-dev-assistant/.agents/skills/common/docs/munto-spec-review \
      /tmp/munto-spec-review.bak.$(date +%Y%m%d-%H%M)

# 2) 본 폴더의 SKILL.md 를 운영 레포에 덮어쓰기 (상단 <!-- ... --> 주석은 *제거 후* 박을 것)
#    주석은 *기획 메모* 이므로 운영 본문에는 불필요
cp /Users/gracegyu/Documents/GitMunto/munto-dev-assistant-report/munto-dev-assistant/skills/munto-spec-writer/SKILL.md \
   /Users/gracegyu/Documents/GitMunto/munto-dev-assistant/.agents/skills/common/docs/munto-spec-writer/SKILL.md
cp /Users/gracegyu/Documents/GitMunto/munto-dev-assistant-report/munto-dev-assistant/skills/munto-spec-review/SKILL.md \
   /Users/gracegyu/Documents/GitMunto/munto-dev-assistant/.agents/skills/common/docs/munto-spec-review/SKILL.md

# 3) 운영 본문의 상단 <!-- ... --> 주석 제거 (sed 또는 수동)
#    (예시 — 1 회용이므로 검증 후 실행)
# sed -i.bak '/^<!--$/,/^-->$/d' /Users/gracegyu/Documents/GitMunto/munto-dev-assistant/.agents/skills/common/docs/munto-spec-writer/SKILL.md

# 4) 운영 레포 PR 생성 (DEVT-XXX) — 본 폴더 README 변경 이력 링크 첨부
# 5) 머지 후 본 폴더의 해당 SKILL.md 는 *그대로 둠* (history 참조용). 신규 변경 발생 시 본 폴더 본문 먼저 갱신.
```

## 4. Hook 트랙 (별도 PR)

`-report/munto-dev-assistant/.claude-hooks-proposal.json` 은 *PHASE 0~1 (c) Claude Code Hook 자동 캡처* 견본입니다.

| 항목 | 값 |
|------|------|
| 적용 위치 | 사용자 홈 `~/.claude/hooks.json` 또는 운영 레포 `.claude/hooks.json` |
| 산출물 | `projects/{프로젝트명}/sessions/spec-hook-turn-{date}.md` (작성자 본인 디버그용) |
| Git 정책 | `.gitignore` 권장 — *팀 공유 X* |
| 적용 절차 | (a) 스킬 트랙 머지·검증 *완료 후* 별도 DEVT-XXX PR |
| 정책 근거 | TO-BE §4.7.4 (5) (c) |

## 5. 본 폴더 변경 이력

| 일자 | 내용 |
|------|------|
| 2026-05-27 | **`munto-spec-writer/SKILL.md` 적용 대기본 신규** — 시작 전 준비 §3 (cwd 점검) + §"세션 저장 — 자동 (a)" + baseline 동결 직전 안내 메시지. 원본 (운영 레포) 의 모든 기존 본문은 그대로 보존, 신규 단계만 추가. TO-BE §4.7.4 동기화 |
| 2026-05-27 | **`munto-spec-review/SKILL.md` 적용 대기본 신규** — PM 모드 표에 *세션 저장*·*baseline 동결 점검* 행 추가, 시작 전 준비 §3 (cwd 점검) + §"세션 저장 — 자동 (a)" + §"baseline 동결 점검" (🔴 BLOCKER 차단 패턴). PM 모드 (2026-04-30) 본문은 그대로 보존. TO-BE §4.7.4 동기화 |
| 2026-05-27 | **`.claude-hooks-proposal.json` 견본 신규** — (c) Stop Hook 트랙. cwd 검사·spec-hook-turn-*.md 최소 캡처·.gitignore 권장 명시 |
| 2026-05-27 | **본 README 신규** — 보관 원칙·운영 이관 절차·Hook 트랙 분리·변경 이력 |
