#!/usr/bin/env python3
"""Validate the repository's structural and hygiene contracts."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import NoReturn

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment failure
    raise SystemExit("PyYAML is required: install it or run inside Hermes Agent") from exc

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "distribution.yaml",
    "SOUL.md",
    "config.yaml",
    "README.md",
    "LICENSE",
    "PROJECT_STATUS.md",
    "PROVENANCE.md",
    "skills/job-hunter-core/SKILL.md",
    "skills/cover-letter-drafting/SKILL.md",
    "skills/cover-letter-drafting/templates/cover_letter_workspace.md",
    "skills/cover-letter-drafting/references/proven_workflow_pattern.md",
    "skills/career-document-rendering/SKILL.md",
    "plugins/career-document-production/plugin.yaml",
    "plugins/career-document-production/__init__.py",
    "plugins/career-document-production/schemas.py",
    "plugins/career-document-production/tools.py",
    "plugins/career-document-production/templates/resume_template.docx",
    "config/source_registry.example.yaml",
    "config/source_access_decisions.example.md",
    "docs/ARCHITECTURE.md",
    "onboarding/voice_calibration.md",
    "tests/acceptance_matrix.md",
]
SCAN_ROOTS = [
    ROOT / "distribution.yaml",
    ROOT / "SOUL.md",
    ROOT / "config.yaml",
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / "PROJECT_STATUS.md",
    ROOT / "PROVENANCE.md",
    ROOT / "skills",
    ROOT / "plugins",
    ROOT / "config",
    ROOT / "docs",
    ROOT / "onboarding",
    ROOT / "tests",
]
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".txt", ".py"}


def fail(message: str) -> NoReturn:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def iter_text_files() -> list[Path]:
    found: list[Path] = []
    for item in SCAN_ROOTS:
        if item.is_file():
            found.append(item)
        elif item.is_dir():
            found.extend(p for p in item.rglob("*") if p.is_file() and p.suffix in TEXT_SUFFIXES)
    return sorted(set(found))


def validate_required_files() -> None:
    missing = [relative for relative in REQUIRED if not (ROOT / relative).is_file()]
    if missing:
        fail(f"missing required files: {', '.join(missing)}")


def validate_distribution() -> None:
    path = ROOT / "distribution.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail("distribution manifest is not a mapping")
    for field in ("name", "version", "description", "hermes_requires", "author", "license"):
        if not data.get(field):
            fail(f"distribution manifest missing field: {field}")
    if data["name"] != "hermes-job-hunter":
        fail("distribution name must be hermes-job-hunter")
    if data["license"] != "MIT":
        fail("distribution licence must be MIT")
    expected_owned = {"distribution.yaml", "SOUL.md", "config.yaml", "skills/", "plugins/"}
    owned = data.get("distribution_owned")
    if not isinstance(owned, list) or set(owned) != expected_owned:
        fail("distribution_owned paths do not match the public runtime payload")

    config = yaml.safe_load((ROOT / "config.yaml").read_text(encoding="utf-8"))
    if not isinstance(config, dict):
        fail("config.yaml is not a mapping")


def validate_registry() -> tuple[int, int]:
    path = ROOT / "config/source_registry.example.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        fail("unsupported source-registry schema")
    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        fail("source registry has no sources")
    required = {
        "source_id", "display_name", "priority", "enabled", "scan_by_default",
        "lane", "purpose", "access_method", "connector_id", "setup_state",
        "authority_needed", "coverage", "employer_verification",
        "known_failure_modes", "last_access_test",
    }
    ids: list[str] = []
    for source in sources:
        missing = required - set(source)
        if missing:
            fail(f"{source.get('source_id', '<unknown>')} missing {sorted(missing)}")
        ids.append(source["source_id"])
        if source["scan_by_default"] and not source["enabled"]:
            fail(f"{source['source_id']} is default-scanned while disabled")
    if len(ids) != len(set(ids)):
        fail("duplicate source IDs")
    enabled = sum(bool(source["enabled"]) for source in sources)
    return len(sources), enabled


def validate_skills() -> int:
    skill_paths = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skill_paths:
        fail("no skills found")
    names: set[str] = set()
    for path in skill_paths:
        text = path.read_text(encoding="utf-8")
        label = str(path.relative_to(ROOT))
        if not text.startswith("---\n"):
            fail(f"{label} frontmatter does not start at byte zero")
        match = re.search(r"\n---\s*\n", text[4:])
        if not match:
            fail(f"{label} frontmatter is not closed")
        end = match.start() + 4
        try:
            frontmatter = yaml.safe_load(text[4:end])
        except yaml.YAMLError as exc:
            fail(f"{label} frontmatter is invalid YAML: {exc}")
        if not isinstance(frontmatter, dict):
            fail(f"{label} frontmatter is not a mapping")
        for field in ("name", "description", "version", "author", "license", "metadata"):
            if not frontmatter.get(field):
                fail(f"{label} missing frontmatter field: {field}")
        if frontmatter["name"] != path.parent.name:
            fail(f"{label} name does not match its directory")
        if frontmatter["name"] in names:
            fail(f"duplicate skill name: {frontmatter['name']}")
        names.add(frontmatter["name"])
        if len(frontmatter["description"]) > 1024:
            fail(f"{label} description exceeds 1024 characters")
        if frontmatter["license"] != "MIT":
            fail(f"{label} licence must be MIT")
        if len(text) > 100_000:
            fail(f"{label} exceeds Hermes size limit")
    return len(skill_paths)


def validate_links() -> int:
    checked = 0
    link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for path in iter_text_files():
        if path.suffix != ".md":
            continue
        for target in link_pattern.findall(path.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            checked += 1
            if not (path.parent / target).resolve().exists():
                fail(f"broken relative link in {path.relative_to(ROOT)}: {target}")
    return checked


def validate_hygiene() -> int:
    # These are generic leakage patterns. Final publication still requires human review.
    patterns = {
        "absolute user home path": re.compile(r"/home/[^/\s]+"),
        "email address": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
        "platform-style numeric identifier": re.compile(r"(?<!\d)\d{17,20}(?!\d)"),
        "private key marker": re.compile(r"BEGIN (?:RSA |OPENSSH )?PRIVATE KEY"),
        "credential-like assignment": re.compile(
            r"(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)\s*[:=]\s*[\"']?[A-Za-z0-9_\-]{16,}",
            re.I,
        ),
    }
    scanned = 0
    for path in iter_text_files():
        text = path.read_text(encoding="utf-8")
        scanned += 1
        for label, pattern in patterns.items():
            if pattern.search(text):
                fail(f"{label} found in {path.relative_to(ROOT)}")
    return scanned


def validate_symlinks() -> None:
    symlinks = [path.relative_to(ROOT) for path in ROOT.rglob("*") if path.is_symlink()]
    if symlinks:
        fail("symlinks require explicit review: " + ", ".join(map(str, symlinks)))


def main() -> None:
    validate_required_files()
    validate_distribution()
    source_count, enabled_count = validate_registry()
    skill_count = validate_skills()
    checked_links = validate_links()
    scanned_files = validate_hygiene()
    validate_symlinks()
    print("PASS: required package structure")
    print("PASS: Hermes distribution manifest and config")
    print(f"PASS: source registry ({source_count} unique sources; {enabled_count} enabled by default)")
    print(f"PASS: skill frontmatter and size ({skill_count} skills)")
    print(f"PASS: relative Markdown links ({checked_links} checked)")
    print(f"PASS: hygiene scan ({scanned_files} public artefacts)")
    print("PASS: no symlinks")


if __name__ == "__main__":
    main()
