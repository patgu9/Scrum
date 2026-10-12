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

<!-- Follow ../references/document-contract.md. Store new task designs beside their task.md, normally tasks/<task-key>/technical-design.md. A simple task can use a short versioned file containing the same required information. Link shared decisions instead of copying them. Remove placeholders and comments from completed output. -->

## Scope and Inputs

- **Goal and acceptance:** $One verifiable goal, assigned product rules, shared contracts, and acceptance conditions.$
- **Exclusions:** $Task boundaries and unrelated work.$
- **Current evidence:** $Relevant code, tests, conventions, and limits of inspection.$
- **Dependencies:** $Required interfaces or tasks, their state, and effect on design or coding readiness.$
- **Deferred decisions assigned here:** $Overall-design references, permitted choices, constraints, and required evidence.$

## Implementation Approach

- **Approach and rationale:** $Local design, meaningful alternatives where needed, and consistency with the overall baseline.$
- **Affected code:** $Likely modules or paths and their responsibilities; avoid prescribing every helper.$
- **Behavior and errors:** $Local flow, failure paths, concurrency or recovery where relevant, and shared contract references.$
- **Diagram:** $Only if it clarifies a material interaction, or a reason it is unnecessary.$
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
| $Q ID, assumption, finding, or None$ | $Affected decision; Blocks approval, task breakdown, or implementation as applicable, with reason$ | $Facts, estimates, missing evidence, and review disposition$ | $Owner, required evidence, and work blocked$ |

- **Review:** $Reviewed task version, reviewer identity, self-review or independent coverage, and remaining limits.$
- **Architect review:** $Required with result and evidence, Pending, or Not required with the basis for routine local refinement.$
- **Advance reviewer agreement:** $Not needed with basis, Pending, or agreement evidence for unusually large/complex scope. Pending blocks affected implementation; agreement does not replace independent review of the actual diff.$
- **Baseline compliance:** $Within approved decisions, or the exact product/shared decision needing upstream revision.$
- **Ready for implementation:** $Yes / No for the named scope and reasons under the task readiness contract; identify any separately blocked proposal. Use READY only when all conditions hold; this is not new human approval or execution authorization.$
- **Handoff summary:** $Task and input versions, output references, conclusion and evidence limits, unresolved issues, next function and recipient.$
- **Feedback:** $None, or issue identity, affected versions/contracts, constraint, observations versus estimates, alternatives and tradeoffs, requested decision, and affected downstream work.$
- **Next action:** $code-development within existing authorization, required review, or the appropriate upstream function.$
