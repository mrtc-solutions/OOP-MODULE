"""
Week 11 PPTX content — REFINING THE OBJECT-ORIENTED DESIGN.
"""
from pptxengine import build

CFG = {
    "week": 11,
    "title": "Refining the Object-Oriented Design",
    "filename": "Week11_Presentation_BICT3202_OOAD.pptx",
}


def slides(d):
    # 2. learning outcomes
    s = d.slide()
    d.header(s, "Learning Outcomes", "By the end of this week, you should be able to…")
    d.bullets(s, 0.9, 1.6, 11.6, 5.0, [
        ("Explain ", "design refinement and the analysis-to-design transformation."),
        ("Distinguish ", "an analysis class from a design class."),
        ("Identify ", "design classes — entity, boundary and control."),
        ("Refine ", "attributes and operations with types and signatures."),
        ("Assign ", "responsibilities; choose association vs inheritance."),
        ("Compare ", "interfaces and abstract classes."),
        ("Explain ", "cohesion, coupling, encapsulation, dependencies, layers, reuse and traceability."),
    ], size=16, gap=11)
    d.takeaway(s, "Drawing a UML class diagram is not the same as completing an OO design.")

    # 3. progression
    s = d.slide()
    d.header(s, "Week 10 → 11 → 12", "What is design? → refine it → integrate it")
    d.pic(s, "w11_progression.png", y=1.6, w=10.6)
    d.takeaway(s, "Week 11 turns the Week 10 models into an implementable design.")

    # 4. refinement
    s = d.slide()
    d.header(s, "Design Refinement", "General → detailed and precise")
    d.pic(s, "w11_refinement.png", y=1.6, w=10.6)
    d.takeaway(s, "The design model becomes increasingly precise toward implementation.")

    # 5. analysis vs design class
    s = d.slide()
    d.header(s, "Analysis Class vs Design Class", "A key examination distinction")
    d.pic(s, "w11_analysis_vs_design_class.png", y=1.6, w=10.6)
    d.takeaway(s, "Analysis = domain concept · Design = how the software represents and manipulates it.")

    # 6. entity/boundary/control
    s = d.slide()
    d.header(s, "Entity, Boundary & Control Classes", "Three roles for thinking about classes")
    d.pic(s, "w11_entity_boundary_control.png", y=1.6, w=10.6)
    d.takeaway(s, "Student → RegistrationPage → RegistrationController → Registration → Course.")

    # 7. attributes
    s = d.slide()
    d.header(s, "Refining Attributes", "From plain names to typed data")
    d.pic(s, "w11_attributes.png", y=1.6, w=10.6)
    d.takeaway(s, "Ask: what does the object need to fulfil its responsibilities?")

    # 8. operations
    s = d.slide()
    d.header(s, "Refining Operations", "Operation signatures communicate much more")
    d.pic(s, "w11_operations.png", y=1.6, w=10.6)
    d.takeaway(s, "registerCourse(course: Course): Registration — name, input, return value.")

    # 9. responsibility
    s = d.slide()
    d.header(s, "Responsibility-Driven Design", "Which object should do this?")
    d.pic(s, "w11_responsibility.png", y=1.6, w=10.6)
    d.takeaway(s, "Assign each responsibility to the object that owns the relevant information.")

    # 10. cohesion
    s = d.slide()
    d.header(s, "Cohesion", "How closely related are the responsibilities inside a class?")
    d.pic(s, "w11_cohesion.png", y=1.6, w=10.6)
    d.takeaway(s, "Good design generally aims for high cohesion.")

    # 11. coupling
    s = d.slide()
    d.header(s, "Coupling", "Reduce dependency with abstractions")
    d.pic(s, "w11_coupling.png", y=1.6, w=10.6)
    d.takeaway(s, "The service depends on the abstraction, not each concrete implementation.")

    # 12. interface
    s = d.slide()
    d.header(s, "Interfaces", "A contract — and the wall-socket analogy")
    d.pic(s, "w11_interface.png", y=1.6, w=10.6)
    d.takeaway(s, "Any class implementing an interface must provide those operations.")

    # 13. abstract vs interface
    s = d.slide()
    d.header(s, "Abstract Class vs Interface", "A comparison you must know")
    d.pic(s, "w11_abstract_vs_interface.png", y=1.6, w=10.6)
    d.takeaway(s, "Abstract class = common base · interface = contract (language details vary).")

    # 14. association vs inheritance
    s = d.slide()
    d.header(s, "Association vs Inheritance", "HAS / USES vs IS-A")
    d.pic(s, "w11_association_inheritance.png", y=1.6, w=10.6)
    d.takeaway(s, "A Student TAKES a Course (association) · a Student IS-A Person (inheritance).")

    # 15. encapsulation
    s = d.slide()
    d.header(s, "Encapsulation & Information Hiding", "The class controls its own state")
    d.pic(s, "w11_encapsulation.png", y=1.6, w=10.6)
    d.takeaway(s, "account.withdraw(500) enforces rules; account.balance = -500000 is blocked.")

    # 16. dependency
    s = d.slide()
    d.header(s, "Dependencies & Dependency Injection", "Provide the dependency, don't construct it")
    d.pic(s, "w11_dependency.png", y=1.6, w=10.6)
    d.takeaway(s, "RegistrationService(repository) improves testability, flexibility, substitution.")

    # 17. layers
    s = d.slide()
    d.header(s, "Layered Design", "Divide the system into logical levels")
    d.pic(s, "w11_layers.png", y=1.5, w=10.4)
    d.takeaway(s, "If the web UI becomes a mobile app, the business rules can remain usable.")

    # 18. reuse
    s = d.slide()
    d.header(s, "Design for Reuse", "One reusable component, many applications")
    d.pic(s, "w11_reuse.png", y=1.6, w=10.6)
    d.takeaway(s, "One AuthenticationService for Student Portal, Staff Portal, Mobile App, Library.")

    # 19. design for change
    s = d.slide()
    d.header(s, "Design for Change", "Requirements will change")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Start: ", "\u201cStudents only use email.\u201d"),
        ("Then: ", "\u201cAdd SMS.\u201d — later, \u201cAdd WhatsApp.\u201d"),
        ("Poor design: ", "every new method changes the Student class."),
        ("Better: ", "NotificationService behind a Notification interface → Email, SMS, WhatsApp."),
        ("Result: ", "the architecture stays adaptable."),
    ], size=16, gap=13)
    d.takeaway(s, "Design for reasonable future change without trying to predict everything.")

    # 20. design quality
    s = d.slide()
    d.header(s, "How Do We Judge a Design?", "Seven questions")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Correct? ", "meets the requirements."),
        ("Understandable? ", "another developer can understand it."),
        ("Maintainable? ", "it can be changed."),
        ("Testable? ", "components can be tested in isolation."),
        ("Reusable? ", "useful parts can be used elsewhere."),
        ("Appropriately coupled? ", "no unnecessary dependencies."),
        ("Cohesive? ", "each component has a focused purpose."),
    ], size=16, gap=13)
    d.takeaway(s, "These mirror the OO design-quality literature (coupling, cohesion, maintainability).")

    # 21. traceability
    s = d.slide()
    d.header(s, "Design Traceability", "Follow requirement R01 to code and test")
    d.pic(s, "w11_traceability.png", y=1.5, w=10.6)
    d.takeaway(s, "\u201cWhere is R01 implemented?\u201d — traceability answers this.")

    # 22. case study
    s = d.slide()
    d.header(s, "Integrated Case Study", "Seven steps to a complete design")
    d.pic(s, "w11_case_study.png", y=1.5, w=10.6)
    d.takeaway(s, "Use case → classes → class design → service → sequence → state → architecture.")

    # 23. mistakes
    s = d.slide()
    d.header(s, "Common Design Mistakes", "Avoid these")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("One giant class ", "— low cohesion and high coupling."),
        ("Everything inherits from everything ", "— only when IS-A genuinely holds."),
        ("Direct database access everywhere ", "— route through repositories."),
        ("Exposing everything ", "— public balance / password undermines encapsulation."),
        ("Designing only for today ", "— consider reasonable future change."),
    ], size=15, gap=11)
    d.takeaway(s, "Five classic traps in examination answers.")

    # 24. summary
    s = d.slide()
    d.header(s, "Week 11 Summary", "The most important idea")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("1. ", "Refinement turns analysis classes into detailed design classes."),
        ("2. ", "Assign responsibilities to the objects that own the information."),
        ("3. ", "Aim for high cohesion and low coupling (use interfaces)."),
        ("4. ", "Encapsulate state; hide implementation; inject dependencies."),
        ("5. ", "Layer the architecture; design for reuse and change; keep traceability."),
    ], size=17, gap=13)
    d.takeaway(s, "Goal: correct, understandable, maintainable, testable, reusable, adaptable design.")

    # 25. closing
    d.closing("REVISION & NEXT STEPS", [
        "Refine the Student/Course/Registration analysis classes into full design classes.",
        "Draw a PaymentGateway interface with Bank and Mobile implementations.",
        "Redesign the HospitalSystem class into a layered, cohesive structure.",
        "Next week: Integrated OO Design — putting all models and decisions together into a complete system.",
    ])


def build_pptx():
    return build(CFG, slides)


if __name__ == "__main__":
    print("Built:", build_pptx())
