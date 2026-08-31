"""
Week 13 PPTX content — MULTILAYER SYSTEMS, REUSABLE COMPONENTS AND ARCHITECTURAL DESIGN.
"""
from pptxengine import build

CFG = {
    "week": 13,
    "title": "Multilayer Systems, Reusable Components and Architectural Design",
    "filename": "Week13_Presentation_BICT3202_OOAD.pptx",
}


def slides(d):
    # 2. learning outcomes
    s = d.slide()
    d.header(s, "Learning Outcomes", "By the end of this week, you should be able to…")
    d.bullets(s, 0.9, 1.6, 11.6, 5.0, [
        ("Explain ", "software architecture and distinguish it from class design."),
        ("Explain ", "multilayer architecture and identify common layers."),
        ("Explain ", "separation of concerns, cohesion and coupling."),
        ("Define ", "a software component and explain component interfaces."),
        ("Explain ", "reusable and adaptable components."),
        ("Draw ", "a basic UML component diagram and explain packages."),
        ("Evaluate ", "the benefits and limitations of multilayer architecture."),
    ], size=16, gap=11)
    d.takeaway(s, "Organise the software so it is easier to maintain, reuse, replace and adapt.")

    # 3. progression
    s = d.slide()
    d.header(s, "Where Week 13 Fits", "From classes to architecture")
    d.pic(s, "w13_progression.png", y=1.6, w=10.6)
    d.takeaway(s, "Not just \u201cwhat objects do we need?\u201d but \u201chow should they be organised?\u201d")

    # 4. architecture vs class
    s = d.slide()
    d.header(s, "Architecture vs Class Design", "Architecture is broader")
    d.pic(s, "w13_architecture_vs_class.png", y=1.6, w=10.6)
    d.takeaway(s, "Class design = what classes; architecture = how they are organised.")

    # 5. layers
    s = d.slide()
    d.header(s, "Basic Multilayer Architecture", "Five logical levels")
    d.pic(s, "w13_layers.png", y=1.5, w=10.4)
    d.takeaway(s, "Presentation → Application → Domain → Data Access → Database.")

    # 6. presentation layer
    s = d.slide()
    d.header(s, "The Presentation Layer", "User interaction only")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Handles: ", "displaying information, collecting input, basic formatting, sending requests, showing responses."),
        ("Does not normally hold ", "all the business rules."),
        ("Why: ", "web, Android, iOS and desktop would each duplicate the same logic."),
    ], size=16, gap=13)
    d.takeaway(s, "One rule change should not mean changing several applications.")

    # 7. domain rules
    s = d.slide()
    d.header(s, "The Domain Layer", "Business rules in one place")
    d.pic(s, "w13_domain_rules.png", y=1.6, w=10.6)
    d.takeaway(s, "max 6 → max 8 courses: centralised = one change; duplicated = four changes.")

    # 8. data access
    s = d.slide()
    d.header(s, "The Data Access Layer", "Route database access through repositories")
    d.pic(s, "w13_data_access.png", y=1.6, w=10.6)
    d.takeaway(s, "Changing database technology then affects far fewer classes.")

    # 9. separation
    s = d.slide()
    d.header(s, "Separation of Concerns", "Different parts, different responsibilities")
    d.pic(s, "w13_separation.png", y=1.6, w=10.6)
    d.takeaway(s, "One huge class is hard to test, modify, reuse and understand.")

    # 10. cohesion
    s = d.slide()
    d.header(s, "Cohesion", "Keep related responsibilities together")
    d.pic(s, "w13_cohesion.png", y=1.6, w=10.6)
    d.takeaway(s, "A good class has a clear reason for existing.")

    # 11. coupling
    s = d.slide()
    d.header(s, "Coupling", "Avoid unnecessary dependencies")
    d.pic(s, "w13_coupling.png", y=1.6, w=10.6)
    d.takeaway(s, "High cohesion + appropriately low coupling.")

    # 12. component vs class
    s = d.slide()
    d.header(s, "Component vs Class", "A component is a larger modular unit")
    d.pic(s, "w13_component_vs_class.png", y=1.6, w=10.6)
    d.takeaway(s, "The engine is a component, but it contains many parts.")

    # 13. component interfaces
    s = d.slide()
    d.header(s, "Component Interfaces", "Communicate through defined contracts")
    d.pic(s, "w13_component_interfaces.png", y=1.6, w=10.6)
    d.takeaway(s, "Replace one payment implementation without rewriting every client.")

    # 14. reuse
    s = d.slide()
    d.header(s, "Reusable Components", "One authentication component, many apps")
    d.pic(s, "w13_reuse.png", y=1.6, w=10.6)
    d.takeaway(s, "Reuse reduces effort and duplication — when the component is well designed.")

    # 15. adaptability
    s = d.slide()
    d.header(s, "Adaptable Components", "Configure or extend, don't hard-code")
    d.pic(s, "w13_adaptability.png", y=1.6, w=10.6)
    d.takeaway(s, "NotificationService with Email, SMS and Push adapts without a redesign.")

    # 16. reuse vs inheritance
    s = d.slide()
    d.header(s, "Reuse vs Inheritance", "Inheritance is not always the best reuse")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Inheritance = ", "an IS-A relationship (Administrator IS-A User)."),
        ("Not: ", "RegistrationService IS-A Database."),
        ("Composition = ", "RegistrationService USES NotificationService."),
        ("Other reuse: ", "composition, interfaces, services, libraries, frameworks, configurable components."),
    ], size=17, gap=13)
    d.takeaway(s, "Reuse does not automatically require inheritance.")

    # 17. component diagram
    s = d.slide()
    d.header(s, "UML Component Diagram", "Organisation and relationships of components")
    d.pic(s, "w13_component_diagram.png", y=1.5, w=10.4)
    d.takeaway(s, "One of UML's structural diagram types.")

    # 18. packages
    s = d.slide()
    d.header(s, "Packages", "Package = organisation · Component = functionality")
    d.pic(s, "w13_packages.png", y=1.5, w=10.6)
    d.takeaway(s, "A package is a namespace; a component encapsulates functionality behind interfaces.")

    # 19. dependency direction
    s = d.slide()
    d.header(s, "Dependency Direction", "Control the direction of dependencies")
    d.pic(s, "w13_dependency_direction.png", y=1.6, w=10.6)
    d.takeaway(s, "Presentation → Application → Domain → Infrastructure — not everything ↔ everything.")

    # 20. benefits
    s = d.slide()
    d.header(s, "Why Multilayer Architecture Matters", "Five practical benefits")
    d.pic(s, "w13_benefits.png", y=1.6, w=10.6)
    d.takeaway(s, "Maintainability · reuse · testability · adaptability · team development.")

    # 21. limitations
    s = d.slide()
    d.header(s, "Limitations of Multilayer Architecture", "More layers is not always better")
    d.pic(s, "w13_limitations.png", y=1.6, w=10.6)
    d.takeaway(s, "Architecture should match the problem — not be a ritual.")

    # 22. deployment
    s = d.slide()
    d.header(s, "Deployment Thinking", "Logical = how it is organised · deployment = where it runs")
    d.pic(s, "w13_deployment.png", y=1.6, w=10.6)
    d.takeaway(s, "A deployment diagram shows software artifacts on nodes at runtime.")

    # 23. reusability principles
    s = d.slide()
    d.header(s, "Reusability Design Principles", "Four principles + a warning")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Clear interfaces ", "— interact through a well-defined contract."),
        ("Minimise dependencies ", "— don't couple to one application."),
        ("Encapsulation ", "— expose processPayment(), hide the internals."),
        ("Configuration ", "— channel = SMS instead of hard-coding SMS."),
        ("Warning: ", "design for appropriate reuse, not reuse at any cost."),
    ], size=16, gap=13)
    d.takeaway(s, "Don't spend three weeks turning a SmallCalculator into a framework.")

    # 24. confusions
    s = d.slide()
    d.header(s, "Common Confusions", "Don't mix these up")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Layer vs component: ", "a level vs a modular unit."),
        ("Component vs class: ", "larger unit vs finer building block."),
        ("Package vs layer: ", "namespace vs responsibility-based separation."),
        ("Reuse vs inheritance: ", "reuse does not require inheritance."),
        ("Cohesion vs coupling: ", "keep related things together; keep dependencies apart."),
    ], size=16, gap=12)
    d.takeaway(s, "Five classic traps in examination answers.")

    # 25. summary
    s = d.slide()
    d.header(s, "Week 13 Summary", "The core message")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("1. ", "Divide responsibilities into logical layers."),
        ("2. ", "Keep related responsibilities together (high cohesion)."),
        ("3. ", "Avoid unnecessary dependencies (low coupling)."),
        ("4. ", "Build components with clear interfaces."),
        ("5. ", "Design for appropriate reuse and adaptability — and let architecture match the problem."),
    ], size=17, gap=13)
    d.takeaway(s, "OO design = responsibilities, objects, components and layers working together.")

    # 26. closing
    d.closing("REVISION & NEXT STEPS", [
        "Classify the registration activities into layers (Presentation/Application/Domain/Data Access/Database).",
        "Draw a component diagram for the online banking system.",
        "Identify three reusable and two adaptable components for the university system.",
        "Next week: integrating the Object, Dynamic and Behavioural models into the OO design.",
    ])


def build_pptx():
    return build(CFG, slides)


if __name__ == "__main__":
    print("Built:", build_pptx())
