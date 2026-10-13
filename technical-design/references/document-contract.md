# Technical design contract

This reference owns mode selection, artifacts, approval, readiness, and handoffs. The [design methods](design-methods.md) own design technique; [engineering review](engineering-review.md) owns review coverage.

## Modes and required inputs

| Mode    | Responsible role                                                      | Required inputs                                                                                                                                                                 | Output and next function                                                                                                       |
| ------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Overall | Architect; engineering lead can hold this responsibility              | Approved product behavior and exact version, project/code context, constraints, relevant feedback                                                                               | Versioned overall design for owner approval, then a planning handoff to engineering lead using `planner`; or upstream feedback |
| Task    | Assigned developer; architect reviews high-risk or cross-task choices | Claimed task and branch reference, approved product and overall-design versions, current code context, acceptance criteria, dependencies, and constraints on deferred decisions | Task design ready for `code-development`, or feedback to overall design, product design, or `planner`                          |

Infer the mode from scope and artifacts. A request to design a change before assignment normally uses overall mode. A request to refine one assigned task normally uses task mode. An existing document's mode is evidence, not authority to ignore the requested scope. Ask one focused question only if context cannot distinguish the modes. Do not reinterpret a task request as overall design merely because required task inputs are missing.

Missing, inaccessible, conflicting, or stale input blocks dependent conclusions. Identify its supplier and apply the [stage and scope rules](#questions-and-assumptions). Independent work can claim readiness only for a named scope that satisfies its own conditions. A draft product source can support explicitly requested provisional exploration; approval and planning readiness still require an approved product baseline. Do not infer approval from document location, a task assignment, or the request to write a design.

In task mode, inspect the recorded branch and code baseline when accessible. Branch creation or reuse belongs to `git-workflow` or the project's authorized Git procedure, not this Skill's design instructions. Do not create a duplicate branch, change another task's checkout, or claim that the branch exists without evidence. A missing branch reference keeps implementation readiness false while useful independent design can continue.

## Document scope and saving

Reuse the source product document's change directory, normally `<project-root>/doc/YYYY-MM-DD-task-slug/`. An assigned development task stays within that directory; it does not start a new product change directory.

- **Overall:** Save `technical-design.md` beside `product-design.md` as the authoritative overall document. It owns shared contracts, source coverage, and integration verification across Features. Use the [overall template](../assets/technical-design-doc-template.md).
- **Task:** Start from the claimed task's standalone entry file and exact version. Save `technical-design.md` beside that entry point, normally `tasks/<task-key>/technical-design.md`. Use the [task template](../assets/task-design-template.md); a simple task can use a short versioned file with the same required information. Link back to `task.md` and to the change-level product and overall technical documents. Once saved, link it from the task and eventual PR through the applicable workflow. An index link changes no shared decision or approval.

Keep supporting records beside the design they belong to. Overall records stay at the change level; task records stay beside that task's design.

| File | Purpose | Template |
| --- | --- | --- |
| `technical-design.md` | Current solution, rationale, contracts, verification obligations, material limits, and readiness | Mode-specific template above |
| `technical-design-questions.md` | Questions, answers, investigation evidence, assumption validation, and baseline/feedback history | [Questions and decisions](../assets/questions-template.md) |
| `technical-design-review.md` | Review attempts, scenario walkthroughs, findings, corrections, and verification history | [Review record](../assets/review-template.md) |

Create a supporting file when its first record is needed; do not create empty logs. Reuse an accessible authoritative external record instead of copying it. In the design's Supporting Records line, link existing files or external records; mark unstarted records as `Not started`. Supporting files link back to their design and identify mode, scope, and applicable versions. Use relative local links and document-qualified IDs across overall, task, and product records. Include all existing supporting references in handoffs.

Reuse a valid existing design location unless migration is requested or needed to resolve ambiguity. Keep one current file per design; do not create `technical-design-final.md` or version-suffixed copies. After an authorized move, verify affected links. Use relative references and exact source versions. In the default task directory, `../../technical-design.md` identifies the overall baseline; `technical-design.md` identifies the local design.

Keep one authoritative location per decision. Task designs link shared decisions rather than copying competing versions. Split additional solution designs only for substantial independent complexity or a clear boundary. Keep shared solution details at the change level and local evidence beside the task; link each from its owning design. Read before editing; preserve unrelated content and stable IDs. Do not create empty downstream artifacts.

Record exact product, overall-design (task mode), and code baselines. Include relevant uncommitted changes or state `Greenfield`. If the source has no explicit version, use a stable snapshot or revision. Requirements confirmed only in conversation need stable source references and explicit approval evidence. Do not invent rules to fill a template.

Use explicit artifact versions, starting at `v1`; increment for substantive changes. Revisions stay in the same file. Separate approval evidence from document and code versions.

Before revising or splitting a handed-off document, preserve the exact baseline and its supporting evidence through an accessible repository revision or immutable snapshot. If a snapshot is needed, use `history/technical-design/v<n>.md` relative to that design's directory, with supporting snapshots as needed. Reuse a matching reference; never overwrite different content at the same version. Record the prior baseline, approval evidence, reason, and resulting version in the questions file's Baseline and Feedback History.

When splitting an existing document, preserve record IDs, sources, states, dependencies, review attempt counts, and approval references. Verify moved content and links; retain forwarding anchors where existing references need them. Relocation changes no decision by itself. Carry forward review and approval only under the [record-only update rules](#review-and-approval-records); substantive changes still need affected review and applicable approval.

## Structure and content placement

Overall mode retains the ten sections of the overall template unless the user supplies another format. They are navigation anchors, not equal-length writing assignments. A section can point to its authoritative content elsewhere; omit unused subheadings and group inapplicable areas with a brief reason.

Both modes answer six questions at their selected depth. Use the template sections as locations, not separate copies of the same information.

| Required information | Overall location | Task location |
| --- | --- | --- |
| Scope, exact baselines, ownership, constraints, and acceptance references | Header; Sections 1–2 | Header; Scope and Inputs |
| Selected approach, rationale, and consequential tradeoffs | Section 4 | Implementation Approach |
| Boundaries, interfaces, data ownership, invariants, and critical failures | Sections 3, 5–6 | Implementation Approach |
| Requirement coverage and meaningful verification | Sections 3, 7 | Self-Test and TDD Plan |
| Dependencies and material uncertainty, with current impact and record links | Sections 5, 8 | Scope and Inputs; readiness summary |
| Current review, applicable approval, readiness, and next responsibility | Sections 9–10 | Review, Questions, and Readiness |

Task designs also identify affected code and local error handling. A short note can contain this information without all template headings. Reference shared decisions and priorities rather than repeating overall design.

Expand only applicable fields. Add interface detail when callers need an agreement, migration and restoration detail when state changes require it, and models when existing expression leaves a material ambiguity. Assess applicable risks before omitting fields; group material omissions with a reason. Do not require a separate “Not applicable” entry for every optional field.

Use the [modeling guide](uml-modeling.md) when selecting or revising models. Overall views belong in Section 5 or beside operational requirements in Section 6; task views belong with the approach. Keep quality priorities in Section 1, their tradeoffs in Section 4, and scenarios in Section 7. Apply the [quality goal method](design-methods.md#prioritize-quality-goals-and-resolve-tradeoffs) when these decisions are needed.

Write concise English unless the user requests another language. Follow [technical-writing](../../technical-writing/SKILL.md). Remove placeholders and instructional comments from completed artifacts.

### Keep the current design concise

Keep the main document focused on the decisions its reader must understand or act on now. Use this placement rule in both modes:

| Content | Placement |
| --- | --- |
| Current decisions, shared guarantees, key models, risks, and acceptance obligations | Main design at the selected scope |
| Q records, answers, dependencies between questions, investigation detail, and validation follow-up | `technical-design-questions.md`; link existing evidence rather than copying logs |
| Prior baselines, approval evidence, superseded decisions, and feedback dispositions | Questions file: Baseline and Feedback History; link retained revisions or snapshots |
| Review attempts, walkthrough traces, findings, corrections, and recheck evidence | `technical-design-review.md`, or the authoritative external review record |
| Local schemas, command syntax, parameter defaults, and detailed test cases | Responsible task design; retain early detail in overall mode only under the decision-depth rule |
| Dispatch IDs, issue-status instructions, Git delivery steps, and one-time replies | Handoff message or delivery record; keep only durable dependencies and next responsibility in the design |

Keep current assumptions, unresolved design effects, critical risks, and blocked stages/scopes visible in the main design. Link their Q or finding records beside affected content. Sections 8–9 and the task readiness summary state current impact; they do not repeat answers, review traces, or resolved findings. Apply confirmed conclusions to the solution, contracts, and verification obligations.

Use the saving rules above when moving records. If no task exists, keep useful local sketches as provisional supporting material with a downstream owner; do not imply assignment. Moving a record does not remove its blocker or evidence obligation.

State each rule or decision once. Elsewhere, link it and explain only the new implication. Prefer diagrams for relationships, flows, and states, and decision tables for condition/outcome combinations under the [modeling guide](uml-modeling.md). Keep rationale, constraints, and exceptions that those views cannot express clearly. Full product-rule restatements and repeated caveats add no coverage.

Revise current conclusions in place instead of appending each investigation or review round. Keep history accessible through its original record or a versioned snapshot. Use descriptive, directly openable links for evidence and approvals; an opaque ID alone needs a retrieval location. If the source is unavailable, state that limit rather than inventing a link or a verified conclusion.

## Decision depth and deferred work

Overall design resolves the decisions needed to divide responsibilities, identify dependencies, and coordinate tasks. Task design resolves the assigned feature or behavior before coding. Task mode owns feature internals by default; it covers more than helpers or parameter selection.

| Decision | Default scope |
| --- | --- |
| System and module boundaries, data ownership, major dependencies, and integration acceptance | Overall |
| Interface semantics and security, consistency, or compatibility guarantees that several tasks must share | Overall |
| Internal feature flows, complete schemas, field mappings, algorithms, storage structures, and provider protocols | Task |
| Libraries, timeouts, retry counts, pagination details, and other local configuration | Task |
| Test data, assertions, fixtures, and concrete Red → Green → Refactor steps | Task |

A shared contract contains only the decisions that other tasks or existing consumers must rely on. Name those consumers and their required agreement. A field, command, or schema may need an exact definition when consumers cannot coordinate without it. Being user-visible, important, or complex does not by itself make every detail a shared contract.

For local detail retained in overall mode, name the consumer or architecture decision that needs it now. Otherwise move it to the location defined above. Calling a long implementation sketch "nonbinding" does not justify keeping it in the overall body. Critical ordering, transaction guarantees, and failure semantics remain shared even when their implementation is deferred.

Investigate a task-level detail early only when it can change feasibility, an architecture decision, a shared guarantee, or a task boundary. State the affected decision and how different findings would change it. For example, a storage capability may determine whether the proposed atomicity guarantee is possible. Stop the investigation when that decision has sufficient evidence; do not continue into the feature's full implementation design.

Record downstream design by feature or module, with its accountable role, constraints, required evidence, and resolution point. Group related local choices instead of listing every future parameter. Planner assigns the developer. A choice that could overturn the architecture remains an explicit risk, not a routine deferral. Apply the [stage and scope rules](#questions-and-assumptions) to missing evidence; reuse existing authorization for any required investigation.

Task mode resolves its local approach against actual code and dependencies. Apply the [task readiness conditions](#task-handoff-to-code-development) for required architect review and the [status rules](#status-and-approval) for baseline changes.

### Stop overall design at planning depth

Move the named scope to review when its boundaries, interactions, shared contracts, dependencies, and integration acceptance support coherent planning. Resolve blocking architecture risks and assign remaining feature design with owners, constraints, evidence obligations, and resolution points.

Unfinished task internals do not keep that scope in `DRAFT`. Review and owner approval still precede [planning readiness](#overall-handoff-to-planner). Keep other blocked scope and dependencies explicit; a bounded review does not waive remaining product acceptance.

## Traceability and evidence

Preserve source Feature, rule, example, and Success Criteria IDs. Assign stable `C<n>` IDs to new technical contracts and `T<n>` IDs to planned tests when useful for traceability. Never renumber or reuse existing IDs. Qualify references by document when IDs occur in multiple artifacts.

Overall design accounts for every included product rule through one of these routes:

- A shared contract and its verification obligation for behavior that crosses task boundaries.
- A responsible feature or module, the product-rule reference, and a downstream design and verification obligation for local behavior.
- An explicitly accepted exclusion with its decision source.

Retain integration acceptance for outcomes that span features. Group rule references where ownership and obligations match. Do not invent a technical contract or repeat product behavior merely to give every rule a C ID. Local behavior still needs an observable verification obligation, not an owner name alone.

Task design maps assigned acceptance conditions to applicable shared contracts, the local approach, and concrete self-tests. It need not reproduce coverage for unrelated tasks.

A test can cover several contracts and vice versa. Inspect expected outcomes and assertions; ID lists alone do not establish coverage. Derive expected results from contracts rather than implementation. Keep existing tests, planned tests, unrun checks, failures, and actual passes distinct.

Separate current facts, proposed behavior, accepted decisions, assumptions, and executed verification. Cite sources, versions, commands or procedures, actual results, and limits as applicable. A failed probe does not establish that a system lacks the capability. Planned TDD steps do not establish Red or Green results.

### Connect decisions to scenarios, risks, and verification

For each consequential decision or quality claim, link its goal or contract, relevant scenario, supporting rationale and evidence, material risks or assumptions, and verification obligation. Explain why the evidence supports the conclusion and what it cannot establish; a list of IDs is insufficient. Where evidence is pending, retain the planned method, owner, required stage, and affected conclusion.

Use document-qualified IDs, section anchors, or existing ADR references. Reuse the authoritative scenario, question, finding, and execution records; no separate numbering scheme or duplicate evidence log is required. Keep risks and their dispositions in the existing question or finding records, or link an existing risk register. Record residual risk and its acceptance basis where applicable; a mitigation plan alone does not resolve it.

Keep these links beside the decision or claim, so a reader can follow it to the scenario and evidence. When a goal, decision, scenario, risk, or result changes, follow the links to reassess dependent conclusions, model views, tests, and readiness. Mark superseded evidence explicitly. Overall mode retains verification obligations; task mode refines them and links actual results when available.

## Questions and assumptions

Reuse the product-design [clarification protocol](../../product-design/references/discovery-methods.md#clarify-decisions-and-terms) for question types and states, and its [evidence requirements](../../product-design/references/document-contract.md#question-records). This contract owns technical placement and impact assessment; a product-level approval field does not replace technical stage/scope analysis.

Store full technical Q records in `technical-design-questions.md` using the [questions template](../assets/questions-template.md). Give new records stable `### Q<n>` headings; preserve existing IDs and qualify cross-document references. Link existing product or overall questions rather than copying them into a task record.

Each record identifies its applicable version and affected decisions, statement, dependencies, answer/evidence or missing fact, blocked stage and scope with reasons, supplier/owner, required evidence, and resolution point. Keep options, tradeoffs, and recommendation for user decisions. Preserve resolved/excluded records and reopening history. Use labeled fields for detailed answers rather than dense table cells.

For review-originated questions, link the finding in both directions. Questions own clarification; the review record owns verification of the correction. An answer or edit alone does not resolve a finding. Keep a concise impact statement and link in the main design while uncertainty affects its interpretation or readiness.

Distinguish architecture approval, task breakdown, task design, coding, acceptance, and activation when assessing impact:

| Unresolved item | Stage and scope to assess |
| --- | --- |
| Capability or security uncertainty that could overturn the architecture | Block the affected architecture decision and dependent work until the risk is resolved or the baseline changes through approval. |
| Feature implementation, parsing, or local configuration choice | Resolve in the responsible task before the affected coding step; block earlier stages only when the decision-depth rule requires it. |
| Missing login, credentials, samples, or test environment | Block checks that require the input. Identify any architecture decision that depends on those checks; unavailable access alone does not prove infeasibility. |
| Unmeasured quality, capacity, or recovery behavior | Set the required evidence and resolution point according to risk. It may gate architecture, implementation, acceptance, or activation; do not automatically apply the earliest gate. |

For example, if product behavior permits missing metrics, an unknown provider field can remain an adapter task obligation. It does not automatically block the shared archive. An unverified isolation capability can block the affected security design if no supported alternative preserves the required boundary.

Assess other scopes before declaring the whole change blocked. Independent work requires evidence that its inputs, interfaces, dependencies, and approvals remain valid. If independence is unknown, investigate that dependency rather than assume either global readiness or global blockage. Preserve the full product scope and all eventual acceptance obligations.

Use the product contract's [assumption validation method](../../product-design/references/document-contract.md#assumption-validation). Keep each material assumption and its current impact in the main design. Track outstanding validation as a linked fact-investigation Q in the technical questions file, with observation, collection method, disconfirming result, affected decisions, and owner. Routine authorized technical choices need no new permission; material tradeoffs beyond that authority require a decision.

## Status and approval

| Mode    | Status      | Meaning                                                                                  |
| ------- | ----------- | ---------------------------------------------------------------------------------------- |
| Both    | `DRAFT`     | Design content is incomplete at the selected depth, or a missing input, decision, or evidence item blocks that scope |
| Both    | `IN_REVIEW` | Design content is ready for review; required review or approval is pending               |
| Overall | `APPROVED`  | The human owner explicitly approved this exact version and named scope; cite the source and date |
| Task    | `READY`     | Task readiness conditions below are satisfied; no new human approval is implied          |

Assess blockers across the design and all applicable supporting records before stating readiness. A missing required or referenced record is an evidence gap; an unstarted file with no records to hold need not exist. Relocation or summary edits cannot close a question or finding.

Record readiness separately from status. An approved overall design can still have an evidence gap that blocks affected task breakdown. For mixed scopes, name the status and approval coverage of each; never imply whole-document approval from approval of a subset. Routine downstream design does not prevent overall review or approval under the stopping conditions above.

An `IN_REVIEW` task is not ready while required architect review is outstanding. Task `READY` applies to its declared scope and baselines, not to other tasks, changed code baselines, or release readiness. If an optional proposal conflicts with the baseline, record its separate blocked disposition. Original work can remain ready only with evidence that it does not depend on or adopt that proposal. Name the ready scope explicitly; an unqualified READY must not cover the blocked proposal.

Owner approval is required for product behavior and the overall technical solution before affected planning proceeds. A task design that refines choices within those approved baselines does not add an owner approval gate. Design approval and readiness do not themselves authorize implementation or external operations; apply existing task authorization.

If approved product behavior or shared technical decisions must change, reopen the affected overall design as `DRAFT` and follow the feedback loop below. A revised task design returns to `DRAFT` until its affected readiness conditions are reassessed; use `IN_REVIEW` when only the required review remains. Local task refinements update the task design and its review/readiness as affected; they do not automatically reopen the overall document. Typographic or link-index edits that change no decision preserve approval. Reassess source and code revisions before every handoff; do not silently adopt changed baselines.

### Review and approval records

The author owns design content. The reviewer owns the version-bound review report and finding dispositions. The human owner supplies approval; Project Manager links those records and assesses the next coordination step. A review report or approval record may be an accessible external artifact or workflow message with a stable reference, exact design revision, scope, author, and time. Preserve the evidence used if that source is revised.

Section 9 and the task readiness summary contain a compact current assessment. Store review attempts, walkthrough traces, findings, and rechecks in `technical-design-review.md` using the [review template](../assets/review-template.md), or link their authoritative external records. Include review scope/version, reviewer and independence, conclusion, open findings, material limits, and approval state; keep full review history in its authoritative record. Section 10 references this assessment instead of repeating it. An approval request can use the reviewed design revision plus its applicable review report; copying the report into the design is not an additional gate. Synchronize summaries during the next authorized maintenance or planning invocation without a separate record-only run.

Treat status and finding summaries in the file as a snapshot. When a later authoritative record changes them for the same revision, identify the stale summary, cite the superseding evidence, and state current readiness by scope in the handoff. Do not silently ignore contradictions. Missing, ambiguous, or inapplicable evidence blocks the dependent conclusion; a newer timestamp alone does not resolve it. Project Manager cannot close a specialist finding or grant approval.

Record-only updates do not change the design's substantive version. If their Git revision changes, retain the reviewed and approved revision. Before carrying evidence forward, verify that only records or their placement changed and that the linked artifact set preserves the reviewed meaning, scope, and evidence. This includes a verified split into supporting files; relocation alone is not a new approval gate. Substantive edits still require affected review and applicable approval. Reuse the existing reviewed revision when no record update is needed; never relabel old evidence as a review of new content.

## Overall handoff to planner

Set `Ready for task breakdown: Yes` only for an explicitly identified scope when:

- Owner approval covers the exact overall version and named scope, together with the included product baseline.
- Included product rules have coverage and verification responsibility under the traceability rules above, or accepted exclusions.
- Cross-task interfaces, data ownership, critical failures, dependencies, and integration checks support coherent assignment.
- No unresolved architecture or shared-design decision blocks that scope. Downstream feature design has owners, constraints, evidence requirements, and resolution points before dependent coding.
- Review findings have dispositions and no applicable approval or breakdown blocker remains.

Output the change directory, document paths and versions, included rules and contracts, ownership boundaries, candidate behavior increments, dependencies, integration acceptance, and downstream design obligations. Candidate increments guide planning; they are not assigned tasks. An assigned task can start its feature design without a complete implementation specification from overall mode.

Report planning readiness separately for each materially different scope, including scope with pending approval. Give the applicable approval reference, `Yes / No`, blocker IDs, dependency reason, and next action. Keep remaining product scope visible. A whole-change `No` must not replace this assessment when independent scope could proceed. Do not declare a subset ready without its required approval and evidence of independence.

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

Apply the supplied reviewability policy using the team's [planning methods](../../planner/references/planning-methods.md#estimate-work-and-review-scope). That reference owns scope assessment and advance-review agreement. Return unmanageable scope or missing review arrangements to `planner` before affected implementation; do not assign replacement tasks here.

During implementation, update task decisions when new evidence changes the approach, before dependent coding continues. Reassess affected self-tests and review. Independent code review, integration, QA, and ship approval remain downstream obligations.

## Feedback and revisions

A constraint or decision request is a valid design output before a forward deliverable is complete. Every handoff contains scope/task and input versions, design and existing supporting-record references, conclusion and evidence, unresolved issues, and next function with its accountable recipient. Supply unchanged information through the [handoff reference method](../../project-manager/references/coordination-contract.md#handoff-by-reference) when applicable. State mode and readiness; do not equate completion of design work with downstream acceptance.

For feedback, also record a stable issue identity, affected requirements/contracts, the constraint, observations versus estimates and uncertainty, impact, alternatives and tradeoffs, and the requested decision or missing fact. Say when no alternative is known. Without a supplied cost or complexity limit, request a tradeoff decision instead of inventing a threshold or declaring impossibility.

Route product scope, behavior, or acceptance changes to PM using `product-design`. Route shared architecture and interface changes to the architect using overall mode. Route task-boundary or assignment problems to engineering lead using `planner`. Local implementation corrections stay with the developer using task mode or `code-development`, as appropriate. Project Manager tracks these handoffs through `project-manager`; missing routing tools do not authorize app operations.

Keep affected work blocked until applicable decisions, approvals, and evidence are current. Identify downstream plans, tasks, interfaces, code, cases, and conclusions needing reassessment. Preserve prior versions and decisions as history. Independent work can continue only when its inputs, interfaces, dependencies, and approvals remain valid; uncertainty about impact is not proof of independence.

A revised product version needs owner approval before renewed overall design; changed overall decisions need technical approval before affected planning resumes. Recheck affected task designs before coding resumes. A local task update within approved constraints needs only its applicable review and readiness check.

Close feedback with supported specialist resolution or an explicit owner decision to defer or stop the affected scope. Approval alone does not prove feasibility. Deferral does not mean delivery. If the same issue returns on the same baseline without new evidence or a viable alternative, stop repeating the handoff. Escalate through Project Manager with attempted options, consequences, and the missing decision; keep affected work blocked.
