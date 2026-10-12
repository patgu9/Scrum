# Review methods

Use the [contract](review-contract.md) for authority and acceptance. Review one complete task change against its stated purpose and baselines.

## Establish the comparison

Read the task, relevant designs, project instructions, developer report, and prior findings before running OCR. Identify what changed, why, which behavior must remain, and what evidence would establish the task's acceptance.

Resolve base and head to immutable commits using [Git Workflow](../../git-workflow/references/task-and-review.md#declare-and-inspect-the-review-diff). Record the declared base tip, actual comparison base, head, comparison convention, integration target, and predecessor for stacked work. Reconcile the PR's displayed diff with the tool's selected range.

Inspect all changed paths and actual scope, including tests, usage, documentation, deletions, generated files, and binary artifacts. Counts describe scope; they cannot establish reviewability or permit omitted files. Use an isolated checkout at the submitted revision when local edits or another worker's checkout could contaminate source inspection or test results.

## Review behavior and evidence

Run OCR using the [tool guide](open-code-review.md). Read the complete diff and enough surrounding code to assess interactions. Use the following lenses where they apply; do not invent unrelated work:

| Area | Review question |
| --- | --- |
| Acceptance and design | Does the implementation satisfy assigned behavior, exclusions, shared contracts, and task decisions? |
| Correctness | Do normal paths, boundaries, failures, retries, and partial results preserve the required behavior? |
| Safety and data | Are authorization, input handling, sensitive data, resource ownership, and destructive operations correct? |
| Interactions | Can API consumers, concurrent operations, persistence, migrations, or dependencies invalidate local assumptions? |
| Tests | Do tests check observable behavior and important failures? Do execution results cover the submitted revision? |
| Maintainability | Is the change understandable and appropriately scoped under project conventions, without unnecessary complexity? |
| Performance | Is there a concrete workload or code path supporting the concern, rather than speculative optimization? |
| Usage and documentation | Are required callers, configuration, compatibility notes, and user-facing instructions consistent with the change? |

Inspect changed tests as authored code. For generated or non-text artifacts, record an appropriate review method and actual validation evidence. Do not infer QA acceptance from developer checks or substitute an OCR run for repository tests.

Read reported evidence before repeating checks. Run focused, permitted checks when a claim needs confirmation; use isolation if a probe creates files. Do not change production code or weaken tests during review. Record commands, revision, environment, actual results, and limits. Unavailable required checks remain gaps.

## Verify tool findings

For each actionable OCR comment, inspect the exact reviewed source and relevant callers. Verify its premise, triggering conditions, impact, and location. Reproduce the behavior when practical; otherwise state the source evidence and uncertainty. A suggested patch is an unverified proposal.

If OCR reports line zero or a misplaced comment, locate the issue in the reviewed revision before publishing it. If no precise line exists, use a verified symbol or artifact location and state the positioning limit. Do not fabricate a line number.

Deduplicate findings while retaining traceability to raw output. Dismiss unsupported claims with reasons. Promote real correctness or safety defects to blocking findings regardless of source severity. Keep optional improvements distinguishable from required corrections.

## Reassess before delivery

Check that the PR still identifies the reviewed head and relevant base. If it changed during review, preserve the completed report for its original revision and reassess the new change before current acceptance. Apply the contract's [re-review rules](review-contract.md#corrections-and-re-review).

Reconcile the full changed-path inventory with OCR results and supplemental review. Identify skipped, unsupported, failed, or unexamined areas and their effect on coverage. An empty finding list is meaningful only within the recorded coverage; unresolved required gaps prevent acceptance.
