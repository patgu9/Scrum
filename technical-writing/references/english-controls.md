# English expression controls

Apply these controls after the [writing guide](writing-guide.md) has established content and order. They combine Google's sentence guidance with selected ASD-STE100 principles for software documentation, requirements, and Skill instructions.

## Scope of STE use

The default is an adaptation, not a claim of full STE compliance. Keep the project's English variant and exact code, commands, paths, UI labels, identifiers, and quotations. Explain an unclear identifier in prose instead of renaming it.

STE controls both writing rules and vocabulary. Its dictionary restricts word meanings and parts of speech; domain terms follow separate rules. For example, `check` is approved as a noun, not a general verb. Clear ordinary English is therefore not automatically STE.

If full compliance is explicitly required, use the applicable edition's complete rules and dictionary, plus the project's domain vocabulary. Record unresolved entries or conflicts. If the standard is unavailable, continue useful editing and report compliance as unverified. Do not invent dictionary approvals or use this short guide as a substitute.

## Control words and their meanings

Use the project's established term consistently, with one intended meaning. Prefer literal, familiar words. Distinguish objects, states, and actions. When a term is overloaded, add a qualifier supported by the source. Avoid synonym changes made only for variety.

Keep a small working term list when several terms could drift: term, intended meaning, and exact label or identifier if relevant. Reuse an existing glossary; do not create a new artifact for every edit. This is a local consistency aid, not an STE-approved dictionary.

Rewrite dense noun groups with prepositions or clauses. For example, “retry limit for failed imports” makes the relationship clearer than “failed import retry limit.” Retain official compound names. Put each modifier beside the word it qualifies.

## Distinguish instructions from descriptions

- Instructions use commands. Give one instruction per sentence, except for actions that must occur together (rules 5.2–5.3).
- Put a condition first when the reader needs it before acting (rule 5.4).
- Keep required actions out of informational notes (rule 5.5).
- STE limits procedural sentences to 20 words and descriptive sentences to 25 (rules 5.1 and 6.3).
- Restructure a sentence when substituting individual words does not work (rule 9.1).

For this Skill's default adaptation, use the sentence limits as review triggers. Shorten long sentences when possible; retain a longer sentence if splitting would obscure a condition or exact term. For full compliance, apply the standard's limits and counting rules, including section 8, rather than a whitespace count.

A requirement describes an obligation; it is not automatically an instruction to the reader. Preserve its actor and modal verb. In mixed documents, classify the passage, not the whole file.

| Passage                   | Preferred expression                                      | Preserve                |
| ------------------------- | --------------------------------------------------------- | ----------------------- |
| Instruction to the reader | “If the export fails, save the error log.”                | Condition before action |
| System behavior           | “The service saves the report after the export succeeds.” | Actor and sequence      |
| Requirement               | “The service must retain failed jobs for 7 days.”         | Obligation and duration |
| Proposal                  | “Proposal: retain failed jobs for 7 days.”                | Unapproved status       |

Examples in this file illustrate local edits; they have not been checked against the complete STE dictionary.

## Make grammar explicit

Prefer active statements. In instructions, address the reader directly. For descriptions, STE permits passive voice when the actor is unknown; do not invent an actor. Inspect ambiguous `-ing` forms, while preserving established technical nouns that contain them.

For this adaptation, rewrite when the actor, relationship, or timing is unclear:

| Unclear or indirect                                  | Clearer when supported by the source                            |
| ---------------------------------------------------- | --------------------------------------------------------------- |
| After saving the file, it is checked.                | After the editor saves the file, the validator checks the file. |
| Processing files can delay shutdown.                 | Shutdown can be delayed while the service processes files.      |
| Perform a review of the draft.                       | Review the draft.                                               |
| In the event that retrieval fails, notify the owner. | If retrieval fails, notify the owner.                           |

The first two rewrites require knowledge of the actor and intended meaning. If the source does not supply it, flag the ambiguity. Preserve meaningful timing and state; do not mechanically remove every `-ing` ending or change every tense.

For ordinary English, prefer specific verbs over nominal phrases. In full STE work, dictionary restrictions can require a different construction; do not override them with a general preference for shorter wording.

In US English, `that` usually introduces an essential restriction; `which` with commas adds supplementary information. “Reports that contain failures need review” does not apply to all reports. Preserve the restriction and follow the project's English variant.

## Preserve logical force

Treat these distinctions as meaning checks, not stylistic substitutions:

- `must` states an obligation; `may` can grant permission; `can` can describe capability. Use the document's defined requirement vocabulary.
- `only if` states a necessary condition. Replacing it with `if` can change the rule.
- `before`, `after`, `until`, and `while` express different timing. Preserve their scope across sentence breaks.
- `and`, `or`, `at least`, and `exactly` affect allowed combinations and limits.
- `proposed`, `not verified`, and `approved` express different evidence or decision states.

Compare the revised passage with the source. If a shorter expression changes any of these distinctions, retain or rewrite the longer expression.
