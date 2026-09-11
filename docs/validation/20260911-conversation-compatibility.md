# 2.2.2 跨对话与并行需求兼容性发布记录

## 发布内容

本次修正既有流程对跨对话接续和并行需求的适用范围：尊重已分配职责，复用可核验的分支、spec 和确认，缺失决策只暂停受影响工作；按用户要求回报其他对话时，明确实际投递结果。保持 1 个 Router、8 个阶段及原有模板，不新增协调器、任务调度或通知机制。

源仓库 main 提交为 [303039790f9ec836fdc604742e92ea10e1ed4c4c](https://github.com/langji3/ai-dev-protocol/commit/303039790f9ec836fdc604742e92ea10e1ed4c4c)，与已审阅需求分支 b9d2170 的文件树一致。快照通过现有同步脚本从该提交导出，先 dry-run 再正式同步；版本为 2.2.2，共 44 个文件。精确来源及规范化摘要见 [来源记录](../../catalog/releases/ai-dev-protocol.json)。

## 验证

| 检查 | 结果 |
| --- | --- |
| 源仓库合回后校验 | 1 个 Router、8 个阶段、44 个发布文件，通过 |
| 源仓库本地测试 | 21 项：20 通过，1 项因 Windows 目录符号链接权限跳过；短名和 junction 测试实际通过 |
| 源提交远端 CI | [本次运行](https://github.com/langji3/ai-dev-protocol/actions/runs/34551633620) 全部通过，覆盖 Windows/Linux × Python 3.11/3.13 |
| marketplace 本地校验与测试 | 快照及来源记录一致，22 项测试全部通过，包含 PowerShell 5.1/7、同步及中断恢复 |
| 独立快照核验 | 版本、源 SHA、44 个文件库存及索引一致，无误纳 tests、evals、plan 或临时产物；对哈希差异疑点复算后确认摘要及源 Git blob 均一致 |
| 行为复核 | 已审阅最终兼容性规则；本次独立演练确认无投递工具时明确“未发送”，不编造目标或额外索要合回决定 |

原有 16 个模型行为场景未在本轮全部重跑；独立演练不等于真实跨对话投递、自动唤醒或通知验证，本轮未测试这些宿主行为。

marketplace 上传后由 [Validate marketplace 工作流](https://github.com/langji3/langji-ai-marketplace/actions/workflows/validate.yml) 校验对应 main 提交。Git HTTPS 连接失败时沿用仓库已有 GitHub Git database API 备用传输，校验 blob/tree/commit SHA 后非强制更新分支。

本次更新远端发布快照，不代表已安装的个人插件缓存自动更新；消费端更新步骤见 [发布与恢复策略](../update-policy.md#消费端更新)。
