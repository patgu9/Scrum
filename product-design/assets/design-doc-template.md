## Design Doc : $TITLE$

- Status: DRAFT
- Version: v1
- Approval: Pending
- Mode: $Startup or Builder$
- Date: $YYYY-MM-DD$
- Stage: Think

<!-- Follow the [document contract](../references/document-contract.md) for structure, content, and approval. Use the [Technical Writing Skill](../../technical-writing/SKILL.md) for wording. Replace placeholders and remove comments. Omit only optional fields. -->

<!-- Save as product-design.md in the task directory defined by the [task artifact layout](../references/artifact-layout.md). -->

<!-- Follow [versions and approval evidence](../references/document-contract.md#versions-and-approval-evidence) when revising. Approval stays Pending until the human approves this version. Deliver the [handoff summary](../references/document-contract.md#handoff-summary) outside this document. -->

### Glossary

<!-- Define unfamiliar terms and abbreviations. Keep one term per concept. State the intended meaning when a term has several common meanings. -->

| Term | Definition |
|-----|-----|
| $Domain term or unfamiliar abbreviation$ | $Meaning and boundaries in this design$ |

### Background

#### Problem Statement

$State the actor, situation, and problem first. Explain the current workaround and impact. Include the context readers need to assess the design.$

- **Evidence:** $Describe observed behavior, interviews, or data. Link sources. State missing evidence.$
- **Constraints (optional):** $State time, resource, platform, or business limits that affect the decision.$

#### What Makes This Cool

$Describe the value compared with the current approach. For Startup: concrete benefits. For Builder: an experience worth trying.$

### Solution Design

#### Approaches Considered

<!-- Compare different ways to achieve the same user goal using the same attributes. -->

| Approach | Core Idea and Benefits | Main Costs and Risks |
|-----|-----|-----|
| A: $Way to achieve the user goal$ | $Describe the user journey, trigger, value, and reuse$ | $Effort: S/M/L/XL. Risk: Low/Medium/High. Drawbacks. If not selected: reason$ |
| B: $Different way to achieve the same goal$ | $Describe the different user journey, trigger, value, and reuse$ | $Effort: S/M/L/XL. Risk: Low/Medium/High. Drawbacks. If not selected: reason$ |

<!-- Follow [approach comparison](../references/discovery-methods.md#compare-approaches). State the basis and uncertainty of estimates. -->

#### Recommended Approach

**Recommendation:** $Name the chosen approach. Explain why it serves the goal. If the decision is unresolved, mark it as pending.$

**How It Works:** $Number the workflow steps. For each step, name the actor, action, and result. Include the trigger, handoffs between actors, how the product reaches users, and shared dependencies where relevant. Link SC and Feature IDs to show how the workflow serves the goal.$

**Scope:** $State the initial audience and smallest useful outcome. List included Feature IDs. State exclusions or deferrals and their reasons. Include the costs of future changes where relevant.$

**Premises and Open Questions:**

| Type | Statement and Impact | Evidence / Validation Status | Follow-up |
|-----|-----|-----|-----|
| $Accepted premise / Assumption to validate$ | $Statement and impact. Affected IDs. Blocks approval: Yes / No, with reason$ | $Evidence or reason. Related SCs. For important assumptions: what to observe, how to collect observations, and which result would not support the assumption$ | $Next action. Owner if needed. If the assumption is unsupported: decisions and IDs to reopen. None only when no follow-up remains$ |
| $Q<n> / Fact to investigate or User decision / protocol state$ | $Question and impact. Affected content: IDs or fields. Depends on: Q IDs or None, with conditions. Blocks approval: Yes / No, with reason$ | $Answer or finding, basis, and source first, or Pending / Unknown. For user decisions: options, tradeoffs, recommendation, and reason. If reopened: prior answer and reason$ | $Next action, required evidence, and content awaiting review. Owner if needed. If EXCLUDED: user's exclusion agreement. None only when no follow-up remains$ |

<!-- Keep each cell readable with short labeled statements. Follow [content placement](../references/document-contract.md#content-placement) for complete record and assumption-validation rules. Follow [status and approval](../references/document-contract.md#status-and-approval) for blockers and approval. -->

**Next Action:** $Give one concrete action and its observable result in one short sentence. For Startup: validate demand or a critical assumption. For Builder: try a usable outcome. Recommend the action without implementing it.$

#### Success Criteria

| ID | Desired Outcome and Pass Condition | Measurement Context and Method |
|-----|-----|-----|
| SC1 | $State the outcome and pass condition. For quantitative goals: metric definition, baseline, target, and units. Link TBDs to open questions$ | $State the observed population, time window, and verification method. Explain how to obtain missing baselines$ |

<!-- Builder may use an observable task or demonstration instead of numerical targets. -->

### Requirements

<!-- Repeat Features with stable IDs. Follow [Feature rules](../references/document-contract.md#feature-rules) for rule coverage, boundaries, exceptions, pending behavior, and example formats. -->

#### Feature 1 — $Capability Name$

##### User Story

> In order to $achieve a specific value or goal$,
> as a $specific role$,
> I want to $perform a specific action$.

- **Related Success Criteria:** $Defined SC IDs.$
- **Boundaries and Dependencies (optional):** $Limits or prerequisites for this Feature.$

##### Rules

- **F1-AC1:** $State the condition, actor, and required behavior. State exceptions separately. Give units where relevant. State whether boundaries are inclusive or exclusive where relevant.$

##### Key Examples

| Example | Related Rule | Given: Context / Input | When: Action / Event | Then: Expected Outcome |
|-----|-----|-----|-----|-----|
| F1-E1: $Scenario name$ | F1-AC1 | $Concrete data and state$ | $Business action$ | $Observable outcome$ |
| F1-E2: $Boundary or exception$ | F1-AC1 | $Facts that establish the boundary$ | $Business action$ | $Observable outcome and what stays unchanged where relevant$ |
