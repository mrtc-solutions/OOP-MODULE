"""
Week 10 visuals — OBJECT-ORIENTED DESIGN.
Analysis vs design · goals · responsibility · cohesion/coupling ·
abstraction/encapsulation · architecture · combining the three models.
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
# 1. Where Week 10 fits — analysis -> design
# --------------------------------------------------------------------------
def progression():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Where Week 10 Fits", sub="From \u201cwhat does the system need?\u201d to \u201chow will we build it?\u201d")

    box(ax, 22, 150, 380, 210, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    t(ax, 212, 330, "ANALYSIS", size=18, color=MAROON_DARK, fam=H_B, z=7)
    t(ax, 212, 296, "\u201cWhat does the system need?\u201d", size=12.5, color=INK, fam=BODY, z=7)
    t(ax, 212, 266, "requirements · use cases · objects · behaviour", size=10.5, color=GREY, fam=B_IT, z=7)
    t(ax, 212, 206, "Weeks 4\u20138", size=11, color=MAROON_SOFT, fam=B_SB, z=7)

    box(ax, 438, 150, 380, 210, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    t(ax, 628, 330, "DESIGN", size=18, color=MAROON, fam=H_B, z=7)
    t(ax, 628, 296, "\u201cHow will we build it?\u201d", size=12.5, color=INK, fam=BODY, z=7)
    t(ax, 628, 266, "classes · interfaces · architecture · responsibilities", size=10.5, color=GREY, fam=B_IT, z=7)
    t(ax, 628, 206, "Week 10 onward", size=11, color=MAROON_SOFT, fam=B_SB, z=7)

    arrow(ax, 406, 255, 434, 255, lw=2.6, ms=20)
    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Analysis = what the system needs · Design = how the software is organised to satisfy those needs.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w10_progression.png")


# --------------------------------------------------------------------------
# 2. House analogy — requirement vs design
# --------------------------------------------------------------------------
def house():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Design: The House Analogy", sub="A requirement states the goal · design decides how to achieve it")

    box(ax, 22, 96, 380, 236, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    t(ax, 212, 300, "REQUIREMENT", size=14, color=MAROON, fam=H_B, z=7)
    t(ax, 212, 262, "\u201cI want a three-bedroom house.\u201d", size=13, color=INK, fam=B_IT, z=7)
    t(ax, 212, 214, "That is WHAT the client wants.", size=11.5, color=GREY, fam=BODY, z=7)
    t(ax, 212, 150, "\u201cI want a student", size=12.5, color=INK, fam=B_IT, z=7)
    t(ax, 212, 124, "registration system.\u201d", size=12.5, color=INK, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 236, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    t(ax, 628, 300, "DESIGN", size=14, color=MAROON_DARK, fam=H_B, z=7)
    for i, s in enumerate(["where the rooms go", "where pipes / electricity run", "what materials to use", "how the building is supported"]):
        t(ax, 628, 262 - i * 30, s, size=11.5, color=INK, fam=BODY, z=7)
    t(ax, 628, 138, "classes · components · layers", size=11.5, color=MAROON_SOFT, fam=B_SB, z=7)
    t(ax, 628, 112, "communication · data · security", size=11.5, color=MAROON_SOFT, fam=B_SB, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Software design decides how the parts of a system are organised and how they work together.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w10_house.png")


# --------------------------------------------------------------------------
# 3. Analysis vs Design — WHAT vs HOW
# --------------------------------------------------------------------------
def analysis_vs_design():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Analysis vs Design", sub="The most important distinction of Week 10")

    box(ax, 22, 110, 380, 230, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    t(ax, 212, 312, "ANALYSIS", size=16, color=MAROON, fam=H_B, z=7)
    t(ax, 212, 278, "\u201cWHAT must be accomplished?\u201d", size=12.5, color=MAROON_SOFT, fam=B_SB, z=7)
    for i, s in enumerate(["business requirements", "user needs · domain concepts", "objects & relationships", "use cases · system behaviour"]):
        t(ax, 212, 232 - i * 30, s, size=11.5, color=INK, fam=BODY, z=7)

    box(ax, 438, 110, 380, 230, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    t(ax, 628, 312, "DESIGN", size=16, color=MAROON_DARK, fam=H_B, z=7)
    t(ax, 628, 278, "\u201cHOW should it be structured?\u201d", size=12.5, color=MAROON_SOFT, fam=B_SB, z=7)
    for i, s in enumerate(["classes · interfaces · components", "architecture · responsibilities", "data access · persistence", "security · technologies"]):
        t(ax, 628, 232 - i * 30, s, size=11.5, color=INK, fam=BODY, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Analysis understands the problem · Design plans the software solution.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w10_analysis_vs_design.png")


# --------------------------------------------------------------------------
# 4. Analysis model vs design model — table
# --------------------------------------------------------------------------
def analysis_design_model():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Analysis Model vs Design Model", sub="The analysis model is the foundation of the design model")

    rows = [
        ("Focus", "Understanding the problem", "Solving the problem"),
        ("Answers", "What the system needs", "How it will be built"),
        ("Nature", "More conceptual", "More technical"),
        ("Orientation", "Domain-oriented", "Implementation-oriented"),
        ("Technology", "Less technology-specific", "More technology-specific"),
    ]
    x0, w1, w2, w3 = 30, 140, 320, 310
    y_top, rh = 330, 44
    box(ax, x0, y_top - rh - len(rows) * rh - 16, w1 + w2 + w3, 16 + rh + len(rows) * rh, WHITE, ec=MAROON, lw=1.6, r=12, z=4)
    box(ax, x0, y_top - rh, w1 + w2 + w3, rh, MAROON, r=0, z=5)
    t(ax, x0 + w1 / 2, y_top - rh / 2, "", size=11, color=WHITE, fam=H_SB, z=6)
    t(ax, x0 + w1 + w2 / 2, y_top - rh / 2, "ANALYSIS MODEL", size=11.5, color=WHITE, fam=H_SB, z=6)
    t(ax, x0 + w1 + w2 + w3 / 2, y_top - rh / 2, "DESIGN MODEL", size=11.5, color=WHITE, fam=H_SB, z=6)
    for i, (k, a, dd) in enumerate(rows):
        yy = y_top - rh * (i + 1) - rh / 2
        fc = WHITE if i % 2 == 0 else MAROON_TINT
        box(ax, x0, y_top - rh * (i + 1) - rh, w1 + w2 + w3, rh, fc, r=0, z=5)
        t(ax, x0 + w1 / 2, yy, k, size=11.5, color=MAROON, fam=B_SB, z=6)
        t(ax, x0 + w1 + w2 / 2, yy, a, size=11.5, color=INK, fam=BODY, z=6)
        t(ax, x0 + w1 + w2 + w3 / 2, yy, dd, size=11.5, color=MAROON_SOFT, fam=BODY, z=6)
        ax.plot([x0, x0 + w1 + w2 + w3], [y_top - rh * (i + 1), y_top - rh * (i + 1)], color=GREY_LIGHT, lw=1.0, zorder=6)
    ax.plot([x0 + w1, x0 + w1], [y_top - rh, y_top - rh - len(rows) * rh], color=GREY_LIGHT, lw=1.0, zorder=6)
    ax.plot([x0 + w1 + w2, x0 + w1 + w2], [y_top - rh, y_top - rh - len(rows) * rh], color=GREY_LIGHT, lw=1.0, zorder=6)

    box(ax, 22, 18, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 31, "The analysis model describes logical structure · the design model adds implementation detail.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w10_analysis_design_model.png")


# --------------------------------------------------------------------------
# 5. Eight design goals
# --------------------------------------------------------------------------
def design_goals():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Design Goals", sub="What makes a good object-oriented design?")
    goals = [
        ("1", "Correctness", "satisfies the requirements"),
        ("2", "Maintainability", "change without breaking others"),
        ("3", "Reusability", "useful parts can be reused"),
        ("4", "Flexibility", "adapts to changing needs"),
        ("5", "Understandability", "developers grasp how it works"),
        ("6", "Testability", "parts can be tested in isolation"),
        ("7", "Scalability", "handles increased demand"),
        ("8", "Security", "protection built into the design"),
    ]
    cols, rows = 4, 2
    bw, bh, gx, gy = 186, 128, 14, 16
    x0 = (W - (cols * bw + (cols - 1) * gx)) / 2
    y0 = 150
    for i, (n, hd, sub) in enumerate(goals):
        r, c = divmod(i, cols)
        x = x0 + c * (bw + gx)
        y = y0 + (rows - 1 - r) * (bh + gy)
        box(ax, x, y, bw, bh, WHITE, ec=MAROON, lw=1.6, r=12, z=5)
        ax.add_patch(Circle((x + 26, y + bh - 26), 15, facecolor=MAROON, zorder=6))
        t(ax, x + 26, y + bh - 26, n, size=12, color=WHITE, fam=H_SB, z=7)
        t(ax, x + bw / 2 + 8, y + bh - 30, hd, size=12.5, color=MAROON, fam=B_SB, z=7)
        t(ax, x + bw / 2, y + bh / 2 - 8, sub, size=10.5, color=GREY, fam=B_IT, ha="center", z=7)
    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "A good design aims for all eight — they reinforce one another.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w10_design_goals.png")


# --------------------------------------------------------------------------
# 6. Poor vs good design
# --------------------------------------------------------------------------
def poor_vs_good():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Poor vs Good Design", sub="One huge class vs focused responsibilities")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "POOR DESIGN", size=14, color=MAROON_SOFT, fam=H_B, z=6)
    uc(ax, 108, 116, 208, "UniversitySystem",
       ops=["login()", "registerCourse()", "payFees()", "sendEmail()", "generateReports()", "connectDatabase()"],
       ec=MAROON_SOFT, name_size=11)
    t(ax, 212, 104, "everything in one huge class", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "BETTER DESIGN", size=14, color=MAROON, fam=H_B, z=6)
    for r in range(3):
        for c in range(2):
            x = 462 + c * 170
            y = 186 + (2 - r) * 40
            box(ax, x, y, 158, 30, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
    names = ["AuthenticationService", "RegistrationService", "PaymentService", "EmailService", "ReportService", "ResultService"]
    for i, n in enumerate(names):
        r, c = divmod(i, 2)
        x = 462 + c * 170
        y = 186 + (2 - r) * 40
        t(ax, x + 79, y + 15, n, size=9.5, color=MAROON_SOFT, fam=B_SB, z=7)
    t(ax, 628, 116, "each component has a focused responsibility", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Good design spreads responsibilities across focused components.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w10_poor_vs_good.png")


# --------------------------------------------------------------------------
# 7. Responsibility — knowing vs doing
# --------------------------------------------------------------------------
def responsibility():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Responsibility", sub="What an object knows · what it does")

    panels = [
        (44, "Student", "KNOWS", ["studentID", "name", "programme"], "DOES", ["registerCourse()", "dropCourse()"]),
        (314, "Course", "KNOWS", ["courseCode", "title", "credits", "capacity"], "DOES", ["hasSpace()"]),
        (584, "Payment", "KNOWS", ["amount", "date", "status"], "DOES", ["process()", "refund()"]),
    ]
    for x, name, k, attrs, dd, ops in panels:
        box(ax, x, 96, 212, 246, WHITE, ec=MAROON, lw=1.7, r=14, z=5)
        t(ax, x + 106, 314, name, size=14, color=MAROON, fam=H_B, z=6)
        t(ax, x + 106, 282, k + "  \u2014  " + ", ".join(attrs), size=9.5, color=INK, fam=BODY, z=6)
        ax.plot([x + 20, x + 192], [262, 262], color=GREY_LIGHT, lw=1.0, zorder=6)
        t(ax, x + 106, 232, dd + "  \u2014  " + " · ".join(ops), size=9.5, color=MAROON_SOFT, fam=BODY, z=6)
        box(ax, x + 20, 110, 172, 30, MAROON_TINT, ec="none", r=8, z=6)
        t(ax, x + 106, 125, "knowing + doing", size=10, color=MAROON_DARK, fam=B_SB, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "A responsibility is something a class is responsible for knowing or doing.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w10_responsibility.png")


# --------------------------------------------------------------------------
# 8. Cohesion — high vs low
# --------------------------------------------------------------------------
def cohesion():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Cohesion", sub="How closely related are the responsibilities inside a class?")

    box(ax, 22, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "HIGH COHESION  (good)", size=13.5, color=MAROON, fam=H_B, z=6)
    uc(ax, 120, 118, 184, "Course", attrs=["courseCode", "title", "capacity"], ops=["hasSpace()", "addStudent()"], name_size=11)
    t(ax, 212, 106, "all about a course", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "LOW COHESION  (bad)", size=13.5, color=MAROON_SOFT, fam=H_B, z=6)
    uc(ax, 536, 118, 184, "Student", ops=["registerCourse()", "payFees()", "sendSMS()", "generatePDF()", "calculateTax()"], ec=MAROON_SOFT, name_size=11)
    t(ax, 628, 106, "too many unrelated things", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Ask: does everything inside this class belong together?",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w10_cohesion.png")


# --------------------------------------------------------------------------
# 9. Coupling — high vs low
# --------------------------------------------------------------------------
def coupling():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Coupling", sub="How strongly does a class depend on other classes?")

    # high coupling chain
    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "HIGH COUPLING  (bad)", size=13.5, color=MAROON_SOFT, fam=H_B, z=6)
    chain = ["Student", "Payment", "Database", "Email", "SMS", "Report"]
    for i, n in enumerate(chain):
        x = 70 + i * 60
        box(ax, x, 150, 52, 34, MAROON_SOFT, r=7, z=6)
        t(ax, x + 26, 167, n, size=8.5, color=WHITE, fam=B_SB, z=7)
        if i < len(chain) - 1:
            arrow(ax, x + 53, 167, x + 69, 167, color=MAROON_SOFT, lw=1.8, ms=12, z=8)
    t(ax, 212, 116, "every class depends directly on others", size=10.5, color=GREY, fam=B_IT, z=7)

    # low coupling
    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "LOW COUPLING  (good)", size=13.5, color=MAROON, fam=H_B, z=6)
    box(ax, 500, 224, 110, 40, MAROON, r=8, z=6)
    t(ax, 555, 244, "Student", size=11, color=WHITE, fam=B_SB, z=7)
    box(ax, 660, 224, 110, 40, MAROON_SOFT, r=8, z=6)
    t(ax, 715, 244, "Service", size=11, color=WHITE, fam=B_SB, z=7)
    arrow(ax, 612, 244, 658, 244, lw=2.0, ms=14, z=8)
    box(ax, 580, 150, 110, 30, WHITE, ec=MAROON, lw=1.5, r=8, z=6)
    t(ax, 635, 165, "<<interface>>", size=9, color=MAROON, fam=B_SB, z=7)
    arrow(ax, 635, 222, 635, 184, lw=2.0, ms=14, z=8)
    box(ax, 470, 90, 110, 30, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
    t(ax, 525, 105, "BankPayment", size=9.5, color=INK, fam=BODY, z=7)
    box(ax, 690, 90, 110, 30, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
    t(ax, 745, 105, "MobileMoney", size=9.5, color=INK, fam=BODY, z=7)
    arrow(ax, 525, 148, 528, 124, lw=1.5, ms=10, z=8)
    arrow(ax, 745, 148, 742, 124, lw=1.5, ms=10, z=8)
    t(ax, 628, 130, "", size=10, color=INK, fam=BODY, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Depend on abstractions (interfaces), not on concrete implementations.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w10_coupling.png")


# --------------------------------------------------------------------------
# 10. Cohesion vs coupling — combined formula
# --------------------------------------------------------------------------
def cohesion_coupling():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Cohesion vs Coupling", sub="One looks inside · the other looks between")

    box(ax, 22, 96, 340, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 192, 314, "COHESION", size=14, color=MAROON, fam=H_B, z=6)
    t(ax, 192, 280, "looks INSIDE a component", size=11.5, color=GREY, fam=B_IT, z=7)
    box(ax, 120, 150, 144, 70, WHITE, ec=MAROON, lw=1.5, r=10, z=6)
    t(ax, 192, 205, "Class A", size=11, color=MAROON, fam=B_SB, z=7)
    t(ax, 192, 176, "related parts?", size=10.5, color=INK, fam=BODY, z=7)

    box(ax, 388, 96, 340, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 558, 314, "COUPLING", size=14, color=MAROON, fam=H_B, z=6)
    t(ax, 558, 280, "looks BETWEEN components", size=11.5, color=GREY, fam=B_IT, z=7)
    box(ax, 462, 150, 84, 70, WHITE, ec=MAROON, lw=1.5, r=10, z=6)
    t(ax, 504, 195, "A", size=11, color=MAROON, fam=B_SB, z=7)
    box(ax, 578, 150, 84, 70, WHITE, ec=MAROON, lw=1.5, r=10, z=6)
    t(ax, 620, 195, "B", size=11, color=MAROON, fam=B_SB, z=7)
    arrow(ax, 548, 185, 576, 185, lw=1.8, ms=12, z=8)
    t(ax, 562, 120, "how strong the dependency?", size=10.5, color=INK, fam=BODY, z=7)

    box(ax, 748, 96, 72, 246, MAROON, r=14, z=5)
    t(ax, 784, 316, "GOOD", size=13, color=GOLD_LIGHT, fam=H_B, z=6)
    t(ax, 784, 288, "DESIGN", size=13, color=GOLD_LIGHT, fam=H_B, z=6)
    t(ax, 784, 196, "HIGH", size=13, color=WHITE, fam=B_B, z=6)
    t(ax, 784, 172, "COHESION", size=10, color=WHITE, fam=B_B, z=6)
    t(ax, 784, 140, "+", size=13, color=GOLD, fam=B_B, z=6)
    t(ax, 784, 112, "LOW", size=13, color=WHITE, fam=B_B, z=6)
    t(ax, 784, 88, "COUPLING", size=10, color=WHITE, fam=B_B, z=6)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Good design = high cohesion + low coupling.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w10_cohesion_coupling.png")


# --------------------------------------------------------------------------
# 11. Abstraction vs encapsulation
# --------------------------------------------------------------------------
def abstraction_encapsulation():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Abstraction vs Encapsulation", sub="What the user sees · what the object hides")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "ABSTRACTION", size=14, color=MAROON, fam=H_B, z=6)
    t(ax, 212, 280, "\u201cWhat should the user see?\u201d", size=11.5, color=GREY, fam=B_IT, z=7)
    uc(ax, 130, 128, 164, "PaymentProcessor", ops=["processPayment()"], name_size=10.5)
    t(ax, 212, 112, "just call processPayment()", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "ENCAPSULATION", size=14, color=MAROON_DARK, fam=H_B, z=6)
    t(ax, 628, 280, "\u201cWhat should the object hide / protect?\u201d", size=11.5, color=GREY, fam=B_IT, z=7)
    uc(ax, 546, 128, 164, "BankAccount", attrs=["-balance"], ops=["+deposit()", "+withdraw()", "+getBalance()"], name_size=10.5)
    t(ax, 628, 112, "balance is not changed from outside", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Abstraction = hide complexity · Encapsulation = protect internal state.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w10_abstraction_encapsulation.png")


# --------------------------------------------------------------------------
# 12. Separation of concerns — layers
# --------------------------------------------------------------------------
def separation():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Separation of Concerns", sub="Different concerns handled by the appropriate part")

    # bad
    box(ax, 22, 96, 320, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 182, 314, "MIXED TOGETHER  (bad)", size=12.5, color=MAROON_SOFT, fam=H_B, z=6)
    box(ax, 52, 132, 260, 150, MAROON_SOFT, r=12, z=6)
    t(ax, 182, 256, "LoginScreen", size=12, color=WHITE, fam=B_SB, z=7)
    for i, s in enumerate(["SQL queries", "password hashing", "authentication logic", "HTML generation", "database connection"]):
        t(ax, 182, 224 - i * 24, s, size=10, color=GOLD_LIGHT, fam=BODY, z=7)

    # good
    box(ax, 372, 96, 446, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 595, 314, "SEPARATED  (good)", size=12.5, color=MAROON, fam=H_B, z=6)
    layers = [
        ("Login UI", MAROON),
        ("Authentication Service", MAROON_SOFT),
        ("User Repository", MAROON_SOFT),
        ("Database", MAROON_DARK),
    ]
    for i, (name, colr) in enumerate(layers):
        y = 238 - i * 42
        box(ax, 420, y, 350, 32, colr, r=8, z=6)
        t(ax, 595, y + 16, name, size=11, color=WHITE, fam=B_SB, z=7)
        if i < len(layers) - 1:
            arrow(ax, 595, y - 2, 595, y - 12, lw=2.0, ms=12, z=8)
    t(ax, 595, 88, "each layer has a clearer responsibility", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Divide a system so each concern is handled by an appropriate part.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w10_separation.png")


# --------------------------------------------------------------------------
# 13. Three-layer architecture with example
# --------------------------------------------------------------------------
def architecture():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Three-Layer Architecture", sub="The high-level organisation of a software system")

    layers = [
        ("PRESENTATION LAYER", "Web / Mobile / Desktop UI", MAROON),
        ("BUSINESS LOGIC LAYER", "rules · services · use cases", MAROON_SOFT),
        ("DATA LAYER", "repositories · database", MAROON_DARK),
    ]
    for i, (hd, sub, colr) in enumerate(layers):
        y = 130 + i * 72
        box(ax, 60, y, 720, 56, colr, r=12, z=6)
        t(ax, 420, y + 38, hd, size=13, color=WHITE, fam=H_SB, z=7)
        t(ax, 420, y + 17, sub, size=11, color=GOLD_LIGHT, fam=B_IT, z=7)
        if i < len(layers) - 1:
            arrow(ax, 420, y - 2, 420, y - 12, lw=2.4, ms=16, z=8)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Presentation -> Business Logic -> Data Access -> Database.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w10_architecture.png")


# --------------------------------------------------------------------------
# 14. Refinement — analysis -> design -> code
# --------------------------------------------------------------------------
def refinement():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Refinement", sub="Progressively add detail: analysis -> design -> code")

    # analysis
    box(ax, 22, 130, 240, 160, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 142, 262, "ANALYSIS", size=13, color=MAROON, fam=H_B, z=6)
    uc(ax, 74, 150, 136, "Student", name_size=10.5)
    t(ax, 142, 138, "conceptual class", size=10, color=GREY, fam=B_IT, z=7)

    # design
    box(ax, 300, 130, 240, 160, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 420, 262, "DESIGN", size=13, color=MAROON_DARK, fam=H_B, z=6)
    uc(ax, 342, 106, 156, "Student",
       attrs=["studentId: String", "name: String", "email: String"],
       ops=["registerCourse()", "dropCourse()"],
       name_size=10.5)
    t(ax, 420, 94, "types · visibility · operations", size=10, color=GREY, fam=B_IT, z=7)

    # code
    box(ax, 578, 130, 240, 160, MAROON, r=14, z=5)
    t(ax, 698, 262, "CODE", size=13, color=WHITE, fam=H_B, z=6)
    t(ax, 698, 222, "Student.java", size=11, color=GOLD_LIGHT, fam=B_SB, z=7)
    t(ax, 698, 196, "Student.cs", size=11, color=GOLD_LIGHT, fam=B_SB, z=7)
    t(ax, 698, 170, "Student.ts", size=11, color=GOLD_LIGHT, fam=B_SB, z=7)
    t(ax, 698, 144, "chosen technology", size=10, color=GREY, fam=B_IT, z=7)

    arrow(ax, 266, 210, 298, 210, lw=2.4, ms=16, z=8)
    arrow(ax, 544, 210, 576, 210, lw=2.4, ms=16, z=8)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Problem -> analysis model -> design model -> implementation -> running software.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w10_refinement.png")


# --------------------------------------------------------------------------
# 15. The three models
# --------------------------------------------------------------------------
def three_models():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Three OOAD Models", sub="Structure · time/state · interaction")

    cards = [
        (22, "OBJECT MODEL", "\u201cWhat things / classes exist?\u201d", ["Student", "Course", "Registration", "Payment"], MAROON),
        (300, "DYNAMIC MODEL", "\u201cHow do objects change over time?\u201d", ["Requested", "Pending", "Confirmed", "Rejected"], MAROON_SOFT),
        (578, "BEHAVIOURAL MODEL", "\u201cWhat do users / objects do?\u201d", ["Register Course", "Validate Registration", "Confirm Registration"], MAROON_DARK),
    ]
    for x, hd, q, items, colr in cards:
        box(ax, x, 96, 240, 246, WHITE, ec=colr, lw=1.8, r=14, z=5)
        box(ax, x, 306, 240, 36, colr, r=12, z=6)
        t(ax, x + 120, 324, hd, size=12.5, color=WHITE, fam=H_SB, z=7)
        t(ax, x + 120, 274, q, size=11, color=GREY, fam=B_IT, z=7)
        for i, s in enumerate(items):
            y = 224 - i * 30
            box(ax, x + 30, y - 12, 180, 24, MAROON_TINT if colr != MAROON_DARK else "#F1E2E2", ec="none", r=8, z=6)
            t(ax, x + 120, y, s, size=10.5, color=INK, fam=BODY, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Structure + behaviour + time/state must fit together.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w10_three_models.png")


# --------------------------------------------------------------------------
# 16. Case study — combining the models (7 steps)
# --------------------------------------------------------------------------
def integration():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Combining the Models", sub="Case study: online course registration")

    steps = [
        ("1", "Requirement", "\u201cStudent registers for an available course\u201d"),
        ("2", "Use Case", "Student -> Register Course"),
        ("3", "Objects", "Student · Course · Registration"),
        ("4", "Object Model", "classes + associations"),
        ("5", "Dynamic Model", "Requested -> Validated -> Confirmed"),
        ("6", "Sequence", "who calls whom, in what order"),
        ("7", "Design", "Service + Repositories"),
    ]
    # two rows: 4 + 3
    for i, (n, hd, sub) in enumerate(steps):
        r = i // 4
        c = i % 4
        if r == 0:
            x = 22 + c * 200
            y = 200
            bw = 186
        else:
            x = 122 + c * 200
            y = 96
            bw = 186
        box(ax, x, y, bw, 82, WHITE if r == 0 else MAROON_TINT, ec=MAROON, lw=1.6, r=12, z=5)
        ax.add_patch(Circle((x + 24, y + 58), 14, facecolor=MAROON, zorder=6))
        t(ax, x + 24, y + 58, n, size=11, color=WHITE, fam=H_SB, z=7)
        t(ax, x + bw / 2 + 10, y + 58, hd, size=11.5, color=MAROON, fam=B_SB, z=7)
        t(ax, x + bw / 2, y + 26, sub, size=9.5, color=GREY, fam=B_IT, z=7)
    arrow(ax, 320, 200, 338, 200, lw=2.0, ms=13, z=8)
    arrow(ax, 520, 200, 538, 200, lw=2.0, ms=13, z=8)
    arrow(ax, 720, 200, 738, 200, lw=2.0, ms=13, z=8)
    arrow(ax, 330, 182, 330, 164, lw=2.0, ms=13, z=8)
    arrow(ax, 520, 182, 520, 164, lw=2.0, ms=13, z=8)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Analysis flows into design — the three models support one another.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w10_integration.png")


# --------------------------------------------------------------------------
# 17. Traceability
# --------------------------------------------------------------------------
def traceability():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Traceability", sub="Follow a requirement through every development artefact")

    chain = [
        ("Requirement", "\u201cStudent can register\u201d"),
        ("Use Case", "Register Course"),
        ("Activity", "registration workflow"),
        ("Sequence", "object interaction"),
        ("Class Model", "Student · Course · Registration"),
        ("Design Classes", "Service · Repositories"),
        ("Code", "implemented classes"),
        ("Test Case", "verifies the requirement"),
    ]
    cw, gap, x0 = 190, 12, 22
    for i, (hd, sub) in enumerate(chain):
        r, c = divmod(i, 4)
        x = x0 + c * (cw + gap)
        y = 232 - r * 124
        box(ax, x, y, cw, 70, WHITE if r == 0 else MAROON_TINT, ec=MAROON, lw=1.6, r=12, z=5)
        t(ax, x + cw / 2, y + 47, hd, size=11.5, color=MAROON, fam=B_SB, z=6)
        t(ax, x + cw / 2, y + 21, sub, size=9, color=GREY, fam=B_IT, z=6)
        if i < len(chain) - 1:
            if c < 3:
                arrow(ax, x + cw + 2, y + 35, x + cw + gap - 2, y + 35, lw=2.0, ms=12, z=8)
            else:
                arrow(ax, x + cw / 2, y - 2, x + cw / 2, y - 12, lw=2.0, ms=12, z=8)

    box(ax, 22, 18, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 31, "If a requirement changes, traceability shows which models and code may be affected.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w10_traceability.png")


# --------------------------------------------------------------------------
# 18. Master diagram
# --------------------------------------------------------------------------
def master():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Week 10 Master Diagram", sub="Requirements -> analysis -> integrated models -> design -> code")

    def flow_box(x, y, w, h, txt, fill=WHITE, ec=MAROON, size=10.5, color=INK, fam=B_SB):
        box(ax, x, y, w, h, fill, ec=ec, lw=1.6, r=10, z=5)
        t(ax, x + w / 2, y + h / 2, txt, size=size, color=color, fam=fam, z=6)

    flow_box(348, 404, 144, 40, "REQUIREMENTS", MAROON, ec=MAROON, size=11, color=WHITE)
    flow_box(348, 350, 144, 40, "USE CASES", WHITE)
    arrow(ax, 420, 402, 420, 394, lw=2.0, ms=13, z=8)
    flow_box(348, 296, 144, 40, "ANALYSIS", MAROON_SOFT, ec=MAROON_SOFT, size=11, color=WHITE)
    arrow(ax, 420, 348, 420, 340, lw=2.0, ms=13, z=8)

    # three models
    models = [("OBJECT MODEL", "\u201cwhat exists?\u201d"), ("DYNAMIC MODEL", "\u201cwhat changes?\u201d"), ("BEHAVIOURAL MODEL", "\u201cwhat happens?\u201d")]
    for i, (hd, sub) in enumerate(models):
        x = 30 + i * 276
        box(ax, x, 200, 260, 64, WHITE, ec=MAROON, lw=1.6, r=12, z=5)
        t(ax, x + 130, 246, hd, size=11.5, color=MAROON, fam=B_SB, z=6)
        t(ax, x + 130, 218, sub, size=10, color=GREY, fam=B_IT, z=6)
    arrow(ax, 420, 294, 160, 268, lw=2.0, ms=13, z=8)
    arrow(ax, 420, 294, 420, 268, lw=2.0, ms=13, z=8)
    arrow(ax, 420, 294, 680, 268, lw=2.0, ms=13, z=8)

    flow_box(348, 134, 144, 40, "INTEGRATED MODEL", MAROON_TINT, ec=MAROON, size=10.5, color=MAROON_DARK)
    arrow(ax, 160, 198, 348, 176, lw=1.8, ms=12, z=8)
    arrow(ax, 420, 198, 420, 176, lw=1.8, ms=12, z=8)
    arrow(ax, 680, 198, 492, 176, lw=1.8, ms=12, z=8)

    flow_box(348, 80, 144, 40, "DESIGN", MAROON, ec=MAROON, size=11, color=WHITE)
    arrow(ax, 420, 132, 420, 124, lw=2.0, ms=13, z=8)

    flow_box(348, 26, 144, 40, "CODE", MAROON_DARK, ec=MAROON_DARK, size=11, color=GOLD_LIGHT)
    arrow(ax, 420, 78, 420, 70, lw=2.0, ms=13, z=8)

    return save(fig, "w10_master.png")


ALL = [
    progression, house, analysis_vs_design, analysis_design_model, design_goals,
    poor_vs_good, responsibility, cohesion, coupling, cohesion_coupling,
    abstraction_encapsulation, separation, architecture, refinement,
    three_models, integration, traceability, master,
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
    print("Generated", len(made), "week-10 visuals:")
    for m in made:
        print("  -", m)
