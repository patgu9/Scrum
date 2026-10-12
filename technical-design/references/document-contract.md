# Technical design contract

This reference owns mode selection, artifacts, approval, readiness, and handoffs. The [design methods](design-methods.md) own design technique; [engineering review](engineering-review.md) owns review coverage.

## Modes and required inputs

| Mode    | Responsible role                                                      | Required inputs                                                                                                                                                                 | Output and next function                                                                                                       |
| ------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Overall | Architect; engineering lead can hold this responsibility              | Approved product behavior and exact version, project/code context, constraints, relevant feedback                                                                               | Versioned overall design for owner approval, then a planning handoff to engineering lead using `planner`; or upstream feedback |
| Task    | Assigned developer; architect reviews high-risk or cross-task choices | Claimed task and branch reference, approved product and overall-design versions, current code context, acceptance criteria, dependencies, and constraints on deferred decisions | Task design ready for `code-development`, or feedback to overall design, product design, or `planner`                          |

Infer the mode from scope and artifacts. A request to design a change before assignment normally uses overall mode. A request to refine one assigned task normally uses task mode. An existing document's mode is evidence, not authority to ignore the requested scope. Ask one focused question only if context cannot distinguish the modes. Do not reinterpret a task request as overall design merely because required task inputs are missing.

Missing, inaccessible, conflicting, or stale input blocks dependent conclusions. Identify the missing input, its supplier, and affected work. Independent analysis can remain a draft, but cannot claim readiness. A draft product source can support explicitly requested provisional exploration; approval and planning readiness still require an approved product baseline. Do not infer approval from document location, a task assignment, or the request to write a design.

In task mode, inspect the recorded branch and code baseline when accessible. Branch creation or reuse belongs to `git-workflow` or the project's authorized Git procedure, not this Skill's design instructions. Do not create a duplicate branch, change another task's checkout, or claim that the branch exists without evidence. A missing branch reference keeps implementation readiness false while useful independent design can continue.

## Document scope and saving

Follow the shared [task artifact layout](../../product-design/references/artifact-layout.md). Reuse the source product document's change directory. An assigned development task stays within that directory; it does not start a new product change directory.

- **Overall:** Keep `technical-design.md` as the authoritative overall document for the coordinated change. It owns shared contracts, source coverage, and integration verification across Features. Use the [overall template](../assets/technical-design-doc-template.md).
- **Task:** Start from the claimed task's standalone entry file and exact version. For a new local design, use `technical-design.md` beside that entry point, normally `tasks/<task-key>/technical-design.md`. Use the [task template](../assets/task-design-template.md); a simple task can use a short versioned file with the same required information. Link back to `task.md` and to the change-level product and overall technical documents. Once saved, link it from the task and eventual PR through the applicable workflow. Reuse a valid existing design location according to the shared layout's migration rules; do not create a competing design. An index link changes no shared decision or approval.

Keep one authoritative location per decision. Task designs link shared decisions rather than copying competing versions. Split other supporting designs only for substantial independent complexity or a clear boundary. Read before editing; preserve unrelated content and stable IDs. Do not create empty downstream artifacts.

Record exact product, overall-design (task mode), and code baselines. Include relevant uncommitted changes or state `Greenfield`. If the source has no explicit version, use a stable snapshot or revision. Requirements confirmed only in conversation need stable source references and explicit approval evidence. Do not invent rules to fill a template.

Use explicit artifact versions, starting at `v1`; increment for substantive changes. Retain earlier decision bases when invalidated. Revisions stay in the same file. Separate approval evidence from document and code versions.

## Structure and content placement

Overall mode retains the ten sections of the overall template unless the user supplies another format:

| Section                                       | Content                                                                                                                |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| 1. Purpose and Scope                          | Outcome, included Feature IDs, exclusions, source constraints, and Success Criteria                                    |
| 2. Current System and Constraints             | Verified behavior, evidence limits, terminology, applicable architecture decisions, and relevant technical debt        |
| 3. Behavioral Contracts                       | Shared observable behavior, product-rule references, and verification obligations                                      |
| 4. Approaches and Decisions                   | Alternatives, tradeoffs, selected approach, evidence, and rejected options                                             |
| 5. Technical Solution                         | Module boundaries, shared interfaces, data ownership, invariants, critical flows, and deferred local decisions         |
| 6. Failure Modes and Operational Requirements | Relevant security, consistency, capacity, availability, recovery, migration, and rollout constraints                   |
| 7. Validation and TDD Strategy                | Test boundaries, critical scenarios, integration verification, candidate behavior increments, and evidence obligations |
| 8. Premises and Open Questions                | Unknowns, assumptions, dependency and approval impact, and decisions to reopen                                         |
| 9. Review and Approval                        | Reviewed version, findings, dispositions, coverage limits, and owner approval evidence                                 |
| 10. Handoff to Task Breakdown                 | Baselines, ownership, dependencies, deferred decisions, and readiness for `planner`                                    |

Task mode records task identity, versions, branch/code baseline, scope and acceptance references, implementation approach, affected code, local error handling, planned self-tests, dependencies, open decisions, review disposition, and implementation readiness. Use only the detail needed for the task. A short note can carry this information without all template headings. Do not repeat the full architecture template for routine tasks.

Write plain, concise English unless the user requests another language. Follow [technical-writing](../../technical-writing/SKILL.md). Remove placeholders and instructional comments from completed artifacts. For an inapplicable area, give a short reason rather than inventing work.

## Decision depth and deferred work

Overall design must resolve enough architecture and shared behavior to split and assign coherent work. Identify module responsibilities, cross-task interfaces, data ownership, invariants, critical failures, integration acceptance, and material feasibility risks.

Resolve a detail before affected assignment when it determines feasibility, shared contracts, security or consistency guarantees, or task boundaries. A critical algorithm, storage capability, migration, or dependency can need deep investigation in overall mode. Private helpers and other local, reversible choices can remain open for task mode.

Each deferred decision identifies its scope, owner or accountable role pending assignment, constraints, required evidence, and the point before which it must be resolved. A detail that could overturn the architecture is an unresolved risk, not a harmless deferral. Missing critical evidence blocks the affected assignment or calls for a separately authorized investigation. Reuse authorization already given for that investigation.

Task mode resolves its local approach against actual code and dependencies. High-risk or cross-task choices receive architect review before affected coding. Routine decisions within approved constraints need no new human gate. Architect review checks consistency; it cannot approve changes to an owner-approved baseline. Keep review identity and any self-review explicit.

## Traceability and evidence

Preserve source Feature, rule, example, and Success Criteria IDs. Assign stable `C<n>` IDs to new technical contracts and `T<n>` IDs to planned tests when useful for traceability. Never renumber or reuse existing IDs. Qualify references by document when IDs occur in multiple artifacts.

Overall design maps each included product rule to an observable contract and verification obligation or an explicitly accepted exclusion. Task design maps its assigned acceptance conditions to shared contracts and concrete self-tests. It need not reproduce coverage for unrelated tasks. Overall mode can defer local test construction while retaining critical scenarios, integration checks, and evidence obligations.

A test can cover several contracts and vice versa. Inspect expected outcomes and assertions; ID lists alone do not establish coverage. Derive expected results from contracts rather than implementation. Keep existing tests, planned tests, unrun checks, failures, and actual passes distinct.

Separate current facts, proposed behavior, accepted decisions, assumptions, and executed verification. Cite sources, versions, commands or procedures, actual results, and limits as applicable. A failed probe does not establish that a system lacks the capability. Planned TDD steps do not establish Red or Green results.

## Questions and assumptions

Reuse the product-design [clarification protocol](../../product-design/references/discovery-methods.md#clarify-decisions-and-terms) and [question records](../../product-design/references/document-contract.md#question-records):

`Type | Statement and Impact | Evidence / Validation Status | Follow-up`

Link existing questions to their authoritative records. Allocate new `Q<n>` IDs without collisions or qualify them by document. State affected rules, contracts, tests, and decisions. Record whether each issue blocks approval, task breakdown, or implementation, with the relevant reason. Independent work needs a valid, unaffected baseline.

Use the product contract's [assumption validation rules](../../product-design/references/document-contract.md#assumption-validation). Specify the observation, how to collect evidence, the disconfirming result, affected decisions, and owner. Keep resolved questions and reopening history. Routine authorized technical choices need no new permission; material tradeoffs beyond that authority require a decision.

## Status and approval

| Mode    | Status      | Meaning                                                                                  |
| ------- | ----------- | ---------------------------------------------------------------------------------------- |
| Both    | `DRAFT`     | Incomplete design, missing required inputs, unresolved direction, or a readiness blocker |
| Both    | `IN_REVIEW` | Design content is ready for review; required review or approval is pending               |
| Overall | `APPROVED`  | The human owner explicitly approved this exact overall version; cite the source and date |
| Task    | `READY`     | Task readiness conditions below are satisfied; no new human approval is implied          |

Record readiness separately from status. An approved overall design can still have an evidence gap that blocks affected task breakdown. An `IN_REVIEW` task is not ready while required architect review is outstanding. Task `READY` applies to its declared scope and baselines, not to other tasks, changed code baselines, or release readiness. If an optional proposal conflicts with the baseline, record its separate blocked disposition. Original work can remain ready only with evidence that it does not depend on or adopt that proposal. Name the ready scope explicitly; an unqualified READY must not cover the blocked proposal.

Owner approval is required for product behavior and the overall technical solution before affected planning proceeds. A task design that refines choices within those approved baselines does not add an owner approval gate. Design approval and readiness do not themselves authorize implementation or external operations; apply existing task authorization.

If approved product behavior or shared technical decisions must change, reopen the affected overall design as `DRAFT` and follow the feedback loop below. A revised task design returns to `DRAFT` until its affected readiness conditions are reassessed; use `IN_REVIEW` when only the required review remains. Local task refinements update the task design and its review/readiness as affected; they do not automatically reopen the overall document. Typographic or link-index edits that change no decision preserve approval. Reassess source and code revisions before every handoff; do not silently adopt changed baselines.

## Overall handoff to planner

Set `Ready for task breakdown: Yes` only for an explicitly identified scope when:

- The exact overall version and included product baseline have owner approval.
- Included product rules have shared contracts and verification obligations, or accepted exclusions.
- Cross-task interfaces, data ownership, critical failures, dependencies, and integration checks support coherent assignment.
- No unresolved material feasibility or shared-design decision blocks that scope. Deferred local choices have owners, constraints, evidence requirements, and deadlines before coding.
- Review findings have dispositions and no applicable approval or breakdown blocker remains.

Output the change directory, document paths and versions, included rules and contracts, ownership boundaries, candidate behavior increments, dependencies, integration acceptance, and deferred decisions. Candidate increments guide planning; they are not assigned tasks. The first task can start its local design without requiring every private implementation decision upfront.

Engineering lead uses the separate `planner` Skill to split and assign work, including design, implementation, and verification effort. Do not assume it is installed. If unavailable, preserve this package and name the missing stage. This Skill does not publish tasks or choose app commands.

Record `Task breakdown: Pending` until the separate stage supplies its output. Completed plans must preserve coverage, dependency order, reviewable goals, and enough context for task design. Readiness for planning is not readiness for every task's coding. Each claimed task follows task mode before implementation.

## Task handoff to code-development

Set `Ready for implementation: Yes` and task status `READY` only when:

- The claimed task, branch reference, exact approved product and overall versions, relevant code context, and dependencies are valid for this work.
- The local approach, affected code, relevant errors, and acceptance-linked self-tests are defined without a blocking local choice or evidence gap.
- Required architect review is complete for high-risk or cross-task decisions, with no unresolved blocking finding. Record why such review is unnecessary for routine local work.
- No unapproved product or shared-design change is needed; the task remains one reviewable goal under its supplied review policy.
- Any required advance reviewer agreement for unusually large or complex scope is recorded under the [reviewability policy](../../planner/references/planning-methods.md#decide-whether-to-split). Pending agreement blocks affected implementation; agreement does not accept unseen code.

Output the task design and common handoff to the assigned developer using `code-development`. Include the task branch, source versions, planned verification, review disposition, and remaining nonblocking issues. Missing follow-on capability does not invalidate a ready design; report it as a delivery blocker rather than claiming implementation occurred.

Apply the task's supplied reviewability policy during design. The team's [planning methods](../../planner/references/planning-methods.md#estimate-work-and-review-scope) own the Google-based scope assessment and advance-review agreement rules. Judge goal, context, footprint, behavioral risk, verification, and simplicity; line counts are descriptive. Keep related tests and necessary usage together, and separate substantial refactoring from behavior changes when feasible. Return unmanageable scope or missing review arrangements to `planner` before affected implementation; do not assign replacement tasks from this Skill.

During implementation, update task decisions when new evidence changes the approach, before dependent coding continues. Reassess affected self-tests and review. Independent code review, integration, QA, and ship approval remain downstream obligations.

## Feedback and revisions

A constraint or decision request is a valid design output before a forward deliverable is complete. Every handoff contains scope/task and input versions, output references, conclusion and evidence, unresolved issues, and next function with its accountable recipient. State mode and readiness; do not equate completion of design work with downstream acceptance.

For feedback, also record a stable issue identity, affected requirements/contracts, the constraint, observations versus estimates and uncertainty, impact, alternatives and tradeoffs, and the requested decision or missing fact. Say when no alternative is known. Without a supplied cost or complexity limit, request a tradeoff decision instead of inventing a threshold or declaring impossibility.

Route product scope, behavior, or acceptance changes to PM using `product-design`. Route shared architecture and interface changes to the architect using overall mode. Route task-boundary or assignment problems to engineering lead using `planner`. Local implementation corrections stay with the developer using task mode or `code-development`, as appropriate. Project Manager tracks these handoffs through `project-manager`; missing routing tools do not authorize app operations.

Keep affected work blocked until applicable decisions, approvals, and evidence are current. Identify downstream plans, tasks, interfaces, code, cases, and conclusions needing reassessment. Preserve prior versions and decisions as history. Independent work can continue only when its inputs, interfaces, dependencies, and approvals remain valid; uncertainty about impact is not proof of independence.

A revised product version needs owner approval before renewed overall design; changed overall decisions need technical approval before affected planning resumes. Recheck affected task designs before coding resumes. A local task update within approved constraints needs only its applicable review and readiness check.

Close feedback with supported specialist resolution or an explicit owner decision to defer or stop the affected scope. Approval alone does not prove feasibility. Deferral does not mean delivery. If the same issue returns on the same baseline without new evidence or a viable alternative, stop repeating the handoff. Escalate through Project Manager with attempted options, consequences, and the missing decision; keep affected work blocked.
