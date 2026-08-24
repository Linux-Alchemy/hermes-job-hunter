# Provenance

This repository is a clean-room public package extracted from a working private Hermes career-specialist profile.

The private profile is used as operational evidence. Private runtime files are not copied wholesale and renamed.

## Current artefacts

| Repository artefact | Classification | Source and treatment |
|---|---|---|
| `profile/SOUL.md` | Clean-room authored | Reconstructed from the proven mission, evidence contract, authority limits, and failure posture. Personal names, paths, integrations, and career facts were excluded. |
| `skills/job-hunter-core/SKILL.md` | Clean-room authored | Reconstructed from the live core procedure. User-specific source precedence, storage paths, messaging, cloud, Kanban, cron, and writing-skill names were replaced by generic contracts. |
| `config/source_registry.example.yaml` | Sanitized from local source | Generated from a locally tested twenty-five-source registry. Owner fields were generalized, local paths removed, access dates cleared, and every source disabled pending adopter verification. |
| `config/source_access_decisions.example.md` | Clean-room authored | Blank human decision-record template implementing the prose/YAML split. |
| `docs/ARCHITECTURE.md` | Clean-room authored | Condenses the proven runtime/package split, source state model, workflow, and authority boundary. |
| `onboarding/voice_calibration.md` | Clean-room authored | Generalizes a successful before/after calibration method without including private writing samples or personal voice rules. |
| `tests/acceptance_matrix.md` | Clean-room authored | Converts observed success and failure requirements into public acceptance cases. |
| `scripts/validate_package.py` | Clean-room authored | Local structural and leakage validator written for this repository. |

## Not included

- runtime profile state, sessions, memory, logs, caches, authentication, or messaging identifiers;
- private career strategy, evidence, résumé material, applications, or target employers;
- private voice samples, calibration rules, or acceptance conversations;
- donor-derived résumé, LinkedIn, or portfolio skills.

The donor-derived candidates remain excluded until licence, exact source lineage, sanitation changes, and semantic authority review can be represented correctly inside this repository.

## Publication rule

Before public release:

1. regenerate this record after the final artefact set is known;
2. record third-party licences and exact upstream commits where applicable;
3. run the automated validator and a separate secret/PII scan;
4. perform a human semantic review for private assumptions that automated patterns cannot detect;
5. obtain explicit repository-owner approval.
