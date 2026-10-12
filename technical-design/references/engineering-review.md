# Engineering review

Review the selected design scope against its product baseline and available system evidence. Task review also uses the exact approved overall design and assigned task. Use the [document contract](document-contract.md) for status, questions, and completion.

## Review coverage

Review these areas in order. Revisit earlier areas when a later finding changes their basis.

| Area | Questions to resolve |
| --- | --- |
| Scope and evidence | Does the design preserve included product rules? Are current facts and relevant technical debt supported? Does reuse reduce unnecessary work? |
| Design depth | Does each overall detail support a named architecture decision or consumer agreement? Are complete feature internals assigned to task design where possible? Are any architecture risks hidden as local deferrals? |
| Architecture and code quality | Are responsibilities cohesive and interfaces, ownership, and dependency boundaries clear? Can callers use the interface without knowing its internals? |
| Behavior and diagrams | Do important paths have defined outcomes? Do diagrams agree with contracts, state transitions, and failures? |
| Tests and TDD | Does each rule have meaningful verification? In overall mode, are critical verification obligations defined and local details responsibly deferred? In task mode, can the first implementation step start? Are assertions independent of implementation? Are test replacements and their limits explicit? |
| Failures and operations | Are relevant recovery, security, performance, capacity, availability, backup restoration, rollout, migration, and rollback behaviors defined and verifiable? |
| Decisions and handoff | Does each blocker identify a stage, scope, dependency reason, and owner? Are approval and execution evidence separate? Is readiness assessed by scope without waiving shared risks or blocking independent work? |

Scale coverage to the mode and change. Overall review checks shared decisions and deferred work. Task review checks local choices, affected code, baseline compliance, self-tests, and dependency readiness; reference overall evidence instead of repeating unrelated architecture review. Record inapplicable areas and the reason. Do not create requirements solely to fill the table.

Apply the [overall stopping conditions](document-contract.md#stop-overall-design-at-planning-depth). Check local rule coverage through its responsible module and verification obligation; do not require a new shared contract for each rule. Challenge both premature implementation choices and missing shared decisions. A request for more detail must identify the decision or consumer that needs it now.

For architecture review, trace each new module and material change to a requirement, constraint, or verification need. Apply the [approach-selection criteria](design-methods.md#design-behavior-and-interfaces) to assess whether reuse or fewer boundaries can reduce complexity. For necessary preparatory refactors, verify that the design explains the reason, affected behavior and callers, and regression protection.

Apply the [current-fact method](design-methods.md#establish-current-facts) to check technical debt dispositions and their scope. Apply the module assessment in [behavior and interface design](design-methods.md#design-behavior-and-interfaces) to check change propagation, coupling, and deployment boundaries.

Use the [operational design method](design-methods.md#define-failures-and-operational-behavior) to review relevant security controls, load assumptions, capacity limits, and architecture reassessment conditions. Check availability and restoration requirements against the proposed failure handling and verification. Keep estimates and planned recovery checks distinct from measured capacity and successful restoration evidence.

## Findings and reconciliation

Give each finding a location, defect or unknown, supporting evidence, consequence, and proposed remedy. Classify its blocked stage and scope under the [question rules](document-contract.md#questions-and-assumptions). Distinguish an observed contradiction from a fact that remains unverified.

Store overall findings in Section 9 and questions in Section 8. Store task findings and questions in the task note's review and readiness record. Keep evidence and question states in their authoritative locations.

Apply wording and structural corrections within the agreed design. Route baseline changes through the contract's feedback and approval rules; reassess local task changes without inventing a new owner gate. After a correction, inspect affected contracts, diagrams, test cases, dependencies, and handoff content.

Mark a finding resolved only when the revised text or evidence addresses it. Keep deferred findings with their impact, owner, required evidence, and dependency. A reviewer's recommendation does not establish user approval.

## Review independence and limits

Task designs with high-risk or cross-task choices require architect review before affected coding. Routine local refinement can use developer self-review; record its scope and why architect review is unnecessary. A required review that is unavailable remains a readiness blocker, even if self-review is complete. Architect review cannot approve a changed product or overall baseline. Record if the author also holds the architect responsibility; do not describe that as independent review.

When an independent reviewer is available and delegation is authorized, use that reviewer for a fresh assessment. Supply the full current design, product baseline, relevant evidence, this review guide, and prior findings. Ask the reviewer to inspect the materials directly.

If an optional independent reviewer is unavailable, perform self-review and state that limit. This fallback does not waive required architect review or later independent code review. A second pass by the author is still self-review.

Bound repeated independent review to three requests for the design under review. Count failed requests. Stop earlier when no findings remain, progress stops, or new evidence or a user decision is required. Continue independent work while questions remain pending. Keep unresolved findings visible when the limit is reached.

Record the reviewed version, reviewer, review type, completed coverage, findings, and remaining limits. A failed or partial review does not establish a clean result. Recheck affected areas after substantive edits; earlier review applies only where its basis still holds.

## Final document checks

Before presenting the design:

1. Verify source versions, stable IDs, local links, section content, and removal of template placeholders.
2. Trace overall product rules through shared contracts or assigned local design and verification obligations; retain accepted exclusions. Trace task acceptance conditions through the local approach and concrete self-tests.
3. Walk through the important diagrams and compare each outcome with interface definitions and tests.
4. Inspect question states, dependencies, assumptions, and unresolved review findings. An empty askable queue does not establish completion.
5. Complete the [Technical Writing editing passes](../../technical-writing/references/writing-guide.md#edit-in-separate-passes).
6. Apply the mode-specific status and handoff rules. Check source versions, the task branch when applicable, required review, downstream design obligations, and the next function. Check readiness and approval coverage for each named scope.

Report these as document checks. Do not report them as successful product tests, validated assumptions, or completed implementation. Planning readiness and task implementation readiness are different conclusions. No automated Technical Design Doc validator is supplied with this Skill.
