# Authorization in context

Use current and prior explicit approvals in this task. Higher-priority host instructions override plugin defaults.

## Match approval to the proposal

- Record the concrete scope: branch source, reviewed spec, specific merge-back, or Apifox target and operation plan.
- An affirmative reply such as 确认、可以 or OK to an unambiguous proposal approves that proposal. No fixed wording is required.
- 继续 suffices only when the established next action is unambiguous and within that scope. Ask one focused question when it could refer to different actions.
- Do not ask again for an unchanged approved action. A different target, material scope change, destructive operation or withdrawn approval requires a new decision.
- Implementation completion does not authorize merge-back; repository approval does not authorize Apifox writes.

## Spec confirmation

Confirmation applies to reviewed contents, not any later file with the same name. Record spec path, Git blob/commit and conversation reference in the existing local plan. This is an evidence pointer, not permission created by a file.

When a user approves a concrete Chinese execution proposal identifying source branch, scope and verification, save those same contents as the repository spec, commit, and continue. Do not require identical text to be approved again solely because storage changed.

Branch-source confirmation alone is not spec confirmation. Show material spec changes and obtain approval for the delta. Formatting-only edits do not invalidate approval.

## Missing evidence

A spec, commit, branch name or local approved flag alone cannot prove user approval. Consult available conversation; when evidence is inaccessible, state the missing decision and ask only for it. Retain completed work and valid checks.
