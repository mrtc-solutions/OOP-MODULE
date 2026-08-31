"""
Week 6 PDF content — OBJECT-ORIENTED ANALYSIS: OBJECT MODELLING II.
"""
from pdfengine import (H1, H2, P, BUL, FIG, CALLOUT, DTABLE, build, DOC_W,
                      C_MAROON, C_SOFT)

CFG = {
    "week": 6,
    "title": "Object-Oriented Analysis — Object Modelling II",
    "filename": "Week6_Module_BICT3202_OOAD.pdf",
}


def story():
    s = []

    # 1. introduction --------------------------------------------------------
    s.append(H1("1.  Week 6 Introduction"))
    s += [P("Week 5 taught students to identify and model classes, objects, attributes, operations, "
            "links, associations, multiplicity, generalization and specialization. Week 6 builds on those "
            "concepts. The progression is: <b>Week 5</b> — what objects/classes exist, how they are "
            "related, and generalization/specialization; <b>Week 6</b> — how objects form whole-part "
            "structures (aggregation), how characteristics are inherited (inheritance), how different "
            "objects respond differently (polymorphism), and how related classes are organized "
            "(grouping)."),
          P("Aggregation, inheritance and polymorphism are not isolated programming concepts. In OOAD "
            "they help us construct models that represent real systems in a reusable and understandable "
            "way. The formal UML specification defines aggregation as a property of an association end and "
            "distinguishes shared aggregation from composite aggregation.")]
    s += FIG("w6_progression.png", "Figure 1 — Where Week 6 fits in the module")

    # 2. learning outcomes -----------------------------------------------------
    s.append(H1("2.  Learning Outcomes"))
    s += [P("By the end of this week, a student should be able to:")]
    s += BUL([
        "Define aggregation and explain the whole-part relationship.",
        "Distinguish ordinary association, aggregation and composition.",
        "Explain shared aggregation and composite aggregation.",
        "Represent aggregation using UML notation (hollow vs filled diamond).",
        "Explain inheritance and its relationship to UML generalization.",
        "Identify superclass and subclass, and inherited attributes and operations.",
        "Distinguish inheritance (is-a) from association and aggregation (has-a).",
        "Explain polymorphism and method overriding with real-world examples.",
        "Explain why polymorphism supports extensibility.",
        "Explain grouping/classification and organize classes into packages.",
        "Develop a complete class hierarchy and evaluate modelling choices.",
    ])

    # ============ PART A — AGGREGATION ============
    s.append(H1("PART A — AGGREGATION"))
    s.append(H1("3.  What Is Aggregation?"))
    s += [P("What does it mean when one object is made up of, or contains, other objects? Consider a "
            "university: a university has departments, and a department has lecturers, students and "
            "courses. We can represent <font name='Mono'>University ◇──── Department</font> — a "
            "<b>whole-part relationship</b>: the university is the whole, the department is a part. "
            "In simple English: <b>aggregation is a relationship in which one object represents a whole "
            "or collection that is related to other objects representing its parts</b> — a Library "
            "contains Books; a Department has Lecturers.")]
    s += FIG("w6_whole_part.png", "Figure 2 — The whole-part relationship and the hollow diamond")

    s.append(H1("4.  The UML Aggregation Symbol"))
    s += [P("Aggregation is represented with a <b>hollow diamond</b>, placed on the <b>whole</b> side. "
            "This is different from the <b>filled diamond</b> used for composition. The distinction "
            "between aggregation and ordinary association is extremely important: an association is a "
            "general relationship (“a Student is related to a Course”), while aggregation is a "
            "whole-part relationship (“a Department is an aggregate involving Lecturers”).")]
    s += FIG("w6_agg_vs_assoc.png", "Figure 3 — Aggregation vs ordinary association")

    s.append(H1("5.  Aggregation Does NOT Mean \"the Part Dies with the Whole\""))
    s += [P("This is the easiest way to distinguish aggregation from composition. If a Department is "
            "reorganized or removed, does the Lecturer cease to exist? No — the lecturer can be assigned "
            "to another department. A football team consists of players, but if a player leaves the club "
            "the player does not cease to exist; if a classroom is closed, the students still exist. "
            "These are examples of <b>weak/shared</b> whole-part aggregation, where the parts have an "
            "independent existence.")]
    s += FIG("w6_football.png", "Figure 4 — Weak aggregation: parts that outlive the whole")

    s.append(H1("6.  Composition — the Strong Form"))
    s += [P("<b>Composition</b> is a stronger form of whole-part relationship, drawn with a "
            "<b>filled/black diamond</b> (<font name='Mono'>House ◆──── Room</font>). UML identifies "
            "composite aggregation as the form where the composite object has responsibility for the "
            "existence and storage of the composed parts; a part can be included in at most one composite "
            "at a time. If an order is deleted, its order lines normally have no independent meaning — so "
            "<font name='Mono'>Order ◆──── OrderLine</font> is a much stronger relationship than "
            "<font name='Mono'>Team ◇──── Player</font>. The relationship therefore tells us something "
            "about the <b>lifecycle and ownership</b> of objects.")]
    s += FIG("w6_agg_vs_comp.png", "Figure 5 — Aggregation (hollow) vs composition (filled)")

    s.append(H1("7.  Aggregation with Multiplicity — and a Warning"))
    s += [P("Aggregation can also carry multiplicity: "
            "<font name='Mono'>University 1 ◇──── 1..* Department</font> reads “one university has one or "
            "more departments”. But do not assume “contains” automatically means aggregation — “a "
            "customer has an address” does not automatically mean <font name='Mono'>Customer ◇──── "
            "Address</font>. The analyst must understand the domain and lifecycle. <b>The goal is not to "
            "use every possible UML symbol, but to choose the relationship that best represents the "
            "requirements.</b>")]
    s += FIG("w6_agg_multiplicity.png", "Figure 6 — Aggregation with multiplicity")

    # ============ PART B — INHERITANCE ============
    s.append(H1("PART B — INHERITANCE"))
    s.append(H1("8.  What Is Inheritance?"))
    s += [P("<b>Inheritance</b> is a mechanism through which a more specific class can acquire "
            "characteristics and behaviour from a more general class. A Car inherits the characteristics "
            "of Vehicle, and a Motorcycle also inherits them. In UML this relationship is represented "
            "through <b>generalization</b>; the UML specification states that an instance of the specific "
            "classifier is also an instance of the general classifier, and that the specific classifier "
            "inherits features of the general classifier.")]
    s += FIG("w6_inheritance.png", "Figure 7 — Inheritance drawn as UML generalization")

    s.append(H1("9.  Generalization vs Inheritance"))
    s += [P("Students often ask whether generalization and inheritance are the same. They are closely "
            "related, but we should be precise: <b>UML terminology</b> calls the relationship in the model "
            "<b>generalization</b>; <b>object-oriented programming terminology</b> calls the "
            "implementation mechanism <b>inheritance</b>. A UML generalization relationship can be "
            "implemented using inheritance in an object-oriented programming language.")]
    s += FIG("w6_gen_vs_inheritance.png", "Figure 8 — Generalization (UML) vs inheritance (OOP)")

    s.append(H1("10.  What Does the Child Inherit?"))
    s += [P("Suppose Employee has employeeID, name, email, login() and logout(). A Manager with "
            "department and approveLeave() can conceptually have employeeID, name, email, department, "
            "login(), logout() and approveLeave() — without re-declaring the common features. Inheritance "
            "supports <b>reuse</b> (common characteristics defined once), <b>consistency</b> (shared "
            "behaviour managed in one class), <b>specialization</b> (subclasses add their own features), "
            "<b>polymorphism</b> (substitutability) and <b>maintainability</b> (changes managed "
            "centrally).")]
    s += FIG("w6_what_inherited.png", "Figure 9 — What a subclass inherits from its superclass")

    s.append(H1("11.  The Is-A Rule — and Inheritance vs Aggregation"))
    s += [P("Inheritance should generally make sense as an <b>is-a</b> relationship: a Dog is an Animal "
            "(good), a Car is a Vehicle (good), but a Car is an Engine (no) and a Student is a Course "
            "(no). This is one of the most common examination questions: <b>inheritance represents "
            "IS-A</b> (Car ─────▷ Vehicle), while <b>aggregation represents HAS-A / PART-OF</b> "
            "(Car ◇──── Engine).")]
    s += FIG("w6_animal.png", "Figure 10 — An animal hierarchy with specialised behaviour")
    s += FIG("w6_isa_hasa.png", "Figure 11 — IS-A (inheritance) vs HAS-A (aggregation)")

    # ============ PART C — POLYMORPHISM ============
    s.append(H1("PART C — POLYMORPHISM"))
    s.append(H1("12.  What Is Polymorphism?"))
    s += [P("The word polymorphism comes from Greek roots meaning roughly <b>“many forms”</b>. In "
            "object-oriented systems, polymorphism allows the same operation/message to be associated "
            "with different implementations or behaviours depending on the object receiving it. In simple "
            "terms: <b>different objects can respond differently to the same request.</b>"),
          P("Imagine you say “Make a sound!” — a Dog barks, a Cat meows, a Cow moos. The request "
            "<font name='Mono'>makeSound()</font> is conceptually the same, but the behaviour differs. "
            "Likewise, <font name='Mono'>draw()</font> draws a circle for Circle and a rectangle for "
            "Rectangle.")]
    s += FIG("w6_polymorphism.png", "Figure 12 — Polymorphism: one makeSound(), many sounds")

    s.append(H1("13.  Why Is Polymorphism Powerful?"))
    s += [P("Suppose a system must work with different payment types. Payment defines "
            "<font name='Mono'>processPayment()</font>, and CardPayment, MobileMoney and BankTransfer "
            "each implement it differently. The system can issue the general request "
            "<font name='Mono'>processPayment()</font> without treating every payment type as completely "
            "unrelated. A notification system works the same way: EmailNotification, SMSNotification and "
            "PushNotification each implement <font name='Mono'>send()</font> differently. If we later add "
            "WhatsAppNotification, we can add another specialization <b>without changing every part of "
            "the system that simply requests send()</b> — this is <b>extensibility</b>.")]
    s += FIG("w6_payment_polymorphism.png", "Figure 13 — Polymorphism across payment types")
    s += FIG("w6_notification.png", "Figure 14 — Polymorphism across notification channels")

    s.append(H1("14.  Method Overriding — and the Modelling View"))
    s += [P("In programming this idea is commonly implemented through <b>method overriding</b>: the "
            "general class defines <font name='Mono'>makeSound()</font>, and each subclass provides a "
            "specialized version that overrides the inherited operation. In Java: "
            "<font name='Mono'>Animal a = new Dog(); a.makeSound();</font> produces “Bark”, while "
            "<font name='Mono'>a = new Cat(); a.makeSound();</font> produces “Meow” — the variable can "
            "refer to an Animal, but the actual object's implementation determines the behaviour."),
          P("Since this is OOAD, students should first understand the <b>modelling</b> idea without "
            "programming syntax: we simply model Payment with CardPayment, MobileMoney and BankTransfer "
            "all supporting <font name='Mono'>processPayment()</font>, each performing it differently.")]

    # ============ PART D — GROUPING ============
    s.append(H1("PART D — GROUPING"))
    s.append(H1("15.  Grouping — Packages"))
    s += [P("As systems become larger, diagrams become difficult to understand — an enterprise system "
            "with 60 classes in one diagram is confusing. Related elements are therefore organized into "
            "meaningful groups: in UML, <b>packages</b> provide the mechanism. <b>Think of a package as a "
            "folder.</b> A University System folder can contain Student Management, Finance, Human "
            "Resources, Library and Accommodation; Student Management in turn contains Student, "
            "Programme, Course, Registration and Result. Grouping supports organization, readability, "
            "modularity, maintenance, team development, navigation and separation of concerns.")]
    s += FIG("w6_grouping.png", "Figure 15 — Grouping classes into packages")

    # ============ COMPLETE EXAMPLES ============
    s.append(H1("16.  Complete Example — Online Shopping"))
    s += [P("All four concepts come together in an online shopping system. "
            "<b>Composition:</b> Order ◆──── OrderItem — an OrderItem is strongly associated with a "
            "particular Order. <b>Inheritance:</b> Payment is generalized into CardPayment, MobileMoney "
            "and BankTransfer. <b>Polymorphism:</b> all payment types support processPayment() but each "
            "performs it differently. <b>Grouping:</b> the system is organized into Customer Management, "
            "Order Management, Product Management, Payment Management and Delivery Management.")]
    s += FIG("w6_online_shopping.png", "Figure 16 — The four concepts in one model")

    s.append(H1("17.  Complete Example — University System"))
    s += [P("Build a larger model: User ▷ Student and User ▷ Lecturer (inheritance); "
            "<font name='Mono'>Department ◇──── Lecturer</font> (aggregation); "
            "<font name='Mono'>Student ─── Registration ─── Course</font> (association); "
            "<font name='Mono'>Course ◆──── CourseMaterial</font> (composition, if materials are strongly "
            "owned parts). For polymorphism, suppose the university supports different assessment types — "
            "Assessment defines <font name='Mono'>calculateMark()</font>, specialized into Assignment, "
            "Exam, Quiz and Project, each calculating marks differently.")]

    # ============ PRACTICAL / VALIDATION ============
    s.append(H1("18.  Practical Lab and Validation"))
    s += [P("Using a CASE tool, model aggregation and inheritance: draw "
            "<font name='Mono'>University ◇──── Department</font>, "
            "<font name='Mono'>Order ◆──── OrderLine</font>, and the User → Student/Lecturer hierarchy, "
            "then add a polymorphic operation (e.g. calculateMark()). After modelling, evaluate each "
            "decision: is the relationship genuinely whole-part? Is the generalization a genuine is-a? Is "
            "polymorphism justified, or would ordinary classes do?")]
    s.append(CALLOUT("EVALUATING A MODEL — KEY QUESTIONS",
        ["Is the aggregation really whole-part, or just an association?", "Are the parts independent of "
         "the whole (aggregation) or owned by it (composition)?", "Is every generalization a genuine "
         "is-a relationship?", "Does the polymorphic operation have a common meaning across subclasses?",
         "Is the model organised into readable packages?"]))

    # ============ SUMMARY ============
    s.append(H1("19.  Week 6 Summary and Key Terms"))
    s.append(DTABLE(
        ["Term", "Simple meaning"],
        [["Aggregation", "Whole-part relationship; hollow diamond; parts can exist independently."],
         ["Composition", "Strong whole-part; filled diamond; the composite owns its parts."],
         ["Inheritance", "A specific class acquires features from a general class."],
         ["Generalization", "The UML relationship drawn as a hollow triangle."],
         ["Superclass / Subclass", "General class / specialised class."],
         ["Polymorphism", "One operation name, different behaviour per object."],
         ["Method overriding", "A subclass provides its own version of an inherited operation."],
         ["Extensibility", "Adding a new subtype without changing the code that requests the operation."],
         ["Grouping / Package", "Organising related classes the way folders organise files."]],
        widths=[0.34 * DOC_W, 0.66 * DOC_W]))
    s.append(CALLOUT("THE BIG PICTURE",
        ["Week 5 answered <b>what objects exist and how they are related</b>. Week 6 adds the deeper "
         "questions: <b>Is this a whole-part relationship?</b> (aggregation/composition), <b>What "
         "behaviour can be inherited?</b> (inheritance), <b>Can different objects respond differently to "
         "the same operation?</b> (polymorphism), and <b>How can related classes be organised?</b> "
         "(grouping). Together these make the object model reusable, extensible and understandable — "
         "preparing the ground for the dynamic and behavioural modelling of Weeks 7–8."]))

    # ============ EXAM QUESTION ============
    s.append(H1("20.  Examination-Style Question"))
    s += [P("<b>Scenario:</b> An online store has customers, orders, order items and products. Payments "
            "can be made by card, mobile money or bank transfer. Each order contains one or more order "
            "items. The system is organised into customer, order, product and payment management areas."),
          P("<b>Required:</b> (a) draw the classes with a suitable generalization hierarchy for Payment "
            "[8]; (b) model Order and OrderItem, explaining whether aggregation or composition is "
            "appropriate and why [6]; (c) explain how polymorphism applies to processPayment() and why "
            "it supports extensibility [8]; (d) group the classes into packages [4]; (e) justify each "
            "modelling decision [4]. <b>Total: 30 marks.</b>")]

    # ============ REFERENCES ============
    s.append(H1("21.  References and Further Reading"))
    s.append(H2("Primary authoritative reference"))
    s += BUL([
        "Object Management Group. (2017). <i>Unified Modeling Language (UML), Version 2.5.1.</i> OMG — the formal UML specification (aggregation as a property of an association end; shared vs composite aggregation; generalization and feature inheritance).",
        "Object Management Group. <i>UML</i> — the UML specification with machine-readable artefacts, including the UML abstract syntax metamodel.",
    ])
    s.append(H2("Prescribed and recommended texts"))
    s += BUL([
        "Mach, E. (2019). <i>Object Oriented Analysis &amp; Design Cookbook: Introduction to Practical System Modeling.</i>",
        "Reddy, V., &amp; Korra, S. (2018). <i>Object-Oriented Analysis and Design Using UML.</i>",
        "The Art of Service. (2021). <i>Object Oriented Analysis and Design: A Complete Guide.</i>",
        "Wixom, B., &amp; Dennis, A. (2018). <i>Systems Analysis and Design.</i>",
        "Blokdyk, G. (2021). <i>Object-Oriented Analysis and Design Standard Requirements.</i>",
        "Wixom, B., &amp; Dennis, A. (2020). <i>Systems Analysis and Design: An Object-Oriented Approach with UML.</i>",
    ])

    return s


if __name__ == "__main__":
    print("Built:", build(CFG, story))
