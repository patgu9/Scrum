# Discovery methods

Choose Startup or Builder from the user's goal. Ask the user to choose only if the distinction affects the work and remains unclear. Use the mode and unresolved decisions to guide discovery. The questions below are prompts, not a required questionnaire. Follow the [Technical Writing Skill](../../technical-writing/SKILL.md) for wording and presentation.

## Conversation rules

Use these rules to pace the conversation:

- Briefly state progress in each conversation turn.
- Use the [clarification protocol](#clarify-decisions-and-terms) to select questions, pace each round, and retain unanswered questions.
- Give a time estimate only when evidence supports it. State the basis and uncertainty.
- When ending unfinished work, give one action the user can start within two minutes. Provide a full explanation when requested. Keep required evidence and decisions in the response.

## Startup

Use Startup for products seeking customers or internal projects that need adoption and support.

| Area | Establish |
|-----|-----|
| Demand and actor | Identify the role and task. Look for observed behavior, commitments, or costs. Interest and signups do not prove willingness to pay. Demand is unknown without customer evidence. |
| Workaround | Describe the current workflow, its cost, failures, and people who influence adoption. Include manual work and doing nothing. |
| Smallest scope | Define one valuable outcome. For internal projects, concrete adoption or resource commitments may replace payment evidence. |
| Observation | Observe use without coaching. Look for results that contradict the assumptions. Distinguish observation from demos and surveys. |
| Future relevance | Identify changes that could increase or reduce value. Consider the organization's ability to adapt and continue operating when relevant. Mark uncertainty. |

Choose the discovery focus from the available evidence:

- **No users:** Prioritize demand, workaround, and actor.
- **Users:** Prioritize workaround, scope, and observation.
- **Paying customers:** Prioritize scope, observation, and future relevance.
- **Infrastructure:** Start with the workflow and a narrow improvement.

Avoid unnecessary personal information.

## Builder

Use Builder for personal tools, learning, research, open-source exploration, demos, and creative work. Completion, enjoyment, and learning are valid goals.

- What would be exciting to use or show?
- Who would try it, and what would they do?
- What is the fastest route to a usable result?
- Which existing tool is closest, and what difference matters?
- What unexpected use could the capability enable?

Explore an unexpected use without adding it to scope by default. Do not require revenue metrics or customer interviews for a personal tool.

## Clarify decisions and terms

Use this protocol during discovery, specification, and review. New findings may require revisiting the problem definition. The document contract defines [where to record questions](document-contract.md#content-placement) and [when the document can be approved](document-contract.md#status-and-approval).

Read existing domain guidance, including `CONTEXT.md` or `CONTEXT-MAP.md` when present. Report conflicting meanings instead of replacing established terms. Use code to verify current behavior when available. Record current and desired behavior separately.

Use these question states. Question states describe individual questions; document Status describes the Design Doc as a whole.

| State | Meaning |
|-----|-----|
| `OPEN` | The question is unresolved. |
| `INVESTIGATING` | You are gathering facts. |
| `WAITING` | You asked the question and are waiting for the user's answer. |
| `RESOLVED` | Evidence supports the fact, or the user authorized the decision. |
| `UNKNOWN` | Evidence is unavailable, or the user answered “I don't know” or “skip.” |
| `EXCLUDED` | The user agreed to remove the affected scope. |

Follow this loop as evidence and decisions change:

1. **Record questions and dependencies.** Give each unresolved question a stable `Q<n>` ID. Never renumber or reuse a question ID. Use `Fact to investigate` or `User decision` as the question type.

   Use the contract's [question fields](document-contract.md#content-placement). List dependencies on other questions or unfinished investigations. State when a dependency applies only to a particular approach. Keep resolved and excluded records so readers can trace later changes.

2. **Set the question state.** A recommendation, silence, or an unanswered option does not resolve a question. When you reopen a question, set its state to `OPEN`. Keep the previous answer and the reason for reopening.

3. **Investigate facts before asking for a decision.** Inspect available project files and code. Use available tools to gather facts. Record unfinished investigations as unresolved prerequisites. Pause work that depends on those investigations. Continue independent decisions and drafting.

   If evidence is unavailable, use `UNKNOWN`. State what evidence is needed and discuss how to validate the assumption or exclude the affected scope. Never present an unknown as a fact.

4. **Choose the next questions.** Update conditional dependencies after new evidence, an answer, or a scope change. Consider only unresolved user decisions relevant to the current scope. Ask a question only when its prerequisites are resolved and its state is not `WAITING`. Prioritize decisions by their impact and the work an answer would allow.

   Ask one question by default. Ask at most three mutually independent questions in one round. Keep the other questions for later. Do not start another round while answers are pending. Continue independent investigation and drafting.

   If a new direction or scope change makes a waiting question irrelevant, record the reason. Do not mark that question as answered.

5. **Explain the decision.** State what the user needs to decide, why it matters now, and which content it affects. Present the main options and tradeoffs. Give your recommendation and reason.

   Reuse a prior explicit answer or authorization within its scope. Otherwise wait for the user's decision. Never record your recommendation as a confirmed rule.

6. **Record partial answers and uncertainty.** Set asked questions to `WAITING`. Resolve only the questions the user answers. Keep the unanswered questions. For “I don't know” or “skip,” use `UNKNOWN`. Propose a step to gather evidence or ask whether to exclude the affected scope.

   Skipping does not exclude scope or accept a recommendation. Put Q IDs beside pending content. Do not state a definite conclusion that depends on an unconfirmed answer.

7. **Apply answers and changes.** Save each answer with its basis and source. Update dependencies. Check affected terms, Success Criteria, Features, rules, and examples.

   If an earlier decision changes, mark content based on that decision for review. Reopen only affected dependent decisions. Keep a dependent decision resolved only after checking that its basis still holds. Preserve unaffected decisions. Add new questions to this loop.

8. **Check blockers and finish discovery.** An empty question queue does not prove that clarification is complete. Check unfinished investigations, waiting answers, unknowns, and cycles in question dependencies. Report the blocker and next action. Break a cycle by clarifying the decision that governs the dependent questions or investigating the unknown fact. Do not resolve a question without a basis.

   When discovery is complete, apply the contract's [status and approval rules](document-contract.md#status-and-approval), including the team or standalone approval route. Set `APPROVED` only from explicit human approval of the current version.

Use concrete counterexamples to clarify ambiguous claims and terms. For example, “sharing” may mean a public link or a workspace invitation. Decide the audience and access rules before invitation expiry. Independent questions can proceed.

For a hypothetical research-sharing design, dependencies might look like this:

| Question | Purpose | Dependency |
|-----|-----|-----|
| Q1 | Choose the audience. | None. |
| Q2 | Investigate existing organization membership. | None. |
| Q3 | Decide who can change access. | Q1. Also Q2 if access is limited to organization members. |
| Q4 | Decide link expiry. | Relevant only if the selected approach uses links. |

Ask Q1 while investigating Q2. After the audience decision, reassess the remaining questions.

Record conclusions using the contract's [content placement](document-contract.md#content-placement). Editing separate domain documents or architecture decision records (ADRs) requires a separate request.

## Revisit a product baseline

Use this path when engineering, planning, development, review, QA, or Ops returns evidence that challenges product value, scope, behavior, or acceptance criteria.

1. **Check the return.** Apply the contract's input checks. Retain the feedback identity, originating function, affected baseline and rule IDs, constraint, observations, estimates and uncertainty, impact, considered alternatives and tradeoffs, and requested decision or missing fact. If no alternative is known, say so. Ask for missing evidence through the handoff route; do not silently apply feedback about an older baseline to the current version.
2. **Reconsider the product decision.** Investigate available facts and use the clarification loop for product decisions. Compare ways to preserve the user goal within the discovered constraints. Keep proven limits separate from estimates and unknowns. Without an agreed budget or limit, report a tradeoff or clarification need rather than inventing a threshold. Send purely technical, task, code, or test-case corrections back to their owning function through Delivery Lead in team work.
3. **Deliver a response.** Produce a revised product proposal with alternatives, tradeoffs, changed rules and examples; or a reasoned response requesting more evidence or explaining why the current product decision still applies. Identify the affected product scope and known downstream references for the coordinator's impact assessment. Use the contract's version and approval rules for changed scope, behavior, or acceptance criteria. An unchanged product decision does not by itself resolve the originating constraint.
4. **Keep the loop explicit.** In team work, Delivery Lead tracks the affected downstream outputs, approvals, resumption, and closure; supply the product evidence it needs. Revised product approval permits renewed technical assessment, not an assumption of feasibility. Closure needs the relevant function's supported resolution or an explicit human decision to defer or stop. Record deferred or stopped scope as undelivered. If the same baseline returns without new evidence or a viable alternative, provide the attempts, options, consequences, and missing facts for a human decision rather than repeating the same proposal. In standalone work, deliver that request to the user.

Preserve prior decisions and unaffected scope. Dependent work stays blocked while required evidence or approval is missing; independent work needs a supported basis for remaining valid. Return a feedback or blocker summary even when no revised product document is ready.

## Compare approaches

Compare at least two meaningful ways to achieve the same user goal. Start with differences in the user journey, trigger, or how users receive value. For example, a trend-monitoring tool might offer active search, a periodic digest, or alerts triggered by events. Choose alternatives relevant to the actual goal.

Consider doing nothing, manual workflows, and existing solutions when they could meet the goal. Record the comparison in the contract's [assigned location](document-contract.md#content-placement). State uncertainty in estimates. Recommend an approach. Obtain the user's decision unless the direction was already supplied or authorized.

After choosing a direction, define the smallest useful scope. Explain the added cost and complexity of future changes. Compare technical alternatives only when they materially affect product behavior, constraints, or feasibility. Include only the detail needed for that decision.

## Impact Mapping

For every Feature, trace **goal → actor → behavioral impact → deliverable**. Behavioral impact means the intended change in what an actor does. Use the map to identify assumptions about how the Feature helps the goal. Challenge unsupported links and mark causal hypotheses. Justify dependencies and consider alternatives that do not require software. Example hypothesis:

`SC1: shorten approval turnaround → approver → reviews pending requests daily → F1: pending-request digest`

A dashboard is a deliverable. Noticing stalled requests is a behavioral impact. A change in team practice may achieve the same result. Record the links and hypotheses in the contract's assigned locations. Include actors who help or hinder the outcome, even if they have no User Stories.

Source: [Drawing impact maps](https://www.impactmapping.org/drawing.html).

## Specification by Example

Use concrete cases to discover and refine rules with the user. Keep cases that distinguish one behavior from another.

For a confirmed limit of 10 entries, examine these cases:

- Add an entry when the count is 9.
- Add an entry when the count is 10.

Record the final count in each case. If the action is rejected, record what stays unchanged. Do not choose the limit yourself.

For “prevent duplicates,” compare `https://example.com/a` with `https://example.com/a/`. Ask what makes two entries equal before defining how to normalize them.

Repetitive examples may reveal a missing concept or separate rules. Record the rules and examples under the contract's [Feature rules](document-contract.md#feature-rules). The number or format of examples does not prove agreement.

Sources: [Specifying with examples](https://gojko.net/2008/11/04/specifying-with-examples/), [Focus on key examples](https://gojko.net/2014/05/05/focus-on-key-examples/).
