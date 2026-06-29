---
name: ai-branch-workflow
description: Manage AI Dev Protocol branch mode decisions and AI branch naming. Use before creating, validating, switching to, or committing on a work branch, especially when deciding between the default developer-branch-to-ai-branch workflow and the compatibility mode of working directly on an existing requirement branch.
---

# AI Branch Workflow

Use this skill before implementation to decide where AI should work.

## Default Mode

Default mode is designed for small teams where each developer has a personal development branch that aggregates multiple AI-assisted requirements.

```text
developer/<name>
  -> ai/{yyyyMMdd}-{developer}-{short-desc}
  <- squash merge back to developer/<name>
```

Rules:

- Treat the developer branch as the aggregation and review branch.
- Create one `ai/...` branch per clear requirement.
- Use each `ai/...` branch as a temporary implementation branch.
- After implementation and verification, use `ai-merge-back` to squash merge the AI branch back to the developer branch.
- The developer leads review, 联调, checks, and downstream merges from the developer branch.

## Compatibility Mode

If the current branch is already a clear requirement branch, AI may work directly on it:

```text
feature/order-filter
fix/user-api-field
hotfix/login-timeout
```

Use compatibility mode only when:

- The branch clearly represents one requirement, fix, or hotfix.
- The user or team does not want an extra `ai/...` branch.
- The branch is not an environment or trunk branch.

In compatibility mode, skip `ai/...` branch creation and skip `ai-merge-back`.

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
2. Determine whether it is a developer branch, a requirement branch, or a forbidden direct work branch.
3. If it is a developer branch, create or suggest one `ai/...` branch for the current requirement.
4. If it is a requirement branch, confirm whether to work directly or create an optional `ai/...` branch.
5. If it is a forbidden direct work branch, stop and ask the user to switch or confirm an exception.
6. Record the selected branch mode for handoff.

## Exceptions

Branch workflow can be skipped when:

- The task is read-only.
- The current directory is not a Git repository.
- The user explicitly asks not to create or switch branches.
- The environment lacks permission to run Git operations.

Mention the exception in the final handoff.

