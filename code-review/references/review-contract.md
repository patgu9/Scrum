# Review contract

This reference owns inputs, authority, findings, and handoff conditions. [Review methods](review-methods.md) own analysis; the [OCR guide](open-code-review.md) owns tool execution.

## Inputs and independence

Start from the standalone task entry and its linked [development evidence](../../code-development/references/development-contract.md#delivery-conditions).

| Input | Required evidence and supplier |
| --- | --- |
| Task and baselines | Task path/version, acceptance, exclusions, approved product and overall-design versions, current task design; developer and design owners |
| Submitted change | PR identity, repository, declared base/head, comparison convention, integration target, predecessor dependencies, and actual scope; developer |
| Verification | Self-tests for the submitted revision, required repository checks, execution evidence, and explicit downstream obligations; developer and check owners |
| Review context | Project instructions, applicable review rules, advance agreement when required, prior findings and correction history |
| Reviewer | Identified reviewer who did not author the reviewed code, with access to the required context and evidence |

Missing, conflicting, or stale inputs block the affected conclusion. Read-only investigation can continue, but an incomplete submission cannot receive ordinary review acceptance. Review of a local draft or commit is advisory until the task PR and required handoff evidence exist.

Independence belongs to the accountable reviewer, not the command name or model. A developer running OCR on its own code provides self-review evidence. If the reviewer is asked to implement a correction, route that work to code-development; the resulting code needs another eligible reviewer. Suggested changes in a report do not authorize edits, commits, PR publication, or merge. Use the applicable platform workflow and existing authorization for external review publication.

## Reviewability and advance agreement

Use the [shared reviewability policy](../../planner/references/planning-methods.md#estimate-work-and-review-scope) as the authority for cohesion, scope reporting, splitting, and unusually large changes. Do not introduce a numerical line-count gate.

For advance agreement, record the task and proposal versions, cohesive goal, alternatives to splitting, expected scope, risks, reviewer responsibilities, and validation strategy. Return `Agreed`, `Changes requested`, or `Insufficient context`, with reasons and the accountable recipient. No code review or OCR run is required to accept a review assignment. Set code acceptance to `Not assessed`.

An agreement applies only to its recorded scope. Reassess changed scope or inputs. If a large PR already exists without the required agreement, retain the work and resolve reviewability with engineering lead before acceptance. Do not invent a past agreement.

## Findings and dispositions

Give each finding a stable ID scoped to its task. Record the affected revision, verified path and line or precise artifact location, triggering behavior, evidence, impact, blocking decision, and responsible recipient. Link the violated acceptance condition or contract where applicable. Distinguish a demonstrated defect from a question requiring investigation.

Keep OCR severity and category as source metadata. They do not decide this team's blocking classification:

- An unmet acceptance criterion or a correctness or safety problem is blocking, even when OCR labels it low severity.
- Missing required evidence or an unresolved material uncertainty blocks the affected conclusion; do not invent a code defect to describe an evidence gap.
- Optional polish may remain nonblocking. Personal preference alone cannot block review acceptance. Preserve retained issues for owner confirmation at ship approval.

Preserve raw tool findings and record reasons for dismissed false positives or duplicates. Do not present unsupported tool claims as confirmed findings. A finding remains `Open` until a supported disposition exists. Use `Resolved` only with confirming review or test evidence for the affected version. `Retained` means a nonblocking issue remains visible; `Dismissed` requires a reason. A developer's reply or a correction task alone cannot close a finding.

## Conclusions and handoff

Report these fields separately:

| Field | Values and meaning |
| --- | --- |
| Review coverage | `Complete`, `Partial`, or `Not started`; identify reviewed scope and gaps, including tool exclusions |
| Code review acceptance | `Accepted`, `Changes requested`, or `Not assessed`; tied to the exact compared revisions |
| Ready for integration handoff | `Yes` only when the current submission satisfies the conditions below; otherwise `No` with the remaining gate |

Set `Accepted` only when the reviewer is independent, inputs are valid, reviewability is resolved, and required review coverage is complete. The submitted code must satisfy applicable acceptance and design obligations, with current developer verification and no unresolved blocking findings. Required evidence gaps prevent acceptance even if no code defect was found. Use `Changes requested` for actionable blocking findings or unmet submission obligations; use `Not assessed` when missing capability, access, independence, or incomplete analysis prevents a supported conclusion. Report known findings even when the overall conclusion is `Not assessed`.

Set `Ready for integration handoff: Yes` only when code review is accepted, required pre-merge checks pass for the current change, and dependencies meet their merge conditions. Pending, failed, unrun, skipped, or unsupported required checks are not passes. Engineering lead still owns the final merge gate under the [integration contract](../../code-integration/references/integration-contract.md#merge-readiness), including current target and repository protection checks.

Use the [report template](../assets/review-report-template.md) in the existing authoritative evidence location. For a new local record, save `review.md` beside `task.md` under the [artifact layout](../../product-design/references/artifact-layout.md) and link it from that entry. Preserve previous reports through accessible history or immutable references. Keep OCR output and logs available with their run identity; do not overwrite earlier evidence as if it covered a new revision.

The handoff identifies task and design versions, reviewer identity, PR and exact diff, scope and coverage, tool run evidence, findings and dispositions, conclusions, limits, and next function/recipient. Delivery Lead routes accepted work to engineering lead for code-integration, or returns findings to their owners.

## Corrections and re-review

Route findings by the decision they affect:

| Finding | Receiving function and accountable owner |
| --- | --- |
| Implementation defect before merge within task scope | code-development; assigned developer, using the existing branch and PR |
| Local design correction within shared constraints | technical-design in task mode; assigned developer |
| Shared architecture, interface, or feasibility problem | technical-design in overall mode; architect |
| Product behavior, scope, or acceptance ambiguity | product-design; PM |
| Task size, split, assignment, dependencies, or post-merge correction | planner; engineering lead, then the assigned developer |
| Missing or stale verification evidence | Responsible developer, check owner, or environment owner |
| Missing review capability, context, or independent reviewer | Responsible supplier through Delivery Lead |

Delivery Lead preserves finding identity, affected baseline, evidence, impact, requested decision, recipient, and resumption condition. Corrections within approved product and overall-design scope need no new scope approval. Changed product or overall technical baselines return to their existing approval points before dependent work resumes.

Before merge, corrections stay in the original task branch and PR. After merge, engineering lead defines a linked correction task with its own branch and PR. Follow self-tests, independent review, integration, and affected QA; a review report never performs the merge.

On re-review, inspect the current task, PR, base/head, corrections, and previous report. Reassess changed code, its interactions, required checks, and affected earlier findings. Carry forward unchanged coverage only with a stated applicability basis. A new head, changed base, conflict resolution, or revised design invalidates affected prior conclusions. Confirm each fix against the updated revision before closing its finding. If the same issue returns without new evidence or a viable resolution, preserve the blocker and escalate through Delivery Lead rather than repeating an identical request.
