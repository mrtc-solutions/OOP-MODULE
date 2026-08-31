"""
Week 4 PPTX content — UML BUILDING BLOCKS, RULES, MECHANISMS AND ARCHITECTURE.
"""
from pptxengine import build

CFG = {
    "week": 4,
    "title": "UML Building Blocks, Rules, Mechanisms and Architecture",
    "filename": "Week4_Presentation_BICT3202_OOAD.pptx",
}


def slides(d):
    # 2. learning outcomes
    s = d.slide()
    d.header(s, "Learning Outcomes", "By the end of this week, you should be able to…")
    d.bullets(s, 0.9, 1.6, 11.6, 5.0, [
        ("Identify ", "the building blocks of UML and their types."),
        ("Explain ", "structural, behavioural, grouping and annotational things."),
        ("Distinguish ", "association, dependency, generalization and realization."),
        ("Explain ", "UML notation, semantics and well-formedness."),
        ("Apply ", "adornments — visibility, multiplicity, constraints and modifiers."),
        ("Use ", "extensibility mechanisms — stereotypes, tagged values, constraints, profiles."),
        ("Explain ", "the layered architecture M0–M3."),
        ("Apply ", "all of it to a university information system."),
    ], size=17, gap=12)
    d.takeaway(s, "Week 4 is the bridge between understanding UML and using it for analysis.")

    # 3. five questions
    s = d.slide()
    d.header(s, "A Simple Way In", "Five questions UML helps you answer")
    d.pic(s, "w4_five_questions.png", y=1.6, w=10.6)
    d.takeaway(s, "What exists? · How are things related? · What can users do? · What happens? · How do objects communicate?")

    # 4. three building blocks
    s = d.slide()
    d.header(s, "The Building Blocks", "Things · Relationships · Diagrams")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Things ", "— structural, behavioural, grouping, annotational."),
        ("Relationships ", "— association, dependency, generalization, realization."),
        ("Diagrams ", "— structural and behavioural views of the model."),
        ("", ""),
        ("Why the classification matters: ", "UML is not a collection of random shapes — every symbol has a defined meaning."),
    ], size=17, gap=14)
    d.takeaway(s, "Building blocks = the vocabulary of UML.")

    # 5. structural things
    s = d.slide()
    d.header(s, "Structural Things", "What exists in the system?")
    d.pic(s, "w4_structural_things.png", y=1.6, w=10.6)
    d.takeaway(s, "Class · Interface · Object · Component · Node — the relatively static parts.")

    # 6. class vs object
    s = d.slide()
    d.header(s, "Class vs Object", "The cake-mould analogy")
    d.pic(s, "w4_class_vs_object.png", y=1.6, w=10.4)
    d.takeaway(s, "A class is a description; an object is a particular instance — student001 : Student.")

    # 7. behavioural / grouping / annotational
    s = d.slide()
    d.header(s, "Behavioural, Grouping & Annotational Things", "What happens · How it's organised · What to note")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Behavioural ", "— interactions (who communicates), activities (workflows), state machines (Draft → Submitted → Approved)."),
        ("Grouping ", "— packages organise a large model (Student Management, Finance, Examination)."),
        ("Annotational ", "— notes explain the model without adding a new business object."),
    ], size=17, gap=14)
    d.takeaway(s, "Not everything in a model is a class — some things happen, group, or explain.")

    # 8. relationships
    s = d.slide()
    d.header(s, "The Four Relationships", "Association · Dependency · Generalization · Realization")
    d.pic(s, "w4_relationships.png", y=1.6, w=10.6)
    d.takeaway(s, "Related-to · Uses · Is-a · Implements — four different arrows, four different meanings.")

    # 9. association as class
    s = d.slide()
    d.header(s, "When a Relationship Needs Its Own Class", "Student — Course → Registration")
    d.pic(s, "w4_association_class.png", y=1.6, w=10.6)
    d.takeaway(s, "If a relationship has data or behaviour (date, status, grade), promote it to a class.")

    # 10. diagrams
    s = d.slide()
    d.header(s, "UML Diagrams", "A diagram is a view of the model — not necessarily the whole system")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Structural diagrams ", "— class, object, component, composite structure, package, deployment → “What exists?”"),
        ("Behavioural diagrams ", "— use case, activity, state machine → “What happens?”"),
        ("Interaction diagrams ", "— sequence, communication, interaction overview, timing → “Who communicates, in what order?”"),
    ], size=17, gap=14)
    d.takeaway(s, "One model supports many views — choose the diagram by the question you ask.")

    # 11. model vs diagram
    s = d.slide()
    d.header(s, "Model vs Diagram", "One model, many diagrams")
    d.pic(s, "w4_model_vs_diagram.png", y=1.6, w=10.4)
    d.takeaway(s, "The diagram shows selected elements; the model holds everything behind them.")

    # 12. rules
    s = d.slide()
    d.header(s, "Rules of UML", "Syntax, semantics and well-formedness")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Syntax ", "— how something is drawn."),
        ("Semantics ", "— what it means; a symbol is not decoration."),
        ("Well-formedness ", "— a model that follows the relevant rules."),
        ("",""),
        ("Never choose a symbol ", "because “it looks nice” — a diamond has a specific meaning."),
    ], size=17, gap=14)
    d.takeaway(s, "Correct notation ≠ correct analysis.")

    # 13. well-formedness
    s = d.slide()
    d.header(s, "Three Ways a Model Can Fail", "Notation · Semantics · Requirements")
    d.pic(s, "w4_wellformed.png", y=1.6, w=10.6)
    d.takeaway(s, "A perfectly drawn diagram can still describe the wrong system.")

    # 14. checklist
    s = d.slide()
    d.header(s, "The Seven-Question Checklist", "Quality-check every UML diagram")
    d.pic(s, "w4_checklist.png", y=1.6, w=10.4)
    d.takeaway(s, "Name · Kind · Meaning · Relationships · Multiplicity · Constraint · Stereotype.")

    # 15. mechanisms overview
    s = d.slide()
    d.header(s, "The Four Common Mechanisms", "Specifications · Adornments · Divisions · Extensibility")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Specifications ", "— the diagram is a view; behind every box lies a richer specification."),
        ("Adornments ", "— visibility, multiplicity, constraints, modifiers added to a basic element."),
        ("Common divisions ", "— class ↔ object (type vs instance); interface ↔ implementation (contract vs behaviour)."),
        ("Extensibility ", "— stereotypes, tagged values, constraints and profiles."),
    ], size=17, gap=14)
    d.takeaway(s, "The classic four mechanisms of Booch, Rumbaugh and Jacobson.")

    # 16. visibility
    s = d.slide()
    d.header(s, "Adornments — Visibility", "Reading the symbols in a class box")
    d.pic(s, "w4_visibility.png", y=1.6, w=10.4)
    d.takeaway(s, "+ public · − private · # protected · ~ package.")

    # 17. stereotypes
    s = d.slide()
    d.header(s, "Extensibility — Stereotypes", "«entity» · «controller» · «boundary»")
    d.pic(s, "w4_stereotypes.png", y=1.6, w=10.6)
    d.takeaway(s, "A stereotype gives an element a specialised meaning.")

    # 18. extensibility comparison
    s = d.slide()
    d.header(s, "Stereotype · Tagged Value · Constraint", "Three extensibility mechanisms compared")
    d.pic(s, "w4_extensibility.png", y=1.6, w=10.6)
    d.takeaway(s, "Specialised meaning · extra metadata · a condition that must hold.")

    # 19. profiles
    s = d.slide()
    d.header(s, "UML Profiles", "Customising UML for a domain")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("UML ", "— a general-purpose modelling language."),
        ("Profile ", "— a tailored UML vocabulary and rules for a domain (security, business process, real-time)."),
        ("Defines ", "stereotypes and their associated extensions."),
        ("",""),
        ("UML 2.5.1 ", "ships with a standard profile as a machine-readable artefact."),
    ], size=17, gap=14)
    d.takeaway(s, "UML = the language · Profile = a customised dialect for a domain.")

    # 20. architecture
    s = d.slide()
    d.header(s, "UML Architecture — M0 to M3", "The meta-modelling hierarchy")
    d.pic(s, "w4_architecture_analogy.png", y=1.55, w=10.6)
    d.takeaway(s, "M3 meta-metamodel (MOF) → M2 metamodel → M1 your model → M0 instances.")

    # 21. architecture vs software architecture
    s = d.slide()
    d.header(s, "Don't Confuse the Two Architectures", "A classic examination trap")
    d.bullets(s, 0.9, 1.6, 5.7, 4.9, [
        ("UML architecture ", "— M3 / M2 / M1 / M0 abstraction levels of the modelling language itself."),
        "","", "Is “Student” M0, M1 or M2? Depends on context:",
        "Student : Class → M1 element", "“Class” as a concept → M2 metamodel", "Francis : Student → M0 instance",
    ], size=16, gap=10)
    d.bullets(s, 6.9, 1.6, 5.4, 4.9, [
        ("Software architecture ", "— Presentation → Business Logic → Data Access → Database."),
        "","", "Completely different concept:",
        "how the system is organised,", "not how the language is defined.",
    ], size=16, gap=10)
    d.takeaway(s, "UML architecture ≠ software architecture — know which one the question asks about.")

    # 22. multiple views
    s = d.slide()
    d.header(s, "One System, Five Views", "The same banking model, different diagrams")
    d.pic(s, "w4_multiview.png", y=1.6, w=10.6)
    d.takeaway(s, "Different diagrams answer different questions — that's why UML suits complex systems.")

    # 23. abstraction
    s = d.slide()
    d.header(s, "UML and Abstraction", "10,000 students → one Student class")
    d.pic(s, "w4_chart_abstraction.png", y=1.6, w=10.4)
    d.takeaway(s, "We model the essential, ignoring the irrelevant — abstraction makes complexity manageable.")

    # 24. packages
    s = d.slide()
    d.header(s, "UML and Complexity Management", "Grouping classes into packages")
    d.pic(s, "w4_chart_packages.png", y=1.6, w=10.4)
    d.takeaway(s, "Don't overload one diagram — split related areas into packages.")

    # 25. generalization mistake
    s = d.slide()
    d.header(s, "Common Mistake — Generalization Direction", "The hollow triangle points to the general class")
    d.pic(s, "w4_generalization_mistake.png", y=1.6, w=10.4)
    d.takeaway(s, "Student ▷ User — triangle at the User end. The most common beginner error.")

    # 26. e-learning case study
    s = d.slide()
    d.header(s, "Case Study — University E-Learning System", "Classes, relationships and the Submission lifecycle")
    d.pic(s, "w4_elearning.png", y=1.6, w=10.6)
    d.takeaway(s, "Student · Lecturer · Course · Assignment · Submission · Grade · LearningMaterial.")

    # 27. summary
    s = d.slide()
    d.header(s, "Week 4 Summary", "The essentials")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Building blocks ", "— things, relationships, diagrams."),
        ("Things ", "— structural, behavioural, grouping, annotational."),
        ("Relationships ", "— association, dependency, generalization, realization."),
        ("Rules ", "— syntax, semantics, well-formedness."),
        ("Mechanisms ", "— specifications, adornments, divisions, extensibility."),
        ("Architecture ", "— M3 → M2 → M1 → M0."),
    ], size=17, gap=13)
    d.takeaway(s, "UML is a language: learn its vocabulary, rules and organisation — then use it.")

    # 28. closing
    d.closing("REVISION & NEXT STEPS", [
        "Study the building blocks and relationship notations — draw each one from memory.",
        "Practice the seven-question checklist on every diagram you create.",
        "Model the university e-learning system: classes, relationships, multiplicity, constraints.",
        "Next week: the object-oriented analysis process — applying everything from Weeks 1–4.",
    ])


def build_pptx():
    return build(CFG, slides)


if __name__ == "__main__":
    print("Built:", build_pptx())
