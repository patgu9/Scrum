# Technical writing guide

Use [Google Technical Writing](https://developers.google.com/tech-writing) to decide what readers need and in what order. For English, then apply the [English controls](english-controls.md). Routine use does not require reopening the sources.

Write in the language requested by the user or required by the project. The calling workflow owns the format, domain rules, and approval process. A writing edit must preserve decisions, conditions, exceptions, IDs, sources, units, and uncertainty. Resolve missing meaning through that workflow; do not invent facts to make a sentence complete.

## Write for the reader

Identify the reader's goal, existing knowledge, and missing knowledge. Select content that closes the gap. Distinguish the document's readers from the product's users. Explain unfamiliar concepts; link background that readers can consult separately. Avoid internal shorthand, idioms, and cultural references. See [Audience](https://developers.google.com/tech-writing/one/audience).

For a substantial draft, use a brief working outline:

- Who will read this, and what do they already know?
- What must they understand, decide, or do after reading?
- Which questions must the document answer to support that outcome?
- What is outside scope but could reasonably be expected here?

Use the answers to write the document; do not add a planning questionnaire to the deliverable. For a small edit, infer these answers from the surrounding text. State the relevant scope and prerequisites in the locations assigned by the template. See [Documents](https://developers.google.com/tech-writing/one/documents).

## Order explanations by need

Put the main point early. Introduce a concept before relying on it, and give prerequisites before the task that needs them. Add detail where it becomes useful. Use headings that help readers find a question, concept, or task. See [Organizing large documents](https://developers.google.com/tech-writing/two/large-docs).

Choose the order from the reader's purpose. These are patterns within the required format, not replacement templates:

| Reader's purpose | Useful order |
| --- | --- |
| Understand behavior | Main behavior → necessary concepts → concrete example → relevant limits |
| Complete a task | Goal and prerequisites → steps → expected result → supported recovery actions |
| Assess a proposal | Problem and proposal status → proposed behavior → evidence and tradeoffs → unresolved decisions |
| Find a reference detail | Stable name → meaning or contract → inputs and outputs → limits and examples |

Keep required headings, fields, and their order. Improve the explanation within those boundaries. Put optional background behind a link when it interrupts the reader's task. Do not move an exception away from the rule it limits.

For Skill instructions, address the agent performing the task. Keep routing in `SKILL.md` and detailed rules in references. Give each rule one authoritative location and link to it where needed.

## Lead each paragraph with its point

Begin with the behavior, result, problem, or decision that the paragraph explains. Follow with the reason or evidence needed to assess it. Keep one topic per paragraph and connect adjacent sentences. Remove preambles, tangents, promotional claims, and repeated recaps. See [Paragraphs](https://developers.google.com/tech-writing/one/paragraphs).

Prefer an explicit actor and a specific action. Replace vague claims such as “fast” or “easy” with supported measurements or observable behavior. When evidence is missing, retain the uncertainty or open question. Never invent a target to make a claim sound precise. See [Clear sentences](https://developers.google.com/tech-writing/one/clear-sentences).

## Keep terms and references clear

Use one name for each concept. Define unfamiliar terms and acronyms where readers first need them, or link to the existing definition. Avoid new acronyms for terms used only a few times. Preserve proper names, UI labels, and exact identifiers. See [Words](https://developers.google.com/tech-writing/one/words).

Replace an ambiguous pronoun with its intended actor or object. Repeat the noun when several referents are possible. Distinguish different operations: structural validation, assumption validation, and user approval do not mean the same thing. If the source does not establish the distinction, flag the ambiguity instead of choosing a meaning.

## Keep sentences focused

Use four moves from [Short sentences](https://developers.google.com/tech-writing/one/short-sentences):

1. Split independent ideas when the sentence changes actor, stage, or topic.
2. Expose embedded sequences or alternatives as lists when that helps the reader.
3. Remove filler and replace indirect expressions with direct verbs.
4. Move side topics into separate sentences; retain clauses that restrict the rule.

Keep a condition with its action. Preserve causes, sequence, alternatives, and simultaneous actions when splitting. Retain “only,” “unless,” “at least,” negation, permission, obligation, and verification limits. These words carry meaning.

| Before | After | Meaning to retain |
| --- | --- | --- |
| When an import starts, the tool checks access, retrieves the document if access is allowed, and saves it after retrieval succeeds. | When an import starts, the tool checks access. If access is allowed, the tool retrieves the document. After retrieval succeeds, the tool saves the document. | Both gates and the action order |
| Files that exceed 10 MB are rejected. | Files larger than 10 MB are rejected. | The threshold excludes files of exactly 10 MB |
| The report, which the team uses in its weekly review, summarizes failed imports. | The report summarizes failed imports. The team uses the report in its weekly review. | The review detail remains available |

These examples illustrate edits; they do not introduce product requirements or claim STE compliance. Reread the passage after splitting so that it remains connected prose.

## Choose lists, tables, and examples deliberately

Use numbered steps when order matters, bullets for unordered items, and tables to compare the same attributes across cases. Keep list items parallel in grammar and detail. Give lists and tables context through a heading, field label, or brief introduction. See [Lists and tables](https://developers.google.com/tech-writing/one/lists-and-tables).

Keep a shared condition in the introduction so it applies to every item. State whether alternatives permit one choice or several. Do not turn “A or B” into steps that require both. Group long lists by topic when helpful; preserve required headers and columns. Do not delete rules or examples merely to shorten a table.

Place an example beside the explanation it supports. Use a simple case first, then a boundary or failure case when needed. Keep example terms and values consistent with the documented behavior. Mark hypothetical examples; do not present them as observed results. For code samples, give the necessary setup, input, and expected output. Verify executable samples when permitted; report samples that were not run. See [Sample code](https://developers.google.com/tech-writing/two/sample-code).

## Keep evidence and visuals useful

State each fact or rule in its assigned location, then use a cross-reference or stable ID. Put source links beside the claims they support. Use descriptive link text. Keep uncertainty, verification limits, and review history in their assigned fields; repeat only when needed to prevent misunderstanding.

For a user-visible failure, explain what failed and the available recovery action. Give a cause only when supported. Never turn “not verified” into success. See [Writing Helpful Error Messages](https://developers.google.com/tech-writing/error-messages).

Use a diagram when it clarifies a relationship or flow. Place it beside the relevant text and explain its essential meaning there. Give informative images concise alt text; use empty alt text for decorative images. See [Write helpful alt text](https://developers.google.com/tech-writing/accessibility/self-study/write-alt-text).

## Edit in separate passes

Review in this order, adapted from [Self-editing](https://developers.google.com/tech-writing/two/editing). These passes supplement the calling workflow's checks.

1. **Content and order:** Can readers find the information needed for their goal? Are prerequisites and concepts introduced before use? Keep each rule in its assigned location and remove irrelevant material.
2. **Expression:** Check sentence focus, actors, references, examples, and list and table structure. For English, apply [English controls](english-controls.md), including the distinction between instructions and descriptions.
3. **Meaning:** Compare source and revision. Verify the same actors, actions, conditions, exceptions, sequence, alternatives, negation, limits, units, IDs, evidence, uncertainty, and approval state. A wording change cannot settle an unresolved decision.
4. **Reader walkthrough:** Follow a documented task or answer the document's main question using only the text and its stated prerequisites. Identify missing steps or unexplained terms. Treat this as a text review, not evidence that the product or procedure works.

Report unresolved meaning and checks that were not performed. Automated structure and style checks do not establish factual truth, approval, reader comprehension, or STE compliance.
