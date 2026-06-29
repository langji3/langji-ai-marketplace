# AI Dev Protocol

本项目使用 AI Dev Protocol 作为 AI 辅助开发流程规约。

默认模式：开发者个人分支是多个 AI 需求的汇总站。每个明确需求从开发者个人分支创建一个 `ai/...` 分支，AI 完成实现和验证后 squash merge 回开发者个人分支，之后由开发者主导 review、联调、检查和后续合并。

兼容模式：如果当前分支已经是明确需求分支，并且用户或团队不希望创建额外 `ai/...` 分支，AI 可以直接在该需求分支工作，并跳过 merge-back。

当任务涉及需求实现、代码修改、bug fix、提交或交付时，Claude Code 必须遵守本协议的阶段化 workflow：

- 需求进入：先澄清需求，确保一个 AI 工作单元只处理一个明确 requirement。
- 分支判断：选择默认 AI 分支模式或直接需求分支兼容模式；不要直接在主干或环境分支上实现。
- Spec：实现前必须写中文 spec，并等待用户确认。
- 实现：只修改当前需求相关内容，不混入无关重构、格式化、依赖升级或 workflow 产物。
- 提交：commit message 使用中文，需求用 `feat:`，修改用 `fix:`。
- Merge-back：默认模式下 squash merge 回开发者个人分支。
- 交付：最终交付包含验证结果、merge-back 状态和开发者接管说明；API 变更包含 Apifox sync summary。

代码标识符、API 路径、表名、配置键保持英文。

完整规则以本仓库 `skills/` 下各 `SKILL.md` 为准。

