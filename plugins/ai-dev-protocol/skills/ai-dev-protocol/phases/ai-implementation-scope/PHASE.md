# AI Implementation Scope

Use during code changes after the Chinese spec is confirmed.

## Preflight

Before editing files, verify:

- One requirement is identified.
- Branch mode is known.
- A Chinese spec exists in the current workflow.
- The user confirmed that spec after branch mode was known.
- The confirmed spec is committed under `docs/specs/` on the `ai/...` branch.
- A local plan exists under `docs/plans/` and is ignored by Git before implementation starts.
- The requested edit still matches the confirmed spec.
- On resumption apply [recovery rules](../../references/recovery.md), comparing reviewed spec and verified revision with current state.
- The affected files or areas are covered by the confirmed spec, or the scope change has been stated and reconfirmed.

If any item is missing, stop and return to [AI Requirement Intake](../ai-requirement-intake/PHASE.md), [AI Branch Workflow](../ai-branch-workflow/PHASE.md), or [AI Spec Writing](../ai-spec-writing/PHASE.md) as appropriate.

Before editing, briefly record what will change and why it is inside scope.

## Implementation Plan

- Before editing, create a local plan file with concrete goals or steps that can be completed and verified. Use the [local plan template](templates/local-plan.md) when structure helps.
- Put every local plan under `docs/plans/{yyyyMMdd}-{short-desc}-plan.md`, using the corresponding `docs/specs/{yyyyMMdd}-{short-desc}.md` basename.
- The `docs/plans/` path must be ignored by Git.
- If missing, establish the ignore rule as necessary workflow setup within the approved task (normally add `docs/plans/` to `.gitignore`) and verify with `git check-ignore` and `git ls-files`. Do not untrack existing user-owned files without approval.
- Confirm the local plan is not tracked by Git before editing implementation files.
- For substantial tasks, include goals for implementation, verification, independent review, and handoff.
- Keep the plan as a local execution aid; do not commit it.
- Update goal status as work progresses instead of only summarizing at the end.
- For tiny single-file edits, a lightweight plan is acceptable, but still state the immediate edit and verification path.
- Borrow only the useful lightweight parts of Superpowers-style work: read necessary context, decompose goals, finish them one by one, guard scope, and review independently. Do not create `.superpowers/` artifacts or hidden workflow state.

## Subagent Collaboration

- When the environment supports subagents and the task is complex enough to benefit, prefer delegating independent side tasks that do not block the main implementation.
- Good subagent tasks include code review, test-gap review, scope/adapter consistency checks, API documentation checks, and security or boundary-condition review.
- For code-change tasks, after implementation and verification, run an independent subagent review when available before final handoff.
- If subagents are unavailable or the task is too small to justify them, perform an explicit self-review checklist and record the reason in handoff.
- Review findings must be fixed before delivery or recorded as accepted residual risk.
- Subagent review does not replace the developer's final review, self-test, integration testing, PR, merge, or code-quality ownership.

## Do

- Change only files directly related to the confirmed requirement.
- Follow existing project patterns, helpers, conventions, and tests.
- Run project-appropriate tests, build, static checks, or manual verification.
- Record checks that cannot run and why.
- Record the revision/worktree contents each check covered; invalidate affected results after relevant edits.
- Keep a short scope record as files are changed: changed area, reason it belongs to the requirement, any scope change from the confirmed spec, and plan/subagent review status when applicable.

## Do Not

- No unrelated refactor, formatting sweep, dependency upgrade, CI/build-tool change, large rename, tracked plan file, `.superpowers/`, or external workflow artifact.
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
- spec 文档路径和提交状态
- plan/goals 完成情况
- 本地 plan 路径和 Git 忽略状态
- subagent 或独立审查情况；如果未执行，说明原因和替代自检
- 验证了什么
- 未覆盖或需开发者复核的点

Next: [AI Commit Rules](../ai-commit-rules/PHASE.md) if committing, then [AI Handoff](../ai-handoff/PHASE.md).
