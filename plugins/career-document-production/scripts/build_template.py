"""Build the controlled ATS-safe DOCX career-document template."""
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "templates" / "resume_template.docx"
FONT = "JetBrainsMono NF"
MIN_FONT_PT = 9.0
MAX_FONT_PT = 12.0


def font(style, points: float, bold: bool = False) -> None:
    if not MIN_FONT_PT <= points <= MAX_FONT_PT:
        raise ValueError(f"Font size {points} is outside {MIN_FONT_PT}-{MAX_FONT_PT} pt")
    style.font.name = FONT
    style.font.size = Pt(points)
    style.font.bold = bold
    fonts = style.element.get_or_add_rPr().rFonts
    for key in ("ascii", "hAnsi", "eastAsia", "cs"):
        fonts.set(qn(f"w:{key}"), FONT)


def paragraph(style, *, before: float = 0, after: float = 0, keep_next: bool = False) -> None:
    fmt = style.paragraph_format
    fmt.space_before = Pt(before)
    fmt.space_after = Pt(after)
    fmt.line_spacing_rule = WD_LINE_SPACING.SINGLE
    fmt.keep_with_next = keep_next
    fmt.widow_control = True


def main() -> None:
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Inches(0.55)
    section.bottom_margin = Inches(0.55)
    section.left_margin = Inches(0.65)
    section.right_margin = Inches(0.65)

    styles = doc.styles

    body = styles.add_style("Resume Body", WD_STYLE_TYPE.PARAGRAPH)
    font(body, 9.5)
    paragraph(body, after=3)

    name = styles.add_style("Resume Name", WD_STYLE_TYPE.PARAGRAPH)
    font(name, 12, bold=True)
    paragraph(name, after=1, keep_next=True)
    name.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

    contact = styles.add_style("Resume Contact", WD_STYLE_TYPE.PARAGRAPH)
    font(contact, 9)
    paragraph(contact, after=2, keep_next=True)
    contact.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

    section_style = styles.add_style("Resume Section", WD_STYLE_TYPE.PARAGRAPH)
    font(section_style, 10.5, bold=True)
    paragraph(section_style, before=7, after=2, keep_next=True)
    ppr = section_style.element.get_or_add_pPr()
    borders = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "4")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "666666")
    borders.append(bottom)
    ppr.append(borders)

    entry = styles.add_style("Resume Entry", WD_STYLE_TYPE.PARAGRAPH)
    font(entry, 9.5, bold=True)
    paragraph(entry, before=4, after=1, keep_next=True)

    bullet = styles.add_style("Resume Bullet", WD_STYLE_TYPE.PARAGRAPH)
    font(bullet, 9.5)
    paragraph(bullet, after=1.5)
    bullet.paragraph_format.left_indent = Inches(0.2)
    bullet.paragraph_format.first_line_indent = Inches(-0.15)

    cover_header = styles.add_style("Cover Letter Header", WD_STYLE_TYPE.PARAGRAPH)
    font(cover_header, 9.5)
    paragraph(cover_header, after=0)

    cover_subject = styles.add_style("Cover Letter Subject", WD_STYLE_TYPE.PARAGRAPH)
    font(cover_subject, 10, bold=True)
    paragraph(cover_subject, before=3, after=6, keep_next=True)

    cover_body = styles.add_style("Cover Letter Body", WD_STYLE_TYPE.PARAGRAPH)
    font(cover_body, 10)
    paragraph(cover_body, after=6)

    # The template carries styles and page geometry only; content comes from approved Markdown.
    first = doc.add_paragraph(style=body)
    first.text = ""
    doc.core_properties.title = "Controlled ATS-safe career document template"
    doc.core_properties.author = ""
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    main()
