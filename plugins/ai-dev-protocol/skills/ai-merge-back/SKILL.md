---
name: ai-merge-back
description: Squash merge completed AI work back to the developer branch in AI Dev Protocol personal branch mode. Use after implementation and verification on an ai/... branch when the work should return to the developer's aggregation branch for human-led review, integration testing, and downstream merges. Do not use for requirement branch mode.
---

# AI Merge Back

Use this skill only in personal branch mode, after AI implementation and verification are complete on an `ai/...` branch.

## Purpose

The `ai/...` branch is a temporary implementation branch. The developer branch is the aggregation branch where the developer leads review, 联调, checks, and downstream merges.

Do not use merge-back when AI worked directly on a requirement branch such as `feature/...`, `fix/...`, `task/...`, or a ticket-named branch. In requirement branch mode, the developer continues review, self-test, integration testing, and PR from that same requirement branch.

## Preconditions

Before merge-back:

- Current branch is an `ai/...` branch.
- The source developer branch is known.
- The requirement has been implemented.
- Verification has run, or the reason it cannot run is recorded.
- Working tree is clean except for intended committed changes.
- The user has not explicitly disabled merge-back.

If any precondition is not satisfied, stop and explain what is missing.

## Process

1. Confirm the current branch and the target developer branch.
2. Confirm there are no uncommitted changes.
3. Switch to the developer branch.
4. Update the developer branch if the team workflow requires it and the user permits it.
5. Squash merge the `ai/...` branch into the developer branch.
6. Create one Chinese squash commit using `feat:` or `fix:`.
7. Run or recommend post-merge verification.
8. Hand off to the developer for review, 联调, checks, and downstream merges.

## Stop Conditions

Stop instead of forcing merge-back when:

- The target developer branch is unknown.
- The current branch is not an `ai/...` branch.
- The working tree is dirty.
- Merge conflicts occur.
- Verification failed and the user has not accepted the risk.
- The user or team uses requirement branch mode.

## Handoff Note

After merge-back, state:

```text
AI implementation has been squash merged back to the developer branch. The developer now leads review, 联调, final checks, and any merge to dev/site/prod or other environment branches.
```
