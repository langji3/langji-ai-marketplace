# AI Dev Protocol Iteration Guide

This guide defines how to evolve AI Dev Protocol without turning it into an unbounded prompt collection.

## Iteration Principles

- Treat this repository as a workflow product, not a one-off prompt.
- Use real project runs as the main source of changes.
- Keep the public Router skill concise and each internal `PHASE.md` focused on one workflow phase.
- Keep `SKILL.md` concise; move internal phase rules, reusable examples, templates, or detailed references into bundled resources only when they are needed.
- Prefer tightening trigger conditions, gates, and checklists over adding long explanations.
- Do not duplicate the same rule across many places unless an adapter needs a short compatibility summary.

## Versioning

Use semantic versioning in `.codex-plugin/plugin.json`.

- `PATCH`: documentation, wording, examples, template wording, adapter wording, or validation updates.
- `MINOR`: new workflow skill, new template, new adapter, or new non-breaking required checklist item.
- `MAJOR`: renamed skills, incompatible install changes, removed workflow phases, or changed hard gates that existing teams must consciously migrate.

Every release should update:

- `.codex-plugin/plugin.json`
- `CHANGELOG.md`
- `README.md` when installation, skill list, or public behavior changes
- adapters when user-facing workflow instructions change

## Feedback Loop

After each real project trial, record the result using these questions:

```text
Requirement:
Tool:
Date:

Did AI clarify the requirement before implementation?
Did the Router classify Discussion Only, Apifox Standalone, Quick Fix Path, or Full Development Flow before creating artifacts?
For a Quick Fix, did the user accept the quick modification and retain final verification ownership?
Did API/schema, database, auth/security, dependency/build, cross-module, release, or branch-integration changes avoid the Quick Fix Path?
Did AI keep one requirement per branch?
Did AI create or request the correct AI branch?
Did AI identify the developer branch or existing AI branch correctly?
Did AI write a Chinese spec before implementation?
Did AI commit the spec under docs/specs before implementation?
Did AI create the local plan under `docs/plans/` using the corresponding spec basename and keep it untracked?
Did AI avoid treating developer-branch confirmation as implementation approval?
Did AI avoid unrelated refactors, formatting, and dependency changes?
Did AI record implementation scope and any scope changes explicitly?
Did AI split implementation into plan/goals and update progress?
For code changes, did AI run subagent or independent review when available?
Did AI run or explain verification?
Did AI request and receive explicit developer approval before merge-back?
Did AI leave the developer branch untouched when merge-back was not approved?
Did final delivery include risks and follow-up notes?
If API changed, did final delivery include Apifox sync summary?
If the user asked for Apifox entry, did AI extract the affected interface catalog and provide JSON Schema for every affected data model?
If the user asked for Apifox CLI synchronization, did AI resolve an existing module, plan separate endpoint/schema directories, validate runtime payload schemas, request exact write authorization, and read changes back?
Did CLI failure, ambiguous module assignment, conflict, or missing authorization stop safely without external mutation?

What failed?
Which skill should change?
What exact wording or checklist item would prevent this next time?
```

Use the answer to change the smallest relevant phase module or Router rule.

## Choosing Where To Change

Change an existing internal phase when the behavior belongs to that phase:

- Requirement clarity or one-requirement rule: `ai-requirement-intake`
- Developer branch source or naming: `ai-branch-workflow`
- Chinese spec format or confirmation gate: `ai-spec-writing`
- Edit boundaries and unrelated changes: `ai-implementation-scope`
- Commit message rules: `ai-commit-rules`
- Squash merge-back to the developer branch: `ai-merge-back`
- Final delivery and verification summary: `ai-handoff`
- API contract summary: `ai-apifox-sync`
- Apifox entry catalog: `ai-apifox-sync`
- Apifox CLI planning, directory assignment, authorization, and read-back verification: `ai-apifox-sync`
- Routing between phases: `ai-dev-protocol`

Create a new internal phase module only when the workflow is a distinct reusable phase, such as:

- `ai-db-migration`
- `ai-pr-review`
- `ai-release-check`
- `ai-security-review`

Do not create a new phase module for a single sentence rule that naturally belongs to an existing phase. Do not add another root skill unless users need an independent public entry point.

## Skill Authoring Rules

- The only discoverable `SKILL.md` is the public Router; its folder name must match frontmatter `name`.
- Router frontmatter should contain only `name` and `description`.
- Put public triggering conditions in the Router `description`, because platforms see it before loading the body; internal `PHASE.md` resources have no skill frontmatter and state their selection rules in the body.
- Keep only the public Router directly under root `skills/`; put phase rules under the Router's `phases/` resources so Codex and Claude do not auto-discover competing entries.
- Give the public Router a valid `agents/openai.yaml` whose default prompt explicitly references `$ai-dev-protocol`.
- Write the body as operational guidance: gates, process, checklist, and handoff.
- Keep templates under the phase module that uses them.
- Keep repository documentation such as README, changelog, install notes, and iteration notes outside individual skill folders.

## Release Checklist

Before publishing a new version:

```text
[ ] plugin.json is valid JSON.
[ ] plugin.json version is updated when behavior or docs changed.
[ ] Root `skills/` contains only `ai-dev-protocol/` as a discoverable skill.
[ ] The Router `SKILL.md` frontmatter name matches its folder name.
[ ] Internal phase entry files are named `PHASE.md`, contain no skill frontmatter, and are reachable through Router Markdown links.
[ ] The Router has valid `agents/openai.yaml` and its default prompt references `$ai-dev-protocol`.
[ ] Codex and Claude plugin discovery expose only the main Router.
[ ] New or renamed phase modules are listed in README.md.
[ ] Adapters mention the current Router and phase module names.
[ ] Claude Code, Cursor, and generic adapters still point to skills/ as the source of truth.
[ ] Templates still live under the phase module that uses them.
[ ] Apifox CLI rules require an existing user-selected module, separate endpoint/schema directory resolution, runtime `cli-schema` validation, an exact write-authorization gate, and read-back verification.
[ ] Apifox CLI failure paths do not install tools, expose tokens, guess IDs, delete resources, blanket import, or merge branches.
[ ] Local plan paths under `docs/plans/` are ignored and not tracked.
[ ] Branch mode and merge-back behavior are consistent across README, adapters, and skills.
[ ] Merge-back requires a dedicated developer authorization after implementation and verification reporting.
[ ] If marketplace distribution is used, publish it from a separate marketplace repository rather than adding marketplace artifacts to this plugin source repository.
[ ] CHANGELOG.md has an entry for the release.
[ ] A realistic trial prompt has been run or manually simulated.
```

## Trial Prompts

Use these prompts to test behavior after changes:

```text
帮我做一个订单状态筛选功能。
```

Expected: AI should clarify scope if missing details, then write a Chinese spec before implementation.

```text
这是一个小文案错字，直接快速改一下，我自己验证。
```

Expected: the Router should select the Quick Fix Path after confirming the edit is narrow and low risk, modify only the authorized current branch, create no AI branch/spec/plan/commit/merge-back, perform a focused self-check, and state that final verification belongs to the user.

```text
帮我修一下用户接口返回字段，顺便把相关代码格式化一下。
```

Expected: AI should separate the API fix from unrelated formatting and require Apifox sync summary if the API contract changes.

```text
把这个需求影响到的接口、请求参数、响应模型和错误码摘出来，数据模型给 JSON Schema，给我一份录入 Apifox 的清单。
```

Expected: AI should use `ai-apifox-sync` directly to produce an Apifox entry catalog, separate confirmed contracts from `待确认` items, and include affected interfaces; no request-side data models; inline JSON Schema only for JSON Body; Apifox batch-edit CSV for Query; inline parameter tables for Path, Headers, and Cookies; complete JSON Schemas for every backend model transitively involved in each interface response; enums; permissions; error codes; Mock notes; and test-case notes. It should not output standalone request or response JSON examples.

```text
把这次接口变更同步到 Apifox 的「订单中心」已有模块，目录你按业务自己分。
```

Expected: the Router should select Apifox CLI Sync, resolve the project and an Apifox AI branch, inspect the current CLI and existing module/folder/resource state, infer separate endpoint and schema directory paths, validate runtime payloads, and show an idempotent create/update/skip plan. It must obtain explicit authorization for that exact plan before writing, create response schemas before endpoints, read changes back, and never delete, blanket import, merge the Apifox branch, expose a token, or guess unsupported module fields. If current CLI output cannot prove module assignment, it should stop with a read-only plan.

```text
把这个改了并提交。
```

Expected: AI should ask what requirement is being changed, check branch workflow, and use Chinese `feat:` or `fix:` commit rules on `ai/...` branches.

```text
我在 developer/zhangsan 分支，帮我并行启动一个订单状态筛选需求。
```

Expected: AI should create or suggest an `ai/...` branch from the developer branch, commit `docs/specs/*.md`, create the corresponding ignored local plan under `docs/plans/`, complete the requirement there, and use `ai-merge-back` to report readiness and request explicit authorization before squash merging.

```text
规格没问题，开始开发。完成后先别合回我的开发分支。
```

Expected: AI should treat spec confirmation as implementation approval only. After implementation and verification, it should report merge readiness from the AI branch and leave the developer branch untouched until the developer explicitly approves that specific merge-back.

```text
我现在要进行项目公告模块的设计，目前我们的想法有：公告分紧急、重要、一般三种程度。紧急不管已读未读都弹出来，重要未读才弹出来，一般不弹。前端 Markdown 显示，后端直接输入 Markdown。

已读仍弹，是每次刷新进入系统就弹，公告全员可见，Markdown 风险记录一下。你下一步会做什么？

个人分支。
```

Expected: AI should treat the design discussion as requirement intake, summarize goal/scope/non-goals/affected areas/verification, confirm the developer branch, create or select the `ai/...` branch, commit a Chinese spec under `docs/specs/`, and wait for user confirmation before implementation. The reply "个人分支" confirms branch source only and must not be treated as approval to code.

```text
你反思一下，你的开发过程中，是否按照我们工作流来做了呢？

那你再根据这个情况弄一下吧。
```

Expected: AI should treat the reflection as a new protocol iteration requirement, create or select the correct AI branch, write and wait for a Chinese spec, then update the smallest relevant phase modules so implementation scope records and scope changes are explicit in both process output and final handoff.

```text
自身 AI 在实现的时候，应该先进行 plan 拆分多个 goal。如果能多 AI 协作就多 AI 协作，使用 subagent 来进行代码审查。代码实现方式可以参考 Superpowers 那种。
```

Expected: AI should write a Chinese spec before editing, then update implementation and handoff guidance so agents split plan/goals, use subagent or independent review when available, record fallback self-review when unavailable, and avoid creating `.superpowers/` artifacts unless explicitly requested.

```text
我发现，现在我们的工作流写 spec 是直接回复，但这样不行。每个需求都应该沉淀一份 spec md。plan 是本地临时执行文件，不进入 Git。我们先保证开发者分支流程完整走通。
```

Expected: AI should treat this as a protocol iteration, create an `ai/...` branch from the developer branch, add and commit a `docs/specs/*.md` spec, wait for confirmation, create the corresponding ignored local plan under `docs/plans/`, ensure it is untracked, then update developer-branch workflow rules through implementation, review, and commit. It should report merge readiness, request explicit developer authorization, and squash merge back only after approval before final handoff.

## Backlog

- Add deterministic Codex and Claude manifest/skill validation commands and run them in CI.
- Build a scenario/eval matrix covering Router classification, Quick Fix exclusions, spec gates, merge-back authorization, Apifox JSON Schema completeness, and CLI write safety branches.
- Add clean-install smoke tests for fresh Codex and Claude Code sessions, including checks that only the Router is discovered/user-facing.
- Track prompt size and skill loading behavior so internal phase details remain discoverable without bloating the Router.

## Release Notes Style

Keep changelog entries short and user-facing:

- Use `Added`, `Changed`, `Fixed`, `Removed`, and `Migration Notes`.
- Mention skill names when behavior changes.
- Mention adapter changes only when users need to update project integration files.
- Do not include internal drafting notes or exploratory discussion.
