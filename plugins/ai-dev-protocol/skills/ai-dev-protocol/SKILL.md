---
name: ai-dev-protocol
description: Route AI-assisted development tasks through AI Dev Protocol. Use for coding tasks that need quick low-risk edit classification, requirement clarification, developer-branch workflow selection, Chinese specs, scoped implementation, commits, merge-back, verified handoff, Apifox API sync summaries, or Apifox-ready interface/model catalogs.
---

# AI Dev Protocol

Public router skill. Users normally invoke only this skill. Treat bundled phase files under `phases/` as internal modules: after selecting a phase, read `phases/<phase>/SKILL.md` completely before acting.

AI Dev Protocol is a lightweight team workflow plugin. It owns requirement clarity, branch gates, specs, scope control, commits, handoff, and API sync. It may borrow useful Superpowers-style working methods, but it must not inherit heavy hidden state, broad agent role systems, or `.superpowers/` artifacts.

## Routing

Classify the request before starting workflow artifacts:

- Use the Quick Fix Path only when every quick-fix condition below is satisfied.
- Use the Full Development Flow for features, non-trivial fixes, risky changes, or any uncertain classification.
- Read only the internal phase modules needed for the selected path. Do not ask users to orchestrate phase modules themselves.

## Full Development Flow

1. `ai-requirement-intake`: clarify one independent requirement.
2. `ai-branch-workflow`: detect developer branch, existing AI branch, or blocked branch.
3. `ai-spec-writing`: write and confirm Chinese spec.
4. `ai-implementation-scope`: implement within confirmed scope.
5. `ai-commit-rules`: prepare/review Chinese `feat:` / `fix:` commits.
6. `ai-merge-back`: report merge readiness, request explicit developer approval, then squash merge `ai/...` back only after approval.
7. `ai-handoff`: final delivery.
8. `ai-apifox-sync`: API changes, Apifox sync summaries, and Apifox-ready interface/model catalogs.

## Quick Fix Path

Use this path for a small, low-risk edit when the user explicitly asks for or accepts a quick modification.

All conditions must hold:

- The scope is narrow and well understood, normally limited to one or a few files.
- The change does not alter API contracts or schemas, database migrations, authentication, authorization, security behavior, dependencies, build/CI configuration, release/versioning, destructive Git operations, cross-module behavior, or branch integration.
- The current branch is safe and intended for the direct edit. Never infer permission to edit a trunk or environment branch; direct work there requires explicit user authorization.
- Verification can reasonably be owned by the user after a focused AI self-check.

On the Quick Fix Path:

1. Confirm the exact small change and inspect the affected context.
2. Edit directly on the current authorized branch with tight scope.
3. Run a focused self-check when practical; do not claim user verification.
4. Do not create an `ai/...` branch, committed spec, `docs/plans/` file, implementation commit, or merge-back unless the user explicitly requests one.
5. Hand off the changed files and behavior, checks performed, residual risk, and a clear statement that final verification belongs to the user.

If any exclusion appears or the scope grows, stop the Quick Fix Path and route the remaining work through the Full Development Flow.

## Product Principles

- One obvious entry: users normally trigger only `ai-dev-protocol`.
- One routing owner: phase files are internal modules, not competing public entry points.
- Keep phase modules small; do not turn the plugin into a large general-purpose agent framework.
- Make gates visible: branch source, spec confirmation, implementation start, commit, merge-back, and handoff.
- Recover from current state by inspecting branch, Git status, existing spec, local plan, and commits.
- Keep temporary AI execution state out of business commits.
- Prioritize developer takeover over automation.

## Conversation Entry

Treat natural design discussion as the start of the workflow when it is likely to become code work.
Examples include "design this module", "our current idea is", "next step", "start implementation", or "build it this way".

Do not treat requirement clarification, branch confirmation, or AI branch creation as permission to implement.
After those steps, continue to the next gate in the flow.

## Branch Workflow

- Developer branch: create `ai/{yyyyMMdd}-{developer}-{short-desc}`, commit a requirement spec under `docs/specs/`, create the corresponding ignored local plan under `docs/plans/`, implement, verify, report readiness, and wait for explicit merge-back approval.
- Existing `ai/...`: continue work; identify source developer branch.
- Trunk/environment branch: stop unless the user explicitly says this branch is their developer aggregation branch.
- Ambiguous branch: ask before editing.

## Full-Flow Gates

These gates apply to the Full Development Flow, not the Quick Fix Path.

Before implementation:

- One requirement only.
- Scope, non-goals, affected areas, and verification are clear.
- Developer branch or existing AI branch is known.
- Chinese spec is confirmed.
- The user has confirmed the Chinese spec in the current workflow after branch mode is known.
- The AI branch has a committed `docs/specs/{yyyyMMdd}-{short-desc}.md` requirement spec.
- The AI branch has an ignored local plan at `docs/plans/{yyyyMMdd}-{short-desc}-plan.md`, using the corresponding spec basename; the plan must not be tracked by Git.
- If the user only confirmed the developer branch, that confirms branch source only; next step is `ai-spec-writing`, not implementation.

Before full-flow delivery:

- Spec document path, spec commit status, local plan execution status, implementation commit status, and merge-back status are recorded.
- Verification ran, or blocker is stated.
- Implementation plan/goals were tracked, or a reason for a lightweight path is stated.
- Subagent or independent review ran when the task was complex or involved code changes and the environment supported it; otherwise the fallback self-review is stated.
- Commits use Chinese `feat:` / `fix:` when created.
- Merge-back status is recorded.
- Developer takeover is stated.
- API changes include Apifox sync summary, and Apifox-ready catalogs when requested.

Before merge-back:

- Report the completed implementation, verification, risks, AI branch, target developer branch, and proposed squash commit message.
- Ask the developer whether this specific AI branch may be merged back.
- Treat this as a new authorization gate. Spec confirmation and implementation approval do not carry forward to merge-back.
- Without an explicit affirmative answer, remain on the AI branch and leave the developer branch untouched.

## Recovery Mode

Do not assume the workflow starts from zero. Before deciding the next phase, infer current state:

- Current branch: developer branch, `ai/...`, trunk/environment branch, or ambiguous branch.
- Git status: clean, unstaged work, staged work, committed implementation, or local branch ahead.
- Spec status: missing, present but unconfirmed, confirmed, or stale.
- Local plan status: missing, present and ignored under `docs/plans/`, or incorrectly tracked / misplaced.
- API sync status: no API change, summary needed, Apifox entry catalog requested, or Apifox-ready list completed.
- Path status: Quick Fix Path still qualifies, or the task must continue through the Full Development Flow.

## Global Rules

- Specs, handoff, Apifox summaries, and AI commit messages use Chinese.
- Code identifiers, API paths, table names, config keys, commands, and file paths stay English.
- No unrelated refactor, formatting sweep, dependency upgrade, tracked plan file, `.superpowers/`, or external workflow artifact unless explicitly requested.
- Implementation may borrow selected Superpowers-style methods: context hygiene, goal decomposition, step-by-step progress, scope guard, and independent review. Create an ignored local plan file for execution; do not create `.superpowers/` files or hidden workflow artifacts.
- Never merge, squash merge, cherry-pick, or commit implementation onto the developer branch without explicit developer approval for that specific merge-back.
- Developer owns final review, self-test, integration testing, PR, merge, and code quality.
