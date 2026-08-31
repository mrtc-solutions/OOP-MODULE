"""
Week 9 PDF content — THE UNIFIED SOFTWARE DEVELOPMENT PROCESS (USDP / UP).
"""
from pdfengine import (H1, H2, P, BUL, FIG, CALLOUT, DTABLE, build, DOC_W,
                      C_MAROON, C_SOFT)

CFG = {
    "week": 9,
    "title": "The Unified Software Development Process (USDP / Unified Process)",
    "filename": "Week9_Module_BICT3202_OOAD.pdf",
}


def story():
    s = []

    # 1. introduction --------------------------------------------------------
    s.append(H1("1.  Week 9 Introduction"))
    s += [P("Weeks 4–8 moved from object modelling, through dynamic modelling, to behavioural modelling. "
            "Week 9 changes the question again: <b>“How do we organise the development of the "
            "software?”</b> The distinction is extremely important — <b>UML tells us how to model a "
            "system; the Unified Process tells us how to organise the work of developing that "
            "system.</b>"),
          P("The <b>Unified Process (UP)</b> is an iterative and incremental software-development process "
            "strongly associated with object-oriented development and UML. A commercial and particularly "
            "well-known implementation is the <b>Rational Unified Process (RUP)</b>. The official outline "
            "covers the USDP, its aspects and characteristics, phases and iterations, process workflows, "
            "artefacts, reuse, concurrency, generalisation and inheritance — all covered this week.")]

    # 2. learning outcomes -----------------------------------------------------
    s.append(H1("2.  Learning Outcomes"))
    s += [P("By the end of this week, a student should be able to:")]
    s += BUL([
        "Define the Unified Software Development Process and explain why it suits OO development.",
        "Explain iterative and incremental development, and distinguish them.",
        "Explain the major characteristics of UP (use-case driven, architecture-centred, iterative & incremental, risk-driven).",
        "Distinguish a phase from an iteration, and explain Inception, Elaboration, Construction and Transition.",
        "Explain milestones, process workflows/disciplines and important artefacts.",
        "Explain requirements-driven, architecture-centred and risk-driven development.",
        "Explain reuse, its guidelines, concurrency, generalisation and inheritance.",
        "Distinguish generalisation from inheritance and connect UP to the UML models already studied.",
    ])

    # ============ PART A/B — PROCESS & UP ============
    s.append(H1("PART A &amp; B — WHAT IS THE UNIFIED PROCESS?"))
    s.append(H1("3.  Software Development Process"))
    s += [P("A <b>software development process</b> is an organised set of activities, roles, "
            "responsibilities, practices, work products and decisions used to develop and maintain "
            "software. In simple language: it tells a development team <b>what work needs to be done, "
            "when, who should do it, and what should be produced</b>. Without a process, the analyst, "
            "programmer, tester and client each build and expect different things — and the manager asks "
            "why the project is six months late.")]
    s += FIG("w9_why_process.png", "Figure 1 — Why software needs a process")

    s.append(H1("4.  The Unified Process — and UP vs RUP"))
    s += [P("The <b>Unified Process</b> is an iterative and incremental software-development process "
            "designed around object-oriented development, closely associated with UML and use-case-driven "
            "development. The <b>Rational Unified Process (RUP)</b> is a specific commercial "
            "implementation of UP developed by Rational and later associated with IBM — UP is the general "
            "framework; RUP is one implementation of it. A traditional process might treat Requirements → "
            "Analysis → Design → Coding → Testing → Deployment as separate stages; UP instead encourages "
            "repeated cycles with feedback.")]
    s += FIG("w9_up_vs_rup.png", "Figure 2 — UP vs RUP")
    s += FIG("w9_waterfall_vs_up.png", "Figure 3 — Waterfall vs UP")

    # ============ PART C — ITERATIVE & INCREMENTAL ============
    s.append(H1("PART C — ITERATIVE AND INCREMENTAL DEVELOPMENT"))
    s.append(H1("5.  Iterative vs Incremental"))
    s += [P("<b>Iterative</b> means the team repeats development activities in multiple cycles and "
            "improves the system from one cycle to the next — like drafting, reviewing and improving an "
            "essay. <b>Incremental</b> means the system grows by adding usable functionality over time — "
            "Increment 1 adds Login, Increment 2 adds course registration, Increment 3 adds assignment "
            "submission, Increment 4 adds results. In practice UP uses both: <b>UP is iterative AND "
            "incremental</b>, with short, timeboxed iterations."),
          P("An <b>iteration</b> is a planned development cycle in which the team performs some "
            "combination of requirements work, analysis, design, implementation, testing and evaluation, "
            "ending with a measurable result. We are not waiting until the very end to discover whether "
            "the system works.")]
    s += FIG("w9_iterative_incremental.png", "Figure 4 — Iterative vs incremental")
    s += FIG("w9_increments.png", "Figure 5 — Incremental growth of an e-learning system")

    # ============ PART D — CHARACTERISTICS ============
    s.append(H1("PART D — THE FOUR MAJOR CHARACTERISTICS"))
    s.append(H1("6.  Use-Case Driven, Architecture-Centred, Iterative &amp; Incremental, Risk-Driven"))
    s += [P("<b>Use-case driven:</b> development is organised around use cases. UC-01 Register Course "
            "becomes a thread running through requirements, analysis, design, implementation and testing — "
            "identifying the objects (Student, Course, Registration), the classes "
            "(RegistrationController, CourseService), the code and the test scenarios."),
          P("<b>Architecture-centred:</b> UP establishes and validates a strong architectural foundation "
            "early, especially during Elaboration. Software architecture is the high-level organisation of "
            "a system (User Interface → Business Logic → Data Access → Database). A system built for 100 "
            "students may collapse with 100,000, so major architectural risks are identified early."),
          P("<b>Iterative and incremental:</b> the system is developed through repeated cycles, each "
            "improving or extending it. <b>Risk-driven:</b> UP identifies and addresses significant risks "
            "early rather than “building the easiest things first” — a mobile banking system that must "
            "process 5,000 transactions per second is tested early, not left to the end.")]
    s += FIG("w9_characteristics.png", "Figure 6 — The four characteristics")
    s += FIG("w9_architecture.png", "Figure 7 — Software architecture layers")

    # ============ PART E — FOUR PHASES ============
    s.append(H1("PART E — THE FOUR UP PHASES"))
    s.append(H1("7.  Inception → Elaboration → Construction → Transition"))
    s += [P("<b>Inception</b> asks “should we build this system, and what are we trying to build?” — it "
            "establishes the business case, scope, high-level requirements, major actors and use cases, "
            "cost, schedule, risks and success criteria, ending at the <b>Lifecycle Objectives "
            "Milestone</b> (a go/no-go decision)."),
          P("<b>Elaboration</b> asks “can we build it, and with what architecture?” — refining "
            "requirements, analysing the domain, establishing architecture and addressing major technical "
            "risks (often via an executable architectural prototype), ending at the <b>Lifecycle "
            "Architecture Milestone</b>."),
          P("<b>Construction</b> asks “can we build the complete system?” — most detailed implementation "
            "takes place here, through iterations that add course registration, payments, results, reports "
            "and administration."),
          P("<b>Transition</b> asks “can real users use it in the real environment?” — deployment, "
            "installation, data migration, training, beta testing, defect fixing and final adjustments "
            "before release.")]
    s += FIG("w9_phases.png", "Figure 8 — The four phases")
    s += FIG("w9_phase_questions.png", "Figure 9 — The four phases compared")

    s.append(H1("8.  A Phase Is NOT a Waterfall Stage"))
    s += [P("Students may look at Inception → Elaboration → Construction → Transition and think it is "
            "“waterfall with different names”. No. <b>A phase contains one or more iterations</b> — "
            "iterations provide planned intervals that deliver incremental value within each phase. That "
            "is what makes UP fundamentally different from treating the four phases as four rigid "
            "sequential stages.")]
    s += FIG("w9_phases_iterations.png", "Figure 10 — Phases contain iterations")

    # ============ PART G — WORKFLOWS ============
    s.append(H1("PART G — PROCESS WORKFLOWS / DISCIPLINES"))
    s.append(H1("9.  Workflows and Their Overlap"))
    s += [P("A <b>workflow</b> (discipline) is a set of related activities performed to achieve a "
            "development objective. Core technical disciplines are <b>Business Modeling</b> (how does the "
            "organisation operate?), <b>Requirements</b> (what must the system do?), <b>Analysis &amp; "
            "Design</b> (how should it be structured — this is where our UML models matter most), "
            "<b>Implementation</b>, <b>Test</b> and <b>Deployment</b>. Supporting disciplines are "
            "<b>Configuration &amp; Change Management</b>, <b>Project Management</b> and "
            "<b>Environment</b>."),
          P("A common misconception is “first requirements, then design, then implementation, then "
            "testing”. In UP the disciplines overlap: during an iteration requirements → analysis → "
            "design → implementation → testing → feedback → refined requirements, and the <b>intensity</b> "
            "of each discipline changes across phases — requirements are heavy in Inception and "
            "Elaboration, coding is heavy in Construction, testing and deployment are heavy in Transition. "
            "Coding can even occur in Elaboration (architectural prototypes).")]
    s += FIG("w9_workflows.png", "Figure 11 — The core and supporting workflows")
    s += FIG("w9_workflow_intensity.png", "Figure 12 — Workflow intensity across phases")

    # ============ PART I — ARTEFACTS ============
    s.append(H1("PART I — ARTEFACTS OF THE UNIFIED PROCESS"))
    s.append(H1("10.  Artefacts"))
    s += [P("An <b>artefact</b> is a work product created, modified or used during development — evidence "
            "of the team's work. Examples: the Vision document, requirements specification, use-case "
            "model, risk list, project plan, glossary, class and sequence diagrams, architecture "
            "document, source code, test plan and cases, deployment package and user manual. Across the "
            "phases: Inception produces the Vision, Business Case, initial use-case model, risk assessment "
            "and project plan; Elaboration produces detailed requirements, the architecture document, the "
            "domain model and an architectural prototype; Construction produces source code, components, "
            "test cases and working builds; Transition produces the deployment package, user documentation "
            "and release notes.")]
    s += FIG("w9_artefacts.png", "Figure 13 — Artefacts across the phases")

    # ============ PART J — REUSE ============
    s.append(H1("PART J — REUSE IN OO DEVELOPMENT"))
    s.append(H1("11.  Reuse — and Its Guidelines"))
    s += [P("<b>Software reuse</b> means using an existing asset again instead of creating the same "
            "functionality from scratch — classes, components, libraries, frameworks, services, APIs, "
            "design patterns and architectural components. Reuse can reduce time and cost, improve "
            "consistency and leverage tested components. But reuse is not automatically good: before "
            "adopting an asset, evaluate its <b>functional suitability, quality, security, compatibility, "
            "maintainability, licence, performance and cost</b>.")]
    s += FIG("w9_reuse.png", "Figure 14 — Reuse: assets and evaluation")

    # ============ PARTS K-M — GENERALISATION, INHERITANCE, CONCURRENCY ============
    s.append(H1("PARTS K–M — GENERALISATION, INHERITANCE AND CONCURRENCY"))
    s.append(H1("12.  Generalisation vs Inheritance"))
    s += [P("<b>Generalisation</b> is a modelling/design relationship in which a more general concept "
            "represents characteristics shared by more specialised concepts (User generalises Student and "
            "Lecturer; Student IS-A User). <b>Inheritance</b> is the programming-language mechanism "
            "through which a specialised class acquires accessible attributes and operations from a more "
            "general class (<font name='Mono'>class Student extends User</font>). They are closely related "
            "but not identical: generalisation is the conceptual relationship; inheritance is the "
            "implementation mechanism. The <b>is-a test</b> — “Is Student a User?” yes; “Student has a "
            "Course” is a different relationship.")]
    s += FIG("w9_gen_vs_inheritance.png", "Figure 15 — Generalisation vs inheritance")

    s.append(H1("13.  Concurrency"))
    s += [P("<b>Concurrency</b> means multiple activities or operations can make progress during "
            "overlapping periods. After a payment succeeds, updating inventory, generating a receipt, "
            "notifying the warehouse and sending an email can happen independently. Concurrency affects "
            "architecture, performance, responsiveness, thread/process design, synchronisation and data "
            "consistency."),
          P("A classic OOAD problem: a course has capacity 1 and two students register at exactly the "
            "same time. Both systems check “available seats = 1”, both register successfully — now "
            "registered = 2 while capacity = 1. <b>Concurrency must sometimes be addressed at the "
            "analysis/design level.</b>")]
    s += FIG("w9_concurrency.png", "Figure 16 — The concurrency problem")

    # ============ CONNECTING ============
    s.append(H1("14.  Connecting UP to the UML Models"))
    s += [P("The class/object, dynamic and behavioural models of previous weeks do not exist in "
            "isolation — within UP they become <b>artefacts</b> used during development: requirement → "
            "use case → use-case diagram → activity diagram → sequence diagram → class/object model → "
            "design → implementation. <b>The Unified Process provides the development process; UML "
            "provides many of the modelling languages used within that process.</b>"),
          P("Worked example — the Mzuni Online Student Registration System: <b>Inception</b> identifies "
            "actors (Student, Registrar, Finance Officer, Payment Gateway), use cases (Login, Register "
            "Course, Drop Course, Pay Fees, View Registration, Generate Reports) and risks (security, "
            "payment integration, database performance, migration, adoption). <b>Elaboration</b> "
            "investigates authentication, database and payment architecture and builds a prototype. "
            "<b>Construction</b> delivers iterations — login, catalogue, registration, payments, reports. "
            "<b>Transition</b> installs, migrates records, trains administrators, pilots, fixes defects "
            "and launches.")]

    # ============ MISUNDERSTANDINGS ============
    s.append(H1("15.  Common Misunderstandings"))
    s += BUL([
        "<b>“UP is the same as Waterfall.”</b> — No: phases contain iterations and activities overlap.",
        "<b>“Inception means collecting every requirement.”</b> — Inception establishes the business case, scope and major requirements; requirements are refined over iterations.",
        "<b>“Coding only happens in Construction.”</b> — Coding can occur earlier (architectural prototypes in Elaboration).",
        "<b>“Testing starts after all coding is finished.”</b> — Testing occurs throughout iterative development.",
        "<b>“Generalisation and inheritance are exactly the same.”</b> — Closely related, but generalisation is the modelling relationship and inheritance is the programming mechanism.",
        "<b>“Reuse means copy and paste code.”</b> — Reuse spans classes, libraries, services, frameworks, APIs and patterns, and requires evaluation.",
    ])

    # ============ SUMMARY ============
    s.append(H1("16.  Week 9 Summary and Key Terms"))
    s.append(DTABLE(
        ["Term", "Simple meaning"],
        [["Unified Process", "Organised OO software-development process."],
         ["RUP", "Rational's commercial implementation of UP."],
         ["Iterative", "Repeat and improve across cycles."],
         ["Incremental", "Add functionality progressively."],
         ["Use-case driven", "Use cases guide development."],
         ["Architecture-centred", "Build and validate important architecture early."],
         ["Risk-driven", "Address significant risks early."],
         ["Inception / Elaboration", "Establish business case & scope / refine requirements & architecture."],
         ["Construction / Transition", "Build the system / deploy and move to users."],
         ["Phase / iteration / workflow / artefact", "Major lifecycle period / cycle within a phase / related activities / work product."],
         ["Reuse", "Use existing software assets (with evaluation)."],
         ["Generalisation / inheritance", "Modelling relationship / programming mechanism."],
         ["Concurrency", "Overlapping execution of activities."]],
        widths=[0.34 * DOC_W, 0.66 * DOC_W]))
    s.append(CALLOUT("THE BIG PICTURE — FIVE THINGS TO REMEMBER",
        ["1. UP is <b>iterative and incremental</b>. 2. UP is <b>use-case driven</b>. 3. UP is "
         "<b>architecture-centred</b>. 4. UP has <b>four phases</b> — Inception → Elaboration → "
         "Construction → Transition. 5. <b>Phases contain iterations</b> — that is what makes UP "
         "different from four rigid sequential stages. Week 8 asked “what should the system do?”; Week 9 "
         "asks “how should the team organise the work?”; Weeks 10+ ask “how should we design the "
         "software?”"]))

    # ============ EXAM QUESTIONS ============
    s.append(H1("17.  Examination-Style Questions"))
    s += [P("<b>Essay (25 marks).</b> Discuss the Unified Software Development Process and explain how "
            "its four phases contribute to successful object-oriented software development — covering the "
            "definition, iterative and incremental nature, use-case driven development, architecture, "
            "risk management, the four phases, milestones and artefacts."),
          P("<b>Scenario.</b> A hospital intends to develop an online patient management system to "
            "register patients, book appointments, process payments, store medical records and generate "
            "reports, and is particularly concerned about security, performance and integration with "
            "existing systems. Required: explain how UP could be used; what should happen during "
            "Inception; why Elaboration is particularly important; give three architectural risks; "
            "suggest three artefacts; explain how iterations could be used during Construction; and "
            "explain the activities of Transition.")]

    # ============ REFERENCES ============
    s.append(H1("18.  References and Further Reading"))
    s.append(H2("Primary / authoritative"))
    s += BUL([
        "Object Management Group. (2017). <i>OMG Unified Modeling Language (UML), Version 2.5.1.</i> OMG — the formal specification, adopted December 2017.",
        "IBM. <i>Project Planning — Phases and Iterations</i> (IBM Rational documentation; identifies the four RUP phases and iterations).",
        "IBM Rational. <i>Rational Unified Process: Best Practices for Software Development Teams.</i> IBM.",
        "Project Management Institute. <i>Project Management and the Rational Unified Process for Software Development Projects.</i> PMI.",
        "The Open University. <i>Approaches to Software Development — Introducing the Unified Process.</i>",
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
