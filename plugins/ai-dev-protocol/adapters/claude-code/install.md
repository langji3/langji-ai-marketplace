# Claude Code 安装说明

## Plugin 元数据

本仓库包含 Claude Code plugin manifest：

```text
.claude-plugin/plugin.json
```

它用于声明 `ai-dev-protocol` 作为 Claude Code 可识别的插件源码。根目录 `skills/` 只包含主 Router，阶段规则作为 Router 内部资源放在 `skills/ai-dev-protocol/phases/`。实际团队安装方式可由团队的 Claude Code 插件市场或项目接入规范决定。

## 接入项目

将 `adapters/claude-code/CLAUDE.snippet.md` 合并到目标项目的 `CLAUDE.md`。

如果团队希望把协议文件一起放入项目，可以复制本仓库的整个 `skills/` 目录，也可以在 `CLAUDE.md` 中引用本仓库 GitHub 地址。

## 建议配置

在 `CLAUDE.md` 中保留项目本身的技术规则，并把 AI Dev Protocol 放在开发流程规则区域。

若项目规则与协议冲突：

- 业务、架构、代码风格规则以项目规则为准。
- 需求澄清、开发者分支工作流、spec、范围控制、提交和交付流程以 AI Dev Protocol 为准。

完整规则以主 Router 和 `skills/ai-dev-protocol/phases/` 下的内部阶段规则为准，尤其是 Quick Fix 分类、`ai-branch-workflow`、`ai-merge-back` 和 `ai-handoff` 中的开发者分支确认、merge-back 和开发者接管规则。

## 验证

分别让 Claude Code 处理一个低风险小修改和一个完整需求，确认它只暴露主 Router，并先进行路径分类。小修改经用户接受后直接修改并由用户验证；完整需求才执行以下流程。

确认它会：

- 创建或进入 `ai/...` 分支。
- 创建并提交 `docs/specs/*.md`。
- 在 `docs/plans/{yyyyMMdd}-{short-desc}-plan.md` 创建对应 spec 的本地 plan，并确认它被忽略且未被 Git 追踪。
- 在 AI 分支提交实现改动，并说明实现提交状态。
- 汇报 merge-back 准备状态，单独取得开发者明确授权后才 squash merge 回开发者分支。
- 交付 spec 文档状态、本地 plan 状态、实现提交状态、merge-back 状态和开发者接管事项。
- 若涉及 API 变更，确认包含 Apifox sync summary；用户需要录入 Apifox 时，确认包含接口清单和数据模型 JSON Schema 清单。
