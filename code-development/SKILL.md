---
name: code-development
description: Implement one claimed development task from a ready task design. Use for feature work, defect corrections, and scoped refactoring, with behavior-driven tests, execution evidence, and a focused handoff to independent code review.
---

# Code Development

The assigned developer implements one task within its approved product and technical baselines. Deliver the change, relevant tests and documentation, execution evidence, and one focused task PR through the authorized workflow.

Planning, task assignment, independent review, integration, QA, and release retain their existing owners. This Skill does not coordinate all tasks in a specification. Reuse existing authorization; invoking a Skill grants no additional authority.

## 1. Establish the task and current state

Read the [development contract](references/development-contract.md) for required inputs, feedback, resumption, and delivery conditions. Start from the task's standalone entry and pinned references. Confirm the claim, existing branch, task-design readiness, dependencies, and current code state before editing.

Read the relevant code, tests, and repository instructions. Use the [implementation methods](references/implementation-methods.md) to turn the assigned acceptance into small, verifiable changes. Resolve missing inputs through their owner; continue only independent work with valid inputs.

## 2. Implement and verify each behavior

Follow [TDD and verification](references/tdd-and-verification.md). For new or corrected behavior, observe a valid Red result, make the smallest sufficient change, confirm Green, then refactor as needed. Preserve actual evidence as work proceeds.

Read only the applicable implementation guidance:

- [Frontend](references/frontend.md) for UI, client state, forms, and asynchronous interaction.
- [Backend](references/backend.md) for APIs, persistence, service interactions, and background work.

Use the project's language, framework, conventions, and approved architecture. Update affected task-design decisions before dependent coding. Route shared-design, product, or task-scope changes through the development contract.

## 3. Prepare the review handoff

Inspect the complete task diff and run the required final checks. Apply the contract's [delivery conditions](references/development-contract.md#delivery-conditions). Write concise evidence using [Technical Writing](../technical-writing/SKILL.md) and the [delivery template](assets/development-report-template.md), adapted to an existing project format.

Return task and baseline references, code and PR identity, verified behavior, actual checks, gaps, readiness, and the next recipient. Self-review does not satisfy independent code review. If PR publication or another required capability is unavailable, preserve the local package and identify the remaining handoff.
