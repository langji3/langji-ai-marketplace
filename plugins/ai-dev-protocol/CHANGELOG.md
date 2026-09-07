# Changelog

All notable changes to AI Dev Protocol are documented here.

版本号遵循语义化版本：

- `MAJOR`：破坏性流程调整，例如阶段顺序、skill 命名或安装方式不兼容。
- `MINOR`：新增 workflow skill、模板或重要规则，但保持已有使用方式兼容。
- `PATCH`：文案修正、说明补充、模板微调或维护性更新。

## [2.2.1] - 2026-09-07

### Fixed

- Accepted legitimate Windows 8.3 path aliases in package validation and bundle generation while still rejecting symbolic links, junctions, and linked ancestors.
- Added real Windows short-path and junction regression fixtures for the CI path checks.

## [2.2.0] - 2026-09-07

### Added

- Added offline package validation, complete project installation bundles, CI checks, and 16 recorded workflow evaluation scenarios.
- Added recovery evidence for interrupted work, changed specs, and developer branches that advance before integration.
- Added per-operation Apifox synchronization records and read-back recovery after partial success or uncertain timeouts.

### Changed

- Reused authorization for an unchanged, concrete proposal; contextual confirmation no longer requires special approval words.
- Split Apifox summaries, catalogs, and CLI synchronization into resources loaded for the selected mode.
- Updated all adapters to use the complete local resource tree and one public Router.

### Migration Notes

- Native plugin users should update the plugin and start a fresh conversation. Manual installations should replace the complete vendor directory and update the marked entry snippet using the installation guide.

## [2.1.0] - 2026-08-26

### Added

- Added an Apifox-only standalone route with read-only catalog and separately authorized CLI synchronization modes.
- Added runtime CLI guidance for existing-module targeting, independent endpoint/schema directory trees, dynamic payload schema validation, idempotent operations, and read-back verification.
- Added CLI planning/execution sections to Apifox and handoff templates.

### Changed

- Converted all internal phase entry files from discoverable `SKILL.md` files to linked, frontmatter-free `PHASE.md` resources so only the main Router is exposed.
- Added explicit Discussion Only routing and clarified `main` branch classification after developer aggregation confirmation.
- Kept request definitions inline: JSON Body uses endpoint JSON Schema, Query CSV is limited to manual catalog mode, and CLI mode maps parameters directly into endpoint payloads.
- Made complete backend response-model schemas the primary Apifox model deliverable and removed standalone request/response JSON examples.
- Updated plugin metadata to version `2.1.0`.

### Safety

- Apifox CLI writes require an exact project, existing module, branch, operation plan, and immediate explicit authorization.
- Missing CLI capability, ambiguous module assignment, conflicts, validation failures, or absent authorization stop safely without external mutation.
- Default CLI synchronization does not install tools, expose tokens, delete resources, blanket import, or merge Apifox branches.

## [2.0.0] - 2026-07-21

### Added

- Added a Router-first Quick Fix Path for user-approved, low-risk small edits, with user-owned final verification.
- Added Codex Router interface metadata and bundled phase resources so Codex and Claude Code discover only the main skill.
- Added cross-platform validation and scenario evaluation work to the iteration backlog.

### Changed

- Moved phase rules into bundled modules selected by `ai-dev-protocol` instead of competing public skill entries.
- Kept API/schema, database, auth/security, dependency/build, cross-module, release, and branch-integration changes on the full workflow.
- Aligned default prompts and trial expectations with the separate developer merge-back authorization gate.
- Unified plugin authorship as `Langji` and updated plugin metadata to version `2.0.0`.

### Migration Notes

- Invoke `ai-dev-protocol` for normal work; phase rules now live under its bundled `phases/` resources and are not independent plugin skills.
- Teams may use Quick Fix only when the user accepts it and every low-risk condition is satisfied; otherwise retain the full spec/plan/AI-branch flow.

## [1.0.0] - 2026-07-20

### Changed

- Made merge-back a separate developer authorization gate after implementation and verification reporting.
- Prevented spec confirmation, implementation approval, or vague earlier consent from being reused as merge-back authorization.
- Required AI to leave the developer branch untouched when merge-back is unapproved, rejected, or cancelled.
- Updated plugin metadata to version `1.0.0` for the hard-gate behavior change.

## [0.4.0] - 2026-07-20

### Added

- Added an Apifox entry catalog capability to extract affected interfaces and data models from requirements, specs, diffs, handoffs, or change descriptions.
- Added `skills/ai-apifox-sync/templates/apifox-entry-catalog.md` for Apifox-ready interface/model checklists.

### Changed

- Expanded `ai-apifox-sync` from API sync summaries to Apifox-ready catalog generation.
- Required JSON Schema blocks for every data model in Apifox entry catalogs, including request-side Path, Query, Header, Cookie, and Body schemas.
- Updated README, adapters, handoff, usage scenarios, and plugin metadata for Apifox catalog extraction.
- Updated plugin metadata to version `0.4.0`.

## [0.3.0] - 2026-07-14

### Added

- Added design principles for the lightweight plugin direction and Superpowers-inspired boundaries.
- Added usage scenarios for new requirements, existing AI branches, small fixes, API sync, design discussion, scope expansion, and handoff.

### Changed

- Repositioned AI Dev Protocol as a lightweight team workflow plugin rather than a broad Superpowers-compatible workflow layer.
- Clarified that the plugin borrows selected Superpowers-style methods without adopting hidden workflow state or `.superpowers/` artifacts.
- Added recovery-mode guidance to the main routing skill.
- Standardized local plan placement under ignored `docs/plans/` using the corresponding spec basename.
- Updated plugin metadata to version `0.3.0`.

## [0.2.9] - 2026-06-30

### Changed

- Removed the current requirement-branch workflow from active rules.
- Made the small-team developer branch workflow the single supported development flow.
- Updated skills, adapters, and install checks to require `ai/...` branches and merge-back.
- Kept old requirement-branch mentions only in historical changelog/spec context.

## [0.2.8] - 2026-06-30

### Fixed

- Required personal branch mode to commit requirement specs under `docs/specs/` before implementation.
- Defined ignored local plan files for personal branch mode execution.
- Updated implementation, merge-back, and handoff guidance to record spec status, local plan status, and merge-back state.
- Added a local plan template and ignored `.ai-dev-protocol/` local workflow state.

## [0.2.7] - 2026-06-30

### Fixed

- Added implementation-stage plan/goals tracking guidance.
- Required subagent or independent review for code changes when available, with fallback self-review recorded when unavailable.
- Updated handoff guidance and template to include plan/goals completion and review status.
- Documented the Superpowers-style working method without creating `.superpowers/` artifacts.

## [0.2.6] - 2026-06-30

### Fixed

- Required specs to call out affected areas and scope-change handling more explicitly.
- Added implementation scope records and scope-change status to implementation and handoff guidance.
- Updated the handoff template with implementation scope and scope-change sections.
- Added a regression prompt for workflow reflection leading to a follow-up protocol iteration.

## [0.2.5] - 2026-06-30

### Fixed

- Tightened workflow gates so natural requirement/design discussions enter requirement intake before implementation.
- Clarified that branch-mode confirmation does not authorize implementation and must be followed by Chinese spec confirmation.
- Added implementation preflight checks requiring a confirmed Chinese spec in the current workflow.
- Added a realistic announcement-module trial prompt for the skipped-spec regression case.

## [0.2.4] - 2026-06-29

### Added

- Added `docs/team-collaboration-guide.md` as the updated team AI collaboration guide.
- Documented how teams should use the plugin marketplace with Codex and Claude Code.

## [0.2.3] - 2026-06-29

### Changed

- Simplified all workflow skills into concise phase rules.
- Kept `ai-dev-protocol` as the router skill and phase details in child skills.
- Aligned spec and Apifox templates with the current fields.
- Bumped plugin version from `0.2.2` to `0.2.3`.

## [0.2.2] - 2026-06-29

### Changed

- Updated branch workflow rules to auto-detect branch mode from the current branch name.
- Promoted direct work on requirement branches to a first-class requirement branch mode instead of treating it as only a compatibility path.
- Clarified that personal developer branches create `ai/...` branches and use merge-back, while requirement branches skip extra AI branches and merge-back.
- Updated Codex, Claude Code, Cursor, and generic adapters to describe branch-mode auto detection.
- Bumped plugin version from `0.2.1` to `0.2.2`.

## [0.2.1] - 2026-06-29

### Added

- Added `.claude-plugin/plugin.json` so the repository is a source plugin for Claude Code as well as Codex.

### Changed

- Kept this repository focused as the pure plugin source project for Codex, Claude Code, Cursor adapters, and generic AI tools.
- Bumped plugin version from `0.2.0` to `0.2.1`.

### Removed

- Removed marketplace template and build script from this plugin source repository. Team marketplace distribution should live in a separate repository.

## [0.2.0] - 2026-06-26

### Added

- Added `ai-merge-back` skill for squash merging completed AI branches back to the developer branch in the default workflow.
- Added branch-mode language for default AI branch mode and direct requirement branch compatibility mode.
- Added marketplace template and build script for publishing a separate Codex plugin marketplace repository.

### Changed

- Reframed the protocol around small-team developer branches as aggregation branches for multiple parallel AI requirements.
- Updated `ai-dev-protocol`, `ai-branch-workflow`, `ai-commit-rules`, and `ai-handoff` to include merge-back and developer-led review/联调.
- Updated README and adapters to explain the default personal developer branch workflow and compatibility mode for existing requirement branches.
- Bumped plugin version from `0.1.1` to `0.2.0`.

## [0.1.1] - 2026-06-26

### Added

- Added `CHANGELOG.md` to record protocol evolution.
- Added `docs/iteration-guide.md` to define the sustainable iteration workflow for skills, templates, adapters, and plugin metadata.

### Changed

- Bumped plugin version from `0.1.0` to `0.1.1`.

## [0.1.0] - 2026-06-26

### Added

- Added Codex plugin manifest at `.codex-plugin/plugin.json`.
- Added multi-skill workflow structure:
  - `ai-dev-protocol`
  - `ai-requirement-intake`
  - `ai-branch-workflow`
  - `ai-spec-writing`
  - `ai-implementation-scope`
  - `ai-commit-rules`
  - `ai-handoff`
  - `ai-apifox-sync`
- Added requirement spec, handoff summary, and Apifox sync summary templates.
- Added Codex, Claude Code, Cursor, and generic AI tool adapters.
