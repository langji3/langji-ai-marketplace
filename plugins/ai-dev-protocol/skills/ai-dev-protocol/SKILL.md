---
name: ai-dev-protocol
description: Route AI-assisted development work through the AI Dev Protocol workflow skills. Use when a development task may require requirement clarification, automatic branch-mode detection from the current branch name, Chinese requirement specs, implementation scope control, optional AI branch merge-back, Chinese commits, verified handoff, or Apifox API sync summaries.
---

# AI Dev Protocol

AI Dev Protocol 是团队 AI 辅助开发流程规约的总入口 skill。进入实现前，先根据当前分支命名风格选择分支模式：需求分支走需求分支模式，个人开发分支走个人分支模式。

如果以 Codex plugin 形式安装，技能可能显示为 `ai-dev-protocol:<skill-name>`；下方名称指对应的 skill basename。

## Core Model

Personal branch mode:

```text
developer/<name>
  -> ai/{yyyyMMdd}-{developer}-{short-desc}
  -> ai/{yyyyMMdd}-{developer}-{another-desc}
  <- squash merge back to developer/<name>
```

Requirement branch mode:

```text
feature/<requirement>
  -> AI works directly on this requirement branch
```

Use requirement branch mode when the current branch already represents one explicit requirement, fix, task, or hotfix. Do not create an extra `ai/...` branch in this mode unless the user explicitly asks for one.

## Branch Mode Auto Detection

Use `ai-branch-workflow` to inspect the current branch before implementation.

- If the current branch is a requirement branch, use requirement branch mode and work directly on it.
- If the current branch is a personal developer branch, use personal branch mode and create one `ai/...` branch from it.
- If the current branch is an existing `ai/...` branch, continue personal branch mode and identify the source developer branch before merge-back.
- If the current branch is a trunk or environment branch, stop and ask the user to switch branches or confirm an exception.
- If the branch style is ambiguous, ask the user whether it is a requirement branch or a personal developer branch.

## Workflow Routing

Use the phase skill that matches the current work:

- `ai-requirement-intake`: clarify the requirement, enforce one requirement per AI work unit, and decide whether the task is ready for a spec.
- `ai-branch-workflow`: inspect the current branch name and decide whether to use requirement branch mode, personal branch mode, or stop on a trunk/environment branch.
- `ai-spec-writing`: write the Chinese requirement spec and wait for user confirmation before implementation.
- `ai-implementation-scope`: keep code edits inside the confirmed requirement and prevent unrelated refactors, formatting, dependency changes, or workflow artifacts.
- `ai-commit-rules`: prepare Chinese `feat:` / `fix:` commit messages for AI work and merge-back commits.
- `ai-merge-back`: after verification, squash merge an AI branch back to the developer branch when personal branch mode is used.
- `ai-handoff`: produce the final delivery summary with verification results, risks, review/联调 handoff notes, and follow-up notes.
- `ai-apifox-sync`: produce the Apifox sync summary whenever API behavior or contracts changed.

## Hard Gates

Do not start implementation until all applicable gates are satisfied:

1. Requirement scope is clear and maps to one independent requirement.
2. The branch mode is known: requirement branch mode, personal branch mode, or existing `ai/...` branch mode.
3. In personal branch mode, the developer branch is known and the AI branch is expected to be created from it.
4. The Chinese requirement spec is written and confirmed.
5. Planned edits are limited to the current requirement.
6. Verification expectations are stated before delivery.

If any gate is not satisfied, use the matching phase skill before proceeding.

## Standard Flow

1. Use `ai-requirement-intake` when the task enters.
2. Use `ai-branch-workflow` to auto-detect branch mode from the current branch and create or validate the work branch.
3. Use `ai-spec-writing` before implementation.
4. Use `ai-implementation-scope` during code changes.
5. Use project-appropriate verification before delivery.
6. Use `ai-commit-rules` before commits.
7. In personal branch mode, use `ai-merge-back` to squash merge the AI branch back to the developer branch after verification.
8. Use `ai-handoff` for final delivery and make clear that the developer now leads review, 联调, and downstream merges.
9. Use `ai-apifox-sync` in addition to handoff if API behavior or contracts changed.

## Checklist

Before implementation:

- [ ] Requirement is one independent requirement.
- [ ] Scope, non-goals, and affected areas are clear.
- [ ] Current branch naming style has been checked.
- [ ] Branch mode is chosen and explained.
- [ ] Personal branch mode has a known developer branch and an `ai/...` branch.
- [ ] Requirement branch mode has a confirmed requirement branch.
- [ ] Chinese spec is written and confirmed.

During implementation:

- [ ] Edits stay inside the approved requirement.
- [ ] No unrelated refactor, formatting sweep, dependency upgrade, or generated workflow artifact is included.
- [ ] Any discovered out-of-scope issue is reported instead of silently fixed.

Before final delivery:

- [ ] Verification commands or manual checks are run, or blockers are explained.
- [ ] Personal branch mode either completed merge-back or explains why merge-back was not done.
- [ ] Delivery states that the developer leads review, 联调, checks, and downstream merges.
- [ ] API changes include Apifox sync summary.
- [ ] Commit messages follow the Chinese `feat:` / `fix:` rule.
