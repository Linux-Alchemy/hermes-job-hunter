"""Schemas exposed by the Hermes Job Hunter career-document production plugin."""

RENDER_APPROVED = {
    "name": "resume_render_approved",
    "description": (
        "Render an APPROVED_MARKDOWN resume or cover-letter source inside a bounded private career packet "
        "to DOCX and PDF using the controlled font standard, then run structural, text, font, size, "
        "and page-preview validation. Refuses unapproved sources, a missing required font, paths outside "
        "the active profile workspace's resumes/ or applications/ lanes, and overwriting an existing version."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "source_markdown": {
                "type": "string",
                "description": "Absolute path to the approved Markdown source under the packet's source/ directory.",
            },
            "document_slug": {
                "type": "string",
                "description": "Snake-case output stem, for example candidate_example_resume or candidate_example_cover_letter.",
            },
            "version": {
                "type": "integer",
                "minimum": 1,
                "description": "Version number for this rendered artifact. Fresh renders cannot overwrite an existing version; authorised layout revision uses resume_revise_layout.",
            },
        },
        "required": ["source_markdown", "document_slug", "version"],
    },
}

VALIDATE_ARTIFACTS = {
    "name": "resume_validate_artifacts",
    "description": (
        "Revalidate an existing career-document DOCX/PDF pair against its approved Markdown source. "
        "Use after a renderer run or authorised layout-only DOCX template adjustment."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "source_markdown": {"type": "string"},
            "docx_path": {"type": "string"},
            "pdf_path": {"type": "string"},
        },
        "required": ["source_markdown", "docx_path", "pdf_path"],
    },
}

REVISE_LAYOUT = {
    "name": "resume_revise_layout",
    "description": (
        "Apply an authorised layout-only revision to an existing rendered career-document DOCX, "
        "regenerate its PDF and QA artifacts in place, and preserve the approved Markdown text. "
        "Use for working renders that are not yet approved for external use; it cannot edit wording."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "source_markdown": {
                "type": "string",
                "description": "Absolute path to the approved Markdown source for this rendered artifact.",
            },
            "docx_path": {
                "type": "string",
                "description": "Existing rendered DOCX under the same packet's outputs/ directory.",
            },
            "operation": {
                "type": "string",
                "enum": ["page_break_before", "remove_page_break_before", "keep_block_together"],
                "description": "Bounded layout operation to apply to the paragraph identified by anchor_text.",
            },
            "anchor_text": {
                "type": "string",
                "description": "Exact visible paragraph text, such as a role heading. Must match exactly once.",
            },
            "human_authorized": {
                "type": "boolean",
                "description": "Must be true only when the human decision owner explicitly requested this layout revision.",
            },
        },
        "required": ["source_markdown", "docx_path", "operation", "anchor_text", "human_authorized"],
    },
}
