"""
Week 4 visuals — UML BUILDING BLOCKS, RULES, MECHANISMS AND ARCHITECTURE.
Deeper notation detail than Week 3.
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
# UML helpers
# --------------------------------------------------------------------------
def uml_class(ax, x, y, w, name, attrs=None, ops=None, ec=MAROON,
              name_color=WHITE, fill=WHITE, line_h=20, pad=12, name_font=H_SB):
    attrs = attrs or []
    ops = ops or []
    h_name = 30
    h_attrs = pad + line_h * len(attrs) + (pad if attrs else 0)
    h_ops = pad + line_h * len(ops) + (pad if ops else 0)
    h = h_name + h_attrs + h_ops
    box(ax, x, y, w, h, fill, ec=ec, lw=1.8, r=0, z=6)
    box(ax, x, y + h - h_name, w, h_name, ec, r=0, z=6)
    t(ax, x + w / 2, y + h - h_name / 2, name, size=13, color=name_color, fam=name_font, z=7)
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


def usecase(ax, x, y, w, h, label, ec=MAROON):
    ax.add_patch(Ellipse((x + w / 2, y + h / 2), w, h, facecolor=WHITE,
                         edgecolor=ec, lw=1.8, zorder=6))
    t(ax, x + w / 2, y + h / 2, label, size=11, color=MAROON, fam=H_SB, z=7)


def node_box(ax, x, y, w, h, label, depth=8, ec=MAROON, fill=WHITE):
    ax.add_patch(Polygon([(x, y), (x + w, y), (x + w, y + h), (x, y + h)],
                         closed=True, facecolor=fill, edgecolor=ec, lw=1.8, zorder=6))
    ax.add_patch(Polygon([(x + w, y), (x + w + depth, y + depth),
                          (x + w + depth, y + h + depth), (x + w, y + h)],
                         closed=True, facecolor=CREAM_2, edgecolor=ec, lw=1.4, zorder=5))
    ax.add_patch(Polygon([(x, y + h), (x + w, y + h),
                          (x + w + depth, y + h + depth), (x + depth, y + h + depth)],
                         closed=True, facecolor=MAROON_TINT, edgecolor=ec, lw=1.4, zorder=5))
    t(ax, x + w / 2, y + h / 2, label, size=11.5, color=MAROON, fam=H_SB, z=7)


def hollow_triangle(ax, x, y, w, h, ec=MAROON, lw=1.8, z=8):
    """Hollow triangle pointing down (towards +y means point at y). Point at (x, y+h)."""
    ax.add_patch(Polygon([(x, y + h), (x - w / 2, y), (x + w / 2, y)],
                         closed=True, fill=False, edgecolor=ec, lw=lw, zorder=z))


# --------------------------------------------------------------------------
# 1. The five questions
# --------------------------------------------------------------------------
def five_questions():
    W, H = 840, 460
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Five Questions UML Helps You Answer",
          sub="A simple way to understand what UML is for")

    qs = [
        ("1", "WHAT EXISTS?", "Student · Lecturer · Course\nRegistration · Payment · Result", "structural things", MAROON),
        ("2", "HOW ARE THINGS RELATED?", "Student — registers for — Course", "relationships", MAROON_DARK),
        ("3", "WHAT CAN USERS DO?", "Student → Register Course\nStudent → View Results · Pay Fees", "use cases", "#8C2B2D"),
        ("4", "WHAT HAPPENS?", "Login → Select → Check → Register → Confirm", "activities / workflows", MAROON_SOFT),
        ("5", "HOW DO OBJECTS COMMUNICATE?", "Student → System → Database", "interactions", GOLD),
    ]
    cw, ch = 380, 130
    pos = [(22, 260), (438, 260), (22, 90), (438, 90), (230, -40)]
    # reposition: 2x2 grid + 1 bottom
    pos = [(22, 270), (438, 270), (22, 105), (438, 105), (230, 20)]
    for (num, q, ex, fam, col), (x, y) in zip(qs, pos):
        box(ax, x, y, cw, ch - 18, WHITE, ec=col, lw=1.8, r=14, z=6)
        box(ax, x + 14, y + ch - 18 - 44, 34, 34, col, r=10, z=7)
        t(ax, x + 31, y + ch - 18 - 27, num, size=15, color=(MAROON_DARK if col == GOLD else WHITE), fam=H_B, z=8)
        t(ax, x + 60, y + ch - 18 - 26, q, size=13, color=col if col != GOLD else MAROON_DARK, fam=H_B, ha="left", z=7)
        t(ax, x + 16, y + 34, ex, size=11, color=INK, fam=MONO, ha="left", z=7, ls=1.3)
        t(ax, x + cw - 16, y + 12, fam, size=9.5, color=GREY, fam=B_IT, ha="right", z=7)

    box(ax, 22, 250, 796, 18, MAROON_DARK, r=9, z=5)
    t(ax, W / 2, 259, "Different questions need different UML elements and diagrams.", size=12,
      color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w4_five_questions.png")


# 2. Structural things gallery
def structural_things():
    W, H = 840, 440
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Structural Things — What Exists?",
          sub="The relatively static parts of a model: Class · Interface · Object · Component · Node")

    # Class
    uml_class(ax, 30, 200, 150, "Student",
              attrs=["- studentID", "- name"], ops=["+ registerCourse()"])

    # Interface
    box(ax, 210, 200, 150, 120, WHITE, ec=MAROON_DARK, lw=1.8, r=0, z=6)
    box(ax, 210, 288, 150, 32, MAROON_DARK, r=0, z=6)
    t(ax, 285, 304, "«interface»", size=9, color=GOLD_LIGHT, fam=MONO, z=7)
    t(ax, 285, 286, "PaymentService", size=11, color=WHITE, fam=H_SB, z=7)
    ax.plot([210, 360], [268, 268], color=MAROON_DARK, lw=1.0, zorder=7)
    for i, o in enumerate(["processPayment()", "refundPayment()"]):
        t(ax, 222, 248 - i * 22, o, size=9.5, color=INK, fam=MONO, ha="left", z=7)

    # Object
    uml_class(ax, 390, 200, 150, "student001 : Student",
              attrs=["studentID = \"ST001\"", "name = \"Francis\""], ec=MAROON_SOFT,
              name_font=H_MD, line_h=20)
    t(ax, 465, 318, "underlined = instance", size=9, color=GREY, fam=B_IT, z=7)

    # Component
    box(ax, 570, 200, 160, 120, WHITE, ec=MAROON, lw=1.8, r=0, z=6)
    box(ax, 576, 296, 26, 14, WHITE, ec=MAROON, lw=1.4, r=0, z=7)
    t(ax, 650, 250, "Registration\nComponent", size=11, color=MAROON, fam=H_SB, z=7, ls=1.2)
    t(ax, 650, 210, "a modular part", size=9, color=GREY, fam=B_IT, z=7)

    # Node
    node_box(ax, 570, 60, 190, 90, "Application Server\n[University API]", depth=10)
    t(ax, 665, 30, "a node = computational resource", size=9, color=GREY, fam=B_IT, z=7)

    # labels under top row
    t(ax, 105, 175, "Class", size=11, color=MAROON, fam=H_SB, z=7)
    t(ax, 285, 175, "Interface", size=11, color=MAROON_DARK, fam=H_SB, z=7)
    t(ax, 465, 175, "Object", size=11, color=MAROON_SOFT, fam=H_SB, z=7)
    t(ax, 650, 175, "Component", size=11, color=MAROON, fam=H_SB, z=7)

    box(ax, 20, 8, 800, 24, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 20, "Structural things answer “what exists?” — behavioural things answer “what happens?”.",
      size=12, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w4_structural_things.png")


# 3. Class vs object (mould/cake)
def class_vs_object():
    W, H = 840, 420
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Class vs Object — the Cake-Mould Analogy",
          sub="A class is the mould · an object is one cake baked from it")

    # mould
    box(ax, 40, 60, 220, 200, WHITE, ec=MAROON, lw=2, r=14, z=6)
    box(ax, 40, 226, 220, 34, MAROON, r=10, z=6)
    t(ax, 150, 243, "CLASS  (the mould)", size=12, color=WHITE, fam=H_SB, z=7)
    t(ax, 150, 186, "Student", size=15, color=MAROON, fam=H_B, z=7)
    t(ax, 150, 150, "studentID · name\nprogramme · year", size=11, color=INK, fam=MONO, z=7, ls=1.4)
    t(ax, 150, 108, "registerCourse()\nviewResults()", size=11, color=MAROON_SOFT, fam=MONO, z=7, ls=1.4)
    t(ax, 150, 80, "describes the general shape", size=9.5, color=GREY, fam=B_IT, z=7)

    arrow(ax, 268, 160, 336, 160, color=MAROON, lw=3)
    t(ax, 302, 188, "creates", size=11, color=GREY, fam=B_IT, z=7)

    # objects
    objs = [("Francis : Student", "ST001"), ("Grace : Student", "ST002"), ("John : Student", "ST003")]
    for i, (name, idv) in enumerate(objs):
        x = 350 + i * 158
        box(ax, x, 60, 138, 200, WHITE, ec=GOLD, lw=2, r=14, z=6)
        t(ax, x + 69, 226, name, size=11, color=MAROON_DARK, fam=H_SB, z=7)
        ax.plot([x + 14, x + 124], [212, 212], color=GOLD, lw=1.2, zorder=7)
        t(ax, x + 69, 170, "studentID = " + idv, size=10.5, color=INK, fam=MONO, z=7)
        t(ax, x + 69, 140, "name = …", size=10.5, color=INK, fam=MONO, z=7)
        t(ax, x + 69, 108, "OBJECT", size=11, color=MAROON_DARK, fam=H_B, z=7)
        t(ax, x + 69, 84, "a particular instance", size=9.5, color=GREY, fam=B_IT, z=7)

    box(ax, 20, 8, 800, 26, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 21, "Class = general definition · Object = particular instance — underline object names.",
      size=12, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w4_class_vs_object.png")


# 4. The four relationship types
def relationships():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Four Relationship Types",
          sub="Association · Dependency · Generalization · Realization")

    cards = [
        ("ASSOCIATION", "\u201CThese elements are related.\u201D", MAROON),
        ("DEPENDENCY", "\u201CThis element uses that element.\u201D", MAROON_DARK),
        ("GENERALIZATION", "\u201CThis is a specialised type of that.\u201D", "#8C2B2D"),
        ("REALIZATION", "\u201CThis element fulfils the contract.\u201D", GOLD),
    ]
    cw, ch, g = 380, 170, 14
    for i, (name, meaning, col) in enumerate(cards):
        r, c = divmod(i, 2)
        x = 22 + c * (cw + g)
        y = 20 + (1 - r) * (ch + g)
        box(ax, x, y, cw, ch, WHITE, ec=col, lw=1.8, r=14, z=6)
        box(ax, x, y + ch - 42, cw, 42, col, r=10, z=6)
        t(ax, x + cw / 2, y + ch - 21, name, size=12.5, color=(MAROON_DARK if col == GOLD else WHITE), fam=H_B, z=7)
        t(ax, x + cw / 2, y + ch - 66, meaning, size=11, color=col if col != GOLD else MAROON_DARK, fam=B_IT, z=7)

    # notation samples
    # association
    box(ax, 60, 66, 120, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 120, 86, "Student", size=11, color=MAROON, fam=H_SB)
    box(ax, 250, 66, 120, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 310, 86, "Course", size=11, color=MAROON, fam=H_SB)
    ax.plot([180, 250], [86, 86], color=MAROON, lw=2.2, zorder=6)
    t(ax, 215, 102, "solid line", size=9, color=GREY, fam=B_IT)

    # dependency
    box(ax, 490, 66, 150, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 565, 86, "ReportGenerator", size=10.5, color=MAROON, fam=H_SB)
    box(ax, 700, 66, 100, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 750, 86, "Payment", size=11, color=MAROON, fam=H_SB)
    ax.plot([640, 696], [86, 86], color=MAROON, lw=1.8, ls=(0, (4, 3)), zorder=6)
    arrow(ax, 640, 86, 696, 86, color=MAROON, lw=0, style="-|>", ms=14)
    t(ax, 668, 102, "dashed open arrow", size=9, color=GREY, fam=B_IT)

    # generalization
    box(ax, 60, -16, 120, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 120, 4, "Student", size=11, color=MAROON, fam=H_SB)
    box(ax, 250, 18, 120, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 310, 38, "User", size=11, color=MAROON, fam=H_SB)
    ax.plot([180, 250], [4, 18], color=MAROON, lw=1.8, zorder=6)
    hollow_triangle(ax, 250, 18, 34, 22, ec=MAROON)
    t(ax, 215, -14, "hollow triangle to parent", size=9, color=GREY, fam=B_IT)

    # realization
    box(ax, 490, 18, 150, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 565, 38, "«interface»", size=8, color=GOLD, fam=MONO)
    t(ax, 565, 26, "PaymentService", size=10, color=MAROON, fam=H_SB)
    box(ax, 490, -20, 150, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 565, 0, "MobilePayment", size=10.5, color=MAROON, fam=H_SB)
    ax.plot([565, 565], [18, 6], color=MAROON, lw=1.8, ls=(0, (4, 3)), zorder=6)
    hollow_triangle(ax, 565, -4, 34, 22, ec=MAROON)
    t(ax, 620, -18, "dashed hollow triangle", size=9, color=GREY, fam=B_IT)

    return save(fig, "w4_relationships.png")


# 5. Association → class
def association_class():
    W, H = 840, 420
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "When a Relationship Deserves Its Own Class",
          sub="Registration has information of its own — so it becomes a class")

    # simple association (left)
    t(ax, 170, 380, "Simple view", size=12, color=GREY, fam=B_SB)
    box(ax, 40, 300, 120, 50, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 100, 325, "Student", size=12, color=MAROON, fam=H_SB)
    box(ax, 210, 300, 120, 50, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 270, 325, "Course", size=12, color=MAROON, fam=H_SB)
    ax.plot([160, 210], [325, 325], color=MAROON, lw=2.2, zorder=6)
    t(ax, 185, 344, "registers for", size=9.5, color=GREY, fam=B_IT)
    t(ax, 185, 286, "1 — 0..*", size=11, color=MAROON, fam=H_SB)

    arrow(ax, 360, 325, 428, 325, color=GOLD, lw=2.6)
    t(ax, 394, 348, "but it has\nits own data", size=9.5, color=GREY, fam=B_IT, ha="center", z=7)

    # richer model (right)
    uml_class(ax, 460, 250, 150, "Student", attrs=["- studentID", "- name"], line_h=18)
    uml_class(ax, 460, 40, 150, "Course", attrs=["- courseCode", "- credits"], line_h=18)
    uml_class(ax, 660, 145, 170, "Registration",
              attrs=["- registrationID", "- date", "- status", "- semester", "- grade"],
              ops=["+ submit()", "+ approve()"], line_h=18)
    ax.plot([610, 652], [280, 235], color=MAROON, lw=1.8, zorder=6)
    t(ax, 628, 262, "1..*", size=10.5, color=MAROON, fam=H_SB)
    ax.plot([610, 652], [90, 195], color=MAROON, lw=1.8, zorder=6)
    t(ax, 628, 130, "1..*", size=10.5, color=MAROON, fam=H_SB)

    box(ax, 20, 8, 800, 26, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 21, "Key OOAD insight: if a relationship has important data or behaviour, model it as a class.",
      size=12, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w4_association_class.png")


# 6. Visibility adornments
def visibility():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Adornments — Visibility Symbols",
          sub="Extra information attached to a basic element")

    # example class
    uml_class(ax, 300, 80, 240, "Student",
              attrs=["- studentID : String", "+ name : String", "# programme : String", "~ year : int"],
              ops=["+ registerCourse()"], line_h=20)

    t(ax, 300, 360, "Example class", size=11.5, color=GREY, fam=B_SB)
    arrow(ax, 180, 210, 130, 210, color=GOLD, lw=1.8)
    t(ax, 160, 232, "adornments", size=10, color=GREY, fam=B_IT)

    # table
    t(ax, 630, 360, "Visibility", size=13, color=MAROON, fam=H_SB)
    rows = [
        ("+", "public", "visible to all"),
        ("-", "private", "visible only inside the class"),
        ("#", "protected", "visible to subclasses"),
        ("~", "package", "visible within the package"),
    ]
    y = 322
    for sym, name, meaning in rows:
        box(ax, 560, y - 16, 40, 38, MAROON_TINT, ec=MAROON, lw=1.4, r=8, z=6)
        t(ax, 580, y + 3, sym, size=14, color=MAROON_DARK, fam=MONO, z=7)
        t(ax, 612, y + 12, name, size=12, color=MAROON, fam=H_SB, ha="left", z=7)
        t(ax, 612, y - 8, meaning, size=10.5, color=GREY, fam=BODY, ha="left", z=7)
        y -= 56

    box(ax, 20, 8, 800, 26, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 21, "Adornments add information without changing the underlying element.",
      size=12, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w4_visibility.png")


# 7. Well-formedness problems
def wellformed():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Three Ways a Model Can Fail", sub="Notation · Semantics · Requirements")

    cards = [
        ("1 · NOTATION ERROR", "The symbol is drawn incorrectly", "wrong arrowhead, wrong line style, missing compartment", MAROON),
        ("2 · SEMANTIC ERROR", "Right symbol, wrong meaning", "a diamond used “because it looks nice”", MAROON_DARK),
        ("3 · REQUIREMENT ERROR", "Valid UML, wrong system", "perfectly drawn — but not what the user needs", GOLD),
    ]
    cw, ch, g = 260, 200, 14
    x = 22
    for (name, sub, ex, col), x in zip(cards, [22, 296, 570]):
        box(ax, x, 30, cw, ch, WHITE, ec=col, lw=1.8, r=14, z=6)
        box(ax, x, 186, cw, 44, col, r=10, z=6)
        t(ax, x + cw / 2, 208, name, size=12.5, color=(MAROON_DARK if col == GOLD else WHITE), fam=H_B, z=7)
        t(ax, x + cw / 2, 156, sub, size=12, color=INK, fam=B_SB, z=7)
        t(ax, x + cw / 2, 96, ex, size=11, color=GREY, fam=BODY, z=7, ls=1.3)
        t(ax, x + cw / 2, 56, "must be fixed", size=10, color=MAROON_SOFT, fam=B_IT, z=7)

    box(ax, 22, 6, 796, 24, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 18, "A perfectly drawn UML diagram can still describe the wrong system.",
      size=12.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w4_wellformed.png")


# 8. Quality checklist
def checklist():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "UML Quality Checklist", sub="Seven questions before accepting a diagram")

    qs = [
        "Are the correct UML symbols being used?",
        "Are relationships represented correctly?",
        "Are names meaningful?",
        "Are multiplicities correct?",
        "Does the model correspond to the requirements?",
        "Can another person understand the model?",
        "Have unnecessary details been removed?",
    ]
    left = [qs[i] for i in range(0, 7, 2)]
    right = [qs[i] for i in range(1, 7, 2)]
    for i, s in enumerate(left):
        n = 2 * i + 1
        y = 330 - i * 68
        box(ax, 40, y - 18, 360, 56, WHITE, ec=MAROON, lw=1.6, r=12, z=6)
        box(ax, 52, y + 2, 30, 30, MAROON, r=8, z=7)
        t(ax, 67, y + 17, str(n), size=12, color=WHITE, fam=H_B, z=8)
        t(ax, 100, y + 10, s, size=12, color=INK, fam=BODY, ha="left", z=7)
    for i, s in enumerate(right):
        n = 2 * i + 2
        y = 330 - i * 68
        box(ax, 430, y - 18, 370, 56, WHITE, ec=MAROON_DARK, lw=1.6, r=12, z=6)
        box(ax, 442, y + 2, 30, 30, MAROON_DARK, r=8, z=7)
        t(ax, 457, y + 17, str(n), size=12, color=WHITE, fam=H_B, z=8)
        t(ax, 490, y + 10, s, size=12, color=INK, fam=BODY, ha="left", z=7)
    return save(fig, "w4_checklist.png")


# 9. Stereotypes
def stereotypes():
    W, H = 840, 420
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Stereotypes — Specialised UML Meaning",
          sub="Written in guillemets, a stereotype tells the reader how to treat the element")

    cards = [
        ("«entity»", "Student", "a persistent business object", MAROON),
        ("«controller»", "RegistrationController", "coordinates the application logic", MAROON_DARK),
        ("«boundary»", "RegistrationPage", "a boundary / UI role", "#8C2B2D"),
    ]
    cw, ch, g = 260, 170, 14
    for (st, name, desc, col), x in zip(cards, [22, 296, 570]):
        box(ax, x, 30, cw, ch, WHITE, ec=col, lw=1.8, r=14, z=6)
        box(ax, x + 20, 150, cw - 40, 50, col, r=10, z=7)
        t(ax, x + cw / 2, 188, st, size=12.5, color=(MAROON_DARK if col == GOLD else WHITE), fam=MONO, z=8)
        t(ax, x + cw / 2, 168, name, size=13, color=WHITE, fam=H_SB, z=8)
        t(ax, x + cw / 2, 106, desc, size=11, color=GREY, fam=BODY, z=7, ls=1.3)
        t(ax, x + cw / 2, 58, "a class, specialised", size=10, color=MAROON_SOFT, fam=B_IT, z=7)

    box(ax, 22, 8, 796, 24, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 20, "“Treat this element as a specialised kind of UML element.”",
      size=12, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w4_stereotypes.png")


# 10. Extensibility comparison
def extensibility():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Stereotype vs Tagged Value vs Constraint",
          sub="Three extensibility mechanisms — easy memory trick below")

    cards = [
        ("STEREOTYPE", "What special kind?", "«entity» Student", MAROON),
        ("TAGGED VALUE", "What extra information?", "Student {author = \"Analysis Team\"}", MAROON_DARK),
        ("CONSTRAINT", "What condition must hold?", "Student {age >= 18}", GOLD),
    ]
    cw, ch, g = 260, 200, 14
    for (name, q, ex, col), x in zip(cards, [22, 296, 570]):
        box(ax, x, 30, cw, ch, WHITE, ec=col, lw=1.8, r=14, z=6)
        box(ax, x, 186, cw, 44, col, r=10, z=6)
        t(ax, x + cw / 2, 208, name, size=12, color=(MAROON_DARK if col == GOLD else WHITE), fam=H_B, z=7)
        t(ax, x + cw / 2, 156, q, size=12.5, color=INK, fam=B_SB, z=7)
        box(ax, x + 16, 70, cw - 32, 62, CREAM_2, ec=col, lw=1.2, r=10, z=7)
        t(ax, x + cw / 2, 101, ex, size=11, color=MAROON_DARK, fam=MONO, z=7)

    return save(fig, "w4_extensibility.png")


# 11. Architecture analogy + context levels
def architecture_analogy():
    W, H = 840, 460
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "M0–M3 — the Language Analogy",
          sub="The same word can live at different levels, depending on context")

    layers = [
        ("M3", "Rules for creating languages", "the grammar of grammars — MOF", MAROON_DEEP, WHITE),
        ("M2", "Grammar & vocabulary definitions", "what “Class”, “Attribute”, “Association” mean", MAROON_DARK, WHITE),
        ("M1", "A sentence written in the language", "your model: Student, Course, Registration", MAROON, WHITE),
        ("M0", "The real-world things referred to", "Francis : Student, BICT3202 : Course", GOLD, MAROON_DARK),
    ]
    y = 40
    h = 84
    for code, name, meaning, col, tcol in layers:
        box(ax, 20, y, 90, h, col, r=12, z=6)
        t(ax, 65, y + h / 2, code, size=19, color=tcol, fam=H_B, z=7)
        box(ax, 122, y + 10, 470, h - 20, WHITE, ec=col, lw=1.4, r=10, z=6)
        t(ax, 357, y + h / 2 + 12, name, size=11.5, color=MAROON_DARK, fam=H_SB, z=7)
        t(ax, 357, y + h / 2 - 14, meaning, size=11, color=INK, fam=BODY, z=7)
        y += h + 8
    for yy in [124, 216, 308]:
        arrow(ax, 65, yy, 65, yy + 8, color=GOLD, lw=2.0, style="-|>", ms=12)

    # context box
    box(ax, 620, 120, 200, 260, CREAM_2, ec=GOLD, lw=1.6, r=12, z=6)
    t(ax, 720, 356, "“Student” at which level?", size=12, color=MAROON_DARK, fam=H_SB, z=7)
    t(ax, 720, 300, "Student : Class\n= an M1 model element", size=11.5, color=INK, fam=BODY, z=7, ls=1.4)
    ax.plot([640, 800], [268, 268], color=GOLD, lw=1.0, zorder=7)
    t(ax, 720, 232, "“Class” as a concept\n= the M2 metamodel", size=11.5, color=INK, fam=BODY, z=7, ls=1.4)
    ax.plot([640, 800], [198, 198], color=GOLD, lw=1.0, zorder=7)
    t(ax, 720, 168, "Francis : Student\n= an M0 instance", size=11.5, color=INK, fam=BODY, z=7, ls=1.4)
    t(ax, 720, 132, "Same word — the level\ndepends on context.", size=10.5, color=GREY, fam=B_IT, z=7, ls=1.25)

    return save(fig, "w4_architecture_analogy.png")


# 12. Model vs diagram
def model_vs_diagram():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Model vs Diagram", sub="One model — many views")

    box(ax, 40, 120, 220, 140, MAROON, r=14, z=6)
    t(ax, 150, 230, "UML MODEL", size=15, color=WHITE, fam=H_B, z=7)
    t(ax, 150, 196, "the underlying collection\nof elements and\nrelationships", size=11, color=GOLD_LIGHT, fam=BODY, z=7, ls=1.3)
    t(ax, 150, 148, "one model", size=10.5, color=CREAM, fam=B_IT, z=7)

    views = ["Class Diagram", "Sequence Diagram", "Activity Diagram", "State Diagram"]
    ys = [300, 200, 100, 20]
    for name, y in zip(views, ys):
        box(ax, 420, y, 300, 56, WHITE, ec=MAROON, lw=1.6, r=10, z=6)
        t(ax, 570, y + 28, name, size=12.5, color=MAROON, fam=H_SB, z=7)
        arrow(ax, 264, 190, 412, y + 28, color=MAROON, lw=1.8)

    t(ax, 570, 380, "each is a VIEW of selected elements", size=11, color=GREY, fam=B_IT, z=7)

    box(ax, 40, 8, 760, 30, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 23, "One model can support multiple views — that's why UML suits complex systems.",
      size=12, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w4_model_vs_diagram.png")


# 13. One system, multiple views (banking)
def multiview():
    W, H = 840, 460
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "One Banking System — Five Views",
          sub="Not five systems — five views of the same system")

    # class view
    box(ax, 20, 300, 250, 100, WHITE, ec=MAROON, lw=1.6, r=10, z=6)
    t(ax, 145, 372, "CLASS VIEW", size=11, color=MAROON, fam=H_B, z=7)
    t(ax, 145, 336, "Customer · Account\nTransaction · Bank", size=11, color=INK, fam=MONO, z=7, ls=1.3)

    # use case view
    box(ax, 295, 300, 250, 100, WHITE, ec=MAROON, lw=1.6, r=10, z=6)
    t(ax, 420, 372, "USE-CASE VIEW", size=11, color=MAROON, fam=H_B, z=7)
    t(ax, 420, 330, "Withdraw · Deposit · Transfer", size=11, color=INK, fam=MONO, z=7)

    # sequence view
    box(ax, 570, 300, 250, 100, WHITE, ec=MAROON, lw=1.6, r=10, z=6)
    t(ax, 695, 372, "SEQUENCE VIEW", size=11, color=MAROON, fam=H_B, z=7)
    t(ax, 695, 330, "Customer → ATM → Bank Server\n→ Database", size=11, color=INK, fam=MONO, z=7, ls=1.3)

    # activity view
    box(ax, 20, 120, 250, 150, WHITE, ec=MAROON_DARK, lw=1.6, r=10, z=6)
    t(ax, 145, 244, "ACTIVITY VIEW", size=11, color=MAROON_DARK, fam=H_B, z=7)
    steps = ["Insert Card", "Enter PIN", "Select Transaction", "Enter Amount", "Validate", "Complete"]
    for i, st in enumerate(steps):
        t(ax, 145, 212 - i * 22, st, size=10.5, color=INK, fam=BODY, z=7)
    for i in range(len(steps) - 1):
        arrow(ax, 145, 206 - i * 22, 145, 194 - i * 22, color=MAROON, lw=1.4, style="-|>", ms=9)

    # state view
    box(ax, 295, 120, 525, 150, WHITE, ec=GOLD, lw=1.6, r=10, z=6)
    t(ax, 557, 244, "STATE VIEW", size=11, color=MAROON_DARK, fam=H_B, z=7)
    states = ["Active", "Blocked", "Closed"]
    for i, name in enumerate(states):
        x = 350 + i * 140
        box(ax, x, 156, 100, 44, MAROON_TINT, ec=MAROON, lw=1.4, r=16, z=7)
        t(ax, x + 50, 178, name, size=11.5, color=MAROON, fam=H_SB, z=8)
        if i < 2:
            arrow(ax, x + 100, 178, x + 130, 178, color=MAROON, lw=1.6, style="-|>", ms=10)

    return save(fig, "w4_multiview.png")


# 14. Generalization mistake
def generalization_mistake():
    W, H = 840, 360
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Common Mistake — Generalization Direction",
          sub="The hollow triangle must point to the general (parent) class")

    # wrong
    box(ax, 40, 60, 300, 180, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    t(ax, 190, 212, "WRONG", size=12, color=MAROON, fam=H_B, z=7)
    box(ax, 90, 130, 110, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 145, 150, "Student", size=11.5, color=MAROON, fam=H_SB)
    box(ax, 90, 70, 110, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 145, 90, "User", size=11.5, color=MAROON, fam=H_SB)
    ax.plot([145, 145], [130, 118], color=MAROON, lw=1.8, zorder=6)
    hollow_triangle(ax, 145, 96, 36, 24, ec=MAROON)
    t(ax, 190, 48, "triangle points away from the parent", size=10.5, color=MAROON_SOFT, fam=B_IT, z=7)

    # arrow to correct
    arrow(ax, 350, 150, 420, 150, color=GOLD, lw=2.6)
    t(ax, 385, 176, "fix", size=11, color=GOLD, fam=H_SB)

    # correct
    box(ax, 440, 60, 300, 180, CREAM_2, ec=GOLD, lw=1.8, r=14, z=6)
    t(ax, 590, 212, "CORRECT", size=12, color=MAROON_DARK, fam=H_B, z=7)
    box(ax, 490, 130, 110, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 545, 150, "User", size=11.5, color=MAROON, fam=H_SB)
    box(ax, 490, 70, 110, 40, WHITE, ec=MAROON, lw=1.6, r=0)
    t(ax, 545, 90, "Student", size=11.5, color=MAROON, fam=H_SB)
    ax.plot([545, 545], [130, 118], color=MAROON, lw=1.8, zorder=6)
    hollow_triangle(ax, 545, 96, 36, 24, ec=MAROON)
    t(ax, 590, 48, "triangle points to the parent", size=10.5, color=MAROON_SOFT, fam=B_IT, z=7)

    box(ax, 20, 8, 800, 26, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 21, "Student is a type of User — so the arrow points to User. A very common beginner error.",
      size=12, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w4_generalization_mistake.png")


# 15. E-learning case study
def elearning():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Case Study — Exploits University E-Learning System",
          sub="Candidate classes, relationships and a submission state machine")

    def cb(x, y, name, attrs, w=130):
        uml_class(ax, x, y, w, name, attrs=attrs, line_h=18, pad=10)

    cb(20, 220, "Student", ["- studentID", "- name"])
    cb(190, 220, "Lecturer", ["- lecturerID", "- name"])
    cb(360, 220, "Course", ["- courseCode", "- title"])
    cb(530, 220, "Assignment", ["- assignmentID", "- title"])
    cb(20, 40, "Submission", ["- submissionID", "- date", "- status"])
    cb(190, 40, "Grade", ["- gradeID", "- value"])
    cb(360, 40, "LearningMaterial", ["- materialID", "- type"])

    # relationships
    ax.plot([85, 250], [220, 250], color=MAROON, lw=1.6, zorder=6)
    t(ax, 168, 262, "enrols", size=9, color=GREY, fam=B_IT)
    ax.plot([320, 360], [250, 250], color=MAROON, lw=1.6, zorder=6)
    t(ax, 340, 262, "teaches", size=9, color=GREY, fam=B_IT)
    ax.plot([85, 85], [220, 200], color=MAROON, lw=1.6, zorder=6)
    ax.plot([480, 480], [220, 200], color=MAROON, lw=1.6, zorder=6)
    ax.plot([85, 340], [60, 60], color=MAROON, lw=1.6, zorder=6)
    ax.plot([260, 360], [60, 60], color=MAROON, lw=1.6, zorder=6)
    t(ax, 200, 44, "submits / graded", size=9, color=GREY, fam=B_IT)

    # state machine
    box(ax, 560, 60, 260, 140, CREAM_2, ec=GOLD, lw=1.6, r=12, z=6)
    t(ax, 690, 178, "Submission lifecycle", size=11, color=MAROON_DARK, fam=H_SB, z=7)
    states = ["Draft", "Submitted", "Marked", "Returned"]
    y = 150
    for name in states:
        box(ax, 585, y - 16, 110, 28, WHITE, ec=MAROON, lw=1.4, r=14, z=7)
        t(ax, 640, y - 2, name, size=10.5, color=MAROON, fam=H_SB, z=8)
        if name != "Returned":
            arrow(ax, 640, y - 16, 640, y - 34, color=MAROON, lw=1.4, style="-|>", ms=9)
        y -= 28

    box(ax, 20, 8, 800, 24, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 20, "Classes + relationships + the state changes of a Submission — three UML views of one system.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w4_elearning.png")


# 16. Chart — abstraction power
def chart_abstraction():
    W, H = 840, 420
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Power of Abstraction",
          sub="Real-world scale vs what we actually model (log scale)")

    labels = ["Students", "Courses", "Lecturers", "Departments"]
    real = [10000, 500, 300, 50]
    colors = [MAROON, MAROON_SOFT, GOLD, "#8C2B2D"]
    y = np.arange(len(labels))[::-1]

    plot = fig.add_axes([0.16, 0.24, 0.62, 0.55])
    bars = plot.barh(y, real, color=colors, height=0.55, zorder=3)
    plot.set_yticks(y)
    plot.set_yticklabels(labels, fontsize=13, family="Open Sans", color=INK)
    plot.set_xscale("log")
    plot.set_xlim(1, 100000)
    plot.set_xticks([1, 10, 100, 1000, 10000, 100000])
    plot.set_xticklabels(["1", "10", "100", "1k", "10k", "100k"], fontsize=10.5,
                         family="Open Sans", color=GREY)
    for s in ("top", "right"):
        plot.spines[s].set_visible(False)
    plot.spines["left"].set_color(GREY_LIGHT)
    plot.spines["bottom"].set_color(GREY_LIGHT)
    plot.set_xlabel("Real-world entities (log scale)", fontsize=12, family="Open Sans", color=INK)
    for yi, v in zip(y, real):
        plot.text(v * 1.15, yi, f"{v:,}", va="center", fontsize=11, family="Open Sans",
                  fontweight="semibold", color=MAROON)

    box(ax, 660, 120, 160, 120, CREAM_2, ec=GOLD, lw=1.6, r=12, z=6)
    t(ax, 740, 210, "We model just", size=11, color=MAROON_DARK, fam=B_SB, z=7)
    t(ax, 740, 182, "4 classes", size=16, color=MAROON, fam=H_B, z=7)
    t(ax, 740, 152, "Student · Course\nLecturer · Department", size=10.5, color=INK, fam=MONO, z=7, ls=1.3)

    fig.text(0.5, 0.08, "A manageable representation — not all 10,000 students drawn on the diagram.",
             ha="center", va="center", fontsize=11, family="Open Sans", fontstyle="italic", color=GREY)
    return save(fig, "w4_chart_abstraction.png")


# 17. Chart — grouping into packages
def chart_packages():
    W, H = 840, 420
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Grouping Classes into Packages",
          sub="13 classes, 5 packages — complexity divided into manageable pieces")

    packages = ["Student\nManagement", "Finance", "Examination", "Library", "Accommodation"]
    counts = [4, 3, 3, 3, 2]
    cols = [MAROON, MAROON_DARK, "#8C2B2D", MAROON_SOFT, GOLD]
    x = np.arange(len(packages))

    plot = fig.add_axes([0.14, 0.28, 0.68, 0.50])
    bars = plot.bar(x, counts, color=cols, width=0.6, zorder=3)
    plot.set_xticks(x)
    plot.set_xticklabels(packages, fontsize=11.5, family="Open Sans", color=INK)
    plot.set_ylim(0, 5)
    plot.set_yticks([0, 1, 2, 3, 4])
    plot.set_ylabel("Classes in package", fontsize=12, family="Open Sans", color=INK)
    for s in ("top", "right"):
        plot.spines[s].set_visible(False)
    plot.spines["left"].set_color(GREY_LIGHT)
    plot.spines["bottom"].set_color(GREY_LIGHT)
    plot.grid(axis="y", color=GREY_LIGHT, lw=0.7, zorder=1)
    for xi, v in zip(x, counts):
        plot.text(xi, v + 0.12, str(v), ha="center", fontsize=13, family="Open Sans",
                  fontweight="bold", color=MAROON)

    fig.text(0.5, 0.08, "Illustrative — derived from the Week 4 complexity-management example (Section 62).",
             ha="center", va="center", fontsize=11, family="Open Sans", fontstyle="italic", color=GREY)
    return save(fig, "w4_chart_packages.png")


ALL = [
    five_questions, structural_things, class_vs_object, relationships,
    association_class, visibility, wellformed, checklist, stereotypes,
    extensibility, architecture_analogy, model_vs_diagram, multiview,
    generalization_mistake, elearning, chart_abstraction, chart_packages,
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
    print("Generated", len(made), "week-4 visuals:")
    for m in made:
        print("  -", m)
