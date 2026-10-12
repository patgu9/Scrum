# Handoff flow

Select the next step from current artifacts and observed state, not an assumed linear stage counter. The [coordination contract](coordination-contract.md) owns authority, evidence, approval, and completion requirements. Each row below still uses its common handoff.

## Forward routing

| Observed state | Next function and accountable recipient | Inputs and gate to check |
| --- | --- | --- |
| Goal received or product revision needed | product-design; PM | Goal, known constraints, product questions or feedback; discovery can identify missing facts |
| Product version ready for owner review | Requirements approval; human owner | Exact product version and decision request; dependent engineering waits |
| Product version approved | technical-design, overall mode; architect | Approved product version, project evidence, constraints; output is a feasible proposal for approval or feedback |
| Overall proposal ready for review | Technical approval; human owner | Exact overall design, product baseline, evidence, risks, and readiness; approval alone cannot establish feasibility |
| Overall design approved and ready for breakdown | planner; engineering lead | Approved product and overall versions, dependencies, repository context, and available developers |
| Ready assigned task exists | Claim workflow, then git-workflow; assigned developer | Exact standalone task path/version, stage prerequisites, and confirmed exclusive ownership; see task handoff below |
| Task claimed and branch established | technical-design, task mode; assigned developer | Claimed task, existing branch, approved baselines, acceptance, dependencies, and deferred choices |
| Task design ready for implementation | code-development; assigned developer | Valid inputs, resolved blocking local choices, required architect review, and any advance reviewer agreement |
| Focused task PR ready for review | code-review; independent Code Reviewer | Task/design links, base/head revisions, scope, self-tests, gaps, and findings; reviewer did not author the code |
| Current independent review accepts PR | code-integration; engineering lead | Current review, required checks, dependency state, target baseline, and task acceptance; integration owns the merge gate |
| Identified merged candidate ready for QA | test-design; QA | Exact candidate, approved acceptance, technical verification strategy, integration evidence, and test environment constraints |
| Versioned test cases available | test-execution; QA | Applicable cases and required checks, exact candidate/environment, and pre-release purpose; cases are planned evidence |
| QA accepts candidate | Ship approval; human owner | Exact candidate, target environment, QA evidence, retained issues, and operational constraints |
| Applicable ship approval recorded | deployment; Ops | QA-accepted candidate, approved environment/issues, access references, deployment and recovery constraints |
| Actual deployment identified | deployment service verification; Ops, and test-execution business verification; QA | Actual candidate/environment, required checks, and post-deployment purpose; neither report replaces the other |
| Both post-deployment reports pass | Final delivery summary; human owner | Reconcile both reports with deployed state and all completion conditions |

Use the existing [product](../../product-design/SKILL.md), [technical design](../../technical-design/SKILL.md), [planning](../../planner/SKILL.md), [development](../../code-development/SKILL.md), [Git](../../git-workflow/SKILL.md), and [integration](../../code-integration/SKILL.md) contracts when routing those functions. Locate other named capabilities in the target environment before dispatch. Their mention in this table does not establish availability.

QA case design follows candidate integration in this workflow. On resumption, QA can establish that an existing plan remains applicable or revise it through test-design before execution. Never infer test results from case coverage. A required failed or unrun check blocks acceptance and the accepted-candidate ship handoff.

## Task handoff and claim

Start from the [planner handoff](../../planner/references/plan-contract.md#common-handoff). Give each assigned developer the change directory, plan path/version, and exact standalone task path/version. Task entries own scope, acceptance, assignment, dependencies, readiness, and execution references; an index is a summary.

Before claim or resumption:

1. Read the task entry and pinned prerequisites. Check disposition, named assignment, readiness for the next stage, dependencies, and current claim/branch/PR evidence.
2. Reconcile conflicting task, index, and coordination records through the accountable owners. Superseded or cancelled tasks cannot be claimed. Completed work is not available merely because its definition remains active.
3. Confirm exclusive ownership through the applicable authorized coordination or platform workflow. Writing a name in Markdown is not a lock. If confirmation is unavailable or another owner holds the task, block claim and branch creation; report the missing capability or conflict.
4. Record confirmed ownership with its source and time through that workflow. The developer then creates or inspects the task branch using git-workflow, prepares task design, and starts coding only when implementation prerequisites hold.

For resumption or reassignment, inspect and reuse the existing task, branch, PR, and claim state. Obtain the applicable ownership transfer confirmation rather than starting another worker from stale records. Do not create duplicate claims or branches, discard work, or alter another task's active checkout. Isolation and claim enforcement belong to the execution workflow.

Readiness for assignment/claim differs from implementation readiness. A coding- or merge-stage dependency can permit independent earlier work only when supported by the task contract. Pending advance reviewer agreement can permit assignment or task design but blocks affected implementation. Apply the [reviewability policy](../../planner/references/planning-methods.md#estimate-work-and-review-scope); no line-count threshold grants readiness.

## Dispatch and progress

Prepare a concrete handoff with the common summary and accessible professional artifacts. Use the authorized transport when available, then record its observed outcome. If dispatch fails or its result is unknown, inspect delivery/receipt and current worker state before retrying. Do not create duplicate work to make a handoff appear successful.

Track each active dependency at its actual gate: claim, task design, coding, review, merge, QA, or release. Report ready next actions and affected blockers together. Do not freeze unrelated work or assume independence when impact is unresolved.

Report progress from role outputs and current evidence. A sent request is not acceptance, an accepted PR is not a merged candidate, and a merge is not permission to deploy. Return findings through [feedback and resumption](feedback-and-resumption.md) instead of skipping the failing stage.
