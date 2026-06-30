---
name: ai-implementation-scope
description: Control implementation scope for AI Dev Protocol work. Use while editing code after the Chinese spec is confirmed to keep changes limited to the requirement and prevent unrelated refactors, formatting sweeps, dependency upgrades, build-tool changes, temporary artifacts, or workflow files.
---

# AI Implementation Scope

Use during code changes after the Chinese spec is confirmed.

## Preflight

Before editing files, verify:

- One requirement is identified.
- Branch mode is known.
- A Chinese spec exists in the current workflow.
- The user confirmed that spec after branch mode was known.
- The requested edit still matches the confirmed spec.
- The affected files or areas are covered by the confirmed spec, or the scope change has been stated and reconfirmed.

If any item is missing, stop and return to `ai-requirement-intake`, `ai-branch-workflow`, or `ai-spec-writing` as appropriate.

Before editing, briefly record what will change and why it is inside scope.

## Do

- Change only files directly related to the confirmed requirement.
- Follow existing project patterns, helpers, conventions, and tests.
- Run project-appropriate tests, build, static checks, or manual verification.
- Record checks that cannot run and why.
- Keep a short scope record as files are changed: changed area, reason it belongs to the requirement, and any scope change from the confirmed spec.

## Do Not

- No unrelated refactor, formatting sweep, dependency upgrade, CI/build-tool change, large rename, standalone plan file, `.superpowers/`, or workflow artifact.
- No temporary test code, debug script, mock data, or local-only artifact unless explicitly confirmed.

## Scope Expansion

- If a discovered issue blocks the requirement, ask before expanding scope.
- If it does not block, leave it for handoff follow-up notes.
- If a planned file or area does not exist or is no longer relevant, state that it is removed from scope before continuing.

## Output

Record:

- 改了什么
- 为什么属于本次范围
- 范围是否变化；如果变化，说明变化内容和确认状态
- 验证了什么
- 未覆盖或需开发者复核的点

Next: `ai-commit-rules` if committing, then `ai-handoff`.
