# Development contract

This reference owns entry conditions, scope, evidence delivery, and handoffs. [Implementation methods](implementation-methods.md) own coding decisions; [TDD and verification](tdd-and-verification.md) owns execution and verification evidence.

## Required inputs

Start from the standalone task entry defined by the shared [artifact layout](../../product-design/references/artifact-layout.md). Read linked sources rather than asking the user to repeat available context.

| Input | Check before dependent implementation |
| --- | --- |
| Task and claim | Exact task path/version, assigned acceptance, exclusions, confirmed developer ownership, and any defect or replacement lineage |
| Product and overall design | Accessible exact versions and their approval evidence; applicable rules and shared contracts |
| Task design | Exact version, ready scope, local approach, affected code, planned self-tests, and required review dispositions |
| Git and code | Existing task branch, working directory, declared base/target, current revision, relevant local changes, and existing PR if any |
| Dependencies | Required interfaces, predecessor versions, environment inputs, and evidence for the stage they gate |
| Project instructions | Build and test configuration, coding conventions, required checks, and review policy |

Assignment alone does not prove a claim. Task-design readiness does not prove that inputs remain current. Recheck changed inputs and dependencies when starting or resuming. Do not silently replace pinned baselines with newer versions.

Route missing inputs to their owner:

| Missing input | Receiving workflow |
| --- | --- |
| Task design | [Technical design in task mode](../../technical-design/SKILL.md) |
| Confirmed claim | Applicable coordination workflow |
| Task definition | Planner |
| Task branch | Git workflow |

Preserve existing work. Read-only investigation and unaffected work can continue with valid inputs. Do not invent approval or readiness to replace missing prerequisites.

## Scope and authority

Implement the assigned acceptance within the approved baselines. Routine local choices need no new human gate. Record consequential local refinements in the task design and reassess affected tests before continuing. Use the [task-design contract](../../technical-design/references/document-contract.md#task-handoff-to-code-development) for required architect review and readiness.

Apply the supplied [reviewability policy](../../planner/references/planning-methods.md#estimate-work-and-review-scope). Report material scope growth before expanding the task. Return multiple independent goals to planner; obtain any required advance reviewer agreement for unusually large cohesive scope. Do not omit tests or necessary usage to reduce the diff.

### Preserve Git state and authorization

One development task retains one active branch and one PR. Use `git-workflow` when available, or the project's authorized Git procedure. Inspect and reuse existing state. Never reset another worker's branch, discard unrelated edits, or change another task's active checkout to obtain a convenient baseline. If isolation is missing, resolve it through the Git/runtime workflow before overlapping edits.

Commit cadence follows project policy and existing authorization. Traceable evidence does not require a commit after every Red or Green step. Preserve evidence before any authorized squash or history change.

Publish the PR through the applicable authorized platform workflow. Missing tools do not authorize a substitute external action or prove that publication occurred.

## Feedback and corrections

When implementation evidence changes the options, report the affected task and source versions, observation, impact, alternatives, uncertainty, and requested decision. Delivery Lead coordinates the receiving function:

| Finding | Decision owner |
| --- | --- |
| Unclear or changed product behavior or acceptance | PM using product-design |
| Shared interface, architecture, or material feasibility conflict | Architect using technical-design in overall mode |
| Local approach needs revision within the shared baseline | Assigned developer using technical-design in task mode |
| Task split, assignment, or dependency planning problem | Engineering lead using planner |
| Incorrect QA case | QA using test-design |
| Code defect within approved baselines | Developer correction, then independent review, integration, and affected QA |

Block only affected work when independence is supported. Never weaken acceptance or rewrite an upstream decision to turn a failing test green. If investigation repeats without new evidence or a viable option, preserve the blocker and request the missing fact or decision through Delivery Lead.

Before merge, corrections update the same task branch and PR. After merge, use a linked correction task with its own branch and PR under planner's contract. Retain finding identities and verify fixes; changes invalidate affected earlier review and test conclusions.

## Resumption

Read the task, design, evidence, current diff, and prior findings before continuing. Determine the last verified behavior and what changed since that evidence. Reproduce relevant checks when state has changed or evidence is insufficient. A recorded Green on an older revision is not proof for new code.

When interrupted, preserve code and record the current phase, completed checks, unfinished behavior, blockers, and next action. Do not fabricate historical Red evidence. [TDD and verification](tdd-and-verification.md#existing-code-and-alternative-verification) defines how to handle inherited work.

## Delivery conditions

### Implementation verification

Set `Implementation verified: Yes` only when:

- Assigned behavior is implemented against valid inputs; required design updates and reviews are complete.
- Each assigned acceptance condition has passing developer verification or a downstream verification obligation defined by its source. Record the downstream recipient and limits. Do not move a required developer check downstream merely because it could not run.
- Required developer checks pass for the delivered code state. Failed, unrun, skipped, or unsupported required checks keep this conclusion false.
- The complete task diff has been self-reviewed; known correctness, safety, and acceptance blockers are resolved. Retained nonblocking findings and scope are explicit.

Verify that the tested state corresponds to the submitted change. A pass that depends on excluded or uncommitted code cannot establish verification of the PR. Preserve unrelated work and validate the intended deliverable in a suitable isolated state when necessary.

### Publication and review handoff

Record `PR publication` separately as `Published`, `Prepared locally`, or `Blocked`, based on what actually happened. The ordinary independent-review handoff is ready only when the PR is published, its evidence is current, and the implementation conditions above are satisfied.

A draft or incomplete package can request help, but must not claim that readiness. Developer verification does not imply review acceptance, merge, QA acceptance, or ship approval.

### Delivery record

The handoff includes:

- Task path/version; product, overall, and task-design versions; claim and branch references.
- Purpose, implemented acceptance, relevant design refinements, changed behavior, and exclusions.
- Declared diff base/head, integration target, dependencies, and local changes not included in the PR.
- Actual authored additions/deletions, affected files/interfaces, risks, and generated artifacts reported separately under the reviewability policy.
- Acceptance-to-test mapping, actual execution evidence, required final checks, and verification limits.
- Open findings, implementation verification, publication state, next function, and responsible recipient.

Use the [delivery template](../assets/development-report-template.md) in the project's existing delivery record. If a separate local record is needed, save `development.md` beside the task entry and link it from `task.md`. Follow the shared artifact layout and reuse an existing valid evidence location.

Keep one authoritative execution record and reference it from the PR. Never insert planned or executed results into a source baseline as if that baseline had approved the implementation.
