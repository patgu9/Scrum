# Adversarial review

If an independent reviewer is available and authorized, use that reviewer before presenting a completed Design Doc for approval. Otherwise complete the contract's [final review](document-contract.md#final-review). Report why independent review was not run.

## Inputs and findings

Give the reviewer:

- The full current Design Doc.
- The template, contract, [Technical Writing Skill](../../technical-writing/SKILL.md), and [discovery methods](discovery-methods.md).
- Relevant evidence and prior designs. For an initially vague idea, include [interview findings](discovery-methods.md#deep-discovery-interviews) and their sources.
- Findings and remedies from earlier review attempts.

Ask the reviewer to:

- Read these materials directly.
- Apply the contract's [final review](document-contract.md#final-review) within its [product review boundary](document-contract.md#product-review-boundary).
- Check question states and dependencies against the [clarification protocol](discovery-methods.md#clarify-decisions-and-terms).

Seek contradictions and counterexamples under those criteria. Challenge the design's assumptions with evidence from the supplied materials.

For each finding, require:

- **Location:** Section or stable ID.
- **Problem:** The defect or unresolved question.
- **Basis:** Evidence or counterexample.
- **Consequence:** The effect on a user goal, product behavior, or observable result; for a document defect, explain the effect on understanding or approval evidence.
- **Remedy:** A product correction or a question that needs an answer. Identify the technical-design owner and stage for an implementation follow-up; do not prescribe its mechanism.
- **Approval impact:** Whether the finding blocks approval and why.

Distinguish unknown facts from contradictions. Separate wording problems from product decisions. User agreement does not prove a factual assumption. In later attempts, use evidence from the revised document to identify new, unresolved, and resolved findings.

## Review loop — maximum three attempts

An attempt is one request sent to a reviewer. Every request counts, even if it fails. Allow at most three attempts.

1. Send the completed draft for review.
2. Stop this review loop before making further edits if any condition applies:

   - No findings remain.
   - The third attempt is complete.
   - An issue remains after a correction, without meaningful progress.

   If a finding needs evidence or a user decision, retain it and use the [clarification protocol](discovery-methods.md#clarify-decisions-and-terms). Record or reopen its question. Pause reviewer requests and dependent work; continue independent investigation or drafting. After resolution or an agreed scope exclusion, return to step 3 only if attempts remain and the issue has progressed.
3. Apply corrections within the agreed design, including any answers or exclusions from clarification. For a material change, apply the contract's [status and approval rules](document-contract.md#status-and-approval).
4. Recheck affected content under the shared [document validation method](../../document-review/references/validation-guide.md), including the contract's structural requirements. Send the full revision and prior findings for the next review attempt. Mark a finding resolved only when the reviewer's evidence supports that conclusion.

If review fails, times out, or returns invalid output, stop the review loop. Report incomplete review coverage. Keep usable findings and concrete evidence for issues that remain unresolved.

Keep prior findings and the total attempt count. Answering a question does not reset the three-attempt limit.

If attempts are exhausted with unresolved findings or incomplete coverage, report those limits. A third review can finish with complete coverage and no remaining findings. Answering a question alone does not complete it.

## Record and approval

Record findings in the contract's [assigned location](document-contract.md#content-placement). Keep every unresolved finding and its remedy across revisions.

Report whether review was independent or performed by you. Include the total attempts, completed reviews, unresolved findings, and areas not fully reviewed. Apply the contract's status and approval rules to the final document Status.
