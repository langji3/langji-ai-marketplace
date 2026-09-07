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

Spec confirmation and implementation approval do not authorize merge-back. Apply [authorization rules](../../references/authorization.md): an affirmative reply such as `可以` or `OK` to this exact proposal is valid. Ask only when its referent is ambiguous; do not require special wording.

## Do

1. Confirm AI branch and developer branch without switching branches.
2. Confirm spec, local plan, implementation commits, working tree, verification and risks. Apply [recovery rules](../../references/recovery.md) if the source/target advanced; verify the intended combined tree in isolation before requesting approval.
3. Report merge readiness, the target developer branch, the commits to merge, and the proposed Chinese squash commit message.
4. Ask a dedicated authorization question such as: `实现和验证已完成，是否同意将 ai/... squash merge 回 developer/...？`
5. Wait for an explicit affirmative answer to this proposal. Reuse existing approval for the unchanged proposal; do not modify the developer branch without it.
6. Re-check both commit IDs and working-tree state. Changed heads require a recomputed proposal and relevant checks; changed merge contents/target require renewed approval.
7. Use the approved developer branch's idle, clean worktree, or switch only when another task is not using it.
8. Squash merge the approved `ai/...` branch.
9. Create one Chinese `feat:` / `fix:` commit.
10. Run relevant verification against the resulting developer tree. If unavailable, report the unverified result. Failed checks stop downstream integration without automatic reset/revert.

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
