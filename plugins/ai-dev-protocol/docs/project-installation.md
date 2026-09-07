# 完整项目资源包

资源目录和 adapter 一起构成完整接入。只复制 adapter 是摘要模式。

## 生成

从 source 仓库根目录执行：

~~~shell
python scripts/build_bundle.py --output dist/project-bundle
~~~

从 marketplace 根目录执行：

~~~shell
python plugins/ai-dev-protocol/scripts/build_bundle.py --output dist/project-bundle
~~~

需要 Python 3.11+。输出目录必须不存在，生成器不会覆盖现有项目。输出包含：
- vendor/ai-dev-protocol/：manifest、Router、phases、references、templates、自检脚本和说明。
- .cursor/rules/ai-dev-protocol.mdc：始终加载的短入口；仅相关任务读取 Router。
- AGENTS.md、CLAUDE.md、AI_DEV_PROTOCOL.md：按工具选择的接入片段。
- bundle.json：版本与资源内容摘要，供构建结果审阅。

## 安装到目标项目

1. 把整个 vendor/ai-dev-protocol/ 复制到项目同路径，保留目录结构。
2. Cursor 同时复制 .cursor/rules/ai-dev-protocol.mdc；Codex/Claude 将对应片段合并到现有 AGENTS.md/CLAUDE.md，保留用户原规则；通用工具明确引用 AI_DEV_PROTOCOL.md。
3. 原生 plugin 已安装时优先使用它，避免同时安装同名直装 skill。
4. 从目标项目根目录执行：

~~~shell
python vendor/ai-dev-protocol/scripts/validate_plugin.py
~~~

确认输出的版本是本次安装版本，且只有一个 Router、8 个内部阶段。打开新会话，先试“只分析，不修改文件”，再在隔离练习项目试低风险修改和完整需求。工具实际读取路径及文件变化才是接入证据。

## 更新

从新的已验证版本生成一个新目录中的完整包，审阅版本与变更记录。备份现有 vendor/ai-dev-protocol/ 和接入片段，然后整体替换该 vendor 目录，更新对应短入口，保留项目原规则。不要只覆盖文件而遗留已移除的旧资源。自检后在新会话重复烟测。

vendor 内容来自上游；团队自定义规则放在项目自己的配置中，避免下次更新覆盖。是否将 vendor 资源提交到项目 Git 由团队明确选择。

## 卸载

移除项目中本次安装的 vendor/ai-dev-protocol/ 和 Cursor 规则文件；从 AGENTS.md/CLAUDE.md 等移除 ai-dev-protocol:begin/end 标记包围的片段，保留用户其他内容。先确认没有本地自定义修改。原生 plugin 的卸载由宿主插件管理界面完成。

## 摘要模式与限制

旧版单文件 adapter 可暂时保留为摘要模式；它没有完整阶段依赖。无法读取本地资源的工具需明确加载 Router 和本次阶段文本。文件自检不能证明工具会遵循规则；未运行的真实平台测试必须标记未验证。
