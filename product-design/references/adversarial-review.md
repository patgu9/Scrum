# Adversarial review

If an independent reviewer is available and authorized, use that reviewer before presenting a completed Design Doc for approval. Otherwise complete the contract's [final review](document-contract.md#final-review). Report why independent review was not run.

## Inputs and findings

Give the reviewer:

- The full current Design Doc.
- The template, contract, [Technical Writing Skill](../../technical-writing/SKILL.md), and [clarification protocol](discovery-methods.md#clarify-decisions-and-terms).
- Relevant evidence and prior designs.
- Findings and remedies from earlier review attempts.

Ask the reviewer to:

- Read these materials directly.
- Apply the contract's [final review](document-contract.md#final-review).
- Check question states and dependencies against the clarification protocol.

Ask the reviewer to look for:

- **Completeness:** Missing actors, journey steps, dependencies, ways to reach users, rules, or examples.
- **Consistency:** Conflicts in terms, scope, criteria, behavior, or decisions.
- **Clarity:** Unclear actors or outcomes, undefined terms, dense wording, or unresolved decisions presented as settled.
- **Scope:** Unsupported Features, missing causal links between goals, actors, behavior, and Features, or weak alternatives.
- **Feasibility:** Unsupported assumptions about adoption, behavior, reuse, or architecture.

For each finding, require:

- **Location:** Section or stable ID.
- **Problem:** The defect or unresolved question.
- **Basis:** Evidence or counterexample.
- **Consequence:** The effect on the design.
- **Remedy:** A correction or a question that needs an answer.
- **Approval impact:** Whether the finding blocks approval and why.

Distinguish unknown facts from contradictions. Separate wording problems from product decisions. User agreement does not prove a factual assumption. In later attempts, use evidence from the revised document to identify new, unresolved, and resolved findings.

## Review loop — maximum three attempts

An attempt is one request sent to a reviewer. Every request counts, even if it fails. Allow at most three attempts.

1. Send the completed draft for review.
2. Stop this review loop before making further edits if any condition applies:

   - No findings remain.
   - The third attempt is complete.
   - New evidence or a user decision is required.
   - An issue remains after a correction, without meaningful progress.

   If evidence or a user decision is needed, keep the finding. Record or reopen its question through the [clarification protocol](discovery-methods.md#clarify-decisions-and-terms). Pause further reviewer requests and work that depends on the answer. Continue independent investigation or drafting.
3. Otherwise correct wording or structure within the agreed design. For a material change, apply the contract's [status and approval rules](document-contract.md#status-and-approval).
4. Recheck affected content under the shared [document validation method](../../document-review/references/validation-guide.md), including the contract's structural requirements. Send the full revision and prior findings for the next review attempt. Mark a finding resolved only when the reviewer's evidence supports that conclusion.

If review fails, times out, or returns invalid output, stop the review loop. Report incomplete review coverage. Keep usable findings and concrete evidence for issues that remain unresolved.

After the question is resolved or the user agrees to exclude the affected scope:

1. Update the affected content.
2. Apply the contract's status rules.
3. Recheck affected structure, meaning, domain rules, and references under the shared validation method.
4. Resume review only if attempts remain and the issue has progressed.

Keep prior findings and the total attempt count. Answering a question does not reset the three-attempt limit.

If all three attempts have been used, report incomplete review coverage and keep unresolved findings. Answering a question alone does not complete the review.

## Record and approval

Record findings in the contract's [assigned location](document-contract.md#content-placement). Keep every unresolved finding and its remedy across revisions.

Report whether review was independent or performed by you. Include the total attempts, completed reviews, unresolved findings, and areas not fully reviewed. Apply the contract's status and approval rules to the final document Status.
