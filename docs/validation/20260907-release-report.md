# 2.2.0 实施与验证记录（2026-09-07）

本文保留 2.2.0 实施阶段的历史记录。首次远端 Windows CI 失败后已修复并升级为 2.2.1，最新结果与来源说明见 [Windows CI 修复记录](20260907-windows-ci-fix.md)。

## 交付范围

已实现已确认方案的六个单元：安全同步、来源追溯与索引/CI、完整安装、Router 与行为评测、Git 恢复、Apifox 部分成功及超时恢复。两仓交付分支均为 codex/20260907-plugin-reliability。

用户随后明确授权两仓合并推送。发布快照源提交更新为源仓库 main 上的 caa2de5b06beaab78c6053cfc3931b7dcde51259；该提交由已验证工作分支 squash 合并产生，文件树一致。marketplace 的 2.2.0 快照仍包含相同的 43 个发布文件，版本、索引和规范化摘要通过 [来源记录](../../catalog/releases/ai-dev-protocol.json) 核验。个人插件缓存和真实 Apifox 项目没有变更。

## 验证证据

| 检查 | 结果 | 范围与限制 |
| --- | --- | --- |
| 源仓库 unittest | 18 项，17 通过、1 跳过 | Git 独立 worktree、目标前进组合、冲突隔离、spec blob 变化、安装包、静态校验、评分器；当前 Windows 无目录符号链接权限，相关测试跳过 |
| marketplace unittest | 19 项全部通过 | 精确提交、重复/试运行、脏源、未追踪文件隔离、非法 manifest、来源不符、路径重叠、复制失败、各发布检查点回滚、中断阻断/恢复、人工修改与备份保护、活进程锁 |
| PowerShell 入口 | 5.1.26100.9168 和 7.6.5 通过 | 属于 marketplace 19 项测试，在临时仓库实际执行 -DryRun |
| 官方 plugin / skill validator | 通过 | 单 Router、manifest 和入口元数据；不能推导模型实际行为 |
| 源包及 marketplace validator | 通过 | 2.2.0，唯一 Router，8 阶段，43 个允许发布文件；相对资源链接和来源/索引一致 |
| 完整项目包 | 生成和安装后自检通过 | 从 marketplace 的 build_bundle.py 生成全新目录，再运行 vendor 内 validator；生成后 marketplace 自身校验仍通过 |
| Codex 原生安装 | 通过 | CLI 0.153.4，在一次性 CODEX_HOME 注册本地市场并安装/list；缓存为 2.2.0、一个 Router、8 阶段，详见 [原始命令结果](20260907-codex-install.json) |
| 独立行为演练 | 16/16 通过 | 源仓库 evals/results/20260907-reviewed-simulation.json；是只读决策模拟，不是实际业务写入 |
| Git diff --check | 通过 | 两仓工作分支变更无空白错误 |

源仓库测试：python -m unittest discover -s tests -v。行为回归：python scripts/evaluate.py score evals/results/20260907-reviewed-simulation.json。marketplace 测试命令相同，另运行 python scripts/validate_marketplace.py。原生安装烟测命令见 scripts/smoke_codex.py --help；会自动清理临时配置。

功能测试与安装烟测针对 d7ca332 的实现完成。最终源提交 e00dc0e 只清理 CI、spec 和评测记录末尾空行；随后重新导出快照并验证来源摘要和完整 diff，没有改变被测功能。

源仓库合回 main 后重新运行 18 项测试，结果仍为 17 通过、1 环境权限跳过，插件校验和 diff 检查通过。来源记录引用 squash 后的远端可达提交，不依赖未推送的工作分支。两仓推送后由 GitHub Actions 执行跨平台检查，结果以对应 main 提交的运行记录为准。

## 审查与修复

两轮代码/规则审查修复了目录链接绕过、发布来源不一致、bundle 输出污染源资源、评测部分覆盖误报整体通过、live 证据缺少文件摘要等问题。事务恢复在写回前同时验证快照、索引和备份，拒绝覆盖中断后的人工变更。

首轮 15 例演练中，短摘要有 1 例误述“响应变化”，记录保留为失败。增加按事实保留明确不变项的规则后，新的独立代理演练通过。最终审查补充了创建超时后空列表不足以证明不存在的条件，并新增第 16 例回归；必须保留 unknown，直到具备原请求幂等保证或不会延迟落地的权威终态证据。未经支持的重试不因用户催促而自动合法。

## 未验证与后续边界

- 已加入 Windows/Linux、Python 3.11/3.13 的 CI 配置；本轮本地执行环境为 Windows、Python 3.14.5。远端 CI 由推送触发，参见各仓库对应提交的 Actions 记录。
- Claude Code、Cursor/agent CLI 在当前 PATH 中不可用，原生运行验证未覆盖；完整资源包生成和结构已核验。
- Codex 安装烟测没有启动新模型会话；真实工具中的 Router 行为仍需要后续用户试点。CLI 关于临时目录不创建 PATH 别名的提示不影响安装/list 命令成功，保留在结果中。
- Apifox 使用原始状态夹具和独立演练，没有登录、同步或写入真实项目。
- 跨文件发布不能保证断电时瞬时原子可见；通过日志、旧快照、互斥和 --recover 恢复。当前同步脚本只负责 ai-dev-protocol。

合回时重新核对两仓 main 与工作分支提交，目标前进则先验证组合结果，再提出针对确切提交的合回方案。
