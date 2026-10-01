---
name: product-design
description: Clarify product value, scope, and behavior through focused questions and concrete examples. Create or revise an English Think-stage Design Doc before implementation; not for visual styling or implementation planning.
---

# Product Design

Help the user choose what is worth building and define its behavior. Stop at Think: code, scaffolding, tickets, and implementation require a separate request.

## 1. Establish context

Read relevant project instructions, existing designs, terminology, and evidence of current behavior. A repository is optional. Reuse supplied answers; investigate available facts yourself. Distinguish implementation, user intent, and evidence of demand.

Find related designs in `doc/design/`, `docs/designs/`, or user-specified locations. Separate approved decisions from superseded proposals and unresolved drafts. Raise conflicts that affect scope; prior approval does not approve a revision.

Read [discovery methods](references/discovery-methods.md) for mode selection, conversation rules, and decision methods. Apply them throughout discovery.

## 2. Resolve decisions

Use [decision clarification](references/discovery-methods.md#clarify-decisions-and-terms) to resolve choices in dependency order.

Draft throughout discovery using the [document contract](references/document-contract.md). Keep unresolved choices visible and continue independent work while answers are pending.

## 3. Connect value to scope

Use [Impact Mapping](references/discovery-methods.md#impact-mapping) to connect each Feature to its goal and actors.

Follow [approach comparison](references/discovery-methods.md#compare-approaches) to select a direction with the user.

Define scope and the user journey using the contract's [content placement](references/document-contract.md#content-placement).

## 4. Specify Features

Read [the template](assets/design-doc-template.md) before specifying Features. Use a user-supplied replacement template when requested.

Use [Specification by Example](references/discovery-methods.md#specification-by-example) to clarify behavior with the user. Apply the contract's [Feature rules](references/document-contract.md#feature-rules) and [document language](references/document-contract.md#document-language) when recording it.

## 5. Review and deliver

Save the document using the contract's [saving rules](references/document-contract.md#saving).

Complete the contract's [final review](references/document-contract.md#final-review) and [structural validation](references/document-contract.md#structural-validation).

Follow [adversarial review](references/adversarial-review.md), then apply the contract's [status and approval rules](references/document-contract.md#status-and-approval).

Finish with the saved path, status, blockers, review coverage, and the document's Next Action.
