---
name: cover-letter-drafting
description: "Use when developing an application-specific cover letter through a shared, iterative workspace grounded in the user's notes, the employer posting, company research, and approved résumé evidence."
version: 0.1.0
author: Linux-Alchemy
license: MIT
metadata:
  hermes:
    tags: [career, cover-letter, drafting, applications, authorship]
    related_skills: [job-hunter-core]
---

# Cover-Letter Drafting

## Overview

Produce one concise, application-specific cover letter through a shared drafting process that keeps the user's real reasons and wording in control. The result should explain why the user wants this role, connect verified experience to the actual work, show that the employer was investigated, and remain defensible in an interview.

This skill owns Markdown argument development, drafting, revision, and approved-source cleanup. It does not own résumé wording, DOCX/PDF rendering, uploading, application submission, employer contact, or salary negotiation.

Load and follow `job-hunter-core`. Load the adopter's approved human-writing cleaner and user-specific voice overlay when available. A public skill must not manufacture a private voice calibration.

## When to use

Use when the user asks the specialist to:

- create a cover letter for an active application;
- develop rough notes or quotations into a professional letter;
- revise an existing application-specific cover letter;
- collaborate through annotations in a shared draft file;
- produce a cleaned Markdown source after explicit approval.

Do not use for:

- generic reusable letters detached from a live role;
- speculative letters without an identified employer and posting;
- résumé rewriting or document rendering;
- application forms, uploads, submission, or employer messages;
- salary research or negotiation.

## The four-source authorship model

Build the letter from four sources:

1. **Current user notes.** These control motive, meaning, emphasis, and personal voice.
2. **Employer-original posting.** This supplies duties, requirements, terminology, and useful ATS language.
3. **Company profile.** This supplies specific employer context and the reason this company is worth addressing. It must not turn the letter into a corporate-history recital.
4. **Approved résumé and evidence.** These bound every claim about experience and capability.

No source is sufficient alone. The posting says what the employer wants but not why the user cares. The résumé establishes evidence but does not automatically form an argument. The company profile supplies context, most of which should remain outside the letter. User notes supply authorship but do not replace factual verification.

Current notes outrank static voice tendencies. Verified evidence outranks convenient phrasing. The posting controls emphasis, not truth.

## Required inputs

Before drafting, require:

- employer-original posting captured in the application packet;
- current company profile or bounded employer research;
- approved general or application-specific résumé source;
- user notes, quotations, reactions, or reasons for applying;
- target application directory;
- confirmation that a cover letter is wanted.

Retrieve existing packet files before asking the user to repeat anything. If the notes already contain a usable argument, do not conduct an intake ceremony. Ask at most one focused question when a missing detail would materially change the letter. Otherwise draft.

Stop when:

- the employer or role is ambiguous;
- the posting is missing or no longer verifiable;
- there is no approved evidence base;
- a requested claim conflicts with verified evidence;
- the user's motive would have to be invented;
- a hard eligibility gate would be obscured rather than preserved.

## Shared workspace

Use the adopter's configured private application workspace. A recommended packet shape is:

```text
applications/<company_slug>/<role_slug>/
├── application_status.md
├── cover_letter_draft.md
├── source/
│   ├── job_posting.md
│   ├── company_profile.md
│   ├── approved_resume_snapshot.md
│   └── approved_cover_letter.md
└── outputs/
```

`cover_letter_draft.md` is the shared conversation surface. Begin with the user's notes exactly as supplied. Beneath them add:

```markdown
---

# First pass draft
```

Do not remove, spell-correct, reorganise, or tidy the user's notes. They are source material and authorship evidence.

Use `templates/cover_letter_workspace.md` when starting a new workspace.

## Argument extraction

Before drafting, privately identify:

- the most genuine reason the user noticed or cares about the role;
- one strong opening hook when the notes contain one;
- what the job actually does rather than what its title implies;
- two or three evidence bridges between the user's background and those duties;
- one or two company-specific details worth using;
- qualifications that are developing rather than professionally established;
- claims that must not be made;
- company research that belongs in interview preparation rather than the letter.

Do not show a formal truth ledger unless asked. Reflect useful conclusions in ordinary language.

## Reflect before drafting

When direction is not already explicit, briefly reflect the strongest argument before writing. Identify:

- the proposed spine of the letter;
- why the supplied notes are useful;
- anything that should be softened or excluded;
- the likely beginning, middle, and end.

This is a reasoning check, not an approval tribunal. If the user agrees and asks for the draft, proceed. If all four sources were already supplied with a direct request for a first pass, do not insert another gate.

## First-pass drafting

Write one complete first pass. Do not produce three synthetic alternatives unless asked.

### Standard structure

**Header**

- user contact information;
- date;
- employer;
- exact role;
- professional salutation.

**Opening**

- how or why the user encountered the opportunity;
- why this employer or problem caught their attention;
- one specific company connection.

**Middle**

- what the role actually combines;
- evidence from work, projects, education, or current development;
- a clear bridge from that evidence to the role's duties;
- relevant posting language used naturally.

**Close**

- the practical reason the company's work matters to the user;
- the contribution they could make;
- a restrained invitation to discuss fit.

### Length and format

- Standard business-letter format.
- One page maximum; preferably somewhat less than a full page.
- Usually four to six compact body paragraphs.
- Remove secondary evidence before shrinking below the renderer's approved font-size floor.
- Do not solve excess length through narrow margins, compressed spacing, or ornamental layout.

## Voice, evidence, and ATS pass

Check that:

- current user notes still control meaning;
- the voice is professional but recognisably the user's;
- company language has not been copied wholesale;
- one or two researched specifics prove attention without showing off the research file;
- ATS terms occur only where evidence supports them;
- unfinished learning is not presented as professional tenure;
- adjacent experience is not renamed to mimic a missing title;
- technical projects are not converted into production experience;
- no unsupported metric, ownership claim, feeling, or certainty appears;
- promotional recruiter fog has been removed;
- the ending stops rather than delivering a motivational summary.

Read the result as speech. If the user could not say or defend a sentence in an interview, simplify, verify, or remove it.

## Collaborative review loop

1. Tell the user that the first pass is in the shared workspace.
2. The user reads and annotates that file directly.
3. Reread the current file from disk before every revision.
4. Apply only requested or clearly implied changes.
5. Preserve approved wording that already works.
6. Do not create alternative versions unless asked.
7. Do not keep improving the draft merely because another revision round is available.

The file is the conversation surface. Chat should carry short decisions, focused questions, and receipts so the user does not have to type the same editorial context twice.

## Approval and clean-source handoff

Only the human decision owner can approve wording. Approval must be explicit, such as:

- `Use it as is.`
- `I have nothing to add.`
- `This is approved.`
- `Create the clean copy.`

Praise alone does not authorise finalisation unless the user also instructs the specialist to use or clean the draft.

Once approved, stop editing. Approval is not permission for one final stealth-polish pass.

Create the configured clean source under the packet's `source/` directory with metadata such as:

```yaml
---
document_type: cover_letter
company: "<Company>"
role: "<Exact role>"
lifecycle_state: APPROVED_MARKDOWN
approved_by: "<Human decision owner>"
approved_at: YYYY-MM-DD
base_resume_path: "<approved résumé source>"
---
```

Remove:

- raw notes;
- workspace separator;
- `# First pass draft`;
- editorial annotations;
- unresolved comments.

The approved letter itself remains unchanged. Read the clean source back and compare it with the approved draft before reporting completion.

## Rendering handoff

Render only when the user explicitly requests DOCX/PDF production and an approved renderer is available.

The renderer should own and enforce its document standard, including:

- configured font family;
- allowed font-size range;
- page limits;
- text agreement between Markdown, DOCX, and PDF;
- page previews and visual inspection;
- refusal to substitute a missing required font silently.

Wording returns to this skill if content changes are required for pagination. A rendering tool must not quietly edit approved prose.

## Lifecycle states

Keep transitions separate:

```text
NOTES_CAPTURED
FIRST_PASS
HUMAN_REVIEW
APPROVED_MARKDOWN
RENDERED
READY_FOR_EXTERNAL_USE
SUBMITTED
```

- Notes do not approve an argument.
- Direction approval does not approve wording.
- Markdown approval does not approve rendering.
- A validated render is not externally ready.
- External-use approval does not authorise submission.
- Submission is recorded only after the user reports completing it.

## Common pitfalls

1. Drafting before reading user notes.
2. Treating the résumé as the letter's argument.
3. Copying a company mission and calling it research.
4. Using every interesting company-profile fact.
5. Stuffing posting keywords into unsupported claims.
6. Asking ten questions when the notes already contain a usable spine.
7. Producing three options instead of one considered draft.
8. Renaming adjacent experience to imitate a missing title.
9. Inflating coursework into professional experience.
10. Removing raw notes before collaboration is finished.
11. Rewriting an approved letter during cleanup.
12. Rendering before clean-source approval.
13. Silently substituting a missing font.
14. Uploading, submitting, or contacting an employer.

## Verification checklist

- [ ] `job-hunter-core` and approved writing/voice procedures were loaded.
- [ ] Employer posting, company profile, approved résumé, and current notes were read.
- [ ] User notes remain verbatim in the workspace.
- [ ] Opening contains a genuine reason for this application.
- [ ] Letter addresses the job's real duties.
- [ ] Company specificity is present but restrained.
- [ ] ATS terminology is natural and evidence-supported.
- [ ] No unsupported experience, ownership, metric, motive, or certainty appears.
- [ ] Standard professional structure is designed for one page.
- [ ] Human decision owner explicitly approved the wording.
- [ ] Clean source matches the approved draft and contains approval metadata.
- [ ] Rendering was separately requested and routed to an approved renderer.
- [ ] No upload, submission, message, or public mutation occurred.

## References

- `templates/cover_letter_workspace.md` — shared notes-plus-draft workspace.
- `references/proven_workflow_pattern.md` — sanitized explanation of the validated four-source method without private application content.
