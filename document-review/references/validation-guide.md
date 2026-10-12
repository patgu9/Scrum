# Document validation

Review the document against the applicable Skill, document contract, template, and source evidence. The applicable instructions define the requirements. Scripts can assist with mechanical checks; they do not replace the review.

The calling workflow defines domain criteria and owns status, independent review, and approval. This guide defines the shared validation method and reporting. Use the existing artifact and delivery format. Do not add a validation document or approval gate by default.

## Review the artifact

1. **Structure:** Check the applicable headings, fields, tables, identifiers, references, and required coverage. Use the calling workflow's checklist. For standalone writing, preserve the requested or existing format instead of imposing a new template.
2. **Content and expression:** Complete the [editing passes](../../technical-writing/references/writing-guide.md#edit-in-separate-passes). Apply [English controls](../../technical-writing/references/english-controls.md) to English prose. Compare revisions with their sources and retain unresolved meaning.
3. **Domain and evidence:** Apply the calling workflow's domain criteria. Check claims against available evidence. Keep intended behavior, planned checks, observed results, and approval evidence distinct. A reader walkthrough reviews the text; it does not demonstrate product behavior.

For a local wording edit, review the changed passage and affected references. For a completed document or material revision, review the full affected artifact. Identify the reviewed path and version or revision when available.

Correct defects within the authorized scope. Record missing evidence or decisions and identify dependent work that remains blocked. After a correction, recheck the affected structure, meaning, domain rules, and references. Never invent content to satisfy a checklist.

## Use automated checks

Use relevant scripts when they help or when the user or project requires them. Report the command, checked artifact, actual result, and coverage limits. If a required check is unavailable, record it as not run and follow the calling workflow's completion rules. Do not treat a manual review as execution of that check.

When a script conflicts with an authorized contract or replacement template, report the mismatch. Review against the applicable instructions; do not change agreed content merely to satisfy a stale checker. A mechanical pass supports only the checks the tool actually performs.

Skill-package checks, such as frontmatter or reference checks, validate the Skill's packaging. They do not validate a generated document. Structure or style checks do not establish factual truth, reader comprehension, user approval, or full STE compliance.

## Report the result

Use the caller's review record or delivery summary. For a small edit, a short statement is enough. Report:

- **Coverage:** Reviewed artifact and scope; checks actually performed; self-review or independent review.
- **Findings:** Corrections, unresolved issues, affected locations or stable IDs, and their completion or approval impact under the calling workflow.
- **Limits:** Unreviewed areas, missing evidence, and required checks that were not run. Include optional tool results only when used or relevant to an explicit request.

State whether the review is complete and whether findings remain unresolved. Do not report a script result as overall document validation. Review completion does not change document status or grant approval.

Before delivery, check the review report itself against these reporting rules and the reviewed evidence. Confirm that findings, coverage, and limits match the checks actually performed. Correct reporting errors and retain unresolved gaps in the same report. This is self-review within the current invocation; do not start another invocation or create a separate report to review this report.
