# Adversarial review

Before presenting a completed Design Doc for approval, use an independent reviewer when available and authorized. Otherwise complete the document-contract self-review and report independent review as unrun, with the reason.

## Inputs and findings

Provide the complete current document, template, contract, relevant evidence and prior designs, and prior-round findings and remedies. Ask the reviewer to read these directly and challenge:

- **Completeness:** missing actors, journey steps, dependencies, distribution, rules, or examples.
- **Consistency:** conflicting terms, scope, criteria, behavior, or decisions.
- **Clarity:** ambiguous outcomes or open choices presented as settled.
- **Scope:** unsupported Features, missing causal links, or weak alternatives.
- **Feasibility:** unsupported adoption, behavior, reuse, or architecture assumptions.

Each finding needs a section or stable ID, problem, evidence or counterexample, consequence, remedy or question, and approval impact with a reason. Distinguish unknown facts from contradictions; user agreement is not empirical validation. Later rounds identify new, persisting, and resolved findings with evidence from the revision.

## Review loop — maximum three attempts

1. Review the completed draft. Every dispatch counts, including failed attempts.
2. Stop before editing if no findings remain, the third attempt is complete, new evidence or a user decision is required, or a previously addressed issue persists without meaningful progress.
3. Otherwise repair wording or structure within the agreed design. Apply the contract's [status and approval rules](document-contract.md#status-and-approval) to any material change.
4. Revalidate structure and submit the complete revision with prior findings. Claim resolution only when supported by reviewer evidence.

On failure, timeout, or invalid output, stop and report incomplete coverage. Retain usable findings and concrete evidence for stalled issues.

## Record and approval

Record findings using the contract's [content placement](document-contract.md#content-placement). Preserve every unresolved finding and its remedy across revisions.

Report review mode, attempts/completed rounds, unresolved findings, and missing coverage. Use the contract's status and approval rules for the final document state.
