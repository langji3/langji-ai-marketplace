# Cursor 安装说明

## 接入项目

将规则文件复制到目标项目：

```text
adapters/cursor/ai-dev-protocol.mdc -> .cursor/rules/ai-dev-protocol.mdc
```

## 使用方式

Cursor 在代码修改、需求实现、bug fix、提交或交付任务中应读取该 rule。

建议同时在团队项目文档中引用本仓库，说明完整规则以 `skills/` 下各阶段 `SKILL.md` 为准，尤其是 `ai-branch-workflow`、`ai-merge-back` 和 `ai-handoff` 中的开发者分支确认、merge-back 和开发者接管规则。

## 验证

分别发起一个低风险小修改和一个完整需求，确认 Cursor AI 会先分类：小修改经用户接受后直接修改并由用户验证，完整需求才执行以下流程：

- 先确认需求范围。
- 确认开发者分支或已有 AI 分支。
- 写中文 spec。
- 创建并提交 `docs/specs/*.md`。
- 在 `docs/plans/{yyyyMMdd}-{short-desc}-plan.md` 创建对应 spec 的本地 plan，并确认它被忽略且未被 Git 追踪。
- 控制实现范围。
- 提交实现改动并说明实现提交状态。
- 说明 squash merge-back 准备状态和授权状态；未取得开发者明确同意时不修改开发者分支。
- 最终交付验证结果和开发者接管事项。
- 最终交付 spec 文档状态、本地 plan 状态和实现提交状态。
- API 变更时输出 Apifox sync summary；用户需要录入 Apifox 时，输出接口清单和数据模型 JSON Schema 清单。
