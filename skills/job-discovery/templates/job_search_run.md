# Job search run — <YYYY-MM-DD>

**State:** advisory | review_ready | blocked  
**Run ID:** `<job-scan-YYYYMMDD-HHMM>`  
**Decision owner:** <human decision owner>

## Decision brief

- **Application-ready roles:** <count and concise outcome>
- **Check first:** <role — employer — why this is the cheapest/highest-value next decision>
- **Check second:** <role — employer — why>
- **Check third:** <optional>
- **Recurring signal or blocker:**
- **Artifact:**
- **External actions:** none

Keep this to roughly 8–12 lines. Lead with the decision, not the machinery.

## Ranked action queue

| Priority | State | Role | Employer | Why now | Next bounded action | Owner |
|---:|---|---|---|---|---|---|

Order every non-`SKIP` serious candidate by best evidence-supported match in descending order. Show state and unresolved verification gates separately; a first-ranked `VERIFY_BEFORE_USE` candidate remains unapproved. Break close fit ties by fewer unresolved hard gates, stronger employer verification, then cheapest bounded check. `SKIP` never appears in this table.

## Verified recommendations

If empty, write:

> No verified application-ready roles in this run.

### <APPLY | APPLY_WITH_TAILORING | BUILD_ONE_MISSING_BRICK> — <role> — <employer>

- Employer-original posting:
- Discovery source(s):
- Open/freshness state:
- Work mode:
- Requested-jurisdiction/subregion eligibility:
- Employment type/salary:
- Why it fits:
- Requirements met:
- Requirements partial:
- Requirements missing:
- Requirements unknown:
- Hard gate:
- Stretch/preferences:
- Tailoring or missing brick:
- Evidence limitations:

Never place a `SKIP` under this heading.

## Verification queue

### VERIFY_BEFORE_USE — <role> — <employer>

- Queue priority and reason:
- Discovery URL/source:
- Employer-original URL: `UNKNOWN` or unverified
- What appears promising:
- Already verified:
- Missing liveness/location/eligibility/requirement evidence:
- Source conflicts:
- Triage: `NOT_ASSIGNED`
- Next bounded verification action:
- Owner:

Order the queue by best evidence-supported match descending. Keep verification readiness and unresolved gates visible, but do not use them as the primary sort. Break close fit ties by fewer unresolved hard gates, stronger employer verification, then cheapest bounded check.

## Verified skips and unresolved patterns

### SKIP — <role> — <employer>

- Concise decision reason:
- Employer-original evidence:
- Why it was tempting, if instructive:
- Evidence limitation or hard gate:

Aggregate ordinary rejects as counts and patterns rather than giving every weak listing a full dossier.

## Market observations

- Label each item `OBSERVED`, `INFERRED`, or `UNKNOWN`.
- Do not generalize beyond the sources and query slice searched.

## Run contract

- Career snapshot:
- Registry schema/version:
- Jurisdiction/subregion:
- Work mode and actual-remote condition:
- Freshness window:
- Included/excluded role families:
- Source lanes and selected sources:
- Query budget used:
- Result cap:
- Output path:
- Prohibited actions:

## Source health

| Source | Lane | Queries | Runtime result | Observed | Retained | Limits/failures |
|---|---|---:|---|---|---:|---|

Runtime result is one of `COMPLETE`, `DEGRADED`, `BLOCKED`, `NOT_EVALUATED`, or `STALE`. `COMPLETE` describes only the bounded query slice.

## Search record

| Source | Query/access route | Access date | Result state | Material limitation |
|---|---|---|---|---|

## Actions and status

- Canonical writes:
- External actions taken: none
- Accounts, credentials, applications, messages, uploads, or public mutations: none
- Blockers/unknowns:
- Next action:
- Next owner: <human decision owner>
- Timestamp:
