# Codex 安装与更新

原生 plugin 包含 .codex-plugin/plugin.json，skills 指向唯一 Router。通过 Langji AI Marketplace 安装后，打开新会话触发 $ai-dev-protocol，确认内部阶段没有变为独立 skill。

若不使用 plugin，可完整安装 skills/ai-dev-protocol/ 到用户 skills 目录，保留 phases、references、templates 和 agents 子目录；升级整体替换同名目录，先备份自定义内容。不要同时安装 plugin 与同名独立 skill。

项目手工接入按 [完整项目资源包](../../docs/project-installation.md) 安装 vendor 资源并合并 AGENTS.snippet.md。仅合并片段不是完整安装。

原生 plugin 更新：刷新 marketplace 并通过宿主插件管理操作更新/重装，再打开新会话核验版本。自检、试运行和卸载见完整包说明；卸载原生 plugin 使用宿主管理界面。
