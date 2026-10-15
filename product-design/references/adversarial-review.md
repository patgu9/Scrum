# Product review

Before delivery, use [Document Review](../../document-review/SKILL.md) to check product documents, review reports, feedback responses, and handoff summaries against the applicable criteria below. If an independent reviewer is available and authorized, use that reviewer before presenting a completed design for approval. Otherwise perform self-review and report why independent review was not run. Review does not grant approval.

## Inputs and findings

Review the full current Design Doc, its exact version and revision or retained snapshot, existing supporting records, and relevant evidence. Include the template, document contract, applicable discovery guidance, prior designs, and earlier findings and remedies. Read the materials directly.

Use the [review template](../assets/review-template.md) for finding fields. Give each finding a precise location, defect or unknown, basis, consequence, remedy, and approval impact. Seek contradictions and counterexamples. Separate wording defects, unknown facts, and product decisions. In later attempts, assess new, unresolved, and resolved findings against the revised evidence.

## Product review boundary

Review user goals, value, behavior, and observable results, including relevant failure and correction paths. Stop when the product behavior and acceptance criteria are clear enough to assess. Leave implementation choices to technical design.

Route technical questions through the caller's [established route](document-contract.md#inputs-and-invocation-context), retaining IDs, needed evidence, owner, and stage. Split mixed findings into product consequences and technical follow-up. Missing schemas, transactions, storage mechanisms, or API protocols alone do not block product approval.

A technical constraint can block approval when concrete evidence shows that a product promise conflicts with stated constraints. Identify the promise, evidence, and needed product decision. An unverified mechanism does not establish that conflict; product approval does not prove feasibility.

## Final review

Apply relevant criteria across the design and existing supporting files. Do not require every discovery method for every change.

| Area | Check |
| --- | --- |
| Need and value | The situation, actor, outcome, selected need, and supporting evidence are understandable without the conversation. Current behavior, intent, and hypotheses remain distinct. |
| Choice and scope | Alternatives serve the same goal. The chosen direction, exclusions, estimate uncertainty, retained complexity, and relevant strategic or adoption constraints have a basis. Apply Occam's Razor. |
| Journey | Terms, triggers, actor handoffs, product dependencies, and access to value are consistent across Features. Include relevant failures and corrections. |
| Measurement | Success Criteria represent the outcome, with applicable guardrails, population, units, baseline, target, window, and method. Unknowns retain a way to obtain evidence. Proxies and borrowed benchmarks do not establish success. |
| Validation | Material assumptions have observable tests, disconfirming results, and affected decisions. The method fits available users and time. Inconclusive evidence stays unresolved. AI claims include representative cases and recovery where relevant. |
| Decisions | Question states, dependencies, answers, and findings have evidence. Confirmed conclusions reached the design; unresolved effects and approval blockers remain visible. |
| Delivery | Next Action is concrete. Version, approval, retained baseline, and handoff match the contract. The work stays within scope. |

Apply [Technical Writing](../../technical-writing/SKILL.md) for clarity and terminology, then the structural checks below.

## Structural validation

Check the [document contract](document-contract.md) and applicable templates:

- Heading order, metadata, labels, table columns, populated fields, and removal of placeholders and instructional comments. Respect the user's replacement template.
- Unique, stable Success Criteria, Feature, Rule, and Example IDs. Each User Story links to defined SC IDs; each rule has an example; each example references valid rules and supplies facts, action, and observable results. Check units, boundaries, exceptions, and unchanged state.
- Relative links and anchors, stable Q/R IDs, valid question states, dependencies, TBD links, and explicit blockers. Check review attempts, revisions, finding history, and coverage. Keep full Q and review logs out of the main design.
- Current Version and Approval, accessible prior baselines and approval evidence, and the required handoff fields.

Structural validity does not establish semantic correctness or approval. A DRAFT can contain pending behavior or TBDs linked to questions. If a provisional Feature would require invented content, save an incomplete DRAFT and report unmet requirements.

## Review loop — maximum three attempts

An attempt is one request sent to a reviewer. Every request counts, even if it fails. Allow at most three attempts.

1. Send the completed draft for review.
2. Stop this review loop before making further edits if any condition applies:

   - No findings remain.
   - The third attempt is complete.
   - An issue remains after a correction, without meaningful progress.

   If a finding needs evidence or a user decision, retain it and use the [clarification protocol](discovery-methods.md#clarify-decisions-and-terms). Record or reopen its question. Pause reviewer requests and dependent work; continue independent investigation or drafting. After resolution or an agreed scope exclusion, return to step 3 only if attempts remain and the issue has progressed.
3. Apply corrections within the agreed design, including any answers or exclusions from clarification. For a material change, apply the contract's [status and approval rules](document-contract.md#status-and-approval).
4. Recheck affected content under the shared [document validation method](../../document-review/references/validation-guide.md), including the [structural checks](#structural-validation). Send the full revision and prior findings for the next review attempt. Mark a finding resolved only when the reviewer's evidence supports that conclusion.

If review fails, times out, or returns invalid output, stop the review loop. Report incomplete review coverage. Keep usable findings and concrete evidence for issues that remain unresolved.

Keep prior findings and the total attempt count. Answering a question does not reset the three-attempt limit.

If attempts are exhausted with unresolved findings or incomplete coverage, report those limits. A third review can finish with complete coverage and no remaining findings. Answering a question alone does not complete it.

## Record and approval

Use `product-design-review.md` and the [review template](../assets/review-template.md). Give each finding a stable `R<n>` ID and heading. Never renumber or reuse IDs. Update recurring findings in place; retain resolved and excluded records, corrections, verification evidence, and attempt history.

Record each request's exact input version and revision or snapshot, reviewer, result, coverage, and findings, including failures. Identify author self-review separately; it is not an independent review or reviewer request.

If clarification is needed, link a Q record in both directions. Keep the finding open until verification supports resolution or the user explicitly excludes its scope. Put corrections and brief unresolved effects in the design; keep full records here. An answer or edit alone does not resolve a finding.

Report independence, attempts, completed reviews, unresolved findings, and coverage gaps under the shared [reporting rules](../../document-review/references/validation-guide.md#report-the-result). Apply the contract's [status and approval rules](document-contract.md#status-and-approval).
