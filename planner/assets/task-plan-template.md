# Task Plan Index: $Change title$

- Status: DRAFT
- Version: v1
- Date: $YYYY-MM-DD$
- Responsible lead: $Engineering lead identity$
- Change directory: $Existing source change directory$
- Product baseline: $Document link, exact version/snapshot, and owner approval evidence$
- Overall technical baseline: $Document link, exact version, owner approval evidence, and scope ready for breakdown$
- Repository context: $Repository, inspected revision, relevant local changes, Git policy, integration target, and evidence limits$
- Developer availability: $Known identities, capabilities, capacity, and source; or missing facts and supplier$
- Review policy: $Applicable reviewability policy and reference; record unresolved conflicts. No default numerical gate.$

<!-- Follow this Skill's artifact rules in ../references/plan-contract.md. Save as task-plan.md in the source change directory. Create each standalone task from task-template.md. This file contains links and summaries, never full task definitions. Remove prompts/comments from completed output. A blocked plan can record missing inputs without inventing assignments. -->

## Scope and Coverage

- **Outcome and included scope:** $Approved outcome and included Features/rules/contracts.$
- **Required path:** $User and complete path to the outcome, with source references; use an existing Story Map when useful. For technical work, name the consumer and engineering outcome.$
- **Exclusions:** $Out-of-scope work and accepted exclusions with source references.$

| Product Rule / Technical Contract | Task IDs | Observable Acceptance and Verification Responsibility | Exclusion or Gap |
| --- | --- | --- | --- |
| $Document-qualified rule/contract and example references$ | $Task IDs$ | $Expected behavior, task self-tests, and shared integration check/recipient$ | $None, accepted exclusion source, or unresolved gap$ |

## Decomposition Basis

- **Behavior boundaries:** $Rules and concrete examples that distinguish candidate slices; link unresolved questions in the issue table below. Reuse source content.$

| Candidate Boundaries / Pattern | Benefits and Tradeoffs | Disposition and Reason |
| --- | --- | --- |
| $Materially different split, or the single viable choice with its basis$ | $Complete outcomes, early feedback, risks, dependencies, and review context$ | $Selected / Rejected / Needs clarification, with evidence or uncertainty$ |

- **Selected approach:** $Why these boundaries fit the approved scope and current code. Keep a small change brief; do not manufacture alternatives. Task files own final task definitions.$

## Task Index and Dependency Order

| Task Entry | Task Version Summarized | Goal | Assignee Summary | Dependency Summary | Readiness Summary |
| --- | --- | --- | --- | --- | --- |
| $T1 with a relative link to tasks/t1/task.md$ | $v1$ | $Outcome$ | $Developer or Unassigned$ | $Dependency task links and gated stage$ | $Ready/blocked/retired with reason; verify the task file before claim$ |

The linked task files own their definitions, assignment, readiness, and observed execution records. These rows are summaries of the stated task versions. Claim confirmation comes from the applicable coordination workflow.

- **Sequence and parallel work:** $Dependency order, independence evidence, overlapping files/interfaces, and capacity constraints.$
- **Integration obligations:** $Shared checks, prerequisites, accountable recipients, and overall-design references.$

## Cross-Task Issues, Revisions, and Feedback

| Issue | Affected Tasks and Baselines | Evidence, Uncertainty, and Impact | Required Resolution / Alternatives | Owner and Receiving Function | State |
| --- | --- | --- | --- | --- | --- |
| $Stable ID or None$ | $Document-qualified refs$ | $Observed constraint versus estimate; stage blocked and dependent outputs$ | $Missing fact/decision, alternatives/tradeoffs, and resumption evidence$ | $Accountable recipient and next function$ | $Open/resolved/deferred with supporting evidence$ |

| Plan Revision | Change and Basis | Lineage / Coverage Impact | Reassessment and Readiness |
| --- | --- | --- | --- |
| v1 | $Initial plan or revision basis$ | $Changed task paths/versions; replacement mapping and retained original scope$ | $Affected task designs, branches/PRs, tests/reviews and valid independent work$ |

## Review and Handoff

- **Review scope:** $Reviewed plan and task versions, reviewer, and review type: self-review or independent review.$
- **Checks performed:** $Actual user-path and rule/example coverage, split rationale, INVEST/SMART and Small CLs checks, combined-scope completeness, dependencies, readiness, and task-entry walkthrough. Include entry links, backlinks, task versions, and index consistency.$
- **Review findings:** $Corrections, unresolved findings and their dispositions, and unreviewed areas; or no unresolved findings within the reviewed scope.$
- **Ready tasks and assignments:** $Exact task paths/versions and accountable developers, or None. Summary only; confirm from each task file.$
- **Blocked, unassigned, or retired tasks:** $Exact IDs, reasons, suppliers, and resumption conditions.$
- **Common handoff:** $Change scope, exact input versions, plan path/version, each receiving Agent's task path/version, conclusion and evidence, unresolved issues, next functions and responsible recipients.$
- **Delivery blockers:** $Missing follow-on capability or routing, with supplier; do not infer that tasks were published, claimed, or executed.$
- **Verification limits:** $What was checked versus planned/unrun. Planning does not establish implementation, independent code review, merge, QA, or ship acceptance.$
