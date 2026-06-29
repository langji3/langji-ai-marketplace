# AI Dev Protocol

本项目使用 AI Dev Protocol 作为 AI 辅助开发流程规约。

默认模式：开发者个人分支是多个 AI 需求的汇总站。每个明确需求从开发者个人分支创建一个 `ai/...` 分支，AI 完成实现和验证后 squash merge 回开发者个人分支，之后由开发者主导 review、联调、检查和后续合并。

兼容模式：如果当前分支已经是明确需求分支，并且用户或团队不希望创建额外 `ai/...` 分支，AI 可以直接在该需求分支工作，并跳过 merge-back。

AI 不应直接在 `main`、`master`、`dev`、`develop`、`site`、`staging`、`test`、`prod`、`production` 等主干或环境分支上实现，除非用户明确确认这是团队规则。

当任务涉及需求实现、代码修改、bug fix、提交或交付时，Codex 必须使用 AI Dev Protocol workflow skills：

- `ai-dev-protocol`：总入口和流程路由。
- `ai-requirement-intake`：需求澄清、一需求一工作单元。
- `ai-branch-workflow`：选择默认 AI 分支模式或直接需求分支兼容模式。
- `ai-spec-writing`：中文 spec 和实现前确认。
- `ai-implementation-scope`：范围控制，禁止无关改动。
- `ai-commit-rules`：中文 `feat:` / `fix:` commit。
- `ai-merge-back`：默认模式下 squash merge 回开发者个人分支。
- `ai-handoff`：最终交付、验证说明和开发者接管说明。
- `ai-apifox-sync`：API 变更后的 Apifox sync summary。

如果这些 skills 由 Codex plugin 加载，名称可能显示为 `ai-dev-protocol:<skill-name>`。

完整规则以 `skills/` 下各 `SKILL.md` 为准。

