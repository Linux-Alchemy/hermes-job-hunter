# Project Status

**Package state:** live-profile capability parity established; release acceptance in progress
**Release state:** public, installable pre-release
**Canonical purpose of this file:** show what is actually present in the repository and what remains private or unfinished.

## Implemented in this repository

| Component | State | Notes |
|---|---|---|
| Repository shape | Complete | Native Hermes distribution manifest, root profile files, skills, configuration, onboarding, tests, and architecture have clear homes. |
| Clean profile installation | Working | The repository installs directly through `hermes profile install` into an isolated Hermes home. |
| Profile authority contract | Initial public version | Generic, review-gated, and free of private paths or identities. |
| SOUL capability wording reconciliation | Complete | The protected contract names the packaged drafting, rendering, employer, portfolio, CV, LinkedIn, and credential capabilities while retaining conservative external-action limits. |
| Core skill | Initial public version | Evidence labels, source precedence, authority, status, and refusal rules. |
| Career matching profile schema | Initial public version | Versioned hard gates, role families, query vocabulary, exclusions, unsupported claims, and stretch-policy contract with no adopter data. |
| Career evidence-bank schema | Initial public version | Versioned evidence units, verification states, ownership/assistance boundaries, metrics provenance, and limitations. |
| Synthetic candidate examples | Initial public version | Coherent fictional profile, evidence bank, and source records containing no real identity, contact, employer, or account data. |
| Synthetic acceptance fixtures | Complete for current workflows | One coherent fictional identity/employer covers discovery success/failure states, application sources and approvals, rendering inputs, and eight external-action refusals. |
| Employer-intelligence skill | Initial public version | Consolidated company research, acquisition context, review synthesis, metric-conflict handling, role implications, and interview questions into one read-only procedure. |
| GitHub portfolio audit | Initial public version | Bounded public/local inspection, repository-role assignment, comprehension tests, provenance/evaluability review, career consistency, and credibility-first cleanup without code execution or GitHub mutation. |
| CV audit | Initial public version | Evidence, requirement, parser, rendering, consistency, and prioritised-correction review with bounded depth and no silent rewriting. |
| LinkedIn audit | Initial public version | Consent-aware bounded review of structured fields, narrative, proof assets, activity, evidence, cross-surface consistency, and algorithm-claim confidence without authenticated access or mutation. |
| Credential ROI | Initial public version | Separates learning/signal/access/structure/confidence value, estimates bounded effort, maps overlap and recognition, audits outcome claims, compares the smallest competing brick, and returns one explicit decision state. |
| Optional integration policy | Complete for current scope | Google mail/calendar, authenticated GitHub, messaging, Kanban, and cron remain external and separately authorised; core workflows degrade without them. |
| Résumé-drafting skill | Initial public version | Separates general and application-specific drafting, requires a human-approved brief, records evidence/build decisions, preserves authorship boundaries, and hands only approved Markdown to rendering. |
| Career-document rendering skill and plugin | Working public version | Packages approval-gated DOCX/PDF rendering, 9–12 pt `JetBrainsMono NF` enforcement in DOCX and PDF, page/structure/text QA, preview generation, bounded rollback-safe layout revision, output-symlink refusal, and ten passing end-to-end tests. |
| Application-packet skill | Initial public version | Defines one-opportunity private dossier structure, evidence manifest, independent artefact states, approval gates, rendered-output provenance, and application lifecycle transitions. |
| Cover-letter drafting skill | Initial public version | Four-source authorship model, shared notes/draft workspace, evidence and voice checks, explicit human approval, and clean-source handoff. |
| Source-registry maintenance skill | Initial public version | Separates source evaluation from runtime search, preserves Markdown rationale plus YAML configuration, and requires explicit approval before local registry mutation. |
| Source-registry schema | Initial public version | Twenty-five source definitions retained as an inert catalogue; jurisdiction selection is blank and every source is disabled/not configured pending adopter verification. |
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

- update, rollback, and release instructions;
- a full-capability clean-profile end-to-end acceptance run;
- tagged-release notes and version metadata for the first stable release.

## Next build sequence

1. Add coherent synthetic posting, source-failure, application, and refusal fixtures.
2. Expand the validator across schemas, plugins, binaries, provenance, and semantic privacy terms.
3. Run full disposable-profile capability and refusal acceptance.
4. Add update, rollback, migration, and release instructions.
5. Repeat leakage, provenance, Git-history, and human semantic review before publication.

## Migration rule

A private artefact reaches this repository only after it is classified as one of:

- **clean-room authored** — rebuilt from the proven procedure without private content;
- **sanitized from local source** — mechanically scrubbed and semantically reviewed;
- **upstream-derived** — licence, exact provenance, changes, and authority review recorded.

Copying a private runtime file and replacing a name is not sufficient sanitation.
