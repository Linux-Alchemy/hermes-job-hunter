# Runtime Contracts

These contracts define how `job-discovery` plans a run, records source health, normalizes postings, verifies eligibility, and hands a short slate back to the user.

## 1. Search-run contract

Every run records:

```yaml
run_id: "job-scan-YYYYMMDD-HHMM"
run_date: "YYYY-MM-DD"
mode: read_only
career_snapshot:
  path: "config/career_matching_profile.local.yaml"
  version: "<observed version or UNKNOWN>"
registry:
  path: "config/job_source_registry.local.yaml"
  schema_version: 1
  registry_version: "<observed version>"
constraints:
  jurisdictions: ["<configured jurisdiction>"]
  subregion_checks: ["<configured state/province/region>"]
  work_modes: ["remote"]
  actual_remote_required: true
  freshness_days: 7
  employment_preferences: ["full_time", "contract_if_labelled"]
  role_families: []
  excluded_terms: []
execution:
  requested_lanes: ["automated_core"]
  selected_source_ids: []
  query_budget: 12
  result_cap: 10
output:
  path: "<declared path>"
  state: advisory
owner: "<human decision owner>"
prohibited_actions:
  - account_or_subscription_creation
  - authenticated_job_board_access
  - connector_installation
  - application_submission
  - external_messaging
```

Use the current date for the actual run. Do not invent a missing snapshot or registry version.

## 2. Source execution record

Every selected or planned source receives one record:

```yaml
source_id: "<registry source_id>"
display_name: "<registry display_name>"
lane: "<registry lane>"
access_method: "<registry access_method>"
queries_attempted: []
accessed_at: "YYYY-MM-DD"
runtime_result: COMPLETE | DEGRADED | BLOCKED | NOT_EVALUATED | STALE
results_observed: 0
candidates_retained: 0
pagination_or_sample_limit: "UNKNOWN"
failures_or_limits: []
notes: ""
```

### State rules

- `COMPLETE`: the intended bounded query slice ran through its approved route and returned enough data to evaluate that slice. It does not mean every job was found.
- `DEGRADED`: extraction was partial, indexed-only, sampled, truncated, missing key metadata, or relied on an unreliable route.
- `BLOCKED`: login, paywall, CAPTCHA, anti-bot control, hard timeout, or unavailable endpoint prevented useful evaluation.
- `NOT_EVALUATED`: the source was eligible but deliberately skipped because the query budget, lane, stop condition, or result cap made it unnecessary.
- `STALE`: the registry/access evidence is too old or internally inconsistent to rely on without source revalidation.

A zero-result slice may be `COMPLETE` if the query executed reliably and the source clearly returned no matches. Do not use `COMPLETE` when only a search-engine snippet was available.

## 3. Normalized posting contract

Every retained posting uses all fields. Missing values are the literal evidence state `UNKNOWN`; do not omit fields.

```yaml
candidate_id: "<stable run-local id>"
title: "<observed title or UNKNOWN>"
employer: "<observed employer or UNKNOWN>"
role_family: "<matched family or UNKNOWN>"
discovery:
  source_id: "<registry source id>"
  url: "<discovery URL>"
  accessed_at: "YYYY-MM-DD"
employer_original:
  url: "<original URL or UNKNOWN>"
  verification_state: VERIFIED | VERIFY_BEFORE_USE | CONFLICT | UNKNOWN
  open_state: OPEN | CLOSED | UNKNOWN
location:
  stated: "<source text or UNKNOWN>"
  work_mode: REMOTE | HYBRID | ONSITE | UNKNOWN
  jurisdiction_eligibility: VERIFIED_ELIGIBLE | VERIFIED_INELIGIBLE | CONFLICT | UNKNOWN
  subregion_eligibility: VERIFIED_ELIGIBLE | VERIFIED_INELIGIBLE | CONFLICT | UNKNOWN
employment_type: "<observed type or UNKNOWN>"
posting_date: "YYYY-MM-DD | UNKNOWN"
freshness_state: VERIFIED | STALE | UNKNOWN
salary:
  value: "<observed range/value or UNKNOWN>"
  currency: "<observed currency or UNKNOWN>"
requirements:
  required: []
  preferred: []
  ambiguous: []
evidence_comparison:
  met: []
  partial: []
  missing: []
  unknown: []
  hard_gates: []
  stretch_requirements: []
  employer_preferences: []
source_conflicts: []
security_notes: []
review_state: VERIFIED_FOR_TRIAGE | VERIFY_BEFORE_USE | REJECTED
triage: APPLY | APPLY_WITH_TAILORING | BUILD_ONE_MISSING_BRICK | SKIP | NOT_ASSIGNED
rationale: "<concise evidence-bounded explanation>"
```

### Required invariants

1. `triage` must be `NOT_ASSIGNED` when `review_state` is `VERIFY_BEFORE_USE`.
2. `APPLY` and `APPLY_WITH_TAILORING` require:
   - employer-original `verification_state: VERIFIED`;
   - `open_state: OPEN`;
   - requested-jurisdiction eligibility verified as eligible;
   - no unresolved hard gate.
3. `VERIFIED_INELIGIBLE` for the requested jurisdiction produces `SKIP` once the employer source is verified.
4. A missing date may produce `freshness_state: UNKNOWN`, never a fabricated date.
5. A job-board `remote` label alone does not produce verified requested-jurisdiction or subregion eligibility.
6. Aggregator/employer conflicts stay in `source_conflicts`; the employer-original source governs current facts when reachable.
7. Near-identical descriptions under different employers produce a warning for possible agency cross-listing; they are not automatically deleted.

## 4. Query planning contract

### Role clusters

Use two to four related titles per query cluster. Avoid vague one-word searches and giant Boolean expressions.

Example shape:

```yaml
cluster_id: technical_support_operations
terms:
  - "technical operations"
  - "application support"
  - "implementation specialist"
  - "product support"
skill_terms:
  - Python
  - SQL
  - APIs
location_terms:
  - Canada
  - remote
```

Do not force every skill term into every board query. Some sources support structured categories; others behave better with one title and one location.

### Budget accounting

Count each independent web search or source query against the default query budget. Employer-original verification fetches for already shortlisted roles do not count as discovery queries, but they remain bounded by the result cap.

If the budget is exhausted, mark remaining planned sources `NOT_EVALUATED` and explain the stop. Do not silently exceed the cap because the results looked interesting.

## 5. Source-route hierarchy

Use the lowest-cost reliable route already allowed by the registry:

| Rank | Route | Typical state |
|---|---|---|
| 1 | Public structured API/RSS/direct ATS | `COMPLETE` when bounded response is readable |
| 2 | Public board pages | `COMPLETE` or `DEGRADED` depending on pagination/metadata |
| 3 | Indexed web result | `DEGRADED`; every retained hit needs employer verification |
| 4 | Login/paywall/anti-bot route | `BLOCKED`; stop for that source |

Do not install tooling or switch to authenticated browsing to improve a source result.

## 6. Liveness and location verification

### Liveness

`OPEN` requires current employer-source evidence such as an active posting page with the role description and an active application control or explicit open status. A search index, aggregator page, cached snippet, or old posting date cannot establish liveness alone.

`CLOSED` requires explicit closure/no-longer-available evidence or an employer page that unambiguously says the role is gone.

Otherwise use `UNKNOWN`.

### Remote condition

Classify workplace mode separately from hiring jurisdiction.

Examples:

| Source wording | Work mode | Canada eligibility |
|---|---|---|
| "Remote — Canada" | `REMOTE` | potentially `VERIFIED_ELIGIBLE` after employer check |
| "Remote — United States only" | `REMOTE` | `VERIFIED_INELIGIBLE` |
| "Remote camp, 14 days on/14 off" | `ONSITE` or `UNKNOWN` depending on facts | do not call work-from-home |
| "Hybrid; Toronto office 3 days/week" | `HYBRID` | Canada may be eligible, but fails a remote-only run |
| "Remote" with no jurisdiction | `REMOTE` | `UNKNOWN` |
| "Work from anywhere" with payroll countries listed | `REMOTE` | use the explicit payroll list |

Ontario eligibility is checked when the posting excludes provinces, requires residence near an office, or otherwise narrows Canadian hiring. Do not infer Ontario exclusion merely because only Canada is stated.

## 7. Requirement comparison

For each material requirement:

- `met`: supported by approved evidence at the required depth;
- `partial`: adjacent or incomplete evidence supports part of the requirement;
- `missing`: available evidence shows the requirement is not currently supported;
- `unknown`: the profile or posting does not establish the answer.

Then classify its decision role:

- `hard_gate`: legal/authorization, licence, explicit mandatory credential, location, or genuinely non-negotiable technical requirement;
- `stretch_requirement`: experience or depth that may be flexible given the role body;
- `employer_preference`: explicitly preferred/nice-to-have;
- `ambiguous`: unclear or internally inconsistent wording.

Years of experience are not automatically a hard gate. Read whether the duties and wording make the number essential. Never inflate experience to bridge it.

## Output ordering

The report is a decision aid first and an audit trail second. Use this sequence:

1. decision brief;
2. ranked action queue;
3. verified recommendations;
4. verification queue;
5. verified skips and unresolved patterns;
6. market observations;
7. run contract and source health;
8. search record;
9. actions, limitations, and next owner.

### Decision brief

Lead with the useful answer in no more than roughly 8–12 lines:

- whether any role is ready for an application decision;
- the top two or three next inspections, in order;
- the main recurring fit signal or blocker;
- the artifact path;
- external actions taken.

Do not make the user read the source-health table before learning whether anything useful was found.

### Ranked action queue

Rank by **decision usefulness**, not by discovery order, employer prestige, or keyword density. Use this precedence:

1. `APPLY`;
2. `APPLY_WITH_TAILORING`;
3. `BUILD_ONE_MISSING_BRICK` when the brick is specific and realistically actionable;
4. all retained `VERIFY_BEFORE_USE` candidates, interleaved with verified outcomes where appropriate and ranked by **best evidence-supported match descending**.

### Match ranking

The queue's primary sort answers: **Which opportunity appears to match the user best?** Rank by:

1. alignment between the actual duties and the user's target role families;
2. depth and relevance of approved `met` evidence;
3. number and severity of `partial` or `missing` material requirements;
4. distance from an explicit hard gate;
5. practical application value, including whether the role accepts early-career or transferable evidence.

Do not rank by employer prestige, source order, title familiarity, or keyword count. Do not invent a numeric score unless the user requests one.

Verification readiness is a separate displayed dimension, not the primary sort:

- employer live + Canada/Ontario eligible;
- employer live + jurisdiction unresolved;
- employer liveness unresolved or conflicting.

A stronger apparent match may rank above a weaker verified role while remaining `VERIFY_BEFORE_USE`. Its unresolved eligibility, liveness, or requirements must be prominent, and its triage remains `NOT_ASSIGNED`.

Within effectively tied match quality, prefer:

1. fewer unresolved hard gates;
2. stronger employer-original verification;
3. cheapest bounded next check.

`SKIP` is never part of the ranked action queue. Keep it in the verified-skips section, except for an optional one-line warning in the decision brief when a false positive is especially tempting.

This precedence is ordinal, not a numeric score. Explain close rankings in one sentence.

### Section invariants

- **Verified recommendations** contains only `APPLY`, `APPLY_WITH_TAILORING`, or `BUILD_ONE_MISSING_BRICK`.
- If there are none, say `No verified application-ready roles in this run.` Do not put `SKIP` entries under a heading containing “recommended.”
- **Verification queue** contains `VERIFY_BEFORE_USE` candidates only, ordered by best evidence-supported match descending with readiness and unresolved gates shown separately.
- **Verified skips** contains rejected roles and concise reasons. Give full detail only for instructive false positives; aggregate low-value rejects as counts/patterns.
- Keep the complete audit trail, but place it after the decision material.

Keep the useful slate short. Counts and reasons are better than dumping every weak listing.
