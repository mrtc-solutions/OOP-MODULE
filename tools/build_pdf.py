"""
Build the Week 1 PDF module (Exploits University, BICT 3202 OOAD).
"""
import os
import re
from PIL import Image as PILImage

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Image, Table, TableStyle, PageBreak,
                                NextPageTemplate, KeepTogether, HRFlowable)
from reportlab.platypus.tableofcontents import TableOfContents

from common import (ROOT, BRAND, VISUALS, FONTS, OUTPUT, MAROON, MAROON_DARK,
                    MAROON_SOFT, MAROON_TINT, GOLD, GOLD_LIGHT, CREAM, CREAM_2,
                    INK, GREY)

PAGE_W, PAGE_H = A4
MARGIN = 0.9 * inch
DOC_W = PAGE_W - 2 * MARGIN

# --------------------------------------------------------------------------
# fonts
# --------------------------------------------------------------------------
def _reg():
    pdfmetrics.registerFont(TTFont("Poppins", os.path.join(FONTS, "Poppins-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("Poppins-SemiBold", os.path.join(FONTS, "Poppins-SemiBold.ttf")))
    pdfmetrics.registerFont(TTFont("Poppins-Bold", os.path.join(FONTS, "Poppins-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("Poppins-ExtraBold", os.path.join(FONTS, "Poppins-ExtraBold.ttf")))
    pdfmetrics.registerFont(TTFont("OpenSans", os.path.join(FONTS, "OpenSans-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("OpenSans-SemiBold", os.path.join(FONTS, "OpenSans-SemiBold.ttf")))
    pdfmetrics.registerFont(TTFont("OpenSans-Bold", os.path.join(FONTS, "OpenSans-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("OpenSans-Italic", os.path.join(FONTS, "OpenSans-Italic.ttf")))
    pdfmetrics.registerFont(TTFont("Mono", os.path.join(FONTS, "DejaVuSansMono.ttf")))
    pdfmetrics.registerFontFamily("OpenSans", normal="OpenSans", bold="OpenSans-Bold",
                                  italic="OpenSans-Italic", boldItalic="OpenSans-Bold")
    pdfmetrics.registerFontFamily("Poppins", normal="Poppins", bold="Poppins-Bold",
                                  italic="Poppins", boldItalic="Poppins-Bold")

_reg()

def _slug(s):
    s = re.sub(r"[^A-Za-z0-9]+", "-", s.strip().lower()).strip("-")
    return s or "section"

# --------------------------------------------------------------------------
# palette as hex strings for Paragraph markup
# --------------------------------------------------------------------------
C_MAROON, C_DARK, C_SOFT, C_GOLD, C_GOLD_L, C_INK, C_GREY, C_CREAM = (
    "#7B1113", "#59090C", "#A94442", "#C9A227", "#E4C97C", "#2B2626", "#6B6B6B", "#FAF6EC")

# --------------------------------------------------------------------------
# styles
# --------------------------------------------------------------------------
S = {}
S["body"] = ParagraphStyle("body", fontName="OpenSans", fontSize=10.5, leading=15.5,
                           textColor=C_INK, alignment=TA_JUSTIFY, spaceAfter=6)
S["bodyL"] = ParagraphStyle("bodyL", parent=S["body"], alignment=TA_LEFT)
S["bullet"] = ParagraphStyle("bullet", parent=S["bodyL"], leftIndent=14, bulletIndent=4,
                             spaceAfter=3)
S["H1"] = ParagraphStyle("H1", fontName="Poppins-Bold", fontSize=14.5, leading=19,
                         textColor=HexColor(C_CREAM), backColor=HexColor(C_MAROON),
                         borderPadding=(7, 10, 7, 10), spaceBefore=20, spaceAfter=10,
                         keepWithNext=1)
S["H2"] = ParagraphStyle("H2", fontName="Poppins-SemiBold", fontSize=12.5, leading=16,
                         textColor=C_MAROON, spaceBefore=13, spaceAfter=4, keepWithNext=1)
S["H3"] = ParagraphStyle("H3", fontName="Poppins-SemiBold", fontSize=11, leading=14,
                         textColor=C_SOFT, spaceBefore=9, spaceAfter=3, keepWithNext=1)
S["caption"] = ParagraphStyle("caption", fontName="OpenSans-Italic", fontSize=8.5,
                              leading=11, textColor=C_GREY, alignment=TA_CENTER,
                              spaceBefore=3, spaceAfter=10)
S["callout"] = ParagraphStyle("callout", parent=S["bodyL"], spaceAfter=2)
S["mono"] = ParagraphStyle("mono", fontName="Mono", fontSize=9.5, leading=13.5,
                           textColor=C_DARK, alignment=TA_LEFT, spaceAfter=6)
S["toc"] = ParagraphStyle("toc", fontName="OpenSans", fontSize=10.5, leading=17,
                          textColor=C_INK, leftIndent=6)

GOLD_RULE = HRFlowable(width="100%", thickness=1.4, color=HexColor(C_GOLD),
                       spaceBefore=0, spaceAfter=10)

# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def H1(text):
    return Paragraph(text, S["H1"])

def H2(text):
    return Paragraph(text, S["H2"])

def H3(text):
    return Paragraph(text, S["H3"])

def P(text, style="body"):
    return Paragraph(text, S[style])

def BUL(items):
    return [Paragraph(f"<bullet>&bull;</bullet>{i}", S["bullet"]) for i in items]

def CAP(text):
    return Paragraph(text, S["caption"])

def _img(name, width):
    path = os.path.join(VISUALS, name)
    with PILImage.open(path) as im:
        w_px, h_px = im.size
    height = width * h_px / w_px
    img = Image(path, width=width, height=height)
    img.hAlign = "CENTER"
    return img

def FIG(name, caption=None, width=DOC_W):
    if caption:
        return [_img(name, width), CAP(caption)]
    return [_img(name, width)]

def TWO_FIG(n1, n2, c1=None, c2=None, width=DOC_W):
    gap = 10
    w = (width - gap) / 2.0
    i1 = _img(n1, w)
    i2 = _img(n2, w)
    t = Table([[i1, i2]], colWidths=[w, w + gap])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    out = [t]
    if c1 and c2:
        out.append(CAP(f"{c1}    |    {c2}"))
    return out

def CALLOUT(title, body_lines, bg=HexColor("#F3E4E4"), bar=C_GOLD, tcol=C_MAROON):
    inner = [Paragraph(f'<font name="Poppins-SemiBold" size="9" color="{tcol}">{title}</font>', S["bodyL"])]
    for line in body_lines:
        inner.append(Paragraph(line, S["callout"]))
    t = Table([[inner]], colWidths=[DOC_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 3, HexColor(bar)),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return t

def DTABLE(headers, rows, widths=None, aligns=None):
    if widths is None:
        widths = [DOC_W / len(headers)] * len(headers)
    hcell = [Paragraph(f'<font name="Poppins-SemiBold" size="9.5" color="{C_CREAM}">{h}</font>',
                       S["bodyL"]) for h in headers]
    data = [hcell]
    for r in rows:
        cells = []
        for j, c in enumerate(r):
            cells.append(Paragraph(f'<font name="OpenSans" size="9.5" color="{C_INK}">{c}</font>',
                                   S["bodyL"]))
        data.append(cells)
    t = Table(data, colWidths=widths, repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), HexColor(C_MAROON)),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#E3D8C8")),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            style.append(("BACKGROUND", (0, i), (-1, i), HexColor(CREAM_2)))
    t.setStyle(TableStyle(style))
    return t

# --------------------------------------------------------------------------
# NumberedCanvas (Page X of Y)
# --------------------------------------------------------------------------
from reportlab.pdfgen import canvas as _canvas_mod

class NumberedCanvas(_canvas_mod.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved = []

    def showPage(self):
        self._saved.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._saved)
        for state in self._saved:
            self.__dict__.update(state)
            self._draw_footer(total)
            super().showPage()
        super().save()

    def _draw_footer(self, total):
        self.setFont("OpenSans", 7.5)
        self.setFillColor(HexColor(C_GREY))
        self.drawRightString(PAGE_W - MARGIN, 0.45 * inch, f"Page {self._pageNumber} of {total}")

# --------------------------------------------------------------------------
# document template with cover + body frames and header/footer
# --------------------------------------------------------------------------
class WeekDoc(BaseDocTemplate):
    def __init__(self, filename, cover_cb, **kw):
        super().__init__(filename, pagesize=A4, **kw)
        self._cover_cb = cover_cb
        self._toc_counter = 0
        cover_frame = Frame(0, 0, PAGE_W, PAGE_H, id="cover")
        body_frame = Frame(MARGIN, MARGIN, DOC_W, PAGE_H - 2 * MARGIN, id="body",
                           leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="Cover", frames=[cover_frame], onPage=self._draw_cover),
            PageTemplate(id="Body", frames=[body_frame], onPage=self._draw_header_footer),
        ])

    def _draw_cover(self, canv, doc):
        self._cover_cb(canv)

    def _draw_header_footer(self, canv, doc):
        canv.saveState()
        # header
        shield = os.path.join(BRAND, "eu_shield.png")
        canv.drawImage(shield, MARGIN, PAGE_H - 0.78 * inch, 0.42 * inch, 0.42 * inch,
                       mask="auto", preserveAspectRatio=True)
        canv.setFont("Poppins-SemiBold", 11)
        canv.setFillColor(HexColor(C_MAROON))
        canv.drawString(MARGIN + 0.52 * inch, PAGE_H - 0.60 * inch, "EXPLOITS UNIVERSITY")
        canv.setFont("OpenSans", 8)
        canv.setFillColor(HexColor(C_GREY))
        canv.drawString(MARGIN + 0.52 * inch, PAGE_H - 0.76 * inch,
                        "BICT 3202 — Object-Oriented Analysis and Design")
        canv.setFont("OpenSans-SemiBold", 8.5)
        canv.setFillColor(HexColor(C_SOFT))
        canv.drawRightString(PAGE_W - MARGIN, PAGE_H - 0.66 * inch, "Week 1 of 16")
        canv.setStrokeColor(HexColor(C_GOLD))
        canv.setLineWidth(1.2)
        canv.line(MARGIN, PAGE_H - 0.90 * inch, PAGE_W - MARGIN, PAGE_H - 0.90 * inch)
        # footer
        canv.setFont("OpenSans", 7.5)
        canv.setFillColor(HexColor(C_GREY))
        canv.drawString(MARGIN, 0.45 * inch,
                        "© Exploits University — BICT 3202 Object-Oriented Analysis and Design")
        canv.setStrokeColor(HexColor("#E3D8C8"))
        canv.setLineWidth(0.5)
        canv.line(MARGIN, 0.62 * inch, PAGE_W - MARGIN, 0.62 * inch)
        canv.restoreState()

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            st = flowable.style.name
            if st == "H1":
                text = flowable.getPlainText()
                if text.strip().lower() == "contents":
                    return
                key = "h1-" + _slug(text)
                self.canv.bookmarkPage(key)
                self.canv.addOutlineEntry(text, key, 0, 0)
                self.notify("TOCEntry", (0, text, self.page, key))

# --------------------------------------------------------------------------
# cover drawing
# --------------------------------------------------------------------------
def draw_cover(canv):
    w, h = PAGE_W, PAGE_H
    # full maroon background
    canv.setFillColor(HexColor(C_MAROON))
    canv.rect(0, 0, w, h, stroke=0, fill=1)
    # subtle darker band at bottom
    canv.setFillColor(HexColor(C_DARK))
    canv.rect(0, 0, w, 1.6 * inch, stroke=0, fill=1)
    # gold frame
    canv.setStrokeColor(HexColor(C_GOLD))
    canv.setLineWidth(2)
    canv.rect(0.42 * inch, 0.42 * inch, w - 0.84 * inch, h - 0.84 * inch, stroke=1, fill=0)
    canv.setLineWidth(0.8)
    canv.rect(0.52 * inch, 0.52 * inch, w - 1.04 * inch, h - 1.04 * inch, stroke=1, fill=0)

    # seal
    seal = os.path.join(BRAND, "eu_seal.png")
    canv.drawImage(seal, w / 2 - 1.05 * inch, h - 3.55 * inch, 2.1 * inch, 2.1 * inch,
                   mask="auto")

    # university name
    canv.setFillColor(HexColor(C_GOLD_L))
    canv.setFont("Poppins-Bold", 30)
    canv.drawCentredString(w / 2, h - 4.05 * inch, "EXPLOITS UNIVERSITY")
    canv.setFont("OpenSans-SemiBold", 12.5)
    canv.setFillColor(HexColor(C_CREAM))
    canv.drawCentredString(w / 2, h - 4.48 * inch, "BSc INFORMATION COMMUNICATION AND TECHNOLOGY")

    # course
    canv.setFillColor(HexColor(C_GOLD))
    canv.setFont("Poppins-SemiBold", 15)
    canv.drawCentredString(w / 2, h - 5.05 * inch, "BICT 3202 · OBJECT-ORIENTED ANALYSIS AND DESIGN")

    # week
    canv.setFillColor(HexColor(C_CREAM))
    canv.setFont("Poppins-ExtraBold", 40)
    canv.drawCentredString(w / 2, h - 5.85 * inch, "WEEK 1")
    canv.setFont("Poppins-SemiBold", 15)
    canv.drawCentredString(w / 2, h - 6.35 * inch,
                           "Business Needs, Software Needs and Object Technology for Business")

    # meta box
    bx, by, bw_, bh_ = 1.1 * inch, 1.95 * inch, w - 2.2 * inch, 1.75 * inch
    canv.setFillColor(HexColor(C_DARK))
    canv.setStrokeColor(HexColor(C_GOLD))
    canv.setLineWidth(1.2)
    canv.roundRect(bx, by, bw_, bh_, 10, stroke=1, fill=1)
    meta = [
        ("Programme", "BSc Information Communication and Technology"),
        ("Course Code / Year", "BICT 3202 · Year 3"),
        ("Lecturer", "Francis Fweta — ICT Lecturer"),
        ("Delivery", "2h Lecture · 1h Tutorial · 1h Practical · 10h Independent Learning"),
    ]
    yy = by + bh_ - 0.42 * inch
    for k, v in meta:
        canv.setFillColor(HexColor(C_GOLD))
        canv.setFont("Poppins-SemiBold", 9)
        canv.drawString(bx + 0.3 * inch, yy, k.upper())
        canv.setFillColor(HexColor(C_CREAM))
        canv.setFont("OpenSans", 10)
        canv.drawString(bx + 2.35 * inch, yy, v)
        yy -= 0.36 * inch

    canv.setFillColor(HexColor(C_CREAM))
    canv.setFont("OpenSans-Italic", 9.5)
    canv.drawCentredString(w / 2, by - 0.42 * inch,
                           "Prepared by Francis Fweta  ·  Exploits University  ·  Week 1 of 16")


# --------------------------------------------------------------------------
# build
# --------------------------------------------------------------------------
def build():
    out = os.path.join(OUTPUT, "week1")
    os.makedirs(out, exist_ok=True)
    pdf_path = os.path.join(out, "Week1_Module_BICT3202_OOAD.pdf")

    story = []
    toc = TableOfContents()
    toc.levelStyles = [S["toc"]]
    story.append(NextPageTemplate("Body"))
    story.append(PageBreak())
    story.append(H1("Contents"))
    story.append(toc)
    story.append(PageBreak())

    # 1. overview -----------------------------------------------------------
    story.append(H1("1.  Week 1 Overview"))
    story += [P("This week covers the first three topics listed under the module's Topics of Study: "
                "<b>Business Needs</b>, <b>Aspects of Business Software Needs</b> and "
                "<b>Object Technology for Business</b>."),
              P("These topics are deliberately placed at the beginning of OOAD. Before students can "
                "create classes, objects, use cases or UML diagrams, they must first understand "
                "<b>why</b> an organisation needs software and <b>what problem</b> the software is "
                "supposed to solve.")]
    story.append(CALLOUT("COMMON MISCONCEPTION",
        ["“Object-Oriented Analysis and Design starts by drawing a class diagram.” — <b>It does not.</b>",
         "A good OOAD process starts by understanding the problem, business objectives, stakeholders "
         "and requirements. Requirements engineering — discovering, analysing, documenting, validating "
         "and managing what a system must accomplish — follows ISO/IEC/IEEE 29148:2018, the current "
         "published edition as of 2026."]))
    story += [Spacer(1, 6)] + FIG("journey.png",
        "Figure 1 — The logical journey: business problem → business need → software need → requirements → analysis → models → design → implementation")

    # 2. learning outcomes ----------------------------------------------------
    story.append(H1("2.  Learning Outcomes"))
    story += [P("By the end of this week, students should be able to:")]
    story += BUL([
        "Define a business need.",
        "Explain why organisations develop or acquire software systems.",
        "Distinguish between a business problem, a business need, a requirement and a software solution.",
        "Identify stakeholders associated with a business system.",
        "Explain functional and non-functional software needs.",
        "Explain the relationship between business objectives and software requirements.",
        "Describe the basic idea behind object technology and explain what an object is.",
        "Explain the relationship between objects, state and behaviour.",
        "Explain why real-world entities are useful when analysing software systems.",
        "Describe major advantages and limitations of object-oriented approaches.",
        "Apply these concepts to a simple real-world business case.",
    ])

    # 3. introduction ----------------------------------------------------------
    story.append(H1("3.  Introduction: Why Do We Need OOAD?"))
    story += [P("Imagine that a university tells a software developer: “We need a new student "
                "management system.” The developer immediately starts programming — a login page, a "
                "student table, a lecturer table, a payment page, an examination page and a dashboard."),
              P("After six months the university tests the system and says: “This isn't what we asked "
                "for.” The developer replies: “But you told us to build a student management system.” "
                "The university responds: “Yes, but students should register courses <b>before</b> "
                "paying fees. Lecturers should approve registration. Students should only register for "
                "courses offered by their programme. Finance should see outstanding balances. Students "
                "should receive notifications. And we need to prevent registration if prerequisites "
                "haven't been met.”")]
    story.append(CALLOUT("THE LESSON",
        ["The problem was not programming ability — it was <b>insufficient analysis of the business "
         "needs before designing the software</b>. This is one of the fundamental reasons OOAD exists."]))
    story += FIG("chart_failure_reasons.png",
        "Figure 2 — Illustrative survey pattern: incomplete or misunderstood requirements are the leading contributor to troubled software projects")

    # 4. business needs --------------------------------------------------------
    story.append(H1("4.  Business Needs"))
    story.append(H2("4.1  What is a Business Need?"))
    story += [P("A business need is a problem, opportunity, objective or desired improvement that an "
                "organisation must address in order to achieve its goals.")]
    story.append(CALLOUT("IN SIMPLE LANGUAGE", ["A business need explains <b>why</b> an organisation needs to change something."]))
    story += [P("For example, a university currently records student registration using paper forms and "
                "students spend hours waiting in queues. The university therefore identifies a need: "
                "<i>“Reduce the time required for student registration and improve the accuracy of "
                "registration records.”</i>"),
              P("Notice that the business need is <b>not yet software</b>. The university has not said "
                "“We need a Java application” — it has identified a business problem and a desired improvement.")]

    story.append(H2("4.2  Business Problem vs Business Need"))
    story += [P("A <b>business problem</b> describes an undesirable current situation. A <b>business "
                "need</b> describes what the organisation must achieve or improve in response to that "
                "situation.")]
    story += FIG("problem_need_solution.png", "Figure 3 — Problem, need and solution are three distinct ideas")

    story.append(H2("4.3  Business Needs Are Not Automatically Software Needs"))
    story += [P("Suppose a hospital says: “Patients wait too long before seeing a doctor.” Is the "
                "solution automatically “build hospital software”? No. There could be several causes — "
                "too few doctors, patients incorrectly assigned to queues, slow registration, hard-to-locate "
                "patient files, inefficient scheduling, or emergency cases mixed with normal appointments."),
              P("Software may solve <b>some</b> of these problems, but not necessarily all of them. An "
                "analyst must investigate the underlying business problem before proposing technology.")]

    story.append(H2("4.4  Business Objectives"))
    story += [P("A business objective is a specific result that an organisation wants to achieve. Examples "
                "include: increase sales, reduce operating costs, improve customer satisfaction, reduce "
                "processing time, improve data accuracy, comply with regulations, increase security, expand "
                "services, and improve decision-making.")]
    story.append(CALLOUT("EXAMPLE — BANK",
        ["Objective: <i>reduce the average time to open a customer account from 45 minutes to 10 minutes.</i>",
         "That objective leads to a business need (a faster account-opening process), which leads to software "
         "requirements: customers submit information electronically, staff verify identity digitally, the system "
         "validates required information, and the system notifies customers about application status."]))

    story.append(H2("4.5  The Business-to-Software Chain"))
    story += [P("This chain is the backbone of the entire 16-week module:"),
              Paragraph("BUSINESS OBJECTIVE<br/>"
                        "&nbsp;&nbsp;&nbsp;&nbsp;↓<br/>"
                        "BUSINESS PROBLEM / OPPORTUNITY<br/>"
                        "&nbsp;&nbsp;&nbsp;&nbsp;↓<br/>"
                        "BUSINESS NEED<br/>"
                        "&nbsp;&nbsp;&nbsp;&nbsp;↓<br/>"
                        "STAKEHOLDER NEEDS<br/>"
                        "&nbsp;&nbsp;&nbsp;&nbsp;↓<br/>"
                        "SYSTEM / SOFTWARE REQUIREMENTS<br/>"
                        "&nbsp;&nbsp;&nbsp;&nbsp;↓<br/>"
                        "ANALYSIS MODELS<br/>"
                        "&nbsp;&nbsp;&nbsp;&nbsp;↓<br/>"
                        "DESIGN<br/>"
                        "&nbsp;&nbsp;&nbsp;&nbsp;↓<br/>"
                        "IMPLEMENTATION", S["mono"])]

    # 5. stakeholders ----------------------------------------------------------
    story.append(H1("5.  Stakeholders"))
    story.append(H2("5.1  What is a Stakeholder?"))
    story += [P("A stakeholder is a person, group or organisation that has an interest in, is affected by, "
                "influences, or interacts with a system."),
              P("For a university registration system, possible stakeholders include: students, lecturers, "
                "registry officers, finance officers, department heads, administrators, ICT staff, university "
                "management and external regulators."),
              P("Not every stakeholder necessarily uses the software directly — the Vice Chancellor may never "
                "log into the registration system but is still affected by its performance and reports.")]
    story.append(H2("5.2  Primary and Secondary Stakeholders"))
    story += [P("<b>Primary stakeholders</b> directly interact with the system or are directly affected by it "
                "(Student, Lecturer, Registrar, Finance Officer). <b>Secondary stakeholders</b> may not directly "
                "use the system but have an interest in its outcomes (University Management, Auditors, Regulators, "
                "ICT Administrators).")]
    story += FIG("stakeholders.png", "Figure 4 — Stakeholder map for a student registration system")
    story.append(H2("5.3  Why Stakeholders Matter in OOAD"))
    story += [P("If developers interview only students, they hear “We need online registration.” But Finance "
                "might say “Students with outstanding fees must not register,” Registry might say “Students must "
                "meet programme requirements,” Lecturers might say “Some courses require approval,” ICT might say "
                "“Only authorised staff access administration,” and Management might say “We need registration "
                "statistics reports.”")]
    story.append(CALLOUT("KEY POINT", ["If the analyst ignores stakeholders, <b>important requirements will be missed</b>."]))
    story.append(DTABLE(
        ["Stakeholder", "Interest / Need"],
        [["Student", "Register courses"],
         ["Lecturer", "Approve or monitor registration"],
         ["Registrar", "Maintain academic registration records"],
         ["Finance Officer", "Verify financial eligibility"],
         ["Department Head", "Monitor programme registration"],
         ["ICT Administrator", "Maintain system and security"],
         ["Management", "Obtain reports"]],
        widths=[0.5 * DOC_W, 0.5 * DOC_W]))

    # 6. aspects of software needs -------------------------------------------
    story.append(H1("6.  Aspects of Business Software Needs"))
    story += [P("A business does not simply need “software” — it usually needs software that satisfies "
                "<b>several categories</b> of needs. The most important distinction is functional versus "
                "non-functional needs.")]
    story += FIG("aspects_overview.png", "Figure 5 — Four aspects of a complete software need")

    story.append(H2("6.1  Functional Software Needs"))
    story += [P("A functional requirement describes <b>what the system should do</b> — think "
                "<b>FUNCTION = ACTION</b>. Examples: register students, calculate fees, generate invoices, "
                "send notifications, reset passwords, generate examination reports.")]
    story.append(CALLOUT("EXAMPLE", ["For an online banking system: <i>“The system shall allow customers to transfer "
        "money between accounts.”</i> — a functional requirement because it describes something the system must do."]))
    story.append(H2("6.2  Non-Functional Software Needs"))
    story += [P("A non-functional requirement describes a <b>quality, constraint or condition</b> under which "
                "the system must operate — think <b>NON-FUNCTIONAL = HOW WELL / UNDER WHAT CONDITIONS</b>. "
                "Examples: security, performance, availability, usability, reliability, scalability, "
                "maintainability and accessibility.")]
    story += FIG("functional_nonfunctional.png", "Figure 6 — Functional (what) versus non-functional (how well)")
    story.append(H2("6.3  Functional vs Non-Functional — Comparison"))
    story.append(DTABLE(
        ["Aspect", "Functional Requirement", "Non-Functional Requirement"],
        [["Main question", "What must the system do?", "What quality / constraint must it satisfy?"],
         ["Example", "Register student", "Registration page loads within 2 seconds"],
         ["Example", "Generate invoice", "Invoice available 99.9% of the time"],
         ["Example", "Transfer money", "Transfers must be encrypted"],
         ["Example", "Search products", "Search results appear quickly"]],
        widths=[0.22 * DOC_W, 0.39 * DOC_W, 0.39 * DOC_W]))
    story += [Spacer(1, 2), P("<b>Easy memory trick:</b> Functional = behaviour · Non-functional = quality / constraint.")]
    story += FIG("chart_needs_mix.png", "Figure 7 — A complete requirement set captures functional, non-functional and rules/constraints")

    story.append(H2("6.4  Business Rules"))
    story += [P("A business rule is a policy, restriction or condition that governs how an organisation "
                "operates. The software must implement it. Examples:"),
              Paragraph("•  “A student may not register for a course unless the student has satisfied the course prerequisite.”<br/>"
                        "•  “A customer may withdraw a maximum of MWK 500,000 per day.”<br/>"
                        "•  “An employee cannot approve their own expense claim.”", S["bodyL"])]
    story.append(H2("6.5  Business Rule vs Functional Requirement"))
    story += [P("<b>Business rule:</b> “Students must pass BICT 2101 before registering for BICT 3202.”"),
              P("<b>Functional requirement:</b> “The system shall check whether a student has passed the "
                "prerequisite before allowing registration for BICT 3202.”"),
              P("The business rule comes from the organisation; the functional requirement describes what the "
                "software must do to enforce or support that rule.")]
    story.append(H2("6.6  Constraints"))
    story += [P("Software also operates under <b>constraints</b> — limitations that restrict the possible "
                "solution: available budget, existing hardware, legal requirements, organisational policies, "
                "required platform, integration with an existing database, internet availability, and the "
                "deployment environment.")]
    story.append(CALLOUT("EXAMPLE", ["“The new system must work with our existing student database.” — that is a constraint."]))
    story.append(H2("6.7  The Analyst's Job"))
    story += [P("An analyst does not simply ask “What software do you want?” Instead the analyst investigates:"),
              Paragraph("1. What problem exists?&nbsp;&nbsp;2. Why does it exist?&nbsp;&nbsp;3. Who is affected?<br/>"
                        "4. What does the organisation want to achieve?&nbsp;&nbsp;5. What processes currently exist?<br/>"
                        "6. What information is required?&nbsp;&nbsp;7. What rules govern the process?<br/>"
                        "8. What should the new system do?&nbsp;&nbsp;9. What constraints exist?<br/>"
                        "10. How will we know the solution is successful?", S["bodyL"])]
    story.append(H2("6.8  Requirements Elicitation"))
    story += [P("Requirements elicitation is the process of discovering and documenting stakeholder needs. "
                "ISO/IEC/IEEE 29148 describes it as using systematic techniques to proactively identify and "
                "document customer and end-user needs. Common techniques:"),
              Paragraph("1. <b>Interviews</b> — talk directly to stakeholders (“How do you currently register students?”)<br/>"
                        "2. <b>Questionnaires</b> — useful when many users must provide information<br/>"
                        "3. <b>Observation</b> — watch users perform their work<br/>"
                        "4. <b>Document analysis</b> — study forms, reports, policies, spreadsheets, databases, manuals<br/>"
                        "5. <b>Workshops</b> — stakeholders discuss requirements together<br/>"
                        "6. <b>Prototyping</b> — show a draft system and collect feedback", S["bodyL"])]
    story += FIG("elicitation.png", "Figure 8 — Six common requirements-elicitation techniques")

    story.append(H2("6.9  Worked Example: Student Registration"))
    story += [P("Suppose Exploits University wants a new registration system. The analyst works through seven steps:"),
              Paragraph("<b>Step 1 — Business problem:</b> registration is paper-based, slow, difficult to monitor and "
                        "vulnerable to data-entry errors.<br/>"
                        "<b>Step 2 — Business need:</b> a faster, more accurate and traceable registration process.<br/>"
                        "<b>Step 3 — Stakeholders:</b> students, lecturers, registry, finance, ICT, management.<br/>"
                        "<b>Step 4 — Functional requirements:</b> authenticate students, display available courses, check "
                        "prerequisites, register/remove courses, submit for approval, generate reports.<br/>"
                        "<b>Step 5 — Non-functional requirements:</b> protect student information, be available during "
                        "registration periods, respond quickly, support many simultaneous users, keep reliable records.<br/>"
                        "<b>Step 6 — Business rules:</b> “A student cannot register without satisfying the prerequisite.”<br/>"
                        "<b>Step 7 — Candidate objects:</b> Student, Course, Lecturer, Registration, Programme, Payment, "
                        "Department.", S["bodyL"])]
    story.append(CALLOUT("NOTE", ["We have not designed the classes yet — we are simply beginning to identify important "
        "concepts in the problem domain. That distinction becomes critical in later weeks."]))

    # 7. object technology -----------------------------------------------------
    story.append(H1("7.  Object Technology for Business"))
    story.append(H2("7.1  What is Object Technology?"))
    story += [P("Object technology is an approach to analysing, designing and developing systems around "
                "<b>objects and their relationships</b>. Instead of viewing a system as a collection of "
                "procedures, object-oriented thinking asks: <i>What entities exist in this problem domain? "
                "What information does each entity have? What can each entity do? How do the entities "
                "interact?</i>"),
              P("A software object combines related <b>state</b> (data) and <b>behaviour</b> (methods).")]
    story.append(H2("7.2  What is an Object?"))
    story += [P("An object is a distinct entity in a software system that has three parts: "
                "<b>identity</b>, <b>state</b> and <b>behaviour</b>."),
              Paragraph("<b>Identity</b> — the object can be distinguished from other objects (e.g. student ID ST001 "
                        "vs ST002; both are Students, but they are separate objects).<br/><br/>"
                        "<b>State</b> — the data describing its current condition (Student ID, Name, Programme, Year, "
                        "Status). State can change: Status = Active may later become Graduated.<br/><br/>"
                        "<b>Behaviour</b> — what the object can do (registerCourse(), dropCourse(), viewResults(), "
                        "payFees()).", S["bodyL"])]
    story += FIG("object_anatomy.png", "Figure 9 — Identity, state and behaviour, with a Student example")
    story.append(H2("7.3  What is a Class?"))
    story += [P("A class is a <b>blueprint or specification</b> from which objects can be created. One architect's "
                "blueprint can be used to build many houses; one Student class can create many Student objects.")]
    story += FIG("class_vs_object.png", "Figure 10 — Class vs object: the blueprint analogy")
    story += [P("Therefore: <b>Student is a class; Francis is an object of the Student class.</b>")]
    story.append(H2("7.4  Why Object Technology Is Useful in Business"))
    story += [P("Organisations deal with real-world entities all the time — a bank deals with customers, accounts, "
                "transactions, loans and employees; a hospital with patients, doctors, appointments and prescriptions; "
                "a university with students, lecturers, courses, programmes and payments. Object-oriented analysis "
                "lets analysts represent these important concepts directly in the software model.")]
    story += FIG("bank_objects.png", "Figure 11 — The bank's real-world concepts modelled as classes")
    story.append(CALLOUT("COMMON MISTAKE",
        ["An object does not have to be physically tangible. <b>Registration, Invoice, Payment, Account, Order, "
         "Appointment, Booking and Transaction</b> are conceptual/business entities, yet they can still be "
         "represented as software objects."]))

    story.append(H2("7.5  Encapsulation — Introduction"))
    story += [P("Encapsulation means combining data with the operations that work on that data while controlling "
                "how the internal state is accessed. We do not want every part of the application directly writing "
                "<font name='Mono'>balance = -500000</font>; instead the account object controls how its balance "
                "changes.")]
    story += FIG("encapsulation.png", "Figure 12 — Encapsulation protects data behind controlled methods")
    story.append(H2("7.6  Inheritance — Basic Introduction"))
    story += [P("A general class <b>User</b> (userID, name, email, login(), logout()) can have specialised classes "
                "<b>Student, Lecturer and Administrator</b> that reuse its common characteristics. This is "
                "inheritance — studied in detail in Week 6.")]
    story += FIG("inheritance.png", "Figure 13 — Specialised classes reuse common state and behaviour")
    story.append(H2("7.7  Polymorphism — Basic Introduction"))
    story += [P("Polymorphism means that related objects can respond differently to the same operation. Both Student "
                "and Lecturer have <font name='Mono'>displayDashboard()</font>, but a Student sees Courses, Fees and "
                "Results while a Lecturer sees Courses Taught, Students, Marks and Attendance.")]
    story += FIG("polymorphism.png", "Figure 14 — One operation, different behaviour per object")
    story.append(H2("7.8  Abstraction — Basic Introduction"))
    story += [P("Abstraction means focusing on the important characteristics of something while leaving out "
                "unnecessary detail. At an ATM the customer sees insert card, enter PIN, select withdrawal, enter "
                "amount and receive cash — not the database queries, network protocols, encryption or transaction "
                "locking underneath.")]
    story.append(H2("7.9  The Four OO Principles"))
    story += FIG("four_principles.png", "Figure 15 — Abstraction, encapsulation, inheritance and polymorphism")
    story.append(H2("7.10  Strengths of Object-Oriented Approaches"))
    story += BUL([
        "<b>Modularity</b> — systems divided into related components.",
        "<b>Reusability</b> — existing components and classes can be reused.",
        "<b>Maintainability</b> — well-designed classes isolate change.",
        "<b>Encapsulation</b> — implementation hidden behind controlled interfaces.",
        "<b>Extensibility</b> — systems extended by adding/modifying components.",
        "<b>Better representation of complex domains</b> — Customer, Account, Order, Student, Course appear naturally.",
        "<b>Multiple levels of abstraction</b> — from high-level concepts to detailed designs.",
    ])
    story.append(H2("7.11  Limitations and Challenges"))
    story += BUL([
        "<b>Complexity</b> — large systems can contain thousands of classes; poor design becomes hard to understand.",
        "<b>Learning curve</b> — objects, classes, relationships, inheritance, interfaces, polymorphism, encapsulation, design principles.",
        "<b>Poor modelling adds complexity</b> — not every noun should become a class (StudentName, StudentAge, StudentChair would be ridiculous).",
        "<b>Inheritance can be misused</b> — deep hierarchies simply because inheritance exists.",
        "<b>Initial modelling effort</b> — careful analysis first, to reduce later misunderstandings.",
    ])
    story.append(H2("7.12  OOA vs OOD vs OOP"))
    story += [P("Students often confuse these three stages:"),
              Paragraph("<b>Object-Oriented Analysis (OOA)</b> — understanding the problem and modelling <b>what</b> the system needs.<br/>"
                        "<b>Object-Oriented Design (OOD)</b> — deciding <b>how</b> the software will satisfy those requirements.<br/>"
                        "<b>Object-Oriented Programming (OOP)</b> — <b>implementing</b> the design in a language (Java, C#, C++, Python, Kotlin, TypeScript).", S["bodyL"])]
    story.append(CALLOUT("IMPORTANT",
        ["“I know Java, so I can do OOAD” is not necessarily true. Programming knowledge helps, but OOAD requires "
         "understanding business problems, communicating with stakeholders, identifying requirements and domain "
         "concepts, modelling relationships and evaluating alternative designs. <b>A person can be an excellent "
         "programmer but a poor analyst.</b>"]))

    # 8. case study + ATM -------------------------------------------------------
    story.append(H1("8.  Case Study & Worked Example"))
    story.append(H2("8.1  Module Case Study — University Registration"))
    story += [P("Throughout the module we use a continuing example: a <b>University Student Management and "
                "Registration System</b> replacing a manual process (collect forms, fill details, select courses, "
                "obtain approvals, visit finance, submit, wait for data entry).")]
    story += [P("Problems: long queues, duplicate records, lost forms, incorrect registration, slow reporting, "
                "difficulty checking prerequisites and limited visibility of status. The business objective is to "
                "<i>improve the efficiency, accuracy, transparency and accessibility of registration</i>; the need "
                "is <i>an integrated student registration process</i>; a potential solution is <i>an online student "
                "management and registration system</i>.")]
    story += [P("Candidate objects identified so far: Student, Course, Programme, Department, Lecturer, "
                "Registration, Payment, Result, User, Notification. These are candidates only — deciding which "
                "become final classes belongs to analysis and design (Week 5).")]
    story.append(H2("8.2  Worked Example: ATM System"))
    story += [P("Applying Week 1 concepts to an ATM: the business problem is that customers must visit branches for "
                "simple transactions; the need is convenient self-service banking; the objective is 24/7 access with "
                "reduced branch workload; the solution is an ATM system."),
              Paragraph("<b>Stakeholders:</b> Customer, Bank, Bank employee, Security administrator, Payment network.<br/>"
                        "<b>Functional needs:</b> authenticate customers, show balance, allow withdrawal/deposits/PIN changes, print receipts.<br/>"
                        "<b>Non-functional needs:</b> secure, reliable, responsive, available 24/7, protect customer information.<br/>"
                        "<b>Potential objects:</b> Customer, Card, Account, Transaction, ATM, Receipt.", S["bodyL"])]
    story += FIG("atm_flow.png", "Figure 16 — The ATM: from business problem to candidate objects")

    # 9. activities -------------------------------------------------------------
    story.append(H1("9.  Practical & Tutorial Activities"))
    story.append(H2("9.1  Practical — Identify Business Needs and Candidate Objects"))
    story += [P("<b>Scenario:</b> A college uses a manual library system. Students physically search shelves, fill "
                "out borrowing forms, wait for librarians to check records, sometimes lose slips, and cannot easily "
                "determine whether a book is available."),
              Paragraph("<b>Task 1</b> — identify at least five business problems.<br/>"
                        "<b>Task 2</b> — identify at least three business needs.<br/>"
                        "<b>Task 3</b> — identify at least six stakeholders.<br/>"
                        "<b>Task 4</b> — write at least eight functional requirements.<br/>"
                        "<b>Task 5</b> — write at least five non-functional requirements.<br/>"
                        "<b>Task 6</b> — identify at least eight candidate objects (e.g. Student, Book, Librarian, "
                        "Library, Borrowing, Return, Fine, Reservation) and explain why each was selected.", S["bodyL"])]
    story.append(H2("9.2  Tutorial — Group Exercise"))
    story += [P("Each group selects one system — mobile money, hospital management, online shopping, hotel booking "
                "or university registration — and produces:"),
              Paragraph("A. Business problem&nbsp;&nbsp; B. Business need&nbsp;&nbsp; C. Business objective&nbsp;&nbsp; D. Stakeholders<br/>"
                        "E. Functional needs&nbsp;&nbsp; F. Non-functional needs&nbsp;&nbsp; G. Business rules&nbsp;&nbsp; H. Candidate objects",
                        S["bodyL"])]
    story += [P("Each group presents its findings to the class.")]

    # 10. independent learning ---------------------------------------------------
    story.append(H1("10.  Independent Learning (10 Hours)"))
    story += BUL([
        "<b>Read</b> — business needs, requirements, functional/non-functional requirements, stakeholders, object technology.",
        "<b>Observe</b> — choose a system you use regularly (mobile banking, mobile money, registration, supermarket, hospital, library) and write its problem, objectives, needs, stakeholders, functional/non-functional requirements, business rules and possible objects.",
        "<b>Object observation</b> — identify 10 real-world objects; for each write its state and behaviour (e.g. Phone: battery, model, volume — call, charge, restart).",
    ])
    story.append(DTABLE(
        ["Object", "State", "Behaviour"],
        [["Phone", "battery, model, volume", "call, charge, restart"],
         ["Student", "name, programme, year", "register, study, graduate"],
         ["Car", "speed, fuel, gear", "start, accelerate, brake"]],
        widths=[0.22 * DOC_W, 0.44 * DOC_W, 0.34 * DOC_W]))

    # 11. common mistakes ---------------------------------------------------------
    story.append(H1("11.  Common Student Mistakes"))
    mistakes = [
        ("Mistake 1 — “Business need means software requirement.”",
         "A business need describes what the organisation needs to achieve; a software requirement describes what the system must provide to support that need."),
        ("Mistake 2 — “Every business problem requires software.”",
         "Some problems are organisational, financial, human-resource, procedural or infrastructural rather than technological."),
        ("Mistake 3 — “Functional means important; non-functional means unimportant.”",
         "Both are important. Functional requirements describe behaviour; non-functional requirements describe qualities and constraints."),
        ("Mistake 4 — “An object must be a physical thing.”",
         "Software can model conceptual entities such as Payment, Registration, Order and Transaction."),
        ("Mistake 5 — “A class and an object are the same thing.”",
         "A class defines a type/blueprint; an object is a particular instance."),
        ("Mistake 6 — “OOAD means programming in Java.”",
         "OOAD is about analysing and designing with object concepts; programming is the implementation stage."),
        ("Mistake 7 — “Create classes from every noun immediately.”",
         "Nouns give candidate concepts, but analysis decides which concepts actually belong in the model."),
    ]
    for head, fix in mistakes:
        story.append(CALLOUT(head, [fix], bg=HexColor("#FBF3F3"), bar=C_SOFT, tcol=C_MAROON))

    # 12. summary ------------------------------------------------------------------
    story.append(H1("12.  Week 1 Summary"))
    story += [P("The table below condenses Week 1 into its essential definitions:")]
    story.append(DTABLE(
        ["Term", "Definition"],
        [["Business Need", "A problem, opportunity or desired improvement an organisation must address."],
         ["Business Objective", "The result the organisation wants to achieve."],
         ["Stakeholder", "A person, group or organisation interested in or affected by the system."],
         ["Functional Requirement", "What the system should do."],
         ["Non-Functional Requirement", "Qualities, constraints or conditions under which the system operates."],
         ["Business Rule", "A policy or condition that governs how the organisation operates."],
         ["Object", "A software entity with identity, state and behaviour."],
         ["Class", "A specification/blueprint from which objects are created."],
         ["Object Technology", "Representing a problem domain using objects, state, behaviour and relationships."]],
        widths=[0.34 * DOC_W, 0.66 * DOC_W]))

    story.append(H2("12.1  The Most Important Concept of Week 1"))
    story += [Paragraph("An organisation has a <b>business objective</b> → a <b>business problem</b> may prevent it → "
                        "the organisation identifies a <b>business need</b> → <b>stakeholders</b> help identify what is "
                        "required → <b>requirements</b> are documented → analysts study the <b>problem domain</b> → "
                        "important entities and their behaviour are represented with <b>object-oriented concepts</b> → "
                        "these models become the foundation for <b>design and implementation</b>.", S["bodyL"])]
    story += [P("<b>That is the foundation upon which the remaining 15 weeks will build.</b>")]

    # 13. revision ----------------------------------------------------------------
    story.append(H1("13.  Revision Questions"))
    story.append(H2("Short-answer questions"))
    story += BUL([
        "Define a business need.", "What is a business problem?",
        "Differentiate between a business problem and a business need.", "What is a business objective?",
        "Define a stakeholder.", "What is a functional requirement?", "What is a non-functional requirement?",
        "What is a business rule?", "Define object technology.", "What is an object?", "What is a class?",
        "Differentiate between a class and an object.", "What is object state?", "What is object behaviour?",
        "Explain encapsulation.", "What is abstraction?", "What is inheritance?", "What is polymorphism?",
        "Give four advantages of object-oriented approaches.", "Give three limitations/challenges of object-oriented approaches.",
    ])
    story.append(H2("Application questions"))
    story += [P("<b>Question 1.</b> A hospital has patients waiting several hours before being attended to. Identify: "
                "(a) the business problem, (b) two business needs, (c) two business objectives, (d) five stakeholders, "
                "(e) five functional requirements, (f) five non-functional requirements, (g) five candidate objects."),
              P("<b>Question 2.</b> A university wants an online examination management system. Identify: (a) the "
                "business need, (b) stakeholders, (c) functional requirements, (d) non-functional requirements, "
                "(e) business rules, (f) candidate objects."),
              P("<b>Question 3.</b> Explain the difference between business need → requirement → software solution, "
                "using a real-world example.")]
    story.append(H2("Examination-style question"))
    story.append(CALLOUT("EXAM QUESTION",
        ["“A retail organisation currently records sales using handwritten receipts. Management wants to introduce a "
         "computerised sales management system. As an object-oriented systems analyst, explain how you would move from "
         "understanding the business need to identifying potential objects for the proposed system.”",
         "A strong answer discusses: current business problem, business objectives, business needs, stakeholders, "
         "requirements elicitation, functional requirements, non-functional requirements, business rules, candidate "
         "objects, and the state and behaviour of those candidate objects."]))

    # 14. references ---------------------------------------------------------------
    story.append(H1("14.  References and Further Reading"))
    story.append(H2("Standards and authoritative references"))
    story += BUL([
        "International Organization for Standardization. (2018). <i>ISO/IEC/IEEE 29148:2018 — Systems and software engineering — Life cycle processes — Requirements engineering.</i> ISO. (Current edition; reviewed and confirmed 2024.)",
        "Object Management Group. (2017). <i>OMG Unified Modeling Language (OMG UML), Version 2.5.1.</i> OMG.",
    ])
    story.append(H2("Object-oriented concepts"))
    story += BUL([
        "Oracle. <i>Object-Oriented Programming Concepts.</i> Oracle documentation on objects, classes, inheritance, encapsulation and related concepts.",
        "Microsoft. <i>Object-oriented programming (C#).</i> Microsoft Learn, updated 2025 — abstraction, encapsulation, inheritance and polymorphism.",
    ])
    story.append(H2("Prescribed and recommended texts"))
    story += BUL([
        "Mach, E. (2019). <i>Object Oriented Analysis &amp; Design Cookbook: Introduction to Practical System Modeling.</i>",
        "Reddy, V., &amp; Korra, S. (2018). <i>Object-Oriented Analysis and Design Using UML.</i>",
        "The Art of Service. (2021). <i>Object Oriented Analysis and Design: A Complete Guide.</i>",
        "Wixom, B., &amp; Dennis, A. (2018). <i>Systems Analysis and Design.</i>",
        "Blokdyk, G. (2021). <i>Object-Oriented Analysis and Design Standard Requirements.</i>",
        "Wixom, B., &amp; Dennis, A. (2020). <i>Systems Analysis and Design: An Object-Oriented Approach with UML.</i>",
    ])

    # build with TOC (multi-pass)
    doc = WeekDoc(pdf_path, draw_cover,
                  leftMargin=MARGIN, rightMargin=MARGIN,
                  topMargin=MARGIN, bottomMargin=MARGIN,
                  title="BICT 3202 — OOAD Week 1",
                  author="Francis Fweta")
    doc.multiBuild(story, canvasmaker=NumberedCanvas)
    return pdf_path


if __name__ == "__main__":
    print("Built:", build())
