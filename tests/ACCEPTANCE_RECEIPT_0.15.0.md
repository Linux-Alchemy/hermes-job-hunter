# Acceptance receipt — 0.15.0

**Date:** 2026-08-26  
**Scope:** disposable-profile package and renderer acceptance  
**External actions:** none

## Package validation

`python scripts/validate_package.py` passed:

- required structure and bounded configuration;
- 25 unique source definitions, all disabled;
- 12 skills;
- one plugin and three registered tools;
- two JSON Schema/example pairs;
- 17 synthetic cases/contracts;
- relative links;
- semantic privacy and common secret/PII patterns;
- DOCX metadata/content hygiene;
- generated-file, binary, credential-file, and symlink controls;
- public Git author and committer identity across rewritten history.

## Renderer suite

The ten-test renderer suite passed. It covered:

- approved résumé rendering and revalidation;
- approved one-page cover-letter rendering;
- required-font failure;
- missing human approval;
- invalid approval date;
- output-symlink escape refusal;
- path containment;
- overwrite refusal;
- explicitly authorised layout revision;
- rollback when revised layout fails QA.

## Disposable-profile installation

The repository installed successfully as an isolated Hermes distribution.

Observed:

- distribution version `0.15.0`;
- author `Linux-Alchemy`;
- 12 local skills, all enabled;
- one enabled user plugin: `career-document-production` version `0.2.0`;
- one enabled plugin toolset: `resume_production`;
- browser, terminal, code execution, memory, delegation, cron, messaging, and computer-use toolsets disabled;
- no profile credentials configured.

The installer added its expected local `.hub` skill-registry metadata and normalized the installed distribution manifest with the profile alias, source, and installation time. Packaged skill files had no missing or changed entries in the comparison; the only extra skill files were installer-owned `.hub` metadata.

## Installed-plugin execution

The plugin loaded from the disposable profile and rendered the synthetic Candidate A application sources:

| Artefact | Result | Pages | Required PDF fonts | External-use state |
|---|---|---:|---|---|
| Résumé | passed | 1 | passed | false |
| Cover letter | passed | 1 | passed | false |

No upload, submission, employer communication, public-profile mutation, or external-use approval occurred.

## Cleanup

The disposable profile was deleted after acceptance. The normal profile inventory returned to its prior state.

## Scope boundary

Job discovery, employer research, audits, and credential decisions are procedural skills rather than deterministic executables. Their normal/degraded/blocked/stale/location/duplicate/injection/empty and refusal contracts are represented by synthetic fixtures and statically validated. This receipt does not claim a live market search or external-account test.
