---
name: ai-apifox-sync
description: Create Apifox sync summaries for AI Dev Protocol API changes. Use when a task changes API endpoints, request parameters, response schemas, status codes, error codes, authentication, permissions, headers, examples, or API behavior.
---

# AI Apifox Sync

Use this skill whenever API behavior or contracts changed.

## Triggers

Include an Apifox sync summary for:

- New, deleted, or modified endpoints.
- Request path params, query params, headers, cookies, or body changes.
- Response body, status code, error code, or error response changes.
- Authentication or permission changes.
- Example, field meaning, or compatibility changes.

## Required Summary

Use `templates/apifox-sync-summary.md` when a structured summary is useful. Include:

- 变更类型
- 受影响 API
- request 变更
- response 变更
- 错误码或 status code 变更
- 兼容性说明
- 需要在 Apifox 中同步的示例或文档

## No API Change

If there is no API change, the handoff may state:

```text
Apifox sync summary：无 API 变更，无需同步。
```

