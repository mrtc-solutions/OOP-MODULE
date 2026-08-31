"""
Week 5 PPTX content — OBJECT-ORIENTED ANALYSIS: OBJECT MODELLING I.
"""
from pptxengine import build

CFG = {
    "week": 5,
    "title": "Object-Oriented Analysis — Object Modelling I",
    "filename": "Week5_Presentation_BICT3202_OOAD.pptx",
}


def slides(d):
    # 2. learning outcomes
    s = d.slide()
    d.header(s, "Learning Outcomes", "By the end of this week, you should be able to…")
    d.bullets(s, 0.9, 1.6, 11.6, 5.0, [
        ("Explain ", "object-oriented analysis."),
        ("Distinguish ", "object vs class, and link vs association."),
        ("Identify ", "candidate objects/classes and filter irrelevant nouns."),
        ("Identify ", "attributes and operations/responsibilities."),
        ("Draw ", "a UML class and object diagram with correct notation."),
        ("Apply ", "association names, roles and multiplicity."),
        ("Explain ", "generalization and specialization, and draw them."),
        ("Use ", "a CASE tool to build a basic class diagram — and evaluate it."),
    ], size=17, gap=12)
    d.takeaway(s, "Week 5 is where we start doing real Object-Oriented Analysis.")

    # 3. transition
    s = d.slide()
    d.header(s, "The Transition", "From knowing UML to doing analysis")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Weeks 1–4 ", "built the foundation: needs, OO principles, UML, UML mechanics."),
        ("Now: ", "\u201cGiven a real-world problem, I can identify objects/classes and their relationships.\u201d"),
        ("Week 5 — Object Modelling I: ", "object/class · notation · links & association · generalization/specialization · CASE tool."),
        ("Week 6 — Object Modelling II: ", "aggregation · inheritance · polymorphism · grouping."),
    ], size=17, gap=14)
    d.takeaway(s, "Analysis first — identify and represent the objects before anything else.")

    # 4. what is OOA
    s = d.slide()
    d.header(s, "What Is Object-Oriented Analysis?", "Studying the problem domain")
    d.pic(s, "w5_ooa_whatis.png", y=1.6, w=10.6)
    d.takeaway(s, "OOA examines the domain as objects, classes, responsibilities, relationships and behaviour.")

    # 5. key question
    s = d.slide()
    d.header(s, "The Key Question", "\u201cWhat important things exist in this problem domain?\u201d")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Banking: ", "Customer · Account · Transaction · Bank · Loan · Card"),
        ("Hospital: ", "Patient · Doctor · Nurse · Appointment · Prescription · MedicalRecord"),
        ("Online university: ", "Student · Lecturer · Course · Assignment · Submission · Grade"),
        ("",""),
        ("These become ", "candidate classes — but not every noun is a class."),
    ], size=17, gap=14)
    d.takeaway(s, "Identify the important objects first, then ask how they are related.")

    # 6. class vs object
    s = d.slide()
    d.header(s, "Class vs Object", "Description vs particular instance")
    d.pic(s, "w5_class_vs_object.png", y=1.6, w=10.6)
    d.takeaway(s, "Car = class · Toyota Corolla ABC123 = object · Student = class · Francis : Student = object")

    # 7. UML class notation
    s = d.slide()
    d.header(s, "UML Class Notation", "Three compartments: name · attributes · operations")
    d.pic(s, "w5_uml_class_notation.png", y=1.6, w=10.6)
    d.takeaway(s, "visibility name : type  —  e.g.  - studentID : String")

    # 8. attributes vs operations
    s = d.slide()
    d.header(s, "Attributes vs Operations", "Information vs behaviour")
    d.pic(s, "w5_attr_vs_op.png", y=1.6, w=10.4)
    d.takeaway(s, "Memory trick: attributes = information · operations = behaviour")

    # 9. object notation
    s = d.slide()
    d.header(s, "Object Notation", "Underlined name + attribute values")
    d.pic(s, "w5_object_notation.png", y=1.6, w=10.4)
    d.takeaway(s, "A class describes structure; an object shows a specific instance and its values.")

    # 10. process
    s = d.slide()
    d.header(s, "The Object Modelling Process", "A beginner-friendly workflow")
    d.pic(s, "w5_process.png", y=1.6, w=10.6)
    d.takeaway(s, "Do not just underline every noun — validate each step against the requirements.")

    # 11. noun technique
    s = d.slide()
    d.header(s, "Identifying Candidate Classes", "The noun technique — with a warning")
    d.pic(s, "w5_noun_technique.png", y=1.6, w=10.6)
    d.takeaway(s, "\u201cMonday\u201d is a value of a date, not a class the system models.")

    # 12. links and associations
    s = d.slide()
    d.header(s, "Links and Associations", "Class level vs object level")
    d.pic(s, "w5_link_vs_association.png", y=1.6, w=10.6)
    d.takeaway(s, "Association connects classes · Link connects objects — a key distinction.")

    # 13. naming and roles
    s = d.slide()
    d.header(s, "Naming an Association & Roles", "Give relationships meaning")
    d.pic(s, "w5_association_naming.png", y=1.6, w=10.4)
    d.takeaway(s, "Student — registers for — Course · roles: student / registeredCourse")

    # 14. multiplicity
    s = d.slide()
    d.header(s, "Multiplicity", "How many instances can participate?")
    d.pic(s, "w5_multiplicity.png", y=1.6, w=10.4)
    d.takeaway(s, "Student 1 — 0..* Course: one student, zero or many courses.")

    # 15. common multiplicities
    s = d.slide()
    d.header(s, "Common Multiplicities", "1 · 0..1 · * · 0..* · 1..* · 2..5")
    d.pic(s, "w5_chart_multiplicity.png", y=1.6, w=10.6)
    d.takeaway(s, "0..* allows zero · 1..* requires at least one.")

    # 16. cardinality
    s = d.slide()
    d.header(s, "One-to-One · One-to-Many · Many-to-Many", "Three relationship shapes")
    d.pic(s, "w5_cardinality.png", y=1.6, w=10.6)
    d.takeaway(s, "Many-to-many often hides data (date, status, grade) — a Registration class may be needed.")

    # 17. generalization
    s = d.slide()
    d.header(s, "Generalization", "The \u201cis-a\u201d relationship")
    d.pic(s, "w5_generalization.png", y=1.6, w=10.6)
    d.takeaway(s, "A Student is a User — the general class holds the shared features.")

    # 18. generalization vs association
    s = d.slide()
    d.header(s, "Generalization vs Association", "Do not confuse them")
    d.pic(s, "w5_gen_vs_assoc.png", y=1.6, w=10.4)
    d.takeaway(s, "is-a (generalization) vs related-to (association) — check the is-a test first.")

    # 19. is-a / has-a
    s = d.slide()
    d.header(s, "The \u201cIs-A\u201d and \u201cHas-A\u201d Tests", "Two questions that prevent most mistakes")
    d.pic(s, "w5_isa_hasa.png", y=1.6, w=10.6)
    d.takeaway(s, "\u201cIs a Student a Course?\u201d No — use an association, not generalization.")

    # 20. complete example
    s = d.slide()
    d.header(s, "A Complete Class Example", "User · Student · Lecturer")
    d.pic(s, "w5_complete_example.png", y=1.6, w=10.6)
    d.takeaway(s, "Common features live in User; each subclass adds its own attributes and operations.")

    # 21. specialization & vocabulary
    s = d.slide()
    d.header(s, "Specialization & Vocabulary", "Opposite perspectives, same structure")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Generalization ", "— bottom-up: \u201cCar is generalized into Vehicle.\u201d"),
        ("Specialization ", "— top-down: \u201cVehicle is specialized into Car.\u201d"),
        ("Superclass / parent / generalized class ", "= the general class (User)."),
        ("Subclass / child / derived class ", "= the specialized class (Student)."),
    ], size=17, gap=14)
    d.takeaway(s, "Same diagram, two viewpoints — know the vocabulary for the exam.")

    # 22. CASE tools
    s = d.slide()
    d.header(s, "CASE Tools", "Computer-Aided Software Engineering")
    d.pic(s, "w5_case_tools.png", y=1.6, w=10.6)
    d.takeaway(s, "The analyst decides; the tool represents and manages — it does not think for you.")

    # 23. practical lab
    s = d.slide()
    d.header(s, "Practical Lab — Your First Class Diagram", "Student · Course · Lecturer · Registration")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Create ", "the four classes with attributes and operations."),
        ("Add associations: ", "Student — makes — Registration · Registration — is for — Course · Lecturer — teaches — Course."),
        ("Add multiplicities: ", "Student 1 — 0..* Registration · Course 1 — 0..* Registration · Lecturer 1 — 0..* Course."),
        ("Add generalization: ", "User ▷ Student · User ▷ Lecturer, then move shared attributes up."),
    ], size=17, gap=13)
    d.takeaway(s, "Document your assumptions — multiplicity depends on the real requirements.")

    # 24. validation
    s = d.slide()
    d.header(s, "Validating a Class Diagram", "Review before you submit")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Purpose ", "— does every class earn its place?"),
        ("Placement ", "— does every attribute belong to the right class?"),
        ("Meaningful operations ", "— no random methods to fill the box."),
        ("Correct relationships ", "— and multiplicities supported by requirements."),
        ("Genuine is-a ", "— is each generalization a real is-a relationship?"),
        ("Readable ", "— can someone else understand it?"),
    ], size=17, gap=13)
    d.takeaway(s, "A diagram is a communication tool — review it the way an examiner would.")

    # 25. common mistakes
    s = d.slide()
    d.header(s, "Common Student Mistakes", "Avoid these five")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Confusing ", "class and object — \u201cJohn is the Student class\u201d is wrong."),
        ("Generalization everywhere ", "— Student ▷ Course is wrong; a student is not a course."),
        ("Forgetting multiplicities ", "— requirements need to know \u201chow many?\u201d"),
        ("Every noun a class ", "— filter, don't just underline."),
        ("Random operations ", "— eat(), sleep(), walk() are not system responsibilities."),
    ], size=16, gap=12)
    d.takeaway(s, "Analysis level: model registerCourse() — leave public void syntax for design.")

    # 26. summary
    s = d.slide()
    d.header(s, "Week 5 Summary", "The essentials")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("OOA ", "— study the domain as objects, classes, responsibilities, relationships, behaviour."),
        ("Class / Object ", "— description vs particular instance."),
        ("Attributes / Operations ", "— information vs behaviour."),
        ("Link / Association ", "— object-level vs class-level connection."),
        ("Multiplicity ", "— how many instances participate."),
        ("Generalization / Specialization ", "— is-a, general-to-specific."),
        ("CASE tool ", "— assists modelling, never replaces analysis."),
    ], size=16, gap=12)
    d.takeaway(s, "OOA is understanding the domain, not just drawing boxes.")

    # 27. closing
    d.closing("REVISION & NEXT STEPS", [
        "Practise the noun technique, then apply the is-a / has-a tests to every candidate class.",
        "Draw the hospital and library models with attributes, operations, associations and multiplicities.",
        "Use your CASE tool to build the registration model from the practical lab.",
        "Next week: Object Modelling II — aggregation, inheritance, polymorphism and grouping.",
    ])


def build_pptx():
    return build(CFG, slides)


if __name__ == "__main__":
    print("Built:", build_pptx())
