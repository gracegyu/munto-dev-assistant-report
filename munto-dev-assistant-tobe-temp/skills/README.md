# `munto-dev-assistant-tobe-temp/skills/` — *적용 대기 본문* 미러

본 폴더는 **운영 레포 `Munto-dev/munto-dev-assistant` 의 `.agents/skills/common/docs/` 스킬 본문 *교체 대기본***을 임시 보관하는 *기획 미러* 입니다.

> *외부 공유본* — 본 폴더는 임시 GitHub 레포 [`Munto-dev/munto-dev-assistant-tobe-temp`](https://github.com/Munto-dev/munto-dev-assistant-tobe-temp) 에 게시되어 있습니다. 본 README 의 *경로 표기* 는 모두 *본 임시 레포 clone 후 그 안* 또는 *운영 레포 (사내 GitHub)* 기준 *상대 경로* 입니다.

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

> 사전 준비: 본 임시 GitHub 레포와 운영 레포를 *같은 부모 디렉토리* 에 clone (예: `~/work/munto-dev-assistant-tobe-temp/` + `~/work/munto-dev-assistant/`). 아래 명령은 *임시 레포 clone 디렉토리 내에서* 실행한다고 가정 (변수 `OPS_REPO` 로 운영 레포 절대 경로 1 회 박음).

```bash
# 0) 운영 레포 절대 경로를 1 회 박음 (각자 PC 의 운영 레포 clone 위치)
export OPS_REPO=~/work/munto-dev-assistant   # 본인 환경에 맞게 수정

# 1) 백업 (만일에 대비)
cp -R "$OPS_REPO/.agents/skills/common/docs/munto-spec-writer" \
      /tmp/munto-spec-writer.bak.$(date +%Y%m%d-%H%M)
cp -R "$OPS_REPO/.agents/skills/common/docs/munto-spec-review" \
      /tmp/munto-spec-review.bak.$(date +%Y%m%d-%H%M)

# 2) 본 폴더의 SKILL.md 를 운영 레포에 덮어쓰기 (상단 <!-- ... --> 주석은 *제거 후* 박을 것)
#    주석은 *기획 메모* 이므로 운영 본문에는 불필요
#    아래 명령은 본 임시 레포 (munto-dev-assistant-tobe-temp) 의 clone 루트에서 실행
cp ./skills/munto-spec-writer/SKILL.md \
   "$OPS_REPO/.agents/skills/common/docs/munto-spec-writer/SKILL.md"
cp ./skills/munto-spec-review/SKILL.md \
   "$OPS_REPO/.agents/skills/common/docs/munto-spec-review/SKILL.md"

# 3) 운영 본문의 상단 <!-- ... --> 주석 제거 (sed 또는 수동)
#    (예시 — 1 회용이므로 검증 후 실행)
# sed -i.bak '/^<!--$/,/^-->$/d' "$OPS_REPO/.agents/skills/common/docs/munto-spec-writer/SKILL.md"

# 4) 운영 레포 PR 생성 (DEVT-XXX) — 본 폴더 README 변경 이력 링크 첨부
# 5) 머지 후 본 임시 레포는 *아카이브/삭제*. 신규 변경이 추가로 필요할 경우 운영 레포 본문을 직접 수정 (본 임시 레포는 *1 회성*).
```

## 4. Hook 트랙 (별도 PR)

본 임시 레포 루트의 [`.claude-hooks-proposal.json`](../.claude-hooks-proposal.json) 은 *PHASE 0~1 (c) Claude Code Hook 자동 캡처* 견본입니다.

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
| 2026-05-27 | **작성자별 파일 분리 정책 (옵션 α) 적용 — 멀티 작성자 race·merge conflict 회피** *(TO-BE §2.3 ⑧ 컨텍스트 단절 원칙 신설에 동기화)* — ① `munto-spec-writer/SKILL.md` 적용 대기본 — 파일명 `spec-session-{date}.md` → `spec-session-{date}-{slack-handle}.md`. 시작 전 준비 §4 신설 (`{slack-handle}` 자동 추출 4 단 우선순위: 명시 인자 → `git config user.email` 의 `@` 앞 → `$USER` → 사용자 1 회 질문). 박을 내용 첫 행에 *작성자 Slack 핸들* 항목 추가. 파일 헤더에 *작성자별 분리 정책* 안내 + `cat .* | sort` 시간순 통합 명령 명시. ② `munto-spec-review/SKILL.md` 적용 대기본 — 파일명 `spec-review-{date}-{doc}.md` → `spec-review-{date}-{doc}-{slack-handle}.md`. 시작 전 준비 §4 신설 (writer 와 동일 정책 cross-link). 박을 내용에 *리뷰어 Slack 핸들* 항목 추가. ③ `.claude-hooks-proposal.json` — Hook 스크립트의 파일명 패턴에 `{slack-handle}` 추가 (bash 내부에서 `git config user.email \| cut -d@ -f1` 추출 + kebab-case slugify + fallback `$USER` → `unknown`). 주석 `_comment_slack_handle` 신설. 파일명 패턴 `spec-hook-turn-{date}-{slack-handle}.md`. ④ baseline-handoff.md 는 *프로젝트당 1 회 Owner 단독 작성* 이므로 변경 없음 (handle 불요) |
| 2026-05-27 | **용어 `{slack-handle}` → `{author-id}` 일괄 변경 + 자동 추출 정책 폐기** *(사용자 본인 환경에서 자동 추출 3 단 추출이 모두 의도값과 어긋남 — git config = ewoosoft 이메일, $USER = PC 계정명, 모두 Munto Slack 핸들과 무관 — 으로 검증 실패)* — ① 용어 변경 — `{slack-handle}` 이 *Slack 만 강조* 해서 *Slack 미사용 도구·다른 식별자 (이메일 ID·GitHub username)* 사용자에게 오해 발생. *역할 명확한* `{author-id}` 로 변경 (= 팀이 합의한 작성자 식별 문자열, Munto 권장 = Slack 멘션 핸들). ② 자동 추출 폐기 — `git config user.email` 추출은 *전 회사 이메일 잔존*·*오픈소스용 별도 계정*·*PC 계정명 불일치* 등으로 사용자 의도와 어긋날 확률 높음. *공식 정책에서 제거*. ③ 신정책 = 2 단계 — (1) 호출 시 명시 인자 `author=gyuhyeon.jeon` (권장 디폴트), (2) 미명시 시 세션 첫 호출에 1 회 질문 + 세션 캐싱. ④ 빈 값 입력 시 *세션 저장 자체 스킵 + 경고* — `unknown` 으로 박지 않음 (익명 산출물 추적 가치 0). ⑤ `munto-spec-writer/SKILL.md` 적용 대기본 — 시작 전 준비 §4 재작성 (4 단 → 2 단), `revision` 갱신, *작성자 Slack 핸들* 헤더 항목 → *작성자 ID (`{author-id}`)*. ⑥ `munto-spec-review/SKILL.md` 적용 대기본 — 동일 (writer cross-link 유지), *리뷰어 Slack 핸들* → *리뷰어 ID (`{author-id}`)*. ⑦ `.claude-hooks-proposal.json` — Hook 은 *비대화형 환경* 이라 질문 불가 → *환경변수 `MUNTO_AUTHOR_ID` 만* 사용, 미설정 시 *silent no-op*. 사용자가 `~/.zshrc` 에 `export MUNTO_AUTHOR_ID=gyuhyeon.jeon` 1 회 설정. git config 추출·`unknown` fallback 모두 제거. `_comment_slack_handle` → `_comment_author_id`. `_comment_apply` 에 환경변수 설정 단계 명시. ⑧ 토큰 `{slack-handle}` → `{author-id}` 일괄 치환 — writer 5 곳, review 5 곳, hook 견본 5 곳 |
