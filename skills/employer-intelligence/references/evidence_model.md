# Employer-intelligence evidence model

Use this reference when public company information is fragmented, promotional, contradictory, or partly inaccessible.

## Evidence matrix

| Claim class | Preferred source | Acceptable fallback | Required caution |
|---|---|---|---|
| Role duties and benefits | Employer-original posting | Employer ATS index | Separate posting promises from established company-wide practice. |
| Legal employer and jurisdiction | Employer posting, offer documentation, company legal page | None | If not explicit, use `UNKNOWN`; remote is not jurisdiction. |
| Product and customers | Product pages, documentation, customer cases | Independent product coverage | Logos and testimonials remain company-curated. |
| Revenue model | Pricing, filings, executive interview | Reputable industry reporting | Date old evidence and do not infer current monetisation. |
| Funding and valuation | Company announcement plus independent reporting | Investor database | Funding is not profitability; valuation carries its round date. |
| Headcount | Current professional-network band plus another directory | One dated directory | Post-acquisition headcount is often unreliable. |
| Acquisitions | Company announcement plus independent trade coverage | Company announcement alone | Announcement supports the transaction claim, not integration success. |
| Culture and benefits | Careers page and current posting | Employer profile | These are employer claims. |
| Employee sentiment | Review platform with sample size and dates | Indexed review summaries | Directional only; preserve access limits and mixed themes. |
| Product abuse or scams | Repeated customer/app evidence plus company trust material | A single complaint | Platform abuse does not prove that the company itself is fraudulent. |

## Review handling

1. Capture the visible review count before quoting an aggregate rating.
2. Record ratings and recommendation percentages only when visible.
3. Extract repeated positive and negative themes rather than centring the most dramatic anecdote.
4. Distinguish current employees, former employees, interns, contractors, and role-specific reviews when visible.
5. If the page blocks extraction, say `indexed summary only`.
6. Treat very small visible samples as low-weight signals.
7. Date the review snapshot because ratings move.
8. After a merger, compare parent and subsidiary evidence separately and keep combined culture `UNKNOWN` until supported.

## Acquisition lens

Investigate:

- acquisition date;
- stated integration approach;
- whether the acquired brand or product remains active;
- platform and infrastructure migration plans;
- legacy benefits and remote policy;
- team or leadership continuity;
- supported and dated restructuring evidence;
- vacancy origin, labelled `INFERRED` until confirmed.

Turn findings into questions about reporting lines, migration, role origin, team changes, workload, and what remains stable.

## Metric-conflict rules

- Keep reach, records, downloads, and active users separate.
- Keep valuation tied to its financing date.
- Keep current employee count separate from a broad directory band.
- Keep subsidiary benefit pages separate from the current employer posting.
- Prefer a visible conflict over tidy but invented reconciliation.

## Decision brief

Lead with:

1. Is the employer credible enough to continue evaluating?
2. What is the organisation actually doing now?
3. What context most changes the interpretation of the role?
4. Which two or three unknowns gate the next action?

The rest of the profile supplies evidence for those answers; it is not an invitation to reproduce the company website.
