# UML modeling

Use models to resolve material questions about structure and behavior. First inspect existing diagrams, tables, or textual flows. Add a view only when it makes unresolved relationships, ordering, or state easier to inspect. Do not produce every diagram type or model every implementation class.

## Select views by design question

Use the table to select a view when existing expression is insufficient. A clear table or textual flow can be sufficient; no diagram is required solely because a characteristic exists. Record material coverage gaps and their effect on the design. Explain alternative notation and preserve the required meaning.

| Design question or characteristic | UML view | Meaning to show |
| --- | --- | --- |
| Several modules or system boundaries must coordinate | Component | Responsibilities, provided and required interfaces, and dependency direction |
| Domain types, ownership, or multiplicity affect correctness | Class | Relevant concepts or types, associations and multiplicities, constraints, and justified composition or generalization |
| Asynchronous work or order-sensitive interaction | Sequence | Participants, synchronous or asynchronous messages, responses, ordering, and relevant failure or retry branches |
| An entity or job has a meaningful lifecycle | State machine | Initial and terminal states where applicable, transition events, guards, effects, and handling of rejected events |
| Branches, parallel work, rejection, or recovery need clarification | Activity | Actions, decisions and guards, fork/join behavior, completion, and failure paths |
| Runtime placement affects trust, availability, or communication | Deployment | Nodes or execution environments, deployed artifacts, communication paths, and relevant trust or failure boundaries |

Use other UML views only when they answer an additional design question. Reference approved product scenarios rather than rebuilding product discovery through use-case diagrams.

## Use views to replace repeated prose

Prefer a diagram when the reader must reconstruct relationships, ordering, or transitions from paragraphs. Use a decision table for combinations of conditions and outcomes, a comparison table for alternatives, and prose for rationale or a simple fact. Do not turn a short statement into a diagram solely to increase visual coverage.

Give each diagram one question and a consistent abstraction level. Distinguish participants, components, and stored data; label their relationships. Show execution or trust boundaries when they affect the decision. Put essential entry paths, branches, guards, and failure outcomes in the view itself; identify intentionally omitted behavior with a reference. Keep independent status dimensions separate instead of inventing a single lifecycle.

After adding a view, remove the prose that merely enumerates its nodes or repeats its paths. Keep a short explanation of its conclusion, constraints, exceptions, and evidence references. If a table cell contains a narrative, keep the comparable fact in the cell and link its detailed basis. Do not squeeze the same long text into node labels or table cells.

Use multiple small views when one becomes difficult to follow. Reuse names and source references across them. Inspect rendered readability when tooling is available; record an unavailable rendering check without treating source syntax as visual verification.

## Keep each mode at its decision depth

Apply the contract's [decision-depth rules](document-contract.md#decision-depth-and-deferred-work) to models. Overall views show shared agreements needed for planning; task views reference them and refine assigned behavior. A conceptual class does not require a matching implementation class. Use the contract's feedback process for changed shared decisions.

Give each view a title, purpose, and scope. Identify whether it describes current or proposed behavior and link its baseline or evidence. In the caption or adjacent explanation, connect relevant elements and paths to document-qualified product rules, `C<n>` contracts, or `T<n>` scenarios. Explain key constraints that the notation cannot express clearly.

## Preserve semantics and editable sources

Reuse the project's diagram tooling when it preserves the required meaning. Prefer Mermaid for Markdown views it can express clearly, such as sequence, state, and class diagrams. Use PlantUML or the established UML tool when the required notation is better supported there, including component, activity, or deployment views.

Keep diagram source in the design or in a linked file beside it. Link any rendered export to that source and update both together. If rendering is unavailable, preserve the source and state that rendering was not verified.

Label simplified or non-UML notation explicitly. A generic flowchart, C4 view, or entity-relationship diagram can supplement the design; it does not automatically establish UML semantics. Define the meaning of any custom arrows or symbols. Do not change a relationship's meaning merely to fit the renderer.

Use association for a structural relationship, dependency for use, generalization for specialization, and composition only when exclusive whole-part ownership and lifecycle semantics apply. Distinguish message order from timing guarantees. Show timeout, retry, cancellation, or compensation paths when required by the contract; do not invent those behaviors to fill the diagram.

## Check the model against the design

Trace a normal path and each relevant boundary or failure path through the selected views and their linked contracts. Check that:

- Names, interfaces, ownership, relationship direction, and multiplicities agree across views and text.
- Sequence messages agree with interfaces; resulting state changes satisfy guards and invariants.
- Activity branches and parallel paths have defined outcomes; deployment paths respect the stated trust and failure boundaries.
- Important transitions, failures, and prohibited outcomes have verification obligations at the selected mode's depth.

Record undefined behavior or contradictions in the existing question or finding record. Recheck affected views when contracts or tests change. Rendering success verifies presentation only; it does not prove semantic correctness or implementation behavior.

Notation references: [OMG UML specification](https://www.omg.org/spec/UML/2.5.1), [Mermaid class diagrams](https://mermaid.js.org/syntax/classDiagram.html), [Mermaid state diagrams](https://mermaid.js.org/syntax/stateDiagram.html), and [PlantUML diagram support](https://plantuml.com/).
