# Task $T1$: $One verifiable outcome$

- Task ID: $Stable ID, unique within the change$
- Version: v1
- Disposition: Active
- Last updated: $Date/time and updating role$
- Plan: $Relative link to ../../task-plan.md and exact source plan version$
- Assignee: $Named available developer and assignment basis, or Unassigned with supplier$
- Ready for assignment/claim: $Yes / No, reason, evidence, and any later-stage restriction$
- Claim: $Pending claim, or confirmed owner, time, and coordination record reference; do not infer ownership from assignment$

<!-- Save new tasks as tasks/<task-key>/task.md under the existing change directory. Follow ../references/plan-contract.md. Keep one entry point per task. Use exact source versions and real relative links. Replace prompts and remove comments; do not create links to artifacts that do not yet exist. -->

## Goal and Boundaries

- **Goal:** $One complete, observable outcome.$
- **Required changes:** $Behavior and likely code/modules; local implementation design follows claim.$
- **Exclusions:** $Unrelated work and explicit limits.$
- **Lineage:** $None, or links to original task/defect, affected candidate, replacement tasks, and distributed acceptance scope.$

## Required Inputs

| Input | Reference and Exact Version | Approval / Validity Evidence |
| --- | --- | --- |
| Product | $Relative link to ../../product-design.md and version$ | $Owner approval evidence for that version, or explicit blocker$ |
| Overall technical design | $Relative link to ../../technical-design.md and version$ | $Approval and relevant planning readiness$ |
| Code and project context | $Repository, inspected code revision, relevant local changes, instructions/test conventions$ | $Observed state, access needs, and inspection limits$ |
| Review policy | $Applicable reference and version or stable source$ | $Applicable policy and unresolved conflicts$ |

- **Assigned requirements and contracts:** $Document-qualified rule/example/contract IDs; link decisions without reproducing competing text.$
- **Source changes:** $Required reassessment if pinned inputs change; unrelated plan-index updates do not silently retarget this task.$

## Acceptance and Planned Verification

| Acceptance Condition | Source | Expected Outcome | Planned Verification / Responsible Recipient |
| --- | --- | --- | --- |
| $Observable condition$ | $Document-qualified reference$ | $Concrete result including relevant boundaries/failures$ | $Self-test/regression obligation or shared integration check and recipient; execution remains pending$ |

## Dependencies and Deferred Decisions

| Dependency / Input | Required Version or Condition | Current Evidence | Gated Stage | Supplier |
| --- | --- | --- | --- | --- |
| $Relative task link, e.g. ../t1/task.md, external input, or None$ | $Version/outcome needed$ | $Actual evidence or missing fact$ | $Claim / Design / Coding / Review / Merge$ | $Accountable recipient$ |

- **Deferred local decisions:** $Source, constraints, required evidence, developer responsible, and resolution point before affected coding; or None.$
- **Independent work:** $What can proceed while a dependency waits, with the supporting basis; do not assume independence.$

## Git Baseline and Review Scope

- **Git baseline:** $Repository, declared base ref/revision, integration target, stack relationship if any, and claim-time rechecks.$
- **Effort:** $Task design, implementation, and verification effort with basis and uncertainty.$
- **Review scope:** $Affected files/interfaces, behavior risks, context/expertise, estimated authored additions plus deletions, generated changes separately, and generation/validation needs.$
- **Reviewability disposition:** $Suitable / Split / Clarify / Advance review agreement needed, with material reasons; no default numerical gate.$
- **Advance reviewer agreement:** $Not needed with basis, Pending, or evidence for the exact large/complex scope. Pending blocks affected implementation; agreement does not accept code.$

## Execution References and Next Handoff

- **Observed stage:** $Not started, or current stage with supporting evidence; this is not a platform status mapping.$
- **Branch and PR:** $Not created, or actual existing links, base/head revisions, and inspection evidence. Reuse existing work on resumption.$
- **Task technical design:** $Not produced, or relative link to the existing technical-design.md beside this file and its version/readiness. This local design is distinct from ../../technical-design.md.$
- **Verification and review evidence:** $Not run, or actual versioned result references and limits. Do not close findings because a plan exists.$
- **Blockers and questions:** $Stable IDs, affected scope/stage, missing evidence/decision, supplier, and resumption conditions; or None.$
- **Next action and recipient:** $Confirm claim through the authorized workflow; then establish branch and produce task design. For resumed, blocked, superseded, or completed work, record its actual next action and recipient.$
- **Handoff summary:** $Task path/version, input versions, output references, conclusion/evidence limits, unresolved issues, and next function/recipient.$

## Revision and Ownership Record

| Task Version / Recorded Time | Change and Basis | Impact / Prior Evidence |
| --- | --- | --- |
| v1 / $time$ | $Initial task definition; later scope changes increment the task version, operational updates record time/source$ | $Prior revision or ownership evidence, affected readiness, updated index/dependent references$ |
