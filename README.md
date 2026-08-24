# Hermes Job Hunter

A reusable Hermes specialist profile for evidence-bounded job discovery, fit analysis, and application drafting.

> **Status:** private active build. The package now has a coherent, validated foundation, but it is not yet ready for general installation. Job discovery, matching, evidence-bank, and document-rendering capabilities are still being integrated.

## What it is

Hermes Job Hunter is a specialist agent package, not an auto-apply bot. It is designed to:

- discover plausible roles through explicitly configured sources;
- preserve degraded, blocked, stale, and unknown source states;
- compare postings against verified career evidence;
- distinguish hard gates, stretch requirements, and employer preferences;
- draft application material for human review;
- refuse unsupported claims and external application actions.

The human owns career facts, consequential decisions, public wording, applications, messages, and commitments.

## How the package fits together

```text
profile/SOUL.md
    defines mission, authority, and non-goals
            ↓
skills/job-hunter-core/SKILL.md
    enforces evidence, source, status, and approval rules
            ↓
config/source_registry.local.yaml
    tells the discovery skill which sources may run and how
            ↓
job-discovery and fit skills (under construction)
    produce evidence-labelled, review-ready artefacts
            ↓
human review and external action
```

The repository ships an inert, Canada-oriented registry example because that is the proven source set available today. Every source starts disabled until the adopter tests it and records the result locally; adopters targeting another jurisdiction should replace the source set and `target_jurisdictions` rather than treating the example as universal.

## Repository map

```text
hermes-job-hunter/
├── README.md
├── PROJECT_STATUS.md
├── PROVENANCE.md
├── profile/
│   ├── SOUL.md
│   └── config.example.yaml
├── skills/
│   └── job-hunter-core/
│       └── SKILL.md
├── config/
│   ├── source_registry.example.yaml
│   └── source_access_decisions.example.md
├── docs/
│   ├── ARCHITECTURE.md
│   └── JOB_DISCOVERY_SKILL_RESEARCH.md
├── onboarding/
│   └── voice_calibration.md
├── tests/
│   └── acceptance_matrix.md
└── scripts/
    └── validate_package.py
```

[PROJECT_STATUS.md](PROJECT_STATUS.md) is the canonical view of what has actually reached this repository. Private runtime notes and live-profile evidence do not count as packaged merely because they exist elsewhere.

The design and source-state model are explained in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md). The job-discovery boundary and candidate audit are in [docs/JOB_DISCOVERY_SKILL_RESEARCH.md](docs/JOB_DISCOVERY_SKILL_RESEARCH.md). Artefact lineage and sanitation status are recorded in [PROVENANCE.md](PROVENANCE.md).

## Safety boundary

The core package does not:

- submit applications;
- click application controls;
- upload documents;
- message employers or recruiters;
- mutate LinkedIn, GitHub, or job-board accounts;
- create accounts, subscriptions, API keys, or saved searches;
- bypass login walls, CAPTCHAs, paywalls, or anti-automation controls;
- turn incomplete source access into a claim that the market was searched exhaustively.

Optional integrations must be configured separately and remain subordinate to the same authority contract.

## Validate the current package

The validator requires Python and PyYAML, both of which are already present in a normal Hermes installation:

```bash
python scripts/validate_package.py
```

It checks required files, YAML structure, skill frontmatter, relative links, symlinks, and common secret/PII leakage patterns.

## Installation

Installation instructions will be added after the discovery skill, matching profile, evidence bank, and synthetic acceptance case are complete. Until then, treat this repository as a versioned build rather than an installable release.

## Licence

A public licence has not been selected yet. Third-party-derived skills will not be added until their licences and provenance can be represented correctly.
