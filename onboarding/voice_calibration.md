# Voice Calibration

Generic human-writing cleanup removes common AI patterns. It does not teach an agent how a particular user thinks, qualifies claims, explains trade-offs, or sounds across different professional registers.

This onboarding exercise creates a user-owned calibration layer without modifying an upstream shared skill.

## Before starting

1. Identify any existing human-writing or voice skills.
2. Determine ownership:
   - patch a clearly user-owned voice skill;
   - otherwise create a small user-specific overlay and calibration reference;
   - do not modify bundled, vendor-maintained, or shared upstream skills.
3. Choose a rollback method: Git history, a versioned copy, or a recorded patch.
4. Keep personal writing samples outside the public repository.

## Collect several registers

Use authentic, unedited writing where possible. One sample is not a voice.

Collect at least:

- a technical explanation;
- a project or scope decision;
- a professional email;
- a public project paragraph;
- a résumé or application paragraph.

Preserve slips in the private evidence file, but never manufacture slips in polished writing to appear human.

## Baseline test

Before changing the voice skill:

1. give the agent a real bounded writing task;
2. save the exact prompt and unedited result;
3. label factual or evidence failures separately from voice failures;
4. ask the user what sounds right, wrong, inflated, generic, or unlike them.

## Derive a narrow rule

The agent should propose:

- the durable pattern it believes the samples support;
- the evidence for that pattern;
- where the rule applies;
- where it does not apply;
- the exact small diff to the user-owned skill or overlay.

Do not turn occasional words, typos, swearing, sentence fragments, or one successful metaphor into compulsory mannerisms.

## Approval and rerun

1. The user reviews the proposed rule and diff.
2. Apply only the approved change.
3. Record the previous and new version.
4. Rerun the same baseline prompt.
5. Compare evidence discipline, naturalness, authorship fidelity, and professional suitability.
6. Mark the result `passed`, `passed_with_feedback`, or `failed`.

Further calibration should come from real work and explicit corrections, not constant personality archaeology.

## Application-writing boundary

The agent may draft and organise. The user remains the author and decision owner.

A later user edit is expected. It is not evidence that calibration failed. Failure means the draft invents substance, hides uncertainty, performs a generic professional identity, or repeatedly ignores confirmed feedback.
