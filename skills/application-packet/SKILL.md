---
name: application-packet
description: "Use when a plausible role becomes an active application. Creates and maintains one local, auditable packet containing preserved source evidence, fit analysis, approved drafting inputs, rendered outputs, QA records, and lifecycle state without submitting or contacting anyone."
version: 0.1.0
author: Linux-Alchemy
license: MIT
metadata:
  hermes:
    tags: [career, applications, dossiers, lifecycle, evidence]
    related_skills: [job-hunter-core, job-discovery, employer-intelligence, resume-drafting, cover-letter-drafting, career-document-rendering]
---

# Application Packet

## Overview

Create one private working packet for one employer/role combination. The packet keeps original evidence, advisory analysis, authored source documents, rendered files, QA records, and lifecycle decisions together without confusing folder placement with approval.

Load `job-hunter-core` first. This skill owns local packet structure and lifecycle bookkeeping. It does not decide whether claims are true, draft documents by itself, render unapproved sources, fill forms, contact anyone, or submit an application.

## When to use

Use when:

- a role survives initial discovery and the user wants active evaluation;
- employer research, fit analysis, résumé tailoring, or cover-letter work will produce several related artefacts;
- an existing application packet needs reconciliation or a clear current state;
- approved source documents and rendered outputs need a traceable handoff;
- the user wants an auditable record of what was considered, approved, rendered, or submitted.

Do not create packets for every weak listing. A packet is a workbench for a serious candidate, not a warehouse for search noise.

## Default private structure

```text
workspace/applications/<employer_slug>/<role_slug>/
├── application_status.md
├── input_manifest.yaml
├── source/
│   ├── job_posting.md
│   ├── company_profile.md
│   ├── fit_brief.md
│   ├── resume_source.md
│   └── cover_letter_source.md
└── outputs/
    ├── <approved documents>.docx
    ├── <approved documents>.pdf
    └── qa_manifest.json
```

The adopter may configure another private root. Use snake_case slugs and filenames. Do not store live applications under the public package checkout.

Source and advisory Markdown belong in `source/`. Rendered DOCX/PDF files and deterministic QA evidence belong in `outputs/`. Never put secrets, credentials, browser cookies, platform session data, or identity-document scans in the packet.

## Lifecycle model

Use exactly one packet state:

- `identified` — captured but not yet evaluated;
- `evaluating` — liveness, eligibility, fit, or employer diligence remains open;
- `approved_to_draft` — human approved preparation of application materials;
- `draft_review` — one or more source documents await wording approval;
- `approved_to_render` — named source documents are approved for deterministic rendering;
- `rendered_review` — outputs exist and await visual/content review;
- `approved_to_submit` — human explicitly approved the final packet for external use;
- `submitted` — user or separately authorised external workflow confirms submission;
- `withdrawn` — human ended the application;
- `closed` — employer closed/rejected the opportunity or the role expired.

State is not authority. `approved_to_draft` does not authorise rendering; `approved_to_render` does not authorise submission. Record the exact approval and scope beside every transition.

## Workflow

### 1. Confirm opportunity identity

Record:

- employer and role;
- employer-original posting URL;
- discovery source and capture date;
- current open/freshness state;
- work mode and jurisdiction eligibility;
- human decision owner;
- packet root and intended local writes;
- external actions: none.

Resolve ambiguous employer/role identities before creating a directory.

### 2. Create or inspect the packet

If the packet exists, read it before writing. Preserve user notes, prior approvals, and version history. Do not overwrite source documents or outputs merely because a new template exists.

For a new packet, instantiate:

- `templates/application_status.md`;
- `templates/input_manifest.yaml`;
- empty `source/` and `outputs/` directories as needed.

Use the configured private root. The public templates remain blank.

### 3. Preserve the posting

Capture the employer-original posting before tailoring. Record:

- title, employer, URL, discovery and capture dates;
- work mode, location, employment type, department, and seniority;
- jurisdiction eligibility separately from `remote`;
- required, preferred, and ambiguous requirements;
- compensation and closing date when observed;
- observed posting text or a faithful bounded capture;
- conflicts and `UNKNOWN` values.

Do not silently rewrite requirements. Disclose editorial cleanup separately.

### 4. Build the input manifest

`input_manifest.yaml` records the exact inputs used for analysis, drafting, and rendering:

- relative path;
- artefact type;
- evidence/lifecycle state;
- source or approval owner;
- observed version or content hash when available;
- last reviewed date;
- allowed use;
- known limitations.

A newer modified timestamp does not establish canonical authority. Missing files remain missing; do not reconstruct private evidence from memory.

### 5. Add advisory artefacts

Use related skills as appropriate:

- `job-discovery` for liveness, location, and first-pass triage;
- `employer-intelligence` for the company profile;
- evidence-bank and matching-profile contracts for `fit_brief.md`;
- `resume-drafting` for `resume_source.md`;
- `cover-letter-drafting` for `cover_letter_source.md`.

Each artefact retains its own state. `review_ready` is not `approved`.

### 6. Gate drafting and rendering

Before drafting, require explicit approval for the named material and target role. Before rendering, require explicit approval of the exact source path and wording.

Record:

- approver;
- approval date;
- exact source path/version;
- permitted output types;
- whether layout-only changes are allowed;
- whether external use is approved.

Layout compression must never alter substantive wording without returning to draft review.

### 7. Record rendered outputs

After deterministic rendering:

- store outputs under `outputs/`;
- record source hash, renderer/template version, page count, font/layout declarations, text-agreement result, and QA state;
- preserve failures rather than replacing them with plausible-looking files;
- set packet state to `rendered_review`, not `approved_to_submit`.

### 8. Reconcile lifecycle state

Update `application_status.md` only from observed evidence or explicit human instruction. Record each transition with old state, new state, date, evidence, and owner.

Submission requires external verification such as a confirmation page, email, or user report. A generated document or opened form is not submission.

## Moving existing artefacts

Move files only when the user authorises the destination and the tool can verify both sides. A move is complete only when the target exists and the old path no longer does. A copied duplicate is not a move.

Preserve links and update the manifest after any move. Cloud-sync status does not prove remote equality.

## Status reporting

Every packet update reports:

- packet path;
- current lifecycle state;
- files created, modified, or moved;
- evidence or approvals used;
- unresolved gates;
- external actions taken;
- next bounded action and owner.

Do not say “application complete” when only drafting or rendering is complete.

## Prohibited actions

Never:

- submit, withdraw, message, contact, upload, or fill forms without separately granted authority;
- create accounts or obtain credentials;
- infer legal, identity, work-authorisation, salary, demographic, consent, or eligibility answers;
- copy unrelated career records into a packet;
- overwrite approved source or output files silently;
- promote `UNKNOWN` into a convenient fact;
- treat folder location as approval;
- store private packet contents in the public repository.

## Common pitfalls

1. **Packet equals permission.** It is organisation, not authority.
2. **Aggregator text becomes canonical.** Preserve employer-original evidence.
3. **One state governs every file.** Packet and artefact states are separate.
4. **Draft approval becomes submission approval.** Keep each gate explicit.
5. **Output without provenance.** Record exact input and renderer versions.
6. **Duplicate called a move.** Verify source removal.
7. **Sync badge called cloud equality.** Verify the destination when it matters.
8. **Status optimism.** Use the narrowest state supported by evidence.

## Verification checklist

- [ ] `job-hunter-core` was followed.
- [ ] Employer/role identity and employer-original URL are explicit.
- [ ] Packet uses a configured private path and snake_case names.
- [ ] Posting capture preserves unknowns and conflicts.
- [ ] Input manifest names every material source and approval state.
- [ ] Advisory, approved source, rendered output, and QA artefacts are separated.
- [ ] Drafting, rendering, external use, and submission gates remain distinct.
- [ ] Every lifecycle transition cites evidence and owner.
- [ ] Moved files were verified at both source and destination.
- [ ] No credential, secret, session data, or identity document was stored.
- [ ] No external action occurred without separate authority and verification.
- [ ] Packet path, state, writes, unknowns, next action, and owner were reported.
