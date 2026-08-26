"""End-to-end tests for the bounded Hermes Job Hunter résumé renderer."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from plugin_test_loader import load_tools


APPROVED = """---
title: "Test Resume"
document_type: resume
resume_scope: general
lifecycle_state: APPROVED_MARKDOWN
approved_by: Human Reviewer
approved_at: 2026-08-25
---

# Test Candidate

Candidate region | portfolio.example.invalid/candidate

## Summary

Technical operator who verifies work before declaring it complete.

## Experience

### Builder | Example Company

January 2024 - Present

- Built one bounded workflow and documented the acceptance checks.
- Investigated failures without inventing successful output.

## Education

- Example Diploma | 2025
"""

COVER_LETTER = """---
title: "Test Cover Letter"
document_type: cover_letter
company: "Example Company"
role: "Operations Analyst"
lifecycle_state: APPROVED_MARKDOWN
approved_by: Human Reviewer
approved_at: 2026-08-26
---

Test Candidate  
Candidate region  
portfolio.example.invalid/candidate

August 26, 2026

Hiring Team  
Example Company

**Re: Operations Analyst**

Dear Hiring Team,

I found this role while testing a bounded job-search workflow. The work combines customer operations and data, which matches the direction I am building toward.

My experience includes coordinating practical work, explaining unfamiliar material, and documenting results so another person can follow them.

Sincerely,

Test Candidate
"""


class ResumeToolsE2E(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "career"
        self.packet = self.root / "resumes" / "general"
        self.source = self.packet / "source" / "resume.md"
        self.source.parent.mkdir(parents=True)
        self.source.write_text(APPROVED, encoding="utf-8")
        self.tools = load_tools()
        self.tools.CAREER_ROOT = self.root.resolve()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def render(self) -> dict:
        return json.loads(self.tools.render_approved({
            "source_markdown": str(self.source),
            "document_slug": "test_resume",
            "version": 1,
        }))

    def test_render_validate_and_refuse_overwrite(self) -> None:
        result = self.render()
        self.assertTrue(result["success"], result)
        self.assertTrue(result["validation_passed"], result)
        self.assertEqual(result["page_count"], 1)
        self.assertTrue(result["checks"]["docx_uses_required_font"])
        self.assertTrue(result["checks"]["docx_font_sizes_within_range"])
        self.assertTrue(result["checks"]["pdf_uses_required_fonts"])
        self.assertFalse(result["ready_for_external_use"])
        for key in ("docx", "pdf", "extracted", "preview", "qa"):
            self.assertTrue(Path(result["artifacts"][key]).exists(), key)
        qa_path = Path(result["artifacts"]["qa"])
        qa = json.loads(qa_path.read_text(encoding="utf-8"))
        self.assertTrue((qa_path.parent / qa["extracted_text"]).exists())
        self.assertTrue(all((qa_path.parent / path).exists() for path in qa["previews"]))
        self.assertTrue(all(font.startswith("JetBrainsMono") for font in qa["pdf_fonts"]))

        revalidated = json.loads(self.tools.validate_artifacts({
            "source_markdown": str(self.source),
            "docx_path": result["artifacts"]["docx"],
            "pdf_path": result["artifacts"]["pdf"],
        }))
        self.assertTrue(revalidated["success"], revalidated)
        self.assertTrue(revalidated["validation_passed"], revalidated)
        self.assertEqual(revalidated["preview_count"], 1)
        self.assertFalse(revalidated["preview_artifacts_persisted"])

        second = self.render()
        self.assertFalse(second["success"])
        self.assertIn("overwrite", second["error"].lower())

    def test_cover_letter_render_is_one_page_and_font_checked(self) -> None:
        cover_source = self.packet / "source" / "cover_letter.md"
        cover_source.write_text(COVER_LETTER, encoding="utf-8")
        result = json.loads(self.tools.render_approved({
            "source_markdown": str(cover_source),
            "document_slug": "test_cover_letter",
            "version": 1,
        }))
        self.assertTrue(result["success"], result)
        self.assertTrue(result["validation_passed"], result)
        self.assertEqual(result["page_count"], 1)
        self.assertTrue(result["checks"]["docx_uses_required_font"])
        self.assertTrue(result["checks"]["docx_font_sizes_within_range"])
        qa = json.loads(Path(result["artifacts"]["qa"]).read_text(encoding="utf-8"))
        self.assertEqual(qa["approval"]["document_type"], "cover_letter")
        self.assertEqual(qa["page_limit"], 1)
        self.assertEqual(qa["font_standard"]["family"], "JetBrainsMono NF")

    def test_missing_required_font_blocks_render(self) -> None:
        with mock.patch.object(
            self.tools,
            "_required_font_available",
            return_value=(False, "font missing for test"),
        ):
            result = self.render()
        self.assertFalse(result["success"])
        self.assertIn("ask the human decision owner", result["error"])
        self.assertIn("font missing", result["font_check"])

    def test_requires_human_approval(self) -> None:
        self.source.write_text(APPROVED.replace("approved_by: Human Reviewer", "approved_by: null"), encoding="utf-8")
        result = self.render()
        self.assertFalse(result["success"])
        self.assertIn("approved_by", result["error"])

    def test_rejects_invalid_approval_date(self) -> None:
        self.source.write_text(APPROVED.replace("2026-08-25", "2026-02-30"), encoding="utf-8")
        result = self.render()
        self.assertFalse(result["success"])
        self.assertIn("approved_at", result["error"])

    def test_refuses_outputs_symlink_escape(self) -> None:
        outside = Path(self.temp.name) / "outside"
        outside.mkdir()
        (self.packet / "outputs").symlink_to(outside, target_is_directory=True)
        result = self.render()
        self.assertFalse(result["success"])
        self.assertIn("symlink", result["error"].lower())

    def test_authorized_layout_revision_edits_existing_version(self) -> None:
        result = self.render()
        docx_path = Path(result["artifacts"]["docx"])
        original_hash = self.tools._sha256(docx_path)

        revised = json.loads(self.tools.revise_layout({
            "source_markdown": str(self.source),
            "docx_path": str(docx_path),
            "operation": "page_break_before",
            "anchor_text": "Builder | Example Company",
            "human_authorized": True,
        }))
        self.assertTrue(revised["success"], revised)
        self.assertTrue(revised["validation_passed"], revised)
        self.assertEqual(revised["artifacts"]["docx"], str(docx_path))
        self.assertNotEqual(self.tools._sha256(docx_path), original_hash)
        qa = json.loads(Path(revised["artifacts"]["qa"]).read_text(encoding="utf-8"))
        self.assertEqual(qa["layout_revision"]["operation"], "page_break_before")
        self.assertEqual(qa["layout_revision"]["anchor_text"], "Builder | Example Company")
        self.assertTrue(qa["validation_passed"])

    def test_layout_revision_requires_explicit_authorization(self) -> None:
        result = self.render()
        docx_path = Path(result["artifacts"]["docx"])
        original_hash = self.tools._sha256(docx_path)
        revised = json.loads(self.tools.revise_layout({
            "source_markdown": str(self.source),
            "docx_path": str(docx_path),
            "operation": "page_break_before",
            "anchor_text": "Builder | Example Company",
            "human_authorized": False,
        }))
        self.assertFalse(revised["success"])
        self.assertEqual(self.tools._sha256(docx_path), original_hash)

    def test_failed_layout_qa_preserves_original_artifacts(self) -> None:
        result = self.render()
        artifacts = {
            key: Path(value)
            for key, value in result["artifacts"].items()
            if key in {"docx", "pdf", "qa"}
        }
        original_hashes = {key: self.tools._sha256(path) for key, path in artifacts.items()}
        with mock.patch.object(
            self.tools,
            "_qa",
            return_value={
                "validation_passed": False,
                "checks": {"forced_failure": False},
                "page_count": 1,
            },
        ):
            revised = json.loads(self.tools.revise_layout({
                "source_markdown": str(self.source),
                "docx_path": str(artifacts["docx"]),
                "operation": "page_break_before",
                "anchor_text": "Builder | Example Company",
                "human_authorized": True,
            }))
        self.assertFalse(revised["success"])
        self.assertIn("preserved", revised["error"])
        self.assertEqual(
            {key: self.tools._sha256(path) for key, path in artifacts.items()},
            original_hashes,
        )

    def test_refuses_path_outside_packet(self) -> None:
        outside = self.root / "unrelated_notes" / "resume.md"
        outside.parent.mkdir(parents=True)
        outside.write_text(APPROVED, encoding="utf-8")
        result = json.loads(self.tools.render_approved({
            "source_markdown": str(outside),
            "document_slug": "test_resume",
            "version": 1,
        }))
        self.assertFalse(result["success"])
        self.assertIn("workspace applications/ or resumes/", result["error"])


if __name__ == "__main__":
    unittest.main()
