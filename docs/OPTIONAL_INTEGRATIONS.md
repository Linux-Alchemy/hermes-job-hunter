# Optional integrations

Hermes Job Hunter is complete without authenticated cloud, messaging, Kanban, cron, or job-board accounts. Optional integrations must be installed and authorised separately and remain subordinate to `SOUL.md` and `job-hunter-core`.

## Google mail alerts

A read-only Gmail connector can supplement public job discovery by reading user-configured job-alert messages. It is **not included in this distribution**.

Why it remains external:

- Gmail read-only scope can expose the whole mailbox, not merely job alerts.
- OAuth credentials and refresh tokens are private runtime state.
- Alert messages contain sender, subject, snippet, URL, and message identifiers.
- A connector needs independent dependency, credential-storage, exception-redaction, scope, and test maintenance.
- Authenticated email access must not become a hidden prerequisite for ordinary public-source discovery.

If an adopter adds a connector:

1. require explicit approval for Gmail read-only access;
2. request only Gmail scope—do not bundle Calendar merely for convenience;
3. store OAuth material outside the repository with restrictive permissions and atomic writes;
4. make query/result counts bounded;
5. filter alerts by adopter-owned criteria without logging raw mailbox contents;
6. expose only the minimum fields needed for discovery;
7. redact provider exceptions before returning them to the model;
8. report `BLOCKED` or `DEGRADED` when unavailable;
9. require employer-original verification before any role recommendation;
10. provide revocation, deletion, rotation, and failure-cleanup instructions.

The source registry should represent mail alerts as an optional supplemental source with explicit authority requirements. A normal search must continue without it.

## Calendar

Calendar read access is unrelated to core job discovery and is not required by this package. If an adopter separately wants interview-calendar assistance, treat it as its own integration and approval scope. Do not require Calendar permission to read Gmail alerts.

## GitHub authentication

`github-portfolio-audit` defaults to public URLs and explicitly approved local paths. Authenticated or private-repository access is optional and separate. If enabled, scope it to named repositories and preserve the difference between public state, private state, and local clones.

## Messaging and Kanban

Messaging and Kanban may help coordinate a private career workflow, but neither belongs to the reusable core. Enabling them must not authorise:

- recruiter or employer contact;
- application submission;
- public-profile mutation;
- external commitments;
- forwarding private career evidence outside the configured workspace.

## Cron and scheduled scans

Scheduled discovery is optional. Use deterministic jobs where no reasoning is needed and self-contained prompts for model-driven scans. A scheduled scan inherits the same registry, query-budget, source-health, and no-external-action boundaries as an interactive run.

## Integration acceptance rule

An optional integration is acceptable only when:

- its authority and scopes are explicit;
- credentials remain adopter-owned and outside version control;
- the core workflow degrades honestly when it is absent;
- synthetic tests cover missing, expired, malformed, and permission-denied states;
- outputs are bounded and redact sensitive identifiers;
- it adds distinct value that public or local read-only inputs cannot provide more cheaply;
- installation does not silently broaden the default agent tool surface.
