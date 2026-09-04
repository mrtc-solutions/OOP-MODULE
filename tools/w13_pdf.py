"""
Week 13 PDF content — MULTILAYER SYSTEMS, REUSABLE COMPONENTS AND ARCHITECTURAL DESIGN.
"""
from pdfengine import (H1, H2, P, BUL, FIG, CALLOUT, DTABLE, build, DOC_W,
                      C_MAROON, C_SOFT)

CFG = {
    "week": 13,
    "title": "Multilayer Systems, Reusable Components and Architectural Design",
    "filename": "Week13_Module_BICT3202_OOAD.pdf",
}


def story():
    s = []

    # 1. introduction --------------------------------------------------------
    s.append(H1("1.  Week 13 Introduction"))
    s += [P("Week 13 addresses one of the explicit learning outcomes of the syllabus: "
            "<b>“Express the value of designing a multilayer system built of reusable and adaptable "
            "components.”</b> Earlier weeks asked what objects we need, how they behave and how they "
            "interact; Weeks 10–12 turned the analysis into an integrated design. Week 13 now asks a "
            "higher-level question: <b>how should we organise the software so that it is easier to "
            "maintain, reuse, replace and adapt?</b>"),
          P("That leads us to architectural layers, components, interfaces, dependencies, reusable and "
            "adaptable components, separation of concerns, coupling, cohesion, package organisation, "
            "component diagrams and deployment thinking. UML provides structural diagram types — "
            "including class, component, package and deployment diagrams — which are particularly "
            "relevant this week.")]
    s += FIG("w13_progression.png", "Figure 1 — Where Week 13 fits")

    # 2. learning outcomes -----------------------------------------------------
    s.append(H1("2.  Learning Outcomes"))
    s += [P("By the end of this week, a student should be able to:")]
    s += BUL([
        "Explain software architecture in OOAD, and distinguish architecture from class design.",
        "Explain multilayer architecture and identify common software layers.",
        "Explain separation of concerns and the relationship between layers and objects.",
        "Define a software component and explain component interfaces.",
        "Explain reusable and adaptable components.",
        "Explain coupling and cohesion in architectural design and identify inappropriate dependencies.",
        "Draw a basic UML component diagram and explain package organisation.",
        "Explain the benefits and limitations of multilayer architecture, and integrate component/architectural thinking into an OOAD solution.",
    ])

    # PART A — architecture ----------------------------------------------------
    s.append(H1("PART A — WHAT IS SOFTWARE ARCHITECTURE?"))
    s.append(H1("3.  A Simple Question"))
    s += [P("A university tells a programmer: <i>“Build us an online registration system.”</i> The "
            "programmer could create hundreds of classes — but another question remains: <b>how should "
            "those classes be organised?</b> Should the class that displays a web page also validate "
            "passwords, calculate fees, talk directly to the database, send emails and create "
            "registrations? It could be programmed that way, but it would become difficult to understand "
            "and maintain. So OOAD asks not only <i>what objects do we need?</i> but <i>how should those "
            "objects and components be organised?</i>"),
          P("<b>Software architecture</b> is the high-level organisation of a software system, including "
            "its major parts, their responsibilities, relationships and interactions — the overall plan "
            "of the software. <b>Class design</b> asks what classes we need (Student, Course, "
            "Registration, Payment); <b>architecture</b> asks how they should be organised (Presentation "
            "Layer -> Registration Service -> Registration Domain -> Repository -> Database). "
            "<b>Architecture is broader than individual class design.</b>")]
    s += FIG("w13_architecture_vs_class.png", "Figure 2 — Architecture vs class design")

    # PART B — multilayer --------------------------------------------------------
    s.append(H1("PART B — MULTILAYER ARCHITECTURE"))
    s.append(H1("4.  What Is a Layer?"))
    s += [P("A <b>layer</b> is a logical grouping of related responsibilities — think of a school "
            "building: third floor administration, second floor classrooms, first floor library, ground "
            "floor reception. Software can be divided into layers in the same way. A common conceptual "
            "structure is the <b>basic multilayer architecture</b>: <b>Presentation -> Application/Service "
            "-> Domain/Business -> Data Access/Infrastructure -> Database</b>. Understand every layer "
            "rather than simply memorising the names.")]
    s += FIG("w13_layers.png", "Figure 3 — Basic multilayer architecture")

    # PART C — presentation -------------------------------------------------------
    s.append(H1("PART C — THE PRESENTATION LAYER"))
    s.append(H1("5.  Presentation"))
    s += [P("The <b>presentation layer</b> interacts with the user — web pages, mobile screens, desktop "
            "windows, forms, buttons, menus, dashboards. It should primarily <b>display information, "
            "collect user input, do basic formatting, send requests to application services and display "
            "responses</b>. It should not normally contain all the business rules: don't scatter "
            "<font name='Mono'>if course.capacity > registeredStudents</font> throughout every "
            "interface, because a web, Android, iOS and desktop application would each duplicate the same "
            "logic — changing one rule would require changing several applications.")]

    # PART D — application layer ----------------------------------------------------
    s.append(H1("PART D — THE APPLICATION / SERVICE LAYER"))
    s.append(H1("6.  Application Services"))
    s += [P("The <b>application layer</b> coordinates application operations. "
            "<font name='Mono'>RegistrationService</font> provides "
            "<font name='Mono'>registerStudent()</font>, <font name='Mono'>dropCourse()</font> and "
            "<font name='Mono'>getRegisteredCourses()</font>; it receives a request from the presentation "
            "layer and coordinates the necessary objects. When the student clicks <b>Register</b>: Web "
            "Page -> RegistrationController -> RegistrationService -> Course -> Student -> Registration. The "
            "UI does not need to know every internal detail.")]

    # PART E — domain layer ----------------------------------------------------------
    s.append(H1("PART E — THE DOMAIN / BUSINESS LAYER"))
    s.append(H1("7.  Domain and Business Rules"))
    s += [P("The <b>domain layer</b> holds the core business concepts and rules — Student, Course, "
            "Registration, Programme, Semester — plus rules such as <i>“a student cannot register without "
            "satisfying the prerequisite”</i> and <i>“a course cannot accept registrations beyond "
            "capacity.”</i> Centralising the rules matters: if the university changes <i>“maximum 6 "
            "courses”</i> to <i>“maximum 8 courses”</i>, a centralised rule is changed in one place, "
            "whereas a duplicated rule would have to be changed in the website, mobile app, desktop app "
            "and reports.")]
    s += FIG("w13_domain_rules.png", "Figure 4 — Centralised business rules")

    # PART F — data access ------------------------------------------------------------
    s.append(H1("PART F — THE DATA ACCESS LAYER"))
    s.append(H1("8.  Data Access"))
    s += [P("The <b>data access layer</b> handles communication with data storage — "
            "<font name='Mono'>StudentRepository</font>, <font name='Mono'>CourseRepository</font>, "
            "<font name='Mono'>RegistrationRepository</font>. The service asks <i>“give me this "
            "student's registrations”</i> and the repository handles the mechanics. If every class "
            "accessed the database directly (Student -> Database, Course -> Database, Payment -> Database), "
            "changing database technology would affect many classes; routing through repositories "
            "reduces direct dependencies.")]
    s += FIG("w13_data_access.png", "Figure 5 — The data access layer")

    # PART G — complete model -----------------------------------------------------------
    s.append(H1("PART G — THE COMPLETE MULTILAYER MODEL"))
    s += [P("The university registration example: <b>Presentation</b> (Web UI / Mobile UI / Desktop UI) "
            "-> <b>Application</b> (RegistrationService, AuthenticationService, CourseService) -> "
            "<b>Domain</b> (Student, Course, Registration, Programme) -> <b>Data Access</b> "
            "(StudentRepository, CourseRepository, RegistrationRepository) -> <b>Database</b>. This is the "
            "central example of the lecture.")]

    # PART H/I/J — separation, cohesion, coupling -----------------------------------------
    s.append(H1("PART H–J — SEPARATION OF CONCERNS, COHESION AND COUPLING"))
    s.append(H1("9.  Separation of Concerns"))
    s += [P("<b>Separation of concerns</b> means different parts of the system concentrate on different "
            "responsibilities: Presentation -> user interaction; Application -> use-case coordination; "
            "Domain -> business rules; Data Access -> persistence. A single "
            "<font name='Mono'>StudentRegistration.java</font> containing displayHTML(), "
            "validatePassword(), connectDatabase(), calculateFees(), registerCourse(), sendEmail(), "
            "generatePDF() and checkPrerequisite() has too many responsibilities and becomes difficult to "
            "test, modify, reuse and understand. Separate them into StudentController, "
            "RegistrationService, Course, Registration, PaymentService, EmailService and "
            "RegistrationRepository.")]
    s += FIG("w13_separation.png", "Figure 6 — Separation of concerns")

    s.append(H1("10.  Cohesion and Coupling"))
    s += [P("<b>Cohesion</b> asks how closely related the responsibilities within one class or component "
            "are — a RegistrationService containing registration operations is cohesive, while one also "
            "handling payroll, image editing, email and weather forecasting is not. A good class should "
            "have a clear reason for existing. <b>Coupling</b> describes how strongly one element depends "
            "on another — a web page that knows the database technology, table names and SQL is strongly "
            "coupled; routing through RegistrationService -> RegistrationRepository -> Database provides a "
            "cleaner separation. The principle: <b>aim for high cohesion and appropriately low "
            "coupling</b> — “keep related things together and unnecessary dependencies apart.”")]
    s += FIG("w13_cohesion.png", "Figure 7 — Cohesion")
    s += FIG("w13_coupling.png", "Figure 8 — Coupling")

    # PART K — components ----------------------------------------------------------------
    s.append(H1("PART K — WHAT IS A SOFTWARE COMPONENT?"))
    s.append(H1("11.  Component vs Class"))
    s += [P("A <b>software component</b> is a modular part of a system that encapsulates functionality "
            "and interacts with other parts through defined interfaces. A <b>class</b> is a "
            "finer-grained modelling/programming element with attributes, operations and relationships; "
            "a <b>component</b> is a larger modular unit — Student, Course and Registration classes can "
            "collectively contribute to a Registration Component. Think of a car: the engine is a "
            "component, but it contains many parts. A Payment Component may internally contain "
            "PaymentService, Payment, PaymentRepository and PaymentValidator, while the external system "
            "does not need to know every internal class.")]
    s += FIG("w13_component_vs_class.png", "Figure 9 — Component vs class")

    # PART L — interfaces ----------------------------------------------------------------
    s.append(H1("PART L — COMPONENT INTERFACES"))
    s.append(H1("12.  Why Components Need Interfaces"))
    s += [P("The registration system wants <font name='Mono'>processPayment()</font> but doesn't care "
            "whether payment goes through bank, mobile money or card — it cares about the service it can "
            "request. A <b>Payment Interface</b> (<font name='Mono'>processPayment(), "
            "refundPayment()</font>) implemented by MobileMoney, BankGateway and CardGateway lets the "
            "system replace one implementation with another without rewriting every client. If both "
            "MobileMoneyPayment and BankPayment implement PaymentGateway, the application works with the "
            "abstraction — an important OO design principle.")]
    s += FIG("w13_component_interfaces.png", "Figure 10 — Component interfaces")

    # PART M/N — reuse and adaptability ------------------------------------------------------
    s.append(H1("PART M &amp; N — REUSABLE AND ADAPTABLE COMPONENTS"))
    s.append(H1("13.  Reusable Components"))
    s += [P("A <b>reusable component</b> is designed so it can be used in more than one context without "
            "rebuilding it — an <b>Authentication Component</b> (login(), logout(), changePassword(), "
            "resetPassword()) can serve the University Portal, Library System, Student Mobile App and "
            "Staff Portal. Reuse can reduce development effort and duplication, improve consistency, "
            "ease maintenance and speed up development — <b>but reuse is not automatically "
            "beneficial</b>: a component that is extremely difficult to adapt may cost more to reuse than "
            "to rebuild.")]
    s += FIG("w13_reuse.png", "Figure 11 — Reusable components")

    s.append(H1("14.  Adaptable Components"))
    s += [P("An <b>adaptable component</b> can be modified, configured or extended to work in different "
            "situations. An <font name='Mono'>EmailNotification.java</font> hard-coded to Gmail, HTML, a "
            "specific sender and message format must be rewritten when SMS is needed; a "
            "<font name='Mono'>NotificationService</font> with EmailNotification, SMSNotification and "
            "PushNotification can support additional methods more easily.")]
    s += FIG("w13_adaptability.png", "Figure 12 — Adaptable components")

    s.append(H1("15.  Reuse and Inheritance"))
    s += [P("Inheritance is <b>not</b> always the best way to reuse code. “Inheritance means reuse” does "
            "not imply “whenever I want reuse, I should use inheritance.” Inheritance represents an "
            "<b>IS-A</b> relationship (Administrator IS-A User), but RegistrationService IS-A Database "
            "makes no sense. Sometimes <b>composition</b> is better: RegistrationService <i>uses</i> "
            "NotificationService — it isn't a type of notification service. Other reuse approaches "
            "include composition, interfaces, services, libraries, frameworks and configurable "
            "components.")]

    # PART P — component diagram ----------------------------------------------------------------
    s.append(H1("PART P — COMPONENT DIAGRAM"))
    s.append(H1("16.  UML Component Diagrams"))
    s += [P("A <b>UML component diagram</b> shows the organisation and relationships of software "
            "components — OMG identifies it as one of UML's structural diagram types. A simplified "
            "university example: Web Application -> Authentication Component -> Registration Component -> "
            "(Course Component, Notification Component) -> Database Component. Students should learn to "
            "represent the same idea using proper UML component notation in a CASE tool.")]
    s += FIG("w13_component_diagram.png", "Figure 13 — University component diagram")

    # PART Q/R — packages -------------------------------------------------------------------------
    s.append(H1("PART Q &amp; R — PACKAGES AND PACKAGE vs COMPONENT"))
    s.append(H1("17.  Packages"))
    s += [P("A <b>UML package</b> groups related model elements — OMG defines a package as a namespace "
            "that can contain or import model elements. A university system might group elements into "
            "Authentication, Academic, Registration, Finance, Notification and Reporting packages. "
            "<b>Package vs component:</b> a package primarily helps <b>organise</b> model elements "
            "(Academic -> Student, Course, Programme), while a component represents <b>modular "
            "functionality</b> with interfaces (RegistrationComponent). They can be used together — a "
            "package is organisation/grouping; a component is modular functionality.")]
    s += FIG("w13_packages.png", "Figure 14 — Packages")

    # PART S/T — dependencies ------------------------------------------------------------------------
    s.append(H1("PART S &amp; T — DEPENDENCIES AND DEPENDENCY DIRECTION"))
    s.append(H1("18.  Dependencies"))
    s += [P("A <b>dependency</b> exists when one element relies on another — RegistrationService depends "
            "on RegistrationRepository. Too many dependencies (A -> B, C, D, E, F, G) means changing any "
            "of them may affect A. A simple architectural rule is that dependencies should move in a "
            "<b>controlled direction</b>: Presentation -> Application -> Domain -> Infrastructure — not "
            "every part depending on every other part.")]
    s += FIG("w13_dependency_direction.png", "Figure 15 — Dependency direction")

    # PART U/V — benefits and limitations ---------------------------------------------------------------
    s.append(H1("PART U &amp; V — BENEFITS AND LIMITATIONS OF MULTILAYER ARCHITECTURE"))
    s.append(H1("19.  Why Multilayer Architecture Matters"))
    s += BUL([
        "<b>Maintainability</b> — change the UI without rewriting the business layer.",
        "<b>Reuse</b> — one service supports web, mobile and desktop.",
        "<b>Testability</b> — test a service without clicking through a graphical interface.",
        "<b>Adaptability</b> — swap MySQL for PostgreSQL at the data-access boundary.",
        "<b>Team development</b> — separate teams per layer with clear boundaries.",
    ])
    s += FIG("w13_benefits.png", "Figure 16 — Benefits of multilayer architecture")

    s.append(H1("20.  Limitations — More Layers Is Not Always Better"))
    s += BUL([
        "<b>Additional complexity</b> — Controller -> Service -> Domain -> Repository -> Database introduces abstractions.",
        "<b>Performance overhead</b> — extra abstractions or network boundaries can cost time.",
        "<b>Overengineering</b> — a tiny app may not need 15 layers, 40 interfaces and 100 packages.",
        "<b>Incorrect layer responsibilities</b> — business logic scattered into controllers, repositories and UI looks layered but is poorly designed.",
    ])
    s += FIG("w13_limitations.png", "Figure 17 — Limitations of multilayer architecture")

    # PART W/X — case studies -----------------------------------------------------------------------------
    s.append(H1("PART W &amp; X — REUSE AND ADAPTABILITY CASE STUDIES"))
    s.append(H1("21.  Component Reuse and Adaptability"))
    s += [P("<b>Reuse case study:</b> a university with a Registration, Notification, Authentication and "
            "Payment component later develops a mobile application — instead of rebuilding "
            "authentication, notification and payment from scratch, the mobile app interacts with the "
            "existing shared services. <b>Adaptability case study:</b> the university wants to notify "
            "students on successful registration — initially email, then SMS, then mobile push; a rigid "
            "architecture requires major changes, while an adaptable Notification abstraction "
            "(Email, SMS, Push) lets the application call <font name='Mono'>notifyStudent()</font> "
            "without being tied to one technology.")]

    # PART Y/Z — component diagram exercise and notation ----------------------------------------------------
    s.append(H1("PART Y &amp; Z — COMPONENT DIAGRAM EXERCISE AND NOTATION"))
    s.append(H1("22.  Exercise and Notation"))
    s += [P("<b>Exercise:</b> model an Online Banking System with components Customer Interface, "
            "Authentication, Account Management, Transaction, Payment, Notification and Database. "
            "Important component-diagram elements to become familiar with: <b>component, interface, "
            "provided interface, required interface, dependency, connector, port</b>. The point is not "
            "merely drawing the interface but understanding <i>what functionality one component offers "
            "and what functionality another component requires</i>.")]

    # PART AB — deployment -----------------------------------------------------------------------------------
    s.append(H1("PART AB — DEPLOYMENT THINKING"))
    s.append(H1("23.  Logical vs Deployment Architecture"))
    s += [P("<b>Logical architecture</b> describes how software is organised; <b>deployment "
            "architecture</b> describes where software executes. Example: Student's Phone (Mobile "
            "Application) -> Internet -> Application Server (Registration Service, Authentication) -> "
            "Database Server (University Database). A <b>UML deployment diagram</b> represents the "
            "runtime arrangement of software artifacts on nodes.")]
    s += FIG("w13_deployment.png", "Figure 18 — Deployment thinking")

    # PART AC/AD — reusability principles ----------------------------------------------------------------------
    s.append(H1("PART AC &amp; AD — REUSABILITY DESIGN PRINCIPLES"))
    s.append(H1("24.  Principles and a Warning"))
    s += BUL([
        "<b>Clear interfaces</b> — a component is easier to reuse through a well-defined interface.",
        "<b>Minimise unnecessary dependencies</b> — don't couple a component to one specific application.",
        "<b>Encapsulation</b> — expose processPayment() while hiding databaseConnection(), APIKeyHandling() and retryLogic().",
        "<b>Configuration</b> — make components configurable (channel = SMS) rather than hard-coded.",
    ])
    s += [P("<b>Warning:</b> a component should not be made reusable simply because “reusable is always "
            "better.” Spending three weeks turning a SmallCalculator into a huge framework may be "
            "unnecessary. Good design considers current requirements, likely changes, maintenance cost, "
            "complexity and reuse opportunities — <b>design for appropriate reuse, not reuse at any "
            "cost.</b>")]

    # tutorial / practical ---------------------------------------------------------------------------------------
    s.append(H1("25.  Tutorial and Practical"))
    s += [P("<b>Tutorial 1</b> — classify each activity into a layer (Student clicks Register -> "
            "Presentation; RegistrationService -> Application; Course business rule -> Domain; "
            "CourseRepository -> Data Access; Database storage -> Database; confirmation display -> "
            "Presentation). <b>Tutorial 2</b> — critique a StudentController containing HTML, SQL, "
            "password validation, registration, email, fees and PDFs: what is wrong, is cohesion high or "
            "low, which responsibilities should move, propose a better architecture. <b>Tutorial 3</b> — "
            "discuss the advantages and disadvantages of a shared authentication component/service for "
            "the web, mobile and desktop applications."),
          P("<b>Practical (1 hour):</b> extend the Week 12 system — (A) package diagram (Authentication, "
            "Academic, Registration, Finance, Notification); (B) component diagram (Web Application, "
            "Mobile Application, Authentication, Registration, Payment, Notification, Database with "
            "relationships); (C) layered architecture (Presentation, Application, Domain, Data Access, "
            "Database); (D) identify three reusable components and explain why; (E) explain how the "
            "system changes if a mobile application is introduced.")]

    # misunderstandings ---------------------------------------------------------------------------------------------
    s.append(H1("26.  Common Student Confusions"))
    s += BUL([
        "<b>Layer vs component</b> — a layer is a logical architectural level; a component is a modular software unit (the Domain Layer may contain Student, Course and Registration components).",
        "<b>Component vs class</b> — a class is a finer-grained building block; a component is a larger modular unit.",
        "<b>Package vs layer</b> — a package is an organisational namespace; a layer is an architectural separation by responsibility.",
        "<b>Reuse vs inheritance</b> — inheritance can support reuse, but reuse does not require it (composition, interfaces, services, libraries, frameworks).",
        "<b>High cohesion vs low coupling</b> — “keep related things together and unnecessary dependencies apart.”",
    ])

    # summary -----------------------------------------------------------------------------------------------------------
    s.append(H1("27.  Week 13 Summary"))
    s.append(DTABLE(
        ["Concept", "Simple meaning"],
        [["Software architecture", "High-level organisation of a software system."],
         ["Layer", "Logical grouping of related responsibilities."],
         ["Presentation / Application", "User interaction / use-case coordination."],
         ["Domain / Data access", "Business rules / persistence."],
         ["Separation of concerns", "Different parts handle different responsibilities."],
         ["Component", "Modular unit encapsulating functionality behind interfaces."],
         ["Component interface", "The contract through which a component is used."],
         ["Reusable component", "Designed for use in more than one context."],
         ["Adaptable component", "Can be configured or extended for new situations."],
         ["Package", "Organisational namespace/grouping of model elements."],
         ["Dependency", "One element relying on another."],
         ["Deployment", "Where the software actually executes."]],
        widths=[0.36 * DOC_W, 0.64 * DOC_W]))
    s.append(CALLOUT("THE CORE MESSAGE",
        ["A good OO designer does not simply produce many UML diagrams. The designer decides how "
         "<b>responsibilities, objects, components and layers</b> should work together, while keeping the "
         "system <b>understandable, reusable, adaptable and maintainable</b>. Aim for <b>high cohesion "
         "and appropriately low coupling</b>; design components for <b>appropriate reuse</b>, not reuse "
         "at any cost; and let <b>architecture match the problem</b>."]))

    # exam -----------------------------------------------------------------------------------------------------------------
    s.append(H1("28.  Examination-Style Questions"))
    s += [P("<b>Essay (25 marks).</b> Explain multilayer architecture in object-oriented design. Using a "
            "University Course Registration System, describe the responsibilities of the Presentation, "
            "Application, Domain and Data Access layers."),
          P("<b>Essay (20 marks).</b> Differentiate a UML package from a UML component, and explain how "
            "both are used when designing a large object-oriented system."),
          P("<b>Essay (25 marks).</b> A company's user interface directly accesses the database and "
            "contains most of the business rules. (a) Identify four problems. (b) Propose a multilayer "
            "architecture. (c) Explain how it improves maintainability and reuse."),
          P("<b>Scenario (30 marks).</b> Design a component-oriented architecture for an online banking "
            "system: major components, responsibilities, interfaces and dependencies, and explain how "
            "the design promotes reuse and adaptability.")]

    # references ---------------------------------------------------------------------------------------------------------------
    s.append(H1("29.  References and Further Reading"))
    s.append(H2("Authoritative / current online sources"))
    s += BUL([
        "Object Management Group (OMG). <i>Unified Modeling Language (UML), Version 2.5.1.</i> OMG — the current formal UML specification.",
        "Object Management Group (OMG). <i>What is UML?</i> Overview of UML structural, behavioural and interaction diagrams.",
        "Microsoft Support. <i>UML diagrams in Visio.</i> Guidance covering class, component, deployment, sequence, activity and state-machine diagrams.",
        "Microsoft Support. <i>Create a UML deployment diagram.</i> Deployment diagrams and the runtime arrangement of software artifacts.",
        "Sparx Systems. <i>Enterprise Architect UML Package Documentation.</i> UML packages and their role in organising model elements.",
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
