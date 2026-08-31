"""
Week 3 PPTX content — MODELLING LANGUAGE: UML.
"""
from pptxengine import build

CFG = {
    "week": 3,
    "title": "Modelling Language — UML",
    "filename": "Week3_Presentation_BICT3202_OOAD.pptx",
}


def slides(d):
    # 2. learning outcomes
    s = d.slide()
    d.header(s, "Learning Outcomes", "By the end of this week, you should be able to…")
    d.bullets(s, 0.9, 1.6, 11.6, 5.0, [
        ("Define UML ", "and explain why it is used in OOAD."),
        ("Separate ", "modelling language vs development methodology."),
        ("Identify ", "the building blocks — things, relationships, diagrams."),
        ("Classify ", "structural, behavioural, grouping and annotational elements."),
        ("Explain ", "the diagram families and their purposes."),
        ("Apply ", "rules, common mechanisms and extensibility (stereotypes, tagged values, constraints)."),
        ("Explain ", "the four-layer architecture M0–M3."),
    ], size=17, gap=13)
    d.takeaway(s, "UML is a standard language for communicating models — not a programming language.")

    # 3. what is UML
    s = d.slide()
    d.header(s, "What Is UML?", "Unified · Modeling · Language")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Unified ", "— brought together ideas from earlier OO modelling approaches."),
        ("Modeling ", "— used to create representations of systems."),
        ("Language ", "— defined concepts and notation for communicating those representations."),
        ("The problem it solves: ", "five people, five different mental pictures — UML makes the structure visible."),
        ("Current specification: ", "UML 2.5.1 (OMG, December 2017)."),
    ], size=17, gap=14)
    d.takeaway(s, "UML = visualise, specify and document systems — structure, behaviour and processes.")

    # 4. what UML is not
    s = d.slide()
    d.header(s, "What UML Is NOT", "Three distinctions that examiners love")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Not a programming language ", "— Java/Python/C# execute; UML communicates models."),
        ("Not a methodology ", "— UML says how to represent; UP/USDP says what activities to do, in what order."),
        ("Not only for software ", "— business processes, workflows and non-software systems too."),
        ("One diagram ≠ everything ", "— use multiple views for different perspectives."),
    ], size=17, gap=14)
    d.takeaway(s, "UML = modelling language · UP = development process (Weeks 12–13).")

    # 5. three building blocks
    s = d.slide()
    d.header(s, "The Three Building Blocks", "Things · Relationships · Diagrams")
    d.pic(s, "w3_three_blocks.png", y=1.6, w=10.6)
    d.takeaway(s, "The classic framework of Booch, Rumbaugh and Jacobson.")

    # 6. things
    s = d.slide()
    d.header(s, "Building Block 1 — Things", "Structural · Behavioural · Grouping · Annotational")
    d.pic(s, "w3_things.png", y=1.6, w=10.6)
    d.takeaway(s, "What exists? · What happens? · How is it organised? · What else to note?")

    # 7. class example
    s = d.slide()
    d.header(s, "A UML Class", "Three compartments with adornments")
    d.pic(s, "w3_class_example.png", y=1.55, w=10.4)
    d.takeaway(s, "Name · Attributes · Operations  —  with − private / + public adornments")

    # 8. interface
    s = d.slide()
    d.header(s, "Interface & Realization", "A contract, fulfilled by different implementations")
    d.pic(s, "w3_interface.png", y=1.65, w=10.6)
    d.takeaway(s, "The user of an interface need not know the internal implementation.")

    # 9. relationships
    s = d.slide()
    d.header(s, "Building Block 2 — Relationships", "Association · Dependency · Generalization · Realization")
    d.pic(s, "w3_relationships.png", y=1.55, w=10.4)
    d.takeaway(s, "Generalization → hollow triangle · Realization → dashed hollow triangle · Dependency → dashed arrow")

    # 10. multiplicity
    s = d.slide()
    d.header(s, "Multiplicity", "How many instances participate?")
    d.pic(s, "w3_multiplicity.png", y=1.6, w=10.6)
    d.takeaway(s, "Student 1 ——— 0..* Course  ·  one student, zero or many courses")

    # 11. diagram map
    s = d.slide()
    d.header(s, "Building Block 3 — Diagrams", "The UML diagram families")
    d.pic(s, "w3_diagram_map.png", y=1.55, w=10.4)
    d.takeaway(s, "Structural (6) · Behavioural (3) · Interaction (4) — per OMG UML 2.5.1")

    # 12. use case
    s = d.slide()
    d.header(s, "Use-Case Diagram", "What should users be able to accomplish?")
    d.pic(s, "w3_use_case.png", y=1.65, w=10.4)
    d.takeaway(s, "Captures functionality from the user's perspective — Week 9 in depth.")

    # 13. sequence
    s = d.slide()
    d.header(s, "Sequence Diagram", "Who communicates with whom, in what order?")
    d.pic(s, "w3_sequence.png", y=1.6, w=10.4)
    d.takeaway(s, "Lifelines + messages; vertical axis = time.")

    # 14. activity
    s = d.slide()
    d.header(s, "Activity Diagram", "Modelling the workflow")
    d.pic(s, "w3_activity.png", y=1.55, w=10.6)
    d.takeaway(s, "Actions, decisions and start/end nodes — Week 11 in depth.")

    # 15. state machine
    s = d.slide()
    d.header(s, "State Machine Diagram", "How an object changes state")
    d.pic(s, "w3_state_machine.png", y=1.7, w=10.6)
    d.takeaway(s, "Events drive transitions: submit → approve → complete. Weeks 7–8 in depth.")

    # 16. component + deployment
    s = d.slide()
    d.header(s, "Component & Deployment Diagrams", "Software parts and where they run")
    d.pic(s, "w3_component.png", x=0.35, y=1.6, w=6.3)
    d.pic(s, "w3_deployment.png", x=6.85, y=1.7, w=6.1)
    d.takeaway(s, "Components = design/architecture · Nodes = servers, devices, execution environments")

    # 17. package
    s = d.slide()
    d.header(s, "Packages", "Grouping elements to manage large models")
    d.pic(s, "w3_package.png", y=1.6, w=10.4)
    d.takeaway(s, "Packages connect directly to Week 2's complexity management.")

    # 18. rules
    s = d.slide()
    d.header(s, "Rules of UML", "Syntax, semantics and well-formedness")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Syntax ", "— how something is drawn."),
        ("Semantics ", "— what it means."),
        ("Well-formedness ", "— satisfies the rules of the language."),
        ("Four checks: ", "notation correct? relationship sensible? requirements met? understandable?"),
        ("A diagram can look right ", "and still mean the wrong thing."),
    ], size=17, gap=14)
    d.takeaway(s, "Correct notation ≠ correct analysis.")

    # 19. mechanisms
    s = d.slide()
    d.header(s, "The Four Common Mechanisms", "Specifications · Adornments · Divisions · Extensibility")
    d.pic(s, "w3_mechanisms.png", y=1.65, w=10.8)
    d.takeaway(s, "Stereotypes «entity» · Tagged values {location=…} · Constraints {balance ≥ 0}")

    # 20. architecture
    s = d.slide()
    d.header(s, "The Four-Layer Architecture", "M3 → M2 → M1 → M0")
    d.pic(s, "w3_architecture.png", y=1.55, w=10.4)
    d.takeaway(s, "Meta-metamodel (MOF) → Metamodel → Your model → Instances")

    # 21. architecture vs software architecture
    s = d.slide()
    d.header(s, "Don't Confuse the Two Architectures", "A classic examination trap")
    d.bullets(s, 0.9, 1.6, 5.6, 4.9, [
        ("UML architecture ", "— M3 / M2 / M1 / M0 abstraction levels of the modelling language itself."),
        "", "", "A dictionary analogy:", "M3 rules for languages, M2 definitions (Class…), M1 your model, M0 actual instances.",
    ], size=16, gap=10)
    d.bullets(s, 6.9, 1.6, 5.4, 4.9, [
        ("Software architecture ", "— Presentation → Business Logic → Data Access → Database."),
        "", "", "Completely different concept:", "how the system is organised, not how the language is defined.",
    ], size=16, gap=10)
    d.takeaway(s, "UML architecture ≠ software architecture — know which one the question asks about.")

    # 22. worked example
    s = d.slide()
    d.header(s, "One System, Five Views", "The university registration requirement")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Use case ", "— Student · Register Course (what users can do)"),
        ("Class ", "— Student, Course + attributes (structure)"),
        ("Sequence ", "— Student → System → Course (interaction)"),
        ("Activity ", "— login → select → check → register (workflow)"),
        ("State ", "— Draft → Submitted → Approved → Completed (lifecycle)"),
    ], size=17, gap=13)
    d.takeaway(s, "Different diagrams answer different questions — that's why UML is powerful.")

    # 23. practical & tutorial
    s = d.slide()
    d.header(s, "Practical & Tutorial", "Try UML yourself")
    d.bullets(s, 0.9, 1.6, 5.9, 4.9, [
        ("Practical — build a class diagram: ", ""),
        "Student · Course · Lecturer · Registration",
        "Add attributes (studentID, courseCode, lecturerID, registrationID…)",
        "Add relationships (Student—Registration, Lecturer—Course…)",
        "Add multiplicities (Student 1 — 0..* Registration)",
    ], size=16, gap=10)
    d.bullets(s, 7.1, 1.6, 5.3, 4.9, [
        ("Tutorial — which diagram? ", ""),
        "Functions a student can do → Use Case", "Classes & relationships → Class",
        "Communication order → Sequence", "Steps of a process → Activity",
        "States of an application → State Machine", "Where components run → Deployment",
    ], size=16, gap=10)
    d.takeaway(s, "Choose the diagram by the question you are trying to answer.")

    # 24. summary
    s = d.slide()
    d.header(s, "Week 3 Summary", "The essentials")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("UML ", "— a standardised language for visualising, specifying and documenting systems."),
        ("Building blocks ", "— Things · Relationships · Diagrams."),
        ("Relationships ", "— association, dependency, generalization, realization."),
        ("Rules ", "— syntax, semantics, well-formedness."),
        ("Mechanisms ", "— specifications, adornments, divisions, extensibility."),
        ("Architecture ", "— M3 meta-metamodel → M2 metamodel → M1 model → M0 instances."),
    ], size=16, gap=12)
    d.takeaway(s, "UML is not pretty pictures — it's a language for communicating models.")

    # 25. closing
    d.closing("REVISION & NEXT STEPS", [
        "Study the OMG UML 2.5.1 specification — the authoritative reference.",
        "Build a table of 10+ diagram types: what each represents, the question it answers, when it is useful.",
        "Map the Week 1–2 registration system onto the right diagrams (requirements, structure, workflow, interaction, lifecycle, deployment).",
        "Next week: deeper into UML building blocks, rules, mechanisms and architecture.",
    ])


def build_pptx():
    return build(CFG, slides)


if __name__ == "__main__":
    print("Built:", build_pptx())
