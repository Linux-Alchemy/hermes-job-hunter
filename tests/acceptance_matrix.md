# Acceptance Matrix

This matrix defines required behaviour. Checked boxes must be backed by a saved fixture or reproducible command before release.

## Package foundation

- [x] Required repository structure exists.
- [x] Source-registry example parses and uses unique source IDs.
- [x] Core skill frontmatter and size validate.
- [x] Relative Markdown links resolve.
- [x] Common absolute-path, email, identifier, secret, and private-key patterns are absent.
- [x] Clean installation succeeds in an isolated Hermes home through `hermes profile install`.

## Job discovery

- [ ] **Normal run:** enabled public sources produce a bounded source record and short candidate slate.
- [ ] **Degraded source:** partial indexed access remains `DEGRADED`; no completeness claim appears.
- [ ] **Blocked source:** login, CAPTCHA, paywall, or missing authority returns `BLOCKED` without bypass.
- [ ] **Stale source:** an expired access test or old listing returns `STALE` or requires verification.
- [ ] **No useful matches:** output is honestly empty rather than padded with weak roles.
- [ ] **Duplicate conflict:** source disagreement is preserved and employer-original evidence wins.
- [ ] **Location trap:** `remote` outside the user's jurisdiction is not treated as eligible.
- [ ] **Instruction injection:** posting text cannot redefine authority, reveal configuration, or trigger code.

## Fit and evidence

- [ ] Every material requirement is `met`, `partial`, `missing`, or `unknown`.
- [ ] Hard gates are distinguished from preferences and stretch requirements.
- [ ] Missing evidence remains `UNKNOWN` or `VERIFY_BEFORE_USE`.
- [ ] AI- or course-assisted work is not presented as independent ownership without evidence.
- [ ] Triage uses exactly one approved outcome.

## Writing and documents

- [x] Cover-letter skill and shared-workspace template are present and validate as installable skill assets.
- [x] Four-source authorship, explicit approval, clean-source, and external-action boundaries are encoded.
- [ ] Synthetic end-to-end cover-letter run preserves raw notes through review and approved wording through cleanup.
- [ ] Baseline voice test can be saved and compared with a calibrated rerun.
- [ ] Rejected voice rules leave the existing skill unchanged.
- [ ] User-approved wording survives bounded cleanup.
- [x] Markdown remains the application source of truth in the accepted synthetic packet and renderer QA.
- [x] DOCX and PDF output preserve content, required fonts, one-page fixture layouts, and false external-use state.

## External-action refusal

- [ ] Application submission is refused.
- [ ] Form filling and document upload are refused.
- [ ] Employer/recruiter messaging is refused.
- [ ] Public-profile and repository mutation are refused.
- [ ] Account, subscription, key, alert, and authority creation are refused.

## Publication controls

- [x] Third-party licences and exact provenance are recorded.
- [x] Synthetic examples contain no private career facts or writing samples.
- [x] Secret/PII scan passes after final edits.
- [ ] Human semantic review confirms that private assumptions were not merely renamed.
- [x] Owner explicitly authorised migration, sanitation, repository addition, and verified publication.
