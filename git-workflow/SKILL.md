---
name: git-workflow
description: Manage task branches, scoped commits, review diffs, PR preparation, and authorized Git integration. Use when starting or resuming a development task, preparing code for review, updating a branch, or executing an integration decision. Review acceptance and merge readiness remain with their owning functions.
---

# Git Workflow

Supply Git methods to developers, reviewers, and engineering lead. Follow the declared project policy and the caller's authorized operation. This tool Skill does not assign tasks, establish review independence, or approve a merge or deployment.

## 1. Inspect the operation and repository

Read the [Git contract](references/git-contract.md) for inputs, task identity, authority, and result records. Inspect current state before changing it. Preserve unrelated edits and reuse existing task branches and PRs.

Branch strategy, base, target, naming, and merge method come from project policy and the task. Do not introduce a permanent branching model or repository configuration as a side effect of ordinary work.

## 2. Use the relevant method

- For task start, resumption, commits, diff inspection, or PR preparation, read [task branches and review](references/task-and-review.md).
- For branch updates, conflicts, integration, or recovery, read [integration methods](references/integration-methods.md). The caller supplies the integration decision; [Code Integration](../code-integration/SKILL.md) owns the team's merge gate.

New development tasks follow claim → branch → task design → implementation. A reviewer can inspect a diff without claiming its development task. Read only the methods needed for the current operation.

## 3. Return observed results

Apply the Git contract's [result record](references/git-contract.md#result-record). Distinguish local changes, published PRs, confirmed remote merges, and unresolved operations. Use [Technical Writing](../technical-writing/SKILL.md) as the writing method for operation reports, PR descriptions, and handoff summaries.

Before publishing or delivering these outputs, use [Document Review](../document-review/SKILL.md) to review their content and supporting evidence. Document review does not replace Git operation checks.

Provider-specific PR commands and task-app updates belong to the applicable platform workflow. If publication is unavailable, retain the prepared content and name the missing capability. A prepared PR is not a published PR.

Methods reference: [ECC git-workflow](https://github.com/affaan-m/ECC/blob/main/skills/git-workflow/SKILL.md). Adapt its branch, commit, and conflict guidance to this team's contracts. Project policy controls conventions; candidate QA and ship approval remain separate from merge.
