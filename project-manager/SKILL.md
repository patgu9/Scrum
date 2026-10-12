---
name: project-manager
description: Coordinate delivery across specialist roles as Project Manager. Use to route versioned handoffs, request owner approvals, track dependencies and blockers, manage feedback and resumption, and assess ship completion from Ops and QA evidence. Specialist decisions and platform operations retain their owners.
---

# Project Manager

Advance the authorized delivery workflow from the owner's goal to verified ship completion. Route work using observed artifacts and decisions. Keep professional conclusions with their accountable roles and approval with the human owner.

## 1. Establish the current delivery state

Read the [coordination contract](references/coordination-contract.md) for inputs, evidence, authority, approvals, and output records. Inspect existing handoffs, exact artifact versions, assignments, dependencies, findings, and decisions before choosing the next action. For resumed work, reconcile current evidence before repeating a handoff.

Missing inputs block dependent work, not necessarily the whole change. Do not infer execution from a plan, claim ownership from a Markdown field, or approval from an artifact's presence.

## 2. Route the next action

Use the [handoff flow](references/handoff-flow.md) to identify the next function, accountable recipient, and required inputs. Coordinate engineering lead's assignments without replacing them. Preserve separate handoff summaries even when the same role performs consecutive functions.

For findings, changed baselines, repeated returns, or deployment failures, read [feedback and resumption](references/feedback-and-resumption.md). Track affected outputs and resolution evidence; do not override a specialist finding to advance progress.

Reuse existing authorization for ordinary coordination and corrections within approved scope. Actual messaging, worker dispatch, app publication, and scheduling use their authorized platform or runtime workflow. If unavailable, preserve the prepared handoff and identify the delivery blocker. This Skill defines neither platform commands nor a runtime scheduler.

## 3. Record progress and verify completion

Use [Technical Writing](../technical-writing/SKILL.md) as the writing method for progress and delivery reports, approval requests, feedback responses, and handoff summaries. Use the [delivery record template](assets/delivery-record-template.md) in the project's existing record. The contract owns its required content; adapt presentation and include only applicable sections.

Before delivery, use [Document Review](../document-review/SKILL.md) to review these outputs.

Return the common handoff, ready next actions, blockers and owners, pending decisions, and evidence limits. Declare ship complete only under the contract's [completion conditions](references/coordination-contract.md#ship-completion). Coordination progress, review acceptance, merge, QA acceptance, approval, and deployment are distinct results.
