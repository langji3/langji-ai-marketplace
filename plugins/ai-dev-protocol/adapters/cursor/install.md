# Cursor 安装说明

## 接入项目

将规则文件复制到目标项目：

```text
adapters/cursor/ai-dev-protocol.mdc -> .cursor/rules/ai-dev-protocol.mdc
```

## 使用方式

Cursor 在代码修改、需求实现、bug fix、提交或交付任务中应读取该 rule。

建议同时在团队项目文档中引用本仓库，说明完整规则以 `skills/` 下各阶段 `SKILL.md` 为准，尤其是 `ai-branch-workflow`、`ai-merge-back` 和 `ai-handoff` 中的分支模式自动判断、merge-back 和开发者接管规则。

## 验证

发起一个小型代码修改任务，确认 Cursor AI 会：

- 先确认需求范围。
- 根据当前分支命名风格判断需求分支模式或个人分支模式。
- 写中文 spec。
- 控制实现范围。
- 个人分支模式下说明 squash merge-back 状态；需求分支模式下跳过 merge-back。
- 最终交付验证结果和开发者接管事项。
- API 变更时输出 Apifox sync summary。
