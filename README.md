# Hermes Job Hunter

A reusable Hermes specialist profile for evidence-bounded job discovery, fit analysis, and application drafting.

> **Status:** installable pre-release. The repository now includes core policy, career schemas, registry-driven discovery, source maintenance, employer intelligence, application packets, résumé and cover-letter drafting, and deterministic DOCX/PDF production. Audit procedures and full release acceptance are still being integrated.

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
application-packet + resume-drafting + career-document-rendering
    preserve approvals, produce controlled DOCX/PDF, and retain QA evidence
            ↓
config/source_registry.local.yaml
    tells the discovery skill which sources may run and how
            ↓
job-discovery
    consumes adopter-approved registry and matching evidence
    to produce a bounded, verified opportunity slate
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

It checks required files, YAML structure, skill frontmatter, relative links, symlinks, and common secret/PII leakage patterns. The packaged renderer also has an executable seven-case test suite under `plugins/career-document-production/tests/`.

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
