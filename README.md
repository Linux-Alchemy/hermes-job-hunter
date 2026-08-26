# Hermes Job Hunter

A reusable Hermes specialist profile for evidence-bounded job discovery, fit analysis, and application drafting.

> **Status:** capability-parity, installable pre-release. Core policy, career schemas, discovery, source maintenance, employer intelligence, application packets, drafting, deterministic DOCX/PDF production, portfolio/profile audits, credential decisions, and synthetic acceptance fixtures are packaged. Disposable-profile and clean remote-clone acceptance passed; the published remote revision was verified against local `master`.

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
distribution.yaml + SOUL.md + job-hunter-core
    define the installed profile, evidence model, and authority
            ↓
local matching profile + evidence bank + job-source registry
    provide adopter-owned facts, constraints, and approved source state
            ↓
job-discovery + employer-intelligence
    produce a bounded, verified opportunity decision
            ↓
application-packet + drafting skills
    preserve sources, approvals, wording, and lifecycle state
            ↓
career-document-rendering + packaged plugin
    produce controlled DOCX/PDF artefacts and QA evidence
            ↓
human visual review, external-use approval, and any external action
```

The repository ships an inert source catalogue derived from a proven Canada-oriented source set, but it does **not** select Canada—or any jurisdiction—as the adopter's default. Every source starts disabled and `not_configured` until the adopter chooses a market, tests the route, and records the result locally. Adopters targeting another jurisdiction should keep only relevant sources rather than treating the catalogue as universal.

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
├── RELEASE_NOTES.md
├── schemas/
│   ├── career_matching_profile.schema.json
│   └── career_evidence_bank.schema.json
├── examples/
│   └── candidate/
│       ├── career_matching_profile.example.yaml
│       ├── career_evidence_bank.example.yaml
│       └── sources/
├── skills/
│   ├── job-hunter-core/
│   │   └── SKILL.md
│   ├── job-discovery/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── templates/
│   ├── source-registry-maintenance/
│   │   ├── SKILL.md
│   │   └── templates/
│   ├── employer-intelligence/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── templates/
│   ├── application-packet/
│   │   ├── SKILL.md
│   │   └── templates/
│   ├── resume-drafting/
│   │   ├── SKILL.md
│   │   └── templates/
│   ├── career-document-rendering/
│   │   └── SKILL.md
│   ├── github-portfolio-audit/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── templates/
│   ├── cv-audit/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── templates/
│   ├── linkedin-audit/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── templates/
│   ├── credential-roi/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── templates/
│   └── cover-letter-drafting/
│       ├── SKILL.md
│       ├── templates/
│       │   └── cover_letter_workspace.md
│       └── references/
│           └── proven_workflow_pattern.md
├── plugins/
│   └── career-document-production/
│       ├── plugin.yaml
│       ├── tools.py
│       ├── schemas.py
│       ├── scripts/
│       ├── templates/
│       └── tests/
├── config/
│   ├── job_source_registry.example.yaml
│   └── source_access_decisions.example.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── OPTIONAL_INTEGRATIONS.md
│   ├── RELEASE_OPERATIONS.md
│   └── JOB_DISCOVERY_SKILL_RESEARCH.md
├── onboarding/
│   └── voice_calibration.md
├── tests/
│   ├── acceptance_matrix.md
│   ├── ACCEPTANCE_RECEIPT_0.15.0.md
│   └── fixtures/
│       ├── job_discovery/
│       ├── application/
│       └── refusal_cases.yaml
└── scripts/
    └── validate_package.py
```

[PROJECT_STATUS.md](PROJECT_STATUS.md) is the canonical view of what has actually reached this repository. Private runtime notes and live-profile evidence do not count as packaged merely because they exist elsewhere.

The design and source-state model are explained in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md). The job-discovery boundary and candidate audit are in [docs/JOB_DISCOVERY_SKILL_RESEARCH.md](docs/JOB_DISCOVERY_SKILL_RESEARCH.md). Authenticated cloud, messaging, Kanban, and scheduling boundaries are in [docs/OPTIONAL_INTEGRATIONS.md](docs/OPTIONAL_INTEGRATIONS.md). Installation, update, rollback, history migration, and release verification are in [docs/RELEASE_OPERATIONS.md](docs/RELEASE_OPERATIONS.md). Artefact lineage and sanitation status are recorded in [PROVENANCE.md](PROVENANCE.md).

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

It checks required files, YAML structure, skill frontmatter, relative links, symlinks, and common secret/PII leakage patterns. The packaged renderer also has an executable ten-case test suite under `plugins/career-document-production/tests/`.

### Renderer prerequisites

The renderer is enabled in the installed profile but exposes tools only when its dependencies are available:

- LibreOffice Writer (`soffice`);
- Poppler tools (`pdfinfo`, `pdftotext`, `pdftoppm`);
- fontconfig (`fc-match`);
- Python package `python-docx==1.2.0`;
- `JetBrainsMono NF` or the canonical installed alias `JetBrainsMono Nerd Font`.

If the required font is absent, rendering stops and asks the human decision owner to choose an alternate. It never substitutes a font silently.

## Installation

Install the current pre-release distribution directly from GitHub:

```bash
hermes profile install github.com/Linux-Alchemy/hermes-job-hunter --alias
```

For local development or inspection:

```bash
hermes profile install . --name hermes-job-hunter-test
```

This installs the profile contract, safe default configuration, current skills, and the bounded career-document plugin. It does not install private career evidence, credentials, account state, application history, or writing samples. Rendering remains dependency-gated and every consequential external action remains human-owned.

## Licence

Hermes Job Hunter is released under the [MIT License](LICENSE).

Third-party-derived skills will not be added until their licences and provenance can be represented correctly.
