# Discovery and decision methods

Use the sections needed for the current decision. Methods do not add required stages or documents. The [document contract](document-contract.md) owns output fields, evidence records, and approval.

## Startup

Use Startup for products seeking customers or internal projects needing adoption. Establish the actor, task, desired outcome, current workaround, and consequences. Separate the idea owner's expectations from target-user evidence.

- **No users:** Investigate the need, current alternatives, and access to the intended audience.
- **Users:** Investigate first value, repeated use, and barriers to adoption.
- **Paying customers:** Investigate scope, retention, viability, and changes that could affect future value.
- **Infrastructure:** Start with the workflow and one narrow improvement. Internal adoption or resource commitments can replace payment evidence.

Use [strategy and positioning](#strategy-and-positioning) when the audience or advantage is unclear. Use [adoption and viability](#adoption-and-viability) when usage or payment falls short.

## Builder

Use Builder for personal tools, learning, research, open-source exploration, demos, and creative work. Completion, enjoyment, and learning are valid outcomes.

Establish who would try it, what would be useful or exciting, the closest existing alternative, and the smallest usable result. Explore unexpected uses without adding them to scope by default. Do not require customer interviews, market positioning, revenue, or product-market fit surveys for personal work.

## Deep discovery interviews

Use this when the situation, desired outcome, or reason for an idea is unclear. Reuse supplied answers before asking more questions.

Start with a recent event: “What happened that led you to this idea?” Follow its trigger, goal, actions, difficulty, workaround, and result. Ask what happened next. Return broad claims such as “often” to a concrete case. Explore a contrasting case when useful.

Ask what completing the task would enable. Explore functional, emotional, or social needs only where relevant. When switching approaches matters, investigate what pushed the change, what attracted the user, what caused concern, and what favored staying. More functionality can add anxiety; a simpler transition may solve the problem.

Keep questions neutral. Ask about past actions, costs, and commitments before presenting an idea. Praise, predicted use, and stated interest do not establish demand. Where access permits, observe a real task without coaching when accounts conflict or the workflow is hard to describe. Otherwise reconstruct it and retain that limit. Avoid unnecessary personal information.

If no relevant event exists, explore the inspiration, related experience, and intended trial. Mark future scenarios as hypothetical; do not invent a pain point for creative work.

Summarize the circumstances, current approach, obstacle or aspiration, consequence, and desired outcome. Separate the user's account from your interpretation and ask for corrections. Clarify these before comparing solutions that depend on them. Record remaining hypotheses and validation actions. User confirmation establishes shared understanding, not demand. Do not impose an interview quota.

## Clarify decisions and terms

Use this protocol throughout discovery, specification, and review. Read existing domain guidance such as `CONTEXT.md` or `CONTEXT-MAP.md`. Verify current behavior from available files or code and distinguish it from desired behavior. Report conflicting meanings.

| Question type | Purpose |
| --- | --- |
| `Exploration question` | Understand experiences, motives, and needs through neutral follow-up |
| `Fact to investigate` | Verify a claim with available evidence or request missing evidence |
| `User decision` | Obtain a choice or authorization after explaining tradeoffs |

| State | Meaning |
| --- | --- |
| `OPEN` | Unresolved |
| `INVESTIGATING` | Gathering facts |
| `WAITING` | Asked and awaiting the user's answer |
| `RESOLVED` | Answered by the user's account, supported evidence, or an authorized decision, as applicable |
| `UNKNOWN` | Evidence unavailable, or the user answered “I don't know” or “skip” |
| `EXCLUDED` | The user agreed to remove the affected scope |

1. **Record:** Give each material unresolved inquiry a stable `Q<n>` ID using the contract's [question fields](document-contract.md#question-records). Keep follow-up on that inquiry under its ID. Create a new ID for a distinct question. Never renumber or reuse IDs; retain resolved and excluded records.
2. **Investigate:** Gather available facts before requesting decisions. Track unfinished investigations as prerequisites. Pause dependent work and continue independent work. Use interviews for experiences that files cannot establish.
3. **Select:** Update conditional dependencies after new evidence or scope changes. Ask only questions with resolved prerequisites that are not already `WAITING`. Ask one by default, at most three mutually independent questions per round. Wait for answers before another round. If a waiting question becomes irrelevant, record why without marking it answered.
4. **Ask:** Use open, neutral prompts for exploration and request specific evidence for facts. For decisions, explain the choice, impact, options, tradeoffs, recommendation, and reason. Reuse explicit authorization within its scope; otherwise wait for the user's choice. Mark asked questions `WAITING`.
5. **Resolve:** Record the answer, basis, and evidence. Resolve only sufficiently answered questions. Retain partial answers and reopen their remaining gaps; leave unanswered questions `WAITING`. Set reopened questions to `OPEN`. Recommendations, silence, and unanswered options are not decisions.
6. **Handle unknowns:** Use `UNKNOWN` when evidence is unavailable or the user skips. Record the needed evidence and propose validation or scope exclusion. Keep dependent content pending. Skipping does not exclude scope or accept a recommendation; `EXCLUDED` requires the user's agreement.
7. **Apply:** Update affected terms, scope, Success Criteria, Features, rules, and examples. Keep pending effects visible with Q links. When a decision changes, preserve its prior answer and reason, reopen affected decisions, and retain others only after checking their basis.
8. **Finish:** Check waiting answers, unknowns, unfinished investigations, and dependency cycles. An empty queue does not establish readiness. Break cycles through the governing decision or missing fact. Apply the contract's [status rules](document-contract.md#status-and-approval).

Use counterexamples to clarify ambiguous terms. For “sharing,” establish the audience before deciding link expiry. Investigating existing membership can proceed independently. Editing separate domain documents or architecture decision records requires a separate request.

## Opportunity selection and impact mapping

Compare unmet needs before selecting solutions. Consider the affected segment, consequence, frequency when known, workaround, and relation to the goal. Retain contrary cases and sampling limits. “I cannot tell which request needs attention” is a need; “add a dashboard” is a solution.

For each retained Feature, connect **goal → actor → behavioral impact → deliverable**. Use the selected need to explain why that behavior should change. Compare alternative deliverables and identify their assumptions. Mark unsupported causal links as hypotheses and justify dependencies. Include actors who help or hinder the outcome, even without User Stories.

Example hypothesis: `SC1: shorten approval turnaround → approver → reviews pending requests daily → F1: pending-request digest`. A change in team practice could be another solution. One compact map is enough; do not create separate diagrams for equivalent relationships.

## Strategy and positioning

Use this for a new product, segment, or material change in direction. Reuse an established strategy when it still applies.

Explain **who benefits, which need matters, what the alternatives are, and why this approach should produce the outcome**. Include manual work and no purchase among relevant alternatives. Translate distinctive capabilities into value, then identify who values those differences most. Choose a market category only when it helps that audience understand the value.

State what will not receive resources and why. For commercial products, consider customer benefit, durable advantage, and economic viability. Make conflicts between growth, experience quality, and monetization explicit. A feature list or target alone does not explain strategy. Keep company-wide strategy and roadmap work outside the change unless requested.

## Compare approaches

For an initial direction, compare at least two meaningful ways to achieve the same goal. Start with differences in the journey, trigger, or delivery of value. Include doing nothing, manual work, and existing solutions where relevant. Compare technical options only when they materially affect product behavior, constraints, or feasibility.

For revisions, reuse the existing comparison and basis while they remain valid. Reopen only choices affected by changes to goals, scope, constraints, or evidence. A wording correction or detail within the agreed direction needs no new alternatives. If no usable comparison exists, complete one; do not reconstruct it from the selected direction alone.

Apply [Occam's Razor](#occams-razor), state estimate uncertainty, and resolve the choice through the clarification protocol. Then refine the smallest useful scope and explain relevant future change costs.

### Prioritization

When opportunities or Features compete for resources, compare outcome contribution, reach, evidence, effort, dependencies, and displaced work. Keep impact separate from confidence. Executive conviction and competitor behavior are not strong customer evidence.

Prefer qualitative comparison unless scores improve the decision. For scores, use compatible units and time windows, show the basis and uncertainty, and respect required constraints. Investigate shortlisted choices more deeply when evidence could change the ranking. Check whether plausible input changes reverse it. Request effort or feasibility evidence from its owner; do not invent precision or write an engineering specification to support a score. Delivery task prioritization remains downstream work.

## Occam's Razor

First assess coverage of agreed outcomes and constraints. When coverage, evidence, and risk are comparable, prefer fewer assumptions, concepts, steps, exceptions, and dependencies. For each addition, identify the outcome or constraint it supports. Propose removing or deferring unsupported additions through the clarification protocol.

Preserve necessary behavior, failure handling, and correction paths. Do not add scope solely for speculative future needs. Explain any retained complexity. Missing evidence does not prove a need has no value; investigate conflicting evidence and retain untested causal links as hypotheses.

## Risk and validation

Distinguish value, usability, feasibility, and organizational viability. Choose the assumption whose failure would most change the decision, considering uncertainty, consequence, and cost to learn. Match the method to the uncertainty:

| Uncertainty | Candidate method | Evidence limit |
| --- | --- | --- |
| Need or switching motive | Recent-event interview or workflow observation | Does not establish prevalence, purchase, or causal impact |
| Comprehension or usability | Observed task with a prototype | Does not establish sustained adoption or production feasibility |
| Value or buyer commitment | Manual trial, pilot, or purchase discussion | Does not establish repeatable market demand |
| Behavioral impact at sufficient scale | Controlled experiment | Applies to the measured population and window |
| Sparse usage or new experience | Trial with explicit success and failure cases | Does not establish a precise causal effect |
| Feasibility or operating constraint | Evidence request to the responsible specialist | Does not establish product approval or implementation authority |

Use the [assumption validation fields](document-contract.md#assumption-validation). Choose an observation that can challenge the assumption and distinguish relevant alternative explanations. Define what supports continuation, revision, or stopping. Keep inconclusive results unresolved.

For a proposed A/B test, establish the decision, eligible population, comparison, outcome, guardrails, and time to useful evidence. Request statistical design and instrumentation checks from the responsible specialist. Do not claim a win from repeated significance checks or unresolved allocation problems. If traffic, time, or a suitable comparison is missing, propose another method and state its limits.

Research effort should match risk. Planning a trial does not authorize building, launching, charging, or contacting participants.

## Outcomes and metrics

Select measures that represent delivered value. Distinguish user outcomes, business results, leading indicators, and guardrails. A guardrail is an outcome that must not worsen beyond an agreed limit. Add one when improving the main measure could materially harm another outcome or constraint. A single North Star metric is optional. Use the contract's [Success Criteria fields](document-contract.md#success-criteria).

For activation, identify first meaningful value rather than setup alone. Separate individual and team adoption. A milestone correlated with retention does not establish that increasing it causes retention.

For retention, define the qualifying action, cohort, measurement unit, return interval, and observation window. Separate users from paying accounts and distinguish exact-period from return-on-or-after measures. Check cohort maturity. Match the cadence to the real task; a monthly need does not imply daily use.

Check whether short-term improvement hides later harm or differences between segments. Choose metrics from the value and business mechanism, not another company's benchmarks. Use an observable trial for Builder goals.

## Adoption and viability

When adoption, growth, retention, or payment matters, describe how users discover the product, reach first value, and return when the need recurs. Identify the buyer, purchase decision, and support or operating burden where relevant. Distinguish sales-assisted and self-service paths. Locate the constraint before adding acquisition or engagement Features.

For products with meaningful usage, a product-market fit (PMF) survey can identify users who depend on the main benefit. Compare feedback by benefit and context. Investigate barriers for users who value that benefit but struggle to obtain it. Do not discard safety, accessibility, or contractual needs from other users.

Treat surveys as leading signals, with respondent eligibility, sample size, and selection bias. Compare them with repeat use, retention, and payment. Do not infer PMF from people who have never used the product or from a universal survey cutoff.

For early B2B work, distinguish one successful account, willingness to pay, actual payment, repeat use, and success across independent accounts. Keep pricing and packaging as hypotheses where they affect adoption. A paid pilot does not prove a repeatable market. Campaign execution and sales operations remain outside this Skill.

## Specification by Example

Use concrete cases to discover rules. For an agreed limit of 10 entries, compare adding an entry when the count is 9 and when it is 10. Record the resulting count and what stays unchanged on rejection. Do not choose the limit yourself.

For “prevent duplicates,” compare `https://example.com/a` with `https://example.com/a/`. Establish equality before choosing normalization. Keep cases that distinguish behavior; use repeated examples to find shared rules before adding exceptions. Return need or scope conflicts to clarification. The contract owns [Feature rules and example format](document-contract.md#feature-rules).

### AI product behavior

When model variability affects outcomes, define representative tasks, input variation, unacceptable results, and observable recovery or user control. Request evaluation evidence before making quality promises; a successful demo is insufficient. Reassess when the model, context, or task population changes. Leave evaluation infrastructure and model implementation to their owners.

## Revisit a product baseline

Use this when downstream feedback or observed results challenge value, scope, behavior, or acceptance. Product intuition may not transfer when the audience changes.

1. **Check inputs:** Apply the contract's [input rules](document-contract.md#inputs-and-invocation-context). Retain feedback identity, origin, baseline and affected IDs, evidence, constraint, impact, estimates and uncertainty, alternatives, and requested decision. State missing facts and unknown alternatives.
2. **Reassess:** Compare observed results with intended outcomes, guardrails, and disconfirming results. Examine segment differences and alternative explanations. Use clarification and approach comparison for affected choices; preserve unaffected decisions after checking their basis. Return non-product corrections to their owner.
3. **Respond:** Provide a revised proposal, an evidence request, or reasons the current choice still applies. Include tradeoffs, affected rules, examples, and downstream references. Apply the contract's version and handoff rules, even when no revision is ready.
4. **Route:** Use the caller's established route. In team work, [Project Manager](../../project-manager/references/feedback-and-resumption.md) owns tracking, reassessment, resumption, and closure. In standalone work, request a decision if the same baseline recurs without new evidence or a viable alternative. State attempts, options, consequences, and missing facts. Keep the issue open until supported resolution or explicit deferral or stop; deferred or stopped scope remains undelivered.

An unchanged decision or revised product approval does not establish feasibility or resolve the originating constraint. Ongoing learning does not authorize experiments, scheduled research, or process changes.
