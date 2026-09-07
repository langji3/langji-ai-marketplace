# Recover the existing task

Use this when resuming or when Git/spec state changes. Reuse the spec and ignored local plan; do not add a task-state store.

## Evidence to retain

- Developer branch and source commit at AI branch creation.
- AI branch and absolute worktree directory.
- Spec path, reviewed Git blob/commit and conversation approval reference.
- Last completed goal and remaining goals.
- Verification commands/results and the commit or worktree contents actually checked.
- Pending merge-back/external-write proposal and authorization scope.

Never substitute today's developer HEAD for an unknown historical source commit. Mark it unknown, inspect history/diffs, and resolve it before integration.

## Continue from evidence

Inspect current branch, git status --short, git worktree list --porcelain, spec history/content, plan ignore/tracking status and implementation commits. Compare current spec with reviewed contents and current code with verified revision. Do not discard changes or replay completed commits.

A missing plan can be reconstructed from Git/spec and available conversation. Missing approval uses [authorization rules](authorization.md). Materially changed spec scope needs delta confirmation before further implementation.

## Concurrent work

Simultaneous implementations need separate worktrees/directories and unique branches. A branch name does not isolate a shared checkout. Never switch branches under another running task.

Before branch creation inspect existing branches/worktrees. Reuse an existing name only after verifying requirement and origin; otherwise choose a unique suffix. Record the source HEAD used. If the developer branch is checked out elsewhere, integrate there only after it is idle and clean.

## Target advancement and integration

Before requesting merge-back compare recorded source commit with current developer HEAD and inspect combined changes. If target advanced, integrate it into an isolated AI or disposable integration worktree, resolve conflicts within approved scope and rerun relevant checks. Never reset/force-update the developer branch.

Report current source/target commits and combined-tree evidence. Immediately after approval recheck heads and worktree state. Changed heads require a recomputed proposal and verification; changed merge contents or target require renewed approval.

After squash merge verify the resulting developer tree. A failed check stops downstream integration and reports the actual commit/failure. Do not automatically reset or revert the developer branch.
