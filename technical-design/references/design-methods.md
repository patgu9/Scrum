# Technical design methods

Use the [document contract](document-contract.md#decision-depth-and-deferred-work) for scope and stopping conditions. Select methods for the decisions and risks present; template size does not determine design depth.

## Establish current facts

Read project instructions, relevant code, tests, schemas, interfaces, build configuration, and deployment guidance. Trace a relevant entry point through dependencies to an observable result. Cite locations and revisions; distinguish current behavior from proposals.

Find reusable behavior, conventions, and relevant technical debt. Record the evidence, impact, and choice to retain, work around, or repair each relevant problem. Keep unrelated cleanup outside scope; include regression protection for necessary repairs.

Reuse the product glossary and applicable architecture decision records (ADRs). Define additional terms in the baseline context and report conflicting definitions or decisions. Inspect existing test boundaries and execution limits. For a new system, keep runtime and test-framework choices proposed until decided.

Use bounded checks for missing facts. Before an overall-mode probe, identify the architecture decision, required evidence, and stopping condition. Keep investigation detail with the relevant Q record or linked evidence; retain the conclusion and limits in the design under the [evidence rules](document-contract.md#traceability-and-evidence). If an experiment exceeds existing authorization, return its purpose and required authorization. Classify missing access by the stage it actually blocks.

## Prioritize quality goals and resolve tradeoffs

Use confirmed product goals and constraints. Separate mandatory limits from preferences; rank competing preferences with their source and decision state. Do not invent weights or priorities.

Express each key goal as a scenario: affected system, operating conditions, event, required response, and observable acceptance criterion. Reuse product examples, contracts, or test scenarios. Record unknown targets and priorities as questions.

Compare meaningful alternatives against the same goals and scenarios. For each material conflict, state the priority, benefit, accepted cost, and permissible limit. A preference cannot override a mandatory constraint. If no approach meets the constraints, return the conflict through the decision process.

Explain the supporting evidence and what changed assumption, load, or requirement would reopen the decision. Investigate missing evidence when it determines the choice. An unexplored alternative is not a proven impossibility. Routine task designs can reference approved priorities without creating a new tradeoff analysis.

## Design behavior and interfaces

Start with product rules and examples: observable outcomes, prohibited results, preserved behavior, and intentional compatibility changes. Choose the highest useful test boundary that gives reliable behavior feedback. Reuse public interfaces where they fit; do not expose private helpers solely for mocking.

Choose the simplest approach that satisfies confirmed behavior and quality constraints. Require a current need for each new abstraction, dependency, configuration option, or extension point. For consequential choices, compare reuse, minimal change, and different boundaries under the [quality method](#prioritize-quality-goals-and-resolve-tradeoffs). Explain when only one meaningful approach remains.

For an uncertain interface, sketch distinct designs and a caller example. Compare caller needs, complexity, testability, failure handling, operational cost, and future change cost. Prefer a small, coherent interface that hides implementation detail.

Assess cohesion and coupling through a representative requirement change. Identify affected callers, circular dependencies, exposed internals, and unrelated responsibilities. Explain accepted coupling. Module separation does not require independent deployment; release or operational needs must justify it.

Apply the contract's [shared-contract rule](document-contract.md#decision-depth-and-deferred-work). Define the agreement consumers need: input/output and failure semantics, validation, invariants, ordering, compatibility, ownership, and relevant time/resource/concurrency limits with units and basis. In overall mode, exact fields or sequences need a named consumer or architecture decision.

Task design resolves local interfaces, algorithms, configuration, and errors against actual code. Identify likely integration points without fixing every future filename. Keep decision rationale, rejected alternatives, risks, and verification together under the contract's [reasoning links](document-contract.md#connect-decisions-to-scenarios-risks-and-verification). Link existing ADRs; create a separate ADR only when project conventions or the request call for one.

## Use diagrams to expose missing behavior

When relationships, ordering, or state remain unclear, use the [modeling guide](uml-modeling.md). Reuse a sufficient existing view, table, or textual flow. Model uncertain paths while comparing approaches, then update the selected representation as decisions change.

## Define failures and operational behavior

Trace relevant normal, boundary, and failure paths. Overall design establishes shared guarantees and recovery responsibilities; task design supplies local detection, retained state, recovery steps, and checks.

Use the applicable rows below. Record unsupported targets as questions with their affected stage and scope. Do not create operational requirements merely to fill the table.

| Trigger | Design work |
| --- | --- |
| Partial completion, duplicates, concurrency, dependency failure, cancellation, or retry | Define transaction and idempotency boundaries, permitted retries, prohibited retries, and exhaustion outcomes. Keep local retry settings in task design unless a shared guarantee depends on them. |
| Trust or access boundary | Define least privileges, default denial, input validation, caller-visible rejection, and audit needs for sensitive actions. Link verification. |
| Performance or resource constraint | Record supported load, concurrency, volume, growth, bottlenecks, and capacity limits. Distinguish estimates from measurements. Identify observable reassessment conditions and options; do not add speculative scaling from user counts alone. |
| Availability requirement | Identify single points of failure and required redundancy or degraded behavior. Define acceptable interruption and verification. |
| Delivery or compatibility change | Describe build/package/deployment, configuration, compatibility, and rollout at the selected depth. |
| Persistent-state change | Define migration, coexistence, recovery, and rollback limits for irreversible data changes. |
| Durability or recovery requirement | Define backup scope, retention, acceptable data loss, restoration time, and verification. Keep release rollback, restart, and backup restoration distinct. |

Specify signals needed to detect failure and assess rollout. Select checks by risk; a change does not automatically require a benchmark or new monitoring system. Apply the contract's decision-depth rule before investigating task mechanics early.

## Plan test-driven development

Plan verification from contracts and product examples. Use unit tests for reliable local checks, integration tests for component/storage/adapter contracts, and end-to-end tests for critical paths that need the full system. Preserve relevant normal, boundary, failure, recovery, and regression coverage.

- **Overall:** Define shared test boundaries, critical architecture scenarios, cross-feature acceptance, required live evidence, and local verification responsibility. Identify candidate behavior increments and dependencies for `planner`.
- **Task:** Map acceptance conditions to concrete setup, action, independent expected result, and the incorrect behavior each test detects. Plan small Red → Green → Refactor steps, starting with a failing behavior test, its intended failure reason, and prerequisites.

Prefer real local components or a test database when practical. Replace external services, time, or randomness at explicit boundaries. State each replacement's limits and how to verify the real integration. Avoid assertions about private call order or collaborators unless the interaction is itself a required contract.

Use the [code-development execution loop](../../code-development/references/tdd-and-verification.md#execute-one-behavior-at-a-time) one behavior at a time. A scenario inventory does not require writing all executable tests before implementation. Resolve blocking design choices instead of expanding the inventory.

Keep planned verification separate from execution. Characterization tests can already pass; label them as baseline evidence, not Red. If TDD is inapplicable, state why and specify alternative verification. Test counts and line coverage alone do not establish behavioral coverage.

The downstream [execution evidence record](../../code-development/references/tdd-and-verification.md#preserve-execution-evidence) owns commands, code states, results, and refactor evidence. Link it rather than copying its fields into the design. For a design-time probe, retain the supported design conclusion and evidence limits with its source reference.
