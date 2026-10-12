# Technical Design: $Title$

- Mode: overall
- Status: DRAFT
- Version: v1
- Date: $YYYY-MM-DD$
- Owner: $Architect responsibility; engineering lead can hold this role$
- Product Design: $Relative link to product-design.md, exact version or revision, and source approval state; or confirmed requirement sources$
- Code Baseline: $Repository revision and relevant local changes, or Greenfield$
- Related Features: $Source Feature IDs$
- Status scope: $Scope covered by the status above; identify different states for other scopes if needed$

<!-- Follow ../references/document-contract.md, including concise design and decision-depth rules. Keep the ten main sections; remove unused subheadings. A section may reference authoritative content elsewhere. Group inapplicable areas with a brief reason. Remove placeholders and comments. -->

<!-- Apply the contract's decision-depth and stopping conditions. Define architecture and shared agreements here; assign feature internals to task design. Explain any detail needed early by its effect on an architecture decision or consumer. -->

<!-- Save as technical-design.md in the task directory defined by the shared task artifact layout at ../../product-design/references/artifact-layout.md. -->

## 1. Purpose and Scope

$State the change and the architecture and shared decisions needed for coherent task planning.$

- **Included:** $Feature IDs and the behavior covered by this design.$
- **Excluded:** $Excluded or deferred behavior and the decision basis.$
- **Product constraints:** $Source rules, Success Criteria, and agreed limits.$
- **Supporting designs:** $Links and versions, or None.$

### Key Quality Goals

| Goal and Source | Constraint or Preference; Priority and Basis | Acceptance Scenario | Decision State |
| --- | --- | --- | --- |
| $Goal and authoritative requirement reference$ | $Mandatory limit, or relative preference order and reason$ | $Existing example, C/T, or Section 6 reference with conditions, response, and measurable/observable criterion$ | $Confirmed source or proposed/unknown with Q reference$ |

<!-- Include only goals material to this design. Keep detailed requirements and scenarios in their authoritative sections; do not invent targets or priorities. -->

## 2. Current System and Constraints

| Area | Current Fact or Constraint | Source | Design Impact |
| --- | --- | --- | --- |
| $Relevant area$ | $Verified behavior or stated constraint; qualify unknowns$ | $File and revision, observation, or decision source$ | $Effect on this design$ |

- **Terminology:** $Link the product Design Doc's Glossary. Define additional technical terms needed by the reader.$
- **Existing architecture decisions:** $Relevant ADRs or None.$
- **Relevant patterns and technical debt:** $Evidence, design impact, and decision to retain, work around, or repair; or None.$
- **Evidence limits:** $Current conclusion and material uncertainty; link versioned investigation records rather than repeating probe chronology.$

## 3. Behavioral Contracts

| Contract | Product Rules and Examples | Required Behavior | Verification |
| --- | --- | --- | --- |
| C1 | $Source rule and example IDs$ | $Shared guarantee, consumers, conditions, invariant, and prohibited outcome; reference product behavior rather than copying it$ | $T IDs or verification obligation$ |

<!-- Use C IDs for shared contracts. Account for local rules below without repeating the full product behavior or inventing shared contracts. -->

| Local Product Rules and Examples | Responsible Feature or Module | Downstream Design and Verification Obligation |
| --- | --- | --- |
| $Rule/example IDs; group related rules$ | $Owner of the local behavior$ | $Design work and observable result to verify; link Section 5 obligations$ |

- **Compatibility:** $Behavior preserved and intentional changes, with source references.$
- **Coverage exceptions:** $Accepted exclusions or pending questions, with reasons and follow-up.$

## 4. Approaches and Decisions

| Approach | How It Works | Benefits | Costs and Risks |
| --- | --- | --- | --- |
| $Approach$ | $Core mechanism$ | $Effect on priority goals$ | $Costs, limits, and rejection reason where applicable$ |

- **Decision and status:** $Selected approach or ADR link; decision authority/source, or Pending with Q reference.$
- **Basis and tradeoff:** $Goal/contract and scenario references; why this approach fits, precedence of competing goals, accepted cost and limit, and evidence basis. Explain if no meaningful alternative remains.$
- **Risks and verification:** $Risk/assumption/finding and T references, evidence limits, and residual risk acceptance basis. Pending evidence retains its owner, required stage, and affected conclusion in that record.$
- **Reopen when:** $Changed assumption, requirement, or evidence that would change this decision.$

<!-- Repeat the decision fields only for consequential decisions, or link their authoritative ADRs. Keep reasoning links beside each conclusion under the document contract; reuse existing record IDs. -->

## 5. Technical Solution

### Modules and Responsibilities

$Show responsibilities, dependencies, and relevant execution/trust boundaries in a structure diagram. For a simple change, use a compact table or explanation. Distinguish components, participants, and stored data.$

- **Ownership and boundary rationale:** $Only ownership, cohesion, change propagation, or accepted coupling not clear from the view; link decisions rather than restating them.$

### UML Models and Key Flows

<!-- Select views under ../references/uml-modeling.md. Keep shared decisions here; assign local modeling to task design. -->

$Embed or link the selected flow, interaction, or state views; use decision tables for condition/outcome combinations. Include essential entry paths, guards, and failures. Caption each view with purpose, scope, current/proposed baseline, and rule/C/T references. Explain only constraints and exceptions the view cannot convey; state an omission reason where applicable.$

- **Notation and rendering:** $Tool/notation, simplifications, and actual rendering result or Not run. Semantic review belongs in Section 9.$

### Cross-Task Interface Contracts

<!-- Repeat for interfaces that require agreement across tasks or with existing consumers. Leave complete command sets, schemas, and provider protocols to task design unless that agreement depends on them. -->

- **Interface and consumers:** $Operation, callers, and C references; state the agreement not already defined there.$
- **Inputs, outputs, and failures:** $Required semantics, validation, and caller-visible results; exact fields only where consumers depend on them.$
- **Constraints:** $Ordering, side effects, compatibility, and invariant references; do not repeat the linked contract or diagram.$

### Data, State, and Dependencies

$Use a relationship model for identities, revisions, ownership, and reference cardinalities when material. Reference lifecycle and interaction views above; keep independent status dimensions separate.$

- **Additional invariants:** $Integrity, retention, transaction, concurrency, or retry guarantees not expressed in the views; link authoritative contracts.$
- **External dependencies:** $Required capabilities, access boundaries, and contract references.$

### Downstream Task Design

| Feature or Module | Design Work and Constraints | Owner | Evidence Required and Resolve Before |
| --- | --- | --- | --- |
| $Feature/module responsibility$ | $Internal flows, schemas, algorithms, protocols, or tests to design within shared constraints; explain independence from unresolved architecture risks$ | $Accountable role; planner assigns the developer$ | $Evidence obligation and the affected coding or validation boundary$ |

## 6. Failure Modes and Operational Requirements

<!-- Record shared guarantees and acceptance. Refer to failure paths already modeled; explain only additional handling here. Review relevant operational areas under design-methods.md, include applicable rows, and group inapplicable areas with a reason. Task design owns local procedures and configuration. -->

| Failure | Trigger or Path | Handling and Recovery | Observable Result | Verification |
| --- | --- | --- | --- | --- |
| $Failure$ | $Condition and affected C IDs$ | $Detection, retained state, recovery, and relevant limits$ | $What the user or caller observes$ | $T IDs or procedure$ |

| Area | Requirement or Decision | Verification |
| --- | --- | --- |
| $Applicable operational area$ | $Shared requirement or decision reference; supported target/conditions, responsibility, and unknowns$ | $T reference or verification method$ |

<!-- Consider security/access, performance/resources, capacity, availability, observability, distribution, rollout, migration, rollback, and backup/restoration. Omitted template rows do not waive this assessment. -->

## 7. Validation and TDD Strategy

### Test Boundaries

| Boundary | Behavior Verified | Real Dependencies and Test Replacements | Limits |
| --- | --- | --- | --- |
| $Public interface or agreed seam$ | $C IDs and behavior$ | $Real components and replacements$ | $What this test boundary cannot establish; follow-up verification$ |

### Critical Architecture Scenarios and Integration Acceptance

| Scenario | Contract or Product Reference | Condition and Observable Outcome | Verification Boundary and Evidence | Responsible Role and Required Stage |
| --- | --- | --- | --- | --- |
| T1 | $C, source, or quality-goal references$ | $Affected system, operating conditions, trigger, required response, and measurable/observable acceptance criterion$ | $Method, real dependency or substitution, actual evidence or Planned, and limits$ | $Owner and when the evidence is needed$ |

<!-- Retain architecture-critical and cross-feature scenarios here. Section 3 assigns local verification obligations; task designs own detailed cases and fixtures. Preserve existing T IDs and relocation links when moving local cases. -->

- **Existing coverage:** $Current tests, baseline, and execution status.$
- **Regression and integration:** $Behavior to protect and checks across Features.$
- **Verification gaps:** $Deferred or nonautomated checks, reasons, owners, and Q references.$

### Candidate Behavior Increments

| Increment | Observable Capability | Verification Obligation | Prerequisites |
| --- | --- | --- | --- |
| $Small behavior slice$ | $Contract and acceptance outcome$ | $Critical T ID or behavior obligation; task mode refines the first Red step$ | $Real dependency or None$ |

- **Execution and evidence:** $Task mode plans Red → Green → Refactor one behavior at a time. Reference the downstream evidence contract; link actual results and limits when available, otherwise Planned. Explain any TDD exception.$

## 8. Premises and Open Questions

| Type | Statement and Impact | Evidence / Validation Status | Follow-up |
| --- | --- | --- | --- |
| $Accepted premise or Assumption to validate$ | $Statement, affected decision/IDs, blocked stage and scope or None, and dependency reason$ | $Basis and source. For an assumption: observation, collection method, and disconfirming result$ | $Owner/supplier, required evidence, resolution point, and decisions to reopen$ |
| $Q ID / Fact to investigate or User decision / State$ | $Question, affected decision/IDs, blocked stage and scope or None, and dependency reason$ | $Answer and source, Pending, or Unknown. For a user decision: options, tradeoffs, and recommendation. Retain prior answers if reopened$ | $Next action, evidence needed, supplier, and resolution point$ |

<!-- Link existing product questions to their authoritative records. Preserve resolved records. Use None only where no uncertainty or follow-up remains. -->

## 9. Review and Approval

- **Current review:** $Exact version/scope, reviewer and independence, conclusion, date and openable source; or Pending. Identify superseded summaries through record links.$
- **Coverage and limits:** $Reviewed areas, skipped coverage and reasons, material evidence limits, and independent review request count if applicable.$

<!-- Summarize the current assessment. Keep review rounds and full traces in their authoritative records; use references instead of duplicating their findings below. -->

| Scenario and Selection Reason | Conclusion and Findings | Basis and Limits |
| --- | --- | --- |
| $Existing scenario and priority/tradeoff/risk basis; baseline above$ | $Expected versus traced outcome and Q/finding references$ | $Inspected model path or openable trace, contract/test references, basis, and remaining uncertainty; expand steps only to explain a finding$ |

| Finding and Location | Evidence and Consequence | Remedy or Question | Disposition, Blocked Stage and Scope |
| --- | --- | --- | --- |
| $Finding or None$ | $Basis and effect$ | $Correction or Q ID$ | $Open, resolved with basis, or deferred with owner; stage/scope affected and dependency reason, or None$ |

- **Recheck:** $Affected paths rechecked after corrections and result; link prior dispositions.$
- **Approval:** $Pending, or approver, exact approved version and scope, date, and source; distinguish any remaining unapproved scope.$

## 10. Handoff to Task Breakdown

- **Handoff references:** $Exact design/product baselines above; Sections 3–5 for contracts, ownership and downstream design; Section 7 for dependencies and integration acceptance; Sections 8–9 for remaining evidence and review.$

<!-- Add only coordination constraints not already recorded. Use a dependency diagram where helpful. Keep dispatch instructions, Git steps, and reply metadata in the delivery record. -->

| Scope | Status and Approval Reference | Ready for Task Breakdown | Blocker, Dependency Reason, and Next Action |
| --- | --- | --- | --- |
| $Named scope; one row if readiness is uniform$ | $Exact version/scope approval, or Pending$ | $Yes / No under the contract$ | $Q/finding IDs, affected stage, owner and action; or None. State evidence of independence where other scope is blocked.$ |

<!-- Include remaining product scope. Do not use an overall No to hide supported independent scope, or a subset's approval to imply approval of the whole change. -->

- **Task breakdown:** Pending
- **Next function and recipient:** $Owner approval, planner handoff, or upstream feedback; accountable recipient and expected result.$
- **Feedback:** $Authoritative issue reference with constraint, evidence/estimates, impact, alternatives, and requested decision; or None.$
