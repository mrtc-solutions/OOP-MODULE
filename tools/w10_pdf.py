"""
Week 10 PDF content — OBJECT-ORIENTED DESIGN.
"""
from pdfengine import (H1, H2, P, BUL, FIG, CALLOUT, DTABLE, build, DOC_W,
                      C_MAROON, C_SOFT)

CFG = {
    "week": 10,
    "title": "Object-Oriented Design",
    "filename": "Week10_Module_BICT3202_OOAD.pdf",
}


def story():
    s = []

    # 1. introduction --------------------------------------------------------
    s.append(H1("1.  Week 10 Introduction"))
    s += [P("Week 9 organised <b>how</b> the development work is done (the Unified Process). "
            "Week 10 now moves into the <b>design</b> part of the syllabus: <b>Object-Oriented "
            "Design</b> — an overview of design, and the combining of the <b>Object Model</b>, the "
            "<b>Dynamic Model</b> and the <b>Behavioural Model</b> that we built in Weeks 4–8."),
          P("The most important transition in OOAD happens here:"),
          P("<b>ANALYSIS — “What does the system need?”  ->  DESIGN — “How are we going to build "
            "it?”</b>")]
    s += FIG("w10_progression.png", "Figure 1 — Where Week 10 fits: analysis -> design")

    # 2. learning outcomes -----------------------------------------------------
    s.append(H1("2.  Learning Outcomes"))
    s += [P("By the end of this week, a student should be able to:")]
    s += BUL([
        "Define software design and object-oriented design.",
        "Distinguish object-oriented analysis from object-oriented design, with examples.",
        "Explain why design is necessary and list the goals of good design.",
        "Explain responsibility, cohesion, coupling, abstraction, encapsulation and separation of concerns.",
        "Explain high cohesion and low coupling, and why good design seeks both.",
        "Describe design architecture, refinement and traceability.",
        "Combine the Object, Dynamic and Behavioural models into a design suitable for implementation.",
        "Explain interfaces and, in outline, design patterns and the SOLID principles.",
    ])

    # PART A — what is design ---------------------------------------------------
    s.append(H1("PART A — WHAT IS SOFTWARE DESIGN?"))
    s.append(H1("3.  The Simple Meaning of Design"))
    s += [P("Before software, think about constructing a house. A client tells an architect: "
            "<i>“I want a three-bedroom house.”</i> That is a <b>requirement</b>. The architect then "
            "decides where the bedrooms, kitchen and bathroom go, how electricity is arranged, where "
            "pipes run, what materials to use and how the building is supported. That is <b>design</b>."),
          P("Software is similar. A customer says: <i>“I want a university student registration "
            "system.”</i> That is a requirement. The designer then decides what classes and "
            "components are needed, how classes communicate, where business logic belongs, how data is "
            "stored, how authentication works, how the system is divided into layers, how errors are "
            "handled and how objects collaborate. That is <b>software design</b>.")]
    s += FIG("w10_house.png", "Figure 2 — The house analogy: requirement vs design")

    s.append(H1("4.  Definitions"))
    s += [P("<b>Software design</b> is the process of determining the structure, components, "
            "interfaces, interactions and implementation decisions needed to transform requirements and "
            "analysis results into a system that can be implemented. A student-friendly version: "
            "<i>“Software design is the process of deciding how a software system will be organised and "
            "how its parts will work together to satisfy its requirements.”</i>"),
          P("<b>Object-Oriented Design (OOD)</b> is the process of designing software around "
            "<b>objects, classes, responsibilities, relationships, interfaces, collaborations, "
            "inheritance (where appropriate) and encapsulated data and behaviour</b>. The designer asks: "
            "<i>“What should the Student object know?”</i> and <i>“What should it be responsible for "
            "doing?”</i>")]

    # 5. analysis vs design ------------------------------------------------------
    s.append(H1("5.  Analysis vs Design — THE KEY DISTINCTION"))
    s += [P("Students often say <i>“analysis and design are the same thing.”</i> They are related, but "
            "not identical. <b>Analysis</b> asks <b>what</b> the system needs to accomplish — business "
            "requirements, user needs, domain concepts, system behaviour, objects, relationships and use "
            "cases. <b>Design</b> asks <b>how</b> the software should be structured and implemented — "
            "classes, interfaces, components, architecture, responsibilities, object collaborations, data "
            "access, security, persistence and technologies.")]
    s += FIG("w10_analysis_vs_design.png", "Figure 3 — Analysis (WHAT) vs Design (HOW)")

    s.append(H1("6.  Worked Example — “Register for a Course”"))
    s += [P("Given the requirement <i>“A student should be able to register for a course.”</i>, "
            "<b>analysis</b> identifies the concepts <b>Student, Course, Registration</b>. "
            "<b>Design</b> then asks how the software will make this happen and introduces "
            "<b>RegistrationService, CourseRepository, StudentRepository</b> and the flow "
            "Student -> RegistrationService -> CourseRepository -> Database. Now we are making "
            "implementation-oriented decisions.")]

    # 7. analysis model vs design model ------------------------------------------
    s.append(H1("7.  Analysis Model vs Design Model"))
    s += [P("The <b>analysis model</b> describes the logical structure of the application without "
            "focusing on how it will be implemented; the <b>design model</b> builds on it and adds "
            "implementation-oriented detail — design classes, interfaces, packages and architectural "
            "elements.")]
    s += FIG("w10_analysis_design_model.png", "Figure 4 — Analysis model vs design model")

    # PART B — why design --------------------------------------------------------
    s.append(H1("PART B — WHY DO WE NEED DESIGN?"))
    s.append(H1("8.  Why Not Just Start Coding?"))
    s += [P("A lecturer says <i>“Build a university management system”</i> and the programmer "
            "immediately opens the editor and writes <font name='Mono'>student.java</font>. Three months "
            "later that file has 15,000 lines containing login, payments, course registration, reports, "
            "database queries, email, SMS, authentication and results — and changing one feature breaks "
            "five others. That is exactly why design matters. <b>Good design makes systems easier to "
            "understand, implement, test, maintain, modify, extend, reuse, debug and scale.</b>")]

    s.append(H1("9.  Design Goals"))
    s += [P("A good object-oriented design should generally aim for eight goals:")]
    s += BUL([
        "<b>Correctness</b> — the design satisfies the requirements.",
        "<b>Maintainability</b> — developers can modify it without destroying unrelated functionality.",
        "<b>Reusability</b> — useful components can be reused elsewhere.",
        "<b>Flexibility</b> — the system can adapt to changing requirements.",
        "<b>Understandability</b> — developers can understand how it works.",
        "<b>Testability</b> — individual parts can be tested effectively.",
        "<b>Scalability</b> — the system can accommodate increased demand where required.",
        "<b>Security</b> — security requirements are incorporated into the design.",
    ])
    s += FIG("w10_design_goals.png", "Figure 5 — Eight design goals")
    s.append(H1("10.  Poor vs Good Design"))
    s += [P("A poor design puts everything — login, registration, fees, email, reports, database — into "
            "one huge class. A better design splits them into focused services such as "
            "<b>AuthenticationService, RegistrationService, PaymentService, EmailService, ReportService, "
            "ResultService</b>.")]
    s += FIG("w10_poor_vs_good.png", "Figure 6 — Poor vs good design")

    # PART D — responsibility -----------------------------------------------------
    s.append(H1("PART D — RESPONSIBILITY"))
    s.append(H1("11.  What Is Responsibility?"))
    s += [P("A <b>responsibility</b> is something an object or class is responsible for "
            "<b>knowing</b> or <b>doing</b>. A <font name='Mono'>Student</font> should know its "
            "<font name='Mono'>studentID, name, programme</font> and should do "
            "<font name='Mono'>registerCourse()</font> and <font name='Mono'>dropCourse()</font>. A "
            "<font name='Mono'>Course</font> should know its <font name='Mono'>courseCode, title, "
            "credits, capacity</font> and should do <font name='Mono'>hasSpace()</font>."),
          P("<b>Responsibility assignment</b> is one of the central design questions: <i>“Which object "
            "should be responsible for this operation?”</i> To calculate total fees, should it be "
            "<font name='Mono'>Student.calculateFees()</font>, "
            "<font name='Mono'>FeeAccount.calculateTotal()</font> or "
            "<font name='Mono'>PaymentService.calculateFees()</font>? The designer chooses based on the "
            "responsibilities and relationships of the objects.")]
    s += FIG("w10_responsibility.png", "Figure 7 — Responsibility: knowing and doing")

    # PART E/F — cohesion and coupling --------------------------------------------
    s.append(H1("PART E &amp; F — COHESION AND COUPLING"))
    s.append(H1("12.  Cohesion"))
    s += [P("<b>Cohesion</b> describes how closely related the responsibilities inside a class or module "
            "are. <b>High cohesion</b> means a class focuses on closely related responsibilities — a "
            "<font name='Mono'>Course</font> with <font name='Mono'>courseCode, title, credits, capacity, "
            "hasSpace(), addStudent(), removeStudent()</font> is cohesive. <b>Low cohesion</b> means a "
            "class does too many unrelated things. Ask: <i>“Does everything inside this class belong "
            "together?”</i>")]
    s += FIG("w10_cohesion.png", "Figure 8 — High vs low cohesion")

    s.append(H1("13.  Coupling"))
    s += [P("<b>Coupling</b> describes how strongly one class/module depends on others. "
            "<b>High coupling</b> means every class directly depends on every other class — changing one "
            "part becomes dangerous. <b>Low coupling</b> means components communicate through clearly "
            "defined interfaces, which makes substitution and testing easier. Generally good OO design "
            "aims for <b>low coupling</b>.")]
    s += FIG("w10_coupling.png", "Figure 9 — High vs low coupling")

    s.append(H1("14.  Cohesion vs Coupling — Do Not Confuse Them"))
    s += [P("<b>Cohesion looks inside a component</b> (how closely related are its responsibilities?); "
            "<b>coupling looks between components</b> (how strongly do they depend on each other?). "
            "Therefore:")]
    s += [P("<b>GOOD DESIGN = HIGH COHESION  +  LOW COUPLING</b>")]
    s += FIG("w10_cohesion_coupling.png", "Figure 10 — Cohesion vs coupling")

    # PART G/H — abstraction and encapsulation -------------------------------------
    s.append(H1("PART G &amp; H — ABSTRACTION AND ENCAPSULATION"))
    s.append(H1("15.  Abstraction"))
    s += [P("<b>Abstraction</b> means focusing on the important characteristics of something while "
            "hiding unnecessary details. Using an ATM you insert a card, enter a PIN, select withdrawal, "
            "enter an amount and receive money — you do not need to know how the bank's database, "
            "encryption, communication or cash dispenser work. In OO design, a "
            "<font name='Mono'>PaymentProcessor.processPayment()</font> hides the internal detail from "
            "the rest of the application.")]

    s.append(H1("16.  Encapsulation"))
    s += [P("<b>Encapsulation</b> means keeping data and the operations that manage that data together "
            "while controlling access to the internal state. A <font name='Mono'>BankAccount</font> has a "
            "private <font name='Mono'>balance</font> and public <font name='Mono'>deposit()</font>, "
            "<font name='Mono'>withdraw()</font> and <font name='Mono'>getBalance()</font> — the balance "
            "is changed through <font name='Mono'>account.deposit(500)</font>, never "
            "<font name='Mono'>account.balance = 500</font>. This protects the object's state."),
          P("<b>Abstraction vs encapsulation:</b> abstraction focuses on <i>what the user should "
            "see</i>; encapsulation focuses on <i>what the object should hide/protect internally</i>.")]
    s += FIG("w10_abstraction_encapsulation.png", "Figure 11 — Abstraction vs encapsulation")

    # PART I/J — separation of concerns and architecture ---------------------------
    s.append(H1("PART I &amp; J — SEPARATION OF CONCERNS AND ARCHITECTURE"))
    s.append(H1("17.  Separation of Concerns"))
    s += [P("<b>Separation of concerns</b> means dividing a system so that different concerns are "
            "handled by appropriate parts — Presentation -> Business Logic -> Data Access -> Database — "
            "rather than mixing SQL, password hashing, HTML and database connections into one "
            "<font name='Mono'>LoginScreen</font>.")]
    s += FIG("w10_separation.png", "Figure 12 — Separation of concerns")

    s.append(H1("18.  Design Architecture"))
    s += [P("<b>Software architecture</b> is the high-level organisation of a software system — its "
            "major components, layers, interfaces, dependencies, communication mechanisms and deployment "
            "decisions. A common conceptual structure is the <b>three-layer architecture</b>: "
            "Presentation (Web/Mobile/Desktop UI), Business Logic (rules/services), and Data "
            "(repositories/database). Example — a student clicks <b>Register Course</b>: the "
            "presentation forwards to business logic, which checks that the student is active, the course "
            "is available, prerequisites are met and there is space, and the data layer retrieves and "
            "updates the records.")]
    s += FIG("w10_architecture.png", "Figure 13 — Three-layer architecture")

    # PART K — refinement -----------------------------------------------------------
    s.append(H1("PART K — DESIGN REFINEMENT"))
    s.append(H1("19.  Refinement"))
    s += [P("<b>Refinement</b> means taking a high-level model and progressively adding detail. The "
            "analysis class <font name='Mono'>Student</font> becomes a design class with typed attributes "
            "(<font name='Mono'>studentId: String, name: String, email: String, status: "
            "StudentStatus</font>) and typed operations (<font name='Mono'>registerCourse(), "
            "dropCourse(), getRegisteredCourses()</font>), and finally implementation in "
            "<font name='Mono'>Student.java</font>, <font name='Mono'>Student.cs</font> or "
            "<font name='Mono'>Student.ts</font>. The path is: Real-world problem -> Analysis model -> "
            "Design model -> Implementation -> Running software.")]
    s += FIG("w10_refinement.png", "Figure 14 — Refinement: analysis -> design -> code")

    # PART L/M — combining the three models -----------------------------------------
    s.append(H1("PART L &amp; M — COMBINING THE THREE MODELS  (the core of Week 10)"))
    s.append(H1("20.  The Three OOAD Models"))
    s += [P("<b>Object Model</b> — describes the <b>structure</b>: what things/classes exist "
            "(Student, Course, Registration, Payment). <b>Dynamic Model</b> — describes how objects "
            "change over <b>time</b> and respond to events (Registration: Requested -> Pending -> "
            "Confirmed, or Pending -> Rejected). <b>Behavioural Model</b> — describes <b>what the system "
            "does</b> and how actors/objects interact (Student -> Register Course -> Validate Registration "
            "-> Confirm Registration)."),
          P("Why do we need all three? Knowing the parts of a car (Wheel, Engine, Brake, Steering) is "
            "not enough — we also need to know what happens when the driver presses the brake, and how "
            "the brake, wheel and engine systems interact. In software, <b>structure + behaviour + "
            "time/state must fit together</b>.")]
    s += FIG("w10_three_models.png", "Figure 15 — The three OOAD models")

    s.append(H1("21.  Case Study — Online Course Registration (7 Steps)"))
    s += [P("Requirement: <i>“A student should be able to register for an available course.”</i> "
            "<b>(1)</b> Behavioural model — use case <b>Register Course</b>. <b>(2)</b> Identify "
            "objects: Student, Course, Registration. <b>(3)</b> Object model — the classes with their "
            "attributes. <b>(4)</b> Relationships — Student 1 — 0..* Registration — Course. "
            "<b>(5)</b> Dynamic model — Registration states Requested -> Validated -> Confirmed (or "
            "Rejected). <b>(6)</b> Sequence — Student -> RegistrationService -> Course -> Registration -> "
            "Student. <b>(7)</b> Design — Student, Course, Registration plus RegistrationService, "
            "CourseRepository and RegistrationRepository.")]
    s += FIG("w10_integration.png", "Figure 16 — Combining the models")

    # PART N — consistency and traceability -----------------------------------------
    s.append(H1("PART N — MODEL CONSISTENCY AND TRACEABILITY"))
    s.append(H1("22.  Model Consistency"))
    s += [P("The different models should not contradict each other. If the class model gives "
            "<font name='Mono'>Course</font> only <font name='Mono'>courseCode, title, capacity</font> "
            "but the sequence diagram calls <font name='Mono'>Course.checkPrerequisite()</font>, the "
            "operation is missing — an inconsistency. Likewise, if the use case actor is "
            "<b>Student</b> but the sequence diagram shows <font name='Mono'>Lecturer -> "
            "registerCourse()</font>, the models disagree and must be reconciled.")]

    s.append(H1("23.  Traceability"))
    s += [P("<b>Traceability</b> means being able to follow a requirement through the development "
            "artefacts: Requirement -> Use Case -> Activity diagram -> Sequence diagram -> Class model -> "
            "Design classes -> Code -> Test case. If the requirement changes, developers can identify what "
            "models and code may be affected — this is extremely valuable.")]
    s += FIG("w10_traceability.png", "Figure 17 — Traceability")

    # PART O/P/Q — sequence, class, interfaces --------------------------------------
    s.append(H1("PART O–Q — SEQUENCE DIAGRAMS, DESIGN CLASSES AND INTERFACES"))
    s.append(H1("24.  Sequence and Class Diagrams in Design"))
    s += [P("<b>Sequence diagrams</b> show the order of interactions between objects — Student -> "
            "RegistrationService <font name='Mono'>register()</font> -> Course "
            "<font name='Mono'>checkAvailability()</font> — telling us far more than simply that "
            "Student, Course and Registration exist. <b>Design class diagrams</b> enrich the analysis "
            "classes with <b>visibility, attribute types, parameter types, return types and "
            "operations</b> (e.g. <font name='Mono'>+registerCourse(c: Course)</font>, "
            "<font name='Mono'>+getCourses(): List&lt;Course&gt;</font>).")]

    s.append(H1("25.  Interfaces"))
    s += [P("An <b>interface</b> defines a set of operations that a class/component agrees to provide "
            "— for example <font name='Mono'>&lt;&lt;interface&gt;&gt; PaymentProcessor + "
            "processPayment()</font>, implemented by both <font name='Mono'>BankPayment</font> and "
            "<font name='Mono'>MobileMoneyPayment</font>. When the university later adds mobile money, "
            "the application can depend on the abstraction and avoid unnecessary coupling.")]

    # PART R/S — patterns and SOLID --------------------------------------------------
    s.append(H1("PART R &amp; S — DESIGN PATTERNS AND SOLID (outline)"))
    s.append(H1("26.  Design Patterns"))
    s += [P("A <b>design pattern</b> is a reusable solution structure for a recurring design problem — "
            "e.g. Factory, Observer, Strategy, Adapter, Singleton. Example: the <b>Strategy pattern</b> "
            "conceptualises <font name='Mono'>PaymentStrategy</font> with Bank, Mobile and Card "
            "implementations instead of a chain of <font name='Mono'>if paymentType == …</font> branches, "
            "making the design more flexible.")]
    s.append(H1("27.  SOLID Principles (outline)"))
    s += [P("<b>S</b> — Single Responsibility; <b>O</b> — Open/Closed; <b>L</b> — Liskov "
            "Substitution; <b>I</b> — Interface Segregation; <b>D</b> — Dependency Inversion. These are "
            "<b>guidelines</b>, not magical rules, and relate closely to cohesion, coupling, abstraction "
            "and dependency management. The Single Responsibility Principle says a class should have a "
            "focused responsibility rather than accumulating unrelated ones; the Open/Closed Principle "
            "says entities should be open for extension but closed for modification.")]

    # PART T — complete process -------------------------------------------------------
    s.append(H1("PART T — THE COMPLETE OO DESIGN PROCESS"))
    s += [P("Requirement -> Use-case model -> Behavioural model -> interactions -> Object model (Student — "
            "Registration — Course) -> Dynamic model (Requested -> Validated -> Confirmed) -> Design model "
            "(RegistrationService, CourseRepository, RegistrationRepository) -> Architecture "
            "(Presentation / Business Logic / Data Access) -> Implementation -> Code. That is the central "
            "lesson of Week 10.")]
    s += FIG("w10_master.png", "Figure 18 — Week 10 master diagram")

    # practical ------------------------------------------------------------------------
    s.append(H1("28.  Practical Class"))
    s += [P("Working individually or in groups, design an online student registration system from the "
            "requirement: <i>“A student logs into the university system, searches for a course, selects "
            "the course, and registers if all conditions are satisfied.”</i>")]
    s += BUL([
        "<b>Task 1</b> — Identify classes (Student, Course, Registration…) and justify each.",
        "<b>Task 2</b> — Add responsibilities (Student: login(), registerCourse(), dropCourse(); Course: checkAvailability(), checkPrerequisite(); Registration: create(), confirm(), cancel()).",
        "<b>Task 3</b> — Draw a class diagram (classes, attributes, operations, associations, multiplicities).",
        "<b>Task 4</b> — Draw a sequence diagram (Student -> RegistrationService -> Course -> Registration).",
        "<b>Task 5</b> — Draw a state machine for Registration (Requested -> Validated -> Confirmed; alternative -> Rejected).",
        "<b>Task 6</b> — Critique a class that contains login(), registerCourse(), payFees(), sendSMS(), generateReport(), connectDatabase(), calculateResults() and uploadAssignment(): is cohesion high or low, why, and how could it be redesigned?",
    ])

    # tutorial --------------------------------------------------------------------------
    s.append(H1("29.  Tutorial Questions"))
    s += BUL([
        "Define Object-Oriented Design.",
        "Differentiate Object-Oriented Analysis from Object-Oriented Design, with an example.",
        "Why should a team not immediately begin coding after receiving a requirement?",
        "Explain cohesion and coupling, and why good design seeks high cohesion and low coupling.",
        "Differentiate abstraction and encapsulation using a BankAccount example.",
        "Explain the Object, Dynamic and Behavioural models.",
        "Explain why the three models must be consistent.",
        "For “Customer withdraws money”, identify possible classes, responsibilities, interactions and states.",
    ])

    # misunderstandings -------------------------------------------------------------------
    s.append(H1("30.  Common Misunderstandings"))
    s += BUL([
        "<b>“Analysis is just drawing diagrams.”</b> — Analysis is understanding requirements, domain, users, objects and behaviour; UML is only the representation.",
        "<b>“Design means coding.”</b> — Coding is implementation; design determines what the implementation should look like.",
        "<b>“A class diagram is enough.”</b> — It mainly shows structure; sequence, state, activity, component and deployment diagrams may also be needed.",
        "<b>“More classes always mean better design.”</b> — The goal is an appropriate structure, not the maximum number of classes.",
        "<b>“Inheritance should always be used.”</b> — Use it only when a genuine IS-A relationship exists (a Student is NOT a Course).",
    ])

    # summary ----------------------------------------------------------------------------
    s.append(H1("31.  Week 10 Summary and Key Terms"))
    s.append(DTABLE(
        ["Concept", "Student-friendly meaning"],
        [["Software design", "Deciding how the software will be structured."],
         ["OO design", "Designing around objects/classes and their responsibilities."],
         ["Analysis vs design", "Understanding the problem vs planning the solution."],
         ["Responsibility", "What a class knows or does."],
         ["Cohesion", "How closely related responsibilities inside a component are."],
         ["Coupling", "How strongly components depend on each other."],
         ["Abstraction", "Showing important things, hiding unnecessary detail."],
         ["Encapsulation", "Protecting internal data / implementation."],
         ["Interface", "Contract of operations a component provides."],
         ["Architecture", "High-level organisation of the system."],
         ["Refinement", "Adding detail to an existing model."],
         ["Traceability", "Following a requirement through models to code."],
         ["Object / Dynamic / Behavioural model", "Structure / states over time / interactions."],
         ["Design pattern", "Reusable solution structure for a recurring problem."]],
        widths=[0.36 * DOC_W, 0.64 * DOC_W]))
    s.append(CALLOUT("THE BIG IDEA",
        ["<b>Analysis tells us what the system needs; design determines how the software will be "
         "organised to satisfy those needs.</b> The three models are not competing — they complement "
         "one another: Object Model (what exists) + Dynamic Model (what changes) + Behavioural Model "
         "(what happens) -> integrated understanding -> object-oriented design -> implementable software."]))

    # exam --------------------------------------------------------------------------------
    s.append(H1("32.  Examination-Style Questions"))
    s += [P("<b>Essay (25 marks).</b> Explain the role of Object-Oriented Design in software "
            "development. Distinguish OO analysis from OO design, and discuss how the Object, Dynamic "
            "and Behavioural models can be combined to produce a design suitable for implementation."),
          P("<b>Scenario (20 marks).</b> A university wants an online student registration system in "
            "which students log in, search for courses, register, drop courses and view registered "
            "courses. (a) Identify five classes. (b) Assign at least two responsibilities to each. "
            "(c) Draw a class diagram. (d) Draw a sequence diagram for course registration. (e) Draw a "
            "state diagram for the Registration object. (f) Explain how the three models support one "
            "another.")]

    # references ---------------------------------------------------------------------------
    s.append(H1("33.  References and Further Reading"))
    s.append(H2("Authoritative / current online sources"))
    s += BUL([
        "Object Management Group (OMG). <i>Unified Modeling Language (UML), Version 2.5.1.</i> OMG. https://www.omg.org/uml/",
        "IBM. <i>Capturing solution architecture in a design model.</i> IBM documentation — the design model builds on the analysis model with design classes, interfaces, packages, sequence and state diagrams, components and deployment views. https://www.ibm.com/docs/en/dma",
        "IBM. <i>Capturing application domain in an analysis model.</i> IBM documentation — the analysis model as the logical foundation for design. https://www.ibm.com/docs/en/dma",
        "Hu, C. (2023). <i>An Introduction to Software Design: Concepts, Principles, Methodologies, and Techniques.</i> Springer. https://link.springer.com/book/10.1007/978-3-031-28311-6",
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
