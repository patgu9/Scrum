# Engineering review

Use [Document Review](../../document-review/SKILL.md) with the criteria below in the same review. Required reviewer roles and rechecks still apply. The [document contract](document-contract.md) owns status, approval, readiness, and handoffs. Review the design and applicable supporting records against exact product and code baselines; task review also uses the approved overall design and assigned task.

## Review coverage

Apply these criteria at the selected mode's depth. Reuse overall evidence for task review and record material omissions with reasons. Revisit earlier conclusions when a finding changes their basis.

| Area | Questions to resolve |
| --- | --- |
| Scope and evidence | Are included rules covered? Are facts, relevant technical debt, and reuse decisions supported? |
| Quality and simplicity | Does each new module or material change serve a requirement, constraint, or verification need? Are mandatory limits and ranked preferences distinct? Do alternatives use the same goals and scenarios? Are accepted costs, limits, and conflicts explicit? |
| Design depth | Does each overall detail serve a named consumer or architecture decision? Are local choices responsibly deferred without hiding architecture risks? Can task implementation start without a blocking local choice? |
| Structure and behavior | Are responsibilities, interfaces, ownership, invariants, and dependencies clear? Can callers use interfaces without knowing their internals? Are coupling and deployment boundaries justified? |
| Models and flows | Do names, interfaces, guards, state changes, and outcomes agree across the selected representations and contracts? Does omitted modeling leave a material question unresolved? |
| Verification | Do expected outcomes detect incorrect behavior independently of implementation? Are test boundaries, substitutions, live evidence, and limits appropriate? Are necessary repairs protected against regression? |
| Failures and operations | Do relevant security, consistency, capacity, availability, recovery, and delivery constraints have feasible handling and verification? |
| Readiness and handoff | Does each blocker name a stage, scope, dependency reason, and owner? Are approval, readiness, and executed evidence distinct? Are shared risks preserved without blocking proven independent work? |

Use the [critical scenario walkthrough](#walk-through-critical-scenarios) to test consistency. For models, apply the [model checks](uml-modeling.md#check-the-model-against-the-design), inspecting sources and rendered output when available. Syntax and rendering checks do not replace semantic review.

Apply the contract's [overall stopping conditions](document-contract.md#stop-overall-design-at-planning-depth). A request for more detail must name the decision or consumer that needs it now.

## Walk through critical scenarios

Select a small set of existing scenarios that exercises priority quality goals, consequential decisions, uncertain assumptions, or significant failure risks. Include representative normal and relevant boundary, failure, recovery, or change scenarios. Record the selection basis and material gaps. A routine task can use its acceptance scenario and explain why other paths are inapplicable.

1. Fix the scenario, baseline, starting state, conditions, trigger, and expected result.
2. Trace responsible components, calls or events, inputs/outputs, state changes, and side effects through the selected models or textual flow.
3. At relevant branches, follow rejection, concurrency, partial completion, timeout, retry, and recovery. Check ownership, guards, invariants, and tradeoff limits. For a change scenario, follow affected components, interfaces, and deployment work.
4. Compare the result with required and prohibited outcomes. Follow decision links to supporting evidence and verification; identify claims that still require execution or measurement.
5. Record the inspected path, conclusion, basis, findings, and limits. Recheck affected paths after corrections.

Record walkthroughs in `technical-design-review.md` using the [review template](../assets/review-template.md), or link an authoritative external review. Reference existing scenarios and traces; expand steps only to explain a finding. Keep only the current conclusion and material limits in overall Section 9 or the task readiness summary. A walkthrough establishes only the consistency inspected, not runtime correctness, measured quality, or approval.

## Check clarity and compression

Apply the contract's [content placement rules](document-contract.md#keep-the-current-design-concise). Locate the key decisions, boundaries, blockers, and evidence using the document and its references. Check for repeated rules, overall implementation detail without a current consumer, mixed diagram abstraction levels, process history obscuring conclusions, and evidence references that cannot be retrieved.

After shortening text, compare conditions, exceptions, IDs, ownership, uncertainty, and approval scope with the source. Fewer words or more diagrams do not compensate for missing meaning.

## Findings and reconciliation

Give each finding a location, defect or unknown, evidence, consequence, and proposed remedy. Apply the contract's [question rules](document-contract.md#questions-and-assumptions) for blocked stage/scope and follow-up. Distinguish contradictions from unverified claims.

Keep full findings and correction evidence in the supporting review record under the [review/approval rules](document-contract.md#review-and-approval-records). Link clarification to its Q record; keep current consequences visible in the design. After corrections, inspect affected contracts, models, tests, dependencies, and handoffs. Resolve a finding only when text or evidence addresses it. Keep deferred findings with their impact, owner, evidence need, and dependency. Route baseline changes through the contract's feedback process.

## Review independence and limits

Apply the contract's [task review requirements](document-contract.md#task-handoff-to-code-development). Routine local refinement can use developer self-review; record why architect review is unnecessary. Required architect review remains a blocker until complete. Architect review cannot approve a baseline change. If the author holds the architect role, label that review as self-review.

When independent review is available and delegation is authorized, supply the current design, product baseline, relevant evidence, these criteria, and prior findings. Ask the reviewer to inspect the sources directly. If optional independent review is unavailable, use self-review and state the limit; this does not waive required review.

Limit independent review to three requests, including failed requests. Stop earlier when findings are resolved, progress stops, or new evidence or a user decision is needed. Preserve unresolved findings and continue only independent work. Record version, reviewer, review type, actual coverage, findings, and limits. Reassess affected coverage after substantive edits; a failed or partial review is not a clean result.

## Final document checks

Complete these within the same review:

1. Verify source versions, stable IDs, links between the design and supporting records, required content, and removal of placeholders. For relocated records, verify preserved evidence, states, dependencies, and attempt counts.
2. Trace included rules through decisions and verification; retain accepted exclusions and downstream obligations.
3. Verify scenario walkthrough results, consistent models/flows, and evidence limits.
4. Reconcile questions, assumptions, findings, and dependencies across the artifact set. Missing referenced evidence blocks dependent conclusions; a short or empty main summary does not establish completion.
5. Complete the [Technical Writing passes](../../technical-writing/references/writing-guide.md#edit-in-separate-passes).
6. Apply mode-specific readiness and approval conditions to each named scope, including the task branch and required review where applicable.

Report document checks as such. No automated Technical Design Doc validator is supplied with this Skill. Product tests, implementation, and approval need their own evidence.
