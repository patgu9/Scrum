# Open Code Review execution

Use the `ocr` CLI from [alibaba/open-code-review](https://github.com/alibaba/open-code-review). The [upstream Skill](https://github.com/alibaba/open-code-review/blob/main/skills/open-code-review/SKILL.md) documents tool options. This reference supplies the team's invocation and evidence requirements; the [review contract](review-contract.md) owns acceptance and correction responsibility.

## Prepare a fixed review range

Use the configured provider and model. Do not run installation or version probes before every review. Consult `ocr review --help` when an option is uncertain or rejected. Configuration needs belong to the environment owner; keep credentials out of context files and reports.

Set `review_repo` to an isolated checkout at the reviewed head, `diff_base_sha` to the verified comparison base, and `head_sha` to the submitted commit. Use [Git Workflow](../../git-workflow/references/task-and-review.md#declare-and-inspect-the-review-diff) to establish these values. OCR range mode uses the merge base of `--from` and `--to`. Passing the actual comparison base reproduces a PR diff when that base is an ancestor of the head. If a required endpoint comparison differs, resolve that mismatch before claiming coverage; do not label a different range as reviewed.

Prepare a concise Markdown context file containing the task goal, acceptance and exclusions, relevant design contracts, risks, dependencies, self-test evidence, and prior finding IDs. Include essential context directly; links alone do not establish that the tool read inaccessible artifacts. Set `background_file` to that file's absolute path.

Set `preview_file`, `result_file`, and `stderr_file` to distinct absolute files in a writable evidence directory outside the reviewed source tree. Use a fresh directory for each run and retain outputs needed by the report. Quote paths and pass context through the file instead of interpolating prose into shell commands.

```sh
ocr review --repo "$review_repo" --audience agent \
  --from "$diff_base_sha" --to "$head_sha" \
  --background-file "$background_file" --preview --output "$preview_file"
```

Compare the preview with the full Git inventory. Record effective rule files and exclusions. Inspect applicable project rules; do not silently replace them or exclude tests to shrink the review. Preview performs no model review and supplies no acceptance evidence.

## Execute and retain results

After the selected range is correct, run:

```sh
ocr review --repo "$review_repo" --audience agent \
  --from "$diff_base_sha" --to "$head_sha" \
  --background-file "$background_file" --format json \
  --output "$result_file" 2> "$stderr_file"
```

Retain the command outcome, exact range, effective options/rules, session identity when available, raw result, and stderr. Inspect the result and warnings in full, using bounded reads if needed. Do not pipe results through `head` or `tail` and lose findings. Read the actual output schema instead of assuming a fixed wrapper around comments.

Avoid bare workspace mode for task acceptance: it includes staged, unstaged, and untracked changes. A single-commit review can support investigation, but cannot replace the full task diff when the PR contains other changes. The default path is a configured OCR review; do not silently substitute delegation mode or author self-review for a failed run.

## Interpret coverage and failures

Exit code zero does not prove complete review. OCR can publish partial results and return zero when a budget limit affects only part of the work. Inspect per-file or group outcomes, warnings, exclusions, and the full changed-path inventory. Record `failed(budget)`, timeouts, oversized or unsupported files, and other gaps explicitly.

Targeted reruns or documented supplemental review by the independent reviewer can address omitted areas. Record the exact files, method, evidence, and interactions covered. Keep the original OCR result partial in the evidence record. A wholly failed OCR run leaves this workflow incomplete; report the capability blocker rather than silently replacing the tool. Required coverage gaps keep review acceptance blocked.

| Failure | Response |
| --- | --- |
| CLI not found | Report the missing capability. Install through the authorized environment workflow if in scope, then rerun; do not claim a review occurred. |
| Unsupported required flag | Inspect help. Preserve the output gap; use an authorized compatible upgrade or request the missing capability. Do not drop `--output` and substitute potentially truncated stdout. |
| Provider or authentication failure | Route configuration to the environment owner. Use `ocr config provider` when setup is authorized; never request secrets in the review report. |
| Session/output permission failure | Preserve the error and request the required authorized access or environment correction. Do not treat failure to create a session as zero findings. |
| Timeout, rate limit, or budget exhaustion | Preserve partial results; address the cause before a targeted retry. Do not increase cost or limits beyond supplied authority. |

For an interrupted range review, resume its session only with the same immutable `--from` and `--to` inputs. Verify any changed rules or context before reusing session evidence. A changed diff needs a new run and the contract's re-review assessment. Stop retries when the same cause persists without a supported remedy; route the blocker through Delivery Lead.
