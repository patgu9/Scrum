## Design Doc : $TITLE$

- Status: DRAFT
- Mode: $Startup or Builder$
- Date: $YYYY-MM-DD$
- Stage: Think

<!-- Preserve headings, labels, table headers, and stable IDs. Replace placeholders and remove comments. Omit only optional fields. Follow the document contract's language, review, and approval rules: use plain words and short sentences; lead with the point; remove repetition without dropping conditions or exceptions. -->

### Glossary

| Term | Definition |
|-----|-----|
| $Ambiguous domain term$ | $Meaning and boundaries in this design$ |

### Background

#### Problem Statement

$Who faces what problem, in which situation? Describe the current workaround and impact.$

- **Evidence:** $Observed behavior, interviews, or data with sources; state evidence gaps.$
- **Constraints (optional):** $Time, resource, platform, or business limits affecting the choice.$

#### What Makes This Cool

$Value compared with the current approach: concrete benefits for Startup, or an experience worth trying for Builder.$

### Solution Design

#### Approaches Considered

| Approach | Core Idea and Benefits | Main Costs and Risks |
|-----|-----|-----|
| A: Minimal implementation | $Smallest useful scope, fastest delivery, and reuse$ | $Effort: S/M/L/XL; risk: Low/Medium/High; drawbacks$ |
| B: Ideal architecture | $Long-term boundaries, expected evolution, and reuse$ | $Effort: S/M/L/XL; risk: Low/Medium/High; added complexity and drawbacks$ |

<!-- Compare meaningful alternatives. Explain estimate basis and uncertainty; include concise rejection reasons. Add a distinct third option only when useful. -->

#### Recommended Approach

**Recommendation:** $Selected approach and rationale tied to the goal; mark an unresolved choice as pending.$

**How It Works:** $Explain who acts, what they do, and how it serves the goal; link SC and Feature IDs. Number the workflow steps. State the trigger, handoffs, result, distribution, and shared dependencies where relevant. Use short sentences.$

**Scope:** $Initial audience, smallest useful outcome, included Feature IDs, exclusions or deferrals, and reasons.$

**Premises and Open Questions:**

| Type | Statement and Impact | Evidence / Validation Status | Follow-up |
|-----|-----|-----|-----|
| $Accepted premise / Assumption to validate / Open decision$ | $Statement, affected IDs, and impact. Blocks approval: Yes / No, with reason$ | $Evidence or rationale; distinguish agreement from verified facts$ | $Validation or resolution action, owner when needed, or none if settled$ |

<!-- Retain unresolved review findings here. Questions preventing definition of core users, scope, or behavior block approval unless the affected scope is excluded by agreement. -->

**Next Action:** $One concrete action and its observable result, in one short sentence. Validate demand or a critical assumption for Startup; try a usable outcome for Builder. Recommend without implementing.$

#### Success Criteria

| ID | Desired Outcome and Pass Condition | Measurement Context and Method |
|-----|-----|-----|
| SC1 | $Outcome and pass condition; quantitative goals need metric definition, baseline, target, and units. Link TBDs to open questions$ | $Observed population, time window, and verification method; explain how to establish missing baselines$ |

<!-- Builder may use an observable task or demonstration instead of numerical targets. -->

### Requirements

<!-- Repeat Features with stable IDs. Every defined rule needs a concrete example; cover relevant boundaries and exceptions without exhaustive enumeration. Use tables or narrative Given/When/Then, not both. Link undecided behavior to open questions. -->

#### Feature 1 — $Capability Name$

##### User Story

> In order to $achieve a specific value or goal$,
> as a $specific role$,
> I want to $perform a specific action$.

- **Related Success Criteria:** $Defined SC IDs.$
- **Boundaries and Dependencies (optional):** $Feature-specific limits or prerequisites.$

##### Rules

- **F1-AC1:** $State the condition and required behavior directly. Use separate short sentences for exceptions. Specify units and inclusive/exclusive boundaries where relevant.$

##### Key Examples

| Example | Related Rule | Given: Context / Input | When: Action / Event | Then: Expected Outcome |
|-----|-----|-----|-----|-----|
| F1-E1: $Scenario name$ | F1-AC1 | $Concrete data and state$ | $Business action$ | $Observable outcome$ |
| F1-E2: $Boundary or exception$ | F1-AC1 | $Facts establishing the boundary$ | $Business action$ | $Outcome and unchanged state where relevant$ |
