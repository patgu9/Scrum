---
name: product-design
description: Explore product needs, choose opportunities and scope, define success, and specify behavior with examples. Create or revise an English Design Doc in the Think stage. Use for product discovery and requirements, not visual styling or implementation planning.
---

# Product Design

Help the user decide what is worth building and how it should behave. Stop at product discovery and design unless downstream work is separately requested.

## Working references

Read only the sections needed for the current step. Each reference has one responsibility:

| Reference | Use for |
| --- | --- |
| [Discovery and decisions](references/discovery-methods.md) | Interviews, clarification, opportunity selection, tradeoffs, validation, and feedback |
| [Document contract](references/document-contract.md) | Output placement, evidence records, versions, approval, and handoffs |
| [Product review](references/adversarial-review.md) | Review scope, checks, findings, and the bounded review loop |
| [Design](assets/design-doc-template.md), [questions](assets/questions-template.md), [review record](assets/review-template.md) | Output layouts; create supporting files only when needed |

## 1. Establish context

Read project instructions, terminology, current behavior, and relevant designs. A repository is optional. Check the contract's [inputs and route](references/document-contract.md#inputs-and-invocation-context); distinguish approved baselines, superseded proposals, and unresolved drafts.

Choose [Startup](references/discovery-methods.md#startup) for customer or adoption goals, or [Builder](references/discovery-methods.md#builder) for personal, learning, or creative goals. Ask only if the distinction remains material and unclear. For feedback on existing work, use [baseline revision](references/discovery-methods.md#revisit-a-product-baseline).

## 2. Discover and decide

Use [interviews](references/discovery-methods.md#deep-discovery-interviews) when the need is unclear and the [clarification protocol](references/discovery-methods.md#clarify-decisions-and-terms) for unresolved facts and decisions. Reuse established answers and draft as discovery progresses.

Connect the [selected opportunity and behavioral impact](references/discovery-methods.md#opportunity-selection-and-impact-mapping) to the goal. Define [observable success](references/discovery-methods.md#outcomes-and-metrics), then [compare approaches](references/discovery-methods.md#compare-approaches) and refine scope with Occam's Razor. Use strategy, prioritization, adoption, or validation guidance only when it can affect the decision.

## 3. Specify and save

Use [Specification by Example](references/discovery-methods.md#specification-by-example) to establish rules and distinguishing cases. Follow the document contract and selected templates. Keep current conclusions and material uncertainty in the design; put question and review history in supporting records.

Apply [Technical Writing](../technical-writing/SKILL.md). For revisions, preserve the baseline and approval evidence under the contract before changing handed-off content.

## 4. Review and deliver

Follow [Product review](references/adversarial-review.md), then the contract's [status and approval rules](references/document-contract.md#status-and-approval). Deliver its [handoff summary](references/document-contract.md#handoff-summary). During discovery, continue the clarification loop instead of issuing a full handoff after each answer.
