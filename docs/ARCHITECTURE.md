# Architecture

## The four layers

Hermes Job Hunter separates runtime identity, reusable procedure, private configuration, and private evidence.

```text
┌──────────────────────────────────────────────┐
│ Profile contract                            │
│ SOUL.md                                     │
│ Mission, authority, refusal, human ownership│
└──────────────────────┬───────────────────────┘
                       ↓
┌──────────────────────────────────────────────┐
│ Skills                                       │
│ Reusable procedures and output contracts     │
└──────────────────────┬───────────────────────┘
                       ↓
┌──────────────────────────────────────────────┐
│ Local configuration                          │
│ Source registry, matching profile, evidence  │
│ bank, integration settings                   │
└──────────────────────┬───────────────────────┘
                       ↓
┌──────────────────────────────────────────────┐
│ Review-ready artefacts                       │
│ Fit reports, drafts, packets, search records │
│ Human approval owns every external action    │
└──────────────────────────────────────────────┘
```

## Package versus live profile

The repository root is a native Hermes profile distribution. `distribution.yaml`, `SOUL.md`, `config.yaml`, and `skills/` are installed as the agent; the remaining directories contain reusable schemas, templates, onboarding, development documentation, and acceptance tests.

A live installation contains private values:

- career evidence;
- target roles and exclusions;
- account and integration state;
- enabled source decisions;
- writing samples and calibration;
- application history;
- runtime logs, sessions, memory, credentials, and scheduled jobs.

The live profile is evidence that the package works. It is not copied into the repository and scrubbed line by line.

## Source model

A source has two kinds of state:

### Configuration state

- execution lane;
- enabled state;
- setup state;
- access method and connector;
- authority requirement;
- known failure modes;
- last local access test;
- employer-verification requirement.

### Runtime result state

- `COMPLETE` — the configured bounded query completed;
- `DEGRADED` — only partial or unreliable access was obtained;
- `BLOCKED` — a technical or authority boundary prevented evaluation;
- `NOT_EVALUATED` — the source was intentionally not run;
- `STALE` — results or access verification are too old for confident use.

These states survive into the final report. A source returning three indexed snippets is not magically promoted to a complete market search.

## Human record and machine registry

Two files do different jobs:

- `source_access_decisions.local.md` records rationale, trade-offs, exclusions, and review decisions;
- `source_registry.local.yaml` supplies stable fields the discovery skill can execute consistently.

The skill reads YAML. Humans maintain the Markdown rationale. Git history records changes without forcing prose to behave like configuration.

## Discovery and fit flow

```text
load profile + registry + matching profile + evidence bank
                            ↓
select explicitly enabled sources
                            ↓
collect bounded listing metadata
                            ↓
normalise and deduplicate
                            ↓
apply jurisdiction, remote, freshness, and hard-gate checks
                            ↓
retrieve duty and evidence detail for plausible roles
                            ↓
verify at employer-original source where possible
                            ↓
classify APPLY / APPLY_WITH_TAILORING /
         BUILD_ONE_MISSING_BRICK / SKIP
                            ↓
write short evidence-labelled slate for human review
```

## Cover-letter drafting flow

```text
current user notes + employer-original posting
                + company profile + approved résumé evidence
                                      ↓
                         extract one truthful argument
                                      ↓
                  preserve notes in a shared draft workspace
                                      ↓
                         write one complete first pass
                                      ↓
                    human annotations and explicit approval
                                      ↓
                 clean approved Markdown source without rewriting
                                      ↓
             separately authorised rendering and external action
```

The file is the collaboration surface. Raw notes remain intact through review, while the clean source is created only after explicit human approval. Rendering remains a separate capability and must not edit approved prose or silently substitute a missing configured font.

## Authority model

The default package is read-and-draft only.

| Effect | Default |
|---|---|
| Read approved private career evidence | Allowed |
| Read approved public sources | Allowed |
| Write private review artefacts | Allowed |
| Create local skill/configuration patches | Requires explicit owner approval |
| Read authenticated accounts | Optional integration with separate review |
| Fill forms or upload documents | Forbidden |
| Submit applications | Forbidden |
| Message employers or recruiters | Forbidden |
| Mutate public profiles or repositories | Forbidden |
| Create accounts, subscriptions, keys, or alerts | Forbidden |
| Bypass access controls | Forbidden |

Optional integrations do not silently inherit broader authority.

## Failure and escalation

Failures remain explicit:

1. record the source or dependency that failed;
2. preserve what was and was not evaluated;
3. return `DEGRADED`, `BLOCKED`, `STALE`, or `UNKNOWN` as appropriate;
4. continue only through already approved fallback lanes;
5. request setup or authority expansion as a separate human decision;
6. never fabricate completion or route around a restriction.

## Configuration still to be added

The source registry exists. Matching-profile and evidence-bank schemas are the next configuration layers. They will remain private in live use and ship only as blank or synthetic examples.
