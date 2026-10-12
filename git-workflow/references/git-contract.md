# Git contract

This reference owns Git inputs, task identity, authority, and operation records. The caller owns professional readiness and the next handoff.

## Required context

Establish the requested operation, its scope, and existing authorization. For task operations, start from the standalone task entry under the [artifact layout](../../product-design/references/artifact-layout.md). Inspect:

| Input | Needed evidence |
| --- | --- |
| Task | Path/version, assigned scope, disposition, claim owner and confirmation source; existing branch and PR |
| Repository | Repository identity, working directory, current branch/revision, index, tracked and untracked changes, in-progress Git operations, and other worktrees |
| Baseline | Declared starting ref and exact revision, review base, integration target, dependencies and any stack relationship |
| Project policy | Branch/commit conventions, permitted update and merge methods, required checks, protected refs, and remote destination |
| Caller decision | Authorized action; for integration, current readiness evidence supplied by engineering lead |

Require only inputs applicable to the operation. Read-only diff inspection needs no development claim. New task branch creation requires confirmed claim and valid baseline, but task design is produced afterward. Do not require an existing PR before creating its branch.

Use repository instructions and existing records before asking for missing context. Resolve conflicting task ownership or baseline information through Delivery Lead. Do not silently use the latest default branch instead of a pinned revision. Missing remote access leaves remote state unverified; cached refs alone cannot prove current publication or merge readiness.

## Task and authority boundaries

Follow the [planner contract](../../planner/references/plan-contract.md#development-task-record): one task retains one active branch and one PR. Reassignment and pre-merge corrections reuse them. A post-merge correction gets a linked task and new branch/PR. Multiple review units require planner to revise task boundaries first.

Claim evidence comes from the applicable coordination workflow. A Markdown field, branch name, or new worktree is not an exclusive claim. Reuse a suitable isolated checkout; concurrent tasks must not switch or edit each other's active checkout. Inspect branch occupancy before creating or attaching a worktree.

Routine actions within existing authorization need no repeated permission request. Invocation does not authorize unrelated commits, a different remote, history rewriting, deletion, or deployment. Do not disable checks, bypass branch protection, discard edits, or overwrite another worker's branch to make an operation succeed. If an operation fails, inspect its resulting state before retrying. Stop dependent mutations when ownership or the outcome remains uncertain.

## Result record

Record observed execution references in the existing task or caller's evidence record. Do not create a second task definition or a separate report for every command. Include:

- Task path/version and caller; repository and working directory.
- Task branch, starting revision, declared review base and head, integration target, and observed remote state.
- Actions completed, resulting commit/ref identities, existing or published PR reference, and excluded local changes.
- Diff scope and checks when applicable, with tested revision, environment, actual results, and gaps.
- Unresolved findings, blocked operation and supplier, next function and accountable recipient.

Record branch and PR links only after observing them. For an uncertain push or merge, report the uncertainty and inspect the destination before retrying. A local commit does not prove a push, and a push does not prove a merge.
