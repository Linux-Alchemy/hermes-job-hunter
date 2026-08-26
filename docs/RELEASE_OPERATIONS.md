# Release operations

This document covers installation, update, rollback, and release verification for Hermes Job Hunter.

## Install

Install from GitHub:

```bash
hermes profile install github.com/Linux-Alchemy/hermes-job-hunter --alias
```

For package testing from a clone:

```bash
git clone https://github.com/Linux-Alchemy/hermes-job-hunter.git
cd hermes-job-hunter
python scripts/validate_package.py
hermes profile install . --name hermes-job-hunter-test -y
```

Do not copy a live profile back into the repository. Candidate evidence, enabled source state, applications, voice samples, credentials, sessions, logs, and OAuth material remain private runtime data.

## Update an installation

Before updating, back up adopter-owned profile data and record the installed revision. The distribution owns only the paths declared in `distribution.yaml`; local evidence and application workspaces should remain outside those package-owned paths.

```bash
git -C /path/to/hermes-job-hunter fetch origin
PREVIOUS_REVISION=$(git -C /path/to/hermes-job-hunter rev-parse HEAD)
git -C /path/to/hermes-job-hunter switch master
git -C /path/to/hermes-job-hunter pull --ff-only
python /path/to/hermes-job-hunter/scripts/validate_package.py
hermes profile install /path/to/hermes-job-hunter --name <profile-name> -y
```

After installation, verify:

- all expected skills are present;
- `career-document-production` exposes three `resume_production` tools;
- the local source registry and private evidence remain outside package-owned paths;
- rendering still blocks if the required font is absent;
- no external integration was enabled implicitly.

## History-rewrite migration

The pre-release history was rewritten before publication to remove private author metadata. Existing clones from before that rewrite must not merge the old and new histories.

Preserve any local work first:

```bash
git status
git branch backup/pre-history-rewrite
```

Then replace the local public branch with the rewritten remote branch:

```bash
git fetch origin --prune
git switch master
git reset --hard origin/master
```

If local commits must survive, export them as patches or cherry-pick reviewed commits onto a new branch created from the rewritten `origin/master`. Do not force-push old-history branches back to the repository.

## Roll back an installed version

Choose a previously verified revision or tag. Do not guess a revision.

```bash
git -C /path/to/hermes-job-hunter log --oneline --decorate -n 20
git -C /path/to/hermes-job-hunter switch --detach <verified-revision>
python /path/to/hermes-job-hunter/scripts/validate_package.py
hermes profile install /path/to/hermes-job-hunter --name <profile-name> -y
```

Rollback restores package-owned profile files. It does not roll back private applications, evidence, credentials, integrations, or external actions. Those require their own backups and reconciliation.

To return to the current release:

```bash
git -C /path/to/hermes-job-hunter switch master
git -C /path/to/hermes-job-hunter pull --ff-only
```

## Release checklist

### Repository state

- [ ] Working tree is clean.
- [ ] `master` is the intended release branch.
- [ ] Distribution version and release notes agree.
- [ ] Every commit uses the public project author/committer identity.
- [ ] No `refs/original/*` history-rewrite refs remain.
- [ ] Reflogs and unreachable pre-rewrite objects have been pruned after a verified external backup.

### Automated validation

```bash
python scripts/validate_package.py
python -m unittest discover \
  -s plugins/career-document-production/tests \
  -p 'test_*.py' -v
git diff --check
```

The validator must pass structure, configuration, source-registry, skill, plugin, schema, fixture, link, semantic privacy, DOCX, generated-file, symlink, and Git-metadata checks.

### Disposable-profile acceptance

```bash
hermes profile install . --name hermes-job-hunter-release-test -y
hermes profile show hermes-job-hunter-release-test
hermes --profile hermes-job-hunter-release-test tools list
hermes --profile hermes-job-hunter-release-test skills list
hermes profile delete hermes-job-hunter-release-test -y
```

Confirm 12 local skills, one plugin, three renderer tools, bounded toolsets, and no unexpected integration.

### Human review

- [ ] Review the public tree for disguised personal assumptions, not merely literal PII.
- [ ] Review `PROVENANCE.md` against every shipped skill, plugin, binary, and fixture.
- [ ] Confirm examples are fictional and source URLs use reserved invalid domains.
- [ ] Confirm `SOUL.md` still forbids submission, uploads, employer messaging, public-profile mutation, account creation, and authority expansion.
- [ ] Confirm Google, authenticated GitHub, messaging, Kanban, and cron remain optional.
- [ ] Record explicit owner publication approval.

### Publish and verify

For an ordinary release, use a fast-forward push. After an authorised history rewrite, use `--force-with-lease` exactly once against the reviewed remote state:

```bash
git fetch origin
git push --force-with-lease=refs/heads/master:<expected-old-remote-sha> origin master
```

Then verify from the remote rather than trusting the push receipt:

```bash
git fetch origin
test "$(git rev-parse master)" = "$(git rev-parse origin/master)"
git log origin/master --format='%H %an <%ae> %cn <%ce>'
```

A release is not complete until remote HEAD equals local HEAD and remote-visible history passes the public-identity check.

## Recovery bundle

A pre-rewrite bundle may be retained outside the repository for disaster recovery. It contains intentionally superseded private metadata and must never be committed, uploaded, attached to a release, or used to restore public history without another sanitation pass.
