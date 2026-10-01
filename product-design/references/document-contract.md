# Design Doc contract

Use the [template](../assets/design-doc-template.md) for structure. This contract owns document content, language, saving, validation, and approval rules; the [skill entrypoint](../SKILL.md) sequences the work.

## Saving

Keep one authoritative document per topic at `<project-root>/doc/design/{topic}.md`, with a lowercase, hyphenated topic name. Resolve an ambiguous project root; read before editing and reuse the topic's existing file. Resolve unrelated-file conflicts before replacing content. Keep glossary, decisions, and review findings in this document.

## Structure

Preserve this order and spelling; repeat only the Feature block. Add no preface, appendix, extra headings, or metadata fields by default.

```text
## Design Doc : <title>
- Status: DRAFT | IN_REVIEW | APPROVED
- Mode: Startup | Builder
- Date: YYYY-MM-DD
- Stage: Think

### Glossary
### Background
#### Problem Statement
#### What Makes This Cool
### Solution Design
#### Approaches Considered
#### Recommended Approach
#### Success Criteria
### Requirements
#### Feature <stable number> — <capability>
##### User Story
##### Rules
##### Key Examples
```

Features express useful capabilities, not technical layers.

Keep the template's labels, table headers, and column order. Only Constraints and Boundaries and Dependencies are optional. Replace placeholders and remove instructional comments. Preserve proper names, identifiers, and source links. Link unknowns marked TBD to an open question.

## Feature rules

Link each value → role → action story to defined SC IDs. Clarify user-visible business rules using agreed terms and concrete cases. Give rules `F<n>-AC<m>` IDs and examples `F<n>-E<m>` IDs; preserve IDs after revision, deletion, or reordering.

Illustrate every defined rule with facts, an action, and an observable result. Cover distinguishing boundaries and exceptions; never invent policies or expected outcomes. Link pending rules or outcomes to open questions and apply Status and approval below. Examples specify intended behavior, not executed tests or evidence of demand.

Use tables by default for comparable cases, or the narrative Given/When/Then format below when clearer. Do not duplicate formats. Retain full IDs and references to one or more applicable rules:

```markdown
**F1-E1: Scenario name**
- **Related Rule:** F1-AC1
- **Given:** Concrete context and input.
- **When:** Business action or event.
- **Then:** Observable result.
```

## Content placement

| Content | Location |
|-----|-----|
| Problem, actors, workaround, demand, and sources | Problem Statement and Evidence |
| Canonical terms and boundaries | Glossary |
| Meaningful alternatives; benefits, drawbacks, effort (S/M/L/XL), risk (Low/Medium/High), reuse, rejection reasons | Approaches Considered |
| Selected approach and rationale, or explicitly pending choice | Recommendation |
| Goal–actor–impact–deliverable links; trigger, handoffs, outcome, distribution, shared dependencies | How It Works; diagrams may be embedded here |
| Initial audience, smallest useful outcome, included Features, exclusions | Scope |
| Premises, assumptions, open decisions, unresolved review findings; approval impact and follow-up | Premises and Open Questions |
| Outcome and verification; quantitative baseline, target, units, population, window | Success Criteria |
| Value → role → action, SC links, rules, and acceptance examples | Feature blocks |
| One action and observable result: validate demand or a critical assumption for Startup; try a usable outcome for Builder | Next Action |

Link evidence beside claims. Mark causal uncertainty in Premises and Open Questions. Every row there needs `Blocks approval: Yes / No` with a reason. Do not add separate impact-map or review sections.

## Status and approval

- **DRAFT:** incomplete discovery or approval blockers remain. If the user skips questions, record explicit unknowns; proposals and silence are not decisions or approval.
- **IN_REVIEW:** complete, agreed direction, no approval blockers; present the document for confirmation.
- **APPROVED:** the user explicitly approved this version, with blockers resolved or affected scope excluded by agreement. Approval does not validate assumptions.

Core user, scope, or behavior questions block approval unless the affected scope is excluded by agreement. Material changes to goals, scope, rules, or outcomes return to DRAFT and require a user decision unless already authorized. Check affected terminology, SCs, stories, and examples; move to IN_REVIEW when complete and unblocked. Typographic edits alone preserve approval.

## Document language

Write the Design Doc in plain, concise English. Adapt the reading principles of `i-have-adhd` to a standalone specification. These rules apply to every section, including tables, rules, and examples. Keep the required structure; do not add chat-style progress updates or an action before the title. The rules below are self-contained and do not require another skill.

1. **Lead with the point.** Start each section or field with its decision, behavior, or result. Follow with only the explanation needed to understand it. Remove preambles, promotional claims, tangents, and closing recaps.
2. **Use plain words and direct verbs.** Name who does what. Prefer “use,” “save,” and “choose” over abstract phrases such as “facilitate utilization” or “enable artifact delivery.” Keep necessary domain terms, define them in Glossary, and use them consistently. Avoid metaphors, ornamental adjectives, and invented compound terms.
3. **Keep each sentence focused.** Use short sentences and paragraphs. Split conditions, actions, and exceptions when a sentence becomes hard to follow. Keep table cells brief. Do not enforce a word limit that removes meaning.
4. **Make actions easy to scan.** Number sequential steps in How It Works. Aim for at most five items per prose list; group longer lists within existing fields. This is not a limit on rules, examples, glossary entries, or table rows: retain all required content and stable IDs. Next Action names one action and its observable result. Use concrete time estimates only when supported; otherwise state the uncertainty.
5. **State facts once, preserve precision.** Put a rule in Rules and refer to its ID elsewhere instead of copying it. Keep evidence, verification limits, and review history in their assigned fields; repeat them only when needed to prevent misunderstanding. Describe failures as cause, outcome, and next action; label unknown causes. Preserve conditions, exclusions, units, sources, approval state, and genuine uncertainty. Never shorten “not verified” into a claim of success.

Examples of wording changes, not additional product requirements:

| Wordy | Plain |
|-----|-----|
| The invocation's current directory serves as the default destination for artifact delivery. | Save the file in the current directory by default. |
| Missing or conflicting evidence requires explicit user selection. | If evidence is missing or conflicting, ask the user to choose. |
| It remains an implementation feasibility gate. | Check that this works before calling the implementation complete. |

## Final review

1. **Value and scope:** Can the document stand alone? Check the problem, evidence, actors, behavioral impact, smallest useful outcome, alternatives, estimate uncertainty, and actual selection. Label hypotheses and distinguish current from desired behavior.
2. **Journey and language:** Check consistent terms, triggers, handoffs, dependencies, distribution, and outcomes across Features. Apply Document language: replace abstract wording, split dense sentences, and remove repeated explanations. Confirm that the edit preserves every condition, exception, and verification limit.
3. **Verifiable behavior:** Link stories to valid SCs and every defined rule to concrete examples. Check units, boundaries, exceptions, and unchanged state. Quantitative goals need metric definitions and measurement context; explain how to establish unknown baselines. Builder may use a qualitative demonstration.
4. **Decisions and approval:** Apply Status and approval to the current version and its unresolved questions.
5. **Completion:** Check a concrete Next Action and compliance with the entrypoint's scope boundary.

## Structural validation

Run `python3 <skill-dir>/scripts/validate_design.py <document-path>`; add `--template <path>` for a user-supplied replacement.

Repair structural defects without changing decisions. If Python is unavailable, check manually and disclose the unrun validation.

The validator checks headings, metadata, labels, tables, placeholders, IDs, example coverage, and explicit blockers. It cannot verify English quality, factual truth, causal reasoning, user consent, or discovery completeness. Complete the review above even after a pass.

A valid DRAFT may contain pending behavior or linked TBDs. When even a provisional Feature would be invented, save an incomplete DRAFT and report unmet structural requirements. Never fabricate content to pass validation.
