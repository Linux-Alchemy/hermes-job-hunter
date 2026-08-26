#!/usr/bin/env python3
"""Validate Hermes Job Hunter structure, runtime assets, provenance, and privacy."""

from __future__ import annotations

import ast
import json
import re
import subprocess
import sys
import unicodedata
import zipfile
from pathlib import Path
from typing import Any, NoReturn
from xml.etree import ElementTree as ET

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("PyYAML is required: install it or run inside Hermes Agent") from exc

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:  # pragma: no cover
    raise SystemExit("jsonschema is required: install it or run inside Hermes Agent") from exc

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {
    "application-packet",
    "career-document-rendering",
    "cover-letter-drafting",
    "credential-roi",
    "cv-audit",
    "employer-intelligence",
    "github-portfolio-audit",
    "job-discovery",
    "job-hunter-core",
    "linkedin-audit",
    "resume-drafting",
    "source-registry-maintenance",
}
EXPECTED_PLUGINS = {"career-document-production"}
REQUIRED = [
    "distribution.yaml",
    "SOUL.md",
    "config.yaml",
    "README.md",
    "LICENSE",
    "PROJECT_STATUS.md",
    "PROVENANCE.md",
    "config/job_source_registry.example.yaml",
    "config/source_access_decisions.example.md",
    "schemas/career_matching_profile.schema.json",
    "schemas/career_evidence_bank.schema.json",
    "examples/candidate/career_matching_profile.example.yaml",
    "examples/candidate/career_evidence_bank.example.yaml",
    "plugins/career-document-production/plugin.yaml",
    "plugins/career-document-production/__init__.py",
    "plugins/career-document-production/schemas.py",
    "plugins/career-document-production/tools.py",
    "plugins/career-document-production/scripts/build_template.py",
    "plugins/career-document-production/templates/resume_template.docx",
    "plugins/career-document-production/tests/test_tools.py",
    "docs/ARCHITECTURE.md",
    "docs/OPTIONAL_INTEGRATIONS.md",
    "onboarding/voice_calibration.md",
    "tests/acceptance_matrix.md",
    "tests/fixtures/job_discovery/cases.yaml",
    "tests/fixtures/application/input_manifest.yaml",
    "tests/fixtures/refusal_cases.yaml",
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
    ROOT / "schemas",
    ROOT / "examples",
    ROOT / "docs",
    ROOT / "onboarding",
    ROOT / "scripts",
    ROOT / "tests",
]
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".txt", ".py", ".toml"}
PRIVATE_TERMS = (
    "Ma" + "tt",
    "Kli" + "mo",
    "rea" + "per",
    "Rogue" + "Wizard",
    "Pre" + "fect",
    "Fo" + "rd",
    "Red" + "XIII",
    "Job" + "Get",
    "Wood" + "lawn",
    "rogue" + "wizard42",
    "matt" + ".klimo",
)
PUBLIC_PROJECT_HANDLE = "Linux-Alchemy"
PUBLIC_GIT_EMAIL = "linux-alchemy" + "@users.noreply.github.com"
W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def fail(message: str) -> NoReturn:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def iter_text_files() -> list[Path]:
    found: list[Path] = []
    for item in SCAN_ROOTS:
        if item.is_file() and item.suffix in TEXT_SUFFIXES:
            found.append(item)
        elif item.is_dir():
            found.extend(
                path
                for path in item.rglob("*")
                if path.is_file()
                and path.suffix in TEXT_SUFFIXES
                and ".git" not in path.parts
                and "__pycache__" not in path.parts
            )
    return sorted(set(found))


def validate_required_files() -> None:
    missing = [item for item in REQUIRED if not (ROOT / item).is_file()]
    if missing:
        fail(f"missing required files: {', '.join(missing)}")


def validate_distribution() -> dict[str, Any]:
    data = yaml.safe_load((ROOT / "distribution.yaml").read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail("distribution manifest is not a mapping")
    for field in ("name", "version", "description", "hermes_requires", "author", "license"):
        if not data.get(field):
            fail(f"distribution manifest missing field: {field}")
    if data["name"] != "hermes-job-hunter":
        fail("distribution name must be hermes-job-hunter")
    if data["author"] != PUBLIC_PROJECT_HANDLE:
        fail("distribution author must use the public project handle")
    if data["license"] != "MIT":
        fail("distribution licence must be MIT")
    if not re.fullmatch(r"0\.\d+\.\d+", str(data["version"])):
        fail("pre-release distribution version must use 0.minor.patch")
    expected_owned = {"distribution.yaml", "SOUL.md", "config.yaml", "skills/", "plugins/"}
    owned = data.get("distribution_owned")
    if not isinstance(owned, list) or set(owned) != expected_owned:
        fail("distribution_owned paths do not match the runtime payload")
    return data


def validate_config() -> None:
    data = yaml.safe_load((ROOT / "config.yaml").read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail("config.yaml is not a mapping")
    plugins = data.get("plugins") or {}
    enabled = set(plugins.get("enabled") or [])
    if enabled != EXPECTED_PLUGINS:
        fail(f"enabled plugins differ from expected set: {sorted(enabled)}")
    toolsets = data.get("platform_toolsets") or {}
    for platform in ("cli", "discord"):
        selected = set(toolsets.get(platform) or [])
        required = {"clarify", "file", "resume_production", "skills", "todo", "vision", "web"}
        if selected != required:
            fail(f"{platform} toolsets differ from bounded package contract")


def validate_registry() -> tuple[int, int]:
    path = ROOT / "config/job_source_registry.example.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        fail("unsupported source-registry schema")
    if data.get("policy", {}).get("target_jurisdictions") != []:
        fail("public source registry must not select an adopter jurisdiction")
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
        if not isinstance(source, dict):
            fail("source registry entry is not a mapping")
        missing = required - set(source)
        if missing:
            fail(f"{source.get('source_id', '<unknown>')} missing {sorted(missing)}")
        ids.append(str(source["source_id"]))
        if source["enabled"] or source["scan_by_default"]:
            fail(f"public registry source is active: {source['source_id']}")
        if source["setup_state"] != "not_configured":
            fail(f"public registry source is not inert: {source['source_id']}")
        if source["last_access_test"] is not None:
            fail(f"public registry contains live access date: {source['source_id']}")
    if len(ids) != len(set(ids)):
        fail("duplicate source IDs")
    return len(sources), 0


def parse_skill_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    label = relative(path)
    if not text.startswith("---\n"):
        fail(f"{label} frontmatter does not start at byte zero")
    end = text.find("\n---\n", 4)
    if end < 0:
        fail(f"{label} frontmatter is not closed")
    try:
        frontmatter = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        fail(f"{label} frontmatter is invalid YAML: {exc}")
    if not isinstance(frontmatter, dict):
        fail(f"{label} frontmatter is not a mapping")
    if not text[end + 5 :].strip():
        fail(f"{label} has no skill body")
    return frontmatter


def validate_skills() -> int:
    skill_paths = sorted((ROOT / "skills").glob("*/SKILL.md"))
    found = {path.parent.name for path in skill_paths}
    if found != EXPECTED_SKILLS:
        fail(f"skill inventory mismatch: expected {sorted(EXPECTED_SKILLS)}, found {sorted(found)}")
    provenance = (ROOT / "PROVENANCE.md").read_text(encoding="utf-8")
    names: set[str] = set()
    related_by_skill: dict[str, set[str]] = {}
    for path in skill_paths:
        text = path.read_text(encoding="utf-8")
        frontmatter = parse_skill_frontmatter(path)
        label = relative(path)
        for field in ("name", "description", "version", "author", "license", "metadata"):
            if not frontmatter.get(field):
                fail(f"{label} missing frontmatter field: {field}")
        name = str(frontmatter["name"])
        if name != path.parent.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            fail(f"{label} name does not match its directory or naming contract")
        if name in names:
            fail(f"duplicate skill name: {name}")
        names.add(name)
        if frontmatter["author"] != PUBLIC_PROJECT_HANDLE:
            fail(f"{label} author must use the public project handle")
        if frontmatter["license"] != "MIT":
            fail(f"{label} licence must be MIT")
        if len(str(frontmatter["description"])) > 1024:
            fail(f"{label} description exceeds 1024 characters")
        if len(text) > 100_000:
            fail(f"{label} exceeds Hermes size limit")
        metadata = frontmatter.get("metadata") or {}
        hermes = metadata.get("hermes") if isinstance(metadata, dict) else None
        if not isinstance(hermes, dict) or not isinstance(hermes.get("tags"), list):
            fail(f"{label} missing metadata.hermes.tags")
        related = hermes.get("related_skills") or []
        if not isinstance(related, list):
            fail(f"{label} related_skills must be a list")
        related_by_skill[name] = {str(item) for item in related}
        if f"skills/{name}/" not in provenance and f"skills/{name}/SKILL.md" not in provenance:
            fail(f"root provenance does not classify {name}")
    for name, related in related_by_skill.items():
        unresolved = related - names
        if unresolved:
            fail(f"{name} references unshipped skills: {sorted(unresolved)}")
    return len(skill_paths)


def registered_plugin_tools(init_path: Path) -> tuple[set[str], set[str]]:
    tree = ast.parse(init_path.read_text(encoding="utf-8"), filename=str(init_path))
    tools: set[str] = set()
    toolsets: set[str] = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
            continue
        if node.func.attr != "register_tool":
            continue
        values = {keyword.arg: keyword.value for keyword in node.keywords if keyword.arg}
        for field, target in (("name", tools), ("toolset", toolsets)):
            value = values.get(field)
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                target.add(value.value)
    return tools, toolsets


def validate_plugins() -> tuple[int, int]:
    manifests = sorted((ROOT / "plugins").glob("*/plugin.yaml"))
    names = {path.parent.name for path in manifests}
    if names != EXPECTED_PLUGINS:
        fail(f"plugin inventory mismatch: {sorted(names)}")
    total_tools = 0
    for manifest_path in manifests:
        data = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            fail(f"{relative(manifest_path)} is not a mapping")
        name = manifest_path.parent.name
        for field in ("name", "version", "manifest_version", "api_version", "description", "license", "provides_tools"):
            if data.get(field) in (None, "", []):
                fail(f"{relative(manifest_path)} missing {field}")
        if data["name"] != name or data["license"] != "MIT":
            fail(f"{relative(manifest_path)} identity/licence mismatch")
        declared = set(data["provides_tools"])
        registered, toolsets = registered_plugin_tools(manifest_path.parent / "__init__.py")
        if declared != registered:
            fail(f"{name} declared/registered tools differ")
        if toolsets != {"resume_production"}:
            fail(f"{name} toolset differs from configured contract")
        total_tools += len(declared)
    caches = [
        path for path in ROOT.rglob("*")
        if "__pycache__" in path.parts or path.suffix in {".pyc", ".pyo"}
    ]
    if caches:
        fail("generated Python cache files are present: " + ", ".join(relative(path) for path in caches[:5]))
    return len(manifests), total_tools


def validate_schema_examples() -> int:
    pairs = [
        ("career_matching_profile", "career_matching_profile"),
        ("career_evidence_bank", "career_evidence_bank"),
    ]
    count = 0
    for schema_stem, example_stem in pairs:
        schema_path = ROOT / f"schemas/{schema_stem}.schema.json"
        example_path = ROOT / f"examples/candidate/{example_stem}.example.yaml"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        data = yaml.safe_load(example_path.read_text(encoding="utf-8"))
        errors = sorted(
            Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(data),
            key=lambda error: list(error.path),
        )
        if errors:
            first = errors[0]
            fail(f"{relative(example_path)} schema error at {list(first.path)}: {first.message}")
        count += 1
    return count


def validate_fixtures() -> int:
    discovery = yaml.safe_load((ROOT / "tests/fixtures/job_discovery/cases.yaml").read_text(encoding="utf-8"))
    cases = discovery.get("cases") if isinstance(discovery, dict) else None
    if not isinstance(cases, list):
        fail("job-discovery fixture cases must be a list")
    required_cases = {
        "normal_verified_fit", "degraded_index_only", "blocked_login", "stale_access_state",
        "remote_location_trap", "duplicate_source_conflict", "instruction_injection", "honest_empty_slate",
    }
    found = {case.get("case_id") for case in cases or [] if isinstance(case, dict)}
    if found != required_cases:
        fail("job-discovery fixture inventory mismatch")
    refusals = yaml.safe_load((ROOT / "tests/fixtures/refusal_cases.yaml").read_text(encoding="utf-8"))
    refusal_cases = refusals.get("cases") if isinstance(refusals, dict) else None
    if not isinstance(refusal_cases, list) or len(refusal_cases) != 8:
        fail("refusal fixture must contain eight cases")
    for case in refusal_cases:
        expected = case.get("expected") or {}
        if expected.get("result") != "REFUSE" or expected.get("side_effects") != "none":
            fail(f"invalid refusal fixture: {case.get('case_id')}")
    manifest = yaml.safe_load((ROOT / "tests/fixtures/application/input_manifest.yaml").read_text(encoding="utf-8"))
    if manifest.get("approvals", {}).get("external_use") is not None:
        fail("synthetic application fixture must not approve external use")
    if manifest.get("approvals", {}).get("submission") is not None:
        fail("synthetic application fixture must not approve submission")
    return len(cases) + len(refusal_cases) + 1


def validate_links() -> int:
    checked = 0
    pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for path in iter_text_files():
        if path.suffix != ".md":
            continue
        for target in pattern.findall(path.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            checked += 1
            if not (path.parent / target).resolve().exists():
                fail(f"broken relative link in {relative(path)}: {target}")
    return checked


def hygiene_patterns() -> dict[str, re.Pattern[str]]:
    return {
        "absolute user home path": re.compile("/" + "home" + r"/[^/\s]+"),
        "email address": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
        "platform-style numeric identifier": re.compile(r"(?<!\d)\d{17,20}(?!\d)"),
        "private key marker": re.compile(r"BEGIN (?:RSA |OPENSSH )?PRIVATE KEY"),
        "credential-like assignment": re.compile(
            r"(?:api[_-]?key|access[_-]?token|refresh[_-]?token|client[_-]?secret|password)"
            r"\s*[:=]\s*[\"']?[A-Za-z0-9_\-]{16,}",
            re.I,
        ),
    }


def validate_hygiene() -> int:
    patterns = hygiene_patterns()
    private_patterns = {
        term: re.compile(rf"(?<![A-Za-z0-9]){re.escape(term)}(?![A-Za-z0-9])", re.I)
        for term in PRIVATE_TERMS
    }
    controls = {chr(code) for code in range(0x202A, 0x202F)} | {chr(code) for code in range(0x2066, 0x206A)}
    scanned = 0
    for path in iter_text_files():
        text = path.read_text(encoding="utf-8")
        scanned += 1
        for label, pattern in patterns.items():
            if pattern.search(text):
                fail(f"{label} found in {relative(path)}")
        for term, pattern in private_patterns.items():
            if path == Path(__file__).resolve():
                continue
            if pattern.search(text):
                fail(f"private semantic term found in {relative(path)}: {term}")
        if any(character in controls for character in text):
            fail(f"bidirectional control character found in {relative(path)}")
        for character in text:
            if unicodedata.category(character) == "Cf" and character not in {"\u200c", "\u200d"}:
                fail(f"unexpected format-control character found in {relative(path)}")
    return scanned


def validate_docx_template() -> None:
    path = ROOT / "plugins/career-document-production/templates/resume_template.docx"
    if not zipfile.is_zipfile(path):
        fail("renderer template is not a valid DOCX package")
    patterns = hygiene_patterns()
    with zipfile.ZipFile(path) as archive:
        names = set(archive.namelist())
        for name in names:
            if name.endswith((".xml", ".rels")):
                text = archive.read(name).decode("utf-8", errors="replace")
                for label, pattern in patterns.items():
                    if label == "platform-style numeric identifier":
                        continue  # OOXML font metadata contains long numeric signatures.
                    if pattern.search(text):
                        fail(f"{label} found inside DOCX {name}")
                for term in PRIVATE_TERMS:
                    if re.search(rf"(?<![A-Za-z0-9]){re.escape(term)}(?![A-Za-z0-9])", text, re.I):
                        fail(f"private semantic term found inside DOCX {name}: {term}")
        core = ET.fromstring(archive.read("docProps/core.xml"))
        creators = [node.text for node in core if node.tag.endswith("creator") or node.tag.endswith("lastModifiedBy")]
        if any((value or "").strip() for value in creators):
            fail("DOCX template creator/last-modifier metadata must be blank")
        forbidden = [
            name for name in names
            if "vbaProject" in name or name.endswith(".bin") or name.startswith("word/embeddings/")
        ]
        if forbidden:
            fail("DOCX template contains active or embedded content")


def validate_no_generated_or_unexpected_files() -> None:
    forbidden_names = {".env", "auth.json", "state.db", "credentials.json", "token.json"}
    hits = [path for path in ROOT.rglob("*") if path.is_file() and path.name in forbidden_names]
    if hits:
        fail("forbidden credential/runtime file found: " + ", ".join(relative(path) for path in hits))
    allowed_binary = {ROOT / "plugins/career-document-production/templates/resume_template.docx"}
    binaries = [
        path for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and path.suffix not in TEXT_SUFFIXES
        and path.name not in {"LICENSE", ".gitignore"}
        and path not in allowed_binary
    ]
    if binaries:
        fail("unexpected binary/runtime files: " + ", ".join(relative(path) for path in binaries[:10]))


def validate_symlinks() -> None:
    symlinks = [path for path in ROOT.rglob("*") if path.is_symlink() and ".git" not in path.parts]
    if symlinks:
        fail("symlinks require explicit review: " + ", ".join(relative(path) for path in symlinks))


def validate_git_metadata() -> int:
    if not (ROOT / ".git").exists():
        return 0
    result = subprocess.run(
        ["git", "log", "--all", "--format=%H%x09%an%x09%ae%x09%cn%x09%ce"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    lines = [line for line in result.stdout.splitlines() if line]
    for line in lines:
        lowered = line.casefold()
        for term in PRIVATE_TERMS:
            if term.casefold() in lowered:
                fail(f"private identity remains in Git metadata: {line.split(chr(9), 1)[0]}")
        fields = line.split("\t")
        if len(fields) != 5:
            fail("unexpected Git metadata format")
        _, author, email, committer, committer_email = fields
        if author != PUBLIC_PROJECT_HANDLE or committer != PUBLIC_PROJECT_HANDLE:
            fail(f"non-project Git author/committer remains: {fields[0]}")
        if email != PUBLIC_GIT_EMAIL or committer_email != PUBLIC_GIT_EMAIL:
            fail(f"non-project Git email remains: {fields[0]}")
    return len(lines)


def main() -> None:
    validate_required_files()
    manifest = validate_distribution()
    validate_config()
    source_count, enabled_count = validate_registry()
    skill_count = validate_skills()
    plugin_count, plugin_tool_count = validate_plugins()
    schema_count = validate_schema_examples()
    fixture_count = validate_fixtures()
    checked_links = validate_links()
    scanned_files = validate_hygiene()
    validate_docx_template()
    validate_no_generated_or_unexpected_files()
    validate_symlinks()
    git_commit_count = validate_git_metadata()
    print("PASS: required package structure")
    print(f"PASS: distribution {manifest['name']} {manifest['version']} and bounded config")
    print(f"PASS: source registry ({source_count} unique sources; {enabled_count} enabled)")
    print(f"PASS: skill inventory/frontmatter/links ({skill_count} skills)")
    print(f"PASS: plugin manifests/registrations ({plugin_count} plugin; {plugin_tool_count} tools)")
    print(f"PASS: JSON Schemas and synthetic examples ({schema_count} pairs)")
    print(f"PASS: synthetic fixtures ({fixture_count} cases/contracts)")
    print(f"PASS: relative Markdown links ({checked_links} checked)")
    print(f"PASS: text/semantic hygiene ({scanned_files} public artefacts)")
    print("PASS: DOCX metadata/content hygiene")
    print("PASS: no generated caches, unexpected binaries, credential files, or symlinks")
    print(f"PASS: Git metadata uses public project identity ({git_commit_count} commits)")


if __name__ == "__main__":
    main()
