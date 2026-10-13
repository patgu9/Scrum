# Technical Design: $Title$

- Mode: overall
- Status: DRAFT
- Version: v1
- Date: $YYYY-MM-DD$
- Owner: $Architect responsibility; engineering lead can hold this role$
- Product Design: $Relative source link, exact version/revision, and approval evidence or pending state$
- Code Baseline: $Repository revision and relevant local changes, or Greenfield$
- Status scope: $Included Feature IDs and scope covered by this status; identify differing states$
- Supporting Records: $Relative links to technical-design-questions.md and technical-design-review.md, or authoritative external records; mark each unstarted record as Not started.$

<!-- Follow ../references/document-contract.md. Save beside the product design. Keep the ten sections unless the user supplies another format; omit unused subheadings. Reference authoritative content instead of filling duplicate fields. Remove instructions and placeholders. -->

## 1. Purpose and Scope

$Outcome, included behavior, exclusions and their decision basis, product constraints, and Success Criteria references.$

### Key Quality Goals

| Goal and Source | Mandatory Limit or Preference Priority | Acceptance Scenario | Decision State |
| --- | --- | --- | --- |
| $Material goal$ | $Constraint, or preference order and basis$ | $Scenario reference$ | $Confirmed, proposed, or Q reference$ |

## 2. Current System and Constraints

| Fact or Constraint | Evidence and Limits | Design Impact |
| --- | --- | --- |
| $Verified behavior, relevant pattern or technical debt$ | $Source and revision; distinguish unknowns$ | $Retain, work around, or repair; regression needs$ |

$Link the product glossary and relevant ADRs; define additional terms as needed. Link investigation evidence instead of repeating its chronology.$

## 3. Behavioral Contracts

| Contract | Product References and Consumers | Shared Guarantee | Verification |
| --- | --- | --- | --- |
| C1 | $Rules/examples and consumers$ | $Conditions, invariant, outcome and prohibited behavior; reference detailed interfaces or flows in Section 5$ | $Scenario or obligation$ |

| Local Product References | Responsible Feature or Module | Downstream Design and Verification |
| --- | --- | --- |
| $Grouped rules/examples$ | $Accountable responsibility$ | $Observable outcome to verify; reference Section 5 work$ |

$State compatibility changes and accepted coverage exclusions with decision sources. Do not create shared contracts merely to assign C IDs.$

## 4. Approaches and Decisions

<!-- Repeat for consequential decisions, or link an authoritative ADR. If only one meaningful approach remains, explain why. -->

- **Decision and basis:** $Approach, status/source, goal and scenario references, evidence, and why the approach is sufficient.$
- **Alternatives and tradeoffs:** $Meaningful alternatives; benefit, accepted cost/limit, priority basis, and rejection reasons.$
- **Risks and verification:** $Question/finding and verification references, evidence limits, and residual risk acceptance basis.$
- **Reopen when:** $Changed assumption, requirement, load, or evidence.$

## 5. Technical Solution

### Structure and Key Flows

$Show responsibilities, dependencies, ownership, invariants, critical flows, and relevant trust/execution boundaries. Reuse a sufficient diagram, table, or textual flow. Add only rationale and constraints not already clear from it.$

<!-- For models, apply ../references/uml-modeling.md. Identify purpose, scope, current/proposed baseline, contract/scenario references, notation simplifications, and rendering result or Not run. Retain editable sources. -->

### Shared Interfaces and Dependencies

$Define only the agreement consumers need beyond Section 3: inputs/outputs, validation, failure semantics, ordering, side effects, and compatibility. Name consumers that need exact fields or sequences. Link external capability requirements and supporting designs with versions.$

<!-- Add data relationships and state models when needed to clarify identity, ownership, cardinality, lifecycle, or transaction/concurrency guarantees. Reference existing contracts and flows. -->

### Downstream Task Design

| Feature or Module | Remaining Design and Constraints | Owner | Evidence and Resolution Point |
| --- | --- | --- | --- |
| $Responsibility$ | $Feature internals to resolve within shared decisions$ | $Accountable role; planner assigns developer$ | $Evidence needed before dependent coding/check; independence from unresolved risks$ |

## 6. Failure Modes and Operational Requirements

<!-- Assess relevant areas using ../references/design-methods.md#define-failures-and-operational-behavior. Include applicable rows only; group material omissions with a reason. Reference failures already specified in Section 3 or 5. -->

| Failure or Operational Constraint | Handling, Guarantee, and Limits | Verification |
| --- | --- | --- |
| $Trigger, operating conditions, or requirement source$ | $Detection, retained state, recovery responsibility, and observable result; supported targets or Q references$ | $Scenario or method$ |

<!-- Expand migration/coexistence/rollback for persistent-state changes; backup scope/retention/restoration for durability requirements. Keep local procedures and settings in task design unless architecture depends on them. -->

## 7. Validation and TDD Strategy

| Scenario | Contract or Product Reference | Conditions and Observable Outcome | Verification and Limits | Owner and Required Stage |
| --- | --- | --- | --- | --- |
| T1 | $Rule/contract/quality goal$ | $Operating conditions, trigger, response, acceptance criterion$ | $Boundary, real/replaced dependencies, required live evidence, and Planned or evidence link$ | $Role and resolution point$ |

$Retain architecture-critical scenarios and cross-feature acceptance here. Link existing coverage with its baseline and execution state. Assign local checks through Section 3; record regression needs and verification gaps with owners and Q references.$

### Candidate Behavior Increments

| Increment | Observable Capability and Verification | Prerequisites |
| --- | --- | --- |
| $Candidate for planner, not an assignment$ | $Contract/scenario references$ | $Dependency or None$ |

$Task mode refines concrete TDD steps. Link actual execution evidence from its authoritative record; do not copy execution logs.$

## 8. Premises and Open Questions

$Current premises, material assumptions, and unresolved effects on the design. State affected decisions and blocked stages/scopes with reasons; link the relevant Q or finding records. Use None when no material uncertainty remains.$

<!-- Keep full Q records, investigation/validation detail, and baseline/feedback history in technical-design-questions.md. Mark affected decisions pending beside their content. Apply resolved conclusions to the solution rather than repeating their history here. -->

## 9. Review and Approval

- **Current review:** $Exact version/scope, reviewer and independence, conclusion, and source; or Pending. Link the current review record and identify superseded summaries.$
- **Material limits:** $Incomplete coverage, unresolved findings and their impact on approval/readiness, with record links; or None.$
- **Approval:** $Pending, or approver, exact approved version/scope, date, and source.$

<!-- Put attempts, walkthrough traces, full findings, and correction/recheck evidence in technical-design-review.md or the authoritative external review. Copying that record into the design is not an approval gate. -->

## 10. Handoff to Task Breakdown

| Scope | Status and Approval Reference | Ready for Task Breakdown | Blocker and Next Action |
| --- | --- | --- | --- |
| $Named scope; include remaining product scope$ | $Exact version/scope evidence or Pending$ | $Yes / No under the contract$ | $Q/finding, stage, dependency reason, owner/action; evidence of independence where other scope is blocked$ |

- **Task breakdown:** Pending
- **Next function and recipient:** $Approval, planner, or upstream feedback; accountable recipient and expected result.$
- **Handoff references:** $Baselines, Sections 3–9, and existing supporting records; add only new coordination constraints. Link feedback with its issue, affected contracts, evidence/estimates, impact, alternatives, and requested decision when needed.$
