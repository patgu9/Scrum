---
name: planner
description: Turn approved product and overall technical designs into assigned, reviewable development tasks. Use for initial task breakdown, reassignment, scope splits, and linked defect corrections. Return product or shared-design constraints to their decision owner.
---

# Planner

As engineering lead, define and assign development work. Produce a plan index and one standalone Markdown file per task. If a constraint prevents planning, return feedback with supporting evidence. Keep product behavior and shared technical decisions in their approved source documents.

This Skill owns planning artifacts and assignment decisions. App publication, runtime scheduling, branch creation, task design, coding, review, merge, and release use their respective workflows. Reuse existing authorization for follow-on work; a completed plan grants no new authority.

## 1. Establish the planning baseline

Read the [plan contract](references/plan-contract.md) for inputs, task fields, readiness, and handoffs. Inspect the exact product and overall-design versions, approval evidence, repository context, existing tasks, and developer availability. Check the overall design's readiness for the requested scope.

Missing or stale inputs block dependent assignment. Preserve useful independent work and identify the input supplier. Do not infer approval from the request to plan, a document's location, or a prior version's approval.

## 2. Decompose and assign

Follow the [planning methods](references/planning-methods.md) to map behavior to tasks, sequence dependencies, estimate the full work, and assess reviewability. Use small, complete changes; line counts are scope information, not a default gate. Use [Technical Writing](../technical-writing/SKILL.md) to write concise task instructions.

Use the [plan index template](assets/task-plan-template.md) and [task template](assets/task-template.md). Follow the shared [artifact layout](../product-design/references/artifact-layout.md): save `task-plan.md` in the source change directory and new tasks at `tasks/<task-key>/task.md`. Project formats may change presentation but must retain one entry file per task. The [plan contract](references/plan-contract.md#development-task-record) defines the required task content.

For resumed work, scope growth, or defect returns, follow the contract's [replanning rules](references/plan-contract.md#replanning-and-feedback). Preserve stable identities, acceptance coverage, and existing branch/PR references.

## 3. Check and hand off

Complete the [plan review](references/planning-methods.md#review-the-plan) and shared [document validation](../technical-writing/references/validation-guide.md). Record actual review coverage and evidence limits. This review checks the plan; it does not prove implementation or test success.

Apply [task readiness](references/plan-contract.md#status-and-readiness) to each task. Distinguish readiness for assignment/claim from later implementation readiness. A required advance reviewer agreement can remain pending during assignment or local design, but blocks affected implementation.

Return the contract's [common handoff](references/plan-contract.md#common-handoff), including artifact versions, coverage, assignments, ready and blocked task IDs, and accountable recipients.

Project Manager coordinates the handoff. The assigned developer claims ready work, uses `git-workflow` to create or inspect its branch, then uses `technical-design` in task mode before `code-development`. If a required capability is unavailable, preserve the handoff and name the delivery blocker.
