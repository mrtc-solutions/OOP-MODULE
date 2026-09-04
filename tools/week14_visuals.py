"""
Week 14 visuals — INTEGRATING OBJECT, DYNAMIC AND BEHAVIOURAL MODELS INTO OOD.
Analysis vs design · three models · design classes · visibility ·
responsibilities · sequence->operations · consistency · traceability.
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (FancyBboxPatch, FancyArrowPatch, Circle,
                                Polygon, Ellipse)

from common import (MAROON, MAROON_DARK, MAROON_DEEP, MAROON_SOFT, MAROON_TINT,
                    GOLD, GOLD_LIGHT, CREAM, CREAM_2, INK, GREY, GREY_LIGHT,
                    WHITE, CHART_COLORS)
from draw import (canvas, box, chev, t, arrow, title, save, H_XB, H_B, H_SB,
                  H_MD, BODY, B_SB, B_B, B_IT, MONO, SYM)


def gtri(ax, x, y, w, h, ec=MAROON, lw=2.0, z=8):
    ax.add_patch(Polygon([(x, y + h), (x - w / 2, y), (x + w / 2, y)],
                         closed=True, fill=False, edgecolor=ec, lw=lw, zorder=z))


def uc(ax, x, y, w, name, attrs=None, ops=None, name_color=WHITE, fill=WHITE,
       ec=MAROON, line_h=17, pad=8, name_size=11.5):
    attrs = attrs or []
    ops = ops or []
    h_name = 27
    h_attrs = pad + line_h * len(attrs) + (pad if attrs else 0)
    h_ops = pad + line_h * len(ops) + (pad if ops else 0)
    h = h_name + h_attrs + h_ops
    box(ax, x, y, w, h, fill, ec=ec, lw=1.8, r=0, z=6)
    box(ax, x, y + h - h_name, w, h_name, ec, r=0, z=6)
    t(ax, x + w / 2, y + h - h_name / 2, name, size=name_size, color=name_color, fam=H_SB, z=7)
    ax.plot([x, x + w], [y + h_attrs + h_ops, y + h_attrs + h_ops], color=ec, lw=1.0, zorder=7)
    ax.plot([x, x + w], [y + h_ops, y + h_ops], color=ec, lw=1.0, zorder=7)
    yy = y + h_attrs + h_ops - pad
    for a in attrs:
        t(ax, x + 9, yy, a, size=10, color=INK, fam=MONO, ha="left", z=7)
        yy -= line_h
    yy = y + h_ops - pad
    for o in ops:
        t(ax, x + 9, yy, o, size=10, color=MAROON_SOFT, fam=MONO, ha="left", z=7)
        yy -= line_h
    return (x, y, w, h)


def state(ax, x, y, w, h, label, sub=None, fill=WHITE, ec=MAROON, lw=2.0,
          lab_size=12, sub_size=9.5, z=6):
    box(ax, x, y, w, h, fill, ec=ec, lw=lw, r=12, z=z)
    cy = y + h / 2 + (7 if sub else 0)
    t(ax, x + w / 2, cy, label, size=lab_size, color=MAROON_DARK, fam=B_SB, z=z + 1)
    if sub:
        t(ax, x + w / 2, y + h / 2 - 10, sub, size=sub_size, color=GREY, fam=B_IT, z=z + 1)


def inode(ax, x, y, r=9, z=8):
    ax.add_patch(Circle((x, y), r, facecolor=MAROON, edgecolor=MAROON_DARK, lw=1.0, zorder=z))


def fnode(ax, x, y, r=10, z=8):
    ax.add_patch(Circle((x, y), r, facecolor=WHITE, edgecolor=MAROON, lw=2.0, zorder=z))
    ax.add_patch(Circle((x, y), r - 4, facecolor=MAROON, edgecolor="none", zorder=z))


# --------------------------------------------------------------------------
# 1. Progression Week 13 -> 14
# --------------------------------------------------------------------------
def progression():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Week 13 -> Week 14", sub="From architecture to the contents of the components")

    box(ax, 22, 110, 380, 216, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 300, "WEEK 13", size=13, color=MAROON, fam=H_B, z=6)
    for i, s in enumerate(["Architecture", "Layers", "Components", "Reuse + Adaptability"]):
        box(ax, 80, 232 - i * 36, 264, 28, MAROON_TINT, r=8, z=6)
        t(ax, 212, 246 - i * 36, s, size=11, color=INK, fam=BODY, z=7)
    t(ax, 212, 126, "\u201chow to organise the software\u201d", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 110, 380, 216, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 300, "WEEK 14", size=13, color=MAROON_DARK, fam=H_B, z=6)
    for i, s in enumerate(["Design Classes", "Responsibilities", "Operations", "Object + Dynamic + Behavioural"]):
        box(ax, 496, 232 - i * 36, 264, 28, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
        t(ax, 628, 246 - i * 36, s, size=10, color=MAROON_SOFT, fam=BODY, z=7)
    t(ax, 628, 126, "\u201cwhat those components contain\u201d", size=10, color=GREY, fam=B_IT, z=7)

    arrow(ax, 406, 220, 434, 220, lw=2.4, ms=16, z=8)
    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Week 14 combines all the models into one coherent software design.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w14_progression.png")


# --------------------------------------------------------------------------
# 2. Analysis vs design
# --------------------------------------------------------------------------
def analysis_vs_design():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Analysis vs Design", sub="What the system needs vs how the software will provide it")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "ANALYSIS", size=14, color=MAROON, fam=H_B, z=6)
    t(ax, 212, 278, "\u201cWhat does the system need?\u201d", size=11.5, color=MAROON_SOFT, fam=B_SB, z=7)
    box(ax, 60, 200, 304, 40, MAROON_TINT, r=10, z=6)
    t(ax, 212, 220, "\u201cA student must register for a course.\u201d", size=10.5, color=INK, fam=B_IT, z=7)
    for i, s in enumerate(["Student", "Course", "Registration"]):
        box(ax, 100, 150 - i * 32, 224, 26, MAROON_TINT, r=8, z=6)
        t(ax, 212, 163 - i * 32, s, size=10.5, color=INK, fam=BODY, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "DESIGN", size=14, color=MAROON_DARK, fam=H_B, z=6)
    t(ax, 628, 278, "\u201cHow will the software implement it?\u201d", size=11.5, color=MAROON_SOFT, fam=B_SB, z=7)
    for i, s in enumerate(["RegistrationController", "RegistrationService", "RegistrationRepository", "RegistrationValidator"]):
        box(ax, 516, 200 - i * 38, 224, 30, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
        t(ax, 628, 215 - i * 38, s, size=10, color=MAROON_SOFT, fam=BODY, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "The design becomes more implementation-oriented.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w14_analysis_vs_design.png")


# --------------------------------------------------------------------------
# 3. Analysis -> design transformation
# --------------------------------------------------------------------------
def transformation():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Analysis Model -> Design Model", sub="Design classes should be justified by requirements and analysis")

    steps = ["REQUIREMENTS", "USE CASES", "ANALYSIS MODEL", "DESIGN DECISIONS", "DESIGN MODEL", "IMPLEMENTATION"]
    cols = [MAROON, MAROON, MAROON_SOFT, MAROON_SOFT, MAROON_DARK, MAROON_DEEP]
    y = 380
    for i, (name, colr) in enumerate(zip(steps, cols)):
        box(ax, 250, y, 340, 52, colr, r=12, z=6)
        t(ax, 420, y + 26, name, size=12, color=WHITE if colr != MAROON_SOFT else WHITE, fam=H_SB, z=7)
        if i < len(steps) - 1:
            arrow(ax, 420, y - 2, 420, y - 12, lw=2.2, ms=14, z=8)
        y -= 66

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "Do not randomly invent design classes \u2014 justify them by requirements and analysis.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w14_transformation.png")


# --------------------------------------------------------------------------
# 4. The three models
# --------------------------------------------------------------------------
def three_models():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Three Major Models", sub="Each answers a different question")

    cards = [
        (22, "OBJECT MODEL", "\u201cWhat things exist and how are they related?\u201d", ["classes · attributes · operations", "associations · generalisation", "aggregation / composition"], MAROON),
        (300, "DYNAMIC MODEL", "\u201cHow do objects change over time?\u201d", ["Course: Available", "-> Full", "-> Closed (events change state)"], MAROON_SOFT),
        (578, "BEHAVIOURAL MODEL", "\u201cWhat does the system do / how do users interact?\u201d", ["use cases · use-case diagrams", "sequence · communication", "activity diagrams"], MAROON_DARK),
    ]
    for x, hd, q, items, colr in cards:
        box(ax, x, 96, 240, 246, WHITE, ec=colr, lw=1.8, r=14, z=5)
        box(ax, x, 306, 240, 36, colr, r=12, z=6)
        t(ax, x + 120, 324, hd, size=11.5, color=WHITE, fam=H_SB, z=7)
        t(ax, x + 120, 276, q, size=10, color=GREY, fam=B_IT, z=7)
        for i, s in enumerate(items):
            y = 224 - i * 30
            box(ax, x + 30, y - 12, 180, 24, MAROON_TINT, r=8, z=6)
            t(ax, x + 120, y, s, size=9.5, color=INK, fam=BODY, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Different UML models answer different questions \u2014 together they describe one system.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w14_three_models.png")


# --------------------------------------------------------------------------
# 5. Multiple views
# --------------------------------------------------------------------------
def multiple_views():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "One System, Multiple Views", sub="Six views \u2014 not six unrelated systems")

    views = [
        ("Use case", "who and what they want"),
        ("Class", "structural elements"),
        ("Sequence", "objects interacting"),
        ("Activity", "workflow progress"),
        ("State machine", "object state changes"),
        ("Component", "modular functionality"),
    ]
    for i, (hd, sub) in enumerate(views):
        r, c = divmod(i, 3)
        x = 30 + c * 268
        y = 214 - r * 96
        box(ax, x, y, 244, 80, WHITE if r == 0 else MAROON_TINT, ec=MAROON, lw=1.6, r=12, z=5)
        t(ax, x + 122, y + 58, hd + " diagram", size=11.5, color=MAROON, fam=B_SB, z=6)
        t(ax, x + 122, y + 24, sub, size=9.5, color=GREY, fam=B_IT, z=6)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Each diagram provides a different view of the same system.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w14_multiple_views.png")


# --------------------------------------------------------------------------
# 6. From use case to design
# --------------------------------------------------------------------------
def use_case_flow():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "From Use Case to Design", sub="Register for Course \u2014 basic flow and candidate classes")

    flow = [
        "1. Student logs in",
        "2. Student selects a course",
        "3. System checks the course exists",
        "4. System checks prerequisites",
        "5. System checks course capacity",
        "6. System creates registration",
        "7. System confirms registration",
    ]
    box(ax, 40, 96, 340, 286, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 210, 356, "BASIC USE-CASE FLOW", size=12, color=MAROON, fam=H_B, z=6)
    for i, s in enumerate(flow):
        y = 310 - i * 36
        t(ax, 210, y, s, size=10.5, color=INK, fam=BODY, ha="left", z=7)

    box(ax, 420, 96, 398, 286, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 619, 356, "CANDIDATE CLASSES", size=12, color=MAROON_DARK, fam=H_B, z=6)
    t(ax, 619, 316, "domain classes:", size=10.5, color=GREY, fam=B_IT, z=7)
    for i, s in enumerate(["Student", "Course", "Registration"]):
        box(ax, 470, 270 - i * 36, 190, 28, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
        t(ax, 565, 284 - i * 36, s, size=10.5, color=INK, fam=BODY, z=7)
    t(ax, 619, 150, "design classes:", size=10.5, color=GREY, fam=B_IT, z=7)
    for i, s in enumerate(["RegistrationController", "RegistrationService", "CourseRepository", "RegistrationRepository"]):
        box(ax, 470, 104 - i * 34, 190, 28, MAROON_TINT, ec=MAROON, lw=1.3, r=8, z=6)
        t(ax, 565, 118 - i * 34, s, size=9.5, color=MAROON_SOFT, fam=BODY, z=7)

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "The designer asks: which objects should perform these responsibilities?",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w14_use_case_flow.png")


# --------------------------------------------------------------------------
# 7. Responsibility — knowing vs doing
# --------------------------------------------------------------------------
def responsibility():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Responsibility Assignment", sub="A class KNOWS things and DOES things")

    box(ax, 22, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "GOOD ASSIGNMENT", size=12.5, color=MAROON, fam=H_B, z=6)
    uc(ax, 120, 118, 184, "Course", attrs=["courseCode", "courseName", "capacity"], ops=["checkCapacity()"], name_size=11)
    t(ax, 212, 106, "KNOWS its capacity · DOES check space", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "BAD ASSIGNMENT  (poor cohesion)", size=12.5, color=MAROON_SOFT, fam=H_B, z=6)
    uc(ax, 536, 118, 184, "Student", ops=["registerAnyCourse()", "calculateCourseCapacity()", "sendEmail()", "generatePaymentReceipt()", "connectToDatabase()"], ec=MAROON_SOFT, name_size=11)
    t(ax, 628, 106, "Student does far too much", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Assign each responsibility to the object that has the information needed to perform it.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w14_responsibility.png")


# --------------------------------------------------------------------------
# 8. Design class (analysis -> design)
# --------------------------------------------------------------------------
def design_class():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Analysis Class -> Design Class", sub="Precise attributes, types, visibility, operations")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "ANALYSIS CLASS", size=13, color=MAROON, fam=H_B, z=6)
    uc(ax, 130, 150, 164, "Student", attrs=["name", "email"], ops=["register()"], name_size=11)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "DESIGN CLASS", size=13, color=MAROON_DARK, fam=H_B, z=6)
    uc(ax, 536, 106, 184, "Student",
       attrs=["-studentId : String", "-name : String", "-email : String", "-programme : Programme"],
       ops=["+register(course: Course): Registration", "+drop(course: Course): void"],
       name_size=11)
    t(ax, 628, 94, "visibility · types · parameters · return types", size=10, color=GREY, fam=B_IT, z=7)

    arrow(ax, 406, 220, 434, 220, lw=2.6, ms=18, z=8)
    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "The design class is much more precise.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w14_design_class.png")


# --------------------------------------------------------------------------
# 9. Visibility
# --------------------------------------------------------------------------
def visibility():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Visibility in Design Classes", sub="UML visibility symbols")

    rows = [("+", "Public"), ("-", "Private"), ("#", "Protected"), ("~", "Package visibility")]
    x0, w1, w2 = 200, 120, 320
    y_top, rh = 300, 44
    box(ax, x0, y_top - rh - len(rows) * rh - 16, w1 + w2, 16 + rh + len(rows) * rh, WHITE, ec=MAROON, lw=1.6, r=12, z=4)
    box(ax, x0, y_top - rh, w1 + w2, rh, MAROON, r=0, z=5)
    t(ax, x0 + w1 / 2, y_top - rh / 2, "SYMBOL", size=12, color=WHITE, fam=H_SB, z=6)
    t(ax, x0 + w1 + w2 / 2, y_top - rh / 2, "MEANING", size=12, color=WHITE, fam=H_SB, z=6)
    for i, (sy, m) in enumerate(rows):
        yy = y_top - rh * (i + 1) - rh / 2
        fc = WHITE if i % 2 == 0 else MAROON_TINT
        box(ax, x0, y_top - rh * (i + 1) - rh, w1 + w2, rh, fc, r=0, z=5)
        t(ax, x0 + w1 / 2, yy, sy, size=13, color=MAROON_SOFT, fam=MONO, z=6)
        t(ax, x0 + w1 + w2 / 2, yy, m, size=12, color=INK, fam=BODY, z=6)
        ax.plot([x0, x0 + w1 + w2], [y_top - rh * (i + 1), y_top - rh * (i + 1)], color=GREY_LIGHT, lw=1.0, zorder=6)
    ax.plot([x0 + w1, x0 + w1], [y_top - rh, y_top - rh - len(rows) * rh], color=GREY_LIGHT, lw=1.0, zorder=6)

    box(ax, 22, 18, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 31, "Example: -studentId : String · +getName() : String · +register() : void.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w14_visibility.png")


# --------------------------------------------------------------------------
# 10. Sequence -> operations
# --------------------------------------------------------------------------
def sequence_to_class():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Sequence Diagram -> Class Design", sub="Messages reveal the operations each class needs")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "SEQUENCE DIAGRAM", size=13, color=MAROON, fam=H_B, z=6)
    objs = ["Student", "RegistrationService", "Course", "Registration"]
    xs = [100, 220, 300, 360]
    for x, name in zip(xs, objs):
        box(ax, x - 34, 250, 68, 26, MAROON, r=6, z=6)
        t(ax, x, 263, name, size=7.5, color=WHITE, fam=B_SB, z=7)
    msgs = [("register(course)", 100, 220, 230), ("checkCapacity()", 220, 300, 210), ("createRegistration()", 300, 360, 190)]
    for label, x1, x2, y in msgs:
        arrow(ax, x1 + 2, y, x2 - 2, y, lw=1.6, ms=10, z=8)
        t(ax, (x1 + x2) / 2, y + 10, label, size=8.5, color=MAROON_SOFT, fam=MONO, z=8)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "INFERRED OPERATIONS", size=13, color=MAROON_DARK, fam=H_B, z=6)
    uc(ax, 546, 180, 164, "Course", ops=["checkCapacity()"], name_size=10.5)
    uc(ax, 546, 96, 164, "RegistrationService", ops=["registerStudent()"], name_size=10.5)
    t(ax, 628, 84, "messages -> operations", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Messages in interaction diagrams help refine operations in the class model.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w14_sequence_to_class.png")


# --------------------------------------------------------------------------
# 11. Model consistency
# --------------------------------------------------------------------------
def consistency():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Model Consistency", sub="The diagrams must agree with one another")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "INCONSISTENT", size=13, color=MAROON_SOFT, fam=H_B, z=6)
    uc(ax, 100, 168, 164, "Course", ops=["checkCapacity()"], ec=MAROON_SOFT, name_size=10.5)
    t(ax, 100, 150, "class diagram", size=9, color=GREY, fam=B_IT, z=7)
    t(ax, 250, 216, "vs", size=12, color=GREY, fam=B_IT, z=7)
    uc(ax, 280, 168, 164, "Course", ops=["verifyCapacity()"], ec=MAROON_SOFT, name_size=10.5)
    t(ax, 280, 150, "sequence diagram", size=9, color=GREY, fam=B_IT, z=7)
    t(ax, 212, 116, "which operation is correct?", size=10.5, color=MAROON_SOFT, fam=B_SB, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "RESOLVED", size=13, color=MAROON, fam=H_B, z=6)
    uc(ax, 546, 168, 164, "Course", ops=["checkCapacity()"], name_size=10.5)
    t(ax, 628, 150, "standardise the terminology", size=10.5, color=GREY, fam=B_IT, z=7)
    t(ax, 628, 120, "register() vs enrol() \u2014 same operation?", size=10.5, color=MAROON_DARK, fam=B_SB, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Cross-check the models and resolve any discrepancy.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w14_consistency.png")


# --------------------------------------------------------------------------
# 12. Object + dynamic model
# --------------------------------------------------------------------------
def object_dynamic():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Object Model + Dynamic Model", sub="Operations relate to state changes")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "OBJECT MODEL", size=13, color=MAROON, fam=H_B, z=6)
    uc(ax, 120, 140, 184, "Course", attrs=["capacity", "status"], ops=["registerStudent()"], name_size=11)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "DYNAMIC MODEL", size=13, color=MAROON_DARK, fam=H_B, z=6)
    state(ax, 520, 200, 120, 40, "Available")
    state(ax, 660, 200, 120, 40, "Full")
    state(ax, 660, 130, 120, 40, "Closed")
    arrow(ax, 642, 220, 658, 220, lw=2.0, ms=13, z=8)
    arrow(ax, 720, 198, 720, 174, lw=2.0, ms=13, z=8)
    t(ax, 620, 118, "registerStudent() -> Available -> Full", size=10, color=MAROON_SOFT, fam=B_SB, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "registerStudent() causes Available -> Full when the final seat is taken.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w14_object_dynamic.png")


# --------------------------------------------------------------------------
# 13. Activity -> responsibility mapping
# --------------------------------------------------------------------------
def activity_mapping():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Object Model + Activity Model", sub="Map each activity to a responsible class")

    rows = [
        ("Select course", "RegistrationController"),
        ("Check prerequisite", "Course / RegistrationService"),
        ("Check capacity", "Course"),
        ("Create registration", "RegistrationService"),
        ("Save registration", "RegistrationRepository"),
        ("Send confirmation", "NotificationService"),
    ]
    x0, w1, w2 = 60, 360, 360
    y_top, rh = 330, 44
    box(ax, x0, y_top - rh - len(rows) * rh - 16, w1 + w2, 16 + rh + len(rows) * rh, WHITE, ec=MAROON, lw=1.6, r=12, z=4)
    box(ax, x0, y_top - rh, w1 + w2, rh, MAROON, r=0, z=5)
    t(ax, x0 + w1 / 2, y_top - rh / 2, "ACTIVITY", size=12, color=WHITE, fam=H_SB, z=6)
    t(ax, x0 + w1 + w2 / 2, y_top - rh / 2, "POSSIBLE RESPONSIBLE CLASS", size=12, color=WHITE, fam=H_SB, z=6)
    for i, (a, dd) in enumerate(rows):
        yy = y_top - rh * (i + 1) - rh / 2
        fc = WHITE if i % 2 == 0 else MAROON_TINT
        box(ax, x0, y_top - rh * (i + 1) - rh, w1 + w2, rh, fc, r=0, z=5)
        t(ax, x0 + w1 / 2, yy, a, size=11, color=INK, fam=BODY, z=6)
        t(ax, x0 + w1 + w2 / 2, yy, dd, size=11, color=MAROON_SOFT, fam=B_SB, z=6)
        ax.plot([x0, x0 + w1 + w2], [y_top - rh * (i + 1), y_top - rh * (i + 1)], color=GREY_LIGHT, lw=1.0, zorder=6)
    ax.plot([x0 + w1, x0 + w1], [y_top - rh, y_top - rh - len(rows) * rh], color=GREY_LIGHT, lw=1.0, zorder=6)

    box(ax, 22, 18, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 31, "This transforms a behavioural model into design responsibilities.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w14_activity_mapping.png")


# --------------------------------------------------------------------------
# 14. Controller vs God class
# --------------------------------------------------------------------------
def controller():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Controller", sub="A controller coordinates \u2014 it does not do everything")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "GOD CLASS  (bad)", size=12.5, color=MAROON_SOFT, fam=H_B, z=6)
    box(ax, 60, 176, 304, 120, MAROON_SOFT, r=12, z=6)
    t(ax, 212, 272, "RegistrationController", size=11, color=WHITE, fam=B_SB, z=7)
    for i, s in enumerate(["check database", "calculate fees", "validate course", "apply business rules", "create HTML", "send SMS"]):
        t(ax, 212, 246 - i * 19, s, size=9.5, color=GOLD_LIGHT, fam=MONO, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "COORDINATES  (good)", size=12.5, color=MAROON, fam=H_B, z=6)
    box(ax, 536, 206, 184, 34, MAROON, r=10, z=6)
    t(ax, 628, 223, "RegistrationController", size=10, color=WHITE, fam=B_SB, z=7)
    arrow(ax, 628, 204, 628, 186, lw=1.8, ms=11, z=8)
    box(ax, 536, 152, 184, 34, MAROON_SOFT, r=10, z=6)
    t(ax, 628, 169, "RegistrationService", size=10, color=WHITE, fam=B_SB, z=7)
    arrow(ax, 578, 166, 500, 128, lw=1.6, ms=10, z=8)
    arrow(ax, 678, 166, 720, 128, lw=1.6, ms=10, z=8)
    box(ax, 440, 104, 120, 26, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
    t(ax, 500, 117, "Course", size=9.5, color=MAROON_SOFT, fam=B_SB, z=7)
    box(ax, 700, 104, 120, 26, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
    t(ax, 760, 117, "Repository", size=9.5, color=MAROON_SOFT, fam=B_SB, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "The controller coordinates rather than owning every responsibility.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w14_controller.png")


# --------------------------------------------------------------------------
# 15. Domain knowledge
# --------------------------------------------------------------------------
def domain_knowledge():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Domain Objects Contain Domain Knowledge", sub="Course knows whether it is available")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "SCATTERED RULES  (bad)", size=12.5, color=MAROON_SOFT, fam=H_B, z=6)
    t(ax, 212, 268, "the rule appears in every UI screen", size=11, color=GREY, fam=B_IT, z=7)
    for i, s in enumerate(["web: capacity > registered?", "mobile: capacity > registered?", "desktop: capacity > registered?"]):
        box(ax, 70, 210 - i * 40, 284, 32, WHITE, ec=MAROON_SOFT, lw=1.3, r=8, z=6)
        t(ax, 212, 226 - i * 40, s, size=9.5, color=MAROON_SOFT, fam=MONO, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "OWNED BY COURSE  (good)", size=12.5, color=MAROON, fam=H_B, z=6)
    uc(ax, 546, 140, 164, "Course",
       attrs=["capacity : Integer", "registered : Integer"],
       ops=["isAvailable()", "hasCapacity()"], name_size=10.5)
    t(ax, 628, 128, "one place for the rule", size=10.5, color=MAROON_DARK, fam=B_SB, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Assign responsibilities to the object that has the information needed to perform them.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w14_domain_knowledge.png")


# --------------------------------------------------------------------------
# 16. Design for change
# --------------------------------------------------------------------------
def design_change():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Designing for Change", sub="Boundaries around what is likely to change")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "TIGHTLY COUPLED  (bad)", size=12.5, color=MAROON_SOFT, fam=H_B, z=6)
    box(ax, 100, 200, 150, 40, MAROON_SOFT, r=8, z=6)
    t(ax, 175, 220, "RegistrationService", size=9.5, color=WHITE, fam=B_SB, z=7)
    box(ax, 100, 130, 150, 40, MAROON_SOFT, r=8, z=6)
    t(ax, 175, 150, "AirtelMoneyAPI", size=9.5, color=WHITE, fam=B_SB, z=7)
    arrow(ax, 175, 198, 175, 174, lw=2.0, ms=13, z=8)
    t(ax, 212, 96, "one provider, tightly connected", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "BEHIND AN ABSTRACTION  (good)", size=12.5, color=MAROON, fam=H_B, z=6)
    box(ax, 546, 200, 150, 40, MAROON, r=8, z=6)
    t(ax, 621, 220, "RegistrationService", size=9.5, color=WHITE, fam=B_SB, z=7)
    box(ax, 546, 130, 150, 34, WHITE, ec=MAROON, lw=1.4, r=8, z=6)
    t(ax, 621, 147, "PaymentGateway", size=9.5, color=MAROON, fam=B_SB, z=7)
    arrow(ax, 621, 198, 621, 168, lw=2.0, ms=13, z=8)
    box(ax, 420, 96, 130, 30, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
    t(ax, 485, 111, "Provider A", size=9.5, color=INK, fam=BODY, z=7)
    box(ax, 700, 96, 130, 30, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
    t(ax, 765, 111, "Provider B", size=9.5, color=INK, fam=BODY, z=7)
    arrow(ax, 485, 128, 490, 132, lw=1.4, ms=9, z=8)
    arrow(ax, 765, 128, 760, 132, lw=1.4, ms=9, z=8)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Likely to change: database, payment provider, notification channel, UI, external API.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w14_design_change.png")


# --------------------------------------------------------------------------
# 17. Strategy pattern
# --------------------------------------------------------------------------
def strategy():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Design Patterns (outline): Strategy", sub="One abstraction, many payment implementations")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "IF / ELSE EVERYWHERE  (rigid)", size=12.5, color=MAROON_SOFT, fam=H_B, z=6)
    box(ax, 60, 150, 304, 130, MAROON_SOFT, r=12, z=6)
    for i, s in enumerate(["if payment == mobile money ...", "else if payment == bank ...", "else if payment == card ..."]):
        t(ax, 212, 246 - i * 26, s, size=9.5, color=GOLD_LIGHT, fam=MONO, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "STRATEGY PATTERN  (flexible)", size=12.5, color=MAROON, fam=H_B, z=6)
    box(ax, 556, 210, 144, 34, MAROON, r=10, z=6)
    t(ax, 628, 227, "PaymentStrategy", size=10.5, color=WHITE, fam=B_SB, z=7)
    for i, s in enumerate(["MobileMoneyPayment", "BankPayment", "CardPayment"]):
        box(ax, 556, 140 - i * 40, 144, 32, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
        t(ax, 628, 156 - i * 40, s, size=9.5, color=MAROON_SOFT, fam=B_SB, z=7)
        if i == 0:
            arrow(ax, 628, 208, 628, 176, lw=1.6, ms=10, z=8)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Use patterns only when they solve an actual recurring design problem.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w14_strategy.png")


# --------------------------------------------------------------------------
# 18. Integrated design model
# --------------------------------------------------------------------------
def integrated_design():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Integrated Design Model", sub="Controller -> Service -> Domain -> Repository")

    uc(ax, 350, 372, 140, "RegistrationController", ops=["+registerCourse()"], name_size=10)
    arrow(ax, 420, 370, 420, 356, lw=2.0, ms=13, z=8)
    uc(ax, 340, 268, 160, "RegistrationService", ops=["+registerStudent()", "+dropCourse()"], name_size=10.5)
    arrow(ax, 390, 266, 250, 196, lw=1.8, ms=12, z=8)
    arrow(ax, 450, 266, 600, 196, lw=1.8, ms=12, z=8)
    uc(ax, 160, 128, 180, "Course", attrs=["capacity", "status"], ops=["isAvailable()"], name_size=10.5)
    uc(ax, 510, 128, 180, "Registration", attrs=["date", "status"], ops=["confirm()"], name_size=10.5)
    arrow(ax, 600, 126, 600, 108, lw=1.8, ms=12, z=8)
    uc(ax, 480, 28, 240, "RegistrationRepository", ops=["+save()", "+find()"], name_size=10.5)

    box(ax, 22, 8, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 21, "That is what it means to integrate the models into one design.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w14_integrated_design.png")


ALL = [
    progression, analysis_vs_design, transformation, three_models, multiple_views,
    use_case_flow, responsibility, design_class, visibility, sequence_to_class,
    consistency, object_dynamic, activity_mapping, controller, domain_knowledge,
    design_change, strategy, integrated_design,
]


if __name__ == "__main__":
    made = []
    for fn in ALL:
        try:
            p = fn()
            made.append(p.split(os.sep)[-1])
        except Exception as e:
            import traceback
            print(f"[FAIL] {fn.__name__}: {e}")
            traceback.print_exc()
    print("Generated", len(made), "week-14 visuals:")
    for m in made:
        print("  -", m)
