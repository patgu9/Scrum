---
name: product-design
description: Explore vague product ideas through deep interviews. Define value, scope, and behavior through evidence, decisions, and concrete examples. Create or revise an English Design Doc in the Think stage before implementation. Use for product discovery and requirements, not visual styling or implementation planning.
---

# Product Design

Help the user decide what is worth building and how the product should behave. Produce a concise Design Doc in the Think stage. Keep questions, dependencies between questions, and review history in separate supporting documents. Code, scaffolding, tickets, and implementation require a separate request.

Read linked reference sections when the corresponding step applies. Reuse unchanged guidance already read. For a completed design, review the full document against all applicable criteria.

## 1. Establish context

Read project instructions, terminology, and evidence of current behavior. A repository is optional. Reuse the user's answers and investigate available facts. Keep current behavior, user intent, and evidence of demand distinct.

For existing work, find the current task and related designs under `doc/`. Separate approved decisions, superseded proposals, and unresolved drafts. Report conflicts that affect scope. Approval applies to the version the user approved.

Choose [Startup](references/discovery-methods.md#startup) for customer or adoption goals, or [Builder](references/discovery-methods.md#builder) for personal, learning, or creative goals. Read the applicable guidance. Ask only if the mode affects the work and remains unclear.

For a vague idea, use [deep discovery interviews](references/discovery-methods.md#deep-discovery-interviews) before offering approaches or defining scope. Reuse established context and answers.

Check the contract's [inputs and invocation context](references/document-contract.md#inputs-and-invocation-context). For downstream feedback, follow [revisit a product baseline](references/discovery-methods.md#revisit-a-product-baseline) before revising the design.

Apply [Technical Writing](../technical-writing/SKILL.md) to product documents, review reports, feedback responses, and handoff summaries.

## 2. Track decisions and dependencies

Follow the [clarification protocol](references/discovery-methods.md#clarify-decisions-and-terms) to distinguish exploration questions, fact investigations, and user decisions. Use [content placement](references/document-contract.md#content-placement) to record findings. Read [question fields](references/document-contract.md#question-records) when tracking questions and [assumption validation](references/document-contract.md#assumption-validation) when recording material assumptions.

Draft as discovery progresses. New findings can change the problem, value, scope, approaches, or examples. In steps 3–5, use the clarification protocol for new questions before continuing work that depends on the answers.

## 3. Connect value to scope

Use [Impact Mapping](references/discovery-methods.md#impact-mapping) to establish the goal, actors, and intended change in behavior before choosing deliverables.

Follow [approach comparison](references/discovery-methods.md#compare-approaches) to compare ways to achieve that goal. Apply [Occam's Razor](references/discovery-methods.md#occams-razor) when recommending a direction and refining the smallest useful scope. Obtain or reuse the user's direction under the clarification protocol.

Trace each retained Feature to the impact map. Record scope, the user journey, and costs of future changes in the contract's [assigned locations](references/document-contract.md#content-placement).

## 4. Specify Features

Read [the template](assets/design-doc-template.md) and [structure rules](references/document-contract.md#structure) before defining Features. Use the user's replacement template when requested.

Use [Specification by Example](references/discovery-methods.md#specification-by-example) to clarify behavior with the user. Record rules and examples under the contract's [Feature rules](references/document-contract.md#feature-rules).

## 5. Review and deliver

Save the Design Doc and needed supporting records using the contract's [saving rules](references/document-contract.md#saving). Keep current product conclusions and material uncertainty visible in the design; link detailed question and review records. For revisions, apply [version and approval evidence rules](references/document-contract.md#versions-and-approval-evidence).

Before delivery, use [Document Review](../document-review/SKILL.md) to validate the structure, content, and evidence of product documents, review reports, feedback responses, and handoff summaries. Keep the review within the [product review boundary](references/document-contract.md#product-review-boundary). Apply the contract's [structural requirements](references/document-contract.md#structural-validation) and [final review](references/document-contract.md#final-review) within that review.

Follow [adversarial review](references/adversarial-review.md). Then apply the contract's [status and approval rules](references/document-contract.md#status-and-approval).

Use the contract's [handoff summary](references/document-contract.md#handoff-summary) for delivery, approval requests, feedback, and blocked work. During ongoing discovery, follow its clarification-reply rules.
