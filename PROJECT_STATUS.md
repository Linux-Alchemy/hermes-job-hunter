# Project Status

**Package state:** native distribution foundation established
**Release state:** public, installable pre-release
**Canonical purpose of this file:** show what is actually present in the repository and what remains private or unfinished.

## Implemented in this repository

| Component | State | Notes |
|---|---|---|
| Repository shape | Complete | Native Hermes distribution manifest, root profile files, skills, configuration, onboarding, tests, and architecture have clear homes. |
| Clean profile installation | Working | The repository installs directly through `hermes profile install` into an isolated Hermes home. |
| Profile authority contract | Initial public version | Generic, review-gated, and free of private paths or identities. |
| Core skill | Initial public version | Evidence labels, source precedence, authority, status, and refusal rules. |
| Cover-letter drafting skill | Initial public version | Four-source authorship model, shared notes/draft workspace, evidence and voice checks, explicit human approval, and clean-source handoff. |
| Source-registry maintenance skill | Initial public version | Separates source evaluation from runtime search, preserves Markdown rationale plus YAML configuration, and requires explicit approval before local registry mutation. |
| Source-registry schema | Initial public version | Twenty-five source definitions retained as an inert template; every source is disabled pending local verification. |
| Source decision-record template | Initial public version | Separates human rationale from executable configuration. |
| Job-discovery runtime skill | Initial public version | Registry-gated bounded search, normalized posting contracts, source-health states, employer-original verification, synthetic acceptance cases, and review-ready output template. |
| Job-discovery skill research | Decision implemented | Candidate audit and clean-room boundary produced the public `job-discovery` runtime skill; source onboarding remains separate. |
| Voice-calibration onboarding | Initial public version | Teaches adopters to calibrate a user-owned overlay without shipping private samples. |
| Acceptance matrix | Initial version | Defines required success, degraded, stale, refusal, and clean-install tests. |
| Package validator | Working | Validates structure, YAML, skill frontmatter, links, symlinks, and common leakage patterns. |
| Licence | Complete | MIT licence recorded at repository root and in distribution/skill metadata. |

## Deliberately private

The following remain outside this repository:

- the live specialist profile and runtime state;
- user-specific career evidence, résumé material, role strategy, and target employers;
- personal voice samples and calibration results;
- live account state, messaging identifiers, tokens, OAuth files, logs, caches, sessions, and scheduled jobs;
- the live source registry and its current access-test dates;
- real application and job-search artefacts.

Private evidence can prove that a public procedure works. It is not itself a public package component.

## Not migrated yet

- matching-profile and evidence-bank schemas;
- application-packet and résumé-drafting skills and templates;
- deterministic résumé and cover-letter rendering;
- sanitized portfolio, résumé, and LinkedIn audit procedures;
- synthetic candidate, posting, source-failure, and application fixtures;
- update, rollback, and release instructions;
- a full-capability clean-profile end-to-end acceptance run;
- tagged-release notes and version metadata for the first stable release.

## Next build sequence

1. Add the normalized matching-profile and evidence-bank contracts used by the implemented discovery and source-maintenance skills.
3. Run synthetic normal, degraded, stale, blocked, location-trap, duplicate, and injection cases.
4. Install the proven generic skill into the private specialist profile through local configuration.
5. Build the smaller `job-source-discovery` onboarding/maintenance skill.
6. Add the reviewed application-packet, résumé-drafting, and deterministic document-rendering capabilities; the collaborative cover-letter drafting skill is already present.
7. Repeat clean-install, leakage, provenance, and human semantic review against the expanded package before a tagged release.

## Migration rule

A private artefact reaches this repository only after it is classified as one of:

- **clean-room authored** — rebuilt from the proven procedure without private content;
- **sanitized from local source** — mechanically scrubbed and semantically reviewed;
- **upstream-derived** — licence, exact provenance, changes, and authority review recorded.

Copying a private runtime file and replacing a name is not sufficient sanitation.
