# Job Discovery Skill Research

**Audit date:** 2026-08-24 16:19 EDT  
**Status:** decision-ready; no third-party skill installed, copied, or executed  
**Recommendation:** build a clean-room `job-discovery` skill from the existing private review draft and proven package contracts. Create a separate, smaller `job-source-discovery` skill for regional/job-board onboarding and periodic source review.

## Decision in one paragraph

No inspected skill is a safe, close-enough base to patch wholesale. The strongest candidates either assume a different state model, hard-code one source, bring browser or scraper machinery, require paid APIs, mutate trackers/preferences, or widen into application automation. The existing private review draft already contains the procedure we need: bounded registry-driven search, normalization, deduplication, employer-original verification, evidence comparison, explicit uncertainty, and no external action. It should be generalized into the repository's first runtime skill. The portable ideas from external projects should be captured as attributed micro-procedures, not imported as their operating systems.

## Skill boundary

### `job-discovery` — frequent runtime procedure

Owns:

- loading the approved source registry, matching profile, and evidence bank;
- selecting only explicitly enabled sources;
- running bounded queries by execution lane;
- collecting lightweight listing metadata before expensive description retrieval;
- normalizing and deduplicating candidates;
- checking jurisdiction, genuine-remote status, freshness, and hard gates;
- verifying shortlisted roles at the employer-original posting;
- comparing requirements with evidence;
- producing a short review-ready slate with source-level status.

Does not:

- search for new job boards;
- install or generate connectors;
- enable sources;
- change source authority or setup state;
- create accounts, subscriptions, API keys, alerts, or browser sessions;
- apply, upload, message, or mutate public state.

If no usable registry exists, it returns `SETUP_REQUIRED` and directs the owner to the source-discovery procedure.

### `job-source-discovery` — infrequent onboarding and maintenance procedure

Owns:

- collecting target jurisdiction, languages, remote/on-site requirements, role families, industries, and acceptable setup cost;
- discovering plausible regional, national, remote-first, niche, aggregator, and direct-employer sources;
- identifying public APIs, RSS/Atom feeds, ATS endpoints, indexed public pages, and blocked/authenticated paths;
- testing a very small public-access sample;
- recording access, coverage, noise, authority, cost, and failure modes;
- proposing changes to the human decision record and machine registry;
- requiring human approval before any source is enabled or any connector work begins.

Does not:

- run during an ordinary job scan;
- silently add whatever board appears in search results;
- generate or install scraping code automatically;
- proceed through login walls or access restrictions;
- treat a country-specific list as universal.

### Why these are separate

Board discovery varies materially by jurisdiction, language, role family, remote eligibility, and willingness to configure accounts or paid APIs. It is setup and maintenance work with configuration-write implications. Runtime job discovery should be deterministic and consume an approved registry. Combining both would let an ordinary search quietly expand its own data sources and authority—the agent equivalent of a contractor ordering new machinery because the drill bit looked a bit tired.

## Requirements for the runtime skill

The implementation should inherit `job-hunter-core` and require:

1. a supported registry schema and recorded registry version;
2. explicit per-source enablement;
3. a run contract containing jurisdiction, remote constraints, freshness, role families, source set, and result cap;
4. cheap discovery before full-description hydration;
5. normalized candidate fields with `UNKNOWN` preserved;
6. source results of `COMPLETE`, `DEGRADED`, `BLOCKED`, `NOT_EVALUATED`, or `STALE`;
7. employer-original liveness and eligibility verification before `APPLY` or `APPLY_WITH_TAILORING`;
8. requirement labels of `met`, `partial`, `missing`, or `unknown`;
9. one triage outcome per serious candidate;
10. a short source/query/access record and explicit statement that external actions were `none`.

## Candidate audit

This was static inspection only. No donor script, package, MCP server, browser extension, dependency, or skill was installed or run.

### 1. Existing private job-board scout draft

**Disposition:** `USE AS CLEAN-ROOM BASE`

Distinctive value already present:

- source-lane ordering;
- bounded multi-query search;
- explicit untrusted-content boundary;
- normalized posting contract;
- employer-original verification;
- jurisdiction and genuine-remote checks;
- evidence-based fit grammar;
- honest empty/degraded results;
- hard stop conditions;
- realistic acceptance cases.

Required changes:

- remove private identities, paths, role terms, target jurisdiction, and source list;
- replace the Markdown board directory with the repository's YAML registry contract;
- load `job-hunter-core` rather than the private core skill;
- separate source discovery and connector work from runtime searching;
- move matching-profile and evidence-bank fields into versioned schemas;
- replace personal output paths with a configured workspace;
- add synthetic fixtures before installation.

This is not a third-party import. It is the most direct proof that the intended procedure already has a coherent shape.

### 2. MadsLorentzen/ai-job-search

- Repository: <https://github.com/MadsLorentzen/ai-job-search>
- Audited HEAD: `e2c311a5b40512daf79a04b22c96d7e049afc745`
- Licence: MIT
- Examined:
  - `.claude/commands/add-portal.md`
  - `.agents/skills/linkedin-search/SKILL.md`
  - `.agents/skills/freehire-search/SKILL.md`

**Disposition:** `CAPTURE MICRO-PROCEDURES; DO NOT PATCH WHOLESALE`

Useful procedures:

- country-agnostic connector contract with market-specific implementations;
- investigate real endpoint/field shapes before scaffolding;
- stable `search` and `detail` interface;
- normalized JSON with null rather than silently omitted fields;
- stderr plus non-zero exit for connector failure;
- bounded results, pagination, backoff, and honest User-Agent;
- lightweight discovery without descriptions, followed by targeted hydration;
- location supplied per user/market rather than embedded in the skill;
- unresolved geography treated as unknown;
- source-specific notes and live smoke tests.

Why it is not our base:

- `/add-portal` creates TypeScript/Bun connector code and installs dev dependencies;
- the command can continue after terms/robots restrictions under a personal-use warning, whereas this package should default to exclusion or explicit unresolved review;
- LinkedIn guest-endpoint automation carries stated Terms-of-Service conflict;
- the portal skills assume executable Bash authority and auto-discovery from a fork-specific directory;
- freehire is tech-focused and depends on one best-effort hosted aggregator;
- this solves connector construction, not broad board discovery for a new user's market.

The connector contract is useful later. Automatic connector generation is not part of V1.

### 3. proficientlyjobs/proficiently-claude-skills — `job-search`

- Repository: <https://github.com/proficientlyjobs/proficiently-claude-skills>
- Audited HEAD: `9bc1f6fd7af532fe0cd4a1843e06ab2b474d0d53`
- Examined: `skills/job-search/SKILL.md`
- Licence note: the skill README claims MIT, but the audited repository root returned no `LICENSE` file. Do not copy text until licence representation is clarified.

**Disposition:** `REJECT AS BASE; CAPTURE TWO SMALL IDEAS`

Useful:

- load preferences and prior history before querying;
- extract listing rows rather than flooding context with the entire page;
- resolve high-value aggregator results to employer-original URLs;
- keep tailoring and application actions in separate skills.

Conflicts:

- hard-coded to hiring.cafe;
- requires Claude-in-Chrome browser automation;
- writes job history and updates preferences during the workflow;
- requests broad browser, file-write, and crontab authority;
- assumes a competing data directory and state model;
- promotes a connected application/fill workflow outside this package's authority;
- includes mandatory service promotion in user-facing output.

### 4. Job Search MCP / JobSpy

- Skill page: <https://hub.openclaw.ai/amoghpurohit/job-search-mcp>
- Version shown: `v1.0.0`
- Licence shown: MIT-0

**Disposition:** `OPTIONAL CONNECTOR CANDIDATE ONLY`

Useful:

- one normalized interface across several large boards;
- explicit platform-specific filter conflicts;
- supported-country/site discovery calls;
- bounded result guidance and pagination;
- rate-limit and error classifications.

Conflicts:

- requires installing an MCP server plus Python/Node dependencies;
- wraps scraper behaviour rather than discovering which boards suit a user;
- includes Easy Apply fields irrelevant to read-only discovery;
- suggests proxy configuration as a response to rate limiting, which conflicts with the no-bypass posture;
- source reliability claims would need independent live testing;
- board coverage is fixed by JobSpy and is not a substitute for regional source discovery.

If adopted later, JobSpy should be one disabled registry connector with a separate installation and authority decision—not the owning job-discovery skill.

### 5. zdeag/theirstack-search-skill

- Repository: <https://github.com/zdeag/theirstack-search-skill>
- Audited HEAD: `9f62fe9f2bbabf94315dfad22cc772da74af0b0f`
- Licence: MIT

**Disposition:** `OPTIONAL CONNECTOR CANDIDATE; CAPTURE COST CONTROLS`

Useful:

- structured natural-language-to-filter translation;
- small default limits and a cheaper quick mode;
- caching and explicit API-credit reporting;
- read-only search and company lookup;
- clear environment-variable credential guidance.

Conflicts:

- paid/keyed third-party API dependency;
- Bun executable and local cache state;
- one aggregator rather than board discovery;
- broad global data claims require supplier trust and current verification;
- not required for a useful no-account core profile.

### 6. santifer/career-ops — portal scanner

- Repository: <https://github.com/santifer/career-ops>
- Audited HEAD: `b15a96338d4f7c492a54a63a02d2250b9742ede6`
- Licence: MIT; project name/brand has a separate trademark policy
- Examined:
  - `modes/scan.md`
  - `docs/SUPPORTED_JOB_BOARDS.md`

**Disposition:** `CAPTURE MICRO-PROCEDURES; REJECT FRAMEWORK IMPORT`

Useful:

- cheap structured source before browser before broad search;
- direct-employer ATS APIs as high-value source families;
- source/provider modules with a common normalization contract;
- per-source health and scan history;
- do not repeat an expensive route when a cheaper source succeeded;
- indexed results are stale leads requiring liveness verification;
- pagination/truncation warnings;
- missing dates and locations remain unknown rather than automatic rejection;
- exact-URL, company/title, and near-duplicate-description checks.

Conflicts:

- very large framework with dozens of providers and extensive JavaScript/Go machinery;
- local parser execution, Playwright, WebSearch, mutable pipeline/history, and broad state authority;
- source additions and fixes are tied to its own `portals.yml`, provider loader, and data contract;
- numeric scoring and automatic pipeline writes conflict with this package's review grammar;
- importing it would replace the package we are building rather than supply one skill.

Its provider catalogue is valuable research evidence for future source discovery, not a subtree to copy.

### 7. ClawHub `JobClaw`

**Disposition:** `REJECT AS BASE`

The inspected skill preview combines conversational onboarding, Python search scripts, daily automation, configuration writes, CSV tracking, scoring, status mutation, and scheduled operation. Its hard-coded platform/search model and competing state directory make sanitation more expensive than clean-room authorship. It may contain useful keyword examples, but nothing distinctive enough to justify importing the package.

## Build recommendation

### Build, do not patch

Implement `skills/job-discovery/SKILL.md` as a clean-room public version of the existing private review draft, subordinate to `job-hunter-core` and driven by `job_source_registry.local.yaml`.

Capture these external micro-procedures with attribution:

- MadsLorentzen: portal contract, real-endpoint investigation, null-preserving output, cheap metadata pass, targeted hydration, connector smoke tests;
- Proficiently: compact listing extraction and employer-original URL resolution;
- JobSpy skill: platform-specific filter constraints and bounded result advice;
- TheirStack skill: cost/credit-aware limits and cache transparency;
- career-ops: cheap-to-expensive source ordering, source health, truncation warnings, liveness verification, and layered deduplication.

Remove:

- browser/session assumptions;
- automatic source or preference mutation;
- connector installation and package-manager commands;
- cron and background scheduling;
- auto-apply, Easy Apply, upload, messaging, or pipeline mutation;
- donor directories, trackers, scores, and state models;
- location, language, source list, and role-family assumptions belonging to one user.

## Proposed repository shape

```text
skills/
├── job-hunter-core/
│   └── SKILL.md
├── job-source-discovery/
│   ├── SKILL.md
│   └── references/
│       └── source_assessment_contract.md
└── job-discovery/
    ├── SKILL.md
    └── references/
        ├── normalized_posting_contract.md
        └── search_run_contract.md

templates/
├── matching_profile.example.yaml
├── evidence_bank.example.yaml
├── job_source_registry.example.yaml
└── job_search_run.example.md

tests/fixtures/job_discovery/
├── normal.json
├── degraded_source.json
├── blocked_source.json
├── stale_index_hit.json
├── remote_location_trap.json
├── duplicate_conflict.json
└── instruction_injection.json
```

The source-discovery skill should be small. The actual runtime procedure belongs in job-discovery. Connectors remain optional implementation modules under a later, separately reviewed contract.

## Resume point

When work resumes:

1. author `job-discovery` from the private review draft and this decision record;
2. replace all personal assumptions with matching-profile and registry fields;
3. add the normalized posting and run contracts;
4. create synthetic acceptance fixtures;
5. validate the skill in the repository before installing it into any live profile;
6. then author the smaller `job-source-discovery` onboarding/maintenance skill.
