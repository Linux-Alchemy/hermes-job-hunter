# Project Status

**Package state:** foundation established  
**Release state:** private, not install-ready  
**Canonical purpose of this file:** show what is actually present in the repository and what remains private or unfinished.

## Implemented in this repository

| Component | State | Notes |
|---|---|---|
| Repository shape | Complete | Runtime profile, skills, configuration, onboarding, tests, and architecture have clear homes. |
| Profile authority contract | Initial public version | Generic, review-gated, and free of private paths or identities. |
| Core skill | Initial public version | Evidence labels, source precedence, authority, status, and refusal rules. |
| Source-registry schema | Initial public version | Twenty-five source definitions retained as an inert template; every source is disabled pending local verification. |
| Source decision-record template | Initial public version | Separates human rationale from executable configuration. |
| Voice-calibration onboarding | Initial public version | Teaches adopters to calibrate a user-owned overlay without shipping private samples. |
| Acceptance matrix | Initial version | Defines required success, degraded, stale, refusal, and clean-install tests. |
| Package validator | Working | Validates structure, YAML, skill frontmatter, links, symlinks, and common leakage patterns. |

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

- the job-discovery and fit skill that consumes the registry;
- matching-profile and evidence-bank schemas;
- application-packet skill and templates;
- deterministic résumé and cover-letter rendering;
- sanitized portfolio, résumé, and LinkedIn audit procedures;
- synthetic candidate, posting, source-failure, and application fixtures;
- install, upgrade, and rollback instructions;
- a clean-profile end-to-end acceptance run;
- public licence and release metadata.

## Next build sequence

1. Build the job-discovery/fit skill against `source_registry.example.yaml`.
2. Add versioned matching-profile and evidence-bank schemas.
3. Run synthetic normal, degraded, stale, blocked, and injection cases.
4. Install the proven generic skill into the private specialist profile through local configuration.
5. Add the reviewed application packet and deterministic document renderer.
6. Complete clean-install, leakage, provenance, and human semantic review.

## Migration rule

A private artefact reaches this repository only after it is classified as one of:

- **clean-room authored** — rebuilt from the proven procedure without private content;
- **sanitized from local source** — mechanically scrubbed and semantically reviewed;
- **upstream-derived** — licence, exact provenance, changes, and authority review recorded.

Copying a private runtime file and replacing a name is not sufficient sanitation.
