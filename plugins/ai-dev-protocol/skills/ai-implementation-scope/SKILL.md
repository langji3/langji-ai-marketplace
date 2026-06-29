---
name: ai-implementation-scope
description: Control implementation scope for AI Dev Protocol work. Use while editing code to keep changes limited to the confirmed requirement and prevent unrelated refactors, formatting sweeps, dependency upgrades, build-tool changes, or workflow artifacts.
---

# AI Implementation Scope

Use this skill during implementation after the Chinese spec has been confirmed.

## Rules

- Only change files directly related to the confirmed requirement.
- Do not include unrelated refactors, formatting sweeps, dependency upgrades, CI/build-tool changes, large renames, standalone plan files, `.superpowers/`, or temporary workflow artifacts unless the user explicitly asks.
- Prefer the existing project patterns and helper APIs.
- If a shared module, public type, or base config must be changed, explain why in the handoff.

## Extra Issues Found During Work

When discovering an additional issue:

1. Decide whether it blocks the current requirement.
2. If it blocks, explain the reason and ask for confirmation before expanding scope.
3. If it does not block, leave it for the handoff follow-up notes.

## Before Delivery

Run project-appropriate verification. If a check cannot run, capture the command, reason, and closest alternative check for `ai-handoff`.

