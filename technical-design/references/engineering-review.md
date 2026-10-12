# Engineering review

Review the selected design scope against its product baseline and available system evidence. Task review also uses the exact approved overall design and assigned task. Use the [document contract](document-contract.md) for status, questions, and completion.

## Review coverage

Review these areas in order. Revisit earlier areas when a later finding changes their basis.

| Area | Questions to resolve |
| --- | --- |
| Scope and evidence | Does the design preserve included product rules? Are current facts and relevant technical debt supported? Does reuse reduce unnecessary work? |
| Quality priorities and tradeoffs | Are mandatory constraints distinguished from ranked preferences? Do competing approaches use the same scenarios? Are accepted costs, limits, priority sources, and unresolved conflicts explicit? |
| Design depth | Does each overall detail support a named architecture decision or consumer agreement? Are complete feature internals assigned to task design where possible? Are any architecture risks hidden as local deferrals? |
| Readability and content placement | Can readers find the current decision, structure, blockers, and evidence? Do views replace repeated prose? Are process logs and local sketches kept at their proper scope? |
| Architecture and code quality | Are responsibilities cohesive and interfaces, ownership, and dependency boundaries clear? Can callers use the interface without knowing its internals? |
| Behavior and UML models | Do selected views answer the material design questions, or is omission justified? Do relationships, messages, guards, and outcomes agree across models, contracts, and verification? Are simplified notation and rendering limits explicit? |
| Tests and TDD | Does each rule have meaningful verification? In overall mode, are critical verification obligations defined and local details responsibly deferred? In task mode, can the first implementation step start? Are assertions independent of implementation? Are test replacements and their limits explicit? |
| Failures and operations | Are relevant recovery, security, performance, capacity, availability, backup restoration, rollout, migration, and rollback behaviors defined and verifiable? |
| Decisions and handoff | Does each blocker identify a stage, scope, dependency reason, and owner? Are approval and execution evidence separate? Is readiness assessed by scope without waiving shared risks or blocking independent work? |

Scale coverage to the mode and change. Overall review checks shared decisions and deferred work. Task review checks local choices, affected code, baseline compliance, self-tests, and dependency readiness; reference overall evidence instead of repeating unrelated architecture review. Record inapplicable areas and the reason. Do not create requirements solely to fill the table.

Use the [scenario walkthrough](#walk-through-critical-scenarios) to apply the [model consistency checks](uml-modeling.md#check-the-model-against-the-design). Inspect editable sources and rendered output when available; distinguish semantic review from syntax or rendering checks.

Apply the [overall stopping conditions](document-contract.md#stop-overall-design-at-planning-depth). Check local rule coverage through its responsible module and verification obligation; do not require a new shared contract for each rule. Challenge both premature implementation choices and missing shared decisions. A request for more detail must identify the decision or consumer that needs it now.

For architecture review, trace each new module and material change to a requirement, constraint, or verification need. Apply the [approach-selection criteria](design-methods.md#design-behavior-and-interfaces) to assess whether reuse or fewer boundaries can reduce complexity. For necessary preparatory refactors, verify that the design explains the reason, affected behavior and callers, and regression protection.

Apply the [current-fact method](design-methods.md#establish-current-facts) to check technical debt dispositions and their scope. Apply the module assessment in [behavior and interface design](design-methods.md#design-behavior-and-interfaces) to check change propagation, coupling, and deployment boundaries.

Use the [operational design method](design-methods.md#define-failures-and-operational-behavior) to review relevant security controls, load assumptions, capacity limits, and architecture reassessment conditions. Check availability and restoration requirements against the proposed failure handling and verification. Keep estimates and planned recovery checks distinct from measured capacity and successful restoration evidence.

## Walk through critical scenarios

Select existing scenarios that exercise the highest-priority quality goals, consequential tradeoffs, uncertain assumptions, or significant failure risks. Include representative normal and relevant boundary, failure, recovery, or change scenarios. Explain the selection and material coverage gaps; use a small set appropriate to the scope, not a fixed quota. A routine task can use its acceptance scenario and state why other paths are inapplicable.

For each selected scenario:

1. Fix the scenario reference, design baseline, starting state, operating conditions, trigger, and expected result from the contract or quality goal.
2. Follow the flow step by step. At each step, identify the responsible component, interface call or event, relevant input/output, state change or side effect, and applicable model element. If diagrams are omitted, use the textual flow and record that limit.
3. At relevant branches, trace rejection, concurrency, partial completion, timeout, retry, and recovery. Check guards, invariants, ownership, and the selected tradeoff's limits against the interfaces and model views. For a change scenario, trace the affected components, interfaces, and deployment work instead of inventing a runtime sequence.
4. Compare the resulting behavior with the expected result, including prohibited outcomes and quality acceptance criteria. Follow the [reasoning links](document-contract.md#connect-decisions-to-scenarios-risks-and-verification) to supporting evidence and the check that could detect a violation. Separate consistency established by inspection from claims that still need execution or measurement.
5. Record the path inspected, conclusion and basis, evidence limits, and linked questions or findings. Recheck affected paths after corrections; preserve skipped coverage and unresolved contradictions.

Record a compact walkthrough result in overall Section 9 or the task review record: scenario and baseline, selection reason, conclusion and basis, findings, and evidence limits. Reference the inspected model paths or an existing trace; expand steps only when needed to explain a finding or disputed conclusion. Do not copy a complete flow already shown in the design. Preserve detailed review traces in their authoritative record when needed. A walkthrough establishes only the consistency inspected; it does not establish runtime correctness, measured performance, or approval. Apply the existing stage and scope rules to gaps.

## Check clarity and compression

Apply the contract's [content placement rules](document-contract.md#keep-the-current-design-concise) and the modeling guide's [view selection rules](uml-modeling.md#use-views-to-replace-repeated-prose). Check for:

- The same rule or status restated in contracts, diagrams, tests, review history, and handoff text without a new implication.
- Overall implementation detail with no named consumer or architecture decision needing it now.
- Mixed diagram abstraction levels, essential paths explained only outside the view, or long prose moved into labels and table cells.
- Investigation chronology, resolved review narratives, or one-time delivery commands obscuring current decisions.
- Opaque evidence IDs without a retrieval location, stale summaries, or missing evidence hidden by shortened text.

During the reader walkthrough, locate the architecture boundaries, key tradeoffs, blocking questions, and evidence for the selected scenarios. After compression, compare conditions, exceptions, IDs, ownership, uncertainty, and approval scope with the source. Word count and diagram count are diagnostic only; fewer words cannot compensate for missing meaning.

## Findings and reconciliation

Give each finding a location, defect or unknown, supporting evidence, consequence, and proposed remedy. Classify its blocked stage and scope under the [question rules](document-contract.md#questions-and-assumptions). Distinguish an observed contradiction from a fact that remains unverified.

Record overall findings or their authoritative review references in Section 9, and questions in Section 8. Use the task note's review and readiness record for task findings and questions. Apply the contract's [review and approval records](document-contract.md#review-and-approval-records) to external results and stale summaries. Keep evidence and question states in their authoritative locations; do not require an author run solely to copy a completed review before requesting approval.

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
2. Trace overall product rules through shared contracts or assigned local design and verification obligations; retain accepted exclusions. Trace task acceptance conditions through the local approach and concrete self-tests. Inspect reasoning links for consequential decisions and quality claims.
3. Verify that the selected critical scenarios have walkthrough records, consistent model/interface/outcome checks, and explicit evidence limits. Reuse current review evidence; recheck paths affected by later changes.
4. Inspect question states, dependencies, assumptions, and unresolved review findings. An empty askable queue does not establish completion.
5. Complete the [Technical Writing editing passes](../../technical-writing/references/writing-guide.md#edit-in-separate-passes).
6. Apply the mode-specific status and handoff rules. Check source versions, the task branch when applicable, required review, downstream design obligations, and the next function. Check readiness and approval coverage for each named scope.

Report these as document checks. Do not report them as successful product tests, validated assumptions, or completed implementation. Planning readiness and task implementation readiness are different conclusions. No automated Technical Design Doc validator is supplied with this Skill.
