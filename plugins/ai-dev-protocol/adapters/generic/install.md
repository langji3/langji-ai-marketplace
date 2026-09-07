# 通用工具接入

按 [完整项目资源包](../../docs/project-installation.md) 安装 vendor/ai-dev-protocol/，把 AI_DEV_PROTOCOL.md 作为项目明确的流程入口。确认工具可以读取本地 Router、所选阶段和模板。

如果工具只能接收单段文本，明确提供 Router 和本次所需阶段内容，并说明文件、Git或CLI能力限制；该模式不等于原生插件安装。

升级、版本核验、烟测和卸载均按完整包说明执行。保留项目自身规则，避免复制多份可能漂移的完整工作流。
