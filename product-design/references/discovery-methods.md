# Discovery methods

Infer Startup or Builder from the goal; ask only when the distinction affects the work. Use the relevant mode and unresolved decisions; do not administer every question. Converse in the user's language.

## Conversation rules

1. Lead with the current decision or next action. State progress briefly each turn; omit preambles, repeated recaps, and pleasantries.
2. Number multi-step work. Show at most five items per group; preserve the full specification even when discussion is brief.
3. Ask one high-impact question by default, up to three independent questions per round. Ask only when prerequisites are settled; dependent questions wait for answers. Resolve side issues independently or defer them.
4. Use concrete time estimates when supported, with their basis and uncertainty. Report errors as cause and next action; never invent precision.
5. End unfinished work with one action the user can start within two minutes. Explain fully when requested; brevity must not remove evidence, uncertainty, or required decisions.

## Startup

Use for products seeking customers or internal initiatives needing adoption and support.

| Area | Establish |
|-----|-----|
| Demand and actor | A specific role, task, observed behavior, commitment, or cost. Interest and signups do not prove willingness to pay; missing customers is an unknown. |
| Workaround | Current workflow, its cost, what breaks, and who influences adoption. Include manual work and doing nothing. |
| Smallest scope | One valuable outcome. Internal projects may use concrete adoption or resource commitments instead of payment. |
| Observation | Uncoached use and contradictory results. Distinguish observation from demos and surveys. |
| Future relevance | Changes that strengthen or weaken value; organizational resilience when relevant. Label uncertainty. |

Without users, prioritize demand, workaround, and actor. With users, prioritize workaround, scope, and observation. With paying customers, prioritize scope, observation, and future relevance. For infrastructure, start with the workflow and a narrow improvement. Avoid unnecessary personal information.

## Builder

Use for personal tools, learning, research, open-source exploration, demos, and creative work. Completion, enjoyment, and learning are valid goals.

- What would be exciting to use or show?
- Who would try it, and what would they do?
- What is the fastest route to a usable result?
- Which existing tool is closest, and what difference matters?
- What unexpected use could the capability enable?

Explore a distinct possibility without expanding scope by default. Do not require revenue metrics or customer interviews for a personal tool.

## Clarify decisions and terms

Track each open decision's prerequisites, evidence, recommendation, and design impact. Separate facts to investigate from user choices. Offer a recommendation with a reason for choices and a way to investigate unknown facts. Wait before dependent work. Reopen decisions only when new evidence or a dependent change warrants it.

Test ambiguous claims and terms with concrete counterexamples. If “sharing” could mean a public link or workspace invitation, settle audience and access before invitation expiry. Independent questions can proceed.

Read existing domain guidance, including CONTEXT.md or CONTEXT-MAP.md when present. Expose conflicting meanings instead of overwriting terminology. Verify current behavior against code when available; record current and desired behavior separately.

Record conclusions using the contract's [content placement](document-contract.md#content-placement). Separate domain documents or ADR edits require a separate request.

## Compare approaches

Compare at least two meaningful approaches:

- **Minimal implementation:** smallest useful scope, fastest delivery, and reuse.
- **Ideal architecture:** long-term boundaries and expected evolution, with added cost and complexity.

Consider doing nothing and existing solutions; add a third approach only when distinct. Use the contract's Approaches Considered fields. Explain estimate uncertainty and keep architecture detail at the level needed to choose. Recommend an approach and obtain the user's choice unless already supplied or authorized.

## Impact Mapping

Trace **goal → actor → behavioral impact → deliverable** for every Feature to expose investment assumptions. Challenge unsupported links, label causal hypotheses, justify dependencies, and consider non-software alternatives. Example hypothesis:

`SC1: shorten approval turnaround → approver → reviews pending requests daily → F1: pending-request digest`

A dashboard is a deliverable; noticing stalled requests is a behavioral impact. A changed team practice may achieve the same result. Record the links and hypotheses using the contract's content placement. Retain enabling or obstructing actors even without their own stories.

Source: [Drawing impact maps](https://www.impactmapping.org/drawing.html).

## Specification by Example

Use concrete cases to discover and refine rules with the user; retain cases that distinguish behavior.

For a confirmed limit of 10 entries, compare additions at 9 and 10, including final count and unchanged state on rejection. Do not choose the limit yourself. For “prevent duplicates,” compare `https://example.com/a` with `https://example.com/a/` to ask about equality before specifying normalization.

Repetitive examples may indicate a missing concept or distinct rules. Use the contract's [Feature rules](document-contract.md#feature-rules) to record them. Scenario count and syntax do not establish agreement.

Sources: [Specifying with examples](https://gojko.net/2008/11/04/specifying-with-examples/), [Focus on key examples](https://gojko.net/2014/05/05/focus-on-key-examples/).
