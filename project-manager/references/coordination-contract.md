# Coordination contract

This reference owns coordination inputs, authority, evidence, approval requests, and output content. The [handoff flow](handoff-flow.md) owns forward routing; [feedback and resumption](feedback-and-resumption.md) owns returns and reassessment.

## Inputs and authority

Project Manager owns workflow coordination. PM means Product Manager and owns product discovery and product decisions through `product-design`.

Project Manager initiates cross-role handoffs, tracks blockers, requests owner decisions, and reports delivery state. A role can use several Skills; a Skill invocation does not create another Agent or independent review.

| Input | Required information and supplier |
| --- | --- |
| Goal and scope | Requested outcome, current change directory, constraints, and authorized work; human owner and PM |
| Professional artifacts | Accessible paths, exact versions or immutable revisions, handoff conclusions, and evidence; originating function |
| Task and dependency state | Plan path/version, standalone task paths/versions, readiness by stage, dependencies, existing claims, branches, and PRs; engineering lead and execution owners |
| Role assignments | Actual accountable recipients, availability, and review independence; team context and engineering lead |
| Human decisions | Decision, covered version or release inputs, conditions, time, and source; human owner |
| Findings and feedback | Stable IDs, originating function, affected versions, impact, disposition, attempts, and resolution evidence; originating and resolving functions |
| Delivery context | Candidate identity, environments, access references, applicable checks, operational constraints, and available handoff capability; QA, Ops, and project context |

Require inputs when their stage needs them. PM can start discovery from an incomplete goal. Do not demand a candidate or deployment context before those stages exist. Do not invent missing product facts, approved baselines, recipients, or completed dependencies.

Engineering lead owns task breakdown, developer assignment, and merge. The architect owns shared design; developers own task design and implementation. Independent Code Reviewer owns code review; QA owns test design and execution; Ops owns deployment and service verification. Project Manager routes their conclusions and challenges missing or inconsistent evidence. It cannot substitute its own acceptance conclusion, rewrite their baselines, or waive a blocking finding.

Apply the recipient's functional contract before a dependent handoff. If a named Skill or capability is unavailable, preserve inputs and identify the missing capability and supplier. Do not assume a planned Skill exists or silently implement its professional function inside coordination.

Calling this Skill grants no extra execution permission. Use the applicable authorized workflow for external messages, app changes, claims, worker dispatch, or scheduled follow-up. Record preparation, dispatch, receipt, and execution separately when observed. A prepared handoff is not proof of delivery or a running worker.

## Evidence and input checks

Inspect references rather than relying only on a status label or previous summary. Confirm scope, accessibility, exact version, approval applicability, required checks, and dependencies at the stage they gate. Evidence includes the reviewed or tested version, relevant environment, performed checks, actual results, gaps, and source.

Planned, pending, unrun, failed, skipped, or unavailable required checks do not establish a pass. An optional gap can remain only when the responsible function establishes that it does not undermine acceptance. A review covers its declared diff and context; deployment checks cover the actual deployed candidate and environment.

Missing, stale, conflicting, or inaccessible input produces a blocker with a stable ID, affected work/stage, needed artifact or decision, accountable supplier, and next action. Preserve uncertainty. Continue independent work only with supported validity of its inputs, interfaces, dependencies, and approvals.

Keep unresolved finding IDs and dispositions across handoffs. An unmet acceptance criterion or correctness or safety problem is blocking. Preserve nonblocking findings for owner confirmation at ship approval. A coordinator cannot relabel a blocking finding as optional to meet a schedule.

## Owner approvals

The workflow has three human approval points. Revisions return to the applicable point; routine task refinement or correction within approved product and overall technical baselines adds no human gate.

| Approval | Request identifies | Affected work that waits |
| --- | --- | --- |
| Requirements | Product artifact path and exact version, scope, unresolved decisions, evidence limits, and decision requested | Engineering dependent on that product baseline |
| Overall technical solution | Overall-design path/version, approved product input, shared decisions, feasibility evidence, risks, deferred local decisions, and readiness for planning | Dependent task breakdown and development |
| Ship | QA-accepted immutable candidate, target environment, retained nonblocking issue IDs and their consequences, QA evidence, and deployment/recovery constraints | Release of that candidate to that environment |

Present the actual artifacts and material tradeoffs before requesting a decision. Reuse a recorded approval only when its scope, version, and conditions cover the present action. Capture the owner's actual response and source; silence, artifact status, approval of a previous version, or a request to coordinate is not approval. A conditional response cannot release dependent work until its conditions are met.

Missing or rejected approval keeps the affected handoff blocked. Route revision requests to the decision owner. Product scope, behavior, or acceptance changes require revised product approval. Changes to the overall technical baseline require renewed technical approval. Local design refinement within approved constraints needs no new human approval, but required architect review still applies.

Ship approval covers the candidate, target environment, and retained issue set together. A change to any of those inputs requires renewed ship approval and reassessment of affected evidence. Approval does not prove technical feasibility, QA acceptance, deployment success, or recovery authority beyond the supplied constraints.

## Coordination record

Reuse the existing delivery record and change directory identified by the request or source artifacts. For a new local record, save `delivery.md` beside `product-design.md`, normally under `<project-root>/doc/YYYY-MM-DD-task-slug/`. If no change directory exists, use the start date and a short lowercase English slug separated by hyphens. Inspect ambiguous candidates before asking; for a new change with a name collision, append `-02`, `-03`, or the next unused suffix. Keep the selected path stable and pass it to receiving functions.

Each function defines its own output filenames and paths. Create the coordination record only when there is substantive content; do not create downstream placeholders. This record links professional outputs rather than becoming another task definition, test report, or design baseline.

Use the [delivery record template](../assets/delivery-record-template.md). Keep one current record with an update time and accessible decision history. Preserve earlier evidence and approvals before replacing their references. Record exact input versions; a live path alone cannot preserve an earlier approved version.

Keep current coordination references separate from detailed execution history. Link the originating specialist's result and the human decision instead of copying their full bodies. Specialist conclusions retain their authors; Project Manager records their applicability and next action without substituting its own acceptance. Platform instructions own storage fields, limits, and publication commands.

Maintain only applicable sections:

- Scope, current conclusions, and source artifact/version references.
- Actual recipients, next functions, required inputs, observed handoff state, and next action.
- Task path/version references and dependencies, without duplicating their authoritative bodies.
- Owner approval requests, responses, covered inputs, conditions, and evidence sources.
- Open blockers and findings, affected stages, suppliers, and resolution criteria.
- Feedback attempts, affected-output reassessment, independent work with supporting evidence, and resolution or escalation.
- Candidate, deployment, Ops verification, QA verification, and final delivery conclusion when relevant.

Use concise English unless the user or project requires another language. Mark absent facts as `Unknown`, `Pending`, or `Not applicable` with reasons. Remove template prompts from completed records. Record factual operational updates through the authorized workflow; task scope and assignment changes remain planner decisions. Do not overwrite another role's contradictory record to manufacture agreement.

## Common handoff

Every output, including an approval request, blocker, return, or final summary, identifies the following information directly or through the [handoff reference method](#handoff-by-reference):

1. Change/task scope and exact input versions.
2. Output artifact references and versions, including the coordination record when used.
3. Conclusion, verification evidence, and limits; distinguish this function's progress from downstream acceptance.
4. Unresolved issues with stable IDs, disposition, affected work, and accountable owners.
5. Next function and responsible recipient, requested action, and required inputs or decision.

Report unknown or unavailable recipients explicitly. For final delivery, the next recipient is the human owner; identify any agreed follow-up owner. An honest blocked handoff is a valid output without claiming the forward stage succeeded.

### Handoff by reference

The calling workflow owns required handoff information. Supply that information directly or through accessible, version-specific references to authoritative artifacts and results. A reference satisfies a field only when the recipient can locate the required information and it still applies to this request.

For a first delivery or substantive revision, provide the workflow's complete result. When forwarding an existing result, cite it and state the requested action, recipient, and any changed scope, evidence, blockers, or limits. Do not copy unchanged reports into another result schema. Expand the relevant context when references are unavailable, versions change, or conclusions conflict. Never hide a new blocker behind an old reference.

Keep summaries for consecutive functions distinct, even when one agent performs them in one authorized run. A separate summary does not require another document, comment, or agent run. If nothing changed, follow the caller's reporting rules without repeating an unchanged dispatch.

## Ship completion

Declare ship complete only when all conditions hold for the declared scope:

- QA accepted the identified merged candidate with usable evidence for applicable acceptance criteria and all required checks, without unresolved blocking issues.
- The owner approved that candidate, target environment, and retained nonblocking issues.
- Ops confirmed deployment of that candidate to that environment.
- Ops service verification passed for the actual deployed candidate and environment.
- QA key business verification passed for the same deployed candidate and environment.

Cite both post-deployment reports in the final summary, along with candidate/environment, deployment result, approval evidence, scope, and retained issues. Failed, unrun, missing, stale, or mismatched required verification keeps ship incomplete. A rollback to an earlier version does not complete delivery of the requested candidate.

A partial delivery is reported only for its explicitly bounded scope with applicable approval and evidence. Keep remaining, deferred, cancelled, or blocked scope visible. Never represent exhaustion of attempts, closure of a feedback loop, or deferral as implemented or shipped functionality.
