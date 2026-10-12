# Feedback and resumption

Any function can return evidence before completing its forward deliverable. Project Manager tracks the return and affected work; the receiving function owns the professional decision.

## Preserve the feedback

Keep a stable issue ID, originating function, affected task/requirement/contract and exact baseline versions, constraint, supporting observations, estimates and uncertainty, impact, alternatives with tradeoffs, and requested decision or missing fact. Name the receiving function and accountable recipient. If no alternative is known, state that explicitly.

Preserve findings and previous attempts across returns. Without a supplied business limit, a cost or complexity estimate is a tradeoff or clarification request, not an invented threshold or proof of infeasibility.

## Route to the decision owner

| Finding | Receiving function and owner | Required next outcome |
| --- | --- | --- |
| Value, scope, behavior, or acceptance ambiguity | product-design; PM | Revised product proposal or supported response requesting evidence; changed product version needs owner approval |
| Shared architecture, interface, feasibility, or technical constraint | technical-design, overall mode; architect | Supported resolution or revised overall proposal; changed baseline needs owner technical approval |
| Local approach within approved shared constraints | technical-design, task mode; assigned developer | Updated task design and readiness, including required architect review |
| Assignment, task size, split, or dependency planning | planner; engineering lead | Revised assignments or task boundaries with preserved lineage and acceptance coverage |
| Code defect before merge, within the same task and approved scope | code-development; assigned developer | Correction in existing branch/PR, self-tests, and current independent review |
| Code defect after merge | planner; engineering lead, then assigned developer | New linked correction task and branch/PR, self-tests, independent review, integration, and affected QA |
| Missing or stale review, review coverage, or advance agreement | code-review; independent Code Reviewer, with engineering lead for scope | Applicable independent review or scope agreement; advance agreement is not code acceptance |
| Integration conflict or failed integration evidence | code-integration; engineering lead | Updated integration result or routed correction; new code still needs self-tests and independent review |
| Incorrect test case | test-design; QA | Corrected, versioned cases before test-execution reruns; acceptance cannot be weakened to obtain a pass |
| Missing test evidence or test environment | test-execution; QA, with the named environment owner | Required execution evidence or explicit blocker; no inferred QA acceptance |
| Deployment or service incident | deployment; Ops | Actual deployed state and recovery result within supplied authority; route design-changing evidence upstream too |
| Missing input, capability, or authority | Accountable supplier or human owner | Supplied input, supported alternative, or explicit decision; dependent work waits |

Corrections within approved product and overall technical scope need no new scope approval. They still pass the affected design, self-test, independent code review, integration, and QA gates. Route growth or splitting to planner before expanding the task. Preserve original task entries and replacement links; coordination does not redistribute acceptance or move code itself.

## Assess impact and resume

Record the affected dependency chain before advancing work. For each affected plan, task, task design, code revision, test plan/case, review conclusion, test result, or approval, identify:

- Previous baseline and evidence reference.
- Changed input and reason it may invalidate the output.
- Stage that waits, accountable reassessment owner, and needed evidence or decision.
- Updated output/version, or an explicit supported conclusion that the output remains valid.

Preserve prior decisions and evidence as history. PM revisits product value and alternatives; engineering reassesses feasibility after the applicable product approval. A changed overall solution returns to technical approval before dependent planning. Approval alone does not resolve feasibility or close feedback.

Resume affected work only after applicable approvals and output reassessments are current. Changed code still receives the required review and tests. Carry evidence forward only with a supported applicability conclusion from the responsible function; do not relabel an old run or reviewed revision as new evidence.

Independent work can continue only when its inputs, interfaces, dependencies, and approvals remain valid. Record why it is independent. If impact is uncertain, obtain the missing assessment before treating that work as unaffected. A plan version increment alone need not invalidate unrelated tasks, and an unchanged plan number cannot validate changed inputs.

After interruption, inspect latest artifacts, claims, PR/merge state, decisions, candidate, and deployment reports relevant to the pending action. Reconcile pending or unknown external outcomes before retrying. Reuse stable identities and report stale summaries; do not restart completed stages merely because the coordination record lagged behind execution.

## Resolve or escalate

Close a defect only with confirming review or test evidence from its responsible function for the affected version. Creating a correction task or sending a handoff does not close it.

A broader feedback loop closes with a supported specialist resolution or an explicit owner decision to defer or stop the affected scope. Record the resolution, source, affected work, and remaining obligations. Deferral and stopping do not establish delivered functionality.

If the same issue returns against the same baseline without new evidence or a viable alternative, do not send an identical automatic handoff again. If necessary facts or authority are unavailable, escalate instead of inventing them. Request a human decision with attempts, options, consequences, missing information, and work that waits. Keep affected work blocked while supported independent work continues. Do not claim success because attempts are exhausted.

## Deployment failure

A failed deployment or required post-deployment check keeps ship incomplete. Obtain Ops' actual deployed candidate/environment, failure evidence, recovery authority, and observed recovery outcome. Ops may act within supplied approved constraints; missing authority requires a decision request through Project Manager.

If code changes, follow the correction path and applicable verification. If candidate, environment, or retained issues change, renew ship approval. Reconcile Ops and QA reports against the actual deployment before reconsidering completion. Returning service to an earlier version is recovery evidence, not delivery of the requested candidate.
