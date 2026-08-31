"""
Week 6 visuals — OBJECT-ORIENTED ANALYSIS: OBJECT MODELLING II.
Aggregation · Inheritance · Polymorphism · Grouping.
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


def gtri(ax, x, y, w, h, ec=MAROON, lw=2.0, z=8):
    """Hollow generalization triangle, apex at top (points to the general class)."""
    ax.add_patch(Polygon([(x, y + h), (x - w / 2, y), (x + w / 2, y)],
                         closed=True, fill=False, edgecolor=ec, lw=lw, zorder=z))


def hdiam(ax, x, y, w, h, ec=MAROON, lw=1.8, z=8, fill=WHITE):
    """Hollow diamond (aggregation) — vertical orientation."""
    ax.add_patch(Polygon([(x, y + h / 2), (x + w / 2, y + h),
                          (x + w, y + h / 2), (x + w / 2, y)],
                         closed=True, facecolor=fill, edgecolor=ec, lw=lw, zorder=z))


def fdiam(ax, x, y, w, h, ec=MAROON_DARK, z=8):
    """Filled diamond (composition) — vertical orientation."""
    ax.add_patch(Polygon([(x, y + h / 2), (x + w / 2, y + h),
                          (x + w, y + h / 2), (x + w / 2, y)],
                         closed=True, facecolor=ec, edgecolor=ec, lw=1.2, zorder=z))


# --------------------------------------------------------------------------
# 1. Where Week 6 fits
# --------------------------------------------------------------------------
def progression():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Where Week 6 Fits", sub="Building on Week 5's objects, associations and generalization")

    box(ax, 22, 210, 380, 150, WHITE, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 212, 336, "WEEK 5", size=13, color=MAROON, fam=H_B, z=7)
    for i, q in enumerate(["What objects/classes exist?", "How are they related?", "Generalization / specialization"]):
        t(ax, 60, 296 - i * 24, q, size=11, color=INK, fam=BODY, ha="left", z=7)

    box(ax, 438, 210, 380, 150, MAROON_TINT, ec=MAROON, lw=1.8, r=12, z=6)
    t(ax, 628, 336, "WEEK 6", size=13, color=MAROON, fam=H_B, z=7)
    for i, q in enumerate(["Whole-part structures? (aggregation)", "Inherited characteristics? (inheritance)",
                           "Different responses? (polymorphism)", "Organize related classes? (grouping)"]):
        t(ax, 476, 296 - i * 24, q, size=11, color=INK, fam=BODY, ha="left", z=7)

    arrow(ax, 402, 280, 438, 280, color=MAROON_SOFT, lw=2.2)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Aggregation, inheritance and polymorphism are not isolated ideas — together they make models reusable and understandable.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w6_progression.png")


# --------------------------------------------------------------------------
# 2. Whole-part concept
# --------------------------------------------------------------------------
def whole_part():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Aggregation — the Whole-Part Relationship",
          sub="One object represents a whole or collection; other objects represent its parts")

    # University -> Department chain
    uc(ax, 60, 220, 200, "University", line_h=14, pad=6, name_size=12)
    hdiam(ax, 270, 226, 26, 26)
    ax.plot([260, 290], [240, 240], color=MAROON, lw=1.8, zorder=7)
    ax.plot([296, 330], [240, 240], color=MAROON, lw=1.8, zorder=7)
    uc(ax, 330, 220, 200, "Department", line_h=14, pad=6, name_size=12)

    # whole / part labels
    box(ax, 40, 120, 130, 46, MAROON, r=9, z=7)
    t(ax, 105, 143, "WHOLE", size=11.5, color=WHITE, fam=H_SB, z=8)
    box(ax, 300, 120, 130, 46, MAROON_TINT, ec=MAROON_SOFT, lw=1.3, r=9, z=7)
    t(ax, 365, 143, "PART", size=11.5, color=MAROON_DARK, fam=H_SB, z=8)

    # other examples
    box(ax, 550, 200, 260, 170, WHITE, ec=MAROON, lw=1.4, r=10, z=6)
    t(ax, 680, 344, "MORE EXAMPLES", size=11.5, color=MAROON, fam=H_SB, z=7)
    for i, e in enumerate(["Library <>-- Book", "Department <>-- Lecturer"]):
        t(ax, 680, 312 - i * 26, e, size=11.5, color=INK, fam=MONO, z=7)
    t(ax, 680, 248, "\"A Library contains Books\"", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "The hollow diamond sits on the WHOLE side:  University <>-- Department",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w6_whole_part.png")


# --------------------------------------------------------------------------
# 3. Aggregation vs ordinary association
# --------------------------------------------------------------------------
def agg_vs_assoc():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Aggregation vs Ordinary Association", sub="A general relationship vs a whole-part relationship")

    box(ax, 22, 120, 380, 250, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 22, 340, 380, 30, MAROON, r=14, z=7)
    t(ax, 212, 355, "ASSOCIATION", size=12.5, color=WHITE, fam=H_B, z=8)
    uc(ax, 40, 210, 150, "Student", line_h=14, pad=6, name_size=11.5)
    ax.plot([190, 250], [240, 240], color=MAROON, lw=2.0, zorder=7)
    uc(ax, 250, 210, 150, "Course", line_h=14, pad=6, name_size=11.5)
    t(ax, 212, 170, "\"A Student is related to a Course\"", size=11.5, color=MAROON_DARK, fam=B_IT, z=7)

    box(ax, 438, 120, 380, 250, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 438, 340, 380, 30, MAROON_DARK, r=14, z=7)
    t(ax, 628, 355, "AGGREGATION", size=12.5, color=WHITE, fam=H_B, z=8)
    uc(ax, 460, 210, 170, "Department", line_h=14, pad=6, name_size=11.5)
    hdiam(ax, 640, 226, 26, 26)
    ax.plot([630, 654], [240, 240], color=MAROON, lw=1.8, zorder=7)
    ax.plot([680, 710], [240, 240], color=MAROON, lw=1.8, zorder=7)
    uc(ax, 710, 210, 170, "Lecturer", line_h=14, pad=6, name_size=11.5)
    t(ax, 628, 170, "\"A Department has Lecturers\"", size=11.5, color=MAROON_DARK, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Association = general relationship · Aggregation = whole-part relationship",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w6_agg_vs_assoc.png")


# --------------------------------------------------------------------------
# 4. Aggregation vs composition
# --------------------------------------------------------------------------
def agg_vs_comp():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Aggregation vs Composition", sub="Hollow diamond (weak/shared)  vs  filled diamond (strong)")

    box(ax, 22, 110, 380, 260, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 22, 340, 380, 30, MAROON, r=14, z=7)
    t(ax, 212, 355, "AGGREGATION  (hollow diamond)", size=13, color=WHITE, fam=H_B, z=8)
    uc(ax, 40, 210, 170, "Department", line_h=14, pad=6, name_size=11.5)
    hdiam(ax, 220, 226, 26, 26)
    ax.plot([210, 234], [240, 240], color=MAROON, lw=1.8, zorder=7)
    ax.plot([260, 290], [240, 240], color=MAROON, lw=1.8, zorder=7)
    uc(ax, 290, 210, 160, "Lecturer", line_h=14, pad=6, name_size=11.5)
    t(ax, 212, 168, "The Lecturer can exist independently", size=11, color=INK, fam=BODY, z=7)
    t(ax, 212, 146, "— can move to another department.", size=11, color=INK, fam=BODY, z=7)

    box(ax, 438, 110, 380, 260, MAROON_TINT, ec=MAROON_DARK, lw=1.8, r=14, z=6)
    box(ax, 438, 340, 380, 30, MAROON_DARK, r=14, z=7)
    t(ax, 628, 355, "COMPOSITION  (filled diamond)", size=13, color=WHITE, fam=H_B, z=8)
    uc(ax, 456, 210, 170, "House", line_h=14, pad=6, name_size=11.5)
    fdiam(ax, 636, 226, 26, 26)
    ax.plot([626, 650], [240, 240], color=MAROON_DARK, lw=1.8, zorder=7)
    ax.plot([676, 706], [240, 240], color=MAROON_DARK, lw=1.8, zorder=7)
    uc(ax, 706, 210, 160, "Room", line_h=14, pad=6, name_size=11.5)
    t(ax, 628, 168, "The Room is strongly owned", size=11, color=INK, fam=BODY, z=7)
    t(ax, 628, 146, "by that particular House.", size=11, color=INK, fam=BODY, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "<> = weak/shared whole-part · <#> = strong/composite whole-part — the filled diamond owns its parts.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w6_agg_vs_comp.png")


# --------------------------------------------------------------------------
# 5. Football team (weak aggregation)
# --------------------------------------------------------------------------
def football():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Weak Aggregation — a Football Team", sub="The parts can outlive the whole")

    box(ax, 22, 120, 380, 250, WHITE, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 212, 344, "MANCHESTER UNITED", size=12.5, color=MAROON, fam=H_B, z=7)
    uc(ax, 110, 230, 200, "FootballTeam", line_h=14, pad=6, name_size=12)
    hdiam(ax, 320, 246, 26, 26)
    ax.plot([310, 334], [260, 260], color=MAROON, lw=1.8, zorder=7)
    ax.plot([360, 390], [260, 260], color=MAROON, lw=1.8, zorder=7)
    uc(ax, 390, 230, 170, "Player", line_h=14, pad=6, name_size=12)
    t(ax, 212, 190, "If the player leaves the club,", size=11, color=INK, fam=BODY, z=7)
    t(ax, 212, 168, "the player does not cease to exist.", size=11, color=INK, fam=BODY, z=7)

    box(ax, 438, 120, 380, 250, MAROON_TINT, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 628, 344, "CLASSROOM", size=12.5, color=MAROON, fam=H_B, z=7)
    uc(ax, 500, 230, 180, "Classroom", line_h=14, pad=6, name_size=12)
    hdiam(ax, 690, 246, 26, 26)
    ax.plot([680, 704], [260, 260], color=MAROON, lw=1.8, zorder=7)
    ax.plot([730, 760], [260, 260], color=MAROON, lw=1.8, zorder=7)
    uc(ax, 760, 230, 170, "Student", line_h=14, pad=6, name_size=12)
    t(ax, 628, 190, "If the classroom is closed,", size=11, color=INK, fam=BODY, z=7)
    t(ax, 628, 168, "the students still exist.", size=11, color=INK, fam=BODY, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Aggregation does NOT mean \"the part dies when the whole dies\" — that is composition.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w6_football.png")


# --------------------------------------------------------------------------
# 6. Aggregation with multiplicity
# --------------------------------------------------------------------------
def agg_multiplicity():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Aggregation with Multiplicity", sub="Whole-part relationships still use multiplicity")

    # University 1 ◇ 1..* Department
    uc(ax, 40, 120, 220, "University", line_h=14, pad=6, name_size=12)
    hdiam(ax, 270, 132, 26, 26)
    ax.plot([260, 284], [146, 146], color=MAROON, lw=1.8, zorder=7)
    ax.plot([310, 340], [146, 146], color=MAROON, lw=1.8, zorder=7)
    uc(ax, 340, 120, 220, "Department", line_h=14, pad=6, name_size=12)
    t(ax, 230, 158, "1", size=14, color=MAROON_DARK, fam=H_B, z=7)
    t(ax, 330, 158, "1..*", size=14, color=MAROON_DARK, fam=H_B, z=7)

    box(ax, 60, 40, 500, 60, WHITE, ec=MAROON_SOFT, lw=1.2, r=9, z=6)
    t(ax, 310, 70, "\"One university has one or more departments.\"", size=12, color=INK, fam=B_IT, z=7)

    # second example
    uc(ax, 40, -160, 220, "Department", line_h=14, pad=6, name_size=12)
    # note: clipped below, so draw second example in a lower box instead
    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Department 1 <>-- 0..* Lecturer  —  one department, zero or many lecturers.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w6_agg_multiplicity.png")


# --------------------------------------------------------------------------
# 7. Inheritance overview
# --------------------------------------------------------------------------
def inheritance():
    W, H = 840, 450
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Inheritance", sub="A specific class acquires characteristics and behaviour from a general class")

    uc(ax, 320, 300, 200, "Vehicle", attrs=["registration", "make"], ops=["start()", "stop()"],
       line_h=17, pad=8, name_size=12)
    gtri(ax, 420, 274, 46, 26, ec=MAROON, lw=2.0, z=8)
    ax.plot([420, 420], [300, 226], color=MAROON, lw=2.0, zorder=7)
    ax.plot([420, 190], [226, 170], color=MAROON, lw=2.0, zorder=7)
    ax.plot([420, 650], [226, 170], color=MAROON, lw=2.0, zorder=7)

    uc(ax, 40, 40, 220, "Car", attrs=["numDoors"], ops=["drive()"], line_h=17, pad=8, name_size=11.5)
    uc(ax, 580, 40, 220, "Motorcycle", attrs=["hasSidecar"], ops=["ride()"], line_h=17, pad=8, name_size=11.5)
    t(ax, 150, 155, "inherits", size=10.5, color=MAROON_SOFT, fam=B_IT, z=7)
    t(ax, 690, 155, "inherits", size=10.5, color=MAROON_SOFT, fam=B_IT, z=7)

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "A Car inherits Vehicle's features — in UML the relationship is drawn as generalization.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w6_inheritance.png")


# --------------------------------------------------------------------------
# 8. Generalization vs inheritance
# --------------------------------------------------------------------------
def gen_vs_inheritance():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Generalization vs Inheritance", sub="Same idea, different vocabulary")

    box(ax, 22, 90, 380, 230, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 22, 290, 380, 30, MAROON, r=14, z=7)
    t(ax, 212, 305, "UML TERM", size=12.5, color=WHITE, fam=H_B, z=8)
    t(ax, 212, 250, "GENERALIZATION", size=17, color=MAROON_DARK, fam=H_B, z=7)
    t(ax, 212, 214, "the relationship in the model", size=11.5, color=INK, fam=BODY, z=7)
    t(ax, 212, 190, "drawn as the hollow triangle", size=11.5, color=INK, fam=BODY, z=7)
    t(ax, 212, 130, "Student ---|> User", size=12, color=MAROON_SOFT, fam=MONO, z=7)

    box(ax, 438, 90, 380, 230, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 438, 290, 380, 30, MAROON_DARK, r=14, z=7)
    t(ax, 628, 305, "OOP TERM", size=12.5, color=WHITE, fam=H_B, z=8)
    t(ax, 628, 250, "INHERITANCE", size=17, color=MAROON_DARK, fam=H_B, z=7)
    t(ax, 628, 214, "the implementation mechanism", size=11.5, color=INK, fam=BODY, z=7)
    t(ax, 628, 190, "used in a programming language", size=11.5, color=INK, fam=BODY, z=7)
    t(ax, 628, 130, "class Student extends User", size=12, color=MAROON_SOFT, fam=MONO, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "A UML generalization can be implemented with inheritance in an OO programming language.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w6_gen_vs_inheritance.png")


# --------------------------------------------------------------------------
# 9. What the child inherits
# --------------------------------------------------------------------------
def what_inherited():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "What Does the Child Inherit?", sub="The subclass gains the superclass's features without duplication")

    uc(ax, 60, 300, 220, "Employee",
       attrs=["- employeeID", "- name", "- email"], ops=["+ login()", "+ logout()"],
       line_h=18, pad=9, name_size=12)
    gtri(ax, 300, 274, 40, 24, ec=MAROON, lw=2.0, z=8)
    ax.plot([300, 300], [300, 240], color=MAROON, lw=2.0, zorder=7)
    ax.plot([300, 300], [220, 190], color=MAROON, lw=2.0, zorder=7)
    uc(ax, 170, 60, 260, "Manager",
       attrs=["- department"], ops=["+ approveLeave()"], line_h=18, pad=9, name_size=12)

    # what manager effectively has
    box(ax, 460, 240, 350, 180, MAROON_TINT, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 635, 396, "MANAGER EFFECTIVELY HAS", size=11.5, color=MAROON, fam=H_B, z=7)
    feats = ["employeeID · name · email", "department", "login() · logout()", "approveLeave()"]
    yy = 364
    for f in feats:
        t(ax, 485, yy, f, size=11, color=INK, fam=MONO, ha="left", z=7)
        yy -= 28

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "The Manager does not re-declare employeeID, name, email, login() or logout() — they are inherited.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w6_what_inherited.png")


# --------------------------------------------------------------------------
# 10. Animal hierarchy
# --------------------------------------------------------------------------
def animal():
    W, H = 840, 450
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "An Inheritance Hierarchy — Animals", sub="Common features in Animal · specialised behaviour in each subclass")

    uc(ax, 320, 300, 200, "Animal", attrs=["name", "age"], ops=["eat()"], line_h=17, pad=8, name_size=12)
    gtri(ax, 420, 274, 46, 26, ec=MAROON, lw=2.0, z=8)
    ax.plot([420, 420], [300, 226], color=MAROON, lw=2.0, zorder=7)
    for xb in (160, 420, 680):
        ax.plot([420, xb], [226, 170], color=MAROON, lw=2.0, zorder=7)

    uc(ax, 20, 40, 220, "Dog", ops=["bark()"], line_h=17, pad=8, name_size=11.5)
    uc(ax, 310, 40, 220, "Cat", ops=["meow()"], line_h=17, pad=8, name_size=11.5)
    uc(ax, 600, 40, 220, "Bird", ops=["fly()"], line_h=17, pad=8, name_size=11.5)

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "Dog is an Animal, Cat is an Animal, Bird is an Animal — each adds its own behaviour.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w6_animal.png")


# --------------------------------------------------------------------------
# 11. is-a vs has-a
# --------------------------------------------------------------------------
def isa_hasa():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "IS-A vs HAS-A", sub="Inheritance vs aggregation — a classic exam question")

    box(ax, 22, 110, 380, 260, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 22, 340, 380, 30, MAROON, r=14, z=7)
    t(ax, 212, 355, "IS-A  =  INHERITANCE", size=12.5, color=WHITE, fam=H_B, z=8)
    uc(ax, 130, 240, 170, "Vehicle", line_h=14, pad=6, name_size=11.5)
    gtri(ax, 215, 214, 38, 24, ec=MAROON, lw=2.0, z=8)
    ax.plot([215, 215], [238, 186], color=MAROON, lw=2.0, zorder=7)
    uc(ax, 130, 130, 170, "Car", line_h=14, pad=6, name_size=11.5)
    t(ax, 212, 118, "\"A Car IS a Vehicle\"", size=11.5, color=MAROON_DARK, fam=B_IT, z=7)

    box(ax, 438, 110, 380, 260, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 438, 340, 380, 30, MAROON_DARK, r=14, z=7)
    t(ax, 628, 355, "HAS-A  =  AGGREGATION", size=12.5, color=WHITE, fam=H_B, z=8)
    uc(ax, 480, 190, 150, "Car", line_h=14, pad=6, name_size=11.5)
    hdiam(ax, 640, 206, 26, 26)
    ax.plot([630, 654], [220, 220], color=MAROON, lw=1.8, zorder=7)
    ax.plot([680, 710], [220, 220], color=MAROON, lw=1.8, zorder=7)
    uc(ax, 710, 190, 150, "Engine", line_h=14, pad=6, name_size=11.5)
    t(ax, 628, 150, "\"A Car HAS an Engine\"", size=11.5, color=MAROON_DARK, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Car -> Vehicle (is-a) vs Car <>-- Engine (has-a / part-of) — do not confuse them.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w6_isa_hasa.png")


# --------------------------------------------------------------------------
# 12. Polymorphism — makeSound
# --------------------------------------------------------------------------
def polymorphism():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Polymorphism — \"Many Forms\"", sub="The same request, different behaviour")

    uc(ax, 300, 310, 220, "Animal", ops=["makeSound()"], line_h=17, pad=8, name_size=12)
    gtri(ax, 410, 286, 44, 24, ec=MAROON, lw=2.0, z=8)
    ax.plot([410, 410], [310, 238], color=MAROON, lw=2.0, zorder=7)
    for xb in (150, 410, 670):
        ax.plot([410, xb], [238, 180], color=MAROON, lw=2.0, zorder=7)

    animals = [("Dog", "bark", 40), ("Cat", "meow", 330), ("Cow", "moo", 620)]
    for nm, sound, x in animals:
        uc(ax, x, 60, 170, nm, ops=[f"makeSound()"], line_h=17, pad=8, name_size=11.5)
        box(ax, x + 185, 66, 90, 40, GOLD, r=8, z=7)
        t(ax, x + 230, 86, sound, size=13, color=MAROON_DARK, fam=H_B, z=8)

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "One operation name — makeSound() — with a different implementation for each animal.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w6_polymorphism.png")


# --------------------------------------------------------------------------
# 13. Payment polymorphism
# --------------------------------------------------------------------------
def payment_polymorphism():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Polymorphism in Practice — Payments", sub="One processPayment() request, several implementations")

    uc(ax, 300, 300, 220, "Payment", ops=["processPayment()"], line_h=17, pad=8, name_size=12)
    gtri(ax, 410, 276, 44, 24, ec=MAROON, lw=2.0, z=8)
    ax.plot([410, 410], [300, 228], color=MAROON, lw=2.0, zorder=7)
    for xb in (150, 410, 670):
        ax.plot([410, xb], [228, 170], color=MAROON, lw=2.0, zorder=7)

    pays = [("CardPayment", "charge the card", 30), ("MobileMoney", "mobile wallet", 320), ("BankTransfer", "bank transfer", 610)]
    for nm, how, x in pays:
        uc(ax, x, 50, 190, nm, ops=["processPayment()"], line_h=17, pad=8, name_size=11)
        t(ax, x + 95, 30, how, size=9.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "The system requests processPayment() without treating each payment type as unrelated.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w6_payment_polymorphism.png")


# --------------------------------------------------------------------------
# 14. Notification polymorphism
# --------------------------------------------------------------------------
def notification():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "A Modern Example — Notifications", sub="Email, SMS and Push all implement send() differently")

    uc(ax, 300, 300, 220, "Notification", ops=["send()"], line_h=17, pad=8, name_size=12)
    gtri(ax, 410, 276, 44, 24, ec=MAROON, lw=2.0, z=8)
    ax.plot([410, 410], [300, 228], color=MAROON, lw=2.0, zorder=7)
    for xb in (150, 410, 670):
        ax.plot([410, xb], [228, 170], color=MAROON, lw=2.0, zorder=7)

    notifs = [("EmailNotification", "send an email", 20), ("SMSNotification", "send an SMS", 320), ("PushNotification", "send a push", 600)]
    for nm, how, x in notifs:
        uc(ax, x, 50, 210, nm, ops=["send()"], line_h=17, pad=8, name_size=11)
        t(ax, x + 105, 30, how, size=9.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "Adding WhatsAppNotification later does not change the code that just requests send().",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w6_notification.png")


# --------------------------------------------------------------------------
# 15. Grouping / packages
# --------------------------------------------------------------------------
def grouping():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Grouping — Packages", sub="Organising related classes the way folders organise files")

    def pkg(x, y, w, h, name, items, ec=MAROON):
        box(ax, x, y, w, h, CREAM_2, ec=ec, lw=1.4, r=0, z=5)
        box(ax, x, y + h - 26, 180, 26, ec, r=0, z=6)
        t(ax, x + 12, y + h - 13, name, size=11, color=WHITE, fam=H_SB, ha="left", z=7)
        yy = y + h - 46
        for it in items:
            t(ax, x + 12, yy, it, size=10, color=INK, fam=MONO, ha="left", z=7)
            yy -= 20

    pkg(22, 200, 380, 220, "Student Management", ["Student", "Programme", "Course", "Registration", "Result"])
    pkg(438, 200, 380, 220, "Finance", ["Invoice", "Payment", "Receipt", "Bursary", "Sponsorship"])
    pkg(22, 40, 380, 140, "Human Resources", ["StaffMember", "Payroll", "Leave", "Recruitment"])
    pkg(438, 40, 380, 140, "Library", ["Book", "Loan", "Member", "Reservation"])

    box(ax, 22, 16, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 27, "One giant 60-class diagram is confusing — packages make the model readable and maintainable.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w6_grouping.png")


# --------------------------------------------------------------------------
# 16. Online shopping — all four concepts
# --------------------------------------------------------------------------
def online_shopping():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Complete Example — Online Shopping", sub="Aggregation + inheritance + polymorphism + grouping together")

    # Aggregation/composition: Order ◆ OrderItem
    box(ax, 22, 300, 360, 140, WHITE, ec=MAROON, lw=1.4, r=10, z=6)
    t(ax, 202, 420, "COMPOSITION", size=11, color=MAROON, fam=H_SB, z=7)
    uc(ax, 40, 320, 140, "Order", line_h=13, pad=5, name_size=10.5)
    fdiam(ax, 190, 334, 22, 22)
    ax.plot([180, 202], [345, 345], color=MAROON_DARK, lw=1.6, zorder=7)
    ax.plot([224, 250], [345, 345], color=MAROON_DARK, lw=1.6, zorder=7)
    uc(ax, 250, 320, 140, "OrderItem", line_h=13, pad=5, name_size=10.5)

    # Inheritance: Payment
    box(ax, 438, 260, 380, 180, MAROON_TINT, ec=MAROON, lw=1.4, r=10, z=6)
    t(ax, 628, 420, "INHERITANCE", size=11, color=MAROON, fam=H_SB, z=7)
    uc(ax, 520, 350, 160, "Payment", line_h=13, pad=5, name_size=10.5)
    gtri(ax, 600, 330, 34, 20, ec=MAROON, lw=1.8, z=8)
    ax.plot([600, 600], [350, 302], color=MAROON, lw=1.8, zorder=7)
    for xb in (500, 600, 700):
        ax.plot([600, xb], [302, 272], color=MAROON, lw=1.8, zorder=7)
    uc(ax, 450, 250, 130, "Card\nPayment", line_h=13, pad=5, name_size=10)
    uc(ax, 590, 250, 130, "Mobile\nMoney", line_h=13, pad=5, name_size=10)
    uc(ax, 730, 250, 130, "Bank\nTransfer", line_h=13, pad=5, name_size=10)

    # Polymorphism + grouping notes
    box(ax, 22, 120, 360, 150, WHITE, ec=MAROON, lw=1.4, r=10, z=6)
    t(ax, 202, 246, "POLYMORPHISM", size=11, color=MAROON, fam=H_SB, z=7)
    t(ax, 202, 214, "all payment types support", size=11, color=INK, fam=BODY, z=7)
    t(ax, 202, 192, "processPayment()", size=12, color=MAROON_SOFT, fam=MONO, z=7)
    t(ax, 202, 164, "but each performs it differently.", size=11, color=INK, fam=BODY, z=7)

    box(ax, 438, 120, 380, 150, CREAM_2, ec=MAROON, lw=1.4, r=10, z=6)
    t(ax, 628, 246, "GROUPING", size=11, color=MAROON, fam=H_SB, z=7)
    for i, p in enumerate(["Customer Management", "Order Management", "Product Management", "Payment Management"]):
        t(ax, 628, 210 - i * 20, p, size=10.5, color=INK, fam=MONO, z=7)

    box(ax, 22, 16, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 27, "All four Week 6 concepts work together in a single, realistic model.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w6_online_shopping.png")


ALL = [
    progression, whole_part, agg_vs_assoc, agg_vs_comp, football,
    agg_multiplicity, inheritance, gen_vs_inheritance, what_inherited, animal,
    isa_hasa, polymorphism, payment_polymorphism, notification, grouping,
    online_shopping,
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
    print("Generated", len(made), "week-6 visuals:")
    for m in made:
        print("  -", m)
