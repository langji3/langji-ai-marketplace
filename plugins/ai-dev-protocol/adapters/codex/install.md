# Codex 安装说明

## 推荐方式：作为 Plugin 安装

本仓库包含 Codex plugin manifest：

```text
.codex-plugin/plugin.json
```

manifest 中声明：

```json
{
  "skills": "./skills/"
}
```

因此 Codex 安装的是 `ai-dev-protocol` 这个 plugin，并只加载一个主 Router skill。阶段规则位于 Router 自身的 `phases/` 目录，不参与 skill 自动发现。

安装后应能看到或触发：

```text
ai-dev-protocol
```

Router 会按需读取 `skills/ai-dev-protocol/phases/` 下的阶段规则，用户不需要触发阶段模块。

## 团队接入

将 `adapters/codex/AGENTS.snippet.md` 合并到目标项目的 `AGENTS.md`。

如果项目已有 `AGENTS.md`，保留原有项目规则，并追加 AI Dev Protocol 段落。若规则冲突：

- 项目业务、架构、代码风格规则优先。
- 需求澄清、开发者分支工作流、spec、范围控制、提交、merge-back 和交付流程遵守 AI Dev Protocol。

## 备用方式：直接安装 Router Skill

如果暂时不使用 Codex plugin，可将 `skills/ai-dev-protocol/` 安装到 `~/.codex/skills/ai-dev-protocol/`。

这种方式仍包含全部内部阶段规则，但没有 plugin 卡片、统一插件元数据或 marketplace 分发能力。

## 验证

分别发起一个低风险小修改和一个完整需求，确认 Codex 会先由 Router 分类：小修改经用户接受后直接修改并交给用户验证，完整需求才执行以下流程：

- 使用 `ai-requirement-intake` 先确认需求范围。
- 使用 `ai-branch-workflow` 确认开发者分支、已有 AI 分支或主干/环境分支阻断。
- 使用 `ai-spec-writing` 写中文 spec，并创建提交 `docs/specs/*.md`。
- 在 `docs/plans/{yyyyMMdd}-{short-desc}-plan.md` 创建对应 spec 的本地 plan，并确认它被忽略且未被 Git 追踪。
- 在 AI 分支提交实现改动，并在交付中说明实现提交状态。
- 使用 `ai-merge-back` 汇报准备状态并单独请求授权，只有开发者明确同意后才 squash merge 回开发者分支。
- 使用 `ai-handoff` 在交付时包含 spec 文档状态、本地 plan 状态、实现提交状态、验证结果、merge-back 状态和开发者接管说明。
- API 变更时使用 `ai-apifox-sync` 输出 Apifox sync summary；用户需要录入 Apifox 时，输出接口清单和数据模型 JSON Schema 清单。
