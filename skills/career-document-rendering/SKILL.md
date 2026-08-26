---
name: career-document-rendering
description: "Use after the human approves an exact résumé or cover-letter Markdown source. Produces bounded DOCX/PDF working artefacts through the packaged renderer, enforces the controlled font and page limits, verifies text/structure, and requires real visual review before external-use approval."
version: 0.1.0
author: Linux-Alchemy
license: MIT
metadata:
  hermes:
    tags: [career, resume, cover-letter, docx, pdf, rendering, validation]
    related_skills: [job-hunter-core, application-packet, resume-drafting, cover-letter-drafting]
---

# Career Document Rendering

## Overview

Turn one human-approved résumé or cover-letter Markdown source into versioned DOCX and PDF artefacts, permit explicitly authorised layout-only correction of a working render, and prove that content, structure, font, and page boundaries survived conversion.

This skill owns **rendering and validation**, not wording. It uses the packaged `resume_production` plugin toolset rather than ad-hoc conversion commands. Résumé wording returns to `resume-drafting`; cover-letter wording returns to `cover-letter-drafting`.

## Trigger and hard gate

Use only when the human explicitly asks to render a named source under the active profile's private workspace and the source frontmatter contains:

```yaml
document_type: resume | cover_letter
lifecycle_state: APPROVED_MARKDOWN
approved_by: <human approver>
approved_at: YYYY-MM-DD
```

A résumé source requires a level-1 candidate/name heading. A cover letter requires standard letter content and a salutation beginning with `Dear`.

Do not infer approval from file location, a previous render, an application-packet state, a conversation summary, or the agent's own review. Do not alter wording to fix pagination. Return substantive changes to the owning drafting skill and obtain approval again.

## Controlled document standard

The packaged template uses:

- font family: `JetBrainsMono NF`;
- permitted controlled-style sizes: 9–12 points inclusive;
- style-specific sizes within that range for hierarchy and page fit;
- no silent font substitution;
- plain single-column layout;
- no tables, drawings, text boxes, macros, headers, or footers.

Before rendering or revising, the plugin asks fontconfig for `JetBrainsMono NF` or the canonical installed alias `JetBrainsMono Nerd Font`. DOCX QA verifies that every controlled style declares `JetBrainsMono NF` and remains within 9–12 points.

If the font is unavailable, stop and ask the human decision owner to select an alternate. Do not use a generic fallback or whatever LibreOffice finds behind the sofa. A different font requires an explicit human choice and a controlled template/plugin revision before work resumes.

## Required tools

Use:

- `resume_render_approved` for initial generation;
- `resume_validate_artifacts` to recheck an existing DOCX/PDF pair;
- `resume_revise_layout` for a human-authorised layout-only edit to a working render;
- `vision_analyze` for actual review of every generated page preview.

If the plugin, LibreOffice, Poppler utilities, Python dependency, required font, or visual-review tool is unavailable, report `BLOCKED`. Do not install packages or invent a replacement renderer during an application task.

## Enforced boundaries

The plugin enforces:

- source and output containment under the active profile workspace's `resumes/` or `applications/` lanes;
- one packet's `source/` to that packet's `outputs/` path;
- snake_case output stems and `_vN` versioning;
- refusal to overwrite an existing fresh-render version;
- approved `resume` or `cover_letter` source type;
- required-font availability before creation;
- controlled DOCX styles using 9–12-point `JetBrainsMono NF`;
- no tables, drawings, text boxes, macros, headers, or footers;
- token-for-token DOCX/PDF agreement with approved Markdown after markup normalization;
- a real PDF text layer;
- maximum two pages for a résumé and one page for a cover letter;
- PDF size below the configured parser threshold;
- page-preview creation and a machine-readable QA manifest.

It does not submit, upload, email, message, or mark an artefact externally ready.

## Procedure

1. Load `job-hunter-core`, `application-packet`, and the owning drafting skill.
2. Confirm source path, packet root, document slug, and next unused version.
3. Read source frontmatter and stop unless approval metadata satisfies the hard gate.
4. Call `resume_render_approved` once. Do not route around a refusal by renaming an existing artefact, weakening source state, changing the root, or bypassing a missing-font check.
5. Read every mechanical QA result. Explicitly confirm font-family, size, page, text-layer, text-agreement, structure, parser-size, and preview checks.
6. If any check fails, retain lifecycle `RENDERED_VALIDATION_FAILED` and report the exact failure.
7. If mechanical checks pass, inspect **every** preview with `vision_analyze`. Check clipping, overlap, detached headings, awkward page breaks, hierarchy, density, tiny text, and conspicuous dead space.
8. Compare extracted text with meaningful source anchors:
   - résumé: header/contact block, section order, every role/project heading, dates, credentials, and final bullet;
   - cover letter: header, employer/role, salutation, every body paragraph, sign-off, and final name.
9. Record visual outcome in the QA manifest or sibling review note:
   - `VALIDATED` for mechanical success;
   - `HUMAN_REVIEW` after agent visual review passes;
   - never `READY_FOR_EXTERNAL_USE` without explicit human approval.
10. Report DOCX, PDF, extracted text, previews, QA manifest, page count/limit, font verdict, warnings, and visual verdict.
11. If the human requests a supported layout correction, call `resume_revise_layout` on the existing working DOCX using the exact paragraph anchor and operation.
12. Reinspect every regenerated preview; previous visual findings are stale after revision.
13. When the human approves the rendered artefact, record `READY_FOR_EXTERNAL_USE` in the private application status. The approved version becomes immutable; later corrections require a new version.

## Supported layout revisions

`resume_revise_layout` accepts only:

- `page_break_before`;
- `remove_page_break_before`;
- `keep_block_together`.

The exact visible paragraph anchor must match once. The caller must set `human_authorized: true` only after explicit instruction.

These operations may alter pagination flags but not text. Reusable changes to margins, spacing, style sizes, font, or heading treatment require a reviewed template/plugin change and regression tests.

## Change routing

- **Résumé wording, claims, bullets, or section order:** `resume-drafting`; reapprove Markdown; render a new version.
- **Cover-letter wording or structure:** `cover-letter-drafting`; reapprove the clean source; render a new version.
- **One-off pagination of a working render:** `resume_revise_layout` after explicit human instruction.
- **Reusable layout or font policy:** controlled plugin/template change with tests.
- **Missing required font:** stop and request a human-selected alternate.
- **Conversion, extraction, or dependency failure:** `BLOCKED`; do not improvise another toolchain.
- **Portal requests another format:** preserve DOCX/PDF, follow the user-approved requirement, and record which file was used.

## Output layout

The plugin writes only inside the packet's `outputs/` directory:

```text
<document_slug>_vN.docx
<document_slug>_vN.pdf
<document_slug>_vN_extracted.txt
<document_slug>_vN_preview/page-1.png
<document_slug>_vN_qa.json
```

Working artefacts remain editable for authorised layout review until the human marks them `READY_FOR_EXTERNAL_USE`. External-ready, submitted, or uploaded versions are immutable.

## Common pitfalls

1. **Approval inferred from location.** Frontmatter and explicit request both matter.
2. **Pagination fixed through rewriting.** Route content back to drafting.
3. **Mechanical QA treated as visual QA.** Inspect every page image.
4. **Old preview reused after revision.** Regenerate and reinspect.
5. **Font fallback accepted silently.** Stop and ask.
6. **Fresh version used for a tiny layout adjustment.** Revise the existing working render when authorised.
7. **Rendered means externally ready.** Human external-use approval is separate.
8. **Plugin unavailable, so shell improvisation begins.** Report the blocked dependency instead.

## Verification checklist

- [ ] Human explicitly approved the exact Markdown source.
- [ ] Source type and approval metadata passed the plugin gate.
- [ ] Correct packet and next unused version were used.
- [ ] Required-font availability passed before document creation.
- [ ] QA confirms controlled styles use `JetBrainsMono NF` at 9–12 points.
- [ ] Mechanical QA passed or exact failures were reported.
- [ ] Résumé is no more than two pages; cover letter is exactly one page.
- [ ] Every page preview received actual visual inspection.
- [ ] Extracted text retained content and reading order.
- [ ] No content changed to solve layout.
- [ ] Any layout correction was explicitly authorised and applied to the existing working render.
- [ ] Every preview was reinspected after the latest revision.
- [ ] Artefact remains short of external-use approval until the human decides.
- [ ] No upload, submission, contact, message, or public mutation occurred.
