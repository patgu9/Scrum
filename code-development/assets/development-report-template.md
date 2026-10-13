# Development Delivery: $Task ID and title$

- Record version: v1
- Updated: $Date/time and developer$
- Task: $Task entry path and exact version$
- Inputs: $Product, overall design, and task-design paths/versions; applicable approval and readiness references$
- Claim and workspace: $Confirmed ownership reference, repository, working directory, and task branch$
- Code: $Diff base/head, integration target, and identifiable local changes not included in the PR$
- Implementation verified: $Yes / No with basis under the development contract$
- PR publication: $Published with actual link / Prepared locally / Blocked with cause$

<!-- Adapt to the existing project delivery format. If a separate local file is needed, save development.md beside task.md and link it. Remove prompts and comments. Never fill an execution field with a planned result. -->

## Change and Acceptance

- **Outcome:** $What changed and why, with a concrete observable result.$
- **Exclusions:** $Assigned exclusions and work not included in this delivery.$
- **Design refinements:** $Updated local design references, or None. Shared decisions remain in their owning source.$
- **Scope:** $Affected files/interfaces, behavioral risks, and any required advance review agreement for this scope.$
- **Actual diff:** $Authored additions plus deletions against the declared base/head; generated changes separately; total diff, including binary/non-text changes.$
- **Generated artifacts:** $Generation and validation commands/evidence, or None.$
- **Dependencies:** $Current evidence and remaining review/merge restrictions.$

| Acceptance / Contract | Implementation and Test Reference | Verified Claim | Limits / Downstream Recipient |
| --- | --- | --- | --- |
| $Document-qualified ID$ | $Code and test identity$ | $Actual established result, or not yet verified$ | $Boundary, dependency replacements, or source-defined downstream obligation$ |

## Execution Evidence

- **Defect investigation, when applicable:** $Supported cause or unresolved hypotheses; key experiments and their predicted/observed results; correction and original reproduction before/after. Link existing evidence.$

| Behavior / Test | Phase and Code State | Command / Procedure and Environment | Expected Result | Actual Result and Evidence |
| --- | --- | --- | --- | --- |
| $Test identity and level$ | $Red / Green / Refactor / Baseline / Retrospective / Alternative; revision or working-tree snapshot$ | $Actual command, working directory, relevant runtime/environment$ | $Expected failure reason or success condition$ | $Observed result and output excerpt or durable log; mark unrun explicitly$ |

Record final checks for the delivered code state. Include required checks and relevant regression/integration checks, including those that did not run.

| Check and Obligation | Delivered Code State | Command / Procedure and Environment | Actual Result and Evidence | Gap and Impact |
| --- | --- | --- | --- | --- |
| $Check name; required or risk-based, with source$ | $Revision or identifiable snapshot$ | $Command, working directory, relevant environment$ | $Passed / Failed / Unrun / Skipped / Unavailable; evidence reference$ | $None, or reason and effect on implementation verification$ |

- **Coverage:** $Applicable project threshold, command, scope/result/exclusions; or not measured with reason.$
- **TDD limits:** $Missing history, alternative verification, or None; no claim of test-first execution without evidence.$
- **Self-review:** $Diff examined, issues fixed, and remaining limits; not independent review.$

## Findings and Handoff

| Finding | Affected Scope / Version | Evidence and Disposition | Recipient / Resumption Condition |
| --- | --- | --- | --- |
| $Stable ID or None$ | $Acceptance, design, code, or environment reference$ | $Blocking / Nonblocking; actual evidence and impact$ | $Responsible function and next action$ |

- **Review handoff readiness:** $Yes / No, evidence, and remaining publication or verification work.$
- **Next function and recipient:** $Independent code-review through Project Manager, or the owner of a blocker/feedback decision.$
- **Handoff summary:** $Task and input versions, output references, conclusion, verification limits, unresolved issues, and next recipient.$
