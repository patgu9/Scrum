---
name: product-design
description: Define product value, scope, and behavior through focused questions and concrete examples. Create or revise an English Design Doc in the Think stage before implementation. Use for product discovery and requirements, not visual styling or implementation planning.
---

# Product Design

Help the user decide what is worth building and how the product should behave. Produce a Design Doc in the Think stage. Code, scaffolding, tickets, and implementation require a separate request.

## 1. Establish context

Read project instructions, terminology, and evidence of current behavior. A repository is optional. Reuse the user's answers and investigate available facts. Keep current behavior, user intent, and evidence of demand distinct.

Find related designs in `doc/design/`, `docs/designs/`, or the user's chosen location. Separate approved decisions, superseded proposals, and unresolved drafts. Report conflicts that affect scope. Approval applies to the version the user approved.

Read [discovery methods](references/discovery-methods.md) to choose a mode and guide questions and decisions.

Read the [Technical Writing Skill](../technical-writing/SKILL.md) before drafting. Apply its writing method to explanations, document prose, tables, rules, and examples.

## 2. Track decisions and dependencies

Read the [document contract](references/document-contract.md) before recording decisions. Follow the [clarification protocol](references/discovery-methods.md#clarify-decisions-and-terms) to track questions and dependencies. The contract defines where to save these records.

Draft as discovery progresses. New findings can change the problem, value, scope, approaches, or examples. In steps 3–5, use the clarification protocol for new questions before continuing work that depends on the answers.

## 3. Connect value to scope

Use [Impact Mapping](references/discovery-methods.md#impact-mapping) to connect each Feature to a goal, actors, and the intended change in behavior.

Follow [approach comparison](references/discovery-methods.md#compare-approaches) to compare ways to achieve the same user goal. Choose a direction with the user. Then define the smallest useful scope and the cost of future changes.

Record scope and the user journey in the contract's [assigned locations](references/document-contract.md#content-placement).

## 4. Specify Features

Read [the template](assets/design-doc-template.md) before defining Features. Use the user's replacement template when requested.

Use [Specification by Example](references/discovery-methods.md#specification-by-example) to clarify behavior with the user. Record rules and examples under the contract's [Feature rules](references/document-contract.md#feature-rules).

## 5. Review and deliver

Save the document using the contract's [saving rules](references/document-contract.md#saving).

Complete the contract's [final review](references/document-contract.md#final-review). Then run [structural validation](references/document-contract.md#structural-validation).

Follow [adversarial review](references/adversarial-review.md). Then apply the contract's [status and approval rules](references/document-contract.md#status-and-approval).

Report the saved path, document Status, blockers, review coverage, and Next Action.
