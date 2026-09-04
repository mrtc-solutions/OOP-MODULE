"""
Week 12 PDF content — INTEGRATED OBJECT-ORIENTED MODELLING AND DESIGN.
"""
from pdfengine import (H1, H2, P, BUL, FIG, CALLOUT, DTABLE, build, DOC_W,
                      C_MAROON, C_SOFT)

CFG = {
    "week": 12,
    "title": "Integrated Object-Oriented Modelling and Design",
    "filename": "Week12_Module_BICT3202_OOAD.pdf",
}


def story():
    s = []

    # 1. introduction --------------------------------------------------------
    s.append(H1("1.  Week 12 Introduction"))
    s += [P("Week 10 asked <i>“What does it mean to move from analysis into design?”</i> Week 11 asked "
            "<i>“How do we make our analysis models detailed enough for implementation?”</i> Week 12 now "
            "asks the next question: <b>“How do we bring all these different models together into ONE "
            "coherent system design?”</b>"),
          P("A real OOAD project does not consist of a class diagram sitting separately from a use-case "
            "diagram, sequence diagram and state diagram. They should describe the <b>same system from "
            "different perspectives</b>. UML is specifically intended for visualising, specifying and "
            "documenting software and systems, and the current formal UML specification listed by OMG is "
            "UML 2.5.1.")]
    s += FIG("w12_progression.png", "Figure 1 — Week 11 -> 12 -> 13 progression")

    # 2. learning outcomes -----------------------------------------------------
    s.append(H1("2.  Learning Outcomes"))
    s += [P("By the end of this week, a student should be able to:")]
    s += BUL([
        "Explain the meaning of integrated modelling and why models must be consistent.",
        "Explain the relationship between the use-case, class, interaction, state and activity models.",
        "Trace a requirement from use cases through classes, interactions and operations.",
        "Apply multiplicity and packages to organise and detail a model.",
        "Think at component and architecture level.",
        "Detect contradictions between models and validate a design against its requirements.",
        "Distinguish a model from a diagram.",
        "Build a complete integrated UML model for a realistic system.",
    ])

    # PART A — integrated modelling --------------------------------------------
    s.append(H1("PART A — WHAT IS INTEGRATED MODELLING?"))
    s.append(H1("3.  Meaning of Integrated Modelling"))
    s += [P("Building a house requires an architectural drawing, an electrical plan, a plumbing plan and "
            "a structural plan. Each shows something different, but they must describe the <b>same "
            "house</b> — you cannot have the architectural drawing say 3 bedrooms while the electrical "
            "drawing says 5 and the plumbing drawing says 2. Software models work the same way.")]
    s += FIG("w12_house_analogy.png", "Figure 2 — The house analogy")

    s.append(H1("4.  Different UML Models Describe Different Views"))
    s += [P("The <b>use-case model</b> answers “what does the user want to accomplish?” The <b>class "
            "model</b> answers “what objects/classes make up the system?” The <b>sequence diagram</b> "
            "answers “how do objects communicate to accomplish a task?” The <b>state machine</b> answers "
            "“how does an object change state?” The <b>activity diagram</b> answers “what activities and "
            "decisions occur in a process?” <b>Component/deployment views</b> answer “how is the "
            "software organised and deployed?” UML groups structural modelling and behavioural modelling "
            "into different parts of its specification.")]
    s += FIG("w12_model_views.png", "Figure 3 — Different models, different questions")

    s.append(H1("5.  The Big Picture"))
    s += [P("Requirements -> use-case model -> (Object model / Dynamic model / Behavioural model) -> class "
            "diagram, state model, sequence/activity model -> integrated design -> implementation. This is "
            "the central idea of Week 12.")]
    s += FIG("w12_big_picture.png", "Figure 4 — The big picture")

    # PART B — consistency -------------------------------------------------------
    s.append(H1("PART B — WHY DO MODELS NEED TO AGREE?"))
    s.append(H1("6.  Model Consistency"))
    s += [P("Suppose the requirement says <i>“A student can register for a course.”</i> The use-case "
            "diagram contains <b>Student -> Register for Course</b> — good. But the class diagram contains "
            "only <b>Student, Teacher, Department</b>, with no <b>Course</b> or <b>Registration</b>. The "
            "use-case model says the system must support course registration, but the class model lacks "
            "the objects needed to support it — <b>the models are inconsistent or incomplete</b>. This is "
            "why OOAD is not simply about drawing diagrams: the diagrams must collectively tell a "
            "coherent story.")]
    s += FIG("w12_consistency.png", "Figure 5 — Model consistency")

    # PART C/D/E — the case study -------------------------------------------------
    s.append(H1("PART C–E — THE CASE STUDY AND TRACEABILITY"))
    s.append(H1("7.  University Course Registration — Building the Models"))
    s += [P("A university wants an online course registration system in which students log in, view "
            "available courses, register, drop and view their registered courses; the system checks "
            "capacity and prerequisites, stores registrations and notifies the student. "
            "<b>Step 1 — actors:</b> Student (later Administrator, Lecturer, Finance Officer). "
            "<b>Step 2 — use cases:</b> Login, View Courses, Register for Course, Drop Course, View "
            "Registered Courses. <b>Step 3 — classes:</b> domain classes Student, Course, Registration; "
            "service classes AuthenticationService, RegistrationService, CourseRepository, "
            "RegistrationRepository. <b>Step 4 — initial class model:</b> Student (studentId, name, "
            "email) — registers -> Registration (registrationId, date, status) — for -> Course "
            "(courseCode, title, credits, capacity).")]

    s.append(H1("8.  Traceability"))
    s += [P("<b>Traceability</b> means being able to answer “Where did this design element come from?” "
            "and “Which requirement does this design element support?” — e.g. Requirement R01 -> Use Case "
            "“Register for Course” -> sequence diagram -> classes Student, Course, Registration, "
            "RegistrationService -> operations register(), checkCapacity(), checkPrerequisite(). That is a "
            "traceable design.")]
    s += FIG("w12_traceability.png", "Figure 6 — Traceability")

    # PART F — sequence ------------------------------------------------------------
    s.append(H1("PART F — THE SEQUENCE DIAGRAM"))
    s.append(H1("9.  Why a Sequence Diagram — and Checking Consistency"))
    s += [P("The use case says “Student registers for a course” but does not tell us exactly how the "
            "interaction happens. The sequence diagram provides that detail: Student -> "
            "RegistrationService <font name='Mono'>register(course)</font> -> Course "
            "<font name='Mono'>checkCapacity()</font> and <font name='Mono'>checkPrerequisite()</font> -> "
            "RegistrationService <font name='Mono'>createRegistration()</font> -> Registration -> "
            "confirmation back to Student. Checking consistency: the elements used in the sequence "
            "diagram (Student, RegistrationService, Course, Registration) should exist in the class "
            "model. If the sequence suddenly says <font name='Mono'>PaymentProcessor</font> but the "
            "system has no payment requirement, ask why — maybe a requirement was forgotten, the class is "
            "unnecessary, or the model needs updating. That is model validation.")]
    s += FIG("w12_sequence.png", "Figure 7 — Registration sequence")

    # PART G — state ----------------------------------------------------------------
    s.append(H1("PART G — STATE MODELLING"))
    s.append(H1("10.  The Registration State Model"))
    s += [P("A registration is not always in the same condition — it may go through Requested, "
            "Validated, Confirmed, Cancelled or Rejected. The state model forces the business rules to "
            "be explicit: is <b>[CONFIRMED] -> [CANCELLED]</b> final, or does the business allow "
            "<b>[CANCELLED] -> [REQUESTED] -> [CONFIRMED]</b> again? The model makes the decision "
            "visible.")]
    s += FIG("w12_state_machine.png", "Figure 8 — Registration state model")

    # PART H — activity --------------------------------------------------------------
    s.append(H1("PART H — ACTIVITY DIAGRAM"))
    s.append(H1("11.  Activity Diagram vs Sequence Diagram"))
    s += [P("Students often confuse these. The <b>sequence diagram</b> focuses on "
            "<i>who communicates with whom, and in what order</i>. The <b>activity diagram</b> focuses "
            "on <i>what activities occur in a workflow</i>. The registration activity is: login -> "
            "display courses -> select course -> check prerequisites -> [satisfied?] -> check capacity -> "
            "[space available?] -> create registration -> confirm.")]
    s += FIG("w12_activity.png", "Figure 9 — Registration activity")
    s += FIG("w12_views_compare.png", "Figure 10 — Comparing the behavioural views")

    # PART I — integrating ------------------------------------------------------------
    s.append(H1("PART I — INTEGRATING THE FOUR MODELS"))
    s.append(H1("12.  Putting Everything Together"))
    s += [P("For <b>Register for Course</b> we now have the use case (Student -> Register for Course), "
            "the activity (login -> select course -> check prerequisite -> check capacity -> create -> "
            "confirm), the sequence (Student -> RegistrationService -> Course -> Registration), the state "
            "(Requested -> Validated -> Confirmed) and the class model (Student, Course, Registration, "
            "RegistrationService). These models now describe the same functionality from different "
            "viewpoints.")]
    s += FIG("w12_integrated_example.png", "Figure 11 — The complete integrated example")

    # PART J — consistency checklist ---------------------------------------------------
    s.append(H1("PART J — MODEL CONSISTENCY CHECKING"))
    s.append(H1("13.  The Consistency Checklist"))
    s += BUL([
        "<b>Actors</b> — does every important actor in the requirements/use cases appear appropriately elsewhere?",
        "<b>Use cases</b> — does every important use case have supporting behaviour?",
        "<b>Classes</b> — do the classes required by interactions exist?",
        "<b>Operations</b> — if the sequence says course.checkCapacity(), does Course have that operation?",
        "<b>Attributes</b> — if a requirement needs course capacity, does Course represent it?",
        "<b>States</b> — if the business distinguishes Pending/Approved/Rejected, does the state model represent them?",
        "<b>Relationships</b> — does the class model represent the right multiplicities?",
    ])

    # PART K — multiplicity -------------------------------------------------------------
    s.append(H1("PART K — MULTIPLICITY"))
    s.append(H1("14.  Why Multiplicity Matters"))
    s += [P("<b>Student —— Course</b> is not enough: how many courses can one student take, and how many "
            "students can take one course? Modelling the Registration as an entity gives precision: "
            "<b>Student 1 — 0..* Registration</b> and <b>Course 1 — 0..* Registration</b>.")]
    s += FIG("w12_multiplicity.png", "Figure 12 — Multiplicity")
    s.append(DTABLE(
        ["Symbol", "Meaning"],
        [["1", "Exactly one"],
         ["0..1", "Zero or one"],
         ["0..*", "Zero or many"],
         ["1..*", "One or many"],
         ["2..5", "Between two and five"]],
        widths=[0.3 * DOC_W, 0.7 * DOC_W]))

    # PART L — packages ----------------------------------------------------------------
    s.append(H1("PART L — PACKAGES: ORGANISING A LARGE MODEL"))
    s.append(H1("15.  Why Packages?"))
    s += [P("A large university system may contain Student, Course, Registration, Payment, Invoice, "
            "Lecturer, Department, LibraryBook, Borrowing, Notification, User, Role, Permission and "
            "Report. Putting everything into one diagram becomes unreadable — so we group related "
            "elements into <b>packages</b> such as Authentication, Academic, Finance, Library and "
            "Notification. UML supports package and other structural modelling constructs as part of its "
            "standard modelling language.")]
    s += FIG("w12_packages.png", "Figure 13 — Package structure")

    # PART M/N — architecture and components --------------------------------------------
    s.append(H1("PART M &amp; N — ARCHITECTURAL INTEGRATION AND COMPONENTS"))
    s.append(H1("16.  Layered Architecture"))
    s += [P("Moving beyond individual classes, a layered architecture organises the system into "
            "Presentation, Application (RegistrationService, AuthenticationService), Domain (Student, "
            "Course, Registration), Data Access (repositories) and Database. Everything inside one "
            "StudentRegistrationSystem class — HTML, database queries, business rules, authentication, "
            "registration, email, reports — becomes hard to maintain; layers give responsibilities "
            "clearer boundaries.")]
    s += FIG("w12_architecture.png", "Figure 14 — Layered architecture")

    s.append(H1("17.  Component Thinking"))
    s += [P("A <b>component</b> is a modular part of a system that provides or requires functionality — "
            "e.g. an Authentication Component, Registration Component, Payment Component, Notification "
            "Component and Reporting Component. This asks not simply “what classes exist?” but “how can "
            "the software be divided into meaningful, replaceable or independently understandable "
            "parts?” A Payment Component with processPayment() and refundPayment() can communicate with "
            "Bank, Mobile Money and Card gateways through an abstraction, keeping the larger system less "
            "dependent on a specific implementation.")]
    s += FIG("w12_components.png", "Figure 15 — Component thinking")

    # PART O/P — validation and review ----------------------------------------------------
    s.append(H1("PART O &amp; P — VALIDATION AND DESIGN REVIEW"))
    s.append(H1("18.  Design Validation"))
    s += [P("<b>Validation</b> asks “Does our design actually represent what the system is supposed to "
            "do?” If the requirement says <i>“students cannot register for a full course”</i> but the "
            "sequence shows Student -> RegistrationService -> Create Registration with no "
            "<font name='Mono'>checkCapacity()</font>, the design is incomplete. The fixed design inserts "
            "<font name='Mono'>Course.checkCapacity()</font> (and likewise "
            "<font name='Mono'>checkPrerequisite()</font> for the prerequisites rule).")]
    s += FIG("w12_validation.png", "Figure 16 — Design validation")

    s.append(H1("19.  Questions a Design Team Should Ask"))
    s += BUL([
        "<b>Requirement coverage</b> — have we represented every important requirement?",
        "<b>Use-case coverage</b> — does every major use case have supporting design elements?",
        "<b>Class / interaction / state coverage</b> — do classes, collaborations and lifecycles cover the requirements?",
        "<b>Architecture</b> — are responsibilities divided appropriately?",
        "<b>Coupling / cohesion</b> — are components unnecessarily dependent? does each have a meaningful focus?",
        "<b>Reuse / maintainability</b> — can components be reused, and what happens when requirements change?",
    ])

    # PART Q — model vs diagram -----------------------------------------------------------
    s.append(H1("PART Q — MODEL vs DIAGRAM"))
    s.append(H1("20.  An Important Distinction"))
    s += [P("“Model” and “diagram” are not synonyms. A <b>diagram</b> is a visual representation; a "
            "<b>model</b> is the underlying structured representation of the system being described — you "
            "may have multiple diagrams representing different aspects of the same model. Google Maps "
            "offers satellite, roads, terrain, traffic and public-transport views of the same geography; "
            "similarly the use-case, class, sequence, state and activity diagrams provide different "
            "perspectives on the same software system.")]
    s += FIG("w12_model_vs_diagram.png", "Figure 17 — Model vs diagram")

    # PART R — complete integrated example ------------------------------------------------
    s.append(H1("PART R — THE COMPLETE INTEGRATED EXAMPLE"))
    s += [P("<b>R01:</b> students should be able to register for available courses online. "
            "<b>Use case:</b> Student — Register for Course. <b>Classes:</b> Student, Course, "
            "Registration, RegistrationService. <b>Attributes:</b> Student (studentId, name, email); "
            "Course (courseCode, title, capacity); Registration (registrationId, date, status). "
            "<b>Operations:</b> Student.registerCourse(); Course.hasAvailableSpace(), "
            "checkPrerequisite(); Registration.confirm(), cancel(); RegistrationService.register(). "
            "<b>Sequence:</b> Student -> register(course) -> RegistrationService -> checkPrerequisite() -> "
            "Course -> available? -> create() -> Registration -> confirm() -> Student. <b>Activity:</b> "
            "login -> select course -> check prerequisite -> check capacity -> create -> confirm. "
            "<b>State:</b> Requested -> Validated -> Confirmed -> Cancelled. <b>Architecture:</b> "
            "Presentation -> RegistrationService -> domain -> repositories -> database.")]
    s += FIG("w12_summary_flow.png", "Figure 18 — The Week 12 mental model")

    # tutorial / practical ----------------------------------------------------------------
    s.append(H1("21.  Tutorial and Practical"))
    s += [P("<b>Tutorial 1</b> — For “A patient can select a doctor, choose an available date and time, "
            "and book an appointment”, identify actors, use cases, classes, attributes, operations, "
            "relationships and possible appointment states. <b>Tutorial 2</b> — Explain the question "
            "answered by each of the use-case, class, sequence, activity and state diagrams. "
            "<b>Tutorial 3</b> — A sequence diagram contains PaymentService, Payment and Invoice but the "
            "class diagram only has Student, Course and Registration: what inconsistency exists, what "
            "should the designer do, and why must the models agree?"),
          P("<b>Practical (1 hour):</b> create a complete integrated UML model for the Online University "
            "Course Registration System — (1) use-case diagram (Student, Administrator), (2) class "
            "diagram (Student, Course, Registration, Programme, User, RegistrationService with "
            "attributes, operations, visibility, relationships, multiplicities), (3) sequence diagram "
            "for registering, (4) activity diagram for the workflow, (5) state diagram for the "
            "Registration lifecycle, (6) package diagram (Authentication, Academic, Registration, "
            "Administration), and (7) architecture (Presentation, Application, Domain, Data Access, "
            "Database).")]

    # misunderstandings ----------------------------------------------------------------------
    s.append(H1("22.  Common Student Confusions"))
    s += BUL([
        "<b>Use case vs sequence</b> — use case = what the user wants to achieve; sequence = how objects communicate to achieve it.",
        "<b>Activity vs state</b> — activity = what activities happen in a process; state = what states a particular object passes through.",
        "<b>Class vs object diagram</b> — class = the blueprint (Student, Course, Registration); object = the actual instance (student:Student, course:Course).",
    ])

    # summary ----------------------------------------------------------------------------------
    s.append(H1("23.  Week 12 Summary"))
    s.append(DTABLE(
        ["Model", "Main question"],
        [["Use case", "What does the actor want to accomplish?"],
         ["Class", "What objects/classes make up the system?"],
         ["Sequence", "How do objects interact over time?"],
         ["Activity", "What workflow/activities take place?"],
         ["State machine", "How does an object change state?"],
         ["Component / deployment", "How is the software organised and deployed?"]],
        widths=[0.34 * DOC_W, 0.66 * DOC_W]))
    s.append(CALLOUT("THE CENTRAL PRINCIPLE OF WEEK 12",
        ["Every model should contribute to the <b>same understanding of the system</b>. Requirements -> "
         "use cases -> what the system must do -> behavioural models -> how the behaviour occurs -> "
         "object/class model -> what structure supports the behaviour -> architecture -> how the software "
         "is organised -> implementation. <b>Don't memorise UML diagrams as independent pictures — learn "
         "to tell the same system's story through different models, and make sure those models "
         "agree.</b>"]))

    # exam ----------------------------------------------------------------------------------------
    s.append(H1("24.  Examination-Style Questions"))
    s += [P("<b>Essay (25 marks).</b> Explain integrated object-oriented modelling. Using an Online "
            "University Registration System, demonstrate how the use-case, class, sequence, activity and "
            "state models can be integrated into a coherent design."),
          P("<b>Essay (20 marks).</b> “Different UML diagrams represent different views of the same "
            "software system.” Explain this statement with examples."),
          P("<b>Essay (20 marks).</b> A sequence diagram contains checkAvailability() but the class "
            "diagram has no such operation. (a) Identify the modelling problem. (b) Explain why "
            "consistency matters. (c) Describe how the designer should resolve it."),
          P("<b>Scenario (25 marks).</b> Design an integrated UML model for an online hospital "
            "appointment system: actors, use cases, classes, relationships, sequence of interactions, "
            "activities, appointment states, and an explanation of how the models are consistent.")]

    # references ------------------------------------------------------------------------------------
    s.append(H1("25.  References and Further Reading"))
    s.append(H2("Authoritative / current online sources"))
    s += BUL([
        "Object Management Group (OMG). <i>Unified Modeling Language (UML), Version 2.5.1.</i> OMG — the formal UML specification and machine-readable UML artefacts.",
        "Object Management Group. <i>UML — Unified Modeling Language.</i> Overview of UML's purpose in visualising, specifying and documenting software and systems.",
        "Object Management Group. <i>UML 2.5.1 Specification — Technical Specification.</i> Structural and behavioural modelling clauses and UML diagram concepts.",
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
