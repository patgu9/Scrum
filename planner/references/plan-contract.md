# Plan contract

This reference owns planning inputs, artifact fields, readiness, and revision handling. [Planning methods](planning-methods.md) owns decomposition, estimation, and plan review.

## Inputs and authority

Engineering lead is accountable for task breakdown and developer assignment. Project Manager coordinates the resulting handoffs and blockers. These responsibilities can use several Skills; invoking another Skill does not create another role or establish independent review.

Before dependent planning, inspect:

| Input | Required evidence and supplier |
| --- | --- |
| Product baseline | Accessible document, exact version or stable snapshot, included scope, and owner approval evidence; supplied by PM |
| Overall technical baseline | Accessible document, exact version, owner approval, and readiness for the requested breakdown scope; supplied by architect |
| Repository context | Relevant code revision and local changes, project instructions, existing work, test conventions, Git policy, and integration target; supplied by project context and engineering lead |
| Dependencies | Shared contracts, external prerequisites, integration obligations, and deferred local decisions with constraints and required evidence; supplied by overall design and current task records |
| Available developers | Actual developer identities, relevant capabilities, availability, and existing assignments; supplied by engineering lead or Project Manager |
| Review scope and feedback | Applicable reviewability policy, existing findings, task/branch/PR identities, and returns affecting task boundaries; supplied by project policy and originating functions |

Use the overall design's [planning readiness contract](../../technical-design/references/document-contract.md#overall-handoff-to-planner). Approval alone cannot resolve missing feasibility evidence. Do not treat an unresolved shared interface, storage guarantee, or security constraint as a harmless local choice.

For missing, inaccessible, conflicting, or stale input, identify the affected scope, required evidence, supplier, and next action. Do not invent approved requirements, developer availability, branch existence, or completed dependencies.

If the user explicitly requests provisional exploration, label it `DRAFT` and keep dependent assignment blocked. Otherwise, return the blocker and continue only work with valid, unaffected inputs.

Routine decomposition, local assignment, and corrections within approved baselines need no additional human approval. Product or shared-design changes return to their owning function and existing approval point. Assignment recorded in a plan is not proof of publication to an app, developer claim, or execution.

## Artifact and versions

Save `task-plan.md` beside the source product and overall technical documents in the existing change directory. Create one standalone entry point per development task at `tasks/<task-key>/task.md` within that directory. Planning does not create another product change directory.

Use the stable task ID in lowercase for `<task-key>`: task `T1` uses `tasks/t1/task.md`. Check for ID and path collisions before creating files. Never renumber existing tasks or overwrite another task. Keep titles, owners, dates, and status in the records, not directory names. Paths stay stable when these values change; do not move tasks between status directories. Qualify cross-change task references with the source change directory.

Reuse valid existing task paths unless migration is requested or needed to resolve ambiguity. When converting a plan with inline task bodies, extract them while preserving IDs, scope, baselines, claims, and branch/PR links. Replace each body with an index link after verifying the extracted content and affected references. Keep one current definition per task.

Use relative links and exact source versions. Each task links back to the plan; in the default directory, use `../../task-plan.md`. Link dependencies to their task files, such as `../t2/task.md`. Add supporting evidence beside its task and link it from `task.md`. A file's presence or location does not establish readiness or approval.

Use the [plan index template](../assets/task-plan-template.md) and [task template](../assets/task-template.md). A project format can change presentation but must retain a standalone Markdown file for each task, even for a one-task plan. Do not create empty task designs, branches, or downstream delivery artifacts.

### Version and identify artifacts

Version the plan and each task independently, starting at `v1`. Increment the version when its contract changes substantively. Revise current files in place and preserve prior content through accessible history or linked immutable snapshots. Do not create competing current files such as `task-v2.md` or `task-final.md`. Preserve the prior decision basis in its revision record. For operational updates, such as a confirmed claim, record the time and source without implying a new scope version.

Keep task and feedback IDs stable; never reuse a retired ID. Qualify rule, contract, test, and task IDs by their source document when they could collide. For example, `T1` in a test inventory is not automatically task `T1`.

Write concise English unless the user or project requires another language. Remove template prompts from completed output. Use `Unknown`, `Pending`, or `Not applicable` with a reason when supported; do not invent content to fill a field.

### Keep the plan and task records consistent

The plan owns change-level scope, coverage, shared integration responsibilities, overall dependency order, cross-task issues, planning review, and handoff. Its task index links every task and names the version summarized. Include accepted source exclusions rather than silently omitting rules.

Record the required user path or the outcome for a technical consumer and the decomposition basis in the plan. Include candidate boundaries, meaningful alternatives when available, and the selection rationale. Reuse source rules and examples; link unresolved questions to their accountable recipients. Scale this record to the change using the [five-step method](planning-methods.md#five-step-decomposition).

Each task file owns its goal, acceptance, direct dependencies, assignment, baselines, readiness, blockers, lineage, and observed execution links. The index may summarize these fields but must not repeat full task bodies.

Update affected task files and the index together, then check their agreement. If they differ, read the task file and referenced evidence. Report the stale summary and resolve it before the affected claim or handoff.

Use `Active`, `Superseded`, or `Cancelled` to distinguish current task definitions from retired ones. Active does not mean available or completed: readiness, confirmed claim, and observed execution evidence remain separate. Superseded or cancelled tasks are not claimable; completed work is not reopened merely because its definition remains active.

Pin exact product and overall-design versions in each task file, together with the source plan version and required code baseline. Link shared decisions without copying their prose.

A later plan revision does not silently retarget tasks to newer inputs. A change only to a summary or another task need not invalidate an unchanged task. Assess actual impact and record the supported conclusion.

## Development task record

Each standalone task must supply the following before assignment is actionable. An Agent must be able to start from that file and follow exact references to its prerequisites without reading every other task or reconstructing conversation history.

| Field | Required content |
| --- | --- |
| Identity and lineage | Stable task ID, task version, title, plan backlink, active/superseded/cancelled disposition, and original task or defect links when split or corrective |
| Goal and boundaries | One verifiable outcome, required changes and likely modules, explicit exclusions, and a brief boundary rationale linked to the plan's decomposition basis; no unrelated cleanup |
| Baselines and traceability | Exact plan, approved product, overall-design, and code versions with accessible paths and approval evidence; assigned rule/example/contract references |
| Acceptance and verification | Observable conditions, concrete scenarios or source example references, expected outcomes, required self-test/regression obligations, and shared integration checks with their responsible recipients; planned evidence remains planned |
| Dependencies | Predecessor or external input, required artifact/version or condition, current evidence, and whether it gates claim, task design, coding, review, or merge |
| Assignment | Named available developer, assignment basis and relevant capacity limits; otherwise `Unassigned` with the missing input and supplier |
| Git baseline | Repository, declared base ref and known revision, integration target, dependency/stack relationship if applicable, and claim-time recheck requirements |
| Existing execution links | Claim owner/state, time and confirmation source; actual branch/PR, task design, and evidence links for resumed tasks. New tasks record `Pending claim` and `Not created`, without links to nonexistent artifacts |
| Deferred decisions | Source decision reference, developer responsible after assignment, allowed choices, constraints, required evidence, and resolution point before affected coding |
| Effort and review scope | Design, implementation, and verification effort; an agreed time boundary/checkpoint or Unknown with supplier; affected files/interfaces, behavioral risk, estimated authored additions plus deletions, generated changes separately, uncertainty, and reviewability disposition with rationale and any required advance reviewer agreement |
| Readiness and handoff | Ready for assignment/claim with reasons, blockers and owners, next function and accountable recipient; this is not readiness for coding |

One assigned development task corresponds to one active branch and one PR against its declared base. A task can depend on another task without being independently deployable. Do not bundle separate tasks into one PR or split one task into several independently reviewed PRs without first revising the task boundaries.

New branches are created by the developer after claim and before code changes, through `git-workflow` or the project's authorized Git procedure. Inspect and reuse recorded branches for resumed or reassigned work. Do not discard work or create duplicates. Concurrent tasks must not change each other's active checkout; the execution workflow handles isolation. Planner records the required baseline and constraints without selecting an unsupported branching model.

## Agent entry point and claim handoff

Project Manager gives the assigned Agent the exact task file path and version. The plan is a discovery index, not sufficient evidence that a task is available. Before claim or resumption, the Agent reads its task file, checks disposition, assignment, readiness, pinned sources, dependency evidence, and any existing claim/branch/PR.

The applicable coordination or platform workflow confirms exclusive ownership before branch creation. A Markdown field is a record, not an atomic lock. If another owner holds the task, records conflict, or exclusive ownership cannot be confirmed, return that blocker through Project Manager; do not race another Agent by editing the file. Planner does not implement claim transport or a scheduler.

Record confirmed claim evidence in the task file through the authorized workflow. Then the developer creates or inspects its branch and produces task-mode technical design. Add the local design link only after the file exists. A simple task may have a short design file; its task entry point still remains separate. Update observed branch, PR, and verification links without treating a plan or a claim as completed implementation.

## Status and readiness

These statuses describe the planning artifact, not task-app states:

| Plan status | Meaning |
| --- | --- |
| `DRAFT` | Planning or plan review is incomplete for the declared scope |
| `READY` | Plan review is complete and every included task is ready for assignment/claim |
| `PARTIAL` | Plan review is complete; explicitly named tasks are ready, while others remain blocked, unassigned, or retired |
| `BLOCKED` | No included active task is ready; record required inputs or decisions and their suppliers |

A task is ready for assignment/claim only when all of these conditions hold:

- Its exact approved baselines remain valid.
- Its boundary and acceptance are clear, and its required task fields are usable.
- It has a named available developer and an actionable Git baseline.
- No unresolved dependency or decision gates claim or task design.

Apply the [reviewability policy](planning-methods.md#estimate-work-and-review-scope). A required advance reviewer agreement can be pending during assignment or local design, but blocks implementation of that scope. Do not claim agreement without evidence or confuse it with acceptance of the resulting code.

Evaluate each dependency at the stage it gates:

| Condition | Readiness consequence |
| --- | --- |
| Missing architectural feasibility or shared contract | Block affected assignment, even if owner approval exists |
| Dependency gates coding or merge, but independent local design is supported | Local design may proceed; state the restriction and evidence of independence |
| New task has no branch yet | Expected before claim; not a planning blocker |
| Git base is missing or invalid | Block affected assignment/claim |
| App publication or a downstream Skill is unavailable | Record a delivery blocker separately from planning readiness |

Unknown impact is not evidence of independence.

Keep `Ready for assignment/claim` separate from `Ready for implementation`. The latter belongs to task-mode `technical-design` after claim and branch creation, including required architect review. Plan readiness also does not establish review acceptance, merge readiness, QA acceptance, or ship approval.

Readiness applies only to the named scope, source versions, and observed conditions. Recheck before handoff and after material changes.

For an already claimed task, assess readiness to resume the affected stage using its current execution state. Do not require a duplicate claim or treat completed stages as pending merely because the plan was revised.

For a plan with no remaining development scope, record that conclusion and the next recipient. Do not label finished work blocked because no new task is ready.

## Replanning and feedback

Read the existing plan and affected task, branch, PR, finding, and dependency records before revising work.

| Trigger | Planner action |
| --- | --- |
| Reassignment or resumption | Inspect current work and baselines, name the new available owner, retain task/branch/PR identities, and recheck readiness |
| Scope growth or oversized review | Assess decomposition before additional unrelated work. Create a standalone file for each replacement task, retain the original with superseded disposition and links, distribute every acceptance condition, and update dependency links and the index |
| Same-task correction before merge | Keep the existing task, branch, and PR. Retain findings; request updated evidence and review for the changed diff |
| Defect after merge | Create a new linked task file and future branch/PR. Preserve the originating defect, candidate/version, and regression acceptance; retain the original task file |
| Product or overall baseline changes | Record invalidated tasks and downstream evidence, block affected work, and replan only after applicable approvals and readiness are current |

When splitting work already in progress, record where existing changes belong and which branch/PR remains active for each task. Mark superseded records explicitly. Leave actual transfer of changes or branch operations to the authorized Git workflow. Do not claim reassignment or a new plan moved the code.

Do not close a defect because its corrective task exists. Closure needs confirming review or test evidence from the responsible function. Preserve nonblocking findings for downstream disposition; planning cannot waive an unmet acceptance condition or a correctness or safety issue.

For an upstream constraint, provide a feedback issue with:

- Stable identity, originating function, affected tasks and document-qualified requirements/contracts, and exact baseline versions.
- Constraint, supporting observations, estimates and uncertainty, and impact on downstream work.
- Considered alternatives and tradeoffs, or an explicit statement that no alternative is known.
- Requested decision or missing fact, receiving function and accountable role, and affected work that must wait.

Route behavior, scope, or acceptance changes to PM using `product-design`. Route shared architecture and interfaces to the architect using overall `technical-design`. Local design corrections go to the assigned developer using task mode. Planning and assignment corrections stay with engineering lead using `planner`. Project Manager tracks these handoffs through `project-manager`; no platform commands belong in this contract.

Do not silently revise upstream decisions, weaken acceptance, or invent a cost/complexity threshold. Without a supplied limit, return an evidenced tradeoff or fact request. Preserve prior decisions and identify affected plans, task designs, interfaces, code, tests, and review conclusions. Independent work continues only with supported validity of its inputs, interfaces, dependencies, and approvals.

Close feedback only with a supported specialist resolution or an explicit owner decision to defer or stop the affected scope. Approval alone does not prove feasibility; deferral is not delivery.

If the same issue returns on the same baseline without new evidence or a viable alternative, stop repeating the handoff. Escalate through Project Manager. Include attempted options, consequences, and the missing fact or authority. Keep affected work blocked.

## Common handoff

Every output, including a blocker or feedback return, identifies:

1. Change/task scope and exact input versions.
2. Plan path/version and standalone task paths/versions, including replacement or superseded entries when relevant.
3. Conclusion, actual plan checks and evidence, and verification limits.
4. Unresolved issues with stable identities, owners, and affected work.
5. Next function and responsible recipient for each ready task or blocker.

For a forward handoff, include ready and blocked task IDs, assignments, dependency conditions, Git baselines, reviewability dispositions and any advance agreements, and deferred decisions. Project Manager coordinates the recorded assignments; the developer claims a ready task, establishes its branch, and completes task design before coding. Preserve a handoff even when the same Agent holds consecutive responsibilities.

Report absent follow-on Skills or unavailable routing separately. Do not publish tasks, contact recipients, spawn workers, or operate Git merely to make the plan appear executed. Such operations require their applicable workflow and existing user authorization. Downstream self-tests, independent code review, integration, QA, and ship approval remain required.
