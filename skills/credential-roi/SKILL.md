---
name: credential-roi
description: "Use when deciding whether a course, certification, programme, or credential is worth the user's time and money. Separates learning, signal, access, structure, and confidence value; maps overlap and market recognition; audits outcome claims; and compares the credential with the smallest evidence-producing alternative."
version: 0.1.0
author: Linux-Alchemy
license: MIT
metadata:
  hermes:
    tags: [career, credentials, education, roi, decision-analysis]
    related_skills: [job-hunter-core, job-discovery, cv-audit, linkedin-audit, github-portfolio-audit]
---

# Credential ROI

## Overview

Evaluate whether a credential deserves the user's next block of time, money, and attention. Treat learning value, labour-market signal, access requirements, structure, and confidence as separate benefits rather than collapsing them into “good course” or “recognised certificate.”

Load `job-hunter-core` first. Use current first-party provider and employer evidence for time-sensitive claims. The result is a decision aid, not a promise of employment.

Supporting files:

- [Decision-report template](templates/decision_report.md)
- [Provenance](references/provenance.md)

## When to use

Use when the user asks:

- whether to start, continue, defer, or skip a credential;
- how much genuinely new learning it adds;
- whether employers request or recognise it;
- whether provider outcome claims are credible;
- how long it will probably take given prior knowledge;
- whether a smaller project, module, or portfolio brick would produce better evidence.

Do not use to enrol, purchase, subscribe, create accounts, alter a résumé/profile, or treat a credential as completed before verification.

## Decision purposes

Classify the user's intended value. More than one may apply:

- `LEARNING` — acquire useful knowledge or practice;
- `SIGNAL` — communicate validated knowledge to employers;
- `ACCESS` — satisfy a formal gate or prerequisite;
- `STRUCTURE` — obtain a bounded sequence, deadline, or assessment framework;
- `CONFIDENCE` — build enough familiarity to act or speak credibly.

A credential can be strong for one purpose and weak for another. A course that teaches well but appears in no job requirements may still be worthwhile for `LEARNING`, but not for `SIGNAL`.

## Authority contract

### Allowed

- approved career, evidence-bank, résumé, portfolio, and learning-plan reads;
- public provider curriculum, price, assessment, renewal, and access information;
- current employer-original postings and public market evidence;
- calculations using an available calculation tool with inputs shown;
- advisory writes to a configured private review workspace.

### Forbidden

- enrolment, purchase, subscription, payment, account creation, or credential sharing;
- logged-in course or job-board access;
- résumé, LinkedIn, portfolio, or application mutation;
- unsupported claims that the credential guarantees interviews, salary, promotion, or employment;
- presenting historical provider prices, curricula, or market references as current without revalidation.

## Evidence states

For commitment and effort, distinguish:

- `PUBLISHED` — current official provider value;
- `LEARNER_REPORTED` — bounded reports from identifiable learner samples;
- `USER_SPECIFIC_INFERENCE` — estimate based on the user's verified overlap and pace;
- `UNKNOWN` — not established.

For topic overlap, use `met / partial / missing / unknown`. For career evidence, use `job-hunter-core` states.

## Workflow

### 1. Establish the decision

Record:

- credential/provider/version;
- user's decision question and intended purposes;
- current price/budget constraint;
- target roles, jurisdictions, and work constraints;
- prior knowledge and relevant evidence;
- time horizon and competing commitments;
- research date;
- external actions: none.

Do not assume that a credential under consideration fits the user's current strategy merely because it is adjacent.

### 2. Map the official commitment

From current first-party sources, separate:

- curriculum and topic coverage;
- provider-stated hours or schedule;
- required versus optional modules;
- assessments, projects, labs, or proctoring;
- skipping, placement, or prior-learning rules;
- subscription versus one-time price;
- trial, financial-aid, cancellation, and refund terms;
- renewal, expiry, continuing-education, and exam-retake requirements;
- regional availability and language;
- credential title and issuing organisation.

Do not conflate course hours, elapsed subscription months, study schedule, and exam preparation.

### 3. Estimate user effort with bounded scenarios

Build at least three scenarios where evidence permits:

- optimistic reuse of prior knowledge;
- expected pace;
- conservative completion with revision or retakes.

Show:

- published baseline;
- overlap assumption;
- weekly time assumption;
- estimated study hours;
- estimated elapsed time;
- likely cost range under the pricing model;
- what could invalidate the estimate.

Use a calculation tool. Do not invent decimals for inherently fuzzy inputs.

### 4. Build a topic-level overlap map

Compare curriculum topics with approved evidence:

| Topic | met/partial/missing/unknown | Existing evidence | Incremental value |
|---|---|---|---|

Distinguish:

- already learned and evidenced;
- learned but weakly evidenced;
- genuinely new knowledge;
- repeated fundamentals useful only for consolidation;
- content irrelevant to target roles;
- access to assessments/labs/projects that creates new proof.

A certificate can add signal without adding much knowledge, or add knowledge without adding credible proof.

### 5. Test market recognition

Use current employer-original postings and first-party programme relationships. Record exact observations:

- credential explicitly required;
- explicitly preferred;
- named as one of several equivalents;
- provider relationship or employer consortium claim;
- no exact mention found in the bounded sample;
- recurring skills/topics requested without credential mention.

State query, source, jurisdiction, role family, sample limits, and access date. Zero hits do not prove zero recognition.

Separate credential recognition from provider brand recognition and from the value of the underlying skills.

### 6. Audit outcome claims

For every placement, salary, completion, promotion, interview, or employer-recognition claim, ask:

- who was included in the population;
- sample size and response rate;
- geography and time period;
- whether participants were career changers, incumbent workers, or selected completers;
- exact outcome definition;
- comparison/control group;
- whether the result is correlation, self-report, marketing aggregation, or causal evidence;
- whether the claim applies to this credential/version.

Provider testimonials and consortium membership do not prove individual hiring advantage.

### 7. Compare the smallest competing brick

Do not compare one large course only with another large course. Identify the smallest realistic alternative that produces the missing value:

- one module;
- one lab or assessment;
- a focused book chapter;
- a small tested project;
- a portfolio case study;
- direct interview preparation;
- targeted practice on a recurring gap;
- waiting until employer demand appears.

Compare time, cost, evidence produced, market signal, maintenance/renewal, and opportunity cost.

### 8. Evaluate ROI dimensions

Rate qualitatively with evidence:

- incremental learning;
- signal/recognition;
- formal access value;
- portfolio/evidence production;
- relevance to target duties;
- time cost;
- financial cost;
- opportunity cost;
- completion risk;
- renewal/maintenance burden;
- confidence/structure value;
- reversibility.

If a numeric model is requested, define inputs and weights, calculate with a tool, and label the score diagnostic rather than predictive.

### 9. Choose one decision state

- `DO_NOW` — strong current value and acceptable opportunity cost;
- `SPRINT_WITH_CAP` — useful if completed inside an explicit time/cost ceiling;
- `TAKE_SELECTED_MODULES` — learning value exists but the full credential does not earn its cost;
- `DEFER_UNTIL_SIGNAL` — revisit when employer demand, prerequisites, price, or timing changes;
- `SKIP` — weak incremental value relative to alternatives.

Name the trigger that would change the decision.

### 10. Define public-claim boundaries

Until completion is verified:

- do not add the credential to résumé or LinkedIn as completed;
- label current study accurately if the user approves public disclosure;
- distinguish course completion from certification/exam award;
- preserve exact credential name, issuer, issue date, and expiry only when verified;
- do not claim employer recognition beyond the researched sample.

## Output contract

Use `templates/decision_report.md`. Lead with:

1. decision state;
2. why;
3. expected time/cost range;
4. genuinely new learning;
5. signal evidence;
6. smallest competing brick;
7. decision-changing trigger.

Then include official commitment, overlap, market sample, outcome-claim audit, ROI dimensions, source ledger, unknowns, actions, and owner.

## Common pitfalls

1. **Provider hours equal user hours.** Build scenarios.
2. **Curriculum overlap means zero value.** Signal, assessment, and structure may differ.
3. **Employer consortium means hiring preference.** Verify exact claims.
4. **Search snippets called market proof.** Use employer-original postings where possible.
5. **Credential compared only with another course.** Find the smallest competing brick.
6. **Numeric ROI treated as truth.** It is a transparent diagnostic.
7. **Sunk cost controls the decision.** Evaluate remaining cost and value.
8. **Research becomes enrolment.** External action remains human-owned.

## Verification checklist

- [ ] `job-hunter-core` was followed.
- [ ] Credential version, purpose, target roles, constraints, and research date are explicit.
- [ ] Official hours, schedule, assessments, price, renewal, and access remain separate.
- [ ] Effort scenarios show inputs and uncertainty.
- [ ] Topic overlap uses `met / partial / missing / unknown`.
- [ ] Recognition evidence uses exact current sources and bounded samples.
- [ ] Provider outcome claims were audited for population, geography, response, definition, and causation.
- [ ] Smallest evidence-producing alternative was compared.
- [ ] One decision state and a decision-changing trigger are named.
- [ ] Public-claim boundaries are explicit.
- [ ] No enrolment, purchase, account, résumé/profile mutation, or application action occurred.
