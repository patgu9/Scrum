---
name: technical-design
description: Create or revise technical designs in two modes. Use overall mode to define architecture and the shared decisions needed for task planning; use task mode to design an assigned feature or behavior before coding. Include verification strategy, design review, and scoped handoffs.
---

# Technical Design

Use one design method at two scopes: overall design supports task planning; task design supports implementation of one assignment. Keep detailed questions, investigation, and review history in linked supporting records; retain current decisions and material limits in the design.

This Skill produces design artifacts and handoffs. Planning, assignment, Git operations, code, executable feature tests, and deployment belong to their respective workflows. Reuse existing authorization for follow-on work; design readiness alone does not grant it.

Use [Technical Writing](../technical-writing/SKILL.md) as the writing method for design documents, review reports, feedback responses, and handoff summaries in both modes. The document contract defines required content, format, and approval.

## 1. Select the mode and baseline

Start with the contract's [mode and input rules](references/document-contract.md#modes-and-required-inputs). Declare the mode; ask only when the requested scope remains ambiguous.

- **Overall:** Use approved product behavior and system evidence to establish architecture and shared decisions before `planner` decomposes work.
- **Task:** Use a claimed task, branch reference, and approved product and overall-design baselines to refine implementation before `code-development` starts.

Read the contract's common sections from [document scope and saving](references/document-contract.md#document-scope-and-saving) through [status and approval](references/document-contract.md#status-and-approval). Then read only the selected mode's handoff conditions: [overall](references/document-contract.md#overall-handoff-to-planner) or [task](references/document-contract.md#task-handoff-to-code-development). Use [feedback and revisions](references/document-contract.md#feedback-and-revisions) when a constraint or baseline change needs an upstream decision.

Read project instructions and exact source versions. Use [current-fact investigation](references/design-methods.md#establish-current-facts) to establish the evidence for this scope.

## 2. Design at the selected scope

Use the [overall template](assets/technical-design-doc-template.md) or [task template](assets/task-design-template.md). A routine task can use a short note with the contract's [required content](references/document-contract.md#structure-and-content-placement).

Read these methods as needed:

- **Every design:** [behavior and interfaces](references/design-methods.md#design-behavior-and-interfaces) and [verification planning](references/design-methods.md#plan-test-driven-development).
- **Competing quality goals or consequential tradeoffs:** [quality priorities](references/design-methods.md#prioritize-quality-goals-and-resolve-tradeoffs). Routine tasks can reference approved priorities.
- **Relevant failure or operational risks:** [failure and operational methods](references/design-methods.md#define-failures-and-operational-behavior). Assess applicability before omitting an area.
- **Relationships, ordering, or states remain unclear:** [modeling guide](references/uml-modeling.md). Reuse a sufficient view, table, or textual flow.

Stop at the contract's selected decision depth. Use the contract's [content placement](references/document-contract.md#keep-the-current-design-concise) and supporting templates for [questions](assets/questions-template.md) and [reviews](assets/review-template.md). Create records only when needed; templates do not create additional design obligations.

## 3. Review and hand off

Use [Document Review](../document-review/SKILL.md) with the [engineering review criteria](references/engineering-review.md) for one review of the design. Include the applicable scenario walkthroughs and document checks in that review. Preserve required reviewer roles and record actual coverage, findings, and limits.

Also use Document Review for review reports, feedback, and handoff summaries. Follow its reporting and forwarding rules; do not repeat the full design review merely to check a summary.

Apply the selected handoff conditions. Return mode, design and supporting-record references, exact baselines, status, readiness by scope, evidence limits, blockers, and the next function and recipient. Report unavailable follow-on capabilities as delivery blockers.
