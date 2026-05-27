# Jira 이슈 초안

## 제목 (Summary)

`Agentic Dev Chain TO-BE 정책·적용 대기본 — 개발자 리뷰 요청`

---

## 설명 (Description)

| 항목 | 내용 |
| --- | --- |
| **배경** | Munto 개발팀은 AI Agent 기반 **Agentic Dev Chain** 으로 Spec 작성 → 설계 → 구현 → 검증 흐름을 자동화하고, 핵심 판단만 사람이 하면 나머지는 **24시간 무인 실행**까지 이어지는 개발 사이클을 목표로 한다. 현재 운영 중인 `munto-dev-assistant` 하네스와 실제 개발 프로세스 사이의 간극을 줄이기 위해, AS-IS 진단·TO-BE 정책·적용 대기 산출물을 정리해 두었다. 본 이슈는 **운영 레포에 반영하기 전** 팀 합의를 받기 위한 리뷰 요청이다. |
| **목적** | 아래 3개 Notion 문서와 1개 GitHub 임시 레포를 검토하여 **정책·실물 산출물의 개선점·누락·충돌**을 찾고, 의견을 취합한다. 리뷰 결과를 바탕으로 `munto-dev-assistant` 수정 범위를 확정하고, **개발 사이클 적용 준비**를 마친다. |
| **절차** | **1단계 — 공통 (전원·필수)**<br>• [팀 개발자 브리핑 (요약)](https://www.notion.so/Agentic-Dev-Chain-TO-BE-36de2bc7639d8093abbbe41b623252d7) — **10~15분 정독** *(전원)*<br>• [AS-IS](https://www.notion.so/Munto-Dev-Assistant-AS-IS-36de2bc7639d808d9cedd2252484fd92) / [TO-BE](https://www.notion.so/Agentic-Dev-Chain-Munto-TO-BE-36de2bc7639d8052b13fc49575c10e56) — **전체 정독 불필요**. brief 후 *거슬리거나 본인 업무와 맞닿는 절* 만 발췌<br><br>**2단계 — 실물 스캔 (전원·발췌)**<br>• [munto-dev-assistant-tobe-temp](https://github.com/Munto-dev/munto-dev-assistant-tobe-temp) — PR 없이 레포 열람. **README + 본인과 연관된 파일만** *(예: Spec 작성 → `skills/munto-spec-*`, IP·프로젝트 구조 → `ip-standard.md`·`projects/_template/`, 대형 `spec-standard.md` 는 발췌)*. *안 읽은 범위는 의견 없어도 됨* — 내일 논의에서 같이 정리<br><br>**3단계 — 의견 취합**<br>• **Notion** → 각 페이지 comment / **GitHub 임시 레포** → **본 Jira 이슈 댓글**에 **BLOCKER / 개선 / 질문** 구분 *(읽은 범위 기준)*<br><br>**4단계 — 반영·적용 (리뷰 PASS 후, 하네스 담당 주도)**<br>• 임시 레포 → 운영 레포 `munto-dev-assistant` 일괄 이관 PR<br>• 1개 프로젝트 파일럿으로 개발 사이클 적용<br>• 파일럿 결과 반영 후 `munto-dev-assistant` 재수정·반복 |
| **고려요소** | • **역할 분리**: Notion 3종 = *원칙·방향* / GitHub 임시 레포 = *실물 (Skill·IP·Spec 표준)* — 둘 사이 정합성도 함께 본다.<br>• **정독 범위**: `spec-standard.md` 등 대형 문서는 **전체 정독 의무 없음**. 본인 도메인(BE/FE/App/하네스) 관련 부분 위주.<br>• **정책 원문 위치**: TO-BE·AS-IS·brief 는 **Notion** (절차 1단계 링크). 임시 GitHub 레포 본문도 동일 Notion URL 을 참조한다.<br>• **코멘트 시**: *"안 읽었지만"* 보다 **구체적 위치 (문서·섹션·파일)** 와 *대안 또는 이유* 를 적어 주면 취합이 빠르다.<br>• **적용 시점**: 본 리뷰 합의 전까지 운영 레포 `munto-dev-assistant` 는 **변경하지 않는다**. |
| **기대결과** | • 도메인별 리뷰 코멘트 취합 완료 (BLOCKER / 개선 / 질문 분류)<br>• `munto-dev-assistant` **적용 범위·우선순위·담당자** 확정<br>• 리뷰 PASS 후 운영 레포 이관 PR 1건 생성<br>• 1개 프로젝트 파일럿 착수 — Agentic Dev Chain TO-BE 가 **실제 개발 사이클에서 동작**하는지 1회 검증<br>• 파일럿 피드백 반영 계획 (2차 수정 필요 항목 목록) |

---

## comment by 전규현

개발팀 (@김범진 @홍진영 @김세현 @김도연 )

위 Notion 3종과 GitHub 임시 레포를 검토해 주세요. **전원 brief 10~15분** 은 필수이고, AS-IS·TO-BE·GitHub 는 **전체 정독 불필요** — 본인과 연관된 부분만 보셔도 됩니다. **Notion** 의견은 각 페이지 comment, **GitHub** 는 PR 없이 레포만 보시고 의견은 **본 Jira 댓글**에 **BLOCKER / 개선 / 질문** 으로 남겨 주세요.
가능하면 **내일** 모여서 의견 정리하고 다음 단계 논의하겠습니다.
