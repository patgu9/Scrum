# Technical Design: $Title$

- Mode: overall
- Status: DRAFT
- Version: v1
- Date: $YYYY-MM-DD$
- Owner: $Architect responsibility; engineering lead can hold this role$
- Product Design: $Relative link to product-design.md, exact version or revision, and source approval state; or confirmed requirement sources$
- Code Baseline: $Repository revision and relevant local changes, or Greenfield$
- Related Features: $Source Feature IDs$

<!-- Follow the document contract at ../references/document-contract.md. Replace placeholders and remove instructional comments. Use for overall mode. Keep the ten main sections. Give a short reason for inapplicable areas. -->

<!-- Save as technical-design.md in the task directory defined by the shared task artifact layout at ../../product-design/references/artifact-layout.md. -->

## 1. Purpose and Scope

$State the change and the architecture and shared decisions needed for coherent task planning.$

- **Included:** $Feature IDs and the behavior covered by this design.$
- **Excluded:** $Excluded or deferred behavior and the decision basis.$
- **Product constraints:** $Source rules, Success Criteria, and agreed limits.$
- **Supporting designs:** $Links and versions, or None.$

## 2. Current System and Constraints

| Area | Current Fact or Constraint | Source | Design Impact |
| --- | --- | --- | --- |
| $Relevant area$ | $Verified behavior or stated constraint; qualify unknowns$ | $File and revision, observation, or decision source$ | $Effect on this design$ |

- **Terminology:** $Link the product Design Doc's Glossary. Define additional technical terms needed by the reader.$
- **Existing architecture decisions:** $Relevant ADRs or None.$
- **Relevant patterns and technical debt:** $Evidence, design impact, and decision to retain, work around, or repair; or None.$
- **Evidence limits:** $What was inspected or executed, and what remains unverified.$

## 3. Behavioral Contracts

| Contract | Product Rules and Examples | Required Behavior | Verification |
| --- | --- | --- | --- |
| C1 | $Source rule and example IDs$ | $Condition, actor, observable result, invariant, and relevant prohibited outcome$ | $T IDs or explicit verification method$ |

- **Compatibility:** $Behavior preserved and intentional changes, with source references.$
- **Coverage exceptions:** $Accepted exclusions or pending questions, with reasons and follow-up.$

## 4. Approaches and Decisions

| Approach | How It Works | Benefits | Costs and Risks |
| --- | --- | --- | --- |
| $Approach$ | $Responsibilities, interface, and dependencies$ | $Benefits under the actual constraints$ | $Tradeoffs, uncertainty, and change cost$ |

- **Selected approach:** $Choice and status, or Pending with a Q ID.$
- **Decision basis:** $Reason, evidence, and user answer or applicable authorization.$
- **Rejected alternatives:** $Reasons, or why no meaningful alternative remains.$
- **Related decisions:** $Authoritative ADR or supporting-design links, if applicable.$

## 5. Technical Solution

### Modules and Responsibilities

| Module | Responsibility | Public Interface | Dependencies |
| --- | --- | --- | --- |
| $Module$ | $Behavior and data owned$ | $Caller-facing operations$ | $Required modules or services$ |

- **Module assessment:** $Cohesion, change propagation, coupling, and any justified deployment boundaries; explain accepted tradeoffs.$

### Key Flows and Diagrams

$Insert relevant architecture, flow, sequence, or state diagrams. Explain the important paths beside each diagram. Link paths to C and T IDs. State why diagrams are unnecessary for a simple change.$

### Interface Contracts

<!-- Repeat for each important interface. Keep private implementation detail open unless it affects a contract. -->

- **Interface:** $Operation and related C IDs.$
- **Inputs and outputs:** $Types or schemas, validation, and observable results.$
- **Errors:** $Caller-visible failures and their conditions.$
- **Invariants and ordering:** $Required state, sequence, and side effects.$
- **Compatibility:** $Existing callers, versions, and intentional changes.$

### Data, State, and Dependencies

- **Data ownership:** $Schema, integrity, storage, retention, and transaction boundaries where relevant.$
- **State transitions:** $Allowed and rejected transitions; refer to the state diagram when applicable.$
- **Concurrency and asynchronous work:** $Idempotency, ordering, retries, cancellation, and limits with units where relevant.$
- **External dependencies:** $Required capabilities, access boundaries, and dependency contracts.$

### Deferred Task Decisions

| Decision | Scope and Constraints | Owner | Evidence Required and Resolve Before |
| --- | --- | --- | --- |
| $Local choice or None$ | $Why it can wait without undermining feasibility or shared contracts$ | $Accountable role; planner assigns the developer$ | $Required evidence and affected coding boundary$ |

## 6. Failure Modes and Operational Requirements

| Failure | Trigger or Path | Handling and Recovery | Observable Result | Verification |
| --- | --- | --- | --- | --- |
| $Failure$ | $Condition and affected C IDs$ | $Detection, retained state, recovery, and relevant limits$ | $What the user or caller observes$ | $T IDs or procedure$ |

| Area | Requirement or Decision | Verification |
| --- | --- | --- |
| Security and access | $Trust boundaries, least privileges, default access denial, input validation, relevant audit trails, and data protection$ | $Behavior tests or checks$ |
| Performance and resources | $Supported targets, units, load context, and limits; link unknowns to Q IDs$ | $Measurement method$ |
| Capacity and evolution | $Load and growth assumptions, bottlenecks, capacity limits, and observable architecture reassessment conditions; qualify estimates and unknowns$ | $Measurement or validation plan$ |
| Availability | $Required service behavior, acceptable interruption, and treatment of relevant single points of failure$ | $Failure and recovery checks$ |
| Observability | $Signals needed to detect failures and assess behavior$ | $How to verify the signals$ |
| Build and distribution | $Build, package, supported environments, and how users receive the change$ | $Relevant checks$ |
| Rollout and configuration | $Activation, compatibility, and rollout conditions$ | $Readiness and acceptance checks$ |
| Migration | $Data changes, old/new coexistence, and ordering$ | $Migration verification$ |
| Rollback and recovery | $Triggers, procedure, and limitations$ | $Recovery verification$ |
| Backup and restoration | $Affected data, retention, acceptable data loss, restoration time, procedure, and limits; distinguish from release rollback$ | $Recovered data and service checks$ |

## 7. Validation and TDD Strategy

### Test Boundaries

| Boundary | Behavior Verified | Real Dependencies and Test Replacements | Limits |
| --- | --- | --- | --- |
| $Public interface or agreed seam$ | $C IDs and behavior$ | $Real components and replacements$ | $What this test boundary cannot establish; follow-up verification$ |

### Critical Scenarios and Planned Verification

| Test | Contract and Example | Given and When | Expected Result | Incorrect Behavior Detected | Test Level |
| --- | --- | --- | --- | --- | --- |
| T1 | $C and source example IDs$ | $Critical setup, input, and action; defer only task-local detail with an owner$ | $Independent observable expectation$ | $Failure this test must detect$ | $Unit, integration, or end-to-end$ |

- **Existing coverage:** $Current tests, baseline, and execution status.$
- **Regression and integration:** $Behavior to protect and checks across Features.$
- **Verification gaps:** $Deferred or nonautomated checks, reasons, owners, and Q references.$

### Candidate Behavior Increments

| Increment | Observable Capability | Verification Obligation | Prerequisites |
| --- | --- | --- | --- |
| $Small behavior slice$ | $Contract and acceptance outcome$ | $Critical T ID or behavior obligation; task mode refines the first Red step$ | $Real dependency or None$ |

- **Downstream execution:** $Require Red → Green → Refactor one behavior at a time. Task mode refines local tests and steps; retain final integration checks here.$
- **Evidence required:** $Test, command, code state, actual Red and Green results, refactoring outcome, and relevant final checks.$
- **Current evidence:** $Planned, or links to actual results with their limits. Explain any TDD exception.$

## 8. Premises and Open Questions

| Type | Statement and Impact | Evidence / Validation Status | Follow-up |
| --- | --- | --- | --- |
| $Accepted premise or Assumption to validate$ | $Statement and affected IDs. Blocks approval: Yes / No and reason. Blocks implementation: Yes / No and reason$ | $Basis and source. For an assumption: observation, collection method, and disconfirming result$ | $Owner, required evidence, timing, and affected decisions to reopen$ |
| $Q ID / Fact to investigate or User decision / State$ | $Question, affected IDs, and dependencies. Approval and implementation impact with reasons$ | $Answer and source, Pending, or Unknown. For a user decision: options, tradeoffs, and recommendation. Retain prior answers if reopened$ | $Next action, required evidence, owner, and content awaiting review$ |

<!-- Link existing product questions to their authoritative records. Preserve resolved records. Use None only where no uncertainty or follow-up remains. -->

## 9. Review and Approval

- **Reviewed version:** $Version and scope of the review.$
- **Review type and reviewer:** $Independent or self-review; reviewer identity.$
- **Coverage and limits:** $Areas reviewed, skipped areas with reasons, and independent review requests used if applicable.$

| Finding and Location | Evidence and Consequence | Remedy or Question | Disposition and Approval Impact |
| --- | --- | --- | --- |
| $Finding or None$ | $Basis and effect$ | $Correction or Q ID$ | $Open, resolved with basis, or deferred with owner; Blocks approval: Yes / No and reason$ |

- **Applied changes:** $Changes and verification of affected content.$
- **Approval:** $Pending, or approver, exact approved version, date, and source.$

## 10. Handoff to Task Breakdown

- **Design baseline:** $Task directory, document paths, and exact technical and product versions, including supporting designs.$
- **Shared contracts and coordination:** $Interface and module ownership constraints.$
- **Deferred decisions:** $References to owners, constraints, evidence, and resolution deadlines; no critical architecture assumption hidden as a local choice.$
- **Sequence constraints:** $Real dependencies, necessary preparatory refactors, and Section 7 increment references.$
- **Final integration acceptance:** $Observable result and verification across the completed change.$
- **Outstanding validation:** $Question or assumption references, owners, evidence, and work blocked.$
- **Ready for task breakdown:** $Yes / No for the named scope, with reasons under the document contract; this does not mean every task is ready to code.$
- **Task breakdown:** Pending
- **Handoff summary:** $Scope and input versions, output references, conclusion and evidence limits, unresolved issues, next function and responsible recipient.$
- **Feedback:** $None, or issue identity, constraint, observations versus estimates, impact, alternatives, requested decision, and affected downstream work.$
- **Next action:** $Owner approval, planner handoff, or upstream feedback with the expected result.$
