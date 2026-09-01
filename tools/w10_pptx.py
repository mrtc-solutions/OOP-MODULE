"""
Week 10 PPTX content — OBJECT-ORIENTED DESIGN.
"""
from pptxengine import build

CFG = {
    "week": 10,
    "title": "Object-Oriented Design",
    "filename": "Week10_Presentation_BICT3202_OOAD.pptx",
}


def slides(d):
    # 2. learning outcomes
    s = d.slide()
    d.header(s, "Learning Outcomes", "By the end of this week, you should be able to…")
    d.bullets(s, 0.9, 1.6, 11.6, 5.0, [
        ("Define ", "software design and object-oriented design."),
        ("Distinguish ", "OO analysis from OO design, with examples."),
        ("Explain ", "why design is necessary and list the goals of good design."),
        ("Explain ", "responsibility, cohesion, coupling, abstraction, encapsulation."),
        ("Explain ", "high cohesion + low coupling, and why good design seeks both."),
        ("Explain ", "architecture, refinement, interfaces and traceability."),
        ("Combine ", "the Object, Dynamic and Behavioural models into a design."),
    ], size=16, gap=11)
    d.takeaway(s, "Analysis = what the system needs · Design = how the software is organised.")

    # 3. progression
    s = d.slide()
    d.header(s, "Where Week 10 Fits", "The most important transition in OOAD")
    d.pic(s, "w10_progression.png", y=1.6, w=10.6)
    d.takeaway(s, "Weeks 4–8 built the models; Week 10 turns them into a design.")

    # 4. house analogy
    s = d.slide()
    d.header(s, "Design: The House Analogy", "A requirement states the goal · design decides how")
    d.pic(s, "w10_house.png", y=1.6, w=10.6)
    d.takeaway(s, "Software design decides how the parts are organised and work together.")

    # 5. analysis vs design
    s = d.slide()
    d.header(s, "Analysis vs Design", "The key distinction of Week 10")
    d.pic(s, "w10_analysis_vs_design.png", y=1.6, w=10.6)
    d.takeaway(s, "Analysis understands the problem · Design plans the software solution.")

    # 6. analysis model vs design model
    s = d.slide()
    d.header(s, "Analysis Model vs Design Model", "The analysis model is the foundation")
    d.pic(s, "w10_analysis_design_model.png", y=1.6, w=10.6)
    d.takeaway(s, "The design model adds implementation detail: classes, interfaces, packages.")

    # 7. why design
    s = d.slide()
    d.header(s, "Why Not Just Start Coding?", "student.java, three months later…")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("One 15,000-line file ", "holds login, payments, registration, reports, database, email, SMS…"),
        ("Change one feature ", "and five others break."),
        ("Good design makes systems easier to ", "understand, implement, test, maintain, modify, extend, reuse, debug, scale."),
    ], size=17, gap=14)
    d.takeaway(s, "Design first — it is far cheaper than redesigning after coding.")

    # 8. design goals
    s = d.slide()
    d.header(s, "Design Goals", "What makes a good object-oriented design?")
    d.pic(s, "w10_design_goals.png", y=1.6, w=10.6)
    d.takeaway(s, "Correctness · maintainability · reusability · flexibility · understandability · testability · scalability · security.")

    # 9. poor vs good
    s = d.slide()
    d.header(s, "Poor vs Good Design", "One huge class vs focused responsibilities")
    d.pic(s, "w10_poor_vs_good.png", y=1.6, w=10.6)
    d.takeaway(s, "Good design spreads responsibilities across focused components.")

    # 10. responsibility
    s = d.slide()
    d.header(s, "Responsibility", "What an object knows · what it does")
    d.pic(s, "w10_responsibility.png", y=1.6, w=10.6)
    d.takeaway(s, "A responsibility is something a class is responsible for knowing or doing.")

    # 11. responsibility assignment
    s = d.slide()
    d.header(s, "Responsibility Assignment", "Which object should do this?")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("To calculate total fees, who should do it?", ""),
        ("Option 1: ", "Student.calculateFees()"),
        ("Option 2: ", "FeeAccount.calculateTotal()"),
        ("Option 3: ", "PaymentService.calculateFees()"),
        ("The designer chooses ", "based on the responsibilities and relationships of the objects."),
    ], size=17, gap=13)
    d.takeaway(s, "Central design question: \u201cWhich object should be responsible for this operation?\u201d")

    # 12. cohesion
    s = d.slide()
    d.header(s, "Cohesion", "How closely related are the responsibilities inside a class?")
    d.pic(s, "w10_cohesion.png", y=1.6, w=10.6)
    d.takeaway(s, "Ask: does everything inside this class belong together?")

    # 13. coupling
    s = d.slide()
    d.header(s, "Coupling", "How strongly does a class depend on other classes?")
    d.pic(s, "w10_coupling.png", y=1.6, w=10.6)
    d.takeaway(s, "Depend on abstractions (interfaces), not on concrete implementations.")

    # 14. cohesion vs coupling
    s = d.slide()
    d.header(s, "Cohesion vs Coupling", "One looks inside · the other looks between")
    d.pic(s, "w10_cohesion_coupling.png", y=1.6, w=10.6)
    d.takeaway(s, "Good design = high cohesion + low coupling.")

    # 15. abstraction
    s = d.slide()
    d.header(s, "Abstraction", "Focus on the important, hide the unnecessary")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Using an ATM: ", "insert card, enter PIN, select withdrawal, enter amount, receive money."),
        ("You don't need to know ", "the database, encryption, communication or cash dispenser internals."),
        ("In design: ", "call PaymentProcessor.processPayment() — the details are hidden."),
    ], size=17, gap=13)
    d.takeaway(s, "Abstraction shows the interface and hides the complexity.")

    # 16. encapsulation
    s = d.slide()
    d.header(s, "Encapsulation", "Keep data and operations together; protect the state")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("BankAccount ", "has private balance with deposit(), withdraw(), getBalance()."),
        ("Change state via ", "account.deposit(500) — never account.balance = 500."),
        ("Result: ", "the object's state is protected from outside interference."),
    ], size=17, gap=13)
    d.takeaway(s, "Encapsulation protects the internal state and implementation.")

    # 17. abstraction vs encapsulation
    s = d.slide()
    d.header(s, "Abstraction vs Encapsulation", "What the user sees · what the object hides")
    d.pic(s, "w10_abstraction_encapsulation.png", y=1.6, w=10.6)
    d.takeaway(s, "Abstraction = hide complexity · Encapsulation = protect internal state.")

    # 18. separation of concerns
    s = d.slide()
    d.header(s, "Separation of Concerns", "Different concerns handled by the appropriate part")
    d.pic(s, "w10_separation.png", y=1.6, w=10.6)
    d.takeaway(s, "Presentation -> Business Logic -> Data Access -> Database.")

    # 19. architecture
    s = d.slide()
    d.header(s, "Design Architecture", "The high-level organisation of a software system")
    d.pic(s, "w10_architecture.png", y=1.6, w=10.6)
    d.takeaway(s, "Major components, layers, interfaces, dependencies and deployment decisions.")

    # 20. refinement
    s = d.slide()
    d.header(s, "Refinement", "Progressively add detail: analysis -> design -> code")
    d.pic(s, "w10_refinement.png", y=1.6, w=10.6)
    d.takeaway(s, "Problem -> analysis model -> design model -> implementation -> running software.")

    # 21. three models
    s = d.slide()
    d.header(s, "The Three OOAD Models", "Structure · time/state · interaction")
    d.pic(s, "w10_three_models.png", y=1.6, w=10.6)
    d.takeaway(s, "Object model = what exists · Dynamic model = what changes · Behavioural model = what happens.")

    # 22. integration case study
    s = d.slide()
    d.header(s, "Combining the Models", "Case study: online course registration")
    d.pic(s, "w10_integration.png", y=1.6, w=10.6)
    d.takeaway(s, "Requirement -> use case -> objects -> models -> sequence -> design.")

    # 23. consistency + traceability
    s = d.slide()
    d.header(s, "Model Consistency & Traceability", "The models must agree — and be followable")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Consistency: ", "if the sequence diagram calls Course.checkPrerequisite(), the class model must define it."),
        ("Consistency: ", "if the use case actor is Student, the sequence must not show Lecturer -> registerCourse()."),
        ("Traceability: ", "requirement -> use case -> activity -> sequence -> class -> code -> test."),
    ], size=16, gap=13)
    d.pic(s, "w10_traceability.png", y=5.6, w=10.6)
    d.takeaway(s, "Traceability shows which models and code a change might affect.")

    # 24. sequence, class, interfaces
    s = d.slide()
    d.header(s, "Sequence, Design Classes & Interfaces", "Design-level UML")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Sequence diagrams ", "show the order of interactions between objects."),
        ("Design classes ", "add visibility, attribute types, parameter and return types, operations."),
        ("Interfaces ", "define a contract — <<interface>> PaymentProcessor.processPayment()."),
        ("BankPayment and MobileMoneyPayment ", "can both implement the same interface -> lower coupling."),
    ], size=16, gap=13)
    d.takeaway(s, "Interfaces let the application depend on the abstraction, not a concrete class.")

    # 25. patterns + SOLID
    s = d.slide()
    d.header(s, "Design Patterns & SOLID (outline)", "Reusable structures · design guidelines")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Design patterns: ", "Factory · Observer · Strategy · Adapter · Singleton."),
        ("Strategy example: ", "PaymentStrategy — Bank, Mobile, Card (no chain of if/else)."),
        ("SOLID: ", "Single Responsibility · Open/Closed · Liskov Substitution · Interface Segregation · Dependency Inversion."),
        ("Treat SOLID ", "as guidelines, not magical rules."),
    ], size=16, gap=13)
    d.takeaway(s, "Patterns and principles support cohesion, low coupling and flexibility.")

    # 26. master diagram
    s = d.slide()
    d.header(s, "Week 10 Master Diagram", "Requirements -> models -> design -> code")
    d.pic(s, "w10_master.png", y=1.6, w=10.4)
    d.takeaway(s, "That is the central lesson of Week 10.")

    # 27. misunderstandings
    s = d.slide()
    d.header(s, "Common Misunderstandings", "Avoid these")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("\u201cAnalysis is just drawing diagrams\u201d ", "— it is understanding requirements, domain and behaviour."),
        ("\u201cDesign means coding\u201d ", "— coding is implementation; design precedes it."),
        ("\u201cA class diagram is enough\u201d ", "— you may also need sequence, state, activity, component and deployment views."),
        ("\u201cMore classes = better design\u201d ", "— aim for an appropriate structure, not a maximum count."),
        ("\u201cAlways use inheritance\u201d ", "— only when a genuine IS-A relationship exists."),
    ], size=15, gap=11)
    d.takeaway(s, "Classic exam traps — know them.")

    # 28. summary
    s = d.slide()
    d.header(s, "Week 10 Summary", "The big idea")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("1. ", "Analysis tells us WHAT the system needs; design determines HOW to organise the software."),
        ("2. ", "Good design aims for high cohesion and low coupling."),
        ("3. ", "Abstraction hides complexity; encapsulation protects state."),
        ("4. ", "The three models complement one another — structure + behaviour + time/state."),
        ("5. ", "Traceability links every requirement to its models, code and tests."),
    ], size=17, gap=13)
    d.takeaway(s, "Week 10 = turning the Weeks 4–8 models into an implementable design.")

    # 29. closing
    d.closing("REVISION & NEXT STEPS", [
        "Define OO design, then explain analysis vs design with the registration example.",
        "For the UniversitySystem class, diagnose cohesion and coupling and propose a redesign.",
        "Combine the three models for \u201cCustomer withdraws money\u201d and draw the sequence.",
        "Next week: Object-Oriented Design continues — refinements, integration and further design detail.",
    ])


def build_pptx():
    return build(CFG, slides)


if __name__ == "__main__":
    print("Built:", build_pptx())
