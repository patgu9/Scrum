# Design Doc contract

This contract defines the Design Doc's structure, content, saving, review requirements, and approval. Use the [template](../assets/design-doc-template.md) for the output format. Follow the [skill entrypoint](../SKILL.md) for the workflow, [Technical Writing](../../technical-writing/SKILL.md) for writing, and [Document Review](../../document-review/SKILL.md) for validation.

## Inputs and invocation context

Accept a goal, available context and constraints, user answers, and any downstream feedback with its affected product baseline. Discovery can start with an incomplete goal. Investigate available facts and record unresolved questions through the clarification protocol.

For a continuation or feedback request, read the referenced artifacts and check their versions and approval evidence against the requested scope. Missing, inaccessible, conflicting, or stale required input blocks dependent work. Report what is needed, who can supply it, and the affected work. Continue only work whose inputs remain valid; do not reconstruct an approved baseline from memory.

Use the caller's established workflow. This section defines the common route for handoffs, feedback, and approval requests:

- **Team:** PM owns product discovery and artifacts. Address formal returns to Project Manager, identifying the intended specialist or human decision. Project Manager routes handoffs and submits approval requests to the human owner.
- **Standalone:** Address the user directly.

Ask about the route only when the supplied context is ambiguous and the answer affects the next handoff. This context is separate from Startup / Builder discovery mode. Platform commands and record transport belong to the caller's platform Skill.

## Saving

Save the product document as `<project-root>/doc/YYYY-MM-DD-task-slug/product-design.md`. One product change uses one stable directory, even when it spans several Features or conversations.

Before saving:

1. Resolve the project root from project instructions and available context.
2. Reuse the change directory identified by the request, source document, or conversation. Read existing content. If continuation versus a new change remains unclear after inspection, ask the user.
3. For a new change, use its start date and a short English capability name with lowercase words separated by hyphens. If the directory belongs to another change, append `-02`, `-03`, or the next unused suffix. Never overwrite unrelated files.

Keep one current `product-design.md`. Revisions and reopened decisions stay in that file; retain earlier baselines under [version rules](#versions-and-approval-evidence). A separate follow-up change gets a new directory and a link to the earlier change. Create only the product artifact needed now; downstream stages use the same change directory for their own outputs.

Keep the glossary, decisions, and review findings in the same product document. Supply its path and task directory in the handoff summary.

## Structure

The [template](../assets/design-doc-template.md) defines heading spelling, order, and metadata fields. Repeat only the Feature block. Do not add a preface, appendix, extra headings, or metadata fields by default. Apply the user's replacement template when supplied.

Use `Startup` or `Builder` for Mode, `YYYY-MM-DD` for Date, and `Think` for Stage. Follow [version and approval evidence rules](#versions-and-approval-evidence) for Version and Approval, and [status rules](#status-and-approval) for Status.

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
| Problem, actors, situation, current workflow, workaround, consequences, desired outcome, demand, and sources | Problem Statement and Evidence |
| Defined terms and their boundaries | Glossary |
| Ways to achieve the same goal. Benefits, drawbacks, effort (S/M/L/XL), risk (Low/Medium/High), reuse, and reasons for rejecting an approach | Approaches Considered |
| Selected approach, reason, and justification for retained complexity, or a choice marked as pending | Recommendation |
| Goal → actor → behavioral impact → deliverable links. Trigger, handoffs between actors, outcome, how the product reaches users, and shared dependencies | How It Works, including diagrams |
| Initial audience, smallest useful outcome, included Features, exclusions, and costs of future changes where relevant | Scope |
| Premises, assumptions, Q records, dependencies, and unresolved review findings. Approval impact, validation plan, decisions to revisit, and follow-up | Premises and Open Questions |
| Prior product baselines and approvals, reasons for revision, and downstream feedback dispositions | Premises and Open Questions, with links to retained evidence |
| Outcome and verification method. For quantitative goals: baseline, target, units, population, and time window | Success Criteria |
| Value → role → action, SC links, rules, and acceptance examples | Feature blocks |
| One action and observable result. For Startup: validate demand or a critical assumption. For Builder: try a usable outcome | Next Action |

Record need hypotheses and uncertainty about causal links in Premises and Open Questions. Every row needs `Blocks approval: Yes / No` and a reason. Do not add separate sections for interview records, impact maps, or review findings to the Design Doc.

### Question records

Store records from the [clarification protocol](discovery-methods.md#clarify-decisions-and-terms) in the existing four columns. Keep the headers. Do not add sections to the Design Doc for question records.

- **Type:** Give the stable question ID, question type, and question state. Use `Exploration question`, `Fact to investigate`, or `User decision`. Example: `Q3 / Exploration question / OPEN`. Keep existing types for premises and assumptions that are not questions.
- **Statement and Impact:** State the question, its impact, and affected IDs or fields. Give `Depends on: Q1, Q2` or `None`. Include any conditions on those dependencies. Add `Blocks approval: Yes / No` and the reason.
- **Evidence / Validation Status:** Start with the answer or finding, its basis, and source. Use `Pending` or `Unknown` when the answer or evidence is missing. For user decisions, also record the main options, tradeoffs, recommendation, and reason. Exploration and fact investigations need no option comparison.

  Cite the conversation turn or quote the user's answer. Support investigated facts with source evidence, including files or tool results when used. Distinguish reported experience, direct observation, stated intent, and agent inference. Mark hypothetical scenarios. For a reopened question, keep the prior answer and the reason for reopening. Agreement does not prove a factual assumption or target-user demand.

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
- **IN_REVIEW:** The document is complete, the direction is agreed, and no approval blockers remain. Request confirmation through the [established route](#inputs-and-invocation-context).
- **APPROVED:** The user explicitly approved this version. Blockers are resolved or the user agreed to exclude affected scope. Approval does not validate assumptions.

Questions about core users, scope, or behavior block approval unless the user agrees to exclude the affected scope.

If goals, scope, rules, or outcomes change materially:

1. Preserve the prior baseline, update Version as required above, set Status to DRAFT, and reset Approval to Pending.
2. Obtain the user's product decision unless the change is already authorized. Authorization to revise is not approval of the resulting version.
3. Check affected terms, Success Criteria, User Stories, and examples.
4. Set IN_REVIEW when the document is complete and no approval blockers remain.

Typographic edits alone preserve approval.

Request human approval of the exact product version through the route in [inputs and invocation context](#inputs-and-invocation-context). Record explicit approval before handing the version to technical design. Clarifying a product decision does not approve the whole version. Approval neither proves feasibility nor authorizes implementation.

## Handoff summary

Provide a handoff summary when delivering a product document, submitting it for approval, returning feedback, or ending work with a blocker. Include references to available artifacts; a blocker summary does not require a completed document.

During ongoing discovery, reply with the relevant answer or finding and the next clarification step. Keep an ordinary wait for an answer within that loop. Update question records with sources, states, and dependencies under the clarification protocol. Use the full summary when a delivery condition above applies.

Put the summary in the caller's delivery record or response, outside the product document's fixed structure. Keep it platform-independent; transport is the caller's responsibility.

Include:

- **Task and inputs:** Task identity and directory; input artifacts and exact versions, applicable approval references, and feedback identity. For a new goal, cite the supplied request rather than inventing an input version.
- **Outputs:** Product document path and Version, or the feedback response and its affected baseline. Link supporting artifacts rather than copying them.
- **Conclusion:** Discovery incomplete, awaiting approval, approved for technical design, or feedback/blocker. State the document Status and approval evidence separately; completing this invocation does not establish downstream acceptance.
- **Evidence:** Document Review results for structure, content, and evidence, review coverage and attempt count, investigated evidence and its limits. Follow the shared [validation reporting rules](../../document-review/references/validation-guide.md#report-the-result). Include relevant environment, actual tool results when used, and required checks that were not run. Planned examples and checks are not execution evidence.
- **Open items:** Stable question/finding IDs, dispositions, affected product rules, missing information, and who can supply it. Preserve feedback identity through revisions.
- **Next handoff:** Next function, responsible recipient, requested action, and prerequisites. Use the route in [inputs and invocation context](#inputs-and-invocation-context) and identify the intended specialist or human decision. An approved forward handoff names `technical-design` in overall mode and the recipient holding the Architect responsibility. Engineering lead can hold this responsibility.

For a feedback response, include the content required by [revisit a product baseline](discovery-methods.md#revisit-a-product-baseline). A blocker or a request for evidence is a valid delivery; it does not require a completed product revision.

## Document language

Write the Design Doc in English using [Technical Writing](../../technical-writing/SKILL.md). Follow [content placement](#content-placement). Include reader prerequisites in Problem Statement or Glossary when needed for understanding. Keep conversation progress updates outside the document.

## Product review boundary

Review user goals, value, product behavior, and observable results. Walk through the user journey, including relevant failures and corrections. State each product finding's effect on those outcomes. Stop when the behavior and acceptance criteria are clear enough to assess; leave implementation choices open.

Describe what users can choose, see, and rely on. For example, define whether merging events changes tracking and what users see after a failed delivery. Leave schemas, transactions, locks, epochs, storage, API protocols, and process isolation to the Architect using `technical-design`.

Route implementation questions through the caller's established handoff. Retain their IDs, needed evidence, owner, and affected technical stage. Split mixed findings into the product consequence and technical follow-up. Missing implementation details alone do not block product approval.

A technical constraint can block product approval when concrete evidence shows that the promised behavior cannot be supported within the stated product constraints. Identify the affected promise, evidence, and required product decision. An unverified mechanism alone does not establish that conflict. Keep feasibility assumptions visible for technical assessment; product approval does not close them.

## Final review

Use Document Review to apply these product-specific checks within the [product review boundary](#product-review-boundary):

1. **Value and scope:** Make sure a reader can understand the document without the conversation. Check the problem, evidence, actors, and intended change in behavior. Check the smallest useful outcome, alternatives for the same goal, uncertainty in estimates, and the user's chosen approach. Mark hypotheses. Distinguish current from desired behavior.

   Check the basis and unresolved validation of need hypotheses from [deep discovery interviews](discovery-methods.md#deep-discovery-interviews). Include relevant contrasts or, for a new experience, related context and a proposed trial.

   Check the approach and scope rationale against [Occam's Razor](discovery-methods.md#occams-razor), including the purpose of retained complexity and coverage of outcomes and constraints.
2. **Journey and language:** Check terms, triggers, handoffs between actors, dependencies, how the product reaches users, and outcomes across Features. Complete the Technical Writing Skill's [editing passes](../../technical-writing/references/writing-guide.md#edit-in-separate-passes).
3. **Verifiable behavior:** Link each User Story to valid Success Criteria. Link every defined rule to concrete examples. Check units, boundaries, exceptions, and what stays unchanged.

   For quantitative goals, check metric definitions and measurement context. Explain how to obtain missing baselines. Builder may use a qualitative demonstration.

   For each important assumption, check what to observe and how to collect observations. Check which result would not support the assumption and which decisions to reopen. Examples of intended behavior alone do not validate assumptions.
4. **Decisions and approval:** Check question records, sources for resolved answers, dependencies, unanswered questions, and content awaiting review. An empty question queue does not prove that approval blockers are resolved. Apply [Status and approval](#status-and-approval) to the current version and its unresolved questions.
5. **Completion:** Check that Next Action is concrete, the handoff summary identifies valid inputs and the next recipient, and the work stays within the entrypoint's scope. For revisions, check retained baselines, current approval evidence, and feedback disposition.

## Structural validation

Use [Document Review](../../document-review/SKILL.md) and its shared [validation method](../../document-review/references/validation-guide.md) for structural validation. Review the document directly against this contract and the applicable template:

1. **Format:** Heading order, metadata values, required labels, table headers and complete rows, and populated sections. Remove template placeholders and instructional comments. Apply the user's replacement template when supplied.
2. **Identifiers and coverage:** Unique, stable Success Criteria, Feature, Rule, and Example IDs. Each User Story links to defined Success Criteria. Each example links to valid rules and contains Given, When, and Then. Every defined rule has an example.
3. **Questions and status:** Q IDs, question states, dependencies, TBD links, and explicit approval blockers. Check consistency with the [clarification protocol](discovery-methods.md#clarify-decisions-and-terms) and [status rules](#status-and-approval).
4. **Versions and handoff:** Current Version and Approval fields, retained baselines and accessible approval evidence, and required handoff-summary fields. Apply [versions and approval evidence](#versions-and-approval-evidence) and [handoff summary](#handoff-summary).

Complete [final review](#final-review) to assess the content behind these fields and references. Correct structural defects without changing decisions.

A structurally valid DRAFT may contain pending behavior or TBDs linked to questions. If even a provisional Feature would require invented content, save an incomplete DRAFT. Report the structural requirements that remain unmet. Never invent content to pass validation.
