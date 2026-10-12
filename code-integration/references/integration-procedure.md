# Integration procedure

Use the [integration contract](integration-contract.md) for acceptance conditions and output meaning. Keep provider commands and task-app status updates in their platform workflows.

## 1. Reconstruct current evidence

Read each task and PR, not only a queue summary. Confirm that the accepted head and declared comparison base match the actual change. Inspect the review's coverage, blocking findings, required check results, and dependency evidence.

If PR head, comparison base, target, scope, or approved inputs changed, assess what earlier evidence still covers. Record the rationale and obtain affected checks or independent review before merge. A green check for an older head does not cover new code. Target movement can change interactions even when the PR head stays unchanged.

Identify pre-merge and post-merge obligations from the technical design and repository policy. Prepare the integration checks and required environment before mutating the target. If merging the target would automatically deploy, resolve that pipeline conflict with the responsible owner before merge so QA and ship approval remain effective. Missing prerequisites block the affected operation; no live deployment is part of this procedure.

## 2. Order and prepare the changes

Order eligible PRs by declared dependencies. Do not bundle tasks into one PR or merge a dependent task before its prerequisite is satisfied. A dependency cycle or unclear required revision returns to planner or architect.

For stacked PRs, verify the predecessor's actual merge result before retargeting or updating the dependent branch. Squash/rebase integration can change predecessor commit identities and the displayed diff. Recalculate the dependent scope through Git Workflow and renew affected evidence; do not mistake inherited changes for newly reviewed work.

When needed, validate the proposed combination in an isolated checkout using the project's merge method. Record the tested source heads, target, and resulting tree or commit. Trial results support preparation but do not prove a remote merge or verification of a different candidate.

Resolve conflicts under [Git integration methods](../../git-workflow/references/integration-methods.md#resolve-conflicts-before-final-integration). Have the developer self-test the changed code. Obtain independent review before accepting the changes. If a shared contract must change, refer the proposed change to its design owner before continuing integration.

## 3. Recheck and merge

Immediately before mutation, re-read the PR head, target state, review conclusion, required checks, and dependencies. Use the approved merge mechanism with guards for the assessed revision or validated merge-queue state. Do not use an administrative override to bypass a failed gate.

If the target or PR changes before completion, reassess or let the protected queue rerun its required validation under project policy. Do not assume a head-only guard also protects the target. If the available mechanism cannot enforce the necessary gate, preserve the prepared result and report the missing capability.

Process each confirmed result before the next dependent PR. A queued response is pending. After a timeout or uncertain response, inspect remote state before retrying. Record already merged PRs even when later PRs fail; integration of a batch is not assumed atomic.

## 4. Verify the resulting candidate

Confirm actual merge results and capture the immutable candidate revision. Check that it includes the intended tasks and dependencies. Account for any other changes in the selected target snapshot; if their inclusion or evidence is unclear, resolve candidate scope before QA handoff.

Run required integration checks against that exact merged candidate in a suitable environment. Include relevant shared interfaces, dependency interactions, builds, migrations, or smoke checks when required by the approved strategy. Record command/check identity, revision, environment, actual result, and evidence location. Do not substitute a developer's pre-merge result for a required candidate check.

If evidence from a tested integration tree is reusable under project policy, demonstrate tree equivalence and state its limits. Commit-dependent builds or environment-dependent behavior may still require execution against the final revision. An unexplained correspondence cannot establish verification.

Pin the tested candidate even if the target later advances. If the delivery scope changes to a newer target revision, identify a new candidate and reassess its evidence. Never send the moving target name to QA as the sole version reference.

## 5. Hand off or return the blocker

Fill the [integration report](../assets/integration-report-template.md) with observed state and apply each output condition separately. A post-merge check failure reports `Merged` and `Integration verified: No`; it does not erase the merge. Route the failure and retain its affected candidate identity. Recovery uses existing authority and Git methods; it cannot declare the requested candidate complete.

For a ready candidate, supply QA with product acceptance, technical verification strategy, candidate and environment context, included tasks, integration evidence, and retained findings. Project Manager routes test-design, then test-execution. Preserve defects and nonblocking issues for downstream disposition. Do not let merging trigger deployment before QA acceptance and owner ship approval.
