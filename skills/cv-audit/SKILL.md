---
name: cv-audit
description: "Use when auditing a résumé or CV for factual support, employer relevance, parser safety, structure, language, consistency, and rendered readability. Uses bounded inspection, separates candidate evidence from job requirements, and returns prioritised corrections without silently rewriting or publishing the document."
version: 0.1.0
author: Linux-Alchemy
license: MIT
metadata:
  hermes:
    tags: [career, resume, cv, audit, ats, evidence]
    related_skills: [job-hunter-core, resume-drafting, career-document-rendering, github-portfolio-audit, linkedin-audit]
---

# CV Audit

## Overview

Audit a résumé or CV as an evidence and communication artefact. Check whether every material claim is supported, the document is relevant to its intended role, parsers can recover its content, and a human can understand it quickly.

Load `job-hunter-core` first. An employer's wording may guide emphasis but cannot prove candidate capability. Recommendations belong to `resume-drafting`; deterministic rendering and visual QA belong to `career-document-rendering`.

Supporting files:

- [Audit-report template](templates/audit_report.md)
- [Provenance](references/provenance.md)

## When to use

Use when the user asks to:

- review a general or tailored résumé/CV;
- check ATS/parser safety;
- compare a résumé against a posting or evidence bank;
- identify unsupported, vague, stale, contradictory, or weak claims;
- assess structure, bullets, keywords, readability, or rendering;
- prioritise revisions before approval or external use.

Do not use to invent metrics, rewrite approved content silently, render documents, mutate public profiles, upload files, or submit applications.

## Audit depth

State the depth:

- **Quick:** factual red flags, top structure/parser problems, and three highest-value corrections.
- **Default:** full source audit plus parser/render checks available from supplied files.
- **Deep:** source, rendered artefacts, evidence bank, target posting, portfolio/LinkedIn consistency, and claim-by-claim ledger.

Do not score or criticise categories that were not inspected. State the limits.

## Source order

Use the cheapest reliable source for each question:

1. editable Markdown or document source for wording and structure;
2. approved evidence bank and source records for factual support;
3. employer-original posting for role requirements and terminology;
4. DOCX/PDF extraction for parser order and content survival;
5. page images for visual layout;
6. portfolio or LinkedIn only when consistency review is requested and access is authorised.

A PDF screenshot cannot establish source structure. An editable source cannot prove the rendered result. Keep those questions separate.

## Authority contract

### Allowed

- read user-supplied or explicitly approved local source and rendered documents;
- read approved evidence, posting, and related public portfolio material;
- extract text through available read-only document tools;
- inspect supplied or generated page images;
- write an advisory report to a configured private workspace when authorised.

### Forbidden

- inventing or strengthening claims without evidence;
- editing the résumé unless the user invokes a drafting/revision workflow;
- rendering through ad-hoc tools;
- uploading, applying, emailing, messaging, or changing public profiles;
- assuming inaccessible ATS, recruiter, or analytics outcomes;
- treating a generic ATS score as a hiring forecast.

## Workflow

### 1. Establish the contract

Record:

- document path, format, scope, and lifecycle state;
- target role or general positioning;
- audit depth;
- controlling evidence and posting sources;
- available source, DOCX, PDF, and page images;
- whether revisions are advisory or separately authorised;
- external actions: none.

If the document claims approval but approval metadata or source version is unclear, report that before content review.

### 2. Check factual integrity

For every material claim, inspect:

- role, organisation, education, credential, project, and date;
- metric and scope;
- responsibility versus outcome;
- experience depth and seniority;
- authorship, course/template, AI assistance, and verification boundaries;
- whether a source is `VERIFIED`, `USER_REPORTED`, `VERIFY_BEFORE_USE`, `PROPOSED`, or `UNKNOWN`.

Classify findings:

- `SUPPORTED`;
- `PARTIAL`;
- `UNSUPPORTED`;
- `CONFLICT`;
- `UNKNOWN`.

Do not repair an unsupported claim by making it vaguer. Either source it, narrow it truthfully, move it to review, or omit it.

### 3. Check role alignment

Separate:

- candidate evidence;
- employer requirements;
- terminology overlap;
- transferable evidence;
- actual gaps.

Use `met / partial / missing / unknown`. Distinguish hard gates, flexible stretch requirements, and preferences. Keyword presence never overrides a failed gate or missing capability.

### 4. Check structure and scanability

Evaluate:

- clear identity/contact block in the private copy;
- summary stance;
- section order;
- role/project headings and dates;
- consistent chronology;
- bullet density and length;
- duplication;
- whether the strongest relevant evidence appears early;
- whether the document tells one coherent professional story.

Apply the ten-second test: can a reviewer identify the candidate's direction, strongest proof, and relevant experience quickly?

### 5. Check bullet quality

A strong bullet usually identifies:

- action or responsibility;
- object/problem/context;
- method or technical detail when useful;
- result only when supported.

Flag:

- unsupported outcomes;
- adjective-heavy self-praise;
- duties inflated into ownership;
- vague “helped with” language hiding real contribution;
- tool lists without applied context;
- repeated sentence patterns;
- numbers added merely to decorate the line.

Approximate metrics require a defensible basis, explicit approximation, and human approval. Otherwise mark them for verification or omit them.

### 6. Check parser safety

Using source and extracted text where available, verify:

- single-column reading order;
- standard headings;
- no essential information trapped in headers, footers, tables, images, text boxes, or drawings;
- dates and headings survive extraction;
- bullets remain associated with the correct entries;
- URLs/contact fields remain readable;
- no placeholder or unresolved evidence labels remain;
- DOCX and PDF text agree with the approved source.

Prefer wording and source-structure corrections over brittle layout hacks.

### 7. Check rendered readability

When page images are available, inspect every page for:

- clipping and overlap;
- tiny or inconsistent text;
- awkward page breaks;
- detached headings;
- excessive density or dead space;
- weak hierarchy;
- inconsistent alignment or spacing.

Mechanical QA is not visual QA. If rendered pages were not inspected, say so.

### 8. Check consistency

When requested, compare inspected résumé claims with approved evidence, portfolio, and LinkedIn inputs. Report:

- direct conflicts;
- stale differences;
- unsupported cross-platform claims;
- missing but defensible proof;
- differences that are harmless because the surfaces have different purposes.

Use “no conflict found in inspected inputs,” not “fully consistent,” unless every controlling source was reviewed.

### 9. Prioritise corrections

Rank by:

1. false, unsupported, conflicting, or legally consequential claims;
2. parser/content loss;
3. failed hard gate or misleading fit;
4. unclear positioning or hidden strongest evidence;
5. weak bullets and excessive density;
6. minor wording and cosmetics.

For each correction, provide the exact section/line, problem, evidence basis, smallest useful change, and owner.

## Optional scoring

Do not invent a precise universal ATS score. If the user requests structured scoring:

- define categories and weights before scoring;
- score only inspected categories;
- rescale weights when a category was unavailable;
- show unearned weighted points as prioritisation, not hiring probability;
- keep unsupported-claim blockers outside the numeric score because they are not cosmetic deductions.

## Output contract

Use `templates/audit_report.md`. Include:

1. decision brief;
2. scope and unavailable checks;
3. factual-integrity findings;
4. requirement alignment;
5. parser and render findings;
6. consistency findings;
7. prioritised correction queue;
8. retained strengths;
9. source ledger, actions, and next owner.

## Common pitfalls

1. **Posting language proves skill.** It does not.
2. **PDF looks fine, so parser is fine.** Extract the text.
3. **Editable source is fine, so render is fine.** Inspect the output.
4. **Every bullet needs a number.** Unsupported metrics reduce credibility.
5. **Generic ATS score treated as destiny.** Use evidence and actual requirements.
6. **Layout hack used to solve wording.** Fix the owning source.
7. **Audit silently becomes rewrite.** Keep advisory and drafting authority separate.
8. **Partial inspection called exhaustive.** State what was not checked.

## Verification checklist

- [ ] `job-hunter-core` was followed.
- [ ] Scope, depth, inputs, and unavailable checks are explicit.
- [ ] Candidate evidence and employer requirements remain separate.
- [ ] Material claims have support states.
- [ ] Metrics, outcomes, ownership, credentials, and tenure were checked.
- [ ] Hard gates, stretch requirements, and preferences are distinct.
- [ ] Parser safety used extracted text where available.
- [ ] Every rendered page was inspected when visual claims are made.
- [ ] Consistency conclusions are bounded to inspected sources.
- [ ] Corrections are prioritised and cite exact locations/evidence.
- [ ] No silent rewrite, render, upload, profile mutation, or application action occurred.
