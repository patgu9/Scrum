# Integration methods

Use these methods for the caller's authorized operation under the [Git contract](git-contract.md). [Code Integration](../../code-integration/SKILL.md) owns merge readiness; command success cannot substitute for that decision.

## Update a task branch

Inspect the current branch, local changes, remote head, target revision, and dependent branches. Follow the project's chosen merge or rebase policy. Avoid an implicit pull that can select an unintended operation or upstream.

Merge preserves existing commit identities. Rebase, amend, and squash rewrite identities and can invalidate review or dependent work. Do not rewrite shared or protected history. A published task branch needs applicable authorization and coordination before any permitted rewrite; being its original author is not sufficient evidence that nobody depends on it.

For an authorized rewrite, record the expected remote head and protect the push against concurrent changes with an explicit lease. A generic example is:

```sh
git push --force-with-lease="refs/heads/${task_branch}:${expected_remote_sha}" "$remote" "HEAD:refs/heads/${task_branch}"
```

Run this only from the verified task checkout and only when project policy permits the rewrite. A rejected lease requires reinspection and coordination; do not weaken the lease or blindly retry. Preserve evidence references and reassess scope, review, and tests after changing commits or the baseline.

## Resolve conflicts before final integration

Reproduce the conflict in the task's isolated workspace or an authorized disposable integration checkout. Record the exact heads and inspect both intended behaviors against approved contracts. Do not choose an entire side merely to clear conflict markers; `ours` and `theirs` have operation-dependent meanings.

Return required behavioral choices to their owner. A resolution that changes code needs self-tests and independent review before acceptance, even when engineering lead authored it. Prefer updating the same unmerged task branch and PR so the resolved diff remains reviewable. Do not hide new logic inside an unreviewed merge commit.

After resolution, inspect the resulting diff, unresolved paths, and required checks. Continue or abort only the operation this workflow owns. Preserve unrelated or pre-existing work. An unresolved conflict produces a blocker with the affected files, revisions, attempted resolution, and responsible recipient.

## Execute an accepted integration

Receive the accepted PR, current head, validated target revision, merge method, and gate evidence from engineering lead. Use the project's protected merge or merge-queue workflow when applicable. Provider-specific commands stay in that platform workflow.

Bind the operation to the reviewed head and validated target or equivalent protected queue state. A guard on PR head alone does not detect target movement. If either changes, reassess the affected evidence before continuing. A local trial merge or local target commit is not a confirmed remote merge.

Observe the remote result after the operation. Record the original PR head, target before integration, actual merge/squash/rebased result, and resulting candidate revision. Squash and rebase can change commit identity; use provider evidence and the resulting change to establish inclusion instead of assuming the original head must be an ancestor.

If the response is lost or times out, inspect the PR and target before retrying. A queued merge remains pending until completion is confirmed. Preserve a confirmed merged result even if subsequent checks fail; return that failure through Code Integration instead of reporting that nothing merged.

## Recovery and cleanup

Prefer a new revert change for an authorized correction to shared history. Inspect its scope and dependencies; a revert still needs the applicable review and verification. Do not use a hard reset or force push to hide a failed integration. Post-merge defects follow the linked correction-task contract.

Branch/worktree cleanup is separate from integration success. Perform it only within the requested scope after confirming merged inclusion, retained evidence, clean worktree state, and no remaining dependent work. Squash merges may need explicit inclusion evidence because ancestry checks differ. Never force-delete work merely because a task is marked complete. Git cleanup and merge do not deploy, tag, or authorize release.
