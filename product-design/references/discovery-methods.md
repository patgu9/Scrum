# Discovery methods

Choose Startup or Builder from the user's goal. Ask the user to choose only if the distinction affects the work and remains unclear. Use the mode and unresolved questions to guide discovery. The questions below are prompts, not a required questionnaire. Follow the [Technical Writing Skill](../../technical-writing/SKILL.md) for wording and presentation.

## Conversation rules

Use the [clarification protocol](#clarify-decisions-and-terms) to select questions, pace each round, and retain unanswered questions.

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

## Deep discovery interviews

Use this path when the user's situation, desired outcome, or reason for an idea remains unclear. Explore the problem or aspiration before asking the user to choose a solution. Reuse specific answers already supplied.

### Start with a specific story

Use [story-based interviews](https://www.producttalk.org/customer-interviews/) to discover needs from a concrete experience. Ask: “What happened recently that led you to this idea?” Follow the event from its trigger to its result.

| Explore | Example prompt |
|-----|-----|
| Situation and goal | What were you trying to accomplish then? |
| Actions | Walk me through what you did next. |
| Difficulty | What, if anything, got in the way? |
| Workaround | How did you handle it? |
| Consequence | What effect did that have on the result or the people involved? |
| Contrast | Tell me about a similar time when it went well. |

After each answer, follow the most useful gap, contradiction, workaround, or unexpected detail. Return broad claims such as “often” or “frustrating” to a specific event. For a Feature request, ask about the situation that prompted it.

If no relevant event exists, explore the inspiration, a related experience, and the result the user wants to try. Learning and creative work need no invented pain point. Mark future scenarios as hypothetical and identify a trial that could supply evidence.

### Understand the progress sought

Use [Jobs to Be Done](https://www.christenseninstitute.org/theory/jobs-to-be-done/) to connect circumstances to desired progress. Ask what completing the task would enable. Explore functional, emotional, or social needs when they affect the outcome. Do not require all three.

If the user sought or adopted a new approach, reconstruct that change. Explore what made the old approach inadequate, what attracted the user, what caused concern, and what favored staying. Keep the user's account separate from your explanation of it.

### Keep questions neutral

Apply [The Mom Test](https://www.momtestbook.com/) throughout exploration to reduce biased feedback. Ask about specific actions, attempts, costs, and commitments before presenting your idea. For example, ask “How did you find the material last time?” before discussing automatic tags.

Explore aspirations, but distinguish them from past behavior. Praise, stated interest, and predicted use do not establish demand. Do not embed your preferred answer in an exploration question.

### Observe when words are insufficient

Use [contextual inquiry](https://www.nngroup.com/articles/contextual-inquiry/) when the user cannot explain a workflow or accounts conflict. Where access permits, ask the user to demonstrate a real task with current tools or materials. Follow observed actions with neutral questions. If direct observation is unavailable, reconstruct the task and retain that evidence limit.

### Form and challenge a need hypothesis

Summarize the situation, current approach, obstacle or aspiration, consequence, and desired outcome. Cite the supporting account or observation. Ask the user to correct your interpretation. Seek a contrasting case where relevant and revise the hypothesis if it does not explain that case.

Before comparing approaches, clarify the situation and desired outcome. Record remaining hypotheses and validation actions. Pause comparisons that depend on missing answers; continue independent work through the clarification protocol. For a new experience, use the related context and proposed trial. Do not impose an interview quota.

User confirmation establishes shared understanding, not validated demand. For products serving others, distinguish the idea owner's expectations from target-user evidence. Record findings and hypotheses in the contract's [assigned locations](document-contract.md#content-placement).

## Clarify decisions and terms

Use this protocol during discovery, specification, and review. New findings may require revisiting the problem definition. The document contract defines [where to record questions](document-contract.md#content-placement) and [when the document can be approved](document-contract.md#status-and-approval).

Read existing domain guidance, including `CONTEXT.md` or `CONTEXT-MAP.md` when present. Report conflicting meanings instead of replacing established terms. Use code to verify current behavior when available. Record current and desired behavior separately.

Distinguish these question types:

| Type | Purpose and response |
|-----|-----|
| `Exploration question` | Discover experiences, motives, and needs through open, neutral follow-up. |
| `Fact to investigate` | Verify a specific claim with source evidence. Request user-held evidence when needed. |
| `User decision` | Obtain a choice or authorization after explaining the tradeoffs. |

Use these question states. Question states describe individual questions; document Status describes the Design Doc as a whole.

| State | Meaning |
|-----|-----|
| `OPEN` | The question is unresolved. |
| `INVESTIGATING` | You are gathering facts. |
| `WAITING` | You asked the question and are waiting for the user's answer. |
| `RESOLVED` | The user's account answers an exploration question, evidence supports an investigated fact, or the user authorized a decision. |
| `UNKNOWN` | Evidence is unavailable, or the user answered “I don't know” or “skip.” |
| `EXCLUDED` | The user agreed to remove the affected scope. |

Follow this loop as evidence and decisions change:

1. **Record questions and dependencies.** Give each material unresolved question a stable `Q<n>` ID. Never renumber or reuse a question ID. Use a question type from the table above. Keep follow-up on the same inquiry under its Q ID; create a new ID for a distinct unresolved question.

   Use the contract's [question fields](document-contract.md#content-placement). List dependencies on other questions or unfinished investigations. State when a dependency applies only to a particular approach. Keep resolved and excluded records so readers can trace later changes.

2. **Set the question state.** A recommendation, silence, or an unanswered option does not resolve a question. When you reopen a question, set its state to `OPEN`. Keep the previous answer and the reason for reopening.

   If evidence is unavailable or the user answers “I don't know” or “skip,” use `UNKNOWN`. Record the needed evidence and propose a validation step or ask whether to exclude the affected scope. Skipping does not exclude scope or accept a recommendation. Keep dependent content pending and link its Q ID.

3. **Investigate facts before asking for a decision.** Inspect available project files and code. Use available tools to gather facts. Record unfinished investigations as unresolved prerequisites. Pause work that depends on those investigations. Continue independent decisions and drafting.

   Use interviews for experiences and needs that project files cannot establish. Follow [deep discovery interviews](#deep-discovery-interviews) when the problem remains unclear.

4. **Choose the next questions.** Update conditional dependencies after new evidence, an answer, or a scope change. Consider unresolved exploration, evidence needs, and decisions relevant to the current inquiry or scope. Ask a question only when its prerequisites are resolved and its state is not `WAITING`. Prioritize what would clarify the need or allow dependent work.

   Ask one question by default. Ask at most three mutually independent questions in one round. Keep the other questions for later. Do not start another round while answers are pending. Continue independent investigation and drafting.

   If a new direction or scope change makes a waiting question irrelevant, record the reason. Do not mark that question as answered.

5. **Ask according to the question type.** For exploration, ask an open question tied to the user's account. For a fact investigation, request the missing evidence without inventing options. Briefly explain the purpose when needed.

   For a user decision, state what needs a choice, why it matters now, and which content it affects. Present the main options and tradeoffs. Give your recommendation and reason. Exploration and fact investigations need no option comparison or recommendation.

   For decisions, reuse a prior explicit choice or authorization within its scope. Otherwise wait for the user's choice. Never record your recommendation as a confirmed rule.

6. **Record partial answers and uncertainty.** Set asked questions to `WAITING`. Resolve only answered questions with a sufficient basis. If an answer leaves material gaps, retain it and set the question to `OPEN` for follow-up. Keep unanswered questions in `WAITING`. Apply step 2 to unknown answers or unavailable evidence.

7. **Apply answers and changes.** Save each answer with its basis and source. Update dependencies. Check affected terms, Success Criteria, Features, rules, and examples.

   If an earlier decision changes, mark content based on that decision for review. Reopen only affected dependent decisions. Keep a dependent decision resolved only after checking that its basis still holds. Preserve unaffected decisions. Add new questions to this loop.

8. **Check blockers and finish discovery.** An empty question queue does not prove that clarification is complete. Check unfinished investigations, waiting answers, unknowns, and cycles in question dependencies. Report the blocker and next action. Break a cycle by clarifying the decision that governs the dependent questions or investigating the unknown fact. Do not resolve a question without a basis.

   When discovery is complete, apply the contract's [status and approval rules](document-contract.md#status-and-approval). Set `APPROVED` only from explicit human approval of the current version.

Use concrete counterexamples to clarify ambiguous claims and terms. For example, “sharing” may mean a public link or a workspace invitation. Decide the audience and access rules before invitation expiry. Independent questions can proceed.

Once the sharing need is understood, a hypothetical research-sharing design might have these dependencies:

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

1. **Check the return.** Apply the contract's [input checks](document-contract.md#inputs-and-invocation-context). Retain the feedback identity, originating function, affected baseline and rules, constraint, evidence, estimates and uncertainty, impact, alternatives, and requested decision or missing fact. State when alternatives are unknown. Request missing evidence through the established handoff route.
2. **Reconsider the product decision.** Investigate facts through the clarification loop. Apply [approach comparison](#compare-approaches) to reassess ways to preserve the user goal within the discovered constraints. Keep proven limits separate from estimates and unknowns; do not invent a budget or threshold. Return non-product corrections to their owner through the caller's route.
3. **Deliver a response.** Provide a revised proposal, a request for evidence, or reasons why the current decision still applies. Include alternatives, tradeoffs, changed rules and examples where applicable, and affected downstream references. Apply the contract's [version rules](document-contract.md#versions-and-approval-evidence) and [handoff summary](document-contract.md#handoff-summary), even when no revision is ready.
4. **Keep the loop explicit.** Use the contract's [established route](document-contract.md#inputs-and-invocation-context). For team feedback, supply product evidence under [feedback and resumption](../../project-manager/references/feedback-and-resumption.md), which owns tracking, reassessment, resumption, and closure. For standalone feedback, request a decision when the same baseline recurs without new evidence or a viable alternative. State attempts, options, consequences, and missing facts. Keep the issue open until supported resolution or an explicit decision to defer or stop; report deferred or stopped scope as undelivered.

An unchanged decision or revised product approval does not establish feasibility or resolve the originating constraint. Preserve prior decisions and unaffected scope through the clarification protocol and input checks.

## Compare approaches

For an initial direction, compare at least two meaningful ways to achieve the same user goal. Start with differences in the user journey, trigger, or how users receive value. For example, a trend-monitoring tool might offer active search, a periodic digest, or alerts triggered by events. Choose alternatives relevant to the actual goal.

For a revision, read the existing comparison and decision basis. Reuse them when they still apply, and retain the comparison in Approaches Considered. Reopen only the affected comparison when changes to goals, scope, constraints, or evidence could change the choice. A wording correction or detail within the agreed direction does not require new alternatives. If no usable comparison exists, complete the initial comparison; do not reconstruct it from the chosen direction alone.

Consider doing nothing, manual workflows, and existing solutions when they could meet the goal. Apply [Occam's Razor](#occams-razor) to the alternatives before recommending an approach. Record the comparison in the contract's [assigned location](document-contract.md#content-placement). State uncertainty in estimates. Resolve the direction through the clarification protocol, reusing prior choices within their scope.

After choosing a direction, use the same principle to refine the smallest useful scope. Explain the cost and complexity of future changes. Compare technical alternatives only when they materially affect product behavior, constraints, or feasibility. Include only the detail needed for that decision.

## Occam's Razor

Apply the [principle of parsimony](https://plato.stanford.edu/entries/simplicity/) during approach comparison and scope refinement. First assess coverage of the agreed user outcomes and constraints. When coverage, evidence, and risk are comparable, prefer fewer assumptions and less product complexity. Otherwise explain the tradeoff.

- For each added Feature, concept, workflow step, exception, or dependency, ask: “Which user outcome or constraint does this support?” Propose removing or deferring additions without a supported purpose.
- Preserve necessary behavior, failure handling, and correction paths. Fewer Features or steps do not help if the user outcome suffers.
- Do not add scope solely for speculative future needs. State the benefit, cost, and reason when recommending a more complex approach.
- Keep untested causal links as hypotheses with validation actions. Neither simplicity nor missing evidence establishes their truth or lack of value. Investigate conflicting evidence.

Record rationale and agreed exclusions in the contract's [assigned locations](document-contract.md#content-placement). Resolve scope changes through the clarification protocol.

## Impact Mapping

Start with **goal → actor → behavioral impact**, then [compare possible deliverables](#compare-approaches). Behavioral impact means the intended change in what an actor does. For each proposed Feature, complete **goal → actor → behavioral impact → deliverable**. Mark unsupported causal links as hypotheses. Justify dependencies. Example hypothesis:

`SC1: shorten approval turnaround → approver → reviews pending requests daily → F1: pending-request digest`

A dashboard is a deliverable. Noticing stalled requests is a behavioral impact. A change in team practice may achieve the same result. Record the links and hypotheses in the contract's assigned locations. Include actors who help or hinder the outcome, even if they have no User Stories.

## Specification by Example

Use concrete cases to discover and refine rules with the user. Keep cases that distinguish one behavior from another.

For a confirmed limit of 10 entries, examine these cases:

- Add an entry when the count is 9.
- Add an entry when the count is 10.

Record the final count in each case. If the action is rejected, record what stays unchanged. Do not choose the limit yourself.

For “prevent duplicates,” compare `https://example.com/a` with `https://example.com/a/`. Ask what makes two entries equal before defining how to normalize them.

Use repeated examples to examine shared rules before adding concepts or exceptions. Apply [Occam's Razor](#occams-razor) while preserving cases that distinguish outcomes. If a case challenges the need or scope, return to the clarification protocol. Record rules and examples under the contract's [Feature rules](document-contract.md#feature-rules). Examples alone do not prove agreement or validate a need hypothesis.
