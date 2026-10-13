---
name: code-development
description: Implement one claimed development task from a ready task design. Use for features, defect corrections, and scoped refactoring. Deliver tests, execution evidence, and a focused handoff to independent code review.
---

# Code Development

Implement one assigned task within its approved product and technical baselines. Deliver the change, relevant tests and documentation, execution evidence, and one focused task PR through the authorized workflow.

Planning, task assignment, independent review, integration, QA, and release retain their existing owners. This Skill does not coordinate all tasks in a specification. Reuse existing authorization; invoking a Skill grants no additional authority.

## 1. Establish the task and current state

Read the [development contract](references/development-contract.md) for inputs, authority, and handoff conditions. Start from the task's standalone entry and pinned references. Confirm ownership, the existing branch, task-design readiness, dependencies, and current code state before editing. For interrupted work, follow the contract's [resumption rules](references/development-contract.md#resumption).

Read the relevant code, tests, and repository instructions. Use the [implementation methods](references/implementation-methods.md) to turn the assigned acceptance into small, verifiable changes. Resolve missing inputs through their owner; continue only independent work with valid inputs.

## 2. Implement and verify each behavior

For defect corrections, use [experiments to identify the cause](references/implementation-methods.md#identify-defect-causes-through-experiments) before choosing the fix.

Follow [TDD and verification](references/tdd-and-verification.md). For new or corrected behavior, observe Red, implement the smallest sufficient change, confirm Green, then refactor as needed. For refactoring, inherited code, or changes that do not need a new behavior test, use the reference's [verification alternatives](references/tdd-and-verification.md#existing-code-and-alternative-verification). Record actual evidence as work proceeds.

Read only the applicable implementation guidance:

- [Frontend](references/frontend.md) for UI, client state, forms, and asynchronous interaction.
- [Backend](references/backend.md) for APIs, persistence, service interactions, and background work.

Use the project's language, framework, conventions, and approved architecture. Update affected task-design decisions before dependent coding. Route shared-design, product, or task-scope changes through the development contract.

## 3. Prepare the review handoff

Inspect the complete task diff and run the required final checks. Apply the contract's [delivery conditions](references/development-contract.md#delivery-conditions).

Use [Technical Writing](../technical-writing/SKILL.md) as the writing method for development reports, feedback responses, and handoff summaries. Use the [delivery template](assets/development-report-template.md) to record the result in the project's delivery format.

Before delivery, use [Document Review](../document-review/SKILL.md) to review these outputs. Document review does not replace execution checks.

Report implementation verification, PR publication, and review handoff readiness separately. Include the references, evidence, gaps, and recipient required by the contract. Self-review does not satisfy independent code review. If publication or another required capability is unavailable, preserve the local package and identify the remaining handoff.
