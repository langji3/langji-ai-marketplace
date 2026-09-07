# AI Dev Protocol Design Principles

AI Dev Protocol is a lightweight team workflow plugin for real development work. It borrows useful ideas from Superpowers-style skill systems, but it does not try to become a large general-purpose agent framework.

## Positioning

AI Dev Protocol is the team process layer for AI-assisted coding:

- It controls requirement clarity, branch workflow, specs, implementation scope, commits, handoff, and API sync.
- It does not replace the coding agent's normal implementation ability.
- It does not introduce a large hidden task system.
- It does not require teams to adopt Superpowers artifacts or directory structures.

The goal is simple:

```text
Every AI code change should be clear in requirement, correct in branch, controlled in scope, clean in commit, easy to hand off, and ready for API sync when needed.
```

## Borrowed Ideas

AI Dev Protocol intentionally borrows these ideas:

- Context hygiene: read enough project context to act safely, but avoid loading unrelated files.
- Plan discipline: split non-trivial work into goals before implementation.
- Scope guard: stop and explain when implementation needs to expand beyond the confirmed spec.
- Review pass: use subagent or independent review when available; otherwise record fallback self-review.
- Handoff quality: final delivery should help the developer take over review, integration testing, and follow-up work.
- Recovery mode: infer current workflow state from Git, spec, plan, and commits so work can continue after interruption.
- Artifact policy: keep temporary AI execution state out of business commits.

## What Not To Borrow

AI Dev Protocol should not inherit complexity that makes day-to-day development harder:

- No large nested workflow system.
- No hidden long-lived task state.
- No required `.superpowers/` artifacts.
- No broad agent role hierarchy.
- No mandatory long documents for tiny fixes.
- No automatic scope expansion because a tool found adjacent work.
- No workflow files committed to business projects unless the user explicitly asks for them.

## Layering

Use this priority when rules conflict:

```text
1. User's explicit current instruction
2. Repository safety and non-destructive rules
3. AI Dev Protocol gates and team workflow
4. Optional tool or Superpowers-style execution suggestions
```

AI Dev Protocol owns routing and workflow gates. Optional tools and borrowed methods can improve execution, but they must not skip the selected path's safety conditions, verification responsibility, or handoff.

## Lightweight Product Rules

- One obvious entry: users should normally trigger `ai-dev-protocol`.
- Router ownership: only the main skill is discoverable and user-facing; phase files are internal modules selected by the router.
- Small phase modules: each internal file owns one stage and stays concise.
- Proportional process: user-approved low-risk small edits may use the Quick Fix Path without branches, specs, plans, commits, or merge-back; final verification remains with the user.
- Conservative fallback: API, schema, database, auth/security, dependency/build, cross-module, release, and branch-integration changes always use the full flow; uncertainty also selects the full flow.
- Visible gates: branch source, spec confirmation, implementation start, commit, and merge-back should be explicit; merge-back requires its own developer authorization after implementation and verification reporting.
- Recoverable state: inspect the source and target revisions, worktree identity, spec blob, approval evidence, and verified revision before deciding the next step. A plan checkbox alone proves neither approval nor verification.
- Contextual authorization: confirmation of a concrete proposal applies to its unchanged scope, including when that proposal is saved as a spec. Integration and external writes retain their separately scoped authorization.
- Minimal artifacts: committed files should be specs, code, tests, docs, and intentional templates; local plans stay ignored.
- Unified paths: committed specs live in `docs/specs/`; local execution plans live only in ignored `docs/plans/` and use the corresponding spec basename.
- Team handoff first: final output should make developer review, self-test, integration, PR, merge, and Apifox sync easier.

## Adding New Capabilities

Add a new internal phase module only when it is a reusable workflow phase. Prefer improving an existing phase module for wording, gates, or checklist changes. Add another discoverable skill only when users genuinely need a second independent entry point.

Good candidates:

- API contract review
- Database migration review
- PR review
- Release check

Poor candidates:

- One sentence rule
- One project's local convention
- A helper that only wraps a single command
- A feature that makes every simple fix go through a heavy process
