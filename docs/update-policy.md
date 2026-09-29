# 发布与恢复策略

源仓库负责规则、模板、adapter 和版本；marketplace 只分发提交快照。禁止直接在 plugins/ai-dev-protocol/ 改规则后把它当作正式源版本。本页以下同步与恢复机制专用于 AI Dev Protocol。

## 发布内容与身份

允许 .codex-plugin/、.claude-plugin/、skills/、adapters/、docs/（排除 docs/plans/）、README.md、CHANGELOG.md，以及安装后使用的 scripts/validate_plugin.py 和 scripts/build_bundle.py。其余维护脚本、tests、evals、CI、.git、dist、未追踪文件不进入快照；目录链接及非普通 Git 文件拒绝发布。

catalog/releases/ai-dev-protocol.json 记录完整源提交、源仓库、版本及所有发布文件摘要。sha256-text-lf-utf8-v1 将已知文本格式解码为 UTF-8、去 BOM 并把 CRLF 转为 LF 后计算 SHA-256；二进制按原字节计算。因此换行差异不构成语义发布差异。此记录保证本地内容一致性，不是远端仓库身份的密码学证明；同步同时核对实际 Git origin 与插件元数据来源。

## 操作顺序

1. 在 source 完成规则修改、自检、行为回归及版本和 CHANGELOG 更新并提交。
2. 确认源提交 SHA。本地来源要求 Git 仓库根目录且已追踪文件无未提交变化；导出指定提交，不复制工作目录。
3. 运行 README 中含 --expected-commit 的 --dry-run，然后正式同步。所有目标必须在 marketplace 范围内，源、缓存、快照不得重叠。
4. 同步自动维护 catalog 与 Claude 索引版本、描述和来源；Codex 入口保留固定本地路径与安装策略并参与检查。
5. 运行 validator、tests，审阅快照、索引、来源记录和 Git diff。经授权合回/推送后用户才能从远端获取新版本。

远端模式默认为 https://github.com/langji3/ai-dev-protocol.git 的 main，缓存为 tmp/source-cache/ai-dev-protocol.git。已有普通工作目录缓存不可复用；选择新 bare cache。CachePath 必须位于本仓库 tmp/ 下；不会 reset 或清理已有源码工作目录。同一版本只允许规范化内容相同的重复同步。

## 失败和中断

同步使用 tmp/release-sync.lock 互斥，临时导出位于 tmp/release-transaction/。替换前保存旧插件、旧索引和恢复日志。普通复制/替换/索引异常恢复旧快照及索引；进程被终止时日志保留，后续同步和独立校验会拒绝继续。

确认原同步进程已停止后运行：

~~~shell
python scripts/sync_plugin.py --recover
~~~

PowerShell 对应 -Recover。活进程持有的锁不会被抢占。恢复前会检查当前快照/索引是否仍为事务中已知状态，以及备份是否完整；中断后的人工修改或损坏备份会阻断自动覆盖。此时先保留事务目录、修改文件和 Git diff，再人工决定保留版本。恢复完成后检查 Git 状态，再重新 dry-run 和同步。不要把恢复目录当普通缓存直接删除。

跨文件替换无法提供断电时的瞬时原子可见性。恢复成功只表示回到旧快照，不表示新版本已经发布；旧快照即使通过校验，也应重新检查拟发布提交。

## 消费端更新

Codex 用户刷新 marketplace 并更新/重新安装插件，开始新任务，核对实际版本和唯一 Router。Claude Code 用户刷新 marketplace、更新 plugin 并重载/开始新会话。更新仓库不等于所有已安装缓存自动更新；手动安装按完整 vendor 目录升级，不覆盖用户自己的入口文件。详见各安装指南。
