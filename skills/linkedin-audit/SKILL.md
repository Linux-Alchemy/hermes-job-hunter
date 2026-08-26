---
name: linkedin-audit
description: "Use when auditing LinkedIn profile content from user-supplied exports, pasted sections, screenshots, or explicitly authorised public reads. Evaluates dual-audience structure, evidence support, consistency, positioning, proof assets, and bounded recent activity without logged-in browsing or profile mutation."
version: 0.1.0
author: Linux-Alchemy
license: MIT
metadata:
  hermes:
    tags: [career, linkedin, profile, audit, positioning]
    related_skills: [job-hunter-core, cv-audit, github-portfolio-audit]
---

# LinkedIn Audit

## Overview

Audit LinkedIn as a dual-audience career surface: structured fields and keywords help search/recruiter workflows, while clear prose, proof assets, and recent activity help humans understand and trust the candidate.

Load `job-hunter-core` first. The profile must remain evidence-bounded and consistent with approved career sources without becoming a résumé pasted into a different box.

Supporting files:

- [Audit-report template](templates/audit_report.md)
- [Provenance](references/provenance.md)

## When to use

Use when the user asks to:

- audit a LinkedIn profile or exported profile PDF;
- review headline, About, Experience, Featured, Skills, credentials, or activity;
- compare LinkedIn with a résumé, portfolio, matching profile, or evidence bank;
- propose ready-to-review wording without publishing it;
- identify positioning, evidence, consistency, or discoverability gaps.

Do not use to log in, edit the profile, post, comment, react, follow, message, connect, upload, or inspect private analytics.

## Consent-aware intake

A LinkedIn URL identifies a profile; it does not automatically authorise fetching or logged-in browsing.

Prefer, in order:

1. user-supplied profile export or PDF;
2. pasted profile sections;
3. user-supplied screenshots;
4. explicitly authorised public profile reads that require no login;
5. indexed snippets, labelled partial and stale-prone.

If the public surface is blocked or incomplete, preserve `BLOCKED`, `DEGRADED`, or `NOT_EVALUATED`. Do not reuse an authenticated browser session or infer inaccessible content.

## Audit depth

- **Quick:** headline, About opening, current role positioning, Featured proof, and top three corrections.
- **Default:** all supplied core sections plus up to five recent activity items.
- **Deep:** complete supplied/exported profile, approved résumé/evidence/portfolio consistency, proof architecture, and bounded activity review.

Do not silently inspect an unlimited activity history. Five recent supplied/public items is the default cap.

## Evidence contract

Use the package vocabulary:

- `VERIFIED` — independently supported by approved evidence;
- `OBSERVED` — directly visible in the supplied/public profile surface;
- `USER_REPORTED` — supplied by the user but not independently checked;
- `INFERRED` — reasoned interpretation, not stated fact;
- `UNKNOWN` — not established;
- `VERIFY_BEFORE_USE` — plausible but unsuitable for public wording until checked.

Context, memory, prior drafts, and AI-generated copy do not independently verify a claim. When evidence conflicts, stop the rewrite and surface the conflict.

## Authority contract

### Allowed

- read user-supplied exports, pasted text, and screenshots;
- read approved résumé, evidence-bank, portfolio, and positioning sources;
- bounded public web reads when explicitly authorised and no login is required;
- draft replacement wording for human review;
- write an advisory audit to a configured private workspace when authorised.

### Forbidden

- logged-in or authenticated LinkedIn browsing;
- profile edits, posts, comments, reactions, follows, connections, messages, uploads, or applications;
- claims about profile views, search ranking, impressions, recruiter behaviour, endorsements, or applicant outcomes without supplied evidence;
- treating third-party “algorithm” commentary as platform fact;
- inventing dates, metrics, credentials, employers, duties, outcomes, or work preferences.

## Dual-audience architecture

Audit four layers separately:

1. **Structured fields:** headline, titles, organisations, dates, location, skills, credentials.
2. **Narrative:** About and Experience prose explaining direction, judgement, and contribution.
3. **Proof assets:** Featured links, projects, publications, credentials, and portfolio evidence.
4. **Activity:** bounded recent posts/comments that reinforce or contradict the professional story.

A strong profile aligns all four without repeating the same paragraph everywhere.

## Workflow

### 1. Establish positioning and scope

Record:

- target role families and professional identity;
- supplied profile surfaces;
- approved evidence and résumé versions;
- audit depth and activity cap;
- whether the task is audit-only or includes draft wording;
- external actions: none.

Do not infer that every approved résumé detail belongs on LinkedIn. The surfaces have different functions and privacy costs.

### 2. Check identity and structured fields

Inspect supplied/visible:

- name and preferred public identity;
- headline;
- location/work preference wording;
- current and previous role titles;
- organisations and dates;
- education and credentials;
- skills and ordering;
- custom URL and contact exposure when supplied.

Flag factual conflicts, stale states, unsupported titles, duplicated entries, and unnecessary private detail. Do not recommend exposing contact or location data merely for completeness.

### 3. Audit the headline

The headline should make role direction and useful capability legible without becoming keyword soup. Check:

- recognisable target role language;
- strongest supported differentiator;
- truthful seniority;
- readability aloud;
- consistency with current evidence.

Avoid invented titles, strings of tools, “aspiring” apologies, and grand claims unsupported by experience.

### 4. Audit About

Check whether the opening quickly answers:

- what kind of work the candidate does or is moving toward;
- which problems they are good at handling;
- what evidence supports that direction;
- what kind of opportunity makes sense next.

The section should sound like the user, not a corporate horoscope. Prefer concrete operating patterns over adjectives. Credentials and tools support the story rather than replacing it.

### 5. Audit Experience and projects

For each supplied entry:

- verify organisation/title/date consistency;
- separate responsibility from outcome;
- preserve transferable evidence without impersonating direct industry tenure;
- distinguish coursework, guided projects, AI assistance, implementation, orchestration, and verification;
- check that important work is understandable without private context;
- ensure public links point to evidence that exists and is safe to share.

Use `SUPPORTED`, `PARTIAL`, `UNSUPPORTED`, `CONFLICT`, or `UNKNOWN` for material claims.

### 6. Audit Featured and proof assets

Ask whether each asset:

- supports the intended career story;
- is currently public and understandable;
- has clear provenance and status;
- avoids private data, stale outputs, or broken links;
- adds distinct proof rather than duplicating another item.

Recommend a small proof set. Featured is a shop window, not the warehouse inventory.

### 7. Audit skills and credentials

Check that visible skills and credentials:

- are supported and current;
- reflect target duties rather than every tool encountered;
- do not imply professional depth from coursework alone;
- use exact credential names and dates when verified;
- avoid expired, proposed, or incomplete items presented as current.

Do not infer endorsement quality or recruiter search impact from skill order.

### 8. Audit bounded activity

Inspect no more than the agreed cap. Evaluate whether recent supplied/public activity:

- reinforces the professional direction;
- demonstrates useful thinking or work;
- contradicts stated positioning;
- exposes private, inflammatory, or employer-sensitive material;
- is too sparse to support any conclusion.

No recommendation to post authorises posting. Drafts remain local until explicit approval and a separate mutation workflow.

### 9. Separate algorithm confidence

Classify platform/discoverability claims:

- **DOCUMENTED:** current official LinkedIn documentation or directly observed UI constraint;
- **REASONABLE_INFERENCE:** ordinary search/recruiter behaviour inferred from structured fields;
- **THIRD_PARTY_COMMENTARY:** consultant/newsletter claims;
- **DISPUTED_OR_UNKNOWN:** no reliable current support.

Do not present folklore about posting cadence, keyword density, creator mode, engagement tricks, or ranking systems as settled fact.

### 10. Check cross-surface consistency

Compare only inspected approved sources. Preserve purposeful differences while flagging:

- conflicting dates/titles;
- unsupported metrics or outcomes;
- stale learning/project states;
- credentials missing or overstated;
- portfolio links that do not support the wording;
- a headline/About direction incompatible with the matching profile.

Say “no conflict found in inspected inputs,” not “fully consistent,” when access is partial.

### 11. Prioritise corrections and draft selectively

Rank:

1. false, unsupported, conflicting, or privacy-sensitive content;
2. unclear positioning;
3. weak or missing proof assets;
4. Experience entries that obscure contribution;
5. stale credentials/skills;
6. discoverability and cosmetic polish.

Draft only the sections requested or required to show the correction. Never rewrite the entire profile merely because one headline is weak.

## Optional scoring

If requested:

- define categories and weights;
- score inspected categories only;
- rescale unavailable categories;
- show evidence and access limits;
- treat scores as prioritisation aids, not recruiter-response predictions.

## Output contract

Use `templates/audit_report.md`. Include:

1. decision brief;
2. scope, sources, and unavailable surfaces;
3. dual-audience architecture findings;
4. section-by-section evidence findings;
5. cross-surface conflicts;
6. prioritised correction queue;
7. proposed wording, clearly marked `DRAFT_REVIEW`;
8. source ledger, external actions, and next owner.

## Common pitfalls

1. **URL treated as consent.** Ask for or use supplied bounded inputs.
2. **Logged-in access used for convenience.** Stop at the boundary.
3. **Résumé pasted into About.** LinkedIn has a different job.
4. **Keyword soup.** Clarity and support beat density.
5. **Algorithm folklore stated as fact.** Label confidence.
6. **Every activity item inspected.** Keep a cap.
7. **Public proof exposes private context.** Review assets before recommending them.
8. **Draft wording becomes published action.** Human review and mutation remain separate.

## Verification checklist

- [ ] `job-hunter-core` was followed.
- [ ] Consent, audit depth, sources, and unavailable surfaces are explicit.
- [ ] No logged-in LinkedIn access occurred.
- [ ] Evidence labels use the package taxonomy.
- [ ] Structured fields, narrative, proof assets, and activity were separated.
- [ ] Material claims were checked against approved evidence.
- [ ] Activity inspection stayed within the agreed cap.
- [ ] Algorithm/discoverability claims have confidence labels.
- [ ] Cross-surface conclusions are bounded to inspected inputs.
- [ ] Draft wording is marked for human review.
- [ ] No edit, post, reaction, follow, connection, message, upload, or application occurred.
