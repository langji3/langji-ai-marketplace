# CLI synchronization and recovery

For a plan or an authorized external write, read [runtime capability rules](apifox-cli.md) before commands and [authorization rules](../../../references/authorization.md). Use the [operation record](../templates/cli-operation-plan.md). Load [catalog rules](catalog-rules.md) when extracting API definitions.

## Resolve the exact target

Resolve projectId from the user or existing .apifox/settings.json without printing secrets, an existing user-selected module, an Apifox branch, and the change source. Prefer an AI branch; main/shared-branch writes require authorization for that exact target. Do not create a module silently.

Modules and typed folders are different concepts. Prove module assignment and supported payload fields from installed CLI help, agentHints and cli-schema. Missing CLI/login or unprovable target assignment stops external work with a read-only plan. Do not guess IDs or install tools silently.

## Plan from current state

Read project/branch, separate endpoint and schema folder trees, endpoints and response models. Choose stable directories using business responsibilities and existing organization; show logical path and each tree's real folder ID.

Match endpoints by known ID or unique Method + normalized Path in the selected module/branch. Match response models by known ID or unique backend type name. Re-read known IDs if names changed. Explicitly new resources may have zero matches; unexpected zero/multiple matches are conflicts, not permission to guess.

Plan create/update/skip operations, dependencies and covered fields. Preserve unrelated metadata. Fetch and validate current runtime schemas for complex payloads. Requests remain inline; reusable models are response-side only. No blanket import, deletion, module replacement or branch merge by default.

For model references, resolve IDs in dependency order. For cycles, use an explicit two-pass plan only if runtime capabilities support it, and include all temporary/final changes in authorization; otherwise leave cyclic resources blocked with the concrete limitation.

## Authorize, execute and record

Show project, existing module, branch, folder mapping, operations and payload scope. Obtain explicit authorization for that exact external plan immediately before mutation. An affirmative reply to this concrete proposal is valid; no magic words are required.

Re-read affected resources before execution. Compare their revision/etag where available, otherwise relevant payload contents with the plan baseline. If external changes affect the proposed write, replan and obtain approval for the changed operations. Prefer conditional writes when supported; otherwise disclose that concurrent remote edits cannot be made atomic by this protocol.

Write schema directories/models before dependent endpoints. Record each operation's stable key, target, returned ID, pre-write baseline, intended payload digest, result and read-back evidence in an ignored local operation record or the existing task plan. Never store tokens. State labels are planned, submitted, verified, failed, unknown and blocked; a timeout is unknown, not failed.

Read each changed resource back from the same target and compare directory, identity, request definitions, response references and covered metadata. Only a matching read-back makes an operation verified.

## Partial success and unknown results

Stop dependent writes after failure or unknown outcome. Preserve verified IDs and results; do not replay the batch or automatically delete successful resources.

Before retrying, query the exact target by returned ID, or its unique stable key if no ID was returned:
- Desired resource exists and matches: mark verified and continue dependent work within unchanged authorization.
- Retry a timed-out create only with the original request's recorded server-enforced idempotency key still within its supported validity period, or authoritative evidence that the original request is terminal without creating a resource and cannot commit later. Keep the original plan/target/payload unchanged, then read back.
- Read fails, matching is ambiguous or the remote contents conflict: remain unknown/blocked; do not create a duplicate or overwrite.

One or several empty list/read results do not prove that an earlier create cannot still commit, especially with eventual consistency. If request status, authoritative consistency, or the original idempotency guarantee cannot be established, leave the operation unknown and stop its dependent writes. Waiting for an arbitrary interval or obtaining user approval does not establish absence.

Do not loop indefinitely: after one failed read/retry attempt in the current run, preserve the record and report the blocker. On a later resume, reread state before choosing remaining operations. Expired/unavailable approval evidence or a material plan change uses the authorization gate again.

Report verified, failed, unknown and blocked resources separately, plus the exact next recoverable step. User controls Apifox branch review/merge.
