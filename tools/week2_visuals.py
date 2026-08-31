"""
Week 2 visuals — Principles of Object Modelling.
"""
import os
import numpy as np
import matplotlib.pyplot as plt

from common import (MAROON, MAROON_DARK, MAROON_SOFT, MAROON_TINT, GOLD,
                    GOLD_LIGHT, CREAM, CREAM_2, INK, GREY, GREY_LIGHT, WHITE,
                    CHART_COLORS)
from draw import (canvas, box, chev, t, arrow, title, save, H_XB, H_B, H_SB,
                  H_MD, BODY, B_SB, B_B, B_IT, MONO, SYM)


# 1. Real world -> object model -> software
def real_to_software():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "From the Real World to Working Software",
          sub="The object model is the bridge between the problem domain and the solution")

    steps = [
        ("REAL WORLD", "the university — people, processes,\nrules, resources", MAROON, WHITE),
        ("OBJECT MODEL", "Student · Course · Lecturer\nRegistration · Payment", MAROON_DARK, WHITE),
        ("DETAILED ANALYSIS", "attributes · relationships\nbehaviour · rules", "#8C2B2D", WHITE),
        ("DESIGN", "classes · interfaces\ncomponents · database", GOLD, MAROON_DARK),
        ("IMPLEMENTATION", "working software\n(Java / C# / Python …)", MAROON_SOFT, WHITE),
    ]
    cw, ch = 150, 120
    x = 18
    for i, (head, body, col, tcol) in enumerate(steps):
        box(ax, x, 120, cw, ch, col, r=14, z=6)
        t(ax, x + cw / 2, 120 + ch - 34, head, size=12.5, color=tcol, fam=H_SB, z=8)
        t(ax, x + cw / 2, 120 + ch / 2 - 8, body, size=10.5, color=tcol, fam=BODY, z=8, ls=1.3)
        if i < 4:
            arrow(ax, x + cw + 2, 180, x + cw + 20, 180, color=MAROON, lw=2.4)

    box(ax, 20, 14, 800, 40, MAROON_TINT, r=14, z=5)
    t(ax, W / 2, 34, "The model hides irrelevant detail and keeps only what the system needs to know.",
      size=12.5, color=MAROON, fam=B_SB)

    # side captions
    t(ax, 20, 266, "identification", size=11, color=GREY, fam=B_IT, ha="left")
    arrow(ax, 90, 262, 90, 248, color=GOLD, lw=2.0)
    t(ax, 178, 266, "modelling", size=11, color=GREY, fam=B_IT, ha="left")
    arrow(ax, 245, 262, 245, 248, color=GOLD, lw=2.0)
    t(ax, 336, 266, "analysis", size=11, color=GREY, fam=B_IT, ha="left")
    arrow(ax, 402, 262, 402, 248, color=GOLD, lw=2.0)
    t(ax, 494, 266, "design", size=11, color=GREY, fam=B_IT, ha="left")
    arrow(ax, 560, 262, 560, 248, color=GOLD, lw=2.0)
    return save(fig, "w2_real_to_software.png")


# 2. A first object model (Student — Course)
def object_model():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "A First Object Model",
          sub="An object model shows objects, their characteristics and their relationships")

    def class_box(x, y, name, attrs, w=250, h=150):
        box(ax, x, y, w, h, WHITE, ec=MAROON, lw=1.8, r=12, z=6)
        box(ax, x, y + h - 32, w, 32, MAROON, r=10, z=6)
        t(ax, x + w / 2, y + h - 16, name, size=14, color=WHITE, fam=H_SB, z=7)
        for i, a in enumerate(attrs):
            t(ax, x + 18, y + h - 56 - i * 24, a, size=11.5, color=INK, fam=MONO, ha="left", z=7)

    class_box(70, 90, "Student", ["studentID", "name", "programme"])
    class_box(520, 90, "Course", ["courseCode", "courseName", "credits"])
    arrow(ax, 330, 165, 508, 165, color=MAROON, lw=2.8, ms=22)
    t(ax, 419, 192, "registers for", size=13, color=MAROON, fam=B_SB, z=8)

    box(ax, 20, 12, 800, 30, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 27, "Student  ———  registers for  ———  Course      (a simplified picture, not the whole university)",
      size=12, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w2_object_model.png")


# 3. Abstraction depends on purpose
def abstraction():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Abstraction Depends on Purpose",
          sub="The same real-world Student is modelled differently for different systems")

    box(ax, 40, 130, 190, 210, WHITE, ec=GOLD, lw=2, r=14, z=6)
    t(ax, 135, 306, "STUDENT", size=15, color=MAROON, fam=H_B, z=7)
    t(ax, 135, 278, "the real person —\nhundreds of characteristics\n(height, hobbies, shoes,\nfood, family, socials …)", size=11, color=GREY, fam=BODY, z=7, ls=1.3)
    t(ax, 135, 168, "only what matters\nis kept", size=10.5, color=MAROON_SOFT, fam=B_IT, z=7)

    panels = [
        ("Registration System", ["studentID", "name", "programme", "year"], MAROON),
        ("Hostel System", ["studentID", "name", "roomNumber", "hostel", "checkInDate"], MAROON_DARK),
        ("Medical System", ["studentID", "name", "medicalRecordNo", "allergies", "emergencyContact"], "#8C2B2D"),
    ]
    ys = [300, 160, 20]
    for (h, attrs, col), y in zip(panels, ys):
        box(ax, 270, y, 540, 118, WHITE, ec=col, lw=1.8, r=14, z=6)
        box(ax, 270, y + 84, 540, 34, col, r=10, z=6)
        t(ax, 540, y + 101, h, size=13, color=WHITE, fam=H_SB, z=7)
        t(ax, 540, y + 46, "  ".join(attrs), size=12, color=INK, fam=MONO, z=7)
        arrow(ax, 238, 230, 262, y + 60, color=col, lw=2.2)

    return save(fig, "w2_abstraction.png")


# 4. The nine principles grid
def principles():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Principles of Object Modelling",
          sub="Nine ideas that guide how we think about objects")

    items = [
        ("A", "Abstraction", "focus on what matters", MAROON),
        ("E", "Encapsulation", "data + behaviour together, access controlled", MAROON_DARK),
        ("I", "Identity", "one object distinguishable from another", "#8C2B2D"),
        ("S", "State", "what is true about it now", MAROON_SOFT),
        ("B", "Behaviour", "what it can do / how it responds", MAROON),
        ("R", "Relationships", "how objects connect and interact", GOLD),
        ("M", "Modularity", "divide the system into parts", MAROON_DARK),
        ("H", "Hierarchy", "general → specialised levels", "#8C2B2D"),
        ("U", "Reuse", "share common characteristics", MAROON_SOFT),
    ]
    cw, ch, gx, gy = 250, 120, 14, 14
    for i, (glyph, name, desc, col) in enumerate(items):
        r, c = divmod(i, 3)
        x = 22 + c * (cw + gx)
        y = 40 + (2 - r) * (ch + gy)
        box(ax, x, y, cw, ch, WHITE, ec=col, lw=1.8, r=14, z=6)
        box(ax, x + 14, y + ch - 46, 40, 40, col, r=10, z=7)
        t(ax, x + 34, y + ch - 26, glyph, size=17, color=(MAROON_DARK if col == GOLD else WHITE), fam=H_B, z=8)
        t(ax, x + 66, y + ch - 20, name, size=13.5, color=col if col != GOLD else MAROON_DARK, fam=H_B, ha="left", z=7)
        t(ax, x + 14, y + 34, desc, size=10.5, color=INK, fam=BODY, ha="left", z=7)
    return save(fig, "w2_principles.png")


# 5. Identity vs attributes
def identity():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Identity vs Attributes",
          sub="Two objects can share the same attribute values — identity still separates them")

    def card(x, idv, name, highlight):
        box(ax, x, 60, 250, 200, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
        box(ax, x, 226, 250, 34, MAROON, r=10, z=6)
        t(ax, x + 125, 243, "Student object", size=12, color=WHITE, fam=H_SB, z=7)
        box(ax, x + 16, 166, 218, 46, highlight, r=10, z=7)
        t(ax, x + 125, 189, "ID: " + idv, size=13, color=WHITE if highlight != GOLD_LIGHT else MAROON_DARK, fam=MONO, z=8)
        t(ax, x + 125, 130, "Name: " + name, size=12, color=INK, fam=BODY, z=7)
        t(ax, x + 125, 100, "Programme: BSc ICT", size=12, color=INK, fam=BODY, z=7)

    card(90, "ST001", "Francis", MAROON)
    card(500, "ST002", "Francis", GOLD)
    t(ax, W / 2, 330, "Same name — different objects", size=14, color=MAROON, fam=B_SB, z=7)
    t(ax, 90 + 125, 48, "identity = ST001", size=10.5, color=GREY, fam=B_IT, z=7)
    t(ax, 500 + 125, 48, "identity = ST002", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 20, 12, 800, 30, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 27, "Identity may be a student ID, account number, UUID or database primary key.",
      size=12, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w2_identity.png")


# 6. Candidate object classification
def classification():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "How Do We Classify Candidate Objects?",
          sub="Six common families of domain concepts")

    cards = [
        ("1", "People", "Student · Lecturer\nCustomer · Doctor", MAROON),
        ("2", "Physical things", "Book · Vehicle\nATM · Computer", MAROON_DARK),
        ("3", "Places", "Branch · Department\nClassroom · Warehouse", "#8C2B2D"),
        ("4", "Events", "Registration · Payment\nAppointment · Transaction", MAROON_SOFT),
        ("5", "Documents", "Invoice · Receipt\nApplication · Certificate", GOLD),
        ("6", "Conceptual", "Account · Course\nProgramme · Policy", MAROON),
    ]
    cw, ch, g = 250, 150, 14
    for i, (num, name, ex, col) in enumerate(cards):
        r, c = divmod(i, 3)
        x = 22 + c * (cw + g)
        y = 30 + (1 - r) * (ch + g)
        box(ax, x, y, cw, ch, WHITE, ec=col, lw=1.8, r=14, z=6)
        box(ax, x + 14, y + ch - 40, 34, 30, col, r=10, z=7)
        t(ax, x + 31, y + ch - 25, num, size=13, color=(MAROON_DARK if col == GOLD else WHITE), fam=H_B, z=8)
        t(ax, x + 60, y + ch - 24, name, size=13.5, color=col if col != GOLD else MAROON_DARK, fam=H_B, ha="left", z=7)
        t(ax, x + 14, y + 42, ex, size=11.5, color=INK, fam=MONO, ha="left", z=7, ls=1.35)
    return save(fig, "w2_classification.png")


# 7. Object vs attribute
def object_vs_attribute():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Object or Attribute?",
          sub="The same concept can be an attribute in one system and an object in another")

    # left: phone as attribute
    box(ax, 20, 40, 380, 230, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 20, 236, 380, 34, MAROON, r=10, z=6)
    t(ax, 210, 253, "Simple system — attribute", size=12.5, color=WHITE, fam=H_SB, z=7)
    box(ax, 40, 90, 150, 120, MAROON_TINT, ec=MAROON, lw=1.4, r=10, z=6)
    t(ax, 115, 186, "Student", size=12.5, color=MAROON, fam=H_SB, z=7)
    t(ax, 115, 150, "name", size=11, color=INK, fam=MONO, z=7)
    t(ax, 115, 124, "phoneNumber", size=11, color=MAROON_DARK, fam=MONO, z=7)
    t(ax, 115, 98, "email", size=11, color=INK, fam=MONO, z=7)
    t(ax, 250, 130, "phoneNumber is just\nan attribute:\n+265 99 000 0000", size=11, color=GREY, fam=BODY, ha="left", z=7, ls=1.3)

    # right: phone as object
    box(ax, 440, 40, 380, 230, WHITE, ec=MAROON_DARK, lw=1.8, r=14, z=6)
    box(ax, 440, 236, 380, 34, MAROON_DARK, r=10, z=6)
    t(ax, 630, 253, "Rich system — separate object", size=12.5, color=WHITE, fam=H_SB, z=7)
    box(ax, 460, 90, 150, 120, MAROON_TINT, ec=MAROON, lw=1.4, r=10, z=6)
    t(ax, 535, 186, "Student", size=12.5, color=MAROON, fam=H_SB, z=7)
    t(ax, 535, 150, "studentID", size=11, color=INK, fam=MONO, z=7)
    t(ax, 535, 124, "name", size=11, color=INK, fam=MONO, z=7)
    box(ax, 650, 90, 150, 120, CREAM_2, ec=GOLD, lw=1.6, r=10, z=6)
    t(ax, 725, 186, "Phone", size=12.5, color=MAROON_DARK, fam=H_SB, z=7)
    t(ax, 725, 150, "number", size=11, color=INK, fam=MONO, z=7)
    t(ax, 725, 124, "type", size=11, color=INK, fam=MONO, z=7)
    t(ax, 725, 98, "verified · status", size=11, color=INK, fam=MONO, z=7)
    arrow(ax, 610, 150, 650, 150, color=MAROON, lw=2.2)
    t(ax, 630, 178, "has", size=11, color=MAROON, fam=B_SB, z=7)

    box(ax, 20, 10, 800, 26, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 23, "Decision depends on requirements — analyse significance and behaviour, don't guess.",
      size=12, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w2_object_vs_attribute.png")


# 8. Decision questions
def decision_questions():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Does This Concept Deserve to Be an Object?",
          sub="Seven questions to test a candidate object")

    qs = [
        "Does it have information the system must remember?",
        "Does it have meaningful behaviour?",
        "Does it have a distinct identity?",
        "Does it participate in important relationships?",
        "Does the business care about it?",
        "Does the system create, modify, retrieve or track it?",
        "Is it within the scope of the system?",
    ]
    for i, q in enumerate(qs):
        y = 60 + (6 - i) * 46
        box(ax, 40, y, 760, 40, WHITE, ec=MAROON, lw=1.4, r=10, z=6)
        box(ax, 48, y + 8, 24, 24, MAROON, r=8, z=7)
        t(ax, 60, y + 20, f"{i+1}", size=11, color=WHITE, fam=H_B, z=8)
        t(ax, 92, y + 20, q, size=13, color=INK, fam=BODY, ha="left", z=7)

    box(ax, 40, 12, 760, 34, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 29, "Several “yes” answers = a strong candidate object.", size=13, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w2_decision_questions.png")


# 9. Cohesion
def cohesion():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Cohesion — Keep Responsibilities Related",
          sub="Poor cohesion mixes unrelated duties; good cohesion stays focused")

    box(ax, 20, 60, 380, 230, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 20, 256, 380, 34, MAROON, r=10, z=6)
    t(ax, 210, 273, "POOR COHESION", size=12.5, color=WHITE, fam=H_SB, z=7)
    t(ax, 210, 214, "Student", size=13, color=MAROON, fam=H_SB, z=7)
    bad = ["registerCourse()", "viewResults()", "payFees()", "repairComputer()", "cookFood()", "manageNetwork()"]
    for i, m in enumerate(bad):
        col = MAROON_SOFT if i < 3 else GOLD
        t(ax, 210, 184 - i * 22, m, size=11.5, color=(MAROON_DARK if col == GOLD else INK), fam=MONO, z=7)

    box(ax, 440, 60, 380, 230, WHITE, ec=GOLD, lw=2, r=14, z=6)
    box(ax, 440, 256, 380, 34, MAROON_DARK, r=10, z=6)
    t(ax, 630, 273, "GOOD COHESION", size=12.5, color=WHITE, fam=H_SB, z=7)
    t(ax, 630, 214, "Student", size=13, color=MAROON_DARK, fam=H_SB, z=7)
    good = ["registerCourse()", "dropCourse()", "viewResults()", "updateProfile()"]
    for i, m in enumerate(good):
        t(ax, 630, 184 - i * 22, m, size=11.5, color=MAROON, fam=MONO, z=7)
    t(ax, 630, 80, "closely related duties", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 20, 12, 800, 32, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 28, "Aim for high cohesion + manageable coupling — vital in object-oriented design.",
      size=13, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w2_cohesion.png")


# 10. Managing complexity — six techniques
def complexity():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Managing Complexity", sub="Six techniques that keep large systems understandable")

    cards = [
        ("Abstraction", "keep only relevant detail", "Student, Course, Registration — not the whole campus"),
        ("Decomposition", "break the system into parts", "Registration · Finance · Exams · Library"),
        ("Hierarchy", "general → specialised levels", "Person → Student / Employee"),
        ("Encapsulation", "hide internal details", "deposit() / withdraw() hide balance logic"),
        ("Modularity", "separate responsibilities", "Auth · Registration · Finance · Reporting"),
        ("Separation of concerns", "no “God object”", "one class ≠ register + salary + SMS + library"),
    ]
    cw, ch, g = 260, 140, 12
    for i, (name, sub, ex) in enumerate(cards):
        r, c = divmod(i, 3)
        x = 22 + c * (cw + g)
        y = 30 + (1 - r) * (ch + g)
        col = CHART_COLORS[i % len(CHART_COLORS)]
        box(ax, x, y, cw, ch, WHITE, ec=col, lw=1.8, r=14, z=6)
        box(ax, x, y + ch - 40, cw, 40, col, r=10, z=6)
        t(ax, x + cw / 2, y + ch - 20, name, size=13, color=WHITE if col != GOLD_LIGHT else MAROON_DARK, fam=H_SB, z=7)
        t(ax, x + cw / 2, y + ch - 62, sub, size=11, color=col, fam=B_B, z=7)
        t(ax, x + cw / 2, y + 32, ex, size=10, color=GREY, fam=BODY, z=7, ls=1.25)
    return save(fig, "w2_complexity.png")


# 11. Poor model vs good model
def poor_vs_good():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Poor Model vs Good Model", sub="Everything in one box is not a model — separation is")

    # poor
    box(ax, 30, 60, 360, 250, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 30, 276, 360, 34, MAROON, r=10, z=6)
    t(ax, 210, 293, "POOR MODEL", size=12.5, color=WHITE, fam=H_SB, z=7)
    t(ax, 210, 240, "UniversitySystem", size=13, color=MAROON, fam=H_SB, z=7)
    t(ax, 210, 200, "Student · Course · Payment\nLibrary · Hostel · Transport\nPayroll · Cafeteria · Security", size=11.5, color=INK, fam=MONO, z=7, ls=1.4)
    t(ax, 210, 108, "everythingElse()", size=11.5, color=MAROON_SOFT, fam=MONO, z=7)
    t(ax, 210, 78, "one giant “God” component", size=10.5, color=GREY, fam=B_IT, z=7)

    # good tree
    box(ax, 470, 276, 340, 40, MAROON, r=12, z=6)
    t(ax, 640, 296, "University", size=13, color=WHITE, fam=H_SB, z=7)
    subs = [("Academic", "Student · Course · Registration", 450), ("Finance", "Payment · Invoice", 585), ("Examination", "Exam · Result", 720)]
    for name, items, x in subs:
        box(ax, x, 150, 150, 90, WHITE, ec=MAROON, lw=1.6, r=10, z=6)
        t(ax, x + 75, 214, name, size=12, color=MAROON, fam=H_SB, z=7)
        t(ax, x + 75, 180, items, size=10.5, color=INK, fam=MONO, z=7, ls=1.3)
        arrow(ax, 640, 276, x + 75, 246, color=MAROON, lw=2.0)
    t(ax, 640, 130, "clear separation of concerns", size=10.5, color=GREY, fam=B_IT, z=7)

    return save(fig, "w2_poor_vs_good.png")


# 12. Modelling viewpoints
def viewpoints():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Modelling Viewpoints", sub="One model is not enough — we view a system from several angles")

    cards = [
        ("Structural view", "What things exist?", "Student · Course · Lecturer", MAROON),
        ("Behavioural view", "What happens?", "student registers\nlecturer approves", MAROON_DARK),
        ("Interaction view", "How do objects talk?", "Student → System → Course", "#8C2B2D"),
        ("Deployment view", "Where does it run?", "App → API server → Database", GOLD),
    ]
    cw, ch, g = 190, 200, 12
    x = 22
    for (name, q, ex, col), x in zip(cards, [22, 226, 430, 634]):
        box(ax, x, 30, cw, ch, WHITE, ec=col, lw=1.8, r=14, z=6)
        box(ax, x, 186, cw, 44, col, r=10, z=6)
        t(ax, x + cw / 2, 208, name, size=12.5, color=(MAROON_DARK if col == GOLD else WHITE), fam=H_SB, z=7)
        t(ax, x + cw / 2, 160, q, size=12, color=col, fam=B_B, z=7)
        t(ax, x + cw / 2, 88, ex, size=11, color=INK, fam=MONO, z=7, ls=1.35)

    box(ax, 22, 10, 796, 24, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 22, "UML supports structure, behaviour and design — not one forced diagram.", size=11.5,
      color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w2_viewpoints.png")


# 13. Mobile money worked example
def mobile_money():
    W, H = 840, 460
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Worked Example — Mobile Money",
          sub="From the business domain to candidate objects and a first model")

    t(ax, 30, 392, "Candidate objects", size=13, color=MAROON, fam=B_SB, ha="left")
    cands = ["Customer", "Wallet", "Transaction", "Agent", "Merchant", "Bill"]
    for i, cname in enumerate(cands):
        x = 30 + i * 130
        box(ax, x, 330, 118, 48, WHITE, ec=MAROON, lw=1.6, r=10, z=6)
        t(ax, x + 59, 354, cname, size=12, color=MAROON, fam=H_SB, z=7)

    # mini model
    def mini(x, y, name, attrs, beh):
        box(ax, x, y, 170, 120, WHITE, ec=MAROON, lw=1.6, r=10, z=6)
        box(ax, x, y + 90, 170, 30, MAROON, r=8, z=6)
        t(ax, x + 85, y + 105, name, size=11.5, color=WHITE, fam=H_SB, z=7)
        t(ax, x + 85, y + 64, attrs, size=9.5, color=INK, fam=MONO, z=7, ls=1.3)
        t(ax, x + 85, y + 22, beh, size=9.5, color=MAROON_SOFT, fam=MONO, z=7, ls=1.3)

    mini(50, 40, "Customer", "customerID\nname · phone", "register()\nsendMoney()")
    mini(330, 40, "Wallet", "walletID\nbalance · status", "deposit()\nwithdraw()")
    mini(610, 40, "Transaction", "transactionID\namount · type", "process()\nreverse()")
    arrow(ax, 228, 100, 322, 100, color=MAROON, lw=2.4)
    t(ax, 275, 126, "owns", size=10.5, color=MAROON, fam=B_SB)
    arrow(ax, 508, 100, 602, 100, color=MAROON, lw=2.4)
    t(ax, 555, 126, "records", size=10.5, color=MAROON, fam=B_SB)

    box(ax, 30, 8, 780, 24, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 20, "Phone → attribute · Money → value · Network → infrastructure · SMS → external service",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w2_mobile_money.png")


# 14. Library mini case study
def library_model():
    W, H = 840, 460
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Mini Case Study — Online Library",
          sub="Candidate objects, attributes, behaviour and relationships")

    def class_box(x, y, name, attrs, beh, w=190, h=150):
        box(ax, x, y, w, h, WHITE, ec=MAROON, lw=1.6, r=12, z=6)
        box(ax, x, y + h - 30, w, 30, MAROON, r=8, z=6)
        t(ax, x + w / 2, y + h - 15, name, size=12.5, color=WHITE, fam=H_SB, z=7)
        for i, a in enumerate(attrs):
            t(ax, x + 14, y + h - 50 - i * 20, a, size=10, color=INK, fam=MONO, ha="left", z=7)
        ax.plot([x + 8, x + w - 8], [y + 74 - 20 * len(attrs), y + 74 - 20 * len(attrs)], color=GOLD, lw=1.0, zorder=7)
        yy = y + 58 - 20 * len(attrs)
        for i, b in enumerate(beh):
            t(ax, x + 14, yy - i * 20, b, size=10, color=MAROON_SOFT, fam=MONO, ha="left", z=7)

    class_box(40, 40, "Student", ["studentID", "name", "programme"], ["searchBook()", "borrowBook()", "returnBook()"], h=180)
    class_box(315, 190, "Loan", ["loanID", "borrowDate", "dueDate", "status"], ["createLoan()", "closeLoan()", "calculateFine()"])
    class_box(590, 190, "Book", ["ISBN", "title", "author", "availability"], ["checkAvailability()"], h=150)
    class_box(315, 30, "Librarian", ["staffID", "name"], ["addBook()", "removeBook()", "updateBook()"], h=150)

    arrow(ax, 230, 130, 307, 250, color=MAROON, lw=2.2)
    t(ax, 238, 205, "makes", size=10.5, color=MAROON, fam=B_SB)
    arrow(ax, 512, 265, 582, 265, color=MAROON, lw=2.2)
    t(ax, 547, 288, "concerns", size=10.5, color=MAROON, fam=B_SB)
    arrow(ax, 505, 200, 582, 200, color=GOLD, lw=2.0)
    t(ax, 543, 224, "manages", size=10.5, color=MAROON_SOFT, fam=B_SB)

    box(ax, 40, 8, 780, 24, MAROON_DARK, r=13, z=5)
    t(ax, W / 2, 20, "Is “Library” itself an object? Only if the system manages branches, locations or staff.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w2_library_model.png")


# 15. Identification checklist (10 steps)
def checklist():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Object-Identification Checklist",
          sub="A 10-step process for examination scenarios")

    steps = [
        "Read the scenario carefully",
        "Underline important nouns",
        "List candidate objects",
        "Remove irrelevant concepts",
        "Combine duplicate concepts",
        "Identify attributes",
        "Identify behaviours",
        "Identify relationships",
        "Check each object has a reason to exist",
        "Check the model against the requirements",
    ]
    left = [steps[i] for i in range(0, 10, 2)]
    right = [steps[i] for i in range(1, 10, 2)]
    for i, s in enumerate(left):
        n = 2 * i + 1
        y = 380 - i * 68
        box(ax, 40, y - 22, 380, 56, WHITE, ec=MAROON, lw=1.6, r=12, z=6)
        box(ax, 52, y - 2, 30, 30, MAROON, r=8, z=7)
        t(ax, 67, y + 13, str(n), size=12, color=WHITE, fam=H_B, z=8)
        t(ax, 100, y + 6, s, size=12.5, color=INK, fam=BODY, ha="left", z=7)
        if i < 4:
            arrow(ax, 67, y - 24, 67, y - 42, color=GOLD, lw=2.0)
    for i, s in enumerate(right):
        n = 2 * i + 2
        y = 380 - i * 68
        box(ax, 440, y - 22, 360, 56, WHITE, ec=MAROON_DARK, lw=1.6, r=12, z=6)
        box(ax, 452, y - 2, 30, 30, MAROON_DARK, r=8, z=7)
        t(ax, 467, y + 13, str(n), size=12, color=WHITE, fam=H_B, z=8)
        t(ax, 500, y + 6, s, size=12.5, color=INK, fam=BODY, ha="left", z=7)
        if i < 4:
            arrow(ax, 467, y - 24, 467, y - 42, color=GOLD, lw=2.0)
    return save(fig, "w2_checklist.png")


# 16. Chart: interaction growth
def chart_interactions():
    W, H = 840, 420
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Why Complexity Must Be Managed",
          sub="Possible pairwise interactions grow quickly as classes are added (illustrative)")

    n = np.arange(2, 21)
    pairs = n * (n - 1) / 2

    plot = fig.add_axes([0.14, 0.24, 0.72, 0.55])
    plot.plot(n, pairs, color=MAROON, lw=3, marker="o", ms=5, zorder=3)
    plot.fill_between(n, pairs, color=MAROON_TINT, zorder=2)
    plot.set_xticks(np.arange(2, 21, 2))
    plot.set_xticklabels([str(int(x)) for x in np.arange(2, 21, 2)], fontsize=11,
                         family="Open Sans", color=INK)
    plot.set_yticks(np.arange(0, 201, 50))
    plot.set_yticklabels([str(int(y)) for y in np.arange(0, 201, 50)], fontsize=11,
                         family="Open Sans", color=INK)
    plot.set_xlabel("Number of classes", fontsize=12, family="Open Sans", color=INK)
    plot.set_ylabel("Possible pairwise links", fontsize=12, family="Open Sans", color=INK)
    for s in ("top", "right"):
        plot.spines[s].set_visible(False)
    plot.spines["left"].set_color(GREY)
    plot.spines["bottom"].set_color(GREY)
    plot.grid(axis="y", color=GREY_LIGHT, lw=0.7, zorder=1)

    plot.annotate("10 classes → 45 links", xy=(10, 45), xytext=(12.2, 85),
                  fontsize=11.5, family="Open Sans", color=MAROON,
                  arrowprops=dict(arrowstyle="->", color=MAROON, lw=1.4))
    plot.annotate("20 classes → 190 links", xy=(20, 190), xytext=(13.2, 165),
                  fontsize=11.5, family="Open Sans", color=MAROON_SOFT,
                  arrowprops=dict(arrowstyle="->", color=MAROON_SOFT, lw=1.4))

    fig.text(0.5, 0.09, "Illustrative — shows why abstraction, decomposition and modularity are essential.",
             ha="center", va="center", fontsize=11, family="Open Sans", fontstyle="italic", color=GREY)
    return save(fig, "w2_chart_interactions.png")


ALL = [
    real_to_software, object_model, abstraction, principles, identity,
    classification, object_vs_attribute, decision_questions, cohesion,
    complexity, poor_vs_good, viewpoints, mobile_money, library_model,
    checklist, chart_interactions,
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
    print("Generated", len(made), "week-2 visuals:")
    for m in made:
        print("  -", m)
