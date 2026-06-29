---
name: ai-dev-protocol
description: Route AI-assisted development tasks through AI Dev Protocol. Use for coding tasks that need requirement clarification, branch-mode selection, Chinese specs, scoped implementation, commits, merge-back, verified handoff, or Apifox API sync summaries.
---

# AI Dev Protocol

Entry skill. Use it to pick the next phase skill; keep detailed rules in phase skills.

## Flow

1. `ai-requirement-intake`: clarify one independent requirement.
2. `ai-branch-workflow`: detect branch mode.
3. `ai-spec-writing`: write and confirm Chinese spec.
4. `ai-implementation-scope`: implement within confirmed scope.
5. `ai-commit-rules`: prepare/review Chinese `feat:` / `fix:` commits.
6. `ai-merge-back`: personal branch mode only, squash merge `ai/...` back.
7. `ai-handoff`: final delivery.
8. `ai-apifox-sync`: API changes only.

## Branch Modes

- Requirement branch: work directly on current branch; skip `ai/...` and merge-back.
- Personal branch: create `ai/{yyyyMMdd}-{developer}-{short-desc}`; squash merge back after verification.
- Existing `ai/...`: continue work; identify source developer branch.
- Trunk/environment branch: stop unless user confirms exception.
- Ambiguous branch: ask before editing.

## Gates

Before implementation:

- One requirement only.
- Scope, non-goals, affected areas, and verification are clear.
- Branch mode is known.
- Chinese spec is confirmed.

Before delivery:

- Verification ran, or blocker is stated.
- Commits use Chinese `feat:` / `fix:` when created.
- Personal branch mode has merge-back status.
- Developer takeover is stated.
- API changes include Apifox sync summary.

## Global Rules

- Specs, handoff, Apifox summaries, and AI commit messages use Chinese.
- Code identifiers, API paths, table names, config keys, commands, and file paths stay English.
- No unrelated refactor, formatting sweep, dependency upgrade, standalone plan file, `.superpowers/`, or workflow artifact unless explicitly requested.
- Developer owns final review, self-test, integration testing, PR, merge, and code quality.
