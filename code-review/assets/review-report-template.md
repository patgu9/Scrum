# Code review: $Task ID and title$

<!-- Reuse the existing evidence record. For a new local report, save review.md beside task.md and link it from the task. Replace prompts and remove this comment. Preserve prior revisions and raw tool evidence. For advance agreement, record its basis and mark code review Not assessed; do not imply an OCR run. -->

- Report identity/version and time: $Stable reference and recorded time$
- Review purpose: $Initial review / Re-review / Advance agreement / Advisory review$
- Reviewer and independence: $Identity, reviewed-code authors, and independence basis$
- Inputs: $Task path/version; approved product and overall versions; current task design; development evidence$
- PR and repository: $References, or missing input$
- Comparison: $Declared base tip, actual comparison base, head, convention, integration target, and predecessor if any$

## Scope and Coverage

- Reviewability: $Disposition, cohesive goal, context, complexity, risks, and basis$
- Advance agreement: $Not required / Agreed / Changes requested / Insufficient context; proposal version, scope, split alternatives, responsibilities, and validation strategy$
- Actual scope: $Authored additions/deletions including Agent work; generated changes separately; binary artifacts and total diff$
- OCR evidence: $Run/session identity, command and effective options/rules, exit outcome, raw output and stderr references; or Not run with reason$

| Changed Area / Acceptance or Contract | Review Method and Evidence | Coverage / Gap |
| --- | --- | --- |
| $Files, interactions, behavior, or artifact$ | $OCR result plus source inspection or supplemental review$ | $Reviewed / Excluded / Failed / Not reviewed; reason and effect$

## Verification Evidence

| Required Check / Source | Revision and Environment | Actual Result and Evidence |
| --- | --- | --- |
| $Developer or pre-merge obligation$ | $Exact revision and environment$ | $Passed / Failed / Pending / Not run / Unsupported; evidence or responsible supplier$

- Dependency readiness: $Required merge conditions and current evidence$
- Reviewer probes: $Actual checks and results, or None; distinguish them from supplied developer evidence$
- Changes since prior review: $Previous report and revisions, changed inputs, reassessed scope, and basis for any carried-forward evidence; or Not applicable$

## Findings and Dispositions

| Finding ID | Revision / Location | Severity / Category | Blocking? | Evidence, Trigger, and Impact | Disposition / Confirmation | Owner / Next Action |
| --- | --- | --- | --- | --- | --- | --- |
| $Stable ID or None$ | $Verified path/line, symbol, or artifact location$ | $OCR source label or reviewer assessment$ | $Yes / No with basis$ | $Observation, relevant contract, and uncertainty$ | $Open / Resolved / Retained / Dismissed; reason and current evidence$ | $Function, accountable recipient, and requested correction or decision$

- Tool finding reconciliation: $False-positive or duplicate dispositions and raw references; or None$

## Conclusion and Handoff

- Review coverage: $Complete / Partial / Not started; scope and basis$
- Code review acceptance: $Accepted / Changes requested / Not assessed; exact revisions and reasons$
- Ready for integration handoff: $Yes / No; remaining gates$
- Verification limits: $Unreviewed scope, unavailable evidence, stale inputs, and retained nonblocking issues$
- Output references: $Report, raw OCR result/logs, verification evidence, prior review, and finding history$
- Next function and recipient: $Engineering lead for code-integration, or correction/decision owner, through Delivery Lead$
- Resumption or closure condition: $Required updated evidence or decision; creating a task does not close a finding$
- Handoff summary: $Task/input versions, outputs, conclusion/evidence, unresolved issues, and next action. Review acceptance does not establish merge, QA acceptance, or ship approval.$
