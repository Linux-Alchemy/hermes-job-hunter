# Hermes Job Hunter

A reusable Hermes specialist profile for evidence-bounded job discovery, fit analysis, and application drafting.

> **Status:** installable pre-release. The repository is a native Hermes profile distribution with a validated core foundation and a collaborative cover-letter drafting skill. Job discovery, matching, evidence-bank, résumé drafting, and deterministic document-rendering capabilities are still being integrated.

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
distribution.yaml
    declares the installable Hermes profile and owned paths
            ↓
SOUL.md
    defines mission, authority, and non-goals
            ↓
skills/job-hunter-core/SKILL.md
    enforces evidence, source, status, and approval rules
            ↓
skills/cover-letter-drafting/SKILL.md
    develops one evidence-bounded letter in a shared human-review workspace
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
├── distribution.yaml
├── SOUL.md
├── config.yaml
├── README.md
├── LICENSE
├── PROJECT_STATUS.md
├── PROVENANCE.md
├── skills/
│   ├── job-hunter-core/
│   │   └── SKILL.md
│   └── cover-letter-drafting/
│       ├── SKILL.md
│       ├── templates/
│       │   └── cover_letter_workspace.md
│       └── references/
│           └── proven_workflow_pattern.md
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

Install the current pre-release distribution directly from GitHub:

```bash
hermes profile install github.com/Linux-Alchemy/hermes-job-hunter --alias
```

For local development or inspection:

```bash
hermes profile install . --name hermes-job-hunter-test
```

This installs the profile contract, safe default configuration, core evidence policy, and collaborative cover-letter drafting workflow. It does not install private career evidence, credentials, account state, application history, rendering tools, or writing samples. Treat the current release as a review-gated foundation rather than a complete career agent.

## Licence

Hermes Job Hunter is released under the [MIT License](LICENSE).

Third-party-derived skills will not be added until their licences and provenance can be represented correctly.
