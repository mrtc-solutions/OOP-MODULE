"""
Week 3 visuals — MODELLING LANGUAGE: UML.
Proper UML-style notation drawn with matplotlib.
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (FancyBboxPatch, FancyArrowPatch, Circle,
                                Polygon, Ellipse)

from common import (MAROON, MAROON_DARK, MAROON_DEEP, MAROON_SOFT, MAROON_TINT,
                    GOLD, GOLD_LIGHT, CREAM, CREAM_2, INK, GREY, GREY_LIGHT,
                    WHITE, CHART_COLORS)
from draw import (canvas, box, t, arrow, title, save, H_XB, H_B, H_SB, H_MD,
                  BODY, B_SB, B_B, B_IT, MONO, SYM)


# --------------------------------------------------------------------------
# UML-specific helpers
# --------------------------------------------------------------------------
def uml_class(ax, x, y, w, name, attrs=None, ops=None, ec=MAROON,
              name_color=WHITE, fill=WHITE, line_h=20, pad=12):
    attrs = attrs or []
    ops = ops or []
    h_name = 30
    h_attrs = pad + line_h * len(attrs) + (pad if attrs else 0)
    h_ops = pad + line_h * len(ops) + (pad if ops else 0)
    h = h_name + h_attrs + h_ops
    box(ax, x, y, w, h, fill, ec=ec, lw=1.8, r=0, z=6)
    # name compartment
    box(ax, x, y + h - h_name, w, h_name, ec, r=0, z=6)
    t(ax, x + w / 2, y + h - h_name / 2, name, size=13, color=name_color, fam=H_SB, z=7)
    # separators
    ax.plot([x, x + w], [y + h_attrs + h_ops, y + h_attrs + h_ops], color=ec, lw=1.0, zorder=7)
    ax.plot([x, x + w], [y + h_ops, y + h_ops], color=ec, lw=1.0, zorder=7)
    yy = y + h_attrs + h_ops - pad
    for a in attrs:
        t(ax, x + 10, yy, a, size=10.5, color=INK, fam=MONO, ha="left", z=7)
        yy -= line_h
    yy = y + h_ops - pad
    for o in ops:
        t(ax, x + 10, yy, o, size=10.5, color=MAROON_SOFT, fam=MONO, ha="left", z=7)
        yy -= line_h
    return x, y, w, h


def actor(ax, cx, cy, s=1.0, color=MAROON, label=None, lw=2.2):
    ax.add_patch(Circle((cx, cy + 30 * s), 8 * s, fill=False, edgecolor=color, lw=lw, zorder=7))
    ax.plot([cx, cx], [cy + 22 * s, cy - 6 * s], color=color, lw=lw, zorder=7)
    ax.plot([cx - 14 * s, cx + 14 * s], [cy + 12 * s, cy + 12 * s], color=color, lw=lw, zorder=7)
    ax.plot([cx, cx - 12 * s], [cy - 6 * s, cy - 30 * s], color=color, lw=lw, zorder=7)
    ax.plot([cx, cx + 12 * s], [cy - 6 * s, cy - 30 * s], color=color, lw=lw, zorder=7)
    if label:
        t(ax, cx, cy - 46 * s, label, size=12, color=MAROON, fam=H_SB, z=7)


def usecase_oval(ax, x, y, w, h, label, ec=MAROON, fill=WHITE):
    ax.add_patch(Ellipse((x + w / 2, y + h / 2), w, h, facecolor=fill,
                         edgecolor=ec, lw=1.8, zorder=6))
    t(ax, x + w / 2, y + h / 2, label, size=11.5, color=MAROON, fam=H_SB, z=7)


def node_box(ax, x, y, w, h, label, depth=8, ec=MAROON, fill=WHITE):
    """3D node (cube) for deployment diagrams."""
    ax.add_patch(Polygon([(x, y), (x + w, y), (x + w, y + h), (x, y + h)],
                         closed=True, facecolor=fill, edgecolor=ec, lw=1.8, zorder=6))
    ax.add_patch(Polygon([(x + w, y), (x + w + depth, y + depth),
                          (x + w + depth, y + h + depth), (x + w, y + h)],
                         closed=True, facecolor=CREAM_2, edgecolor=ec, lw=1.4, zorder=5))
    ax.add_patch(Polygon([(x, y + h), (x + w, y + h),
                          (x + w + depth, y + h + depth), (x + depth, y + h + depth)],
                         closed=True, facecolor=MAROON_TINT, edgecolor=ec, lw=1.4, zorder=5))
    t(ax, x + w / 2, y + h / 2, label, size=11.5, color=MAROON, fam=H_SB, z=7)


def diamond(ax, cx, cy, w, h, color=WHITE, ec=MAROON, lw=1.8):
    ax.add_patch(Polygon([(cx, cy + h / 2), (cx + w / 2, cy), (cx, cy - h / 2),
                          (cx - w / 2, cy)], closed=True, facecolor=color,
                         edgecolor=ec, lw=lw, zorder=6))


def component_box(ax, x, y, w, h, label, ec=MAROON, fill=WHITE):
    box(ax, x, y, w, h, fill, ec=ec, lw=1.8, r=0, z=6)
    # component "tab" icon top-left
    box(ax, x + 6, y + h - 18, 26, 14, fill, ec=ec, lw=1.4, r=0, z=7)
    t(ax, x + w / 2 + 6, y + h / 2, label, size=11.5, color=MAROON, fam=H_SB, z=7)


def package_box(ax, x, y, w, h, label, ec=MAROON, fill=WHITE, tab=40):
    ax.add_patch(Polygon([(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y + tab)],
                         closed=False, facecolor="none", edgecolor="none"))
    # main body
    ax.add_patch(Polygon([(x, y), (x + w, y), (x + w, y + h - tab), (x, y + h - tab)],
                         closed=True, facecolor=fill, edgecolor=ec, lw=1.8, zorder=6))
    # tab
    ax.add_patch(Polygon([(x, y + h - tab), (x + tab, y + h - tab), (x + tab, y + h),
                          (x, y + h)], closed=True, facecolor=CREAM_2, edgecolor=ec, lw=1.8, zorder=6))
    t(ax, x + w / 2, y + (h - tab) / 2, label, size=11.5, color=MAROON, fam=H_SB, z=7)


# --------------------------------------------------------------------------
# 1. The three conceptual building blocks
# --------------------------------------------------------------------------
def three_blocks():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Three Conceptual Building Blocks of UML",
          sub="Things · Relationships · Diagrams — the classic UML mental model")

    box(ax, 270, 240, 300, 70, MAROON, r=14, z=6)
    t(ax, 420, 275, "UML", size=22, color=WHITE, fam=H_B, z=7)

    cards = [
        ("THINGS", "the modelling elements\nthemselves", "Class · Interface · Object\nUse Case · Component · Node", MAROON),
        ("RELATIONSHIPS", "how the elements\nconnect", "Association · Dependency\nGeneralization · Realization", MAROON_DARK),
        ("DIAGRAMS", "views of selected\nparts of the model", "Class · Use Case · Sequence\nActivity · State · Deployment", "#8C2B2D"),
    ]
    xs = [30, 305, 580]
    for (name, sub, ex, col), x in zip(cards, xs):
        box(ax, x, 30, 230, 180, WHITE, ec=col, lw=1.8, r=14, z=6)
        box(ax, x, 168, 230, 42, col, r=10, z=6)
        t(ax, x + 115, 189, name, size=13, color=WHITE, fam=H_B, z=7)
        t(ax, x + 115, 138, sub, size=11, color=GREY, fam=B_IT, z=7, ls=1.2)
        t(ax, x + 115, 88, ex, size=10.5, color=INK, fam=MONO, z=7, ls=1.35)
        arrow(ax, 420, 240, x + 115, 216, color=col, lw=2.2)

    box(ax, 30, 6, 780, 24, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 18, "Associated with the foundational UML teaching approach of Booch, Rumbaugh and Jacobson.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w3_three_blocks.png")


# 2. Four kinds of things
def things():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Four Kinds of “Things”", sub="Structural · Behavioural · Grouping · Annotational")

    cards = [
        ("Structural", "What exists?", "Class · Interface · Object\nComponent · Node", MAROON),
        ("Behavioural", "What happens?", "Interaction · Activity\nState Machine", MAROON_DARK),
        ("Grouping", "How is it organised?", "Package — groups related\nmodel elements", "#8C2B2D"),
        ("Annotational", "What else should we note?", "Note — a comment or\nconstraint on the model", GOLD),
    ]
    cw, ch, g = 380, 150, 14
    for i, (name, q, ex, col) in enumerate(cards):
        r, c = divmod(i, 2)
        x = 22 + c * (cw + g)
        y = 30 + (1 - r) * (ch + g)
        box(ax, x, y, cw, ch, WHITE, ec=col, lw=1.8, r=14, z=6)
        box(ax, x, y + ch - 42, cw, 42, col, r=10, z=6)
        t(ax, x + cw / 2, y + ch - 21, name, size=13.5, color=(MAROON_DARK if col == GOLD else WHITE), fam=H_B, z=7)
        t(ax, x + 16, y + ch - 66, q, size=11, color=col if col != GOLD else MAROON_DARK, fam=B_B, ha="left", z=7)
        t(ax, x + 16, y + 18, ex, size=11, color=INK, fam=MONO, ha="left", z=7, ls=1.3)
    return save(fig, "w3_things.png")


# 3. Class example with adornments
def class_example():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "A UML Class — Name, Attributes, Operations",
          sub="Three compartments, with visibility adornments")

    uml_class(ax, 300, 60, 240, "Student",
              attrs=["- studentID : String", "+ name : String", "- programme : String", "- year : int"],
              ops=["+ registerCourse() : bool", "+ viewResults() : List"])

    # annotations
    annots = [
        ("Top compartment", "class name", 40, 300, 350),
        ("Middle compartment", "attributes (state)", 100, 300, 260),
        ("Bottom compartment", "operations (behaviour)", 155, 300, 175),
        ("Adornments", "− private   + public", 215, 300, 100),
    ]
    for label, sub, yy, x1, x2 in annots:
        box(ax, 585, yy - 12, 225, 46, WHITE, ec=MAROON, lw=1.4, r=10, z=6)
        t(ax, 697, yy + 16, label, size=11.5, color=MAROON, fam=H_SB, z=7)
        t(ax, 697, yy - 4, sub, size=10.5, color=GREY, fam=BODY, z=7)
        arrow(ax, x1, yy + 10, x2, yy + 10, color=GOLD, lw=1.8)

    box(ax, 20, 8, 800, 26, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 21, "Class diagram notation is studied in depth in Week 5.", size=12,
      color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w3_class_example.png")


# 4. Interface + realization
def interface():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Interface & Realization", sub="An interface is a contract — different classes can fulfil it")

    # interface box
    box(ax, 40, 150, 250, 150, WHITE, ec=MAROON, lw=1.8, r=0, z=6)
    box(ax, 40, 262, 250, 38, MAROON, r=0, z=6)
    t(ax, 165, 281, "«interface»", size=10.5, color=GOLD_LIGHT, fam=MONO, z=7)
    t(ax, 165, 260, "PaymentService", size=13, color=WHITE, fam=H_SB, z=7)
    ax.plot([40, 290], [238, 238], color=MAROON, lw=1.0, zorder=7)
    for i, o in enumerate(["processPayment()", "refundPayment()", "checkStatus()"]):
        t(ax, 56, 216 - i * 24, o, size=11, color=INK, fam=MONO, ha="left", z=7)

    # implementations
    impls = ["BankPayment", "MobileMoneyPayment", "CardPayment"]
    for i, name in enumerate(impls):
        x = 460 + i * 130
        box(ax, x, 150, 110, 70, WHITE, ec=MAROON_DARK, lw=1.6, r=0, z=6)
        box(ax, x, 190, 110, 30, MAROON_DARK, r=0, z=6)
        t(ax, x + 55, 205, name, size=10, color=WHITE, fam=H_SB, z=7)
        ax.plot([x, x + 110], [150, 150], color=MAROON_DARK, lw=1.0, zorder=7)
        t(ax, x + 55, 165, "processPayment()", size=8.5, color=INK, fam=MONO, z=7)
        # realization dashed hollow triangle
        ax.plot([310, 452], [225, 190], color=MAROON, lw=1.8, ls=(0, (4, 3)), zorder=6)
        ax.add_patch(Polygon([(460, 192), (452, 180), (452, 204)], closed=True,
                             fill=False, edgecolor=MAROON, lw=1.8, zorder=8))

    box(ax, 20, 10, 800, 34, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 27, "The user of the interface does not need to know the internal implementation.",
      size=12, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w3_interface.png")


# 5. Four relationship types
def relationships():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Main UML Relationships", sub="Association · Dependency · Generalization · Realization")

    # association
    t(ax, 180, 380, "Association", size=13, color=MAROON, fam=H_SB)
    box(ax, 40, 330, 150, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 115, 350, "Student", size=11.5, color=MAROON, fam=H_SB)
    box(ax, 320, 330, 150, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 395, 350, "Course", size=11.5, color=MAROON, fam=H_SB)
    ax.plot([190, 320], [350, 350], color=MAROON, lw=2.0, zorder=6)
    t(ax, 255, 366, "registers for", size=10.5, color=GREY, fam=B_IT)

    # dependency (dashed open arrow)
    t(ax, 620, 380, "Dependency", size=13, color=MAROON, fam=H_SB)
    box(ax, 500, 330, 160, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 580, 350, "ReportGenerator", size=11, color=MAROON, fam=H_SB)
    box(ax, 720, 330, 130, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 785, 350, "Payment", size=11.5, color=MAROON, fam=H_SB)
    ax.plot([660, 714], [350, 350], color=MAROON, lw=1.8, ls=(0, (4, 3)), zorder=6)
    arrow(ax, 660, 350, 714, 350, color=MAROON, lw=0, style="-|>", ms=14)

    # generalization (hollow triangle to general)
    t(ax, 400, 250, "Generalization", size=13, color=MAROON, fam=H_SB)
    box(ax, 160, 120, 140, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 230, 140, "Student", size=11.5, color=MAROON, fam=H_SB)
    box(ax, 460, 120, 140, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 530, 140, "Lecturer", size=11.5, color=MAROON, fam=H_SB)
    box(ax, 310, 180, 140, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 380, 200, "User", size=11.5, color=MAROON, fam=H_SB)
    ax.plot([230, 355], [160, 180], color=MAROON, lw=1.8, zorder=6)
    ax.plot([530, 405], [160, 180], color=MAROON, lw=1.8, zorder=6)
    ax.add_patch(Polygon([(380, 218), (362, 188), (398, 188)], closed=True,
                         fill=False, edgecolor=MAROON, lw=1.8, zorder=8))

    # realization (dashed hollow triangle)
    t(ax, 725, 250, "Realization", size=13, color=MAROON, fam=H_SB)
    box(ax, 660, 180, 150, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 735, 200, "«interface»", size=9, color=GOLD, fam=MONO)
    t(ax, 735, 188, "PaymentService", size=11, color=MAROON, fam=H_SB)
    box(ax, 660, 90, 150, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 735, 110, "MobileMoney", size=11, color=MAROON, fam=H_SB)
    ax.plot([735, 735], [180, 134], color=MAROON, lw=1.8, ls=(0, (4, 3)), zorder=6)
    ax.add_patch(Polygon([(735, 126), (723, 138), (747, 138)], closed=True,
                         fill=False, edgecolor=MAROON, lw=1.8, zorder=8))

    box(ax, 20, 8, 800, 26, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 21, "Include/extend (use cases) and aggregation/composition come later.",
      size=12, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w3_relationships.png")


# 6. Multiplicity
def multiplicity():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Multiplicity on Associations", sub="How many instances can participate in a relationship?")

    box(ax, 40, 200, 180, 70, WHITE, ec=MAROON, lw=1.8, r=0)
    t(ax, 130, 235, "Student", size=13, color=MAROON, fam=H_SB)
    box(ax, 40, 60, 180, 70, WHITE, ec=MAROON, lw=1.8, r=0)
    t(ax, 130, 95, "Course", size=13, color=MAROON, fam=H_SB)
    ax.plot([130, 130], [200, 136], color=MAROON, lw=2.0, zorder=6)
    t(ax, 150, 250, "1", size=13, color=MAROON, fam=H_B)
    t(ax, 150, 112, "0..*", size=13, color=MAROON, fam=H_B)
    t(ax, 130, 168, "registers for", size=10.5, color=GREY, fam=B_IT)

    # table of common multiplicities
    t(ax, 320, 250, "Common multiplicities", size=13, color=MAROON, fam=H_SB, ha="left")
    rows = [
        ("1", "exactly one"),
        ("0..1", "zero or one"),
        ("*", "many"),
        ("0..*", "zero or many"),
        ("1..*", "one or many"),
        ("2..5", "between two and five"),
    ]
    y = 218
    for code, meaning in rows:
        box(ax, 320, y - 14, 70, 34, MAROON_TINT, ec=MAROON, lw=1.2, r=8, z=6)
        t(ax, 355, y + 3, code, size=11.5, color=MAROON_DARK, fam=MONO, z=7)
        t(ax, 420, y + 3, meaning, size=12, color=INK, fam=BODY, ha="left", z=7)
        y -= 36

    box(ax, 620, 60, 200, 210, CREAM_2, ec=GOLD, lw=1.6, r=12, z=6)
    t(ax, 720, 240, "Reads as:", size=11, color=MAROON_DARK, fam=H_SB, z=7)
    t(ax, 720, 200, "One Student can be\nassociated with zero\nor many Courses.", size=12, color=INK, fam=BODY, z=7, ls=1.4)
    arrow(ax, 220, 160, 610, 160, color=GOLD, lw=2.2)

    return save(fig, "w3_multiplicity.png")


# 7. Use case diagram
def use_case():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Use-Case Diagram", sub="What should users be able to accomplish with the system?")

    box(ax, 420, 40, 380, 260, WHITE, ec=MAROON, lw=1.8, r=10, z=4)
    t(ax, 610, 285, "Registration System", size=11, color=GREY, fam=B_IT, z=6)

    usecase_oval(ax, 470, 200, 260, 60, "Register Course")
    usecase_oval(ax, 470, 90, 260, 60, "View Results")

    actor(ax, 130, 170, s=1.4, label="Student")
    ax.plot([164, 470], [200, 230], color=MAROON, lw=1.8, zorder=6)
    ax.plot([164, 470], [140, 120], color=MAROON, lw=1.8, zorder=6)

    box(ax, 20, 8, 800, 26, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 21, "Use cases capture functionality from the user's perspective — studied in depth in Week 9.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w3_use_case.png")


# 8. Sequence diagram
def sequence():
    W, H = 840, 420
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Sequence Diagram", sub="Who communicates with whom, and in what order?")

    lifelines = [("Student", 150), ("System", 420), ("Database", 690)]
    top, bot = 350, 60
    for name, x in lifelines:
        box(ax, x - 60, top, 120, 34, MAROON, r=0, z=6)
        t(ax, x, top + 17, name, size=12, color=WHITE, fam=H_SB, z=7)
        ax.plot([x, x], [top, bot], color=MAROON_SOFT, lw=1.6, ls=(0, (5, 4)), zorder=5)

    msgs = [
        (150, 420, 290, "login()"),
        (420, 690, 240, "verify()"),
        (690, 420, 210, "result"),
        (420, 150, 160, "confirmation"),
    ]
    for x1, x2, y, label in msgs:
        ax.plot([x1, x2], [y, y], color=MAROON, lw=1.8, zorder=6)
        arrow(ax, x1, y, x2, y, color=MAROON, lw=0, style="-|>", ms=12)
        t(ax, (x1 + x2) / 2, y + 14, label, size=10.5, color=MAROON_DARK, fam=MONO, z=7)

    t(ax, 55, 190, "time", size=11, color=GREY, fam=B_IT, ha="left", rotation=90)
    arrow(ax, 55, 60, 55, 340, color=GREY, lw=1.4, style="-|>", ms=10)

    box(ax, 20, 8, 800, 26, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 21, "Vertical direction represents the progression of time.", size=12,
      color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w3_sequence.png")


# 9. Activity diagram
def activity():
    W, H = 840, 440
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Activity Diagram", sub="Modelling the workflow of a process")

    def action(cx, cy, label, w=240, h=46):
        box(ax, cx - w / 2, cy - h / 2, w, h, WHITE, ec=MAROON, lw=1.8, r=20, z=6)
        t(ax, cx, cy, label, size=12, color=MAROON, fam=H_SB, z=7)

    # start node
    ax.add_patch(Circle((420, 408), 10, facecolor=MAROON, edgecolor="none", zorder=7))
    action(420, 372, "Login")
    action(420, 306, "Select Course")
    action(420, 240, "Check Eligibility")
    diamond(ax, 420, 168, 120, 64)
    t(ax, 420, 168, "Eligible?", size=11, color=MAROON, fam=H_SB, z=8)
    action(640, 168, "Register Course", w=200)
    action(640, 90, "Display Confirmation", w=220)

    # end nodes
    ax.add_patch(Circle((300, 90), 12, facecolor=WHITE, edgecolor=MAROON, lw=2, zorder=7))
    ax.add_patch(Circle((300, 90), 5, facecolor=MAROON, edgecolor="none", zorder=8))
    t(ax, 300, 62, "End", size=10.5, color=GREY, fam=B_IT)

    # arrows
    ax.plot([420, 420], [398, 395], color=MAROON, lw=1.8, zorder=5)
    arrow(ax, 420, 395, 420, 352, color=MAROON, lw=1.8, style="-|>", ms=12)
    arrow(ax, 420, 349, 420, 306, color=MAROON, lw=1.8, style="-|>", ms=12)
    arrow(ax, 420, 283, 420, 240, color=MAROON, lw=1.8, style="-|>", ms=12)
    arrow(ax, 420, 217, 420, 202, color=MAROON, lw=1.8, style="-|>", ms=12)
    arrow(ax, 420, 134, 420, 90, color=MAROON, lw=1.8, style="-|>", ms=12)
    t(ax, 406, 116, "No", size=11, color=GREY, fam=B_IT)
    arrow(ax, 480, 168, 540, 168, color=MAROON, lw=1.8, style="-|>", ms=12)
    t(ax, 508, 186, "Yes", size=11, color=MAROON, fam=B_SB)
    arrow(ax, 640, 145, 640, 113, color=MAROON, lw=1.8, style="-|>", ms=12)

    box(ax, 20, 8, 800, 24, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 20, "Activity diagrams model workflows — studied in detail in Week 11.", size=11.5,
      color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w3_activity.png")


# 10. State machine
def state_machine():
    W, H = 840, 360
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "State Machine Diagram", sub="How an object changes state as events occur")

    ax.add_patch(Circle((120, 180), 9, facecolor=MAROON, edgecolor="none", zorder=7))

    states = ["Draft", "Submitted", "Approved", "Completed"]
    events = ["submit", "approve", "complete"]
    x = 200
    for i, name in enumerate(states):
        box(ax, x, 150, 140, 60, WHITE, ec=MAROON, lw=1.8, r=16, z=6)
        t(ax, x + 70, 180, name, size=13, color=MAROON, fam=H_SB, z=7)
        if i < 3:
            arrow(ax, x + 140, 180, x + 168, 180, color=MAROON, lw=1.8, style="-|>", ms=14)
            t(ax, x + 154, 202, events[i], size=10.5, color=MAROON_DARK, fam=MONO, z=7)
        x += 168

    t(ax, 320, 90, "An event causes each transition.", size=12, color=GREY, fam=B_IT, z=7)
    box(ax, 20, 10, 800, 28, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 24, "State modelling is developed fully in Weeks 7 and 8.", size=12,
      color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w3_state_machine.png")


# 11. Component diagram
def component():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Component Diagram", sub="Major software components and their dependencies")

    component_box(ax, 320, 300, 200, 60, "Mobile App")
    component_box(ax, 320, 200, 200, 60, "API Component")
    component_box(ax, 130, 80, 170, 60, "Auth")
    component_box(ax, 540, 80, 170, 60, "Registration")
    component_box(ax, 320, 20, 200, 44, "Database")

    arrow(ax, 420, 300, 420, 268, color=MAROON, lw=2.0, style="-|>", ms=14)
    arrow(ax, 420, 200, 420, 148, color=MAROON, lw=2.0, style="-|>", ms=14)
    arrow(ax, 320, 110, 220, 110, color=MAROON, lw=1.8, style="-|>", ms=12)
    arrow(ax, 520, 110, 620, 110, color=MAROON, lw=1.8, style="-|>", ms=12)
    arrow(ax, 390, 80, 390, 72, color=MAROON, lw=1.8, style="-|>", ms=12)
    arrow(ax, 450, 80, 450, 72, color=MAROON, lw=1.8, style="-|>", ms=12)

    box(ax, 20, 8, 800, 26, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 21, "Components relate to design and architecture more than early requirements analysis.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w3_component.png")


# 12. Deployment diagram
def deployment():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Deployment Diagram", sub="The physical / execution environment where software runs")

    node_box(ax, 300, 280, 240, 70, "Mobile Device\n[Mobile App]", depth=10)
    node_box(ax, 300, 150, 240, 80, "Application Server\n[API]", depth=10)
    node_box(ax, 300, 30, 240, 70, "Database Server\n[Database]", depth=10)

    arrow(ax, 420, 280, 420, 240, color=MAROON, lw=2.0, style="-|>", ms=14)
    arrow(ax, 420, 150, 420, 108, color=MAROON, lw=2.0, style="-|>", ms=14)

    t(ax, 700, 320, "Node = server,\ndevice, execution\nenvironment or\nhardware resource", size=11, color=GREY, fam=BODY, ha="left", z=7, ls=1.3)
    box(ax, 680, 60, 140, 70, CREAM_2, ec=GOLD, lw=1.6, r=10, z=6)
    t(ax, 750, 110, "3-tier\narchitecture", size=11, color=MAROON_DARK, fam=H_SB, z=7)
    t(ax, 750, 80, "client, server, database", size=10, color=INK, fam=BODY, z=7, ls=1.2)

    return save(fig, "w3_deployment.png")


# 13. Package diagram
def package():
    W, H = 840, 420
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Packages Group Model Elements", sub="Grouping helps manage large models")

    package_box(ax, 320, 300, 200, 60, "University System", tab=30)
    package_box(ax, 60, 60, 200, 180, "Student Management", tab=30)
    package_box(ax, 320, 60, 200, 180, "Finance", tab=30)
    package_box(ax, 580, 60, 200, 180, "Examination", tab=30)

    for px, items in [(60, ["Student", "Programme", "Registration"]),
                      (320, ["Payment", "Invoice"]),
                      (580, ["Exam", "Result"])]:
        y = 200
        for it in items:
            box(ax, px + 20, y - 20, 160, 32, MAROON_TINT, ec=MAROON, lw=1.2, r=8, z=7)
            t(ax, px + 100, y - 4, it, size=11, color=MAROON_DARK, fam=H_SB, z=8)
            y -= 40

    arrow(ax, 360, 300, 160, 244, color=MAROON, lw=1.8)
    arrow(ax, 420, 300, 420, 244, color=MAROON, lw=1.8)
    arrow(ax, 480, 300, 680, 244, color=MAROON, lw=1.8)

    box(ax, 20, 8, 800, 26, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 21, "Packages directly connect to Week 2's discussion of complexity management.",
      size=12, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w3_package.png")


# 14. Diagram map
def diagram_map():
    W, H = 840, 440
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The UML Diagram Map", sub="Structural, behavioural and interaction diagram families")

    box(ax, 320, 360, 200, 54, MAROON, r=12, z=6)
    t(ax, 420, 387, "UML DIAGRAMS", size=15, color=WHITE, fam=H_B, z=7)

    box(ax, 120, 250, 200, 46, MAROON_DARK, r=12, z=6)
    t(ax, 220, 273, "STRUCTURAL", size=13, color=WHITE, fam=H_B, z=7)
    box(ax, 520, 250, 200, 46, "#8C2B2D", r=12, z=6)
    t(ax, 620, 273, "BEHAVIOURAL", size=13, color=WHITE, fam=H_B, z=7)

    struct = ["Class", "Object", "Component", "Composite Structure", "Package", "Deployment"]
    for i, sname in enumerate(struct):
        x = 30 + i * 130
        box(ax, x, 180, 118, 40, WHITE, ec=MAROON_DARK, lw=1.4, r=8, z=6)
        t(ax, x + 59, 200, sname, size=10, color=MAROON_DARK, fam=H_SB, z=7)

    behav = ["Use Case", "Activity", "State Machine"]
    for i, bname in enumerate(behav):
        x = 440 + i * 130
        box(ax, x, 180, 118, 40, WHITE, ec="#8C2B2D", lw=1.4, r=8, z=6)
        t(ax, x + 59, 200, bname, size=10, color="#8C2B2D", fam=H_SB, z=7)

    box(ax, 320, 60, 200, 46, GOLD, r=12, z=6)
    t(ax, 420, 83, "INTERACTION", size=12.5, color=MAROON_DARK, fam=H_B, z=7)
    inter = ["Sequence", "Communication", "Timing", "Interaction Overview"]
    for i, iname in enumerate(inter):
        x = 90 + i * 170
        box(ax, x, 10, 150, 34, WHITE, ec=GOLD, lw=1.4, r=8, z=6)
        t(ax, x + 75, 27, iname, size=9.5, color=MAROON_DARK, fam=H_SB, z=7)

    arrow(ax, 360, 360, 220, 300, color=MAROON, lw=2.0)
    arrow(ax, 480, 360, 620, 300, color=MAROON, lw=2.0)
    arrow(ax, 620, 250, 480, 110, color=MAROON, lw=2.0)
    t(ax, 700, 190, "interaction is a\nspecialized form\nof behaviour", size=10, color=GREY, fam=B_IT, ha="left", z=7, ls=1.2)

    return save(fig, "w3_diagram_map.png")


# 15. Four-layer architecture
def architecture():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Four-Layer UML Architecture", sub="M3 · M2 · M1 · M0  —  the meta-modelling stack")

    layers = [
        ("M3", "Meta-metamodel", "The language/framework used to define metamodels — MOF", MAROON_DEEP, WHITE),
        ("M2", "Metamodel", "Defines UML concepts: Class, Attribute, Association, Operation", MAROON_DARK, WHITE),
        ("M1", "Model", "Your UML model: Student, Course, Registration", MAROON, WHITE),
        ("M0", "Instances", "Real instances: Francis, BICT 3202, Registration #12345", GOLD, MAROON_DARK),
    ]
    y = 40
    h = 84
    for code, name, meaning, col, tcol in layers:
        box(ax, 20, y, 150, h, col, r=12, z=6)
        t(ax, 95, y + h / 2 + 14, code, size=20, color=tcol, fam=H_B, z=7)
        t(ax, 95, y + h / 2 - 18, name, size=10.5, color=tcol, fam=B_SB, z=7)
        box(ax, 190, y + 12, 620, h - 24, WHITE, ec=col, lw=1.4, r=10, z=6)
        t(ax, 500, y + h / 2, meaning, size=12, color=INK, fam=BODY, z=7)
        y += h + 10

    # arrows between layers
    for yy in [124, 218, 312]:
        arrow(ax, 95, yy, 95, yy + 10, color=GOLD, lw=2.0, style="-|>", ms=12)

    t(ax, 700, 430, "separates the language,\nthe models, and the\ninstances they describe", size=11, color=GREY, fam=B_IT, ha="left", z=7, ls=1.25)

    return save(fig, "w3_architecture.png")


# 16. Common mechanisms
def mechanisms():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Four Common Mechanisms of UML", sub="Specifications · Adornments · Common divisions · Extensibility")

    cards = [
        ("Specifications", "A symbol is not the whole definition", "behind every box: name, attributes,\noperations, visibility, constraints", MAROON),
        ("Adornments", "Extra information on a symbol", "− private  ·  + public\nstereotypes, multiplicity, constraints", MAROON_DARK),
        ("Common divisions", "Useful paired distinctions", "Class \u2194 Object\nInterface \u2194 Implementation", "#8C2B2D"),
        ("Extensibility", "Extend UML for your domain", "Stereotypes · Tagged values\nConstraints", GOLD),
    ]
    cw, ch, g = 380, 150, 14
    for i, (name, sub, ex, col) in enumerate(cards):
        r, c = divmod(i, 2)
        x = 22 + c * (cw + g)
        y = 30 + (1 - r) * (ch + g)
        box(ax, x, y, cw, ch, WHITE, ec=col, lw=1.8, r=14, z=6)
        box(ax, x, y + ch - 42, cw, 42, col, r=10, z=6)
        t(ax, x + cw / 2, y + ch - 21, name, size=13, color=(MAROON_DARK if col == GOLD else WHITE), fam=H_B, z=7)
        t(ax, x + 16, y + ch - 66, sub, size=10.5, color=col if col != GOLD else MAROON_DARK, fam=B_B, ha="left", z=7)
        t(ax, x + 16, y + 16, ex, size=10.5, color=INK, fam=MONO, ha="left", z=7, ls=1.3)
    return save(fig, "w3_mechanisms.png")


# 17. Chart — diagram counts per family
def chart_diagram_counts():
    W, H = 840, 420
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "How Many Diagrams Per Family?", sub="The UML 2.x diagram families at a glance")

    fams = ["Structural", "Behavioural", "Interaction"]
    counts = [6, 3, 4]
    cols = [MAROON, "#8C2B2D", GOLD]
    y = np.arange(len(fams))[::-1]

    plot = fig.add_axes([0.20, 0.28, 0.62, 0.50])
    bars = plot.barh(y, counts, color=cols, height=0.5, zorder=3)
    plot.set_yticks(y)
    plot.set_yticklabels(fams, fontsize=14, family="Open Sans", color=INK)
    plot.set_xlim(0, 8)
    plot.set_xticks(range(0, 9))
    plot.set_xticklabels([str(i) for i in range(0, 9)], fontsize=11, family="Open Sans", color=GREY)
    for s in ("top", "right"):
        plot.spines[s].set_visible(False)
    plot.spines["left"].set_color(GREY_LIGHT)
    plot.spines["bottom"].set_color(GREY_LIGHT)
    plot.set_xlabel("Number of diagram types", fontsize=12, family="Open Sans", color=INK)
    for yi, v in zip(y, counts):
        plot.text(v + 0.15, yi, str(v), va="center", fontsize=13, family="Open Sans",
                  fontweight="bold", color=MAROON)

    labels = ["Class, Object, Component,\nComposite Structure, Package, Deployment",
              "Use Case, Activity, State Machine",
              "Sequence, Communication,\nTiming, Interaction Overview"]
    for yi, lab in zip(y, labels):
        plot.text(0.4, yi + 0.28, lab, va="bottom", ha="left", fontsize=9.5,
                  family="Open Sans", color=GREY)

    fig.text(0.5, 0.10, "Source of counts: OMG UML 2.5.1 diagram catalogue (structural / behavioural / interaction).",
             ha="center", va="center", fontsize=11, family="Open Sans", fontstyle="italic", color=GREY)
    return save(fig, "w3_chart_diagram_counts.png")


ALL = [
    three_blocks, things, class_example, interface, relationships, multiplicity,
    use_case, sequence, activity, state_machine, component, deployment, package,
    diagram_map, architecture, mechanisms, chart_diagram_counts,
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
    print("Generated", len(made), "week-3 visuals:")
    for m in made:
        print("  -", m)
