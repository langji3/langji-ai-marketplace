# AI Dev Protocol Usage Scenarios

This document shows how AI Dev Protocol should behave in real team work. Users normally only need to invoke the main entry skill: `ai-dev-protocol`.

## 1. Start A New Requirement

User says:

```text
按 AI Dev Protocol 做一个订单状态筛选需求。
```

Expected behavior:

- Clarify one independent requirement.
- Confirm the developer branch or identify that the current branch can be used as the developer aggregation branch.
- Create or suggest an `ai/{yyyyMMdd}-{developer}-{short-desc}` branch.
- Write a Chinese spec under `docs/specs/`.
- Commit the spec before implementation.
- Wait for user confirmation of the spec.
- Create an ignored local plan under `docs/plans/{yyyyMMdd}-{short-desc}-plan.md`, using the corresponding spec basename.
- Implement within the confirmed scope.
- Verify, review, commit, and prepare merge-back.
- Report merge readiness and wait for explicit developer approval before modifying the developer branch.

## 2. Continue An Existing AI Branch

User says:

```text
继续这个 AI 分支，把剩下的需求做完。
```

Expected behavior:

- Detect the current `ai/...` branch.
- Identify or ask for the source developer branch if it is not clear.
- Read the existing spec and confirm it still matches the requested work.
- Check whether the corresponding local plan exists under `docs/plans/` and whether it is untracked.
- Inspect Git status to distinguish implemented, staged, committed, and pending work.
- Continue from the current stage instead of restarting the workflow.

## 3. Small Bug Fix

User says:

```text
修一下用户列表的空指针问题。
```

Expected behavior:

- Keep the requirement narrow.
- Ask for missing reproduction or expected behavior only when needed.
- Classify the change before creating workflow artifacts.
- If the user accepts a quick modification and the fix is narrow and low risk, use the Quick Fix Path: edit the authorized current branch directly, create no AI branch/spec/plan/commit/merge-back, run a focused self-check, and state that the user owns final verification.
- If the fix affects API contracts, schemas, databases, auth/security, dependencies/build, cross-module behavior, release/versioning, or branch integration, use the Full Development Flow.
- Avoid formatting sweeps, unrelated refactors, dependency upgrades, or adjacent cleanup.
- Commit with a Chinese `fix:` message when asked to commit.

## 4. API Change With Apifox Sync

User says:

```text
给公告模块增加批量已读接口。
```

Expected behavior:

- Treat the endpoint as an API contract change.
- Include request, response, permission, error cases, compatibility, and verification in the spec.
- In final delivery, include Apifox sync summary.
- Ask whether the user needs a read-only Apifox-ready "接口清单 + 响应数据模型 JSON Schema" or a CLI synchronization plan for an existing module.
- If requested, generate the complete Apifox-ready artifact using `ai-apifox-sync`.

## 5. Extract Apifox Entry Catalog

User says:

```text
把这个需求影响到的接口和数据模型摘出来，数据模型给 JSON Schema，给我一份录入 Apifox 的清单。
```

Expected behavior:

- Use `ai-apifox-sync` directly, even if implementation is not being done in the current turn.
- Read the provided requirement, spec, diff, handoff, or change description.
- Extract affected endpoints, inline request parameters, complete backend response models, enums, permissions, error codes, Mock needs, and test-case notes.
- Do not create request-side data models: provide JSON Schema only for JSON Body, Apifox batch-edit CSV for Query, and inline parameter tables for Path / Headers / Cookies. Provide complete JSON Schema entries for every model transitively involved in an interface response, preserving the backend's real type names.
- Do not output standalone request or response JSON examples.
- Mark uncertain items as `待确认` instead of inventing contracts.
- Output an Apifox-ready "接口清单 + 响应数据模型 JSON Schema" catalog.

## 6. Synchronize An Existing Apifox Module With CLI

User says:

```text
把这次接口变更同步到 Apifox 的「订单中心」已有模块，目录你按业务自己分。
```

Expected behavior:

- Use the Apifox Standalone CLI route unless repository implementation is also requested.
- Resolve a non-secret `projectId`, the user-selected existing module, and an Apifox AI branch. Do not create a module silently or write to a shared branch without exact authorization.
- Inspect current CLI help, login identity, existing endpoint/schema folder trees, endpoints, schemas, and dynamic payload schemas.
- Infer a stable logical business directory, then resolve separate endpoint and schema directories. Reuse an unambiguous existing directory and show the mapping before writes.
- Keep requests inline: JSON Body uses endpoint JSON Schema; Query and other parameters go directly into the endpoint payload. Create reusable schemas only for complete response-side backend models.
- Build an idempotent create/update/skip plan, validate every payload, and request explicit authorization for the exact project/module/branch/plan immediately before writing.
- Create or update response schemas before endpoints, then read every changed resource back.
- Never expose a token, guess IDs or undocumented module fields, delete resources, blanket import, or merge the Apifox branch by default.
- If the installed CLI cannot prove assignment to the selected module, stop with a read-only plan and a clear blocker.

## 7. Design Discussion Only

User says:

```text
我想讨论一下公告模块怎么设计，先不要写代码。
```

Expected behavior:

- Stay in discussion mode.
- Help clarify goals, scope, risks, data model, API surface, and alternatives.
- Do not create branches, specs, plans, or code unless the user asks to enter implementation workflow.
- If the discussion begins to turn into implementation, summarize the requirement and ask whether to start AI Dev Protocol.

## 8. Scope Expansion During Implementation

User says:

```text
顺便把列表页也重构一下。
```

Expected behavior:

- Identify that this expands the confirmed scope.
- Explain whether it should be a separate requirement.
- Continue only after the user explicitly confirms the scope change.
- Record the scope change in the local plan and final handoff.

## 9. Already Implemented, Need Handoff

User says:

```text
你交付一下这次改动。
```

Expected behavior:

- Inspect Git status and recent commits.
- Summarize changed files and confirmed scope.
- Report spec path, local plan state, implementation commit state, verification, review, risks, and merge-back status.
- State that the developer owns final review, self-test, integration testing, PR, merge, and follow-up.
- Include Apifox sync summary when API behavior changed.
- If Apifox CLI was requested, report the operation-plan authorization, target project/module/branch, directory mapping, created/updated/skipped/blocked resources, and read-back verification separately from Git merge-back.

## 10. Developer Approval Before Merge-back

User says after reviewing the completion summary:

```text
先不要合回我的开发分支。
```

Expected behavior:

- Keep the implementation and commits on the `ai/...` branch.
- Mark merge-back as `未授权` or `已取消`.
- Leave the developer branch untouched; do not switch to it, merge, cherry-pick, commit, reset, restore, or rebase it.
- Report the exact AI branch, target developer branch, verification result, and pending commits.
- Ask for merge-back authorization only when the developer is ready.

When implementation is ready, the dedicated question should name both branches:

```text
实现和验证已完成，是否同意将 ai/... squash merge 回 developer/...？
```

Spec confirmation, implementation approval, or a vague earlier `ok` must not be reused as merge-back authorization.
