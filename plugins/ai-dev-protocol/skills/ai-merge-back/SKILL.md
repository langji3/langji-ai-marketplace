---
name: ai-merge-back
description: Squash merge completed AI work back to the developer branch in AI Dev Protocol personal branch mode. Use after implementation and verification on an ai/... branch when work should return to the developer aggregation branch. Do not use for requirement branch mode.
---

# AI Merge Back

Use only in personal branch mode after verified work is complete on an `ai/...` branch.

## Preconditions

- Current branch is `ai/...`.
- Source developer branch is known.
- Implementation is complete.
- Verification ran, or blocker is recorded.
- Working tree is clean except intended committed changes.
- User has not disabled merge-back.

## Do

1. Confirm AI branch and developer branch.
2. Ensure no uncommitted changes.
3. Switch to developer branch.
4. Squash merge `ai/...`.
5. Create one Chinese `feat:` / `fix:` commit.
6. Run or recommend post-merge verification.

## Stop

Stop on unknown target branch, wrong current branch, dirty tree, conflicts, failed verification without accepted risk, or requirement branch mode.

## Output

Record:

- AI 分支
- 开发者分支
- squash commit message
- merge-back 状态
- post-merge verification 状态

State that the developer now leads review, 联调, checks, and downstream merges.
