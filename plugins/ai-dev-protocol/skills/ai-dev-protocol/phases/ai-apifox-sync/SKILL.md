---
name: ai-apifox-sync
description: Create Apifox sync summaries and Apifox-ready interface/model catalogs for AI Dev Protocol API changes. Use when a task changes endpoints, request parameters, response schemas, status codes, error codes, authentication, permissions, headers, examples, observable API behavior, or when the user asks to extract affected APIs and data models for Apifox entry.
---

# AI Apifox Sync

Use whenever API behavior or contracts changed, or when the user needs to enter a requirement/change into Apifox.

This skill is both:

- A final-delivery sync summary for API changes.
- An independent Apifox entry catalog capability that extracts affected interfaces and data models from a requirement, spec, diff, implementation, or change description.

## Triggers

- Endpoint added, removed, or changed.
- Request path/query/header/cookie/body changed.
- Response body, status code, error code, or error response changed.
- Auth, permission, example, field meaning, compatibility, or observable behavior changed.
- User asks for Apifox entry, Apifox import, interface list, API list, data model list, request/response model list, or affected API/model checklist.
- User provides a requirement or change and asks what should be recorded in Apifox.

## Modes

### Sync Summary

Use when final handoff only needs a short API change summary.

## Include

Use `templates/apifox-sync-summary.md` when structure helps.

- 变更类型
- 受影响 API
- Request 变更
- Response 变更
- 错误码或 status code 变更
- 权限或认证变化
- 兼容性说明
- Apifox 中需同步的文档、示例、Mock、测试用例

### Apifox Entry Catalog

Use `templates/apifox-entry-catalog.md` when the user asks for a list that can be handed to the Apifox maintainer.

When the user asks for an Apifox-ready artifact, or when final delivery should provide a directly transferable API document, produce a complete "接口清单 + 数据模型" instead of only a short sync summary.

The catalog can be generated from:

- A confirmed requirement or Chinese spec.
- A code diff or implementation summary.
- A handoff summary.
- A natural-language change description.
- Existing controller/service/API files when available.

The output should be convenient for an Apifox maintainer to copy into Apifox:

- 公共信息：模块、Base Path、认证方式、返回结构、时间格式、变更类型、兼容性
- 影响范围清单：新增 / 修改 / 删除的接口、数据模型、枚举、错误码、权限
- 接口清单：接口名称、Method、Path、权限、请求类型、请求模型、响应模型、变更类型
- 接口详情：说明、权限、Path / Query / Body、请求示例、响应示例、错误场景、兼容性
- 数据模型：请求模型、响应模型、分页模型、通用响应模型、枚举模型；每个模型必须给出 JSON Schema
- 枚举说明：字段、枚举值、含义
- Apifox 同步结论：新增 / 修改 / 删除接口数量，模型、权限、错误码、Mock、测试用例同步项

## Extraction Rules

- Separate confirmed facts from inferred items.
- If an API or model is likely affected but not confirmed, mark it as `待确认`.
- Keep code identifiers, API paths, field names, and enum values in their original English/case.
- Use Chinese for explanations, descriptions, and Apifox maintainer notes.
- Every request model, response model, page model, common response model, and enum-backed model must include a JSON Schema block.
- Request models include Path params, Query params, Headers, Cookies, and Body. Even when there is no request body, the affected Path/Query/Header/Cookie request schemas must still be represented when present.
- In interface details, show request-side schemas as `Path Params Schema`, `Query Params Schema`, `Headers Schema`, `Cookies Schema`, and `Body Schema` as applicable.
- Do not output data models as only prose, tables, TypeScript/Java classes, or field lists; tables can be supplementary, but JSON Schema is required.
- If a field is uncertain, keep it out of `required`, describe the uncertainty in `description`, and list it again in `待确认项`.
- Include examples only when they are known or can be safely inferred from the contract.
- Do not invent endpoints, fields, permissions, or error codes; list unknowns explicitly.

## No API Change

Use:

```text
Apifox sync summary：无 API 变更，无需同步。
```
