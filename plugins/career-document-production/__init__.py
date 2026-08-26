"""Register bounded career-document production tools for Hermes Job Hunter."""

from __future__ import annotations

from typing import Any

from . import schemas, tools


def register(ctx: Any) -> None:
    ctx.register_tool(
        name="resume_render_approved",
        toolset="resume_production",
        schema=schemas.RENDER_APPROVED,
        handler=tools.render_approved,
        check_fn=tools.available,
    )
    ctx.register_tool(
        name="resume_validate_artifacts",
        toolset="resume_production",
        schema=schemas.VALIDATE_ARTIFACTS,
        handler=tools.validate_artifacts,
        check_fn=tools.available,
    )
    ctx.register_tool(
        name="resume_revise_layout",
        toolset="resume_production",
        schema=schemas.REVISE_LAYOUT,
        handler=tools.revise_layout,
        check_fn=tools.available,
    )
