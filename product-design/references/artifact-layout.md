# Task artifact layout

This reference owns document paths and directory naming for product design, technical design, planning, and quality assurance (QA). Stage contracts own document contents, readiness, and approvals.

## Directory and filenames

Keep each coordinated product change in one directory under `<project-root>/doc/`. A change can include several Features and span several conversations. Development tasks produced by planner are children of that change, not separate product changes.

Use this layout:

```text
doc/
  YYYY-MM-DD-task-slug/
    product-design.md
    technical-design.md
    task-plan.md
    tasks/
      t1/
        task.md
        technical-design.md
      t2/
        task.md
        technical-design.md
    qa.md
    history/
      product-design/
        v1.md
```

The tree shows locations, not files to create in advance. `task-plan.md` and each `task.md` are planner outputs. Task technical designs appear after claim and branch creation. QA and history files appear only when their stages require them.

Use the change's start date and a short English slug with lowercase words separated by hyphens. Name the outcome or capability, such as `2026-10-12-team-invitations`. Keep that directory name stable.

| Filename | Purpose | Owning stage |
| --- | --- | --- |
| `product-design.md` | Product value, scope, rules, and examples | Product design |
| `technical-design.md` | Overall architecture, shared contracts, and verification strategy | Overall technical design |
| `task-plan.md` | Change-level scope, coverage, dependency overview, and links to standalone tasks | Planner |
| `tasks/<task-key>/task.md` | Authoritative task definition and entry point for the assigned Agent | Planner; execution owners update observed handoff evidence |
| `tasks/<task-key>/technical-design.md` | Local decisions and implementation readiness for that task | Task technical design |
| `qa.md` | QA scope, cases, execution results, and defects; distinguish planned checks from executed results | QA |
| `history/product-design/v<n>.md` | Immutable source version retained before a product revision | Product design |

Create each document when its stage produces content. An absent downstream document means that artifact has not been produced. Do not create empty technical designs, QA documents, review reports, or delivery directories. This layout defines the QA filename, not a QA workflow or template.

## Development task directories

Each development task has exactly one current standalone Markdown entry point. For task `T1`, use `tasks/t1/task.md`; for `T2`, use `tasks/t2/task.md`. Keep the task's title inside the document and plan index. The directory key uses the stable task ID in lowercase, without dates, titles, assignees, or status suffixes. Existing IDs stay unchanged; do not renumber tasks to make paths uniform. Check for ID/key collisions before creating files, and never overwrite a different task.

Keep paths stable when titles, owners, readiness, or execution state change. Do not move tasks between `todo/`, `doing/`, and `done/` directories. Task IDs are unique within a change; references across changes also identify the source change directory.

`task-plan.md` indexes tasks; it does not contain their full definitions. Each task file links back to the plan and pins its own source versions. Any owner, readiness, dependency, or state shown in the index is a summary of the referenced task version, not a second authority. The planner [plan contract](../../planner/references/plan-contract.md) defines synchronization, claim checks, and required task content.

Keep a task's new local technical design beside its entry point. Even a brief design uses that file. Other substantial task-local evidence can live in the same directory when needed; link it from `task.md`. Shared supporting designs remain at the change level and are linked from the overall technical design.

## Revisions and existing artifacts

Edit each current task file in place. Preserve substantive revisions through accessible repository history or an explicitly linked immutable snapshot when needed by the stage contract. Do not create parallel current files such as `task-v2.md` or `task-final.md`.

On a split, retain the original task file with its superseded disposition and replacement links. Create a new entry point for each replacement task and preserve acceptance coverage and dependency links. A post-merge correction also gets a new linked task file. Neither case permits reuse of the original ID for a different goal.

When revising an existing plan with inline task bodies, extract each task into its own entry point while preserving IDs, scope, baselines, claims, and branch/PR links. Replace inline bodies with index links after checking the extracted content and all affected references. Do not leave two authoritative task definitions. Retain an existing valid standalone task path or task-design location unless migration is requested or needed to resolve ambiguity; the new layout is the default for new artifacts.

## Select or create the change directory

1. Resolve the project root from the current project and available instructions.
2. Reuse the change directory identified by the user's request, source document, or current conversation. Read existing artifacts before editing.
3. For a new product change, create a new directory under `doc/`. If the name belongs to another change, append `-02`, `-03`, or the next unused suffix. Never overwrite another change to reuse its name.
4. When the change is ambiguous, inspect the candidate documents. Ask only if the available context cannot distinguish continuation from a new change.

Starting overall technical design, planning, or QA for an existing change does not create another change directory. Creating `tasks/t1/` adds a development task within the same change. Revisions and reopened decisions stay in that change's current files. A separate follow-up product change gets a new change directory; link the earlier change as context.

Keep one current product, overall technical, plan, and QA document per change, plus one task entry point and task design per development task. Record versions and approval according to the stage contract. Avoid filenames such as `product-design-v2.md`, `technical-design-final.md`, or `qa-latest.md`.

For product baseline retention, follow the [product version rules](document-contract.md#versions-and-approval-evidence). Immutable snapshots under `history/product-design/` are historical evidence; they do not replace the current `product-design.md`.

## References and handoff

Use relative links between task artifacts, such as `[Product design](product-design.md)`. Include the exact source version or revision when a downstream document depends on an approved baseline. Directory proximity does not establish approval or version compatibility.

Use these relative references for the default layout:

| From | To | Relative path |
| --- | --- | --- |
| Change-level plan | Task T1 entry point | `tasks/t1/task.md` |
| Task T1 entry point | Plan | `../../task-plan.md` |
| Task T1 entry point or local design | Product baseline | `../../product-design.md` |
| Task T1 entry point or local design | Overall technical baseline | `../../technical-design.md` |
| Task T1 entry point | Its local design | `technical-design.md` |
| Task T1 local design | Its task definition | `task.md` |
| Task T2 entry point | Dependency T1 | `../t1/task.md` |

Read before editing and recheck links after extraction or an authorized move. Distinguish the overall and task documents explicitly; both are named `technical-design.md` but have different scopes and paths.

Pass the change directory, plan path/version, and each receiving Agent's task path/version to downstream stages. A task entry point provides enough instructions and exact references to find its inputs without reconstructing prior conversations. Scope rule, question, contract, and test IDs to their source documents. File presence alone does not establish readiness, claim ownership, or completion.
