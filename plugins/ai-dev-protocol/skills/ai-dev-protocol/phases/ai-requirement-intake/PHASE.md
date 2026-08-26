# AI Requirement Intake

Use before spec writing when the request is not clearly one actionable requirement.
Also use it when a natural design discussion is likely to become code work, even if the user has not said "implement" yet.

## Do

- Confirm the problem, expected result, scope, non-goals, affected areas, and verification.
- Keep discussion in Chinese unless the user asks otherwise.
- Keep code identifiers, API paths, table names, config keys, commands, and file paths in English.
- Split bundled work; handle only one independent requirement per AI work unit.
- When the user adds missing business rules, summarize the clarified requirement before moving to branch workflow.
- If the user asks "next step" after requirement discussion, close intake first, then move to [AI Branch Workflow](../ai-branch-workflow/PHASE.md); do not jump to implementation.

## Stop

Ask before continuing when:

- The request is only a direction.
- Multiple independent requirements are mixed.
- Acceptance criteria or affected modules are unclear.
- A business, compatibility, permission, or data-risk decision is missing.

## Gate

Requirement intake is complete only after the assistant has stated the goal, scope, non-goals, affected areas, and verification plan in Chinese.
This closes clarification, but it does not authorize implementation.

## Output

State in Chinese:

- 本次需求目标
- 本次需求范围
- 明确不做的内容
- 初步影响区域
- 计划验证方式

Next: [AI Branch Workflow](../ai-branch-workflow/PHASE.md) or [AI Spec Writing](../ai-spec-writing/PHASE.md).
