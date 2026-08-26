---
name: resume-drafting
description: "Use when creating or revising a general or application-specific résumé Markdown source. Requires evidence, input-manifest, draft-brief, and human-approval gates; owns truthful selection and wording but not rendering, submission, or external profile mutation."
version: 0.1.0
author: Linux-Alchemy
license: MIT
metadata:
  hermes:
    tags: [career, resume, drafting, applications, evidence]
    related_skills: [job-hunter-core, application-packet, cv-audit, career-document-rendering]
---

# Résumé Drafting

## Overview

Produce one evidence-bounded Markdown résumé source for human review. This skill owns **selection and wording**. Rendering belongs to `career-document-rendering` after the human approves the exact Markdown source.

Load `job-hunter-core` first. Use the matching profile, evidence bank, application packet, and CV-audit procedure rather than guessing from memory. If the adopter has a user-owned voice calibration, apply it conservatively after factual and structural review.

## When to use

Use for:

- a new general résumé source;
- a résumé tailored to one approved opportunity;
- a bounded revision to an existing résumé Markdown source.

Do not use for DOCX/PDF generation, public-profile mutation, application submission, employer contact, or unapproved claims.

## Required sources

### General résumé

Before drafting, require:

1. approved or review-ready career matching profile;
2. career evidence bank;
3. relevant project/employment/education source evidence;
4. current positioning decision;
5. any existing general résumé source that must be preserved or replaced.

A first general résumé may be drafted without an existing approved résumé because creating that base is the task. Missing evidence does not become permission to invent it.

### Application-specific résumé

Do not draft until the private application packet contains:

1. employer-original posting;
2. company profile, or an explicit decision to proceed without one;
3. current general résumé with lifecycle `APPROVED_MARKDOWN`;
4. input manifest recording source paths and versions or SHA-256 hashes;
5. human-approved draft brief.

The general résumé is the content base. The posting controls emphasis and terminology, not truth. Employer intelligence controls context and risk, not candidate claims. Use the evidence bank only to support additions or resolve uncertainty.

If the approved general résumé does not exist, report `BLOCKED` with the human decision owner. Do not substitute an old master, public-profile scrape, or earlier tailored résumé.

## Private workspace layout

General résumé work:

```text
workspace/resumes/general/
├── source/
├── reference/
└── outputs/
```

Application-specific work stays in the application packet:

```text
workspace/applications/<employer_slug>/<role_slug>/
├── application_status.md
├── input_manifest.yaml
├── source/
│   ├── job_posting.md
│   ├── company_profile.md
│   ├── general_resume_snapshot.md
│   ├── draft_brief.md
│   ├── build_decisions.md
│   └── resume_source.md
└── outputs/
```

Use snake_case. Do not scatter active application files through unrelated notes. Public repository examples remain synthetic and must never receive private résumé content.

## Draft-brief gate

Prepare `source/draft_brief.md` from `templates/draft_brief.md` before an application-specific résumé. Keep it short and decision-shaped:

- target role and employer;
- three or fewer messages the résumé should communicate;
- requirements classified `met / partial / missing / unknown`;
- experiences and projects to lead with;
- material to retain, compress, omit, or verify;
- proposed summary stance;
- unresolved claims or eligibility gates;
- exact source files and versions/hashes used.

Set it to `HUMAN_REVIEW`. The human must explicitly approve or amend it. Do not infer approval from silence, praise, or a request to inspect the materials.

If target, emphasis, or evidence changes after approval, update and reapprove the brief before drafting. Polishing the wrong frame is sanding a door before checking whether it fits the opening.

## Draft procedure

1. **Create or reconcile the workspace.** Read existing files first. Preserve approved text and user notes.
2. **Snapshot the approved base.** For application work, copy the approved general résumé into the packet and record source path plus hash in `input_manifest.yaml`.
3. **Prepare the draft brief.** Stop at `HUMAN_REVIEW` until explicitly approved.
4. **Select evidence.** Start from the general résumé. Add evidence-bank material only when it strengthens a real requirement and is defensible at the stated depth.
5. **Record build decisions.** Use `templates/build_decisions.md` with `retain`, `rephrase`, `compress`, `omit`, and `verify`. Name the reason and evidence reference without writing an essay.
6. **Draft Markdown.** Preserve approved content where it works. Use exact, plain wording. Do not invent numbers to make bullets look busy.
7. **Run factual and structural review.** Apply `job-hunter-core` and `cv-audit`; resolve contradictions, unsupported claims, parser hazards, and placeholders.
8. **Run voice review.** Remove generic résumé paste and unsupported self-praise. Preserve professional clarity over imitation.
9. **Present one draft.** Set lifecycle to `HUMAN_REVIEW`, report the exact path, and provide a concise change summary.
10. **Apply consolidated feedback.** Do not repeatedly “improve” approved wording between review rounds.
11. **Record approval.** Only explicit human instruction may promote the exact source to `APPROVED_MARKDOWN`.

## Evidence and authorship rules

- Use `VERIFIED`, `USER_REPORTED`, `PROPOSED`, `VERIFY_BEFORE_USE`, and `UNKNOWN` consistently.
- Separate duties performed from business outcomes caused.
- Distinguish coursework, guided projects, AI assistance, independent implementation, orchestration, and verification.
- A repository proves observed behaviour, not unaided authorship.
- Metrics require a source and scope. If a number is uncertain, omit it or keep it in review notes.
- Transferable evidence may bridge duties when labelled honestly; it must not impersonate direct industry tenure.
- Do not convert familiarity into expertise or a course into professional experience.

## Content selection

Prefer evidence that:

1. directly supports required duties;
2. demonstrates transferable patterns with clear attribution;
3. shows recent, inspectable work;
4. can be explained in an interview;
5. survives source review without qualification theatre.

Compress or omit material that is stale, repetitive, weakly related, impossible to defend, or included only for keyword density.

Keyword alignment is subordinate to truth and readability. Use employer terminology only when it accurately names supported work.

## Source frontmatter

Every résumé source uses:

```yaml
---
title: "<document title>"
document_type: resume
resume_scope: general | application_specific
employer: null              # application-specific only
role: null                  # application-specific only
lifecycle_state: DRAFT | HUMAN_REVIEW | APPROVED_MARKDOWN
approved_by: null
approved_at: null           # YYYY-MM-DD after approval
base_resume_path: null      # application-specific only
base_resume_sha256: null
---
```

The agent may set `DRAFT` and `HUMAN_REVIEW`. It must not populate approval fields or `APPROVED_MARKDOWN` without explicit approval for the exact source.

## Handoff to rendering

Rendering requires:

- exact source path;
- `lifecycle_state: APPROVED_MARKDOWN`;
- approval owner and date;
- permitted output types;
- output stem;
- declared layout policy;
- whether layout-only revision is allowed.

A renderer may adjust spacing and style within the approved layout policy. It may not rewrite substantive content. Any content change returns to `HUMAN_REVIEW`.

## Stop conditions

Stop and ask one precise question when:

- a required application source is missing;
- the general résumé is not approved;
- the draft brief has not been approved;
- sources conflict on a material fact;
- a desired bullet needs an unsupported metric, credential, tenure, or ownership claim;
- requested emphasis would obscure a known hard gate;
- the output would require guessing legal, demographic, location, or eligibility information.

A blocked gate is cheaper than a polished wrong answer.

## Common pitfalls

1. **Tailoring from the posting alone.** Start from approved candidate evidence.
2. **Old résumé treated as canonical.** Verify lifecycle state and hash.
3. **Keywords over truth.** Alignment does not permit inflated depth.
4. **Activity written as outcome.** Do not invent impact.
5. **AI assistance erased.** Preserve ownership boundaries where material.
6. **Drafting and rendering mixed.** Keep Markdown approval separate.
7. **Approval inferred.** Only explicit approval promotes the exact source.
8. **Endless polish.** Apply consolidated feedback and stop changing approved prose.

## Verification checklist

- [ ] `job-hunter-core` was followed.
- [ ] Correct matching profile, evidence bank, and source evidence were used.
- [ ] Application work used the correct packet and approved general résumé snapshot.
- [ ] Input manifest records paths and versions/hashes.
- [ ] Draft brief was explicitly approved.
- [ ] Posting and employer profile informed emphasis without creating candidate facts.
- [ ] Material changes appear in `build_decisions.md`.
- [ ] Metrics, credentials, tenure, ownership, and outcomes have evidence.
- [ ] No unresolved placeholders or contradictions remain.
- [ ] CV structural/parser review was performed.
- [ ] Source state is `HUMAN_REVIEW`, not rendered or externally ready.
- [ ] Exact path, change summary, unresolved items, and next decision owner were reported.
