---
name: code-integration
description: Integrate independently accepted task PRs as engineering lead. Use to check current review, required checks, dependencies, and target state; merge eligible changes; verify the resulting candidate; and hand it to QA or return an integration blocker.
---

# Code Integration

Engineering lead owns merge and integration. Produce an identified merged candidate with integration evidence, or a supported blocker. Independent code review, QA acceptance, ship approval, and deployment retain their owners.

## 1. Establish the integration inputs

Read the [integration contract](references/integration-contract.md) for required inputs, readiness, feedback, and output conditions. Inspect task entries, their exact baselines, PRs, review reports, check results, dependencies, and the current target. Reuse confirmed authorization; this stage adds no routine human approval gate.

## 2. Integrate eligible changes

Follow the [integration procedure](references/integration-procedure.md) to reassess stale evidence, order dependent PRs, handle conflicts, and verify the merge result. Use [Git Workflow](../git-workflow/SKILL.md) for Git methods and the applicable platform workflow for provider operations.

Keep each task's PR distinct even when several accepted tasks form one candidate. New code introduced during integration needs self-tests and independent review before acceptance. Missing tools or unresolved gates produce a blocker rather than an invented merge result.

## 3. Deliver the candidate or return feedback

Apply the contract's output conditions. Use [Technical Writing](../technical-writing/SKILL.md) and the [integration report template](assets/integration-report-template.md) in the project's existing evidence record. Keep merged state, integration verification, and QA handoff readiness explicit.

Project Manager routes a ready candidate to QA for test-design and test-execution. The handoff identifies the immutable revision, included tasks, checks, gaps, and retained findings. It grants no deployment authority.
