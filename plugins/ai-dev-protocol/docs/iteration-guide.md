# AI Dev Protocol Iteration Guide

This guide defines how to evolve AI Dev Protocol without turning it into an unbounded prompt collection.

## Iteration Principles

- Treat this repository as a workflow product, not a one-off prompt.
- Use real project runs as the main source of changes.
- Keep each skill focused on one workflow phase.
- Keep `SKILL.md` concise; move reusable examples, templates, or detailed references into bundled resources only when they are needed.
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
Did AI keep one requirement per branch?
Did AI create or request the correct AI branch?
Did AI identify the developer branch or existing AI branch correctly?
Did AI write a Chinese spec before implementation?
Did AI commit the spec under docs/specs before implementation?
Did AI create a local plan and keep it untracked?
Did AI avoid treating developer-branch confirmation as implementation approval?
Did AI avoid unrelated refactors, formatting, and dependency changes?
Did AI record implementation scope and any scope changes explicitly?
Did AI split implementation into plan/goals and update progress?
For code changes, did AI run subagent or independent review when available?
Did AI run or explain verification?
Did AI squash merge back to the developer branch?
Did final delivery include risks and follow-up notes?
If API changed, did final delivery include Apifox sync summary?

What failed?
Which skill should change?
What exact wording or checklist item would prevent this next time?
```

Use the answer to change the smallest relevant skill.

## Choosing Where To Change

Change an existing skill when the behavior belongs to an existing phase:

- Requirement clarity or one-requirement rule: `ai-requirement-intake`
- Developer branch source or naming: `ai-branch-workflow`
- Chinese spec format or confirmation gate: `ai-spec-writing`
- Edit boundaries and unrelated changes: `ai-implementation-scope`
- Commit message rules: `ai-commit-rules`
- Squash merge-back to the developer branch: `ai-merge-back`
- Final delivery and verification summary: `ai-handoff`
- API contract summary: `ai-apifox-sync`
- Routing between phases: `ai-dev-protocol`

Create a new skill only when the workflow is a distinct reusable phase, such as:

- `ai-db-migration`
- `ai-pr-review`
- `ai-release-check`
- `ai-security-review`

Do not create a new skill for a single sentence rule that naturally belongs to an existing phase.

## Skill Authoring Rules

- Folder name must match `SKILL.md` frontmatter `name`.
- Frontmatter should contain only `name` and `description`.
- Put triggering conditions in `description`, because Codex sees it before loading the skill body.
- Write the body as operational guidance: gates, process, checklist, and handoff.
- Keep templates under the skill that uses them.
- Keep repository documentation such as README, changelog, install notes, and iteration notes outside individual skill folders.

## Release Checklist

Before publishing a new version:

```text
[ ] plugin.json is valid JSON.
[ ] plugin.json version is updated when behavior or docs changed.
[ ] Every skills/* directory has SKILL.md.
[ ] Every SKILL.md frontmatter name matches its folder name.
[ ] New or renamed skills are listed in README.md.
[ ] Codex adapter mentions the current skill names.
[ ] Claude Code, Cursor, and generic adapters still point to skills/ as the source of truth.
[ ] Templates still live under the skill that uses them.
[ ] Local plan paths such as `.ai-dev-protocol/` are ignored and not tracked.
[ ] Branch mode and merge-back behavior are consistent across README, adapters, and skills.
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
帮我修一下用户接口返回字段，顺便把相关代码格式化一下。
```

Expected: AI should separate the API fix from unrelated formatting and require Apifox sync summary if the API contract changes.

```text
把这个改了并提交。
```

Expected: AI should ask what requirement is being changed, check branch workflow, and use Chinese `feat:` or `fix:` commit rules on `ai/...` branches.

```text
我在 developer/zhangsan 分支，帮我并行启动一个订单状态筛选需求。
```

Expected: AI should create or suggest an `ai/...` branch from the developer branch, commit `docs/specs/*.md`, create an ignored local plan, complete the requirement there, and use `ai-merge-back` to squash merge back after verification.

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

Expected: AI should treat the reflection as a new protocol iteration requirement, create or select the correct AI branch, write and wait for a Chinese spec, then update the smallest relevant skills so implementation scope records and scope changes are explicit in both process output and final handoff.

```text
自身 AI 在实现的时候，应该先进行 plan 拆分多个 goal。如果能多 AI 协作就多 AI 协作，使用 subagent 来进行代码审查。代码实现方式可以参考 Superpowers 那种。
```

Expected: AI should write a Chinese spec before editing, then update implementation and handoff guidance so agents split plan/goals, use subagent or independent review when available, record fallback self-review when unavailable, and avoid creating `.superpowers/` artifacts unless explicitly requested.

```text
我发现，现在我们的工作流写 spec 是直接回复，但这样不行。每个需求都应该沉淀一份 spec md。plan 是本地临时执行文件，不进入 Git。我们先保证开发者分支流程完整走通。
```

Expected: AI should treat this as a protocol iteration, create an `ai/...` branch from the developer branch, add and commit a `docs/specs/*.md` spec, wait for confirmation, create an ignored local plan under `.ai-dev-protocol/plans/`, ensure it is untracked, then update developer-branch workflow rules through implementation, review, commit, squash merge-back, and handoff.

## Release Notes Style

Keep changelog entries short and user-facing:

- Use `Added`, `Changed`, `Fixed`, `Removed`, and `Migration Notes`.
- Mention skill names when behavior changes.
- Mention adapter changes only when users need to update project integration files.
- Do not include internal drafting notes or exploratory discussion.
