# Source Access Decisions

This is the human-readable companion to `job_source_registry.local.yaml`. Keep operational reasoning here; keep executable settings in YAML.

## Review metadata

- Registry version:
- Reviewed on:
- Reviewed by:
- Environment/profile:

## Source decision template

### `<source_id>` — `<display name>`

- **Decision:** core | supplemental | setup deferred | excluded
- **Observed access:**
- **Coverage value:**
- **Known gaps/noise:**
- **Authority or setup cost:**
- **Why enabled or disabled:**
- **Employer-original verification path:**
- **Revisit when:**

## Global decisions

Record decisions that apply across sources, such as:

- jurisdiction and genuine-remote requirements;
- acceptable freshness windows;
- result caps;
- when supplemental sources may run;
- whether keyed APIs, accounts, subscriptions, or alerts are allowed;
- which external actions remain forbidden.

Do not store API keys, tokens, cookies, passwords, OAuth material, personal identifiers, or raw private messages in this file.
