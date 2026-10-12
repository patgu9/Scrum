---
name: technical-design
description: Create or revise technical designs in two modes. Use overall mode to define architecture and the shared decisions needed for task planning; use task mode to design an assigned feature or behavior before coding. Include verification strategy, design review, and scoped handoffs.
---

# Technical Design

Use one design method at two scopes. Overall design supports coherent task planning; task design supports implementation and verification of one assignment. Engineering lead can hold the architect responsibility. Design continues as implementation exposes new evidence.

This Skill produces design artifacts and handoffs. Planning, assignment, Git operations, code, executable feature tests, and deployment belong to their respective workflows. Reuse existing authorization for follow-on work; design readiness alone does not grant it.

Use [Technical Writing](../technical-writing/SKILL.md) as the writing method for design documents, review reports, feedback responses, and handoff summaries in both modes. The document contract defines required content, format, and approval.

## 1. Select the mode and baseline

Read the [document contract](references/document-contract.md) for mode selection, required inputs, approval, and readiness. Infer the mode from the request and artifacts; ask only when the intended scope remains ambiguous. Declare the mode in the output.

- **Overall:** Use approved product behavior and system evidence to establish architecture and shared decisions before `planner` decomposes work.
- **Task:** Use a claimed task, branch reference, and approved product and overall-design baselines to refine implementation before `code-development` starts.

Read relevant project instructions and exact source versions. Use [current-fact investigation](references/design-methods.md#establish-current-facts). Keep missing or stale inputs explicit; continue only independent design work.

## 2. Design at the selected scope

Read the [design methods](references/design-methods.md). Compare meaningful approaches and connect behavior to verification.

Use the [overall template](assets/technical-design-doc-template.md) for overall mode. Use the [task template](assets/task-design-template.md) for task mode; a simple task can use a compact note with the same required information.

Apply the contract's [decision depth and stopping conditions](references/document-contract.md#decision-depth-and-deferred-work). Leave feature internals to task mode unless they determine an architecture decision or shared contract. In overall mode, define verification obligations; in task mode, plan concrete Red → Green → Refactor steps. Return baseline changes through the [feedback loop](references/document-contract.md#feedback-and-revisions).

## 3. Review and hand off

Follow the [engineering review](references/engineering-review.md), scaled to the mode and risk. Complete the writing passes and document checks. Record actual review coverage and unresolved findings.

Before delivery, use [Document Review](../document-review/SKILL.md) to review design documents, review reports, feedback responses, and handoff summaries in both modes.

Apply the contract's [status and readiness rules](references/document-contract.md#status-and-approval). Overall mode hands approved architecture to `planner`; task mode hands a ready task design to `code-development`. Neither substitutes for independent code review or ship approval.

Return the mode, artifact and baseline references, status, readiness by scope, evidence limits, and next function with its responsible recipient. Identify the stage and work affected by each blocker. If a required follow-on Skill is unavailable, preserve the handoff and report the missing capability.
