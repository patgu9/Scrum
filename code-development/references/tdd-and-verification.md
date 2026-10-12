# TDD and verification

This reference owns the development execution loop. Technical design owns the planned scenarios, boundaries, and evidence obligations. Reuse those inputs and refine tests as implementation reveals facts.

## Establish the runner and baseline

Inspect the project's test files, scripts, lockfiles, configuration, and CI requirements. Identify the actual runner and commands for focused tests, relevant regression, build, lint, types, and coverage where applicable. A package manager is not necessarily the test runner. Do not assume a particular stack or helper script exists.

Run relevant existing checks to establish the starting state. Record existing failures separately from new ones. Repair necessary setup within scope; route larger environment or infrastructure work to its owner. An unavailable required test environment remains an evidence blocker, not a reason to claim TDD is inapplicable.

Select the smallest reliable test boundary that proves the assigned claim. Use the design's integration and end-to-end checks where narrower tests cannot establish it. Control time, randomness, and external dependencies at explicit boundaries. A mock proves behavior against the replacement; retain required real integration checks.

## Execute one behavior at a time

1. **Red:** Add or change a test for one required behavior. Derive its expected result from acceptance or a shared contract. Run the exact target and confirm the intended missing or incorrect behavior causes the failure before changing the corresponding production behavior.
2. **Green:** Make the smallest sufficient implementation change. Rerun the same target and confirm that the previously failing check passes. Run relevant regression checks. Correct production code rather than weakening valid assertions.
3. **Refactor:** Improve structure where useful without changing the required behavior. Keep relevant tests green. If no refactor is warranted, record that judgment.
4. Repeat for the next behavior. Keep code and tests together within the task. A scenario inventory does not require writing every executable test before the first implementation step.

A runtime Red requires evidence that the intended test executed and failed for the expected reason. An intentional compile-time Red is valid when the new test exercises a missing API or type contract and the compiler diagnostic demonstrates that gap. Unrelated syntax errors, failed discovery, missing dependencies, or broken setup do not count. A test file that has not run supplies no Red evidence.

If a new test passes immediately, investigate whether the behavior already exists or the test misses the defect. Strengthen a deficient test without inventing a failure. Do not break correct production code to manufacture Red. A legitimate discovery can reduce the implementation needed; report the evidence and route any task-scope change to planner.

Tests should assert observable results and relevant side effects rather than reproduce the implementation's private call sequence. Several assertions can establish one behavior. Keep fixtures isolated and failures diagnosable. Never suppress a required failing test, loosen its expected result, or blindly replace snapshots to obtain Green.

## Existing code and alternative verification

| Change or starting state | Verification treatment |
| --- | --- |
| Bug with missing regression protection | Add a reproducer that fails for the defect, then fix and verify it |
| Bug already caught by an applicable test | Reproduce its valid failure, then use it for the loop; no duplicate test is needed |
| Behavior-preserving refactor | Establish passing characterization or regression checks before editing; rerun afterward. This is baseline protection, not an invented Red |
| Documentation, configuration, generated output, or mechanical change | Select checks for its actual effects, such as links, schema validation, generation reproducibility, build, or relevant regression. Explain why a new failing behavior test is unnecessary |
| Inherited implementation without historical Red evidence | Preserve it and report the gap. A safe isolated replay against the recorded earlier state can add explicitly labeled retrospective evidence; never present it as test-first history or reset the shared checkout |

Separate lack of historical TDD evidence from current correctness evidence. An inherited change can have passing verification without proving test-first development. State that limit for independent review. If an explicit project rule requires missing historical evidence, keep the affected delivery condition blocked rather than waiving it.

## Final verification

Run project-required developer checks and the relevant regression and integration checks for the delivered code state. Select broader checks from changed behavior, dependencies, and risk. Include browser, accessibility, migration, concurrency, or performance checks when needed to substantiate assigned acceptance. Do not require every category for every task.

Apply project-defined coverage thresholds and report the command, measurement scope, result, and exclusions. If no threshold exists, identify untested relevant behavior without inventing a percentage gate. Line coverage cannot establish assertion quality, real dependency compatibility, or complete acceptance coverage.

A pass applies to its tested state and environment. After code or baseline changes, reassess and rerun affected checks. Record flaky failures and their investigation; a later pass alone does not explain an earlier failure. Required checks that remain failed, skipped, unavailable, or unrun block implementation verification under the development contract.

## Preserve execution evidence

For each implemented behavior, record the source acceptance or contract, test identity and level, actual command and working directory, relevant environment, and code revision or identifiable working-tree state. Record expected and actual Red, subsequent Green, and refactor/regression results with concise output excerpts or durable log references. Record chronology as work happens; a final passing suite cannot reconstruct earlier execution.

Mark planned, unrun, failed, passed, baseline-only, retrospective, and inapplicable evidence accurately. Include the reason and affected conclusion for gaps. Keep claims no broader than their checks, especially when services were mocked or only a unit boundary ran.

Store the evidence in the development delivery record defined by the [contract](development-contract.md#delivery-conditions). Include the final code state and carry the record into the PR handoff. Commit identifiers can locate code, but commit messages alone do not prove a test ran.
