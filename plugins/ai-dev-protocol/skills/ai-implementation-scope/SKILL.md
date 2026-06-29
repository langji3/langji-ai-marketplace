---
name: ai-implementation-scope
description: Control implementation scope for AI Dev Protocol work. Use while editing code after the Chinese spec is confirmed to keep changes limited to the requirement and prevent unrelated refactors, formatting sweeps, dependency upgrades, build-tool changes, temporary artifacts, or workflow files.
---

# AI Implementation Scope

Use during code changes after the Chinese spec is confirmed.

## Do

- Change only files directly related to the confirmed requirement.
- Follow existing project patterns, helpers, conventions, and tests.
- Run project-appropriate tests, build, static checks, or manual verification.
- Record checks that cannot run and why.

## Do Not

- No unrelated refactor, formatting sweep, dependency upgrade, CI/build-tool change, large rename, standalone plan file, `.superpowers/`, or workflow artifact.
- No temporary test code, debug script, mock data, or local-only artifact unless explicitly confirmed.

## Scope Expansion

- If a discovered issue blocks the requirement, ask before expanding scope.
- If it does not block, leave it for handoff follow-up notes.

## Output

Record:

- 改了什么
- 为什么属于本次范围
- 验证了什么
- 未覆盖或需开发者复核的点

Next: `ai-commit-rules` if committing, then `ai-handoff`.
