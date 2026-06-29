---
name: ai-branch-workflow
description: Manage AI Dev Protocol branch mode decisions and AI branch naming. Use before creating, validating, switching to, or committing on a work branch, especially when auto-detecting whether the current branch is a requirement branch, personal developer branch, existing ai/... branch, or forbidden trunk/environment branch.
---

# AI Branch Workflow

Use this skill before implementation to inspect the current branch name and decide where AI should work.

## Branch Mode Auto Detection

Classify the current branch before implementation:

1. **Requirement branch mode**: work directly on the current requirement branch.
2. **Personal branch mode**: create one `ai/...` branch from the current personal developer branch.
3. **Existing AI branch mode**: continue on the current `ai/...` branch and identify the source developer branch for merge-back.
4. **Forbidden branch**: stop on trunk or environment branches.
5. **Ambiguous branch**: ask the user to classify the branch before changing code.

Prefer project rules from `AGENTS.md`, `CLAUDE.md`, or equivalent local instructions when they define exact branch patterns. Use the heuristics below only when project rules do not say.

## Requirement Branch Mode

If the current branch already represents one clear requirement, task, bug fix, or hotfix, AI works directly on it:

```text
feature/order-filter
feat/order-filter
fix/user-api-field
bugfix/user-api-field
hotfix/login-timeout
task/image-job-create
story/payment-callback
requirement/order-export
JIRA-123-order-export
```

Use requirement branch mode when:

- The branch name contains a requirement-oriented prefix such as `feature/`, `feat/`, `fix/`, `bugfix/`, `hotfix/`, `task/`, `story/`, or `requirement/`.
- The branch name contains a ticket-style identifier plus a short requirement description, such as `JIRA-123-order-export`.
- The branch clearly maps to one requirement, fix, task, or hotfix.
- The branch is not a trunk or environment branch.

In requirement branch mode:

- Do not create an extra `ai/...` branch by default.
- Do not run `ai-merge-back`.
- The developer reviews, self-tests, performs integration testing, and opens the downstream PR from this requirement branch.

## Personal Branch Mode

Personal branch mode is designed for small teams where each developer has a personal development branch that aggregates multiple AI-assisted requirements.

```text
developer/<name>
dev/<name>
<name>/dev
<name>/develop
  -> ai/{yyyyMMdd}-{developer}-{short-desc}
  <- squash merge back to developer/<name>
```

Use personal branch mode when:

- The project rules identify the current branch as the developer's personal branch.
- The branch follows a personal developer pattern such as `developer/<name>`, `dev/<name>`, `<name>/dev`, `<name>/develop`, `personal/<name>`, or `users/<name>`.
- The branch is an aggregation branch for multiple AI-assisted requirements rather than one specific requirement.

Rules:

- Treat the developer branch as the aggregation and review branch.
- Create one `ai/...` branch per clear requirement.
- Use each `ai/...` branch as a temporary implementation branch.
- After implementation and verification, use `ai-merge-back` to squash merge the AI branch back to the developer branch.
- The developer leads review, 联调, checks, and downstream merges from the developer branch.

## Existing AI Branch Mode

If the current branch already starts with `ai/`, continue the current AI work instead of creating a nested AI branch.

Before implementation or merge-back:

- Confirm the branch name matches `ai/{yyyyMMdd}-{developer}-{short-desc}`.
- Identify the source developer branch from user input, project rules, branch description, or recent Git history.
- If the source developer branch is unknown and merge-back is expected, ask the user before proceeding.

## Forbidden Direct Work Branches

Do not directly implement on environment or trunk branches unless the user explicitly confirms this is the team rule:

```text
main
master
dev
develop
site
staging
test
prod
production
```

If currently on one of these branches, ask the user to switch to a developer branch or requirement branch before implementation.

## Ambiguous Branches

If a branch could be either a personal branch or a requirement branch, ask before changing code. Examples:

```text
wzh
mt
dev-wzh
login
order
```

Ask a concise question such as:

```text
当前分支 `<branch>` 是个人开发分支还是当前需求分支？如果是个人分支，我会创建 `ai/...` 分支；如果是需求分支，我会直接在当前分支工作。
```

## AI Branch Naming

Default AI branch naming:

```text
ai/{yyyyMMdd}-{developer}-{short-desc}
```

Example:

```text
ai/20260626-zhangsan-order-status-filter
```

If the developer identifier is unknown, ask the user. Do not invent it.

## Process

1. Check the current branch.
2. Apply project-defined branch patterns first; otherwise use the auto-detection heuristics.
3. If it is a requirement branch, work directly on it and skip merge-back.
4. If it is a personal developer branch, create or suggest one `ai/...` branch for the current requirement.
5. If it is an existing `ai/...` branch, continue there and identify the source developer branch.
6. If it is a forbidden direct work branch, stop and ask the user to switch or confirm an exception.
7. If it is ambiguous, ask the user to classify the branch.
8. Record the selected branch mode for handoff.

## Exceptions

Branch workflow can be skipped when:

- The task is read-only.
- The current directory is not a Git repository.
- The user explicitly asks not to create or switch branches.
- The environment lacks permission to run Git operations.

Mention the exception in the final handoff.
