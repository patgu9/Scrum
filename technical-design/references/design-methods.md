# Technical design methods

Use these methods in both modes. Apply the [document contract](document-contract.md#decision-depth-and-deferred-work) to select decision depth and readiness. Overall mode defines architecture, shared behavior, and critical verification before planning. Task mode refines one assignment against those baselines before coding. Scale detail to risk and dependencies, not to template size.

## Establish current facts

Read the relevant source, tests, schemas, interfaces, build configuration, and deployment guidance. Find reusable behavior before proposing new modules.

Use the product Design Doc's Glossary for product terms. Define additional technical terms in the overall design's Section 2 or the task note's baseline context. If the project has separate domain guidance or architecture decision records (ADRs), consult them and report conflicting definitions or decisions. Separate domain documents are optional inputs.

Trace the current path from a relevant entry point through dependencies to an observable result. Identify where the proposed change alters that path. Cite source locations with their revision; separate current code from intended behavior.

Identify existing patterns, conventions, and technical debt that affect this change. For each relevant problem, record its evidence and effect on correctness or change cost. Explain whether to retain, work around, or repair it. Keep unrelated cleanup outside scope. Record this assessment with current-system evidence; place necessary repairs and regression protection in the solution and handoff.

For an existing system, inspect the test framework and useful test boundaries. Identify protected behavior, uncovered paths, and constraints on local execution. For a new system, record framework and runtime choices as proposals until decided.

Use bounded, safe checks to answer questions at the selected design depth. Before an overall-mode probe, state the architecture decision, evidence needed, and stopping condition under the [decision-depth rule](document-contract.md#decision-depth-and-deferred-work). Record commands, results, and limits. If a needed experiment exceeds the authorized work, return its purpose and required authorization. Keep dependent conclusions provisional; classify missing access by the stage it actually blocks.

## Prioritize quality goals and resolve tradeoffs

Identify the quality goals that materially influence this design, using confirmed product goals and constraints as their basis. Separate mandatory constraints from preferences that can be traded. Rank competing preferences, explain ties where relevant, and cite the priority's source and decision state. Do not invent a universal ordering or numeric weights.

Express each key goal through a usage, failure, or change scenario: the affected system, operating conditions, event, required response, and measurable or otherwise observable acceptance criterion. Reuse existing product examples, contracts, or `T<n>` scenarios. Keep unknown targets or priorities explicit in the question record; classify the work they block under the document contract.

Compare meaningful alternatives against the same goals and scenarios. For each material conflict, state the goals affected, which takes precedence under the stated conditions, the benefit, the accepted cost or degradation, and its permissible limit. A preference cannot override a mandatory constraint. If no approach satisfies the constraints, return the conflict through the existing decision process.

Explain how evidence supports the selected tradeoff and what change in assumptions, load, or requirements would reopen it. Distinguish estimates and untested claims from observations. Use bounded investigation when the decision depends on missing evidence; do not turn an unexplored alternative into a proven impossibility.

Overall mode owns shared quality priorities and tradeoffs. Task mode references those decisions and resolves local choices within them. Route proposed changes to approved targets or priorities through the existing baseline feedback rules. A simple task can cite the applicable goals and state that no new tradeoff arises.

## Design behavior and interfaces

Start with product rules and examples. Define what a caller or user can observe, including outcomes that must not occur. Distinguish intentional behavior changes from behavior that must remain compatible.

Choose the highest useful test boundary that provides reliable feedback for the behavior. Reuse existing public interfaces where they fit. A test seam is a boundary where a dependency can be replaced during testing. Establish shared test boundaries before task breakdown. Refine task-local seams during task design without exposing new shared contracts silently.

Compare alternatives for consequential choices under the [quality priorities and tradeoff method](#prioritize-quality-goals-and-resolve-tradeoffs). Consider reuse, minimal change, and a different module or dependency boundary when relevant. Compare interface complexity, caller needs, testability, failure handling, operational cost, and future change cost. Explain why one approach is sufficient when no meaningful alternative remains.

Choose the simplest approach that satisfies confirmed behavior and quality constraints. Explain the current need for each new abstraction, dependency, configuration option, or extension point. Do not add capabilities solely for hypothetical future use.

For an uncertain interface, sketch distinct designs and a caller example before selecting one. Prefer modules that hide substantial implementation detail behind a small, coherent interface. Do not expose internal helpers solely to make them easy to mock.

Assess cohesion and coupling in the selected scope's solution. Group responsibilities that change for the same reason. Trace which modules and callers must change for a representative requirement change. Examine circular dependencies, exposed internals, and modules with unrelated responsibilities. Separate module boundaries from deployment boundaries; require independent deployment only when actual release or operational needs justify it. Explain accepted coupling and its consequences.

Select interfaces under the contract's [shared-contract rule](document-contract.md#decision-depth-and-deferred-work). In overall mode, define the agreement required by consumers:

- Inputs, outputs, validation, and caller-visible failure semantics needed across the boundary.
- Invariants, ordering, and compatibility requirements.
- Ownership of data and side effects.
- Time, resource, and concurrency constraints that affect coordination, including units and their basis.

Identify which consumer needs each exact field, command, or sequence before specifying it in overall mode. Leave complete feature protocols and schemas to task design where the shared agreement does not depend on them. In task mode, define the local interfaces, algorithms, configuration, and errors needed to begin coding. Investigate high-risk choices before treating the task as ready. Use existing paths as evidence or likely integration points; avoid fixing every future filename in the design.

Keep important decisions and rejected alternatives in the design. Connect their basis, risks, and verification under the contract's [reasoning links](document-contract.md#connect-decisions-to-scenarios-risks-and-verification). Link an existing ADR when it owns a decision. A separate ADR is useful for a hard-to-reverse choice with non-obvious tradeoffs; create one when project conventions or the request call for it.

## Use diagrams to expose missing behavior

Use the [UML modeling guide](uml-modeling.md) to select views, define their semantics, and check consistency with contracts and verification. Model uncertain relationships and paths while comparing approaches; revise the model as decisions change. Place each view beside its explanation. Show one shared flow for Features that participate in the same behavior.

## Define failures and operational behavior

Trace normal, boundary, and failure paths at the selected scope. Overall mode defines shared guarantees, failure containment, recovery responsibilities, and integration checks. Task mode defines the local detection, retained state, recovery steps, and tests needed to implement those guarantees.

Examine duplicates, partial writes, concurrency, dependency failures, cancellation, and retry exhaustion where the design permits them. State idempotency and transaction boundaries explicitly when correctness depends on them. Define which operations may retry and which outcomes prohibit retry. Task design selects retry counts, delays, and mechanisms unless those values determine a shared guarantee.

Address security and data access at the actual trust boundaries. Specify the least privileges needed and deny access by default. Define input validation and caller-visible rejection behavior at relevant boundaries. Identify security-sensitive actions that need an audit trail. Map these requirements to behavior contracts and verification where applicable.

Define relevant performance and resource constraints using supported targets. Record expected load, concurrency, data volume, and growth assumptions. Identify likely bottlenecks and the current design's capacity limits; distinguish estimates from measurements. Specify observable conditions that would require architecture reassessment and the options to evaluate then. Use open questions for missing targets, thresholds, or measurement evidence. Do not prescribe architecture changes from user counts alone or implement speculative scaling capabilities.

When service availability matters, define the required service behavior and acceptable interruption under relevant failures. Identify single points of failure and the redundancy or degraded behavior needed to meet confirmed requirements. State how to verify those outcomes.

Describe how the change reaches users: build, package or deploy, configuration, compatibility, and rollout. For persistent-state changes, describe migration, coexistence, and recovery. State rollback limitations when data changes cannot be reversed safely.

When the change affects data durability or recovery, record supported backup scope, retention, acceptable data loss, and restoration-time requirements. Keep release rollback, service restart, and backup restoration distinct. Overall Sections 6 and 7 define shared recovery guarantees and acceptance; the responsible task defines the procedure and concrete checks. Record unconfirmed targets as questions with the stage they block. Investigate recovery mechanics early only when an architecture decision depends on them.

Specify the signals needed to detect failures and assess rollout. Match verification to the risk; do not require a benchmark or a new monitoring system for every change.

## Plan test-driven development

Test-driven development (TDD) uses a failing behavior test to guide a small implementation step, followed by refactoring while tests remain green.

Plan observable behavior before private implementation detail. In overall mode, define critical architecture scenarios and integration outcomes, with verification responsibility for local product rules. In task mode, specify concrete setup, action, independent expected result, and the incorrect behavior each test detects. Derive expectations from contracts or product examples, not the implementation being tested.

Choose test levels by the claim:

- Use unit tests for behavior that can be checked reliably within a small boundary.
- Use integration tests for contracts between components, storage, or adapters.
- Use end-to-end tests for critical user paths that require the full system.

In overall mode, identify shared test boundaries, required live evidence, and limits of substituted dependencies. Task design chooses concrete fixtures and replacements. Prefer real local components or a test database when practical. Replace external services, time, or randomness at explicit boundaries. State what a replacement cannot verify and how to check the real integration contract.

Avoid tests coupled to private call order, internal collaborators, or implementation-derived expectations. Use interaction assertions when the interaction is itself part of the required public contract.

Retain verification obligations for relevant normal, boundary, failure, recovery, and regression behavior. Overall mode assigns local coverage to the responsible feature or module and retains cross-feature acceptance. Task mode develops the assigned cases. Test count and line coverage alone do not demonstrate coverage.

In overall mode, identify candidate behavior increments and their dependencies. Specify the TDD evidence expected downstream without drafting every functional test. These increments inform `planner`; they do not assign work. Stop at the contract's [overall completion conditions](document-contract.md#stop-overall-design-at-planning-depth).

In task mode, refine the assigned increment into small Red → Green → Refactor steps. Describe the first failing test, its intended failure reason, and prerequisites. Each step adds observable behavior across the layers it needs. Do not use a large test inventory to avoid resolving a blocking implementation choice.

Plan for the downstream [code-development execution loop](../../code-development/references/tdd-and-verification.md#execute-one-behavior-at-a-time): a valid Red, minimal Green, and necessary refactoring for each behavior. That reference owns execution conditions and evidence recording. Task design supplies the intended failure and concrete test setup within the overall verification obligations.

Do not prescribe writing all executable tests before any implementation. A task design can contain its scenario inventory while execution proceeds one behavior at a time.

Existing behavior may need characterization tests that already pass. Label them as baseline evidence. Do not fabricate a Red result. If TDD does not apply to a change, state why and specify alternative verification without claiming a TDD cycle.

Specify the [execution evidence](../../code-development/references/tdd-and-verification.md#preserve-execution-evidence) required at handoff. At design time, keep results `Planned` unless actual evidence exists. Link any development results from their authoritative delivery record rather than maintaining a competing execution log in the design.
