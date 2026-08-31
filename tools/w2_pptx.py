"""
Week 2 PPTX content — PRINCIPLES OF OBJECT MODELLING.
"""
from pptxengine import (build, CREAM, MAROON, DARK, GOLD_L)

CFG = {
    "week": 2,
    "title": "Principles of Object Modelling",
    "filename": "Week2_Presentation_BICT3202_OOAD.pptx",
}


def slides(d):
    # 2. learning outcomes
    s = d.slide()
    d.header(s, "Learning Outcomes", "By the end of this week, you should be able to…")
    d.bullets(s, 0.9, 1.6, 11.6, 5.0, [
        ("Define object modelling ", "and an object model."),
        ("Explain ", "why object models are useful in analysis."),
        ("Relate ", "object → class → object model."),
        ("Identify objects ", "in a problem domain — and reject irrelevant nouns."),
        ("Identify ", "attributes, behaviours and relationships of objects."),
        ("Explain ", "identity, abstraction and encapsulation in modelling."),
        ("Show how models ", "manage system complexity."),
        ("Build ", "a conceptual object model from a text description."),
    ], size=17, gap=13)
    d.takeaway(s, "Modelling is simplification — keep what matters, hide the rest.")

    # 3. overview / journey
    s = d.slide()
    d.header(s, "From the Real World to Software", "The object model is the bridge")
    d.pic(s, "w2_real_to_software.png", y=1.6, w=10.6)
    d.takeaway(s, "Real world → object model → analysis → design → implementation")

    # 4. definition
    s = d.slide()
    d.header(s, "What Is an Object Model?", "Objects, characteristics, behaviour and relationships")
    d.pic(s, "w2_object_model.png", y=1.65, w=10.4)
    d.takeaway(s, "Student — registers for — Course: a simplified, purposeful picture")

    # 5. principles grid
    s = d.slide()
    d.header(s, "The Nine Principles", "The ideas that guide object thinking")
    d.pic(s, "w2_principles.png", y=1.55, w=10.6)
    d.takeaway(s, "Abstraction · Encapsulation · Identity · State · Behaviour · Relationships · Modularity · Hierarchy · Reuse")

    # 6. abstraction
    s = d.slide()
    d.header(s, "Abstraction Depends on Purpose", "The same Student, modelled three ways")
    d.pic(s, "w2_abstraction.png", y=1.55, w=10.6)
    d.takeaway(s, "Keep only the characteristics the system actually needs.")

    # 7. identity
    s = d.slide()
    d.header(s, "Identity vs Attributes", "Two “Francis” students — different objects")
    d.pic(s, "w2_identity.png", y=1.7, w=10.4)
    d.takeaway(s, "Identity = student ID, account number, UUID or primary key.")

    # 8. state & behaviour & relationships
    s = d.slide()
    d.header(s, "State · Behaviour · Relationships", "What it is, what it does, how it connects")
    d.bullets(s, 0.9, 1.55, 5.6, 4.9, [
        ("State ", "— values describing current condition (Status: Active → Graduated)."),
        ("Behaviour ", "— what it can do (registerCourse(), payFees())."),
        ("Identity ", "— distinguishes it from every other object."),
        ("Relationships ", "— Student—registers for—Course; Customer—owns—Account."),
    ], size=17, gap=14)
    d.bullets(s, 6.9, 1.55, 5.4, 4.9, [
        "Student", "  studentID · name · programme", "  registerCourse() · dropCourse()",
        "", "Course", "  courseCode · courseName · credits", "  checkAvailability()",
    ], size=15, gap=6)
    d.takeaway(s, "An object = identity + state + behaviour, linked to others by relationships.")

    # 9. noun technique
    s = d.slide()
    d.header(s, "Object Identification", "The noun technique — and why nouns are not enough")
    d.bullets(s, 0.9, 1.55, 11.6, 4.9, [
        ("Candidate ≠ final object. ", "Underline nouns, then analyse."),
        "“A student uses a mobile phone to register for a course.” → Student, Course… but Phone?",
        ("Judge, don't just parse grammar: ", "scope, information, behaviour, identity, relationships."),
        "Events can be objects — Payment, Registration, Appointment, Transaction.",
    ], size=17, gap=14)
    d.takeaway(s, "Object identification is analytical reasoning, not noun extraction.")

    # 10. classification
    s = d.slide()
    d.header(s, "Classifying Candidates", "Six families of domain concepts")
    d.pic(s, "w2_classification.png", y=1.65, w=10.8)
    d.takeaway(s, "People · Physical · Places · Events · Documents · Conceptual")

    # 11. decision questions
    s = d.slide()
    d.header(s, "Does It Deserve to Be an Object?", "Seven questions for each candidate")
    d.pic(s, "w2_decision_questions.png", y=1.6, w=10.4)
    d.takeaway(s, "Several “yes” answers = a strong candidate.")

    # 12. object vs attribute
    s = d.slide()
    d.header(s, "Object or Attribute?", "It depends on the requirements")
    d.pic(s, "w2_object_vs_attribute.png", y=1.6, w=10.6)
    d.takeaway(s, "phoneNumber is an attribute — until you must track type, verification and status.")

    # 13. cohesion
    s = d.slide()
    d.header(s, "Cohesion & Coupling", "Keep duties related, dependencies controlled")
    d.pic(s, "w2_cohesion.png", y=1.6, w=10.6)
    d.takeaway(s, "Aim for high cohesion + manageable coupling.")

    # 14. complexity
    s = d.slide()
    d.header(s, "Managing Complexity", "Six techniques for large systems")
    d.pic(s, "w2_complexity.png", y=1.55, w=10.6)
    d.takeaway(s, "Abstraction · Decomposition · Hierarchy · Encapsulation · Modularity · Separation of concerns")

    # 15. poor vs good
    s = d.slide()
    d.header(s, "Poor Model vs Good Model", "Don't build a “God object”")
    d.pic(s, "w2_poor_vs_good.png", y=1.55, w=10.6)
    d.takeaway(s, "Separate Academic, Finance and Examination — one box is not a model.")

    # 16. viewpoints
    s = d.slide()
    d.header(s, "Modelling Viewpoints", "One angle is never enough")
    d.pic(s, "w2_viewpoints.png", y=1.65, w=10.8)
    d.takeaway(s, "Structural · Behavioural · Interaction · Deployment")

    # 17. standards
    s = d.slide()
    d.header(s, "Standards for Modelling", "Why UML — and why standards don't replace thinking")
    d.bullets(s, 0.9, 1.55, 11.6, 4.9, [
        ("UML (Unified Modeling Language) ", "— the OMG standard; current formal spec is UML 2.5.1."),
        "Standard notation gives agreed meaning — no personal drawing styles.",
        ("But correct notation ≠ correct analysis. ", "“Student owns Toilet” is valid UML, meaningless modelling."),
        "Good modelling = understand business + requirements + right concepts + right notation.",
    ], size=17, gap=14)
    d.takeaway(s, "UML is the language; object modelling is the thinking.")

    # 18. mobile money
    s = d.slide()
    d.header(s, "Worked Example — Mobile Money", "From candidates to a first model")
    d.pic(s, "w2_mobile_money.png", y=1.55, w=10.6)
    d.takeaway(s, "Phone → attribute · Money → value · Network → infrastructure · SMS → external")

    # 19. library case study
    s = d.slide()
    d.header(s, "Mini Case Study — Online Library", "Candidate objects and their relationships")
    d.pic(s, "w2_library_model.png", y=1.55, w=10.6)
    d.takeaway(s, "Is “Library” an object? Only if the system manages branches/locations/staff.")

    # 20. checklist
    s = d.slide()
    d.header(s, "The Identification Checklist", "A 10-step process for exam scenarios")
    d.pic(s, "w2_checklist.png", y=1.55, w=10.4)
    d.takeaway(s, "Read → underline nouns → candidates → filter → attributes → behaviour → relationships → verify.")

    # 21. practical & tutorial
    s = d.slide()
    d.header(s, "Practical & Tutorial", "Apply Week 2 to real scenarios")
    d.bullets(s, 0.9, 1.55, 5.9, 4.9, [
        ("Practical — hospital appointments: ", ""),
        "Identify candidates (Patient, Doctor, Appointment, Receptionist, Specialty)",
        "List attributes (patientID, doctorID, appointmentID…)", "List behaviours (request, schedule, cancel…)",
        "List relationships (Patient—requests—Appointment…)", "Justify every decision",
    ], size=16, gap=10)
    d.bullets(s, 7.1, 1.55, 5.3, 4.9, [
        ("Tutorial — “Is it an object?”: ", ""),
        "Student · Name · Course · Mobile Phone · Payment", "Money · University · Registration · Keyboard",
        "Invoice · Lecturer · Internet",
        "Classify each and justify: object / attribute / external / scope-dependent / irrelevant.",
    ], size=16, gap=10)
    d.takeaway(s, "Reasoning matters more than the final label.")

    # 22. summary
    s = d.slide()
    d.header(s, "Week 2 Summary", "The definitions to remember")
    d.bullets(s, 0.9, 1.55, 11.6, 4.9, [
        ("Object modelling ", "— representing a domain with objects, characteristics, behaviour and relationships."),
        ("Abstraction / Encapsulation ", "— keep what matters; protect state behind operations."),
        ("Identity / State / Behaviour ", "— the three parts of every object."),
        ("Object identification ", "— judgement, not noun extraction."),
        ("Complexity ", "— tamed by decomposition, modularity, hierarchy and separation of concerns."),
        ("UML ", "— the standard language (2.5.1) we start in Week 3."),
    ], size=16, gap=12)
    d.takeaway(s, "Problem domain → candidate concepts → relevant objects → attributes → behaviour → relationships → model.")

    # 23. closing
    d.closing("REVISION & NEXT STEPS", [
        "Attempt the revision and examination-style questions in the Week 2 module and the assignment.",
        "Identify 15 candidate objects for a system you use daily — then filter them.",
        "Practise the 10-step identification checklist on a past-paper scenario.",
        "Next week: UML — the standard language for expressing the models we build.",
    ])


def build_pptx():
    return build(CFG, slides)


if __name__ == "__main__":
    print("Built:", build_pptx())
