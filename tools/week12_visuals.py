"""
Week 12 visuals — INTEGRATED OBJECT-ORIENTED MODELLING AND DESIGN.
Consistency · model views · traceability · packages · architecture ·
components · validation · the integrated example.
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
# 1. Progression Week 11 -> 12 -> 13
# --------------------------------------------------------------------------
def progression():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Week 11 -> 12 -> 13", sub="From detailed design elements to one coherent system")

    cols = [
        ("WEEK 11", "DESIGN REFINEMENT", "\u201cHow do I turn analysis models\ninto detailed design elements?\u201d", MAROON),
        ("WEEK 12", "INTEGRATED MODELLING", "\u201cHow do all these models\nwork together as one system?\u201d", MAROON_SOFT),
        ("WEEK 13", "MULTILAYER SYSTEMS", "\u201cReusable, adaptable components\nin a multilayer architecture.\u201d", MAROON_DARK),
    ]
    for i, (wk, hd, sub, colr) in enumerate(cols):
        x = 30 + i * 268
        box(ax, x, 110, 244, 216, WHITE, ec=colr, lw=1.8, r=14, z=5)
        box(ax, x, 288, 244, 38, colr, r=12, z=6)
        t(ax, x + 122, 307, wk, size=12.5, color=WHITE, fam=H_SB, z=7)
        t(ax, x + 122, 254, hd, size=13, color=MAROON_DARK, fam=H_B, z=7)
        t(ax, x + 122, 186, sub, size=10.5, color=GREY, fam=B_IT, z=7)
        if i < 2:
            arrow(ax, x + 248, 220, x + 264, 220, lw=2.4, ms=16, z=8)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Week 12 brings every model together into one coherent, consistent system design.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w12_progression.png")


# --------------------------------------------------------------------------
# 2. Integrated modelling — house analogy
# --------------------------------------------------------------------------
def house_analogy():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Integrated Modelling: The House Analogy", sub="Different drawings must describe the SAME house")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "CONSISTENT DRAWINGS", size=13, color=MAROON, fam=H_B, z=6)
    for i, s in enumerate(["Architectural: 3 bedrooms", "Electrical: 3 bedrooms", "Plumbing: 3 bedrooms"]):
        box(ax, 60, 218 - i * 40, 304, 30, MAROON_TINT, r=8, z=6)
        t(ax, 212, 233 - i * 40, s, size=11, color=INK, fam=BODY, z=7)
    t(ax, 212, 96, "same house -> agree", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "CONTRADICTORY DRAWINGS", size=13, color=MAROON_SOFT, fam=H_B, z=6)
    for i, s in enumerate(["Architectural: 3 bedrooms", "Electrical: 5 bedrooms", "Plumbing: 2 bedrooms"]):
        box(ax, 476, 218 - i * 40, 304, 30, WHITE, ec=MAROON_SOFT, lw=1.4, r=8, z=6)
        t(ax, 628, 233 - i * 40, s, size=11, color=MAROON_SOFT, fam=BODY, z=7)
    t(ax, 628, 96, "the drawings contradict each other", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Software models work the same way — they must collectively tell a coherent story.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w12_house_analogy.png")


# --------------------------------------------------------------------------
# 3. Different models answer different questions
# --------------------------------------------------------------------------
def model_views():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Different Models, Different Questions", sub="Many views of the same system")

    views = [
        ("Use-case model", "What does the user want to accomplish?"),
        ("Class model", "What objects/classes make up the system?"),
        ("Sequence diagram", "How do objects communicate to accomplish a task?"),
        ("State machine", "How does an object change state?"),
        ("Activity diagram", "What activities and decisions occur in a process?"),
        ("Component / deployment", "How is the software organised and deployed?"),
    ]
    for i, (hd, sub) in enumerate(views):
        r, c = divmod(i, 3)
        x = 30 + c * 268
        y = 200 - r * 112
        box(ax, x, y, 244, 88, WHITE if r == 0 else MAROON_TINT, ec=MAROON, lw=1.6, r=12, z=5)
        t(ax, x + 122, y + 62, hd, size=12.5, color=MAROON, fam=B_SB, z=6)
        t(ax, x + 122, y + 26, sub, size=10, color=GREY, fam=B_IT, z=6)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "UML groups structural modelling and behavioural modelling into different parts of its specification.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w12_model_views.png")


# --------------------------------------------------------------------------
# 4. The big picture
# --------------------------------------------------------------------------
def big_picture():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Big Picture", sub="Requirements -> models -> integrated design -> implementation")

    def fb(x, y, w, h, txt, fill=WHITE, ec=MAROON, size=10.5, color=INK):
        box(ax, x, y, w, h, fill, ec=ec, lw=1.6, r=10, z=5)
        t(ax, x + w / 2, y + h / 2, txt, size=size, color=color, fam=B_SB, z=6)

    fb(348, 406, 144, 38, "REQUIREMENTS", MAROON, ec=MAROON, size=11, color=WHITE)
    fb(348, 352, 144, 38, "USE-CASE MODEL", WHITE)
    arrow(ax, 420, 404, 420, 394, lw=2.0, ms=13, z=8)
    arrow(ax, 420, 350, 420, 340, lw=2.0, ms=13, z=8)

    models = [("OBJECT MODEL", "class diagram"), ("DYNAMIC MODEL", "state model"), ("BEHAVIOURAL MODEL", "sequence / activity")]
    for i, (hd, sub) in enumerate(models):
        x = 30 + i * 276
        box(ax, x, 210, 260, 62, WHITE, ec=MAROON, lw=1.6, r=12, z=5)
        t(ax, x + 130, 254, hd, size=11.5, color=MAROON, fam=B_SB, z=6)
        t(ax, x + 130, 226, sub, size=10, color=GREY, fam=B_IT, z=6)
    arrow(ax, 420, 308, 160, 276, lw=1.8, ms=12, z=8)
    arrow(ax, 420, 308, 420, 276, lw=1.8, ms=12, z=8)
    arrow(ax, 420, 308, 680, 276, lw=1.8, ms=12, z=8)

    fb(348, 148, 144, 38, "INTEGRATED DESIGN", MAROON_TINT, ec=MAROON, size=10.5, color=MAROON_DARK)
    arrow(ax, 160, 208, 348, 188, lw=1.8, ms=12, z=8)
    arrow(ax, 420, 208, 420, 188, lw=1.8, ms=12, z=8)
    arrow(ax, 680, 208, 492, 188, lw=1.8, ms=12, z=8)

    fb(348, 94, 144, 38, "IMPLEMENTATION", MAROON_DARK, ec=MAROON_DARK, size=11, color=GOLD_LIGHT)
    arrow(ax, 420, 146, 420, 136, lw=2.0, ms=13, z=8)

    return save(fig, "w12_big_picture.png")


# --------------------------------------------------------------------------
# 5. Consistency — an inconsistency example
# --------------------------------------------------------------------------
def consistency():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Model Consistency", sub="The models must agree — here they do not")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "USE-CASE MODEL", size=13, color=MAROON, fam=H_B, z=6)
    box(ax, 80, 210, 264, 50, MAROON_TINT, r=10, z=6)
    t(ax, 212, 235, "Student \u2014 Register for Course", size=12, color=MAROON_DARK, fam=B_SB, z=7)
    t(ax, 212, 160, "says the system supports registration", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "CLASS MODEL", size=13, color=MAROON_SOFT, fam=H_B, z=6)
    for i, s in enumerate(["Student", "Teacher", "Department"]):
        box(ax, 516, 210 - i * 38, 224, 30, WHITE, ec=MAROON_SOFT, lw=1.4, r=8, z=6)
        t(ax, 628, 225 - i * 38, s, size=11, color=MAROON_SOFT, fam=BODY, z=7)
    t(ax, 628, 96, "no Course, no Registration", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "The class model lacks the objects needed to support the use case \u2014 the models are inconsistent.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w12_consistency.png")


# --------------------------------------------------------------------------
# 6. Traceability
# --------------------------------------------------------------------------
def traceability():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Traceability", sub="Where did this design element come from? Which requirement does it support?")

    chain = [
        ("R01", "\u201cStudents can register for courses\u201d"),
        ("Use Case", "Register for Course"),
        ("Sequence", "registration interaction"),
        ("Classes", "Student · Course · Registration · RegistrationService"),
        ("Operations", "register() · checkCapacity() · checkPrerequisite()"),
    ]
    n = len(chain)
    cw, gap, x0 = 190, 12, 22
    for i, (hd, sub) in enumerate(chain):
        r, c = divmod(i, 3)
        x = x0 + c * (cw + gap)
        y = 268 - r * 132
        colr = MAROON if r == 0 else MAROON_SOFT
        box(ax, x, y, cw, 76, WHITE if r == 0 else MAROON_TINT, ec=colr, lw=1.6, r=12, z=5)
        t(ax, x + cw / 2, y + 52, hd, size=11.5, color=colr, fam=B_SB, z=6)
        t(ax, x + cw / 2, y + 22, sub, size=9, color=GREY, fam=B_IT, z=6)
        if i < n - 1:
            if c < 2:
                arrow(ax, x + cw + 2, y + 38, x + cw + gap - 2, y + 38, lw=2.0, ms=12, z=8)
            else:
                arrow(ax, x + cw / 2, y - 2, x + cw / 2, y - 12, lw=2.0, ms=12, z=8)

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "A traceable design links every element back to a requirement.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w12_traceability.png")


# --------------------------------------------------------------------------
# 7. Sequence diagram
# --------------------------------------------------------------------------
def sequence():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Registration Sequence", sub="How objects collaborate to accomplish the task")

    objs = ["Student", "RegistrationService", "Course", "Registration"]
    xs = [120, 360, 600, 780]
    top, bot = 330, 70
    for x, name in zip(xs, objs):
        box(ax, x - 62, top, 124, 34, MAROON, r=8, z=6)
        t(ax, x, top + 17, name, size=11, color=WHITE, fam=B_SB, z=7)
        ax.plot([x, x], [top, bot], color=GREY, lw=1.2, ls=(0, (4, 3)), zorder=5)

    msgs = [
        (120, 360, "register(course)", 330 - 26),
        (360, 600, "checkCapacity()", 330 - 52),
        (600, 360, "", 330 - 78),
        (360, 600, "checkPrerequisite()", 330 - 104),
        (600, 360, "", 330 - 130),
        (360, 780, "createRegistration()", 330 - 156),
        (780, 360, "", 330 - 182),
        (360, 120, "confirmation", 330 - 208),
    ]
    for x1, x2, label, y in msgs:
        arrow(ax, x1 + 2, y, x2 - 2, y, lw=1.8, ms=11, z=8)
        if label:
            t(ax, (x1 + x2) / 2, y + 10, label, size=9.5, color=MAROON_SOFT, fam=MONO, z=8)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "The sequence diagram provides the detail the use case alone does not give.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w12_sequence.png")


# --------------------------------------------------------------------------
# 8. State machine
# --------------------------------------------------------------------------
def state_machine():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Registration State Model", sub="How a registration changes state")

    inode(ax, 120, 300)
    state(ax, 180, 276, 170, 48, "REQUESTED")
    state(ax, 430, 276, 170, 48, "VALIDATED")
    state(ax, 430, 150, 170, 48, "CONFIRMED")
    state(ax, 180, 150, 170, 48, "REJECTED")
    state(ax, 680, 150, 150, 48, "CANCELLED")
    arrow(ax, 122, 300, 178, 300, lw=2.0, ms=13, z=8)
    arrow(ax, 352, 300, 428, 300, lw=2.0, ms=13, z=8)
    t(ax, 390, 310, "validation", size=10, color=GREY, fam=B_IT, z=8)
    arrow(ax, 470, 276, 470, 202, lw=2.0, ms=13, z=8)
    t(ax, 512, 240, "valid", size=10, color=GREY, fam=B_IT, z=8)
    arrow(ax, 470, 276, 300, 202, lw=2.0, ms=13, z=8)
    t(ax, 360, 250, "invalid", size=10, color=GREY, fam=B_IT, z=8)
    arrow(ax, 470, 174, 678, 174, lw=2.0, ms=13, z=8)
    t(ax, 560, 186, "cancellation", size=10, color=GREY, fam=B_IT, z=8)
    fnode(ax, 758, 174)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "The state model makes the business rules explicit \u2014 e.g. can a cancelled registration be confirmed again?",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w12_state_machine.png")


# --------------------------------------------------------------------------
# 9. Activity diagram
# --------------------------------------------------------------------------
def activity():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Registration Activity", sub="What activities and decisions occur in the workflow?")

    def ab(x, y, w, txt, fill=WHITE, ec=MAROON, size=10.5, color=INK, fam=B_SB):
        box(ax, x, y, w, 34, fill, ec=ec, lw=1.5, r=10, z=5)
        t(ax, x + w / 2, y + 17, txt, size=size, color=color, fam=fam, z=6)

    ab(340, 412, 160, "START", MAROON, ec=MAROON, size=11, color=WHITE)
    arrow(ax, 420, 410, 420, 402, lw=1.8, ms=12, z=8)
    ab(310, 366, 220, "Student logs in")
    arrow(ax, 420, 364, 420, 356, lw=1.8, ms=12, z=8)
    ab(310, 320, 220, "Student selects course")
    arrow(ax, 420, 318, 420, 310, lw=1.8, ms=12, z=8)
    ab(310, 274, 220, "Check prerequisites")
    arrow(ax, 420, 272, 420, 264, lw=1.8, ms=12, z=8)

    ax.add_patch(Polygon([(420, 252), (360, 228), (420, 204), (480, 228)], closed=True,
                         facecolor=MAROON_TINT, edgecolor=MAROON, lw=1.6, zorder=5))
    t(ax, 420, 228, "pass?", size=10, color=MAROON_DARK, fam=B_SB, z=7)
    ab(120, 204, 170, "Reject (NO)", WHITE, ec=MAROON_SOFT, size=9.5, color=MAROON_SOFT)
    arrow(ax, 360, 228, 294, 222, lw=1.8, ms=12, z=8)

    arrow(ax, 420, 228, 420, 196, lw=1.8, ms=12, z=8)
    t(ax, 436, 210, "YES", size=9.5, color=MAROON_SOFT, fam=B_SB, z=8)
    ab(310, 160, 220, "Check capacity")
    arrow(ax, 420, 158, 420, 150, lw=1.8, ms=12, z=8)

    ax.add_patch(Polygon([(420, 138), (360, 114), (420, 90), (480, 114)], closed=True,
                         facecolor=MAROON_TINT, edgecolor=MAROON, lw=1.6, zorder=5))
    t(ax, 420, 114, "space?", size=10, color=MAROON_DARK, fam=B_SB, z=7)
    ab(120, 90, 170, "Reject (NO)", WHITE, ec=MAROON_SOFT, size=9.5, color=MAROON_SOFT)
    arrow(ax, 360, 114, 294, 108, lw=1.8, ms=12, z=8)

    arrow(ax, 420, 114, 420, 82, lw=1.8, ms=12, z=8)
    t(ax, 436, 96, "YES", size=9.5, color=MAROON_SOFT, fam=B_SB, z=8)
    ab(310, 46, 220, "Create registration")
    arrow(ax, 420, 44, 420, 36, lw=1.8, ms=12, z=8)
    ab(340, 0, 160, "Confirm \u2014 END", MAROON_DARK, ec=MAROON_DARK, size=11, color=GOLD_LIGHT)

    return save(fig, "w12_activity.png")


# --------------------------------------------------------------------------
# 10. Comparing behavioural views — table
# --------------------------------------------------------------------------
def views_compare():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Comparing the Behavioural Views", sub="A distinction that is extremely important")

    rows = [
        ("Use case", "What does the actor want to accomplish?"),
        ("Sequence", "How do objects interact over time?"),
        ("Activity", "What workflow / activities take place?"),
        ("State machine", "How does an object change state?"),
    ]
    x0, w1, w2 = 60, 220, 500
    y_top, rh = 330, 52
    box(ax, x0, y_top - rh - len(rows) * rh - 16, w1 + w2, 16 + rh + len(rows) * rh, WHITE, ec=MAROON, lw=1.6, r=12, z=4)
    box(ax, x0, y_top - rh, w1 + w2, rh, MAROON, r=0, z=5)
    t(ax, x0 + w1 / 2, y_top - rh / 2, "MODEL", size=12, color=WHITE, fam=H_SB, z=6)
    t(ax, x0 + w1 + w2 / 2, y_top - rh / 2, "MAIN QUESTION", size=12, color=WHITE, fam=H_SB, z=6)
    for i, (k, v) in enumerate(rows):
        yy = y_top - rh * (i + 1) - rh / 2
        fc = WHITE if i % 2 == 0 else MAROON_TINT
        box(ax, x0, y_top - rh * (i + 1) - rh, w1 + w2, rh, fc, r=0, z=5)
        t(ax, x0 + w1 / 2, yy, k, size=11.5, color=MAROON, fam=B_SB, z=6)
        t(ax, x0 + w1 + w2 / 2, yy, v, size=11.5, color=INK, fam=BODY, z=6)
        ax.plot([x0, x0 + w1 + w2], [y_top - rh * (i + 1), y_top - rh * (i + 1)], color=GREY_LIGHT, lw=1.0, zorder=6)
    ax.plot([x0 + w1, x0 + w1], [y_top - rh, y_top - rh - len(rows) * rh], color=GREY_LIGHT, lw=1.0, zorder=6)

    box(ax, 22, 18, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 31, "Know which model answers which question before the examination.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w12_views_compare.png")


# --------------------------------------------------------------------------
# 11. Multiplicity
# --------------------------------------------------------------------------
def multiplicity():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Multiplicity", sub="Precise numbers on each side of a relationship")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "STUDENT \u2014 REGISTRATION \u2014 COURSE", size=12.5, color=MAROON, fam=H_B, z=6)
    box(ax, 60, 210, 130, 44, MAROON_TINT, ec=MAROON, lw=1.5, r=8, z=6)
    t(ax, 125, 232, "Student", size=11, color=MAROON_DARK, fam=B_SB, z=7)
    box(ax, 250, 210, 130, 44, MAROON_TINT, ec=MAROON, lw=1.5, r=8, z=6)
    t(ax, 315, 232, "Registration", size=11, color=MAROON_DARK, fam=B_SB, z=7)
    ax.plot([192, 248], [232, 232], color=MAROON, lw=1.8, zorder=8)
    t(ax, 195, 246, "1", size=11, color=MAROON_SOFT, fam=B_SB, z=8)
    t(ax, 245, 246, "0..*", size=11, color=MAROON_SOFT, fam=B_SB, z=8)
    box(ax, 250, 110, 130, 44, MAROON_TINT, ec=MAROON, lw=1.5, r=8, z=6)
    t(ax, 315, 132, "Course", size=11, color=MAROON_DARK, fam=B_SB, z=7)
    arrow(ax, 250, 152, 250, 158, lw=1.8, ms=10, z=8)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "SYMBOLS", size=13, color=MAROON_DARK, fam=H_B, z=6)
    sym = [("1", "Exactly one"), ("0..1", "Zero or one"), ("0..*", "Zero or many"), ("1..*", "One or many"), ("2..5", "Between two and five")]
    for i, (sy, m) in enumerate(sym):
        y = 252 - i * 32
        t(ax, 512, y, sy, size=11, color=MAROON_SOFT, fam=MONO, ha="left", z=7)
        t(ax, 600, y, m, size=11, color=INK, fam=BODY, ha="left", z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Student 1 \u2014 0..* Registration \u2014 Course gives much more precise information.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w12_multiplicity.png")


# --------------------------------------------------------------------------
# 12. Packages
# --------------------------------------------------------------------------
def packages():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Packages", sub="Organising a large model into related groups")

    pkgs = [
        (30, "Authentication", ["User", "Role", "Permission"]),
        (200, "Academic", ["Student", "Course", "Programme", "Registration"]),
        (370, "Finance", ["Payment", "Invoice"]),
        (540, "Library", ["Book", "Borrowing"]),
        (700, "Notification", ["Email", "SMS"]),
    ]
    for x, name, items in pkgs:
        box(ax, x, 96, 132, 246, WHITE, ec=MAROON, lw=1.7, r=8, z=5)
        box(ax, x, 306, 132, 36, MAROON, r=8, z=6)
        t(ax, x + 66, 324, name, size=10.5, color=WHITE, fam=B_SB, z=7)
        for i, it in enumerate(items):
            y = 244 - i * 30
            box(ax, x + 10, y - 11, 112, 22, MAROON_TINT, r=6, z=6)
            t(ax, x + 66, y, it, size=9.5, color=INK, fam=BODY, z=7)
    box(ax, 22, 42, 796, 32, MAROON_TINT, ec=MAROON, lw=1.2, r=10, z=5)
    t(ax, 420, 58, "University System", size=12, color=MAROON_DARK, fam=B_SB, z=6)

    box(ax, 22, 12, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 25, "Grouping related elements makes a large model easier to navigate.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w12_packages.png")


# --------------------------------------------------------------------------
# 13. Architecture layers
# --------------------------------------------------------------------------
def architecture():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Architectural Integration", sub="Organising classes into a layered software system")

    layers = [
        ("PRESENTATION", "Web / Mobile / Desktop", MAROON),
        ("APPLICATION", "RegistrationService · AuthenticationService", MAROON_SOFT),
        ("DOMAIN", "Student · Course · Registration", MAROON_SOFT),
        ("DATA ACCESS", "StudentRepository · CourseRepository · RegistrationRepository", MAROON_DARK),
        ("DATABASE", "persistent storage", MAROON_DEEP),
    ]
    y = 52
    for i, (hd, sub, colr) in enumerate(layers):
        box(ax, 60, y, 720, 58, colr, r=12, z=6)
        t(ax, 420, y + 40, hd, size=13, color=WHITE, fam=H_SB, z=7)
        t(ax, 420, y + 17, sub, size=11, color=GOLD_LIGHT, fam=B_IT, z=7)
        if i < len(layers) - 1:
            arrow(ax, 420, y - 2, 420, y - 12, lw=2.2, ms=14, z=8)
        y += 70

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "Layers give responsibilities clearer boundaries and make the system maintainable.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w12_architecture.png")


# --------------------------------------------------------------------------
# 14. Components
# --------------------------------------------------------------------------
def components():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Component Thinking", sub="How can the software be divided into meaningful, replaceable parts?")

    comps = ["Authentication Component", "Registration Component", "Payment Component", "Notification Component", "Reporting Component"]
    for i, name in enumerate(comps):
        r, c = divmod(i, 3)
        x = 50 + c * 260
        y = 210 - r * 70
        box(ax, x, y, 220, 48, WHITE, ec=MAROON, lw=1.6, r=10, z=6)
        t(ax, x + 110, y + 24, name, size=11.5, color=MAROON, fam=B_SB, z=7)
    box(ax, 300, 96, 240, 52, MAROON, r=12, z=6)
    t(ax, 420, 134, "UNIVERSITY SYSTEM", size=12.5, color=WHITE, fam=H_SB, z=7)
    t(ax, 420, 112, "replaceable, independently understandable parts", size=9.5, color=GOLD_LIGHT, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Beyond \u201cwhat classes exist?\u201d \u2014 how is the software divided into parts?",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w12_components.png")


# --------------------------------------------------------------------------
# 15. Validation
# --------------------------------------------------------------------------
def validation():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Design Validation", sub="Does the design represent what the system is supposed to do?")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "REQUIREMENT", size=13, color=MAROON_SOFT, fam=H_B, z=6)
    box(ax, 60, 210, 304, 50, WHITE, ec=MAROON_SOFT, lw=1.4, r=10, z=6)
    t(ax, 212, 246, "\u201cStudents cannot register for a full course.\u201d", size=11, color=MAROON_SOFT, fam=B_IT, z=7)
    t(ax, 212, 216, "implies capacity must be checked", size=10, color=GREY, fam=B_IT, z=7)
    t(ax, 212, 150, "Sequence: Student -> Service -> Create", size=10.5, color=INK, fam=BODY, z=7)
    t(ax, 212, 128, "Registration   (no checkCapacity!)", size=10.5, color=MAROON_SOFT, fam=B_SB, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "FIXED DESIGN", size=13, color=MAROON, fam=H_B, z=6)
    for i, s in enumerate(["Student", "RegistrationService", "Course.checkCapacity()", "Create Registration"]):
        y = 236 - i * 32
        box(ax, 480, y - 13, 296, 26, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
        t(ax, 628, y, s, size=10.5, color=INK, fam=BODY, z=7)
        if i < 3:
            arrow(ax, 628, y - 15, 628, y - 19, lw=1.6, ms=10, z=8)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Validation catches designs that are incomplete relative to the requirements.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w12_validation.png")


# --------------------------------------------------------------------------
# 16. Integrated example — R01 across models
# --------------------------------------------------------------------------
def integrated_example():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Complete Integrated Example", sub="Requirement R01 expressed through every model")

    tiles = [
        ("R01", "students register for available courses online", "REQUIREMENT"),
        ("Use Case", "Student \u2014 Register for Course", "USE CASE"),
        ("Classes", "Student · Course · Registration · RegistrationService", "CLASS MODEL"),
        ("Sequence", "register -> checkPrerequisite -> create -> confirm", "SEQUENCE"),
        ("Activity", "login -> select -> check -> create -> confirm", "ACTIVITY"),
        ("State", "Requested -> Validated -> Confirmed -> Cancelled", "STATE"),
        ("Architecture", "Presentation -> Service -> Domain -> Data", "ARCHITECTURE"),
    ]
    for i, (hd, sub, tag) in enumerate(tiles):
        r, c = divmod(i, 3)
        x = 30 + c * 268
        y = 240 - r * 108
        colr = MAROON if r == 0 else (MAROON_SOFT if i == 6 else MAROON)
        box(ax, x, y, 244, 84, WHITE if r == 0 else MAROON_TINT, ec=colr, lw=1.6, r=12, z=5)
        t(ax, x + 122, y + 60, hd, size=12, color=MAROON, fam=B_SB, z=6)
        t(ax, x + 122, y + 30, sub, size=9.5, color=GREY, fam=B_IT, z=6)
        box(ax, x + 168, y + 8, 68, 20, colr, r=8, z=7)
        t(ax, x + 202, y + 18, tag, size=7.5, color=WHITE, fam=B_SB, z=8)

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "Every model contributes to the same understanding of the system.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w12_integrated_example.png")


# --------------------------------------------------------------------------
# 17. Model vs diagram (Google Maps)
# --------------------------------------------------------------------------
def model_vs_diagram():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Model vs Diagram", sub="Different views of the same underlying system")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "GOOGLE MAPS ANALOGY", size=13, color=MAROON, fam=H_B, z=6)
    for i, s in enumerate(["satellite imagery", "roads", "terrain", "traffic", "public transport"]):
        box(ax, 80, 226 - i * 32, 264, 26, MAROON_TINT, r=8, z=6)
        t(ax, 212, 239 - i * 32, s, size=11, color=INK, fam=BODY, z=7)
    t(ax, 212, 96, "different views of the same geography", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "SOFTWARE MODELS", size=13, color=MAROON_DARK, fam=H_B, z=6)
    for i, s in enumerate(["Use Case", "Class", "Sequence", "State", "Activity"]):
        box(ax, 496, 226 - i * 32, 264, 26, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
        t(ax, 628, 239 - i * 32, s + " Diagram", size=11, color=INK, fam=BODY, z=7)
    t(ax, 628, 96, "different perspectives on one system", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "A diagram is a visual representation; a model is the underlying structured representation.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w12_model_vs_diagram.png")


# --------------------------------------------------------------------------
# 18. Summary mental model
# --------------------------------------------------------------------------
def summary_flow():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Week 12 Mental Model", sub="Every model contributes to the same understanding")

    steps = [
        ("REQUIREMENTS", "what the system must do", MAROON),
        ("USE CASES", "what actors accomplish", MAROON),
        ("BEHAVIOURAL MODELS", "how the behaviour occurs", MAROON_SOFT),
        ("OBJECT / CLASS MODEL", "what structure supports the behaviour", MAROON_SOFT),
        ("ARCHITECTURE", "how the software is organised", MAROON_DARK),
        ("IMPLEMENTATION", "the running system", MAROON_DEEP),
    ]
    y = 380
    for i, (hd, sub, colr) in enumerate(steps):
        box(ax, 250, y, 340, 52, colr, r=12, z=6)
        t(ax, 420, y + 34, hd, size=12.5, color=WHITE, fam=H_SB, z=7)
        t(ax, 420, y + 12, sub, size=10, color=GOLD_LIGHT, fam=B_IT, z=7)
        if i < len(steps) - 1:
            arrow(ax, 420, y - 2, 420, y - 12, lw=2.2, ms=14, z=8)
        y -= 68

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "Don't memorise diagrams as independent pictures \u2014 tell the same story and make the models agree.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w12_summary_flow.png")


ALL = [
    progression, house_analogy, model_views, big_picture, consistency,
    traceability, sequence, state_machine, activity, views_compare,
    multiplicity, packages, architecture, components, validation,
    integrated_example, model_vs_diagram, summary_flow,
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
    print("Generated", len(made), "week-12 visuals:")
    for m in made:
        print("  -", m)
