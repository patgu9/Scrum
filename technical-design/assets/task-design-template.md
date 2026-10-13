# Task Technical Design: $Task ID and title$

- Mode: task
- Status: DRAFT
- Version: v1
- Date: $YYYY-MM-DD$
- Owner: $Assigned developer$
- Task: $task.md link, exact version, confirmed claim, and scope$
- Product baseline: $../../product-design.md in the default layout; exact version and approval evidence$
- Overall baseline: $../../technical-design.md in the default layout; exact version and approval evidence$
- Branch and code baseline: $Existing branch, declared base, revision, and relevant local changes$
- Supporting Records: $Relative links to this task's technical-design-questions.md and technical-design-review.md, or authoritative external records; mark each unstarted record as Not started.$

<!-- Follow ../references/document-contract.md. Save beside task.md. A short note can carry the same required information. Expand only applicable fields; reference approved decisions and authoritative records. Remove instructions and placeholders. -->

## Scope and Inputs

$One verifiable goal, acceptance/rule/contract references, exclusions, applicable quality priorities, current code/test evidence, and inspection limits. Identify dependencies and assigned deferred design, with constraints, evidence needs, and resolution points.$

## Implementation Approach

$Local approach and affected code, baseline compliance, relevant error handling, and acceptance/self-test links. Explain why the approach is sufficient; reference approved tradeoffs. For consequential new choices, include alternatives, evidence, accepted costs/limits, risks, and conditions to reopen.$

<!-- Expand only where needed to begin implementation: local interfaces, schemas, algorithms, protocols, configuration, state changes, and recovery. Use models when existing text/tables leave material ambiguity. For models, retain sources, scope/baseline, contract/test references, notation limits, and rendering result. -->

- **Review scope:** $One complete goal and scope assessment under the supplied reviewability policy; reference an existing assessment and record any change.$

## Self-Test and TDD Plan

| Test | Acceptance or Contract | Given and When | Expected Result and Incorrect Behavior Detected | Boundary and Dependencies |
| --- | --- | --- | --- | --- |
| T1 | $Document-qualified reference$ | $Concrete setup and action$ | $Independent expected outcome and failure detected$ | $Level, real/replaced dependencies, limits, and required live check$ |

- **First Red step:** $First failing behavior test, intended failure reason, and prerequisites.$
- **Behavior steps:** $Small Green/Refactor increments and relevant regression/integration checks. Explain alternative verification if TDD is inapplicable.$
- **Evidence:** $Planned, or link to authoritative execution results with design implications and limits. Keep characterization evidence distinct from Red; do not copy the execution log.$

## Review, Questions, and Readiness

- **Current assumptions and open items:** $Material premises, uncertainty, and effects on the approach or readiness. Link Q/finding records and state blocked stages/scopes with reasons; or None.$
- **Current review:** $Exact version/scope, reviewer and independence, conclusion and source, material coverage limits, and pending findings. Include required architect review evidence, or the basis for routine self-review.$
- **Review arrangements:** $When advance reviewer agreement is required, link evidence or record Pending with its affected implementation scope. Otherwise retain the basis in Review scope.$
- **Ready for implementation:** $Yes / No for named scope and baselines under the contract. Identify separately blocked proposals and evidence that ready work is independent. READY grants no new approval or execution authority.$
- **Next action and recipient:** $code-development within existing authorization, required review, or upstream function. Reference task/baselines, design/tests, supporting records, and current readiness. Link feedback with its requested decision when needed.$

<!-- Store full questions, validation, and baseline/feedback history in this task's technical-design-questions.md. Store attempts, walkthroughs, findings, and rechecks in its technical-design-review.md or authoritative external records. Keep current consequences visible above and beside affected design content. -->
