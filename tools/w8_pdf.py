"""
Week 8 PDF content — OBJECT-ORIENTED ANALYSIS: BEHAVIOURAL MODELLING.
"""
from pdfengine import (H1, H2, P, BUL, FIG, CALLOUT, DTABLE, build, DOC_W,
                      C_MAROON, C_SOFT)

CFG = {
    "week": 8,
    "title": "Object-Oriented Analysis — Behavioural Modelling",
    "filename": "Week8_Module_BICT3202_OOAD.pdf",
}


def story():
    s = []

    # 1. introduction --------------------------------------------------------
    s.append(H1("1.  Week 8 Introduction"))
    s += [P("The progression matters: Weeks 4–6 modelled <b>what things exist</b> (object modelling); "
            "Week 7 modelled <b>how objects change state over time</b> (dynamic modelling); Week 8 models "
            "<b>how users and objects interact to accomplish tasks</b> (behavioural modelling). Week 9 "
            "turns to the development process itself, and Weeks 10+ to design."),
          P("Behavioural modelling is not simply another collection of UML diagrams. The major idea is: "
            "<b>behavioural modelling describes what the system does, how users interact with it, how "
            "objects communicate, and how activities flow to achieve a goal.</b> The official outline "
            "covers use cases, use case diagrams, interaction diagrams, sequence diagrams, collaboration "
            "(communication) diagrams, activity diagrams and full analysis documentation — all seven are "
            "covered this week.")]

    # 2. learning outcomes -----------------------------------------------------
    s.append(H1("2.  Learning Outcomes"))
    s += [P("By the end of this week, a student should be able to:")]
    s += BUL([
        "Define behavioural modelling and explain why it is important.",
        "Define use cases and actors, and construct a use case diagram.",
        "Explain the system boundary and include, extend and generalization relationships.",
        "Write a detailed use-case specification.",
        "Construct sequence diagrams with lifelines, activation bars and messages.",
        "Explain synchronous/asynchronous messages, and alt/loop/opt fragments.",
        "Construct communication (collaboration) diagrams.",
        "Explain the difference between sequence and communication diagrams.",
        "Construct activity diagrams with decisions, parallel flows and swimlanes.",
        "Connect use cases, activity diagrams and interaction diagrams into coherent analysis documentation.",
    ])

    # ============ PART A — WHAT IS BEHAVIOURAL MODELLING ============
    s.append(H1("PART A — WHAT IS BEHAVIOURAL MODELLING?"))
    s.append(H1("3.  Definition and Why We Need It"))
    s += [P("<b>Behavioural modelling</b> is the process of representing how a system behaves in response "
            "to users, events, inputs and other objects — in simple language, it tells us <b>what the "
            "system does and how things interact while it is doing it</b>. “Build a university "
            "registration system” is far too vague; we need to know who uses it, what each role can do, "
            "what happens when registration succeeds or fails, what messages pass between objects, and "
            "which activities happen in parallel. Behavioural models answer these questions."),
          P("Think of behavioural modelling as a <b>family</b>: use cases (use case diagrams), "
            "interactions (sequence and communication diagrams) and activities (activity diagrams). Each "
            "diagram answers a slightly different question, summarised below — this is very important for "
            "examinations.")]
    s += FIG("w8_family.png", "Figure 1 — The behavioural modelling family")
    s += FIG("w8_questions.png", "Figure 2 — What question each diagram answers")

    # ============ PART B — USE CASES ============
    s.append(H1("PART B — USE CASES"))
    s.append(H1("4.  What Is a Use Case?"))
    s += [P("A <b>use case</b> describes a goal-oriented interaction between an actor and a system that "
            "produces a result of value to the actor — something a user wants to accomplish. Examples: "
            "Login, Register for Course, Make Payment, Withdraw Money, Place Order, Track Order, Generate "
            "Report, Submit Assignment, Book Appointment."),
          P("When identifying a use case, ask: <b>“What does the actor want to accomplish?”</b> A student "
            "saying “I want to register for a course” gives the use case <b>Register for Course</b> — not "
            "<i>Click Register Button</i>, which is only one interface action. A use case is the user's "
            "goal; the functions/actions (read card, validate PIN, check balance, dispense cash) are the "
            "steps used to achieve it.")]
    s += FIG("w8_use_case_goal.png", "Figure 3 — A use case is a goal, not a function")

    s.append(H1("5.  Actors"))
    s += [P("An <b>actor</b> is an external role that interacts with the system, outside the system "
            "boundary — Student, Lecturer, Administrator, Customer, Bank, Payment Gateway, Email Service. "
            "An actor represents a <b>role</b>: one person who is both a Student and a Teaching Assistant "
            "plays two roles. An actor does not have to be human — a Payment Gateway that is external to "
            "the system being modelled is also an actor.")]
    s += FIG("w8_actor_human.png", "Figure 4 — Human and non-human actors")

    # ============ PART C — USE CASE DIAGRAMS ============
    s.append(H1("PART C — USE CASE DIAGRAMS"))
    s.append(H1("6.  The Use Case Diagram and System Boundary"))
    s += [P("A <b>use case diagram</b> provides a high-level view of actors, use cases, the system "
            "boundary and their relationships — it answers <b>“who interacts with the system and what "
            "goals can they accomplish?”</b> The <b>system boundary</b> is drawn as a rectangle containing "
            "the use cases; actors sit outside it. A basic association line shows that an actor "
            "participates in a use case: <font name='Mono'>Student ─── (Register Course)</font>.")]
    s += FIG("w8_use_case_diagram.png", "Figure 5 — A complete use case diagram")

    s.append(H1("7.  Use Case Relationships — include, extend, generalisation"))
    s += [P("Large systems can have dozens of use cases, some sharing behaviour. UML provides "
            "relationships: <b>association</b> (an actor participates in a use case), <b>include</b> (one "
            "use case incorporates another as part of its execution — “this behaviour is always needed”; "
            "e.g. Register Course <font name='Mono'>&lt;&lt;include&gt;&gt;</font> Authenticate Student), "
            "<b>extend</b> (additional behaviour that occurs under particular circumstances — “sometimes "
            "this extra behaviour happens”; e.g. Withdraw Cash <font name='Mono'>&lt;&lt;extend&gt;&gt;</font> "
            "Report Suspicious Transaction), and <b>generalisation</b> (a specialised actor/use case "
            "inherits from a more general one — Student and Lecturer are specialised Users)."),
          P("Memory trick: <b>INCLUDE = “I need this as part of the job”</b>; <b>EXTEND = “I might add "
            "this under a condition”</b>. Include factors common/reused behaviour; extend models "
            "optional/exceptional behaviour.")]
    s += FIG("w8_relationships.png", "Figure 6 — The four use case relationships")
    s += FIG("w8_include_extend.png", "Figure 7 — include vs extend")

    # ============ PART E — SPECIFICATIONS ============
    s.append(H1("PART E — USE CASE SPECIFICATIONS"))
    s.append(H1("8.  The Diagram Is Not Enough"))
    s += [P("A use case diagram gives only a high-level view. Serious analysis needs a <b>use-case "
            "specification</b> describing what happens inside the use case — its ID, name, primary actor, "
            "goal, preconditions, main success scenario, alternative flows and postconditions. For "
            "Register for Course, the main scenario might be: select Register Course → view available "
            "courses → select a course → check prerequisites → check capacity → confirm → create "
            "registration → show confirmation. Alternative flows handle a full course (offer waitlist) and "
            "missing prerequisites (stop registration)."),
          P("Telling a programmer only “build course registration” leaves them guessing what happens when "
            "a course is full or payment fails. The specification captures those requirements — which is "
            "why behavioural analysis connects requirements to design, and why we must model alternative "
            "and exception paths, not only the “happy path”.")]
    s += FIG("w8_specification.png", "Figure 8 — A use case specification")

    # ============ PART F/G — INTERACTION & SEQUENCE ============
    s.append(H1("PART F &amp; G — INTERACTION AND SEQUENCE DIAGRAMS"))
    s.append(H1("9.  Sequence Diagrams"))
    s += [P("An <b>interaction</b> describes how participants communicate by exchanging messages. A "
            "<b>sequence diagram</b> shows interactions in <b>time order</b> — who communicates with "
            "whom, what messages are exchanged, and in what order. Its components are: actor, object, "
            "<b>lifeline</b> (the vertical dashed line representing a participant's existence), "
            "<b>activation bar</b> (a period during which a participant is performing an operation), "
            "<b>message</b> (communication from one participant to another) and return message. Read from "
            "top to bottom: time flows downward."),
          P("A login sequence: Student → System <font name='Mono'>login()</font>; System → Database "
            "<font name='Mono'>validate()</font>; Database → System <font name='Mono'>valid</font>; "
            "System → Student <font name='Mono'>confirmation</font>. Order matters — you cannot send "
            "“login successful” before validating the credentials. A registration sequence introduces "
            "Registration UI, Registration Controller and Course Database, moving from requirements toward "
            "the software objects that will participate.")]
    s += FIG("w8_sequence_components.png", "Figure 9 — Sequence diagram components")
    s += FIG("w8_sequence_login.png", "Figure 10 — A login sequence diagram")

    s.append(H1("10.  Alternative Sequences — alt, loop, opt"))
    s += [P("Real systems do not always follow the happy path. Combined fragments model alternatives: "
            "<b>alt</b> — only the branch whose guard is true executes (course available → register; "
            "course full → show message); <b>loop</b> — behaviour repeats (for each student, send the "
            "result); <b>opt</b> — behaviour occurs only if a condition is true (send SMS only if "
            "notifications are enabled).")]
    s += FIG("w8_fragments.png", "Figure 11 — Combined fragments: alt, loop, opt")

    # ============ PART I — COMMUNICATION ============
    s.append(H1("PART I — COMMUNICATION (COLLABORATION) DIAGRAMS"))
    s.append(H1("11.  Communication Diagrams"))
    s += [P("The course outline uses the older term <b>collaboration diagram</b>; in UML 2.x the standard "
            "term is <b>communication diagram</b> — students may meet both names. A communication diagram "
            "focuses on <b>which objects communicate and what messages they exchange</b>, emphasising "
            "object relationships rather than vertical time. Messages are numbered — 1: register(), "
            "2: checkCourse(), 3: availability, 4: confirmation — to show order. The same interaction can "
            "be shown as a sequence diagram (emphasising time and message order) or a communication "
            "diagram (emphasising participating objects and their links).")]
    s += FIG("w8_communication.png", "Figure 12 — A communication diagram")
    s += FIG("w8_seq_vs_comm.png", "Figure 13 — Sequence vs communication diagram")

    # ============ PART J — ACTIVITY ============
    s.append(H1("PART J — ACTIVITY DIAGRAMS"))
    s.append(H1("12.  Activity Diagrams"))
    s += [P("An <b>activity diagram</b> models a workflow or flow of activities — the steps involved in "
            "carrying out a process, including decisions and parallel activities. Its notation: the "
            "initial node (●), actions (rounded rectangles), the decision/merge diamond (◇), the final "
            "node (◎), flow arrows, and <b>fork/join</b> thick bars. The diamond represents a decision "
            "whose outgoing paths carry guard conditions — [balance sufficient] / [balance "
            "insufficient]."),
          P("A fork splits one flow into multiple <b>concurrent</b> flows (after an order is confirmed: "
            "Prepare Food <b>and</b> Assign Driver, then join before Deliver Order). An online shop after "
            "payment may update inventory, prepare an invoice, notify the warehouse and send confirmation "
            "— some of which can occur independently.")]
    s += FIG("w8_activity_notation.png", "Figure 14 — Activity diagram notation")
    s += FIG("w8_activity_example.png", "Figure 15 — An online shopping activity diagram")

    s.append(H1("13.  Swimlanes"))
    s += [P("A <b>swimlane</b> divides an activity diagram according to responsibility, answering "
            "“<b>who is responsible for performing each activity?</b>” Without swimlanes, a list of "
            "activities (check prerequisites, confirm registration, update database) does not tell us who "
            "performs what; with swimlanes, Student performs Select course and Confirm, while System "
            "performs Check prerequisites, Create registration and Display confirmation.")]
    s += FIG("w8_swimlanes.png", "Figure 16 — Swimlanes")

    # ============ PART M — WORKING TOGETHER ============
    s.append(H1("PART M — HOW THE MODELS WORK TOGETHER"))
    s.append(H1("14.  Use Case → Activity → Sequence"))
    s += [P("The most important concept of Week 8: the models work together. From the requirement “a "
            "student should be able to register for a course”, we write the <b>use case</b> (Register "
            "Course), model the <b>workflow</b> with an activity diagram (select course → check "
            "prerequisite → check availability → confirm → create registration), then model the "
            "<b>object interactions</b> with a sequence diagram (Student → Registration UI → "
            "Registration Controller → Course Database). The chain runs: requirement → use case → activity "
            "diagram → sequence diagram → object responsibilities → design.")]
    s += FIG("w8_traceability.png", "Figure 17 — Requirement to design, with traceability")

    s.append(H1("15.  Full Analysis Documentation"))
    s += [P("<b>Analysis documentation</b> is the collection of models and written descriptions that "
            "explain what the proposed system must do: the problem statement, business/functional/"
            "non-functional requirements, actors, use cases, use-case and activity and sequence and "
            "communication diagrams, class and state-machine diagrams, assumptions, constraints, business "
            "rules and a glossary. It matters because the client, analyst, designer, programmer, tester "
            "and project manager all need a common language and <b>traceability</b> — the client says "
            "“register courses”, the analyst calls it UC-03, the designer draws the sequence diagram, the "
            "programmer identifies the objects, and the tester derives the scenarios. REQ-05 → UC-05 → "
            "activity model → sequence model → design → test cases.")]

    # ============ COMMON CONFUSIONS ============
    s.append(H1("16.  Common Student Confusions"))
    s.append(DTABLE(
        ["Confusion", "Clarification"],
        [["Use case vs use case diagram", "A use case is one goal/behaviour (Register Course); the diagram is the visual representation of actors, use cases and relationships."],
         ["Use case vs activity diagram", "Use case = what goal; activity diagram = what workflow happens."],
         ["Activity vs sequence", "Activity = workflow/process (check stock → process payment); sequence = messages between participants over time."],
         ["Sequence vs communication", "Sequence emphasises time/order; communication emphasises objects and links."],
         ["Actor vs class", "An actor is external to the system (Student); a class is a type inside the model (StudentAccount)."]],
        widths=[0.3 * DOC_W, 0.7 * DOC_W]))

    # ============ PRACTICAL & TUTORIAL ============
    s.append(H1("17.  Practical Lab and Tutorial"))
    s += [P("<b>Practical — University Online Course Registration System:</b> identify at least four "
            "actors (Student, Lecturer, Administrator, Payment Gateway) and eight use cases (Login, "
            "Register Course, Drop Course, View Timetable, Make Payment, View Results, Enter Marks, "
            "Generate Report); draw a complete use-case diagram with a system boundary, associations, at "
            "least one include, one extend and one generalisation; write a full specification for Register "
            "Course; draw an activity diagram with decisions, alternative paths and swimlanes; draw a "
            "sequence diagram (Student, Registration Interface, Registration Controller, Course Database) "
            "with at least eight messages; and represent the same scenario as a numbered communication "
            "diagram."),
          P("<b>Tutorial:</b> (1) for an ATM system identify at least three actors, six use cases and one "
            "external system; (2) explain include vs extend vs generalisation with practical examples; "
            "(3) decide whether an activity diagram or a sequence diagram best fits a given workflow or "
            "message exchange; (4) explain why a sequence diagram should model a specific scenario rather "
            "than an entire system in one enormous diagram.")]

    # ============ EXAM QUESTIONS ============
    s.append(H1("18.  Examination-Style Questions"))
    s += [P("<b>Question 1 (Definitions).</b> Define behavioural modelling, use case, actor, interaction "
            "diagram, sequence diagram, communication diagram and activity diagram. [14 marks]"),
          P("<b>Question 2 (Comparison).</b> Differentiate between: use case and use case diagram; "
            "activity diagram and sequence diagram; sequence diagram and communication diagram; include "
            "and extend. [20 marks]"),
          P("<b>Question 3 (Design).</b> A university wants an online examination system where students "
            "log in, view examinations, start an examination, answer questions, submit answers and receive "
            "confirmation, and lecturers create examinations, enter questions, view submissions and "
            "generate results. Identify the actors and use cases, draw a use-case diagram, write a use-case "
            "specification for Start Examination, draw an activity diagram for Submit Examination, and "
            "draw a sequence diagram for Start Examination.")]

    # ============ SUMMARY ============
    s.append(H1("19.  Week 8 Summary and Key Terms"))
    s.append(DTABLE(
        ["Concept", "Meaning"],
        [["Behavioural modelling", "Models system behaviour — the registration process."],
         ["Use case / actor", "A user/system goal · an external role."],
         ["System boundary", "The rectangle defining system scope."],
         ["include / extend", "Required/reused behaviour · conditional additional behaviour."],
         ["Sequence diagram", "Messages in time order (lifelines, activation bars)."],
         ["Communication diagram", "Objects and numbered messages (collaboration)."],
         ["Activity diagram", "A workflow with decisions, forks/joins and swimlanes."],
         ["Use-case specification", "The detailed textual behaviour inside a use case."],
         ["Full analysis documentation", "All models + descriptions, with traceability."]],
        widths=[0.32 * DOC_W, 0.68 * DOC_W]))
    s.append(CALLOUT("THE BIG PICTURE",
        ["A system is not just a collection of classes — it is a collection of behaviours performed by "
         "users and software objects working together to achieve goals. From “I need a registration "
         "system”: <b>Who?</b> Student → <b>What goal?</b> Register Course → <b>What workflow?</b> "
         "activity diagram → <b>Which objects interact?</b> sequence diagram → <b>How are they "
         "connected?</b> communication diagram → <b>What does the complete requirement say?</b> full "
         "analysis documentation. The OMG UML 2.5.1 specification remains the key normative reference for "
         "these constructs."]))

    # ============ REFERENCES ============
    s.append(H1("20.  References and Further Reading"))
    s.append(H2("Primary authoritative reference"))
    s += BUL([
        "Object Management Group. (2017). <i>OMG Unified Modeling Language (UML), Version 2.5.1.</i> OMG — the formal specification, including use cases, sequence diagrams, communication diagrams and activity diagrams.",
        "Object Management Group. <i>UML</i> — official UML resources, specifications and guidance.",
    ])
    s.append(H2("Additional behavioural modelling references"))
    s += BUL([
        "Microsoft. <i>UML diagrams in Visio</i> — overview of sequence, activity, state-machine, use-case and communication diagrams.",
        "NILUS Consulting. (2026). <i>Object-Oriented Analysis and Design Using UML — Behavioral Modeling with Sequence, Activity, and State Diagrams.</i>",
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
