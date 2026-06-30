# Changelog

All notable changes to AI Dev Protocol are documented here.

版本号遵循语义化版本：

- `MAJOR`：破坏性流程调整，例如阶段顺序、skill 命名或安装方式不兼容。
- `MINOR`：新增 workflow skill、模板或重要规则，但保持已有使用方式兼容。
- `PATCH`：文案修正、说明补充、模板微调或维护性更新。

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
