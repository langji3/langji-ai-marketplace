# 在 Cursor 安装

在 marketplace 根目录生成一个全新安装包：

~~~shell
python plugins/ai-dev-protocol/scripts/build_bundle.py --output dist/project-bundle
~~~

1. 将生成的 vendor/ai-dev-protocol/ 完整复制到目标项目同名目录。
2. 将生成的 .cursor/rules/ai-dev-protocol.mdc 复制到目标项目；同名规则存在时先比较并保留用户自定义内容。
3. 在目标项目运行 python vendor/ai-dev-protocol/scripts/validate_plugin.py，确认唯一 Router、8 个阶段、版本和资源链接通过。
4. 重新打开项目/新建会话，确认规则启用；用“只分析并给方案”检查它读取 Router 后保留只读边界，再试用一个低风险修改。

短 rule 的 alwaysApply 只提供读取入口，具体阶段按请求加载。仅复制 .mdc 会退化为摘要模式。升级和卸载按 [完整项目包指南](../plugins/ai-dev-protocol/docs/project-installation.md) 操作，整包替换而非叠加旧资源。

