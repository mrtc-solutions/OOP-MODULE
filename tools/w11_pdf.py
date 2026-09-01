"""
Week 11 PDF content — REFINING THE OBJECT-ORIENTED DESIGN.
"""
from pdfengine import (H1, H2, P, BUL, FIG, CALLOUT, DTABLE, build, DOC_W,
                      C_MAROON, C_SOFT)

CFG = {
    "week": 11,
    "title": "Refining the Object-Oriented Design",
    "filename": "Week11_Module_BICT3202_OOAD.pdf",
}


def story():
    s = []

    # 1. introduction --------------------------------------------------------
    s.append(H1("1.  Week 11 Introduction"))
    s += [P("Week 10 introduced Object-Oriented Design and the distinction "
            "<b>analysis = what the system needs, design = how the software is organised</b>. Week 11 "
            "goes one step deeper: <b>how do we refine those models into a design that developers can "
            "actually implement, maintain, test and extend?</b>"),
          P("Drawing a UML class diagram is not the same as completing an OO design. This week we "
            "refine analysis classes into design classes, refine attributes and operations, assign "
            "responsibilities, design relationships, choose association vs inheritance, work with "
            "interfaces and abstract classes, manage dependencies, and judge the quality of the "
            "resulting design.")]
    s += FIG("w11_progression.png", "Figure 1 — Week 10 -> 11 -> 12 progression")

    # 2. learning outcomes -----------------------------------------------------
    s.append(H1("2.  Learning Outcomes"))
    s += [P("By the end of this week, a student should be able to:")]
    s += BUL([
        "Explain the meaning of design refinement and the analysis-to-design transformation.",
        "Distinguish an analysis class from a design class.",
        "Identify design classes, including entity, boundary and control classes.",
        "Refine class attributes and operations with types, parameters and return values.",
        "Assign responsibilities appropriately (responsibility-driven design).",
        "Choose association vs inheritance using the HAS / IS-A test.",
        "Explain interfaces and abstract classes, and compare them.",
        "Explain cohesion, coupling, encapsulation, information hiding, separation of concerns and dependency management.",
        "Explain layered design, design for reuse, design for change, design quality and traceability.",
    ])

    # PART A — refinement -----------------------------------------------------
    s.append(H1("PART A — WHAT DOES “REFINEMENT” MEAN?"))
    s.append(H1("3.  The Meaning of Design Refinement"))
    s += [P("<b>Refinement</b> means taking something general and making it more detailed and precise. "
            "Saying <i>“I want to build a house”</i> is not enough for a construction team — you "
            "eventually need room dimensions, door and window locations, electrical and water layouts, "
            "materials, foundation and roof. Software design works the same way: during analysis we "
            "identify <b>Student, Course, Registration</b>; we then refine them into classes with typed "
            "attributes and operations. The design model becomes increasingly precise as it moves toward "
            "implementation.")]
    s += FIG("w11_refinement.png", "Figure 2 — Refinement: general -> detailed")

    s.append(H1("4.  Analysis Class vs Design Class"))
    s += [P("An <b>analysis class</b> represents an important concept in the problem domain (Student, "
            "Course, Registration). A <b>design class</b> adds the detail required to implement the "
            "solution — visibility, attribute types, parameter types, return values and operations. We "
            "move from <i>“there is a Student concept”</i> to <i>“here is how the software will "
            "represent and manipulate Student.”</i>")]
    s += FIG("w11_analysis_vs_design_class.png", "Figure 3 — Analysis class vs design class")

    # PART B — identifying design classes ---------------------------------------
    s.append(H1("PART B — IDENTIFYING DESIGN CLASSES"))
    s.append(H1("5.  What Is a Design Class?"))
    s += [P("A <b>design class</b> is a class defined with enough structural and behavioural detail to "
            "contribute to implementation. It may contain attributes, operations, visibility, types, "
            "parameters, return values, relationships, interfaces and constraints. For the requirement "
            "<i>“Students can register for courses online”</i>, analysis identifies Student, Course and "
            "Registration — but design also discovers <font name='Mono'>RegistrationService, "
            "StudentRepository, CourseRepository, RegistrationRepository</font> and "
            "<font name='Mono'>AuthenticationService</font>, because design must answer not just "
            "<i>what concepts exist</i> but <i>what software components are required to make the system "
            "work</i>.")]

    s.append(H1("6.  Entity, Boundary and Control Classes"))
    s += [P("<b>Entity classes</b> represent information important to the business/domain (Student, "
            "Course, Registration, Payment, Invoice). <b>Boundary classes</b> handle interaction between "
            "the system and external actors (LoginPage, RegistrationForm, StudentDashboard, "
            "PaymentScreen). <b>Control classes</b> coordinate activities or use-case logic "
            "(RegistrationController, PaymentController, LoginController) — so we may have Student -> "
            "RegistrationPage -> RegistrationController -> Registration -> Course.")]
    s += FIG("w11_entity_boundary_control.png", "Figure 4 — Entity, boundary and control classes")

    # PART C/D — attributes and operations --------------------------------------
    s.append(H1("PART C &amp; D — REFINING ATTRIBUTES AND OPERATIONS"))
    s.append(H1("7.  Refining Attributes"))
    s += [P("An <b>attribute</b> represents information maintained by an object — "
            "<font name='Mono'>Student</font> has <font name='Mono'>studentId, name, email, "
            "programme</font>. Design specifies types: <font name='Mono'>studentId : String</font>, "
            "<font name='Mono'>credits : Integer</font>, <font name='Mono'>capacity : Integer</font>. "
            "A good designer asks: <i>“What information does the object actually need to fulfil its "
            "responsibilities?”</i> (not <font name='Mono'>everything</font>).")]
    s += FIG("w11_attributes.png", "Figure 5 — Refining attributes")

    s.append(H1("8.  Refining Operations"))
    s += [P("An <b>operation</b> represents something an object can do. The design model makes it "
            "precise: <font name='Mono'>registerCourse(course : Course) : Registration</font> tells the "
            "developer the operation name, the input (a Course) and the return value (a Registration) — "
            "far more useful than a bare <font name='Mono'>register()</font>. That is design "
            "refinement.")]
    s += FIG("w11_operations.png", "Figure 6 — Refining operations")

    # PART E — responsibility-driven design --------------------------------------
    s.append(H1("PART E — RESPONSIBILITY-DRIVEN DESIGN"))
    s.append(H1("9.  Responsibility Assignment"))
    s += [P("A major design question is <i>“Which object should perform a particular operation?”</i> To "
            "check whether a course has space, <font name='Mono'>Course.hasAvailableSpace()</font> is "
            "more logical than <font name='Mono'>Student.checkCourseAvailability()</font>, because "
            "availability is a property of the course. As systems grow, registration may involve "
            "prerequisite checking, timetable conflicts, financial restrictions, capacity and deadlines — "
            "so we introduce a <font name='Mono'>RegistrationService</font> to coordinate the process "
            "across Student, Course and Registration. That is a design decision.")]
    s += FIG("w11_responsibility.png", "Figure 7 — Responsibility assignment")

    # PART F/G — cohesion and coupling -------------------------------------------
    s.append(H1("PART F &amp; G — COHESION AND COUPLING"))
    s.append(H1("10.  Cohesion"))
    s += [P("<b>Cohesion</b> asks how closely related the responsibilities inside a class or component "
            "are. <b>High cohesion</b>: a <font name='Mono'>Course</font> with courseCode, title, "
            "capacity, credits and hasSpace(), addStudent(), removeStudent() — everything about the "
            "course. <b>Low cohesion</b>: a <font name='Mono'>Course</font> that also registers students, "
            "sends email, calculates salary, generates PDFs, compresses images and backs up the "
            "database.")]
    s += FIG("w11_cohesion.png", "Figure 8 — High vs low cohesion")

    s.append(H1("11.  Coupling"))
    s += [P("<b>Coupling</b> describes the degree of dependency between components. High coupling — "
            "Student -> Payment -> Database -> Email -> SMS -> Reports — means changing the database affects "
            "everything. Lower coupling uses an abstraction: "
            "<font name='Mono'>PaymentService</font> depends on a <font name='Mono'>PaymentGateway</font> "
            "interface implemented by Bank and MobileMoney, so the service need not know every "
            "implementation detail.")]
    s += FIG("w11_coupling.png", "Figure 9 — High vs low coupling")

    # PART H — interfaces ---------------------------------------------------------
    s.append(H1("PART H — INTERFACES"))
    s.append(H1("12.  What Is an Interface?"))
    s += [P("An <b>interface</b> is essentially a contract: <i>“Any class implementing me must provide "
            "these operations.”</i> For example <font name='Mono'>&lt;&lt;interface&gt;&gt; "
            "PaymentGateway</font> with <font name='Mono'>processPayment()</font> and "
            "<font name='Mono'>refundPayment()</font>, implemented by both "
            "<font name='Mono'>BankGateway</font> and <font name='Mono'>MobileGateway</font>. "
            "<b>Real-world analogy:</b> a phone charger doesn't care whether electricity came from "
            "hydro, solar, thermal or wind — it cares about the interface (the socket). The application "
            "similarly need not know which concrete payment provider implements the gateway.")]
    s += FIG("w11_interface.png", "Figure 10 — Interfaces: contract and wall-socket analogy")

    # PART I — abstract classes ----------------------------------------------------
    s.append(H1("PART I — ABSTRACT CLASSES"))
    s.append(H1("13.  Abstract Class vs Interface"))
    s += [P("An <b>abstract class</b> is intended to provide common structure/behaviour for subclasses "
            "but is generally not instantiated directly — e.g. <font name='Mono'>Payment</font> (amount, "
            "date, process()) generalises <font name='Mono'>BankPayment</font> and "
            "<font name='Mono'>MobilePayment</font>. The comparison below is a classic examination "
            "area. Exact implementation possibilities depend on the language, so students should not "
            "assume Java, C# and C++ treat these constructs identically.")]
    s += FIG("w11_abstract_vs_interface.png", "Figure 11 — Abstract class vs interface")

    # PART J/K — inheritance and association ----------------------------------------
    s.append(H1("PART J &amp; K — ASSOCIATION VS INHERITANCE"))
    s.append(H1("14.  Association vs Inheritance — the Easy Test"))
    s += [P("<b>Association</b> means objects/classes are related: <i>Student HAS/TAKES Course</i>. "
            "<b>Inheritance</b> means one class is a specialised form of another: <i>Student IS-A "
            "Person</i>. The easy test — <b>HAS / USES / KNOWS / INTERACTS WITH</b> signals association; "
            "<b>IS-A</b> signals inheritance. Never write <font name='Mono'>Student extends Course</font> "
            "just because both are classes: a Student is not a kind of Course.")]
    s += FIG("w11_association_inheritance.png", "Figure 12 — Association vs inheritance")

    # PART L/M — encapsulation and dependencies -------------------------------------
    s.append(H1("PART L &amp; M — ENCAPSULATION, INFORMATION HIDING AND DEPENDENCIES"))
    s.append(H1("15.  Encapsulation and Information Hiding"))
    s += [P("<b>Encapsulation</b> keeps data and the operations that manage it together while "
            "controlling access to internal state. In UML, <font name='Mono'>-balance : Decimal</font> "
            "means private; <font name='Mono'>account.withdraw(500)</font> lets the object enforce rules "
            "(<font name='Mono'>if balance &lt; 500: reject</font>), whereas "
            "<font name='Mono'>account.balance = -500000</font> would let external code corrupt the "
            "state. <b>Information hiding</b> means hiding unnecessary implementation details.")]
    s += FIG("w11_encapsulation.png", "Figure 13 — Encapsulation and information hiding")

    s.append(H1("16.  Dependencies and Dependency Injection"))
    s += [P("A <b>dependency</b> exists when one component relies on another (RegistrationService "
            "depends on CourseRepository). <b>Dependency injection</b> provides the dependency instead "
            "of letting the service construct it — <font name='Mono'>RegistrationService(repository)</font> "
            "— improving testability, flexibility, substitution and maintainability.")]
    s += FIG("w11_dependency.png", "Figure 14 — Dependencies and dependency injection")

    # PART N/O/P/Q — layered design, reuse, change, quality ----------------------------
    s.append(H1("PART N–Q — LAYERS, REUSE, CHANGE AND QUALITY"))
    s.append(H1("17.  Separation of Concerns and Layered Design"))
    s += [P("A <b>concern</b> is a responsibility or area of functionality (authentication, payments, "
            "registration, reporting, notifications). Instead of one "
            "<font name='Mono'>StudentController</font> doing login(), registerCourse(), payFees(), "
            "sendSMS(), generateReport() and calculateResults(), we provide separate services. "
            "<b>Layered design</b> divides the system into logical levels — Presentation, "
            "Application/Service, Domain, Data Access, Database — so that if the web application becomes "
            "a mobile application, the business rules remain usable.")]
    s += FIG("w11_layers.png", "Figure 15 — Layered design")

    s.append(H1("18.  Design for Reuse and Design for Change"))
    s += [P("<b>Reuse</b> means designing software elements so they can be used again — a reusable "
            "<font name='Mono'>AuthenticationService</font> can serve the Student Portal, Staff Portal, "
            "Mobile App and Library System instead of four separate implementations. <b>Design for "
            "change</b> recognises that requirements change: a <font name='Mono'>NotificationService</font> "
            "behind a Notification interface lets you add Email, then SMS, then WhatsApp without "
            "rewriting the Student class.")]
    s += FIG("w11_reuse.png", "Figure 16 — Design for reuse")

    s.append(H1("19.  Judging a Design"))
    s += [P("Ask: is it <b>correct</b> (meets the requirements)? <b>understandable</b>? "
            "<b>maintainable</b>? <b>testable</b>? <b>reusable</b>? <b>flexible</b>? Is it "
            "<b>appropriately coupled</b> (no unnecessary dependencies)? Is it <b>cohesive</b> "
            "(each component has a focused purpose)?")]

    # PART T — traceability -----------------------------------------------------------
    s.append(H1("PART T — DESIGN TRACEABILITY"))
    s.append(H1("20.  Traceability"))
    s += [P("<b>Traceability</b> means being able to follow a requirement through the models into "
            "implementation and testing. Requirement <b>R01</b> (“students must be able to register for "
            "courses”) traces through the Register Course use case, the registration activity and "
            "sequence diagrams, Student/Course/Registration, RegistrationService, "
            "<font name='Mono'>registerCourse()</font> and the automated test — so when someone asks "
            "<i>“Where is R01 implemented?”</i> we can trace it.")]
    s += FIG("w11_traceability.png", "Figure 17 — Design traceability")

    # PART U — integrated case study ----------------------------------------------------
    s.append(H1("PART U — INTEGRATED CASE STUDY"))
    s.append(H1("21.  Online Course Registration — Seven Steps"))
    s += [P("<b>(1) Use case</b> — Student registers for a course. <b>(2) Identify classes</b> — domain "
            "classes Student, Course, Registration; design classes RegistrationService, "
            "AuthenticationService, CourseRepository, RegistrationRepository. <b>(3) Class design</b> — "
            "typed attributes and operations for Student, Course and Registration. <b>(4) Service</b> — "
            "RegistrationService coordinates across Student, Course and Registration. <b>(5) Sequence</b> — "
            "Student -> RegistrationService <font name='Mono'>register()</font> -> Course "
            "<font name='Mono'>hasSpace()</font> / <font name='Mono'>checkPrerequisite()</font> -> "
            "Registration created -> confirmation. <b>(6) State model</b> — Requested -> Validated -> "
            "Confirmed (or Rejected). <b>(7) Architecture</b> — Interface -> Services -> Domain -> "
            "Repositories -> Database.")]
    s += FIG("w11_case_study.png", "Figure 18 — The integrated case study")

    # PART V — mistakes -------------------------------------------------------------------
    s.append(H1("22.  Common Design Mistakes"))
    s += BUL([
        "<b>One giant class</b> (login, payments, registration, results, SMS, reports, database) — low cohesion and high coupling.",
        "<b>Everything inherits from everything</b> — only inherit when a meaningful IS-A relationship exists.",
        "<b>Direct database access everywhere</b> — route through repositories / data access.",
        "<b>Exposing everything</b> (public balance, public password) — undermines encapsulation.",
        "<b>Designing only for today</b> — consider reasonable future change without trying to predict everything.",
    ])

    # practical/tutorial --------------------------------------------------------------------
    s.append(H1("23.  Practical Class and Tutorial"))
    s += [P("<b>Practical (1 hour):</b> model an Online University Course Registration System and "
            "produce (A) a class diagram (Student, Course, Registration, RegistrationService), "
            "(B) a sequence diagram for registering a course, (C) a state diagram for the Registration "
            "lifecycle (Requested, Validated, Confirmed, Rejected, Cancelled), (D) an architecture "
            "diagram, and (E) an explanation of why each class and responsibility exists, where cohesion "
            "is high, where coupling is reduced, and where encapsulation and abstraction are used.")]
    s += BUL([
        "<b>Tutorial Q1</b> — Explain the difference between an analysis class and a design class.",
        "<b>Tutorial Q2</b> — Critique a StudentSystem class (login, register, payFees, sendEmail, sendSMS, generateResults, connectDatabase): cohesion, why, five services, how the redesign improves it.",
        "<b>Tutorial Q3</b> — Explain association vs inheritance using Student, Course and Person.",
        "<b>Tutorial Q4</b> — Why are interfaces useful in OO design? Give a payment-system example.",
    ])

    # summary ---------------------------------------------------------------------------------
    s.append(H1("24.  Week 11 Summary and Key Terms"))
    s.append(DTABLE(
        ["Concept", "Simple explanation"],
        [["Design refinement", "Adding detail to an existing model."],
         ["Design class", "A class detailed enough to support implementation."],
         ["Attribute / operation", "Data/state of an object / something an object can do."],
         ["Responsibility", "What an object knows or does."],
         ["Cohesion", "How closely related responsibilities within a component are."],
         ["Coupling", "How strongly components depend on one another."],
         ["Interface", "A contract for behaviour."],
         ["Abstract class", "A common base abstraction (not directly instantiated)."],
         ["Encapsulation", "Keeping internal state controlled."],
         ["Information hiding", "Hiding unnecessary implementation details."],
         ["Dependency injection", "Providing a dependency instead of constructing it."],
         ["Layering", "Organising software into logical levels."],
         ["Reuse", "Designing components that can be used again."],
         ["Traceability", "Following requirements through models and implementation."]],
        widths=[0.34 * DOC_W, 0.66 * DOC_W]))
    s.append(CALLOUT("THE MOST IMPORTANT IDEA OF WEEK 11",
        ["Drawing a UML class diagram is <b>not</b> the same as completing an OO design. The goal is "
         "not simply to create more diagrams — it is to create a design that is <b>correct, "
         "understandable, maintainable, testable, reusable and adaptable</b>. Path: requirement -> "
         "analysis (Student, Course…) -> refinement (attributes + operations) -> responsibilities -> "
         "interfaces + dependencies -> cohesion + coupling decisions -> architecture -> implementable "
         "design."]))

    # exam ---------------------------------------------------------------------------------------
    s.append(H1("25.  Examination-Style Questions"))
    s += [P("<b>Essay (25 marks).</b> Explain the process of refining an analysis model into an "
            "object-oriented design model, illustrating with an Online Student Registration System. "
            "Discuss analysis classes, design classes, attributes, operations, responsibilities, "
            "relationships, interfaces, cohesion, coupling, encapsulation, architecture and "
            "traceability."),
          P("<b>Essay (20 marks).</b> “A good object-oriented design should have high cohesion and low "
            "coupling.” Discuss this statement using suitable examples."),
          P("<b>Essay (20 marks).</b> Explain the difference between association, inheritance and "
            "interface implementation, using UML examples."),
          P("<b>Scenario (25 marks).</b> A university wants an online payment system supporting bank, "
            "mobile-money and card payments. Design an OO solution that allows new payment methods to be "
            "added with minimal changes — provide a class/interface model, relationships, "
            "responsibilities, and an explanation of coupling and how the design supports reuse and "
            "change.")]

    # references -----------------------------------------------------------------------------------
    s.append(H1("26.  References and Further Reading"))
    s.append(H2("Authoritative / current online sources"))
    s += BUL([
        "Object Management Group (OMG). <i>Unified Modeling Language (UML), Version 2.5.1.</i> OMG.",
        "Noback, M. (2018). <i>Principles of Package Design: Creating Reusable Software Components.</i> Apress/Springer.",
        "Gonzalez, P. (2025). <i>Clean Apex Code: Software Design for Salesforce Developers.</i> Springer — OO design, modularity, coupling, cohesion, testing, dependency injection, maintainability.",
        "<i>Recognising Object-Oriented Software Design Quality: A Practitioner-Based Questionnaire Survey.</i> Software Quality Journal, Springer.",
    ])
    s.append(H2("Prescribed and recommended texts"))
    s += BUL([
        "Mach, E. (2019). <i>Object Oriented Analysis &amp; Design Cookbook: Introduction to Practical System Modeling.</i>",
        "Reddy, V., &amp; Korra, S. (2018). <i>Object-Oriented Analysis and Design Using UML.</i>",
        "The Art of Service. (2021). <i>Object Oriented Analysis and Design: A Complete Guide.</i>",
        "Wixom, B., &amp; Dennis, A. (2018). <i>Systems Analysis and Design.</i>",
        "Blokdyk, G. (2021). <i>Object-Oriented Analysis and Design Standard Requirements.</i>",
    ])

    return s


if __name__ == "__main__":
    print("Built:", build(CFG, story))
