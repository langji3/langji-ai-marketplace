---
name: ai-merge-back
description: Squash merge completed AI work back to the developer branch in AI Dev Protocol. Use after implementation and verification on an ai/... branch when work should return to the developer aggregation branch.
---

# AI Merge Back

Use after verified work is complete on an `ai/...` branch.

## Preconditions

- Current branch is `ai/...`.
- Source developer branch is known.
- Implementation is complete.
- Implementation changes are committed on the AI branch.
- Spec document is committed under `docs/specs/`.
- Local plan was used and is not tracked by Git.
- Verification ran, or blocker is recorded.
- Working tree is clean except intended committed changes.
- Merge-back is the standard required return path for completed AI work.

## Do

1. Confirm AI branch and developer branch.
2. Confirm spec document path and spec commit status.
3. Confirm local plan execution status and that the plan file is not tracked.
4. Confirm implementation commit status on the AI branch.
5. Ensure no uncommitted changes.
6. Switch to developer branch.
7. Squash merge `ai/...`.
8. Create one Chinese `feat:` / `fix:` commit.
9. Run or recommend post-merge verification.

## Stop

Stop on unknown target branch, wrong current branch, dirty tree, conflicts, failed verification without accepted risk, or explicit user cancellation of the task. Record the blocker in handoff; do not silently skip merge-back for completed work.

## Output

Record:

- AI 分支
- 开发者分支
- spec 文档路径和提交状态
- 本地 plan 执行状态和未追踪状态
- AI 分支实现提交状态
- squash commit message
- merge-back 状态
- post-merge verification 状态

State that the developer now leads review, 联调, checks, and downstream merges.
