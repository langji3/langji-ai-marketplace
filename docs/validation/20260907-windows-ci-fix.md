# 2.2.1 Windows CI 修复记录

## 原因与修复

[2.2.0 的首次 CI](https://github.com/langji3/ai-dev-protocol/actions/runs/34078302733) 在 Windows Python 3.11/3.13 的临时目录测试中失败，直接仓库校验和 Linux 任务通过。旧实现把 resolve() 与 absolute() 的路径差异当作链接证据；Windows 8.3 短名解析成长名后会产生这种差异。

使用 GetShortPathNameW 创建真实短名别名，本地复现相同的 Linked plugin root 错误。2.2.1 改为先逐级检查输入目录及祖先的 lstat 链接/reparse 属性，再规范化短名；没有取消符号链接或 junction 限制。源包校验、完整包生成、marketplace 独立清单和事务路径使用相同处理原则。新增真实短名、根目录/祖先 junction、短路径同步与恢复回归；版本测试使用 UTF-8 和 manifest 当前版本。

## 已验证

| 检查 | 结果 |
| --- | --- |
| 本地源仓库 | 21 项测试：20 通过、1 项因 Windows symlink 权限跳过；短名及两项 junction 回归实际通过 |
| 本地 marketplace | 22 项全部通过，包含实际短路径同步/中断恢复、junction 保护和 PowerShell 5.1/7 入口 |
| 源提交远端 CI | [修复提交运行](https://github.com/langji3/ai-dev-protocol/actions/runs/34079772042) 全部通过，覆盖 Windows/Linux × Python 3.11/3.13 |
| Codex 2.2.1 安装 | 临时配置中安装/list、唯一 Router、8 阶段通过；见 [命令结果](20260907-codex-2.2.1-install.json) |
| 发布内容 | 43 个文件；规范化清单与 [来源记录](../../catalog/releases/ai-dev-protocol.json) 一致 |

源仓库 main 提交为 48b589c61bbda7a0b4b83f6b296a16488637bcae，与通过 CI 的修复提交相同。marketplace 推送后由其 [Validate marketplace 工作流](https://github.com/langji3/langji-ai-marketplace/actions/workflows/validate.yml) 校验相应 main 提交。

本轮 Git HTTPS 连接多次失败，改用 GitHub 官方 Git database API 上传同一 origin 的对象，逐项验证 blob/tree/commit SHA 一致后，使用非强制分支更新；该一次性传输脚本保留在 ignored tmp/，不属于发布插件或业务代码。源码路径修复未改变 Router/Apifox 行为，因此 2.2.0 的 16 例独立决策演练保留为规则行为证据；未将其升级为真实模型执行或真实 Apifox 写入验证。
