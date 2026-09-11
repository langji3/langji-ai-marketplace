---
name: ai-dev-protocol
description: Guide team coding work through requirement clarification, safe branches, Chinese specs, scoped implementation and verified handoff. Also prepare Apifox API catalogs or separately authorized CLI synchronization.
---

# AI Dev Protocol

One public Router for a small-team workflow. Internal PHASE.md files are bundled resources, not discoverable skills. Follow the selected phase link and read it completely before acting. Load only resources needed now.

Respect the conversation's existing assignment and the user's collaboration arrangements. Loading this skill does not assign a coordinating role or start another task; a read-only scout/review stays read-only. A branch name alone does not determine the conversation's responsibility.

One requirement applies to an implementation work unit/branch, not the whole conversation. Several requirements may be discussed or advanced independently; a missing decision pauses only dependent work. When continuing work from another conversation, use [recovery](references/recovery.md) to reuse the existing branch, spec and applicable approval instead of restarting completed stages.

## Choose a route

| Request | Route |
| --- | --- |
| Analysis, explanation, design discussion, review or proposal without mutation | Discussion Only: answer directly; create no Git/spec/plan/Apifox artifacts. |
| Apifox summary, catalog, plan or requested write without repository implementation | Apifox Standalone: select a mode in [AI Apifox Sync](phases/ai-apifox-sync/PHASE.md). |
| User requests or accepts a narrow, understood, low-risk edit satisfying every condition below | Quick Fix Path. |
| Feature, nontrivial/risky change or uncertain development classification | Full Development Flow. |

A discussion stays read-only until the user requests an artifact or implementation. An explicit request to commit a spec enters the branch/spec stages only. API code changes use Full Development Flow before optional external synchronization.

## Quick Fix Path

All conditions must hold:
- Scope is narrow and understood, normally one or a few files.
- No API/schema, database migration, auth/security, dependency/build/CI, release/version, destructive Git action, cross-module behavior or branch integration change.
- The current branch is intended and authorized for the edit. Direct edits on trunk/environment branches require explicit user authorization.
- A focused AI self-check and subsequent user verification are reasonable.

Inspect context, make the edit, perform a practical self-check and report changed behavior, checks and remaining user verification. Do not create an AI branch, spec, plan, commit or merge-back unless requested. Reclassify remaining work if scope or risk grows.

## Full Development Flow

Use the first incomplete stage supported by current evidence:
1. [Requirement intake](phases/ai-requirement-intake/PHASE.md): one requirement, scope and acceptance.
2. [Branch workflow](phases/ai-branch-workflow/PHASE.md): source developer branch and isolated AI work.
3. [Spec writing](phases/ai-spec-writing/PHASE.md): Chinese repository spec, committed and confirmed before implementation.
4. [Implementation scope](phases/ai-implementation-scope/PHASE.md): ignored local plan, scoped work, verification and independent review.
5. [Commit rules](phases/ai-commit-rules/PHASE.md): review and create requested Chinese commits.
6. [Merge-back](phases/ai-merge-back/PHASE.md): readiness, specific approval, integration and verification.
7. [Handoff](phases/ai-handoff/PHASE.md): evidence and developer takeover; delivery can happen on the AI branch while merge-back is pending.
8. For changed APIs, [AI Apifox Sync](phases/ai-apifox-sync/PHASE.md): short summary; catalog or CLI work when requested.

## Authorization and recovery

For workflow permission, read [authorization rules](references/authorization.md). Recognize affirmative answers in context without requiring special wording. Branch selection, spec implementation and merge-back have different scopes. Apifox writes need their own exact plan and approval.

When resuming or discovering changed Git/spec state, read [recovery rules](references/recovery.md). Infer state from Git, the spec, existing local plan and conversation evidence. Ask only for missing decisions instead of restarting all stages.

## Shared conventions

- User instructions and repository/host constraints take precedence over plugin defaults.
- One approved requirement per AI work unit. Specs, handoff, API explanations and commits use Chinese; identifiers retain their spelling.
- Specs live in docs/specs/{yyyyMMdd}-{short-desc}.md; full-flow local plans live in ignored docs/plans/{yyyyMMdd}-{short-desc}-plan.md.
- Keep edits within approved scope; avoid unrelated refactoring, dependency changes, tracked temporary plans or hidden task systems.
- Keep one public skill. Developer review, self-test, integration and downstream release remain explicit handoff responsibilities.
