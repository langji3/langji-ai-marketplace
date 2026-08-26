# AI Merge Back

Use after verified work is complete on an `ai/...` branch. Treat merge-back as a separate authorization gate.

## Readiness Preconditions

- Current branch is `ai/...`.
- Source developer branch is known.
- Implementation is complete.
- Implementation changes are committed on the AI branch.
- Spec document is committed under `docs/specs/`.
- Local plan was used and is not tracked by Git.
- Verification ran, or blocker is recorded.
- Working tree is clean except intended committed changes.

## Execution Authorization

Before any command that switches to or modifies the developer branch, the developer must explicitly approve this specific merge-back after receiving the completion and verification summary.

Spec confirmation, implementation approval, commit approval, earlier workflow consent, and task-completion instructions do not authorize merge-back. A vague reply such as `ok` or `继续` is not enough; require a clear merge-back instruction such as `同意合回`、`可以合回` or `合并吧`.

## Do

1. Confirm AI branch and developer branch without switching branches.
2. Confirm spec, local plan, implementation commits, working tree, verification, and known risks.
3. Report merge readiness, the target developer branch, the commits to merge, and the proposed Chinese squash commit message.
4. Ask a dedicated authorization question such as: `实现和验证已完成，是否同意将 ai/... squash merge 回 developer/...？`
5. Stop and wait. Do not switch to or modify the developer branch before an explicit affirmative answer such as `同意合回`、`可以合回` or `合并吧`.
6. After approval, re-check branch and working-tree state.
7. Switch to the approved developer branch.
8. Squash merge the approved `ai/...` branch.
9. Create one Chinese `feat:` / `fix:` commit.
10. Run or recommend post-merge verification.

## No Approval Or Rejection

- If approval is missing, finish the handoff on the AI branch with merge-back marked `等待开发者授权`; do not infer consent.
- If the developer declines or withdraws approval, mark merge-back `未授权` or `已取消` and leave the developer branch untouched.
- Do not reset, restore, rebase, cherry-pick, merge, commit, or otherwise clean up the developer branch in response to rejection.
- If any developer-branch mutation already started, stop, report the exact Git state and commands already run, and ask for explicit instructions before corrective action.

## Stop

Stop on missing explicit approval, unknown target branch, wrong current branch, dirty tree, conflicts, failed verification without accepted risk, or developer cancellation. Record the status in handoff; completed work may remain safely on the AI branch.

## Output

Record:

- AI 分支
- 开发者分支
- spec 文档路径和提交状态
- 本地 plan 执行状态和未追踪状态
- AI 分支实现提交状态
- 开发者授权状态
- squash commit message
- merge-back 状态
- post-merge verification 状态

State that the developer now leads review, 联调, checks, and downstream merges.
