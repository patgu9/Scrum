# Planning methods

Use the [plan contract](plan-contract.md) for required inputs, fields, and readiness. This reference owns how to derive and review the plan.

## Five-step decomposition

Use these steps to derive tasks from approved baselines. Revisit earlier steps when a candidate exposes a gap. Keep routine work brief; do not create separate methodology documents or force multiple options for an obvious small change.

| Step | Method | Result |
| --- | --- | --- |
| 1. Understand the goal and flow | Existing requirements; Story Mapping when useful | Required user paths and scope |
| 2. Clarify behavior boundaries | Example Mapping | Rules, concrete examples, and unresolved questions |
| 3. Generate candidate splits | Vertical slices and SPIDR / story splitting patterns | Candidate boundaries with reasons |
| 4. Check task quality | INVEST / SMART and Small CLs | Complete, actionable, reviewable tasks |
| 5. Check combined scope and order | WBS coverage principle and dependency analysis | Full coverage, dependency order, and integration responsibility |

These methods serve different purposes. Story splitting finds candidate boundaries; quality checks assess them. A user story describes user-visible behavior. A development task can also deliver a shared contract, migration, or necessary refactor.

## 1. Understand the goal and flow

Read the product rules and examples alongside the overall design's contracts, verification strategy, candidate increments, and deferred decisions. Inspect relevant code and existing work before creating tasks. A candidate increment is a planning input, not an assignment already made.

Identify the user, intended outcome, and required path through the system. For a broad flow, reuse an upstream Story Map or outline activities and their variations in narrative order. Select a thin path that still completes the intended goal. A short path description is enough for a small change. For technical work, name the downstream consumer and observable engineering outcome.

Record the path and source references in the plan. Changing approved scope or release commitments requires feedback to the product owner; a proposed slice does not authorize that change.

## 2. Clarify behavior boundaries

Use Example Mapping to connect the intended behavior to rules, concrete examples, and unresolved questions. Reuse source IDs and examples. Add normal, boundary, or failure examples only where they clarify a candidate boundary; distinguish inferred examples from approved behavior.

Check that each example has a setup, action, and observable expected result. Group examples by the rule or variation they exercise. Do not turn every rule or example into a separate task. If the result is unknown, record the question, affected stage, supplier, and required decision instead of inventing acceptance.

Carry scenario references into task acceptance. Keep cross-task questions in the plan and task-local blockers in their task records. Missing product behavior returns to PM; unresolved shared contracts or feasibility return to the architect.

## 3. Generate candidate splits

Choose the smallest complete change that a reviewer can understand and verify against its declared dependencies. Prefer behavior increments when they fit the approved architecture. A shared contract, migration, or necessary preparatory refactor can be its own task when it has a verifiable outcome and explicit downstream consumers. Do not force every change into one layer-based task or require each task to deploy independently. Each integrated increment must preserve a working system; a later task cannot be required to repair an intentionally broken build.

Find the main source of complexity, then reduce the variations through it. SPIDR stands for Spike, Paths, Interfaces, Data, and Rules. Use these prompts and related story splitting patterns to find useful alternatives:

| Pattern | Question to find a boundary |
| --- | --- |
| Paths and workflows | Can one complete user path work before adding alternate paths? Keep the steps needed to reach its outcome together. |
| Interfaces | Can one interaction channel or platform work before another? This means user entry points, not frontend/backend layers. |
| Data | Can one format, source, or data category be supported before the others? |
| Rules | Can distinct business-rule variations be implemented separately without weakening the rules applicable to each slice? |
| Operations and simple/complex cases | Does a broad verb such as “manage” hide separate outcomes? Can a complete simple case precede a richer case? |
| Spike | Is a specific unknown preventing a supported split? Request a bounded investigation with a question, evidence target, time limit, owner, and decision to revisit. |

Use a spike when the other patterns cannot resolve the uncertainty. Route it through the existing authorized investigation workflow. Keep dependent assignment blocked when feasibility or a shared decision is unresolved. An investigation produces knowledge, not completed functionality; it does not bypass the development-task contract.

For nontrivial scope, compare materially different candidate boundaries when available. Consider complete outcomes, early feedback, risk reduction, dependency cost, and review context. Record the selected split and why the alternatives fit less well. For a small change or only one viable split, record the reason without inventing options. Keep rejected candidates as brief plan notes, not assigned task files.

Preserve required permissions, validation, consistency, and failure handling within each slice. A later task may add another supported variation; it cannot repair a required guarantee omitted from an earlier slice. Preserve all approved scope across the selected tasks or record an accepted exclusion.

Keep required implementation, tests, and documentation together for the same goal. Separate unrelated improvements even when their combined diff is small. A dedicated test-infrastructure task is appropriate only when it delivers a distinct prerequisite; it cannot be used to postpone required verification from an implementation task.

Avoid splits that remove essential context. Keep a new interface with enough usage to assess its contract; reference existing or already reviewed dependencies. Separate substantial refactoring, renaming, or formatting from behavior changes when possible. A small local cleanup can remain when it clarifies the same change without hiding behavior. Do not add speculative abstractions merely to manufacture smaller tasks.

Carry the overall design's Red → Green → Refactor obligations into task verification scope. Task design chooses concrete test steps; development supplies executed evidence. Do not report a planned failure or pass as an observed result.

Describe required changes and likely modules at the level needed to estimate and assign work. Leave private implementation choices to task-mode `technical-design`. Carry each deferred decision's constraints, evidence requirements, and deadline into the receiving task. Resolve missing feasibility or shared-contract decisions upstream before affected assignment.

### Example: compare import boundaries

This is a hypothetical comparison, not an approved scope or executed result. Suppose the approved change supports CSV and JSON imports, each for creating and updating records.

| Candidate | Assessment |
| --- | --- |
| Separate UI, parsing, storage, then tests | Leaves behavior and verification disconnected. Rework the boundaries unless a distinct prerequisite has its own outcome and consumers. |
| CSV creation; CSV update; JSON creation; JSON update | Uses operation and data variations. Each task includes its applicable validation and tests; declare shared dependencies and combined integration checks. |
| All creation formats; then all update formats | Can fit when formats share reviewed infrastructure and update semantics dominate the complexity. Compare actual code and review scope before choosing. |

Do not always choose the same pattern. Record which complexity and dependency evidence supports the selected boundaries.

## 4. Check task quality

Use INVEST for behavior slices and SMART for all development tasks. Apply them as questions, not a score or a new approval gate:

| Check | Apply to the candidate |
| --- | --- |
| INVEST: Independent, Negotiable, Valuable | Minimize avoidable overlap and ordering constraints; keep useful outcomes. Negotiate local choices within approved baselines. Explicit dependencies remain valid. |
| INVEST: Estimable, Small, Testable | Explain effort and uncertainty; keep a manageable outcome with observable acceptance. Missing evidence calls for clarification, not a fabricated estimate. |
| SMART: Specific, Measurable, Achievable, Relevant | State the change and completion evidence; check capability and prerequisites; link the work to the approved goal or a necessary consumer. |
| SMART: Time-boxed | Use an agreed duration or checkpoint to detect overrun and trigger help or replanning. Record unknown timing and its supplier; do not invent a deadline or add a timing-only readiness gate. |

Technical prerequisites need a verifiable engineering outcome and downstream consumers; they need not directly deliver a user story. Google's Small CLs guidance concerns small changelists. Use the assessment below to apply it to task PRs, including tests and necessary context.

### Estimate work and review scope

Estimate task design, implementation, and verification together. Explain the basis and uncertainty using affected behavior, modules, tests, integration needs, and current code. Use ranges or qualitative effort when precise estimates lack support. Do not manufacture schedule commitments or line counts.

Split work into small, complete task PRs and assess reviewability in context. This team has no default numerical limit or automatic line-count exception.

Assess reviewability across these dimensions. Explain only the factors material to the task; a routine task needs a short rationale, not a scoring exercise.

| Dimension       | Planning question and action                                                                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Goal            | Can the task deliver one clear outcome? Separate unrelated goals.                                                                                                        |
| Context         | Can the reviewer understand the change from its diff, description, repository, and reviewed dependencies? Include missing usage or return unresolved contracts upstream. |
| Footprint       | How many files, modules, owners, and interfaces must be understood together? A small scattered diff can require substantial review.                                      |
| Behavioral risk | Which invariants, permissions, concurrency paths, data transitions, or failure modes need careful reasoning? Name appropriate review expertise and supporting checks.    |
| Verification    | Do required tests and documentation accompany the behavior? Can each integrated increment work correctly without a later repair?                                         |
| Simplicity      | Does the approach add avoidable indirection or speculative behavior? Prefer a simpler valid approach and split separable preparatory work.                               |

Plan for reviewers to examine all assigned authored changes, including tests, with enough surrounding code to understand behavior. Different reviewer assignments can cover different areas, but their combined coverage must include the whole change and its interactions. Mark missing expertise or context as a gap; additional Agent names alone do not establish coverage.

#### Report estimated and actual scope

Include these measures in the scope report:

- Authored additions plus deletions in implementation, tests, and documentation, including Agent-written content.
- Reproducible generated changes, reported separately with generation and validation context.
- The total diff, with binary and other non-text changes kept visible.

Count deletions as observed even when their review cost is low. Google permits treating whole-file deletion as cheap to review; record that judgment separately instead of changing the raw count. AI authorship alone does not make maintained code a reproducible generated artifact or excuse reviewing it.

Label planning figures as estimates. At review submission, the developer reports the actual base-to-head scope, changed files, behavioral risks, and verification evidence. Neither a low count nor a large model context window proves reviewability. Never hide changes or omit required tests to make a diff appear smaller.

#### Decide whether to split

Use these dispositions when planning and reassessing work:

- **Suitable:** One complete goal, understandable context, and manageable review effort. Proceed through the ordinary task workflow; this is not code-review acceptance.
- **Split:** Separate outcomes or excessive combined complexity can be reduced. Define smaller tasks, preserving acceptance coverage, tests, working increments, and dependencies.
- **Clarify:** Missing context or evidence prevents a supported judgment. Identify the supplier and block only affected work.
- **Advance review agreement needed:** An unusually large or complex cohesive change remains after meaningful split options are assessed. Follow the agreement procedure below.

For advance review agreement, record why the scope remains cohesive, alternatives considered, affected scope, review responsibilities, and validation strategy. Obtain the independent Code Reviewer's agreement to undertake that scope before implementing it. If the need is discovered mid-task, stop expansion and obtain agreement before continuing affected coding.

A pending advance agreement can leave assignment or local design possible, but it blocks implementation of the proposed large scope. It is a specialist review commitment, not a new human approval gate or acceptance of unseen code. If a large PR already exists, retain it and resolve scope before review acceptance. Reviewer rejection returns it to engineering lead for decomposition or clarification. No agreement permits unrelated goals, missing required checks, or blocking defects.

Code Reviewer can reject an unmanageable change regardless of line count. Scope, baseline, or diff changes require current evidence and reassessment of affected agreements and review conclusions. Seek a maintainable improvement, not perfection or compliance with personal preferences. Optional polish alone does not force more tasks; required correctness, acceptance, and project conventions remain binding.

This workflow's assignment roles, independent Agent review, raw counting, readiness fields, and approval gates are local policy. Do not present them as Google's exact process. If an explicit project rule conflicts with this default and its authority is unclear, identify the conflict instead of silently replacing it.

#### Boundary examples

These are hypothetical planning examples, not executed results:

| Input                                                                                               | Planning consequence                                                                                                                            |
| --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| A cohesive change grows from 500 to 501 authored changed lines without new behavior or dependencies | Refresh the scope report; the extra line alone changes no review disposition.                                                                   |
| A 200-line diff spans 50 files and several ownership boundaries                                     | Assess interactions and review expertise; split separable work or clarify context despite the small count.                                      |
| 120 lines combine invitation validation and unrelated billing cleanup                               | Split the goals despite the small diff.                                                                                                         |
| A new API is separated from every usage merely to shorten its diff                                  | Include enough usage and related tests for a meaningful review; avoid an incomplete artificial split.                                           |
| 180 authored lines plus 2,000 reproducible generated lines                                          | Report 180 authored, 2,000 generated, and 2,180 total; keep generation/validation and review burden visible.                                    |
| An Agent writes 900 maintained source/test lines                                                    | Count all 900 as authored; judge actual behavior and complexity. Neither automatic exemption nor numerical rejection applies.                   |
| A trusted refactoring tool performs a broad mechanical rename                                       | Consider a separate change with transformation evidence and regression checks; confirm review coverage rather than mixing new behavior into it. |
| A whole-file deletion removes 1,200 obsolete lines                                                  | Report the actual deletions; check remaining references and behavior. Low reading effort does not prove removal is safe.                        |
| A cohesive change remains unusually complex after reasonable split options                          | Seek advance reviewer agreement on scope and review responsibilities before affected implementation; retain all verification obligations.       |

## 5. Check combined scope and order

Apply the Work Breakdown Structure (WBS) coverage principle: the selected work must cover the approved parent scope without omissions or duplicate implementation responsibility. Use the existing coverage map; a separate WBS artifact is unnecessary. Include supporting work such as migrations, compatibility, tests, and documentation when required. Keep QA, Ops, and other downstream obligations with their responsible functions rather than turning every delivery activity into a developer PR.

Build a coverage map from each included product rule and technical contract to task acceptance and verification responsibility. Retain accepted exclusions with their source. Check expected outcomes rather than merely copying ID lists. Include integration obligations that span tasks and name the role responsible for verifying them; several locally passing tasks do not establish end-to-end acceptance.

Walk through the user path from step 1 using the combined tasks. Check that every required behavior and failure case has an owner. Shared verification may span tasks, but its responsibility and prerequisites must be explicit. If coverage or sequencing fails, revise the candidate boundaries and repeat affected quality checks.

### Sequence dependencies and assignments

For each dependency, name the required outcome, artifact or version, evidence of its current state, and stage it blocks. Distinguish:

- A shared decision that must be settled before assignment.
- A predecessor contract or code change needed before design or coding.
- A declared review base that permits a focused dependent diff under project Git policy.
- A predecessor that must be accepted into the integration baseline before merge.

Check for cycles, missing predecessors, incompatible interfaces, and overlapping ownership. Resolve a cycle by revising task boundaries when that preserves the approved design. Return a shared-design conflict to the architect. Do not invent a new interface to make the task graph acyclic.

Sequence work from actual prerequisites and available developers. Assign one accountable developer per task using known capability, availability, and workload. If that information is absent, mark the task `Unassigned` and request it from the supplier. Do not invent developer identities or treat concurrent assignment as a guarantee of parallel progress.

For proposed parallel work, state the independence basis and any shared-file or integration constraints. Unknown overlap remains an issue to resolve. The plan describes ordering; it does not schedule runtimes or switch worktrees.

Record the repository and declared Git base/target from project policy and current evidence. If a future prerequisite revision does not yet exist, describe its required acceptance condition and keep dependent readiness restricted. At claim or resumption, the developer checks the actual baseline and existing branch through the Git workflow. Updating the base later requires affected scope and evidence reassessment.

## Review the plan

Review the full plan before handoff; after a narrow revision, also inspect affected coverage, dependencies, and readiness. Use the shared [document validation method](../../technical-writing/references/validation-guide.md) and complete the [writing passes](../../technical-writing/references/writing-guide.md#edit-in-separate-passes).

1. **Inputs:** Verify accessible source versions, owner approval evidence, overall readiness, and current repository facts. Compare against the prior plan on a replan.
2. **Coverage:** Trace the required user path, rules, contracts, and concrete examples to observable acceptance and verification responsibility, or an accepted exclusion. Check combined outcomes, supporting work, and duplicate responsibility.
3. **Task boundaries and quality:** Check candidate comparisons and selection reasons, scaled to scope. Apply INVEST/SMART and Small CLs checks, including complete goals, context, working increments, Git baselines, and full effort estimates. Record a supported reviewability disposition; check required advance agreement before affected implementation.
4. **Dependencies and ownership:** Check ordering, cycles, external prerequisites, developer availability, deferred decisions, claim evidence, and actual branch/PR reuse where applicable. Distinguish claim, coding, and merge blockers. A plan-index summary cannot establish exclusive claim ownership.
5. **Revisions and evidence:** Ensure split/replacement tasks preserve lineage and coverage; stale conclusions are marked for reassessment. Planned tests and estimated diffs cannot appear as passes or actual counts.
6. **Readiness and handoff:** Open each task from its plan-index link. Verify a unique standalone entry point, matching task ID/version, plan backlink, pinned input references, dependency links, and agreement between the task and its index summary. Reassess readiness, name blockers and recipients, and remove template prompts. Do not add links to unproduced task designs or PRs.

If the plan has ready tasks, walk through at least one using only its entry file and linked prerequisites. Cover assignment, confirmed claim, branch creation, task design, implementation, review, and integration prerequisites. This is a text review; do not execute those stages. Preserve QA and ship gates after integration.

For a blocked or revised plan, also trace the affected return and resumption conditions. Check that a superseded task cannot be mistaken for available work and that replacement links preserve scope.

Record reviewed plan version, review type, checks actually performed, findings and their dispositions, and remaining limits in the plan. Self-review remains self-review. A mechanical package check, a paper walkthrough, and a real downstream trial establish different evidence; report only what occurred.

## Method sources

The five-step sequence adapts these sources to this team's approved-baseline and task-PR workflow. It does not adopt every source's process or sizing advice.

- [Jeff Patton: Story Mapping](https://jpattonassociates.com/wp-content/uploads/2015/03/story_mapping.pdf) — user paths and complete delivery slices.
- [Cucumber: Example Mapping](https://cucumber.io/docs/bdd/example-mapping/) — rules, examples, and questions.
- [Humanizing Work: Story Splitting](https://www.humanizingwork.com/the-humanizing-work-guide-to-splitting-user-stories/) and [Mike Cohn: SPIDR](https://www.mountaingoatsoftware.com/agile/five-simple-but-powerful-ways-to-split-user-stories) — candidate boundaries and sources of variation.
- [Bill Wake: INVEST and SMART](https://xp123.com/invest-in-good-stories-and-smart-tasks/) — story and task quality checks.
- [Google: Small CLs](https://google.github.io/eng-practices/review/developer/small-cls.html) — cohesive changes, review context, and related tests.
- [PMI: Developing Work Breakdown Structures](https://www.pmi.org/learning/library/developing-elaborating-work-breakdown-structures-7241) — complete scope coverage.
