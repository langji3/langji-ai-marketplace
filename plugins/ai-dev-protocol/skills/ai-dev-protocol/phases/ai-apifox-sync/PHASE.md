# AI Apifox Sync

Use for changed API contracts or an explicit request for an Apifox summary, catalog, plan or write. Select one mode; the other modes' templates and details need not be loaded.

## Sync Summary

For ordinary API-change handoff, use the short [summary template](templates/apifox-sync-summary.md): affected APIs, request/response changes, errors, auth, compatibility, documentation/Mock/test follow-up. No full model library or CLI plan is required.
Report only changes evidenced by the supplied diff/contract. Preserve explicitly unchanged parts as unchanged; mark uncertain parts 待确认 instead of inventing changes.

Without API changes state: Apifox sync summary：无 API 变更，无需同步。

## Entry Catalog

When the user wants a transferable interface/model catalog, read [catalog extraction rules](references/catalog-rules.md) and use the [catalog template](templates/apifox-entry-catalog.md). This is read-only and creates no Git workflow or Apifox branch.

## CLI Sync or a CLI plan

Read [CLI synchronization and recovery](references/cli-sync.md). A request for a plan is read-only. Actual external writes require their exact target/operation authorization; repository implementation or catalog approval does not supply it.

Repository API implementation should finish verification before the optional external-write route. Preserve unknown contracts as 待确认.
