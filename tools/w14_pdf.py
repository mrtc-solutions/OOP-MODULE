"""
Week 14 PDF content — INTEGRATING OBJECT, DYNAMIC AND BEHAVIOURAL MODELS INTO OOD.
"""
from pdfengine import (H1, H2, P, BUL, FIG, CALLOUT, DTABLE, build, DOC_W,
                      C_MAROON, C_SOFT)

CFG = {
    "week": 14,
    "title": "Integrating Object, Dynamic and Behavioural Models into Object-Oriented Design",
    "filename": "Week14_Module_BICT3202_OOAD.pdf",
}


def story():
    s = []

    # 1. introduction --------------------------------------------------------
    s.append(H1("1.  Week 14 Introduction"))
    s += [P("Students have travelled a long way: from <i>what problem does the organisation have?</i> "
            "through <i>what objects exist, how do they relate, behave and interact?</i> to Week 13's "
            "<i>how should the software be organised into layers and components?</i> Week 14 now reaches "
            "a critical question: <b>how do we combine all these models into one coherent software "
            "design?</b>"),
          P("The official UML specification treats structural modelling, behavioural modelling, use "
            "cases, deployments and related modelling concepts as parts of the same overall modelling "
            "language — so students should not think of UML diagrams as independent drawings. "
            "<b>Each diagram provides a different view of the same system.</b>")]
    s += FIG("w14_progression.png", "Figure 1 — Week 13 → Week 14")

    # 2. learning outcomes -----------------------------------------------------
    s.append(H1("2.  Learning Outcomes"))
    s += [P("By the end of this week, a student should be able to:")]
    s += BUL([
        "Define object-oriented design and explain the difference between analysis and design.",
        "Explain why analysis models must be transformed into design models.",
        "Explain design classes and identify their responsibilities.",
        "Assign operations to appropriate classes and explain attributes vs operations.",
        "Integrate the object model with the dynamic model and with behavioural models.",
        "Trace a requirement from a use case to classes and operations.",
        "Use sequence, state and activity diagrams to refine class responsibilities.",
        "Identify design inconsistencies and refine an analysis model into a design model.",
    ])

    # PART A — what is OOD -------------------------------------------------------
    s.append(H1("PART A — WHAT IS OBJECT-ORIENTED DESIGN?"))
    s.append(H1("3.  Analysis vs Design"))
    s += [P("<b>Object-oriented design (OOD)</b> is the process of transforming the understanding of a "
            "system developed during analysis into a detailed design that can guide implementation. "
            "<b>Analysis tells us what the system needs and what exists; design decides how the software "
            "will actually be organised to provide it.</b> If someone tells an architect <i>“I need a "
            "house with three bedrooms, a kitchen, two bathrooms and a garage”</i>, that is requirements "
            "and analysis; the architect then decides where rooms, doors, electricity and pipes go and "
            "what materials are needed — that is design."),
          P("Given <i>“a student must register for a course”</i>, analysis identifies Student, Course "
            "and Registration; design introduces RegistrationController, RegistrationService, "
            "RegistrationRepository and RegistrationValidator. The design is more "
            "implementation-oriented.")]
    s += FIG("w14_analysis_vs_design.png", "Figure 2 — Analysis vs design")

    s.append(H1("4.  Analysis Model → Design Model"))
    s += [P("Requirements → Use cases → Analysis model → Design decisions → Design model → "
            "Implementation. The important point: <b>we should not randomly invent design classes</b> — "
            "they should be justified by the requirements and analysis.")]
    s += FIG("w14_transformation.png", "Figure 3 — Analysis → design transformation")

    # PART B — the three models ----------------------------------------------------
    s.append(H1("PART B — THE THREE MAJOR MODELS"))
    s.append(H1("5.  Object, Dynamic and Behavioural Models"))
    s += [P("The <b>object model</b> describes the structural/static view — what things exist and how "
            "they relate (classes, objects, attributes, operations, associations, generalisation, "
            "aggregation/composition). The <b>dynamic model</b> focuses on how objects behave and change "
            "over time — Course: Available → Full → Closed, with events such as “student registers” or "
            "“course reaches capacity.” The <b>behavioural model</b> focuses on what the system does from "
            "the users' perspective — use cases, use-case diagrams, sequence diagrams, communication "
            "diagrams and activity diagrams."),
          P("<b>Why do we need all three?</b> A class diagram alone tells us the structure but not what "
            "happens when a student registers; a sequence diagram shows the interaction; a state model "
            "shows state-dependent behaviour. <b>Different UML models answer different questions.</b>")]
    s += FIG("w14_three_models.png", "Figure 4 — The three major models")

    # PART C — one system, multiple views ---------------------------------------------
    s.append(H1("PART C — ONE SYSTEM, MULTIPLE VIEWS"))
    s.append(H1("6.  Six Views of One System"))
    s += [P("Modelling a University Course Registration System: the <b>use-case diagram</b> tells who "
            "uses the system and what they want; the <b>class diagram</b> tells what structural elements "
            "exist; the <b>sequence diagram</b> tells how objects interact in a scenario; the "
            "<b>activity diagram</b> tells how a workflow progresses; the <b>state machine</b> tells how "
            "an object changes state; the <b>component diagram</b> tells how functionality is "
            "modularised. These are not six unrelated systems — they are six views of one system.")]
    s += FIG("w14_multiple_views.png", "Figure 5 — One system, multiple views")

    # PART D — use case to design ---------------------------------------------------------
    s.append(H1("PART D — FROM USE CASE TO DESIGN"))
    s.append(H1("7.  The Basic Use-Case Flow and Candidate Classes"))
    s += [P("For <b>Register for Course</b> (actor Student): (1) student logs in; (2) selects a course; "
            "(3) system checks the course exists; (4) checks prerequisites; (5) checks capacity; "
            "(6) creates registration; (7) confirms. From this we identify the domain classes Student, "
            "Course and Registration, plus the design classes RegistrationController, "
            "RegistrationService, CourseRepository and RegistrationRepository. The designer asks: "
            "<b>which objects should perform these responsibilities?</b>")]
    s += FIG("w14_use_case_flow.png", "Figure 6 — From use case to design")

    # PART E — responsibility assignment -----------------------------------------------------
    s.append(H1("PART E — RESPONSIBILITY ASSIGNMENT"))
    s.append(H1("8.  Knowing and Doing"))
    s += [P("A <b>responsibility</b> is something a class is responsible for <b>knowing</b> (Student "
            "knows studentId, name, programme; Course knows courseCode, courseName, capacity) or "
            "<b>doing</b> (Course checks whether space is available). A Student class that also does "
            "registerAnyCourse(), calculateCourseCapacity(), sendEmail(), generatePaymentReceipt() and "
            "connectToDatabase() has poor cohesion — a better assignment routes through "
            "RegistrationService → Course → RegistrationRepository so each class has a focused "
            "purpose.")]
    s += FIG("w14_responsibility.png", "Figure 7 — Responsibility assignment")

    # PART F/G — design classes and visibility ------------------------------------------------
    s.append(H1("PART F &amp; G — DESIGN CLASSES AND VISIBILITY"))
    s.append(H1("9.  Analysis Class → Design Class"))
    s += [P("A <b>design class</b> is defined with sufficient detail to support implementation: precise "
            "attributes, data types, operations, parameter types, return types, visibility, "
            "relationships, interfaces and dependencies. The analysis class "
            "<font name='Mono'>Student (name, email, register())</font> becomes "
            "<font name='Mono'>Student { -studentId: String; -name: String; -email: String; "
            "-programme: Programme; +register(course: Course): Registration; +drop(course: Course): "
            "void }</font>.")]
    s += FIG("w14_design_class.png", "Figure 8 — Analysis class → design class")

    s.append(H1("10.  Visibility"))
    s += [P("Common UML visibility: <font name='Mono'>+</font> public, <font name='Mono'>-</font> "
            "private, <font name='Mono'>#</font> protected, <font name='Mono'>~</font> package "
            "visibility — e.g. <font name='Mono'>-studentId : String</font> and "
            "<font name='Mono'>+getName() : String</font>.")]
    s += FIG("w14_visibility.png", "Figure 9 — Visibility symbols")

    # PART H — attributes and operations -----------------------------------------------------------
    s.append(H1("PART H — ATTRIBUTES AND OPERATIONS"))
    s += [P("<b>Attributes</b> describe what an object knows (studentId, name, email, dateOfBirth); "
            "<b>operations</b> describe what it can do (register(), dropCourse(), viewCourses()). A "
            "BankAccount has attributes <font name='Mono'>-accountNumber : String</font> and "
            "<font name='Mono'>-balance : Decimal</font> and operations "
            "<font name='Mono'>+deposit(amount): void</font>, <font name='Mono'>+withdraw(amount): "
            "boolean</font>, <font name='Mono'>+getBalance(): Decimal</font> — attributes store "
            "information, operations perform actions.")]

    # PART I — sequence -> class ----------------------------------------------------------------
    s.append(H1("PART I — SEQUENCE DIAGRAM → CLASS DESIGN"))
    s.append(H1("11.  From Messages to Operations"))
    s += [P("A sequence diagram is not only for presentation — it helps discover <b>which objects need "
            "which operations</b>. If the sequence shows Course → checkCapacity(), the Course class "
            "should probably have <font name='Mono'>checkCapacity()</font>; if RegistrationService → "
            "registerStudent(), then <font name='Mono'>registerStudent()</font> is required. "
            "<b>Messages in interaction diagrams can help refine operations in the class model.</b>")]
    s += FIG("w14_sequence_to_class.png", "Figure 10 — Sequence diagram → class design")

    # PART J — consistency ------------------------------------------------------------------------
    s.append(H1("PART J — MODEL CONSISTENCY"))
    s.append(H1("12.  Making the Diagrams Agree"))
    s += [P("<b>Model consistency</b> means the diagrams agree. If the class diagram says "
            "<font name='Mono'>Course.checkCapacity()</font> but the sequence diagram says "
            "<font name='Mono'>Course.verifyCapacity()</font>, there is an inconsistency to resolve. "
            "Likewise, if the class model says <font name='Mono'>register()</font> and the sequence says "
            "<font name='Mono'>enrol()</font>, the team must decide whether these are the same operation "
            "and standardise the terminology. Models should be cross-checked.")]
    s += FIG("w14_consistency.png", "Figure 11 — Model consistency")

    # PART K/L — integrating object + dynamic + activity ---------------------------------------------
    s.append(H1("PART K &amp; L — INTEGRATING THE MODELS"))
    s.append(H1("13.  Object Model + Dynamic Model"))
    s += [P("The class diagram shows the structure (Course with capacity, status, registerStudent()); "
            "the state machine shows Available → Full → Closed. Connecting them: "
            "<font name='Mono'>registerStudent()</font> may cause Available → Full when the final seat "
            "is taken (e.g. capacity 50, registrations 49 → 50). "
            "<b>The operation has a relationship with the object's state.</b>")]
    s += FIG("w14_object_dynamic.png", "Figure 12 — Object model + dynamic model")

    s.append(H1("14.  Object Model + Activity Model"))
    s += [P("Given the registration workflow, ask <i>which objects perform these activities?</i> — "
            "Select course → RegistrationController; Check prerequisite → Course/RegistrationService; "
            "Check capacity → Course; Create registration → RegistrationService; Save registration → "
            "RegistrationRepository; Send confirmation → NotificationService. This transforms a "
            "behavioural model into design responsibilities.")]
    s += FIG("w14_activity_mapping.png", "Figure 13 — Activity → responsibility mapping")

    # PART M/N — use case model + traceability ---------------------------------------------------------
    s.append(H1("PART M &amp; N — USE CASE MODEL AND TRACEABILITY"))
    s.append(H1("15.  Use Case → Scenario → Sequence → Responsibilities → Operations → Design Classes"))
    s += [P("The use case tells what the user wants; the class model tells what objects are available; "
            "the sequence diagram tells how those objects cooperate. This gives one of the most useful "
            "workflows in OOAD. <b>Traceability</b> follows a requirement through the process: "
            "requirement (“students must register for courses”) → use case (Register for Course) → "
            "sequence (Student → RegistrationService → Course → RegistrationRepository) → classes → "
            "operations (registerCourse(), checkCapacity(), checkPrerequisite(), saveRegistration()) → "
            "code.")]

    # PART O/P/Q — controller, service, domain knowledge ------------------------------------------------
    s.append(H1("PART O–Q — CONTROLLER, SERVICE AND DOMAIN KNOWLEDGE"))
    s.append(H1("16.  The Controller, the Service and the Domain Object"))
    s += [P("A <b>controller</b> coordinates a system operation initiated by an external actor — "
            "RegistrationController receives <font name='Mono'>registerCourse(studentId, courseId)</font> "
            "and coordinates the process. A controller does <b>not</b> mean “do everything” — it must not "
            "become a God class checking the database, calculating fees, applying rules, creating HTML "
            "and sending SMS; it coordinates RegistrationService → (Course, Repository) instead."),
          P("A <b>service</b> provides an application capability — RegistrationService with "
            "registerStudent(), dropStudent(), getRegistration() — coordinating check prerequisite → "
            "check capacity → create Registration → save → send confirmation. "
            "<b>Domain objects should contain domain knowledge:</b> rather than scattering the "
            "capacity rule throughout the UI, give Course <font name='Mono'>isAvailable()</font> and "
            "<font name='Mono'>hasCapacity()</font> — assigning responsibilities to the object that has "
            "the information needed to perform them.")]
    s += FIG("w14_controller.png", "Figure 14 — Controller vs God class")
    s += FIG("w14_domain_knowledge.png", "Figure 15 — Domain knowledge")

    # PART R/S — refinement and change ----------------------------------------------------------------
    s.append(H1("PART R &amp; S — DESIGN REFINEMENT AND DESIGN FOR CHANGE"))
    s.append(H1("17.  Refinement and Change"))
    s += [P("<b>Design refinement</b>: the design model is often richer than the analysis model — "
            "Student, Course, Registration become Student, RegistrationController, RegistrationService, "
            "Course, Registration, CourseRepository, RegistrationRepository and NotificationService. "
            "Adding classes is not a sign the analysis was wrong; implementation introduces technical "
            "responsibilities (e.g. “save registration” → RegistrationRepository) that were not obvious "
            "during early analysis."),
          P("<b>Designing for change</b>: ask <i>what is likely to change?</i> — database, payment "
            "provider, notification channel, user interface, external API — while the core concepts of "
            "Student, Course and registration rules are less likely to change. Put boundaries around the "
            "likely changes: instead of RegistrationService → AirtelMoneyAPI, use RegistrationService → "
            "PaymentGateway → (Provider A, Provider B).")]
    s += FIG("w14_design_change.png", "Figure 16 — Designing for change")

    # PART T — design patterns ----------------------------------------------------------------
    s.append(H1("PART T — DESIGN PATTERNS (outline)"))
    s.append(H1("18.  The Strategy Pattern"))
    s += [P("A <b>design pattern</b> is a reusable solution structure for a recurring design problem — "
            "a proven way of organising a solution, not simply code to copy. The <b>Strategy "
            "pattern</b>: instead of chaining <font name='Mono'>if payment == mobile money / else if "
            "bank / else if card</font> everywhere, define a common abstraction "
            "<font name='Mono'>PaymentStrategy</font> with MobileMoneyPayment, BankPayment and "
            "CardPayment — the system works with the abstraction. <b>Warning:</b> patterns should be "
            "used when they solve an actual recurring problem; otherwise the pattern itself becomes "
            "unnecessary complexity.")]
    s += FIG("w14_strategy.png", "Figure 17 — The Strategy pattern")

    # PART U — integrated case study --------------------------------------------------------------
    s.append(H1("PART U — INTEGRATED CASE STUDY"))
    s.append(H1("19.  University Course Registration"))
    s += [P("Requirement: students must register for available courses. <b>Use case:</b> Register for "
            "Course. <b>Analysis classes:</b> Student — registers → Registration — for → Course. "
            "<b>Sequence:</b> Student → RegistrationController → RegistrationService → "
            "checkCapacity() → Course → create → Registration → save → RegistrationRepository. "
            "<b>Dynamic model:</b> Course Available → Full → Closed. <b>Activity:</b> select course → "
            "check prerequisite → check capacity → [available?] → create → save → send confirmation. "
            "<b>Design model:</b> RegistrationController (+registerCourse()) → RegistrationService "
            "(+registerStudent(), +dropCourse()) → Course (capacity, status, isAvailable()) and "
            "Registration (date, status, confirm()) → RegistrationRepository (+save(), +find()). "
            "<b>That is what it means to integrate the models.</b>")]
    s += FIG("w14_integrated_design.png", "Figure 18 — The integrated design model")

    # PART V — validation --------------------------------------------------------------
    s.append(H1("PART V — MODEL VALIDATION"))
    s.append(H1("20.  How Do We Know Our Models Are Correct?"))
    s += BUL([
        "Does every important use case have supporting classes?",
        "Does every important sequence message correspond to an operation?",
        "Do operations belong to sensible classes?",
        "Do state changes correspond to actual events or operations?",
        "Do activity flows agree with use-case descriptions?",
        "Do class relationships support the required interactions?",
        "Are there duplicated responsibilities, or any class doing too much?",
    ])
    s += [P("<b>Example of inconsistency:</b> the use case says “students can drop courses”, but no "
            "class has a drop operation — introduce <font name='Mono'>RegistrationService.dropCourse()"
            "</font>.")]

    # PART W — quality checklist --------------------------------------------------------------
    s.append(H1("PART W — DESIGN QUALITY CHECKLIST"))
    s += BUL([
        "<b>Structure</b> — classes clearly identified, meaningful relationships, appropriate responsibilities.",
        "<b>Behaviour</b> — sequence diagrams and state transitions make sense; important events represented.",
        "<b>Requirements</b> — every major requirement traces to the design.",
        "<b>Architecture</b> — layers clearly separated; dependencies controlled.",
        "<b>Reuse / adaptability / maintainability</b> — appropriate components reusable; likely changes accommodated; system understandable.",
    ])

    # PART X — mistakes --------------------------------------------------------------
    s.append(H1("21.  Common Student Mistakes"))
    s += BUL([
        "<b>Treating UML diagrams as independent drawings</b> — the sequence diagram should explain how the classes from the class model cooperate.",
        "<b>Putting every operation into one class</b> — a System class doing login(), register(), pay(), sendEmail()… is poor responsibility assignment.",
        "<b>Confusing analysis and design</b> — analysis says Student needs to register; design says the controller receives the request and the service coordinates it.",
        "<b>Adding classes without justification</b> — Manager, Helper, Processor, Utility must have an explained responsibility.",
        "<b>Ignoring consistency</b> — register() vs enrolStudent() must be reconciled.",
    ])

    # tutorial/practical --------------------------------------------------------------
    s.append(H1("22.  Tutorial and Practical"))
    s += [P("<b>Tutorial 1</b> — for “a student selects a course; the system checks prerequisites and "
            "capacity; a registration record is created and confirmation sent”, identify actors, the use "
            "case, analysis classes, design classes, operations, the sequence of interactions and course "
            "states. <b>Tutorial 2</b> — given a class model (Student, Course, Registration), a sequence "
            "message (RegistrationService → verifyPrerequisite()) and a state model (Course Available → "
            "Full), state what changes make the models consistent. <b>Tutorial 3</b> — redesign a "
            "Student class doing registerCourse(), sendEmail(), saveToDatabase(), calculateFees(), "
            "checkCourseCapacity() and generateReport()."),
          P("<b>Practical (1 hour):</b> produce an integrated design package for the University Course "
            "Registration System — refine the class diagram (attributes, types, operations, visibility, "
            "relationships); a sequence diagram (Student, RegistrationController, RegistrationService, "
            "Course, Registration, RegistrationRepository); a state model for Course (Created → "
            "Available → Full → Closed); an activity diagram; and cross-check at least three "
            "consistency relationships (sequence message → operation, state transition → event, "
            "activity → responsibility, use case → design classes).")]

    # summary --------------------------------------------------------------
    s.append(H1("23.  Week 14 Summary and Key Terms"))
    s.append(DTABLE(
        ["Concept", "Simple meaning", "Example"],
        [["Analysis / design", "Understand the problem / decide how to implement", "Student needs registration / RegistrationService"],
         ["Object model", "What exists", "Student, Course"],
         ["Dynamic model", "How things change", "Available → Full"],
         ["Behavioural model", "What the system does / interactions", "Register Course"],
         ["Responsibility", "What a class knows/does", "Course checks capacity"],
         ["Attribute / operation", "Information held / action performed", "courseCode / register()"],
         ["Controller", "Coordinates a request", "RegistrationController"],
         ["Service", "Provides an application capability", "RegistrationService"],
         ["Repository", "Handles persistence", "CourseRepository"],
         ["Traceability", "Follow requirement through design", "Requirement → Code"],
         ["Model consistency", "Diagrams agree", "sequence message matches operation"]],
        widths=[0.28 * DOC_W, 0.4 * DOC_W, 0.32 * DOC_W]))
    s.append(CALLOUT("THE MOST IMPORTANT CONCEPT TO TAKE HOME",
        ["Requirement → “Student registers” → use case “Register for Course” → scenario → sequence "
         "diagram → class model → responsibilities → design classes → component/architecture → "
         "implementation. Alongside: <b>class model ↔ dynamic model ↔ behavioural model</b> — the models "
         "must <b>support one another, not contradict one another</b>. That is the central lesson of "
         "Week 14."]))

    # exam --------------------------------------------------------------
    s.append(H1("24.  Examination-Style Questions"))
    s += [P("<b>Essay (20 marks).</b> Define object-oriented design and explain how it differs from "
            "object-oriented analysis, using a University Course Registration System."),
          P("<b>Essay (25 marks).</b> Explain how a sequence diagram can be used to identify and refine "
            "operations in a class diagram, with a practical example."),
          P("<b>Essay (25 marks).</b> Explain how the object, dynamic and behavioural models complement "
            "one another during object-oriented design."),
          P("<b>Scenario (30 marks).</b> A university wants an online course registration system: a "
            "student selects a course, the system verifies prerequisites and capacity, creates a "
            "registration record and sends confirmation. Identify (a) the relevant classes, (b) their "
            "responsibilities, (c) major operations, (d) object interactions, (e) relevant course "
            "states, and (f) how the UML models remain consistent.")]

    # references --------------------------------------------------------------
    s.append(H1("25.  References and Further Reading"))
    s.append(H2("Primary standards"))
    s += BUL([
        "Object Management Group (OMG). <i>Unified Modeling Language (UML), Version 2.5.1.</i> OMG — the formal UML specification.",
        "Object Management Group (OMG). <i>Introduction to OMG Specifications.</i> Overview of UML diagram categories: class, component, deployment, use-case, sequence, statechart, activity and package diagrams.",
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
