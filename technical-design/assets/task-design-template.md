# Task Technical Design: $Task ID and title$

- Mode: task
- Status: DRAFT
- Version: v1
- Date: $YYYY-MM-DD$
- Owner: $Assigned developer$
- Task: $Link to task.md beside this file, exact task version, confirmed claim/assignment, and scope$
- Product baseline: $For the default layout: ../../product-design.md, exact version, and approval evidence$
- Overall baseline: $For the default layout: ../../technical-design.md, exact version, and approval evidence; this is the change-level design, not this task file$
- Branch and code baseline: $Existing task branch reference, declared base, current revision and relevant local changes$

<!-- Follow ../references/document-contract.md, including concise design rules. Save beside task.md, normally tasks/<task-key>/technical-design.md. Use a shorter versioned note for simple tasks. Reference shared decisions and existing records; omit unused detail. Remove placeholders and comments. -->

## Scope and Inputs

- **Goal and acceptance:** $One verifiable goal, assigned product rules, shared contracts, and acceptance conditions.$
- **Quality priorities:** $Applicable overall goal/scenario references, mandatory constraints and ranked preferences; flag missing targets or priority conflicts.$
- **Exclusions:** $Task boundaries and unrelated work.$
- **Current evidence:** $Relevant code, tests, conventions, and limits of inspection.$
- **Dependencies:** $Required interfaces or tasks, their state, and effect on design or coding readiness.$
- **Design work assigned here:** $Feature internals and deferred choices from the overall design, shared constraints, required evidence, and resolution points.$

## Implementation Approach

- **Approach and tradeoffs:** $Local choice, alternatives and baseline compliance; priority basis, accepted costs/limits, and conditions to reopen, or no new tradeoff.$
- **Decision basis:** $Goal/contract and scenario references; rationale and evidence limits; risk/finding and self-test links. Pending evidence retains owner, required stage, and dependent conclusion in its record.$
- **Feature internals:** $Required local schemas, algorithms, protocols, or configuration. Use diagrams or decision tables for relationships and behavior; explain only what they do not convey.$
- **Affected code:** $Likely modules or paths and their responsibilities; avoid prescribing every helper.$
- **Models and behavior:** $Embed/link local views with purpose, scope, baseline and contract/test references; show essential guards and failures. Reference shared models; explain omissions and constraints not visible in the views.$
- **Notation and rendering:** $Simplifications and actual rendering result or Not run; omit if no model is needed. Semantic checks belong in the review record.$
- **Review scope:** $One complete goal, affected files/interfaces, required context, behavioral risk, tests, and estimated authored additions plus deletions; generated artifacts separately. State reviewability, split needs, and any required advance reviewer agreement under the supplied policy. Counts alone do not decide.$

## Self-Test and TDD Plan

| Test | Acceptance or Contract | Given and When | Expected Result and Incorrect Behavior Detected | Boundary and Dependencies |
| --- | --- | --- | --- | --- |
| T1 | $Document-qualified reference$ | $Concrete setup and action$ | $Independent expected outcome and failure detected$ | $Test level, real dependencies, replacements, and limits$ |

- **First Red step:** $Test and expected failure from missing behavior; do not invent execution.$
- **Green and Refactor:** $Small behavior steps, relevant checks, and refactor intent; alternative verification and reason if TDD is inapplicable.$
- **Regression and integration:** $Affected checks and overall verification references.$
- **Execution evidence:** $Planned, or actual test identity, command, code state, results, refactor outcome, and limits. Distinguish characterization tests from Red evidence.$

## Review, Questions, and Readiness

| Type | Statement and Impact | Evidence / Validation Status | Follow-up |
| --- | --- | --- | --- |
| $Q ID, assumption, finding, or None$ | $Affected decision, blocked stage and scope or None, and dependency reason$ | $Facts, estimates, missing evidence, and review disposition$ | $Owner/supplier, required evidence, resolution point, and next action$ |

- **Review:** $Reviewed task version, reviewer identity, self-review or independent coverage, and remaining limits; use exact external result references where applicable and identify superseded summaries.$
- **Scenario walkthroughs:** $Scenario and selection reason, expected versus traced outcome, findings, inspected model path/trace reference, and evidence limits. Explain material omissions; expand steps only when needed for a finding.$
- **Architect review:** $Required with result and evidence, Pending, or Not required with the basis for routine local refinement.$
- **Advance reviewer agreement:** $Not needed with basis, Pending, or agreement evidence for unusually large/complex scope. Pending blocks affected implementation; agreement does not replace independent review of the actual diff.$
- **Baseline compliance:** $Within approved decisions, or the exact product/shared decision needing upstream revision.$
- **Ready for implementation:** $Yes / No for the named scope and reasons under the task readiness contract; identify any separately blocked proposal. Use READY only when all conditions hold; this is not new human approval or execution authorization.$
- **Handoff references:** $Task/baselines above, design/self-tests, current review/readiness and remaining issues; reference these records in the delivery message.$
- **Feedback:** $None, or issue identity, affected versions/contracts, constraint, observations versus estimates, alternatives and tradeoffs, requested decision, and affected downstream work.$
- **Next action:** $code-development within existing authorization, required review, or the appropriate upstream function.$
