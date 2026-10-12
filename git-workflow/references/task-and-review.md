# Task branches and review

The [Git contract](git-contract.md) applies to every operation here. Commands below are examples using caller-supplied variables, not a fixed branching policy. Verify variable values and use explicit paths and refs.

## Establish or resume the branch

Inspect without changing the checkout:

```sh
git status --short --branch
git branch --show-current
git rev-parse HEAD
git worktree list --porcelain
git diff --stat
git diff --cached --stat
```

Read relevant diffs, including staged changes and task-related untracked files. Detect an unfinished merge, rebase, or cherry-pick before starting another operation. Identify who owns that work; do not automatically abort it. Inspect remote destinations without exposing embedded credentials in handoffs.

For a new claimed task, resolve the declared start revision and check for an existing local or remote task branch. Refresh the relevant remote refs when needed and accessible. Fetching discovers remote state; it does not change a pinned task baseline.

Use the runtime's workspace mechanism when available. Otherwise, prepare an authorized isolated location. First, resolve `start_ref` to a commit ID:

```sh
git rev-parse --verify "${start_ref}^{commit}"
```

If resolution fails, resolve the missing or invalid ref before continuing. Set `start_sha` to the returned commit ID. Confirm that it matches the task's declared baseline before creating the worktree:

```sh
git worktree add -b "$task_branch" "$task_worktree" "$start_sha"
```

Follow supplied naming conventions; if none exist, use a unique task-specific name under the environment's required prefix. Confirm the resulting branch, directory, and HEAD before recording them. Continue with [task technical design](../../technical-design/SKILL.md) before code changes.

For resumed work, inspect the recorded branch, PR, findings, and local changes. Reuse its checkout if suitable; otherwise use the authorized isolation mechanism without forcing a branch already checked out elsewhere. A missing local branch can track the verified existing remote branch. Do not create a second task branch merely because its previous checkout is unavailable.

## Commit the intended change

Keep behavior, related tests, and necessary documentation together. Use project commit conventions; when unspecified, a concise subject naming the change and an optional reason are sufficient. Conventional Commits can be used when the project adopts them; this Skill does not install a commit template or change global configuration.

Stage explicit files or hunks after inspecting the whole index. Pre-existing staged changes are not automatically part of this task. If they cannot be safely separated, preserve them and prepare the deliverable in an isolated checkout. Do not use an indiscriminate `git add .` in a shared or mixed worktree.

```sh
git add -- "$task_file"
git diff --cached --check
git diff --cached
git commit -m "$commit_subject"
```

Inspect the resulting commit and remaining status. Required checks must cover the delivered code, not a working tree that depends on excluded edits. Follow the caller's verification contract; a commit hook pass is evidence only for the checks it ran. Preserve execution evidence before an authorized squash or amend.

## Declare and inspect the review diff

Resolve the declared base and head to commit IDs and set `base_sha` and `head_sha`, respectively. Distinguish the declared base tip from the actual comparison base. Before running the diff commands, set `diff_base_sha` according to the review provider's comparison convention:

- For a common-ancestor PR diff, run `git merge-base "$base_sha" "$head_sha"`. Set `diff_base_sha` to the returned merge-base commit ID. If the command fails or the comparison base is ambiguous, resolve that issue before continuing.
- For an endpoint comparison, set `diff_base_sha` to `base_sha`.

Record the comparison convention and exact commit IDs. Match the review provider's displayed diff and explain any mismatch before claiming coverage.

```sh
git diff --name-status "$diff_base_sha" "$head_sha"
git diff --numstat "$diff_base_sha" "$head_sha"
git diff --stat "$diff_base_sha" "$head_sha"
git diff --check "$diff_base_sha" "$head_sha"
```

Review the full diff and relevant surrounding code, not only these summaries. Stacked work declares its predecessor and final target so that ancestor changes are not mistaken for the task's own changes. A changed predecessor or retargeted PR requires scope and evidence reassessment.

Apply the existing [reviewability policy](../../planner/references/planning-methods.md#estimate-work-and-review-scope). Report actual additions and deletions in maintained code, tests, and documentation, including Agent-authored work. Separately report reproducible generated artifacts, generation/validation evidence, and total raw changes. Binary `numstat` entries are not zero-line changes; name the artifacts and review method. Account for renames and unusual filenames; use NUL-delimited Git output if automating path parsing.

Counts describe scope and introduce no numerical gate. Keep tests and usage needed for a complete change. Return unrelated goals or material growth to planner; missing advance reviewer agreement cannot be repaired by merely reporting a small count.

## Prepare or update the task PR

Find and reuse the task's existing PR before publishing. Prepare a concise description containing:

- Task path/version, requirement references, and product, overall, and task-design baselines.
- Problem, resulting behavior, acceptance scope, and exclusions.
- Branch, comparison convention, exact base/head revisions, target, and dependencies.
- Actual scope, affected interfaces, risks, applicable advance reviewer agreement, and evidence links.
- Self-test results for the submitted state, unrun checks, unresolved findings, and the next reviewer.

Use [Technical Writing](../../technical-writing/SKILL.md) and the project's PR format. Keep one authoritative execution record and reference it. When branch publication is authorized, verify the checkout, remote destination, and task head before pushing an explicit ref:

```sh
git push -u "$remote" "HEAD:refs/heads/${task_branch}"
git ls-remote --heads "$remote" "refs/heads/${task_branch}"
```

Compare the observed remote revision with the intended head. A non-fast-forward rejection requires inspection of concurrent work, not an automatic force push. Publish or update the PR through the authorized platform workflow; verify returned PR identity, head, and target. Retain a local draft if publication is unavailable. Subsequent commits retain findings and require reassessment of affected review and checks.
