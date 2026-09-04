"""
Week 5 visuals — OBJECT-ORIENTED ANALYSIS: OBJECT MODELLING I.
Class / object, notation, links & associations, generalization /
specialization, multiplicity, CASE tools.
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


# --------------------------------------------------------------------------
# UML helpers
# --------------------------------------------------------------------------
def uc(ax, x, y, w, name, attrs=None, ops=None, name_color=WHITE, fill=WHITE,
       ec=MAROON, line_h=19, pad=10, name_size=12.5):
    """UML class box with three compartments."""
    attrs = attrs or []
    ops = ops or []
    h_name = 28
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


def uo(ax, x, y, w, name, vals=None, ec=MAROON, fill=WHITE, line_h=19, pad=10):
    """UML object box — underlined name, attribute = value lines."""
    vals = vals or []
    h = pad + line_h * (1 + len(vals)) + pad
    box(ax, x, y, w, h, fill, ec=ec, lw=1.8, r=0, z=6)
    yn = y + h - pad - line_h / 2
    t(ax, x + w / 2, yn, name, size=11.5, color=MAROON, fam=B_B, z=7)
    ax.plot([x + w * 0.16, x + w * 0.84], [yn - 8, yn - 8], color=ec, lw=1.2, zorder=7)
    yy = yn - 8 - line_h
    for v in vals:
        t(ax, x + 9, yy, v, size=10, color=INK, fam=MONO, ha="left", z=7)
        yy -= line_h
    return (x, y, w, h)


def gtri(ax, x, y, w, h, ec=MAROON, lw=2.0, z=8):
    """Hollow generalization triangle, apex at top (points to the general class)."""
    ax.add_patch(Polygon([(x, y + h), (x - w / 2, y), (x + w / 2, y)],
                         closed=True, fill=False, edgecolor=ec, lw=lw, zorder=z))


def diamond(ax, x, y, w, h, fill=WHITE, ec=MAROON, lw=1.8, z=8):
    ax.add_patch(Polygon([(x, y + h / 2), (x + w / 2, y + h),
                          (x + w, y + h / 2), (x + w / 2, y)],
                         closed=True, facecolor=fill, edgecolor=ec, lw=lw, zorder=z))


# --------------------------------------------------------------------------
# 1. What is OOA
# --------------------------------------------------------------------------
def ooa_whatis():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "What Is Object-Oriented Analysis?",
          sub="Studying the problem domain in terms of objects, classes, responsibilities, relationships and behaviour")

    box(ax, 22, 250, 380, 176, WHITE, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 212, 400, "ANALYSIS = STUDYING A PROBLEM", size=12, color=MAROON, fam=H_B, z=7)
    items = ["what exists", "what users need", "what activities occur",
             "what information is involved", "what rules apply", "how the parts relate"]
    yy = 372
    for i in items:
        t(ax, 48, yy, "+", size=11, color=GOLD, fam=B_B, ha="left", z=7)
        t(ax, 70, yy, i, size=11.5, color=INK, fam=BODY, ha="left", z=7)
        yy -= 20

    box(ax, 438, 250, 380, 176, MAROON_TINT, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 628, 400, "OOA EXAMINES THE DOMAIN AS", size=12, color=MAROON, fam=H_B, z=7)
    oo = ["objects", "classes", "responsibilities", "relationships", "behaviour"]
    yy = 372
    for i in oo:
        t(ax, 462, yy, "+", size=11, color=MAROON, fam=B_B, ha="left", z=7)
        t(ax, 484, yy, i, size=11.5, color=INK, fam=BODY, ha="left", z=7)
        yy -= 20

    # contrast
    box(ax, 22, 70, 380, 150, CREAM_2, ec=GREY, lw=1.4, r=12, z=6)
    t(ax, 212, 196, "TRADITIONAL ANALYSIS", size=11.5, color=GREY, fam=B_B, z=7)
    t(ax, 212, 158, "Input  ->  Process  ->  Output", size=13, color=INK, fam=MONO, z=7)
    t(ax, 212, 116, "focuses on functions and data flow", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 70, 380, 150, WHITE, ec=MAROON, lw=1.8, r=12, z=6)
    t(ax, 628, 196, "OBJECT-ORIENTED ANALYSIS", size=11.5, color=MAROON, fam=B_B, z=7)
    t(ax, 628, 150, "Student · Course · Registration", size=13, color=MAROON_DARK, fam=B_SB, z=7)
    t(ax, 628, 122, "Lecturer · Programme", size=13, color=MAROON_DARK, fam=B_SB, z=7)
    t(ax, 628, 92, "then: how are they related?", size=10.5, color=MAROON_SOFT, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "OOA asks \"who/what are the important objects?\" — not \"what are the inputs and outputs?\"",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w5_ooa_whatis.png")


# --------------------------------------------------------------------------
# 2. Class vs Object
# --------------------------------------------------------------------------
def class_vs_object():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Class vs Object", sub="A class is a description · an object is a particular instance")

    # Car analogy
    box(ax, 22, 250, 380, 176, WHITE, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 212, 400, "THE CAR ANALOGY", size=12, color=MAROON, fam=H_B, z=7)
    box(ax, 110, 330, 204, 42, MAROON, r=8, z=7)
    t(ax, 212, 351, "Car  (CLASS)", size=12.5, color=WHITE, fam=H_SB, z=8)
    t(ax, 212, 300, "describes common characteristics", size=10, color=GREY, fam=B_IT, z=7)
    objs = ["Toyota Corolla ABC123", "Honda Civic DEF456", "Mazda Demio GHI789"]
    xx = 22
    for o in objs:
        box(ax, xx, 236, 122, 40, MAROON_TINT, ec=MAROON_SOFT, lw=1.2, r=7, z=7)
        t(ax, xx + 61, 256, o, size=8.6, color=INK, fam=B_SB, z=8)
        xx += 130

    # Student example
    box(ax, 438, 250, 380, 176, WHITE, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 628, 400, "THE STUDENT EXAMPLE", size=12, color=MAROON, fam=H_B, z=7)
    uc(ax, 450, 280, 150, "Student", attrs=["studentID", "name", "programme", "yearOfStudy"],
       line_h=16, pad=8, name_size=11)
    t(ax, 620, 355, "is a", size=11, color=GREY, fam=B_IT, z=7)
    uo(ax, 640, 268, 172, "Francis : Student", vals=["studentID = ST001", "name = Francis", "year = 3"],
       line_h=16, pad=8)
    t(ax, 628, 236, "class = Student      object = Francis", size=10, color=MAROON_SOFT, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Every object belongs to a class — the class defines the structure, each object holds its own values.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w5_class_vs_object.png")


# --------------------------------------------------------------------------
# 3. UML class notation
# --------------------------------------------------------------------------
def uml_class_notation():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "UML Class Notation", sub="A rectangle with three compartments")

    # annotated example
    uc(ax, 300, 70, 240, "Student",
       attrs=["- studentID : String", "- name : String", "- programme : String", "- year : Integer"],
       ops=["+ registerCourse()", "+ viewResults()"],
       line_h=20, pad=10, name_size=13)

    # callouts
    def callout(x, y, label):
        box(ax, x, y, 150, 34, MAROON, r=8, z=7)
        t(ax, x + 75, y + 17, label, size=10.5, color=WHITE, fam=H_SB, z=8)

    callout(70, 320, "1 · Class name")
    callout(70, 210, "2 · Attributes")
    callout(70, 100, "3 · Operations")
    for y1, y2 in [(337, 340), (227, 245), (117, 160)]:
        ax.plot([220, 300], [y1, y2], color=MAROON_SOFT, lw=1.6, zorder=6)

    t(ax, 555, 340, "name = Student", size=12, color=INK, fam=MONO, ha="left", z=7)
    t(ax, 555, 312, "A class name should", size=11, color=INK, fam=BODY, ha="left", z=7)
    t(ax, 555, 292, "communicate meaning:", size=11, color=INK, fam=BODY, ha="left", z=7)
    for i, nm in enumerate(["Student · Course · Account", "Payment · Employee · Order"]):
        t(ax, 575, 268 - i * 20, nm, size=10.5, color=MAROON_SOFT, fam=MONO, ha="left", z=7)
    t(ax, 555, 208, "poor names:", size=11, color=INK, fam=BODY, ha="left", z=7)
    t(ax, 575, 188, "Thing · Data · Stuff · ClassA", size=10.5, color=GREY, fam=MONO, ha="left", z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "visibility name : type   —   e.g.  - studentID : String   ( - = private )",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w5_uml_class_notation.png")


# --------------------------------------------------------------------------
# 4. Attributes vs operations
# --------------------------------------------------------------------------
def attr_vs_op():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Attributes vs Operations", sub="What the object has/knows  vs  what the object can do")

    box(ax, 22, 120, 380, 250, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 22, 340, 380, 30, MAROON, r=14, z=7)
    t(ax, 212, 355, "ATTRIBUTE", size=13, color=WHITE, fam=H_B, z=8)
    t(ax, 212, 308, "what the object has / knows", size=11, color=GREY, fam=B_IT, z=7)
    for i, a in enumerate(["name", "studentID", "programme", "yearOfStudy"]):
        t(ax, 60, 272 - i * 30, a, size=12.5, color=MAROON_DARK, fam=MONO, ha="left", z=7)

    box(ax, 438, 120, 380, 250, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 438, 340, 380, 30, MAROON_DARK, r=14, z=7)
    t(ax, 628, 355, "OPERATION", size=13, color=WHITE, fam=H_B, z=8)
    t(ax, 628, 308, "what the object can do", size=11, color=GREY, fam=B_IT, z=7)
    for i, a in enumerate(["registerCourse()", "viewResults()", "dropCourse()"]):
        t(ax, 476, 272 - i * 30, a, size=12.5, color=MAROON_SOFT, fam=MONO, ha="left", z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Memory trick:   Attributes = information      ·      Operations = behaviour",
      size=12, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w5_attr_vs_op.png")


# --------------------------------------------------------------------------
# 5. Object notation
# --------------------------------------------------------------------------
def object_notation():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Object Notation", sub="A rectangle with an underlined name and attribute values")

    uo(ax, 300, 110, 240, "Francis : Student",
       vals=["studentID = \"ST001\"", "name = \"John Banda\"", "programme = \"BSc ICT\"", "yearOfStudy = 3"],
       line_h=22, pad=12)

    t(ax, 300, 86, "name is underlined  ·  shows values, not types", size=11, color=GREY, fam=B_IT, z=7)

    # side notes
    box(ax, 30, 300, 260, 90, WHITE, ec=MAROON_SOFT, lw=1.4, r=10, z=6)
    t(ax, 160, 362, "class", size=11.5, color=MAROON, fam=H_SB, z=7)
    t(ax, 160, 338, "describes possible structure", size=10.5, color=INK, fam=BODY, z=7)
    t(ax, 160, 318, "(types, no fixed values)", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 550, 300, 260, 90, MAROON_TINT, ec=MAROON_SOFT, lw=1.4, r=10, z=6)
    t(ax, 680, 362, "object", size=11.5, color=MAROON, fam=H_SB, z=7)
    t(ax, 680, 338, "a specific instance", size=10.5, color=INK, fam=BODY, z=7)
    t(ax, 680, 318, "(with actual values)", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Object name format:   objectName : ClassName   —   e.g.   Francis : Student",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w5_object_notation.png")


# --------------------------------------------------------------------------
# 6. Object modelling process
# --------------------------------------------------------------------------
def process():
    W, H = 840, 440
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Object Modelling Process", sub="A beginner-friendly workflow (do not just underline every noun)")

    steps = [
        ("1", "Problem\nDescription"),
        ("2", "Identify Candidate\nObjects"),
        ("3", "Identify Candidate\nClasses"),
        ("4", "Identify\nAttributes"),
        ("5", "Identify\nOperations"),
        ("6", "Identify\nRelationships"),
        ("7", "Validate\nModel"),
        ("8", "Draw UML\nClass Diagram"),
    ]
    cw, ch, gap = 92, 92, 8
    x = 22
    for n, lab in steps:
        chev(ax, x, 260, cw, ch, MAROON if int(n) < 8 else MAROON_DARK, z=6)
        t(ax, x + cw / 2 + 6, 306, lab, size=9, color=WHITE, fam=B_SB, z=7)
        x += cw + gap

    t(ax, W / 2, 220, "Iterative: the first model is rarely the final model", size=12, color=MAROON_SOFT, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Object modelling requires reasoning, not just drawing — then validate against the requirements.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w5_process.png")


# --------------------------------------------------------------------------
# 7. Noun technique
# --------------------------------------------------------------------------
def noun_technique():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Noun Technique — with a Warning", sub="Nouns are a starting point, not a final answer")

    box(ax, 22, 300, 796, 130, WHITE, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 60, 404, "\"A student registers for a course on Monday.\"", size=13.5, color=INK, fam=B_IT, z=7)
    t(ax, 60, 372, "candidate nouns:", size=11, color=GREY, fam=B_SB, z=7)
    chips = [("student", MAROON, True), ("course", MAROON, True), ("Monday", GREY, False)]
    xx = 200
    for nm, col, ok in chips:
        box(ax, xx, 320, 120, 44, MAROON if ok else GREY_LIGHT, ec=col, lw=1.4, r=9, z=7)
        t(ax, xx + 60, 342, nm, size=12, color=WHITE if ok else GREY, fam=B_SB, z=8)
        t(ax, xx + 60, 316, "class" if ok else "attribute?", size=9, color=GOLD_LIGHT if ok else GREY, fam=B_IT, z=8)
        xx += 136

    box(ax, 22, 120, 380, 150, MAROON_TINT, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 212, 244, "FILTER EVERY NOUN", size=12, color=MAROON, fam=H_B, z=7)
    qs = ["Is it relevant to the system?", "Does the system need to store it?",
          "Does it have meaningful properties?", "Does it have behaviour?", "Does it participate in relationships?"]
    yy = 216
    for q in qs:
        t(ax, 48, yy, "-", size=11, color=GOLD, fam=B_B, ha="left", z=7)
        t(ax, 66, yy, q, size=10.5, color=INK, fam=BODY, ha="left", z=7)
        yy -= 20

    box(ax, 438, 120, 380, 150, WHITE, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 628, 244, "MONDAY — WHY NOT A CLASS?", size=12, color=MAROON, fam=H_B, z=7)
    t(ax, 628, 212, "Monday is a value of a date,", size=11, color=INK, fam=BODY, z=7)
    t(ax, 628, 192, "not a thing the system models.", size=11, color=INK, fam=BODY, z=7)
    t(ax, 628, 158, "It belongs as an attribute or", size=11, color=INK, fam=BODY, z=7)
    t(ax, 628, 138, "value of a Registration.", size=11, color=INK, fam=BODY, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Not every noun is a class — that is one of the most important lessons in OOA.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w5_noun_technique.png")


# --------------------------------------------------------------------------
# 8. Link vs association
# --------------------------------------------------------------------------
def link_vs_association():
    W, H = 840, 450
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Link vs Association", sub="Class level vs object level")

    box(ax, 22, 210, 380, 190, WHITE, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 212, 370, "CLASS LEVEL", size=12, color=MAROON, fam=H_B, z=7)
    uc(ax, 40, 250, 140, "Student", line_h=14, pad=6, name_size=11)
    t(ax, 205, 285, "---------", size=11, color=MAROON, fam=B_B, z=7)
    uc(ax, 242, 250, 140, "Course", line_h=14, pad=6, name_size=11)
    t(ax, 212, 236, "ASSOCIATION", size=12, color=MAROON_DARK, fam=B_SB, z=7)

    box(ax, 438, 210, 380, 190, MAROON_TINT, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 628, 370, "OBJECT LEVEL", size=12, color=MAROON, fam=H_B, z=7)
    uo(ax, 456, 250, 150, "Francis : Student", line_h=14, pad=6)
    t(ax, 621, 285, "---------", size=11, color=MAROON, fam=B_B, z=7)
    uo(ax, 658, 250, 150, "BICT3202 : Course", line_h=14, pad=6)
    t(ax, 628, 236, "LINK", size=12, color=MAROON_DARK, fam=B_SB, z=7)

    # summary table
    box(ax, 22, 60, 380, 110, CREAM_2, ec=GREY, lw=1.2, r=10, z=6)
    t(ax, 212, 148, "ASSOCIATION", size=11.5, color=MAROON, fam=H_SB, z=7)
    t(ax, 212, 120, "connects classes", size=11, color=INK, fam=BODY, z=7)
    t(ax, 212, 100, "Student — Course", size=10.5, color=MAROON_SOFT, fam=MONO, z=7)
    box(ax, 438, 60, 380, 110, CREAM_2, ec=GREY, lw=1.2, r=10, z=6)
    t(ax, 628, 148, "LINK", size=11.5, color=MAROON, fam=H_SB, z=7)
    t(ax, 628, 120, "connects objects", size=11, color=INK, fam=BODY, z=7)
    t(ax, 628, 100, "Francis — BICT3202", size=10.5, color=MAROON_SOFT, fam=MONO, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Association connects classes · Link connects objects — an extremely important distinction.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w5_link_vs_association.png")


# --------------------------------------------------------------------------
# 9. Association naming and roles
# --------------------------------------------------------------------------
def association_naming():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Naming an Association & Roles", sub="Give relationships meaning, not just a line")

    # main line
    uc(ax, 60, 200, 170, "Student", line_h=14, pad=6, name_size=11.5)
    uc(ax, 610, 200, 170, "Course", line_h=14, pad=6, name_size=11.5)
    ax.plot([230, 610], [260, 260], color=MAROON, lw=2.0, zorder=7)
    t(ax, 420, 278, "registers for", size=12.5, color=MAROON_DARK, fam=B_IT, z=7)

    # roles
    t(ax, 140, 196, "role: student", size=10, color=GREY, fam=B_IT, z=7)
    t(ax, 700, 196, "role: registeredCourse", size=10, color=GREY, fam=B_IT, z=7)

    # other examples
    box(ax, 22, 60, 380, 110, WHITE, ec=MAROON, lw=1.4, r=10, z=6)
    t(ax, 212, 148, "MORE NAMES", size=11.5, color=MAROON, fam=H_SB, z=7)
    for i, e in enumerate(["Lecturer — teaches — Course", "Customer — places — Order"]):
        t(ax, 212, 120 - i * 20, e, size=10.5, color=INK, fam=MONO, z=7)
    box(ax, 438, 60, 380, 110, MAROON_TINT, ec=MAROON, lw=1.4, r=10, z=6)
    t(ax, 628, 148, "WHY ROLES MATTER", size=11.5, color=MAROON, fam=H_SB, z=7)
    t(ax, 628, 120, "a role clarifies what each class", size=10.5, color=INK, fam=BODY, z=7)
    t(ax, 628, 100, "plays in the relationship", size=10.5, color=INK, fam=BODY, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "A meaningful association name helps people understand the relationship instantly.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w5_association_naming.png")


# --------------------------------------------------------------------------
# 10. Multiplicity
# --------------------------------------------------------------------------
def multiplicity():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Multiplicity", sub="How many instances can participate in a relationship?")

    uc(ax, 60, 180, 170, "Student", line_h=14, pad=6, name_size=11.5)
    uc(ax, 610, 180, 170, "Course", line_h=14, pad=6, name_size=11.5)
    ax.plot([230, 610], [240, 240], color=MAROON, lw=2.0, zorder=7)
    t(ax, 180, 255, "1", size=16, color=MAROON_DARK, fam=H_B, z=7)
    t(ax, 660, 255, "0..*", size=16, color=MAROON_DARK, fam=H_B, z=7)

    t(ax, W / 2, 150, "One Student can be associated with zero or many Courses.", size=13, color=INK, fam=B_SB, z=7)
    t(ax, W / 2, 126, "Why zero?  A newly admitted student may not yet have registered for any course.",
      size=11, color=MAROON_SOFT, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Read the multiplicity at the FAR end of the association — it constrains the class at the other side.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w5_multiplicity.png")


# --------------------------------------------------------------------------
# 11. Common multiplicities chart
# --------------------------------------------------------------------------
def chart_multiplicity():
    W, H = 840, 460
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Common Multiplicities", sub="Memorise these — but understand what each one means")

    rows = [
        ("1", "Exactly one"),
        ("0..1", "Zero or one"),
        ("*", "Many"),
        ("0..*", "Zero or many"),
        ("1..*", "One or many"),
        ("2..5", "Between two and five"),
    ]
    x0, y0, cw, ch = 60, 70, 300, 52
    for i, (n, m) in enumerate(rows):
        y = y0 + (len(rows) - 1 - i) * (ch + 6)
        box(ax, x0, y, 140, ch, MAROON if i % 2 == 0 else MAROON_DARK, r=9, z=6)
        t(ax, x0 + 70, y + ch / 2, n, size=14, color=WHITE, fam=B_B, z=7)
        box(ax, x0 + 148, y, 340, ch, WHITE, ec=MAROON_SOFT, lw=1.2, r=9, z=6)
        t(ax, x0 + 168, y + ch / 2, m, size=12, color=INK, fam=BODY, ha="left", z=7)

    # example reading
    box(ax, 540, 250, 260, 170, MAROON_TINT, ec=MAROON, lw=1.4, r=10, z=6)
    t(ax, 670, 396, "READ IT CAREFULLY", size=11, color=MAROON, fam=H_SB, z=7)
    t(ax, 670, 366, "Department 1 — 1..* Lecturer", size=11, color=INK, fam=MONO, z=7)
    t(ax, 670, 336, "= a Department must have", size=10.5, color=INK, fam=BODY, z=7)
    t(ax, 670, 316, "at least one Lecturer", size=10.5, color=INK, fam=BODY, z=7)
    t(ax, 670, 286, "0..* allows zero;", size=10.5, color=MAROON_SOFT, fam=BODY, z=7)
    t(ax, 670, 266, "1..* requires at least one.", size=10.5, color=MAROON_SOFT, fam=BODY, z=7)

    return save(fig, "w5_chart_multiplicity.png")


# --------------------------------------------------------------------------
# 12. Cardinality examples
# --------------------------------------------------------------------------
def cardinality():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "One-to-One · One-to-Many · Many-to-Many",
          sub="Three relationship shapes, with multiplicities")

    def row(y, l_name, l_mult, r_name, r_mult, note, tag, tagcol):
        box(ax, 22, y, 796, 112, WHITE, ec=MAROON_SOFT, lw=1.3, r=10, z=6)
        box(ax, 22, y + 78, 190, 34, tagcol, r=8, z=7)
        t(ax, 117, y + 95, tag, size=10, color=WHITE, fam=H_SB, z=8)
        uc(ax, 60, y + 16, 130, l_name, line_h=12, pad=4, name_size=10)
        ax.plot([190, 470], [y + 40, y + 40], color=MAROON, lw=1.8, zorder=7)
        t(ax, 150, y + 52, l_mult, size=12, color=MAROON_DARK, fam=B_B, z=7)
        t(ax, 505, y + 52, r_mult, size=12, color=MAROON_DARK, fam=B_B, z=7)
        uc(ax, 500, y + 16, 130, r_name, line_h=12, pad=4, name_size=10)
        t(ax, 668, y + 60, note, size=9.8, color=GREY, fam=B_IT, z=7)

    row(300, "Student", "1", "IDCard", "1", "each student has one ID card", "1 : 1", MAROON)
    row(178, "Lecturer", "1", "Course", "0..*", "one lecturer, many courses", "1 : M", MAROON_DARK)
    row(56, "Student", "0..*", "Course", "0..*",
        "many-to-many — may need its own class", "M : N", MAROON_SOFT)

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "Many-to-many often hides data (date, status, grade) — a Registration class may be needed.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w5_cardinality.png")


# --------------------------------------------------------------------------
# 13. Generalization
# --------------------------------------------------------------------------
def generalization():
    W, H = 840, 450
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Generalization", sub="A more general class and more specific classes — the \"is-a\" relationship")

    uc(ax, 320, 300, 200, "UniversityUser", attrs=["userID", "name", "email"], ops=["login()", "logout()"],
       line_h=17, pad=8, name_size=12)
    gtri(ax, 420, 274, 46, 26, ec=MAROON, lw=2.0, z=8)
    ax.plot([420, 420], [300, 226], color=MAROON, lw=2.0, zorder=7)
    ax.plot([420, 160], [226, 160], color=MAROON, lw=2.0, zorder=7)
    ax.plot([420, 560], [226, 160], color=MAROON, lw=2.0, zorder=7)
    ax.plot([420, 680], [226, 160], color=MAROON, lw=2.0, zorder=7)

    uc(ax, 30, 40, 160, "Student", attrs=["programme", "yearOfStudy"], line_h=15, pad=6, name_size=11)
    uc(ax, 340, 40, 160, "Lecturer", attrs=["department", "academicRank"], line_h=15, pad=6, name_size=11)
    uc(ax, 650, 40, 160, "Admin", attrs=["role", "accessLevel"], line_h=15, pad=6, name_size=11)

    t(ax, 110, 150, "is a", size=10, color=MAROON_SOFT, fam=B_IT, z=7)
    t(ax, 420, 150, "is a", size=10, color=MAROON_SOFT, fam=B_IT, z=7)
    t(ax, 730, 150, "is a", size=10, color=MAROON_SOFT, fam=B_IT, z=7)

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "The general class holds common features; the specialised classes add their own characteristics.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w5_generalization.png")


# --------------------------------------------------------------------------
# 14. Generalization vs association
# --------------------------------------------------------------------------
def gen_vs_assoc():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Generalization vs Association", sub="Do not confuse these two relationships")

    box(ax, 22, 100, 380, 250, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 22, 320, 380, 30, MAROON, r=14, z=7)
    t(ax, 212, 335, "GENERALIZATION", size=12.5, color=WHITE, fam=H_B, z=8)
    uc(ax, 120, 250, 170, "User", line_h=14, pad=6, name_size=11.5)
    gtri(ax, 205, 224, 40, 24, ec=MAROON, lw=2.0, z=8)
    ax.plot([205, 205], [248, 196], color=MAROON, lw=2.0, zorder=7)
    uc(ax, 120, 130, 170, "Student", line_h=14, pad=6, name_size=11.5)
    t(ax, 212, 118, "\"A Student IS a User\"", size=11.5, color=MAROON_DARK, fam=B_IT, z=7)

    box(ax, 438, 100, 380, 250, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 438, 320, 380, 30, MAROON_DARK, r=14, z=7)
    t(ax, 628, 335, "ASSOCIATION", size=12.5, color=WHITE, fam=H_B, z=8)
    uc(ax, 470, 190, 150, "Student", line_h=14, pad=6, name_size=11.5)
    ax.plot([620, 700], [222, 222], color=MAROON, lw=2.0, zorder=7)
    uc(ax, 700, 190, 150, "Course", line_h=14, pad=6, name_size=11.5)
    t(ax, 628, 168, "\"A Student is RELATED TO a Course\"", size=11, color=MAROON_DARK, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "is-a (generalization)  vs  related-to (association) — check the \"is-a\" test before drawing the triangle.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w5_gen_vs_assoc.png")


# --------------------------------------------------------------------------
# 15. is-a vs has-a
# --------------------------------------------------------------------------
def isa_hasa():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The \"Is-A\" and \"Has-A\" Tests", sub="Two simple questions that prevent most beginner mistakes")

    rows = [
        ("Dog is an Animal", "is-a", "YES — generalization", MAROON, True),
        ("Car has an Engine", "has-a", "whole–part (Week 6)", MAROON_DARK, True),
        ("Student is a Course", "is-a?", "NO — use association", MAROON_SOFT, False),
        ("Car is a Driver", "is-a?", "NO — related, not the same", GREY, False),
    ]
    x0, y0, cw, ch = 60, 70, 560, 56
    for i, (stmt, kind, verdict, col, ok) in enumerate(rows):
        y = y0 + (len(rows) - 1 - i) * (ch + 10)
        box(ax, x0, y, 330, ch, WHITE, ec=col if ok else GREY, lw=1.4, r=9, z=6)
        t(ax, x0 + 20, y + ch / 2, stmt, size=12.5, color=INK, fam=B_SB, ha="left", z=7)
        box(ax, x0 + 340, y, 90, ch, MAROON_TINT if ok else GREY_LIGHT, ec=col if ok else GREY, lw=1.2, r=9, z=6)
        t(ax, x0 + 385, y + ch / 2, kind, size=11, color=col if ok else GREY, fam=MONO, z=7)
        box(ax, x0 + 440, y, 280, ch, MAROON if ok else GREY, ec="none", r=9, z=6)
        t(ax, x0 + 460, y + ch / 2, verdict, size=11.5, color=WHITE, fam=B_SB, ha="left", z=7)

    box(ax, 650, 240, 150, 150, MAROON_TINT, ec=MAROON, lw=1.4, r=10, z=6)
    t(ax, 725, 366, "REMEMBER", size=11, color=MAROON, fam=H_SB, z=7)
    t(ax, 725, 336, "is-a", size=12, color=MAROON_DARK, fam=B_B, z=7)
    t(ax, 725, 312, "generalization", size=10, color=INK, fam=BODY, z=7)
    t(ax, 725, 288, "has-a", size=12, color=MAROON_DARK, fam=B_B, z=7)
    t(ax, 725, 264, "whole–part (Week 6)", size=10, color=INK, fam=BODY, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "When in doubt, say the sentence out loud: \"Is a Student a Course?\" — No.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w5_isa_hasa.png")


# --------------------------------------------------------------------------
# 16. Complete class example
# --------------------------------------------------------------------------
def complete_example():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "A Complete Class Example", sub="Shared features in User · specialised features in Student and Lecturer")

    uc(ax, 300, 300, 240, "User",
       attrs=["- userID : String", "- name : String", "- email : String"],
       ops=["+ login()", "+ logout()"], line_h=19, pad=10, name_size=12.5)
    gtri(ax, 420, 276, 46, 26, ec=MAROON, lw=2.0, z=8)
    ax.plot([420, 420], [300, 224], color=MAROON, lw=2.0, zorder=7)
    ax.plot([420, 190], [224, 170], color=MAROON, lw=2.0, zorder=7)
    ax.plot([420, 650], [224, 170], color=MAROON, lw=2.0, zorder=7)

    uc(ax, 40, 40, 220, "Student", attrs=["- programme : String", "- yearOfStudy : Integer"],
       ops=["+ register()"], line_h=17, pad=8, name_size=11.5)
    uc(ax, 580, 40, 220, "Lecturer", attrs=["- department : String", "- academicRank : String"],
       ops=["+ assignGrade()"], line_h=17, pad=8, name_size=11.5)

    t(ax, 150, 150, "is a", size=10, color=MAROON_SOFT, fam=B_IT, z=7)
    t(ax, 690, 150, "is a", size=10, color=MAROON_SOFT, fam=B_IT, z=7)

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "Common features live in User — no duplication. Each subclass adds its own attributes and operations.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w5_complete_example.png")


# --------------------------------------------------------------------------
# 17. CASE tools
# --------------------------------------------------------------------------
def case_tools():
    W, H = 840, 460
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "CASE Tools", sub="Computer-Aided Software Engineering — assist modelling, never replace analysis")

    box(ax, 22, 280, 796, 130, WHITE, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 60, 384, "CASE = Computer-Aided Software Engineering", size=14, color=MAROON, fam=H_B, ha="left", z=7)
    t(ax, 60, 352, "supports: modelling · diagram creation · documentation ·", size=11.5, color=INK, fam=BODY, ha="left", z=7)
    t(ax, 60, 330, "requirements management · design · code-related workflows", size=11.5, color=INK, fam=BODY, ha="left", z=7)

    box(ax, 22, 100, 380, 150, MAROON_TINT, ec=MAROON, lw=1.4, r=12, z=6)
    t(ax, 212, 224, "EXAMPLE TOOLS", size=12, color=MAROON, fam=H_B, z=7)
    tools = ["Enterprise Architect", "Visual Paradigm", "StarUML", "PlantUML", "draw.io", "Modelio"]
    for i in range(3):
        for j in range(2):
            idx = j * 3 + i
            xx = 40 + i * 122
            yy = 180 - j * 34
            t(ax, xx, yy, tools[idx], size=10.5, color=MAROON_DARK, fam=MONO, ha="left", z=7)

    box(ax, 438, 100, 380, 150, WHITE, ec=MAROON, lw=1.8, r=12, z=6)
    t(ax, 628, 224, "THE KEY POINT", size=12, color=MAROON, fam=H_B, z=7)
    t(ax, 628, 190, "The tool can create a Student box,", size=11, color=INK, fam=BODY, z=7)
    t(ax, 628, 168, "but it does not know whether", size=11, color=INK, fam=BODY, z=7)
    t(ax, 628, 146, "Student should be a class.", size=11, color=INK, fam=BODY, z=7)
    t(ax, 628, 120, "That decision is analysis.", size=11, color=MAROON_SOFT, fam=B_SB, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "The analyst makes modelling decisions — the CASE tool helps represent and manage them.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w5_case_tools.png")


ALL = [
    ooa_whatis, class_vs_object, uml_class_notation, attr_vs_op, object_notation,
    process, noun_technique, link_vs_association, association_naming, multiplicity,
    chart_multiplicity, cardinality, generalization, gen_vs_assoc, isa_hasa,
    complete_example, case_tools,
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
    print("Generated", len(made), "week-5 visuals:")
    for m in made:
        print("  -", m)
