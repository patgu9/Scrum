---
name: code-review
description: Independently review a development task PR with open-code-review (ocr). Use for initial review, advance review agreement, and re-review after corrections. Deliver evidence-backed findings, coverage, and an explicit acceptance conclusion for engineering lead integration.
---

# Code Review

Independent Code Reviewer owns the review conclusion. Use `open-code-review` (`ocr`) to examine the declared change, then assess its findings against the task and approved designs. Developers own corrections; engineering lead owns merge.

## 1. Establish the review inputs

Read the [review contract](references/review-contract.md) for inputs, independence, conclusions, and feedback ownership. Start from the task entry, submitted PR, and current evidence. Use [Git Workflow](../git-workflow/SKILL.md) to identify the exact comparison base, head, and integration target.

Apply the [shared reviewability policy](../planner/references/planning-methods.md#estimate-work-and-review-scope). For advance agreement, assess the proposed scope and record the review commitment under the contract. Agreement does not accept code that has not been reviewed.

## 2. Review the change and verify findings

Follow the [review methods](references/review-methods.md) for behavioral coverage and evidence assessment. Use the [OCR guide](references/open-code-review.md) for execution, complete result capture, coverage gaps, and recovery. The CLI is the default review tool; the optional installed `open-code-review` Skill supplies tool guidance, not this team's role or acceptance policy.

Review without implementing corrections. Running OCR on code you authored remains self-review. Missing prerequisites or failed tool execution produce explicit gaps, not independent acceptance.

## 3. Deliver the conclusion or return findings

Apply the contract's conclusion conditions. Use [Technical Writing](../technical-writing/SKILL.md) and the [review report template](assets/review-report-template.md) in the existing evidence record. Identify reviewed revisions, coverage, findings, limitations, and the next accountable recipient.

Delivery Lead routes corrections and tracks closure. Return updated code for independent review before engineering lead integration. A review conclusion does not establish a merge, QA acceptance, or ship approval.
