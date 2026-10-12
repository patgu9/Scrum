# Frontend implementation

Read this for changed UI behavior. Use the approved interaction and visual requirements, existing component system, and installed framework. Missing product behavior returns upstream; small local implementation choices stay with the developer.

- **Composition and state:** Reuse existing components. Keep state near its owner; avoid duplicating derived state or adding a global store for local behavior. In React, follow hook rules and use prior-state updates when the new value depends on it.
- **Asynchronous interaction:** Implement the required loading, empty, success, and error states. Prevent stale responses from overwriting newer input. Clean up subscriptions and timers; handle cancellation and duplicate submission according to the contract. Prefer an existing data library over an improvised cache.
- **Forms and access:** Use semantic controls, associated labels, usable error messages, keyboard operation, and appropriate focus behavior. Preserve user input on recoverable errors. Browser validation improves feedback; server-side validation and authorization remain required at their own boundaries.
- **Performance:** Use memoization, lazy loading, or virtualization when evidence or a stated target warrants them. Verify the result without removing necessary loading, focus, or accessibility behavior.

Test observable interaction and relevant failures. Include changed keyboard/focus paths and representative layouts where applicable; keep actual visual or browser checks distinct from component-test passes. Framework examples do not establish a complete accessibility implementation.
