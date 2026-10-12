# Integration contract

This reference owns integration inputs, gate decisions, feedback, and output conditions. The [procedure](integration-procedure.md) owns execution order; [Git Workflow](../../git-workflow/SKILL.md) owns Git mechanics.

## Inputs and responsibility

Start from the task entry and its linked [development evidence](../../code-development/references/development-contract.md#delivery-conditions). For several PRs, inspect each task separately and record their candidate scope together.

| Input | Required evidence and supplier |
| --- | --- |
| Task and baseline | Task path/version, acceptance, exclusions, approved product and overall-design versions, current task design; developer and design owners |
| Submitted change | Existing PR identity, current head, declared review base and comparison convention, integration target, scope report, self-tests, and unresolved findings; developer |
| Independent review | Report identity/version, reviewer who did not author the code, covered base/head, coverage and findings, explicit acceptance, and any required advance reviewer agreement; Code Reviewer |
| Required checks | Applicable repository and technical-design checks, actual results tied to revisions and environment, logs or stable evidence references; check owners |
| Dependencies | Predecessor tasks, required revisions/contracts, merge order, and evidence for each merge prerequisite; task records and engineering lead |
| Integration context | Current target revision, permitted merge method, protected-branch or queue policy, available execution capability, and existing authorization; project context |

Missing, inaccessible, conflicting, or stale inputs block dependent integration. Do not infer approval from artifact presence, independent review from a Skill name, or acceptance from an advance reviewer agreement. A developer's self-review cannot satisfy the independent gate. If engineering lead authored conflict-resolution code, another eligible reviewer must accept it.

## Merge readiness

Merge only when all applicable conditions hold for the current PR and relevant target:

- Task acceptance is satisfied at this stage, including required developer verification. Source-defined downstream QA obligations remain explicit.
- Independent review accepts the submitted change with adequate coverage and no unresolved blocking finding.
- Required pre-merge checks pass with usable, current evidence. Pending, failed, cancelled, unrun, skipped, or unsupported required checks do not establish a pass.
- Dependencies satisfy their merge conditions, and the combined increment keeps the system working.
- Baselines, scope, and target remain valid; affected review and checks have been reassessed after changes.
- The authorized merge mechanism can enforce the assessed state or an equivalent validated queue result without bypassing repository protection.

Reviewability follows the [shared policy](../../planner/references/planning-methods.md#estimate-work-and-review-scope). A low line count cannot waive a gate; an optional preference alone cannot block acceptance. Any unmet acceptance criterion or correctness or safety problem remains blocking. Retain nonblocking findings with IDs and disposition for QA and eventual owner confirmation at ship approval.

Checks have a stage: required pre-merge checks gate the merge; required integration checks on the actual merged candidate gate the normal QA handoff. Derive these obligations from project policy and the technical verification strategy. Do not move an unavailable pre-merge check downstream to permit a merge.

## Output conditions

Report these conclusions separately:

| Field | Values and meaning |
| --- | --- |
| Merge outcome | `Not merged`, `Pending`, `Merged`, `Partially merged`, or `Unverified`; identify actual PR results and revisions |
| Integration verified | `Yes` only when the included scope is confirmed in the identified candidate and all required integration checks pass for that state; otherwise `No` with evidence gaps |
| Ready for QA | `Yes` only when the declared candidate scope is merged, integration is verified, and no blocking issue or invalid input remains; otherwise `No` |

A partial batch can yield a narrower QA candidate only when its scope is explicitly recorded and independently valid. Confirm required dependencies, coherent behavior, and integration evidence for that subset. Keep remaining tasks and blockers visible; do not call the original batch complete.

Include the following in the handoff:

- **Input versions:** Task paths and versions, input versions and approvals, PR references, and reviewed revisions.
- **Merge results:** Target revisions before and after integration, merge results, and the exact candidate identity.
- **Verification evidence:** Integration environment, executed checks, verification scope, and limits.
- **Next handoff:** Retained findings, next function, and accountable recipient.

A branch name alone is not a candidate identity. If a build artifact is used, include its immutable identifier and source revision.

Use the [report template](../assets/integration-report-template.md), adapted to existing project records. For a new local record, use `integration.md` in the existing change directory under the [artifact layout](../../product-design/references/artifact-layout.md) and link it from affected task entries. Preserve earlier candidate evidence in version history or immutable references. Do not overwrite old results as if they tested a newer candidate.

Integration verification does not establish QA acceptance, ship approval, or deployment. An incomplete candidate can be shared for investigation, but its normal QA handoff remains blocked.

## Feedback and resumption

Preserve finding identity, originating function, affected task/candidate and baseline versions, observations, impact, uncertainty, alternatives, requested fact or decision, and accountable recipient. Project Manager routes the feedback:

| Finding | Receiving function and owner |
| --- | --- |
| Code or conflict-resolution defect within approved scope | code-development by developer; updated self-tests and independent Code Reviewer acceptance |
| Missing or stale independent review | code-review by independent Code Reviewer |
| Task split, assignment, dependency order, or post-merge correction | planner by engineering lead |
| Shared interface, architecture, or feasibility conflict | technical-design in overall mode by architect |
| Local approach correction within shared constraints | technical-design in task mode by assigned developer |
| Product scope, behavior, or acceptance ambiguity | product-design by PM |
| Unavailable checks or integration capability | Responsible environment/tool owner, coordinated by Project Manager |

Before merge, corrections retain the task branch and PR. After merge, a defect requires a linked correction task with a new branch and PR, followed by self-tests, independent review, integration, and affected QA. Do not weaken acceptance or edit approved baselines to make integration pass.

Product or overall-design changes need their existing owner approval and reassessment of affected outputs. Independent work can continue only with supported valid inputs. If a return repeats without new evidence or a viable alternative, request the missing decision through Project Manager instead of retrying indefinitely.

On resumption, inspect remote PR/target state and existing candidate reports before any mutation. Keep confirmed merges, failed checks, and pending results distinct. A new candidate needs current evidence; previous QA or ship approval does not automatically cover it. A task or correction record alone cannot close a finding.
