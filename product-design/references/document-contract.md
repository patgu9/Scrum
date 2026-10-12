# Design Doc contract

This contract defines the Design Doc's structure, content, saving, structural validation, and approval. Use the [template](../assets/design-doc-template.md) for the output format. Follow the [skill entrypoint](../SKILL.md) for the workflow and the [Technical Writing Skill](../../technical-writing/SKILL.md) for writing methods.

## Inputs and invocation context

Accept a goal, available context and constraints, user answers, and any downstream feedback with its affected product baseline. Discovery can start with an incomplete goal. Investigate available facts and record missing product decisions through the clarification protocol.

For a continuation or feedback request, read the referenced artifacts and check their versions and approval evidence against the requested scope. Missing, inaccessible, conflicting, or stale required input blocks dependent work. Report what is needed, who can supply it, and the affected work. Continue only work whose inputs remain valid; do not reconstruct an approved baseline from memory.

Use the caller's established workflow. In a team workflow, PM owns product discovery and artifacts; Project Manager routes handoffs and submits approval requests to the human owner. In standalone work, deliver directly to the user. Ask about the route only when the supplied context is ambiguous and the answer affects the next handoff. This context is separate from Startup / Builder discovery mode. Platform commands and record transport belong to the caller's platform Skill.

## Saving

Follow the shared [task artifact layout](artifact-layout.md) for directory selection, filenames, and revisions. Save the product document as `<project-root>/doc/YYYY-MM-DD-task-slug/product-design.md`.

Before saving:

1. Resolve the project root if it is unclear.
2. Select the task directory and read its existing product document, if present.
3. Resolve conflicts with unrelated files before replacing content.

Keep the glossary, decisions, and review findings in the same product document. Supply its path and task directory in the handoff summary.

## Structure

Keep the heading order and spelling below. Repeat only the Feature block. Do not add a preface, appendix, extra headings, or metadata fields by default.

```text
## Design Doc : <title>
- Status: DRAFT | IN_REVIEW | APPROVED
- Version: v1
- Approval: Pending
- Mode: Startup | Builder
- Date: YYYY-MM-DD
- Stage: Think

### Glossary
### Background
#### Problem Statement
#### What Makes This Cool
### Solution Design
#### Approaches Considered
#### Recommended Approach
#### Success Criteria
### Requirements
#### Feature <stable number> — <capability>
##### User Story
##### Rules
##### Key Examples
```

Define each Feature as a useful capability, not a technical layer.

Keep the template's labels, table headers, and column order. Only **Constraints** and **Boundaries and Dependencies** are optional.

Replace placeholders with content. Remove instructional comments. Preserve proper names, identifiers, and source links. Link every unknown marked TBD to an open question.

## Feature rules

Write each User Story in value → role → action order. Link the User Story to defined Success Criteria (SC) IDs. Use agreed terms and concrete cases to clarify business rules that affect users.

Give each rule an `F<n>-AC<m>` ID. Give each example an `F<n>-E<m>` ID. Keep existing IDs when revising or reordering content. Never reuse a deleted ID.

Give every defined rule an example with facts, an action, and an observable result. Cover boundaries and exceptions that distinguish behavior. Never invent policies or expected outcomes.

Link pending rules or outcomes to open questions. Apply [Status and approval](#status-and-approval). Examples describe intended behavior. They do not prove that tests ran or demand exists.

Use tables by default for comparable cases. If narrative examples are clearer, use the Given/When/Then format below. Use one format for the examples; do not duplicate both. Keep each example's full ID and references to applicable rules:

```markdown
**F1-E1: Scenario name**
- **Related Rule:** F1-AC1
- **Given:** Concrete context and input.
- **When:** Business action or event.
- **Then:** Observable result.
```

## Content placement

| Content | Location |
|-----|-----|
| Problem, actors, workaround, demand, and sources | Problem Statement and Evidence |
| Defined terms and their boundaries | Glossary |
| Ways to achieve the same goal. Benefits, drawbacks, effort (S/M/L/XL), risk (Low/Medium/High), reuse, and reasons for rejecting an approach | Approaches Considered |
| Selected approach and reason, or a choice marked as pending | Recommendation |
| Goal → actor → behavioral impact → deliverable links. Trigger, handoffs between actors, outcome, how the product reaches users, and shared dependencies | How It Works, including diagrams |
| Initial audience, smallest useful outcome, included Features, exclusions, and costs of future changes where relevant | Scope |
| Premises, assumptions, Q records, dependencies, and unresolved review findings. Approval impact, validation plan, decisions to revisit, and follow-up | Premises and Open Questions |
| Prior product baselines and approvals, reasons for revision, and downstream feedback dispositions | Premises and Open Questions, with links to retained evidence |
| Outcome and verification method. For quantitative goals: baseline, target, units, population, and time window | Success Criteria |
| Value → role → action, SC links, rules, and acceptance examples | Feature blocks |
| One action and observable result. For Startup: validate demand or a critical assumption. For Builder: try a usable outcome | Next Action |

Record uncertainty about causal links in Premises and Open Questions. Every row needs `Blocks approval: Yes / No` and a reason. Do not add separate sections for impact maps or review findings to the Design Doc.

### Question records

Store records from the [clarification protocol](discovery-methods.md#clarify-decisions-and-terms) in the existing four columns. Keep the headers. Do not add sections to the Design Doc for question records.

- **Type:** Give the stable question ID, question type, and question state. Example: `Q3 / User decision / OPEN`. Keep existing types for premises and assumptions that are not questions.
- **Statement and Impact:** State the question, its impact, and affected IDs or fields. Give `Depends on: Q1, Q2` or `None`. Include any conditions on those dependencies. Add `Blocks approval: Yes / No` and the reason.
- **Evidence / Validation Status:** Start with the answer or finding, its basis, and source. Use `Pending` or `Unknown` when the answer or evidence is missing. For user decisions, also record the main options, tradeoffs, recommendation, and reason. Fact investigations need no option comparison.

  Cite the conversation turn or quote the user's answer. Support investigated facts with file or tool evidence. For a reopened question, keep the prior answer and the reason for reopening. Agreement does not prove a factual assumption.

- **Follow-up:** Give the next investigation, clarification, or validation action. State the required evidence, affected content awaiting review, and an owner when needed. For `EXCLUDED`, record the user's agreement to exclude the scope. Use `None` only when no follow-up remains.

Keep resolved and excluded question rows, their IDs, and the basis for each state. Put Q IDs beside pending or disputed content so readers can trace dependencies. The clarification protocol governs question states and transitions. [Status and approval](#status-and-approval) governs the document Status.

### Assumption validation

For each assumption that materially affects value, scope, or the chosen approach, use these existing fields:

1. **Evidence / Validation Status:** State what to observe, how to collect observations, and which result would not support the assumption. Use an agreed threshold or concrete qualitative counterexample. If the method or threshold is unresolved, record an open decision. Do not invent either.
2. **Follow-up:** Name the decisions and affected IDs to reopen if that result occurs. Include the next validation action and an owner when needed.
3. Link relevant Success Criteria for measurement context. Do not repeat that context in these fields.

Next Action identifies one concrete validation or trial step. It need not cover every assumption. Approval does not remove outstanding validation work.

## Versions and approval evidence

Use `Version: v<n>`, starting at `v1`. Increment the version when substantive changes alter a product version already handed off for review, approval, or downstream use. Work in progress may retain its version until that handoff. Typographic changes alone preserve the version.

Before changing a handed-off version, retain its exact content through an accessible repository revision or an immutable snapshot at `history/product-design/v<n>.md` within the task directory. Reuse an existing matching reference; never overwrite a different snapshot at that version. Historical snapshots are evidence, not competing current documents. Record the prior version, reference, approval evidence, and reason for revision in Premises and Open Questions. The current `product-design.md` remains authoritative.

Keep `Approval: Pending` for DRAFT and IN_REVIEW. For APPROVED, use `Approval: <version> | <YYYY-MM-DD> | <human approver> | <evidence reference>`. The version must equal the current Version. Cite the actual approving message or decision record; preserve its explicit scope. Approval relayed by Project Manager must identify the human decision, not the coordinator's own conclusion. An unavailable or ambiguous approval record blocks approved handoff.

When revising an older document without version fields, identify and retain the source revision first. Add `v1` for the newly tracked document; do not invent earlier versions or approval evidence. Preserve APPROVED only when evidence covers the exact content; otherwise record the uncertainty and seek confirmation through the applicable route.

## Status and approval

- **DRAFT:** Discovery is incomplete or issues still block approval. Record unknowns when the user skips questions. Proposals and silence do not establish decisions or approval.
- **IN_REVIEW:** The document is complete, the direction is agreed, and no approval blockers remain. Deliver it for confirmation through the route below.
- **APPROVED:** The user explicitly approved this version. Blockers are resolved or the user agreed to exclude affected scope. Approval does not validate assumptions.

Questions about core users, scope, or behavior block approval unless the user agrees to exclude the affected scope.

If goals, scope, rules, or outcomes change materially:

1. Preserve the prior baseline, update Version as required above, set Status to DRAFT, and reset Approval to Pending.
2. Obtain the user's product decision unless the change is already authorized. Authorization to revise is not approval of the resulting version.
3. Check affected terms, Success Criteria, User Stories, and examples.
4. Set IN_REVIEW when the document is complete and no approval blockers remain.

Typographic edits alone preserve approval.

In team work, send the approval request and exact product version to Project Manager for submission to the human owner. PM may clarify business decisions with the owner but does not take over cross-role approval routing. In standalone work, request approval directly from the user. Record explicit approval before handing the version to technical design. Approval neither proves feasibility nor authorizes implementation.

## Handoff summary

Every invocation delivers a summary plus references to its professional artifacts, including when blocked or returning feedback. Put the summary in the caller's delivery record or response, outside the product document's fixed structure. Keep it platform-independent; transport is the caller's responsibility.

Include:

- **Task and inputs:** Task identity and directory; input artifacts and exact versions, applicable approval references, and feedback identity. For a new goal, cite the supplied request rather than inventing an input version.
- **Outputs:** Product document path and Version, or the feedback response and its affected baseline. Link supporting artifacts rather than copying them.
- **Conclusion:** Discovery incomplete, awaiting approval, approved for technical design, or feedback/blocker. State the document Status and approval evidence separately; completing this invocation does not establish downstream acceptance.
- **Evidence:** Structure and final-review results, review coverage and attempt count, investigated evidence and its limits. Follow the shared [validation reporting rules](../../technical-writing/references/validation-guide.md#report-the-result). Include relevant environment, actual tool results when used, and required checks that were not run. Planned examples and checks are not execution evidence.
- **Open items:** Stable question/finding IDs, dispositions, affected product rules, missing information, and who can supply it. Preserve feedback identity through revisions.
- **Next handoff:** Next function, responsible recipient, requested action, and prerequisites. In team work, address Project Manager and identify the intended specialist or human decision; in standalone work, address the user. An approved forward handoff names `technical-design` in overall mode and the recipient holding the Architect responsibility. Project Manager routes the team handoff. Engineering lead can hold this responsibility.

For a feedback response, include the content required by [revisit a product baseline](discovery-methods.md#revisit-a-product-baseline). A blocker or a request for evidence is a valid delivery; it does not require a completed product revision.

## Document language

Write the Design Doc in plain, concise English. Follow the [Technical Writing Skill](../../technical-writing/SKILL.md) for every section, table, rule, and example. Keep the required structure and content placement. Do not add conversation progress updates or text before the title.

Put essential reader context in Problem Statement and Glossary. Put boundaries in Scope. State reader prerequisites in these locations only when they affect understanding. Keep the selected direction in Recommendation and diagrams in How It Works. Do not add audience metadata or new sections by default.

Within each assigned location, answer the reader's main question first. Then give the necessary reason or evidence. Explain concepts before using them in rules or examples. Use short labeled statements in dense table cells. Keep decisions, evidence, dependencies, and follow-up distinct. Preserve every required field and unresolved question.

## Final review

1. **Value and scope:** Make sure a reader can understand the document without the conversation. Check the problem, evidence, actors, and intended change in behavior. Check the smallest useful outcome, alternatives for the same goal, uncertainty in estimates, and the user's chosen approach. Mark hypotheses. Distinguish current from desired behavior.
2. **Journey and language:** Check terms, triggers, handoffs between actors, dependencies, how the product reaches users, and outcomes across Features. Complete the Technical Writing Skill's [editing passes](../../technical-writing/references/writing-guide.md#edit-in-separate-passes).
3. **Verifiable behavior:** Link each User Story to valid Success Criteria. Link every defined rule to concrete examples. Check units, boundaries, exceptions, and what stays unchanged.

   For quantitative goals, check metric definitions and measurement context. Explain how to obtain missing baselines. Builder may use a qualitative demonstration.

   For each important assumption, check what to observe and how to collect observations. Check which result would not support the assumption and which decisions to reopen. Examples of intended behavior alone do not validate assumptions.
4. **Decisions and approval:** Check question records, sources for resolved answers, dependencies, unanswered questions, and content awaiting review. An empty question queue does not prove that approval blockers are resolved. Apply [Status and approval](#status-and-approval) to the current version and its unresolved questions.
5. **Completion:** Check that Next Action is concrete, the handoff summary identifies valid inputs and the next recipient, and the work stays within the entrypoint's scope. For revisions, check retained baselines, current approval evidence, and feedback disposition.

## Structural validation

Use the shared [document validation method](../../technical-writing/references/validation-guide.md). Check the document directly against this contract and the applicable template:

1. **Format:** Heading order, metadata values, required labels, table headers and complete rows, and populated sections. Remove template placeholders and instructional comments. Apply the user's replacement template when supplied.
2. **Identifiers and coverage:** Unique, stable Success Criteria, Feature, Rule, and Example IDs. Each User Story links to defined Success Criteria. Each example links to valid rules and contains Given, When, and Then. Every defined rule has an example.
3. **Questions and status:** Q IDs, question states, dependencies, TBD links, and explicit approval blockers. Check consistency with the [clarification protocol](discovery-methods.md#clarify-decisions-and-terms) and [status rules](#status-and-approval).
4. **Versions and handoff:** Current Version and Approval fields, retained baselines and accessible approval evidence, and required handoff-summary fields. Apply [versions and approval evidence](#versions-and-approval-evidence) and [handoff summary](#handoff-summary).

Complete [final review](#final-review) to assess the content behind these fields and references. Correct structural defects without changing decisions.

A structurally valid DRAFT may contain pending behavior or TBDs linked to questions. If even a provisional Feature would require invented content, save an incomplete DRAFT. Report the structural requirements that remain unmet. Never invent content to pass validation.

### Optional script assistance

For mechanical assistance, use `python3 <skill-dir>/scripts/validate_design.py <document-path>`. For a compatible replacement template, add `--template <path>`. This script is optional unless the user or project requires it.

- **Checks:** Headings, metadata, version and approval field format and consistency, labels, tables, placeholders, Success Criteria/Feature/Rule/Example IDs, example coverage, and explicit approval blockers.
- **Omits:** Q IDs, question states, dependencies, baseline accessibility, external handoff summaries, and dialogue behavior.
- **Does not establish:** English quality, factual truth, causal reasoning, user consent, or discovery completeness.

Report its actual result and limits under the shared validation method. A script pass does not replace structural or final review.
