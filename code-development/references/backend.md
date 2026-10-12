# Backend implementation

Read this for APIs, persistent state, service calls, or jobs. Follow the approved contracts and the project's existing boundaries. Repository, service, and middleware patterns are options; introduce a layer only for a present responsibility.

- **Request boundaries:** Validate input and enforce authorization for the affected resource. Preserve the contracted response and error semantics. Distinguish authentication, permission, validation, and internal failures; avoid exposing internal details.
- **Data and consistency:** Preserve transaction boundaries, invariants, and idempotency. Test relevant duplicates, concurrent updates, and partial failure. Use bounded queries and inspect repeated queries before introducing batching or indexes.
- **Dependencies and retries:** Apply supplied timeouts and cancellation behavior. Retry only eligible failures when repeated effects are safe, with bounded attempts. Do not hide exhausted retries as successful empty results.
- **Caching and background work:** Implement agreed freshness, invalidation, durability, and recovery behavior. A process-local cache, limiter, or queue cannot by itself prove guarantees across replicas or restarts. Resolve missing shared guarantees with the architect.
- **Operations:** Preserve required diagnostic context without exposing secrets. Keep schema changes, compatibility, and migration verification within the assigned design; production rollout remains a separate workflow.

Verify relevant storage and service contracts with realistic integration checks. Mocked success does not prove atomicity, migration correctness, or persistent job delivery. Verify performance claims with appropriate measurements rather than inferring them from a pattern.
