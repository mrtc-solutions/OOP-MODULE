"""
Week 3 PDF content — MODELLING LANGUAGE: UML.
"""
from pdfengine import (H1, H2, P, BUL, FIG, CALLOUT, DTABLE, build, DOC_W)

CFG = {
    "week": 3,
    "title": "Modelling Language — UML",
    "filename": "Week3_Module_BICT3202_OOAD.pdf",
}


def story():
    s = []

    # 1. overview -----------------------------------------------------------
    s.append(H1("1.  Week 3 Overview"))
    s += [P("Week 1 moved us from business problems to business needs and software requirements. Week 2 "
            "taught us to think about the problem in terms of objects, classes, attributes, behaviour, "
            "relationships, abstraction, encapsulation, modularity and complexity management."),
          P("Now we face a practical problem: <b>how do we communicate all these models in a standard way</b> "
            "so that analysts, developers, clients and other stakeholders can understand them? The answer is "
            "<b>UML — the Unified Modeling Language</b>."),
          P("The course outline places five topics here: an overview of UML, the building blocks of UML, the "
            "rules of UML, the mechanisms of UML, and UML architecture. These form the conceptual foundation "
            "needed before drawing formal UML diagrams."),
          P("The Object Management Group (OMG) describes UML as a standard language for visualising, "
            "specifying and documenting software and systems, including their structures, behaviours and "
            "processes. The current formal specification listed by OMG is <b>UML 2.5.1</b>, adopted in "
            "December 2017.")]

    # 2. learning outcomes ----------------------------------------------------
    s.append(H1("2.  Learning Outcomes"))
    s += [P("By the end of this week, students should be able to:")]
    s += BUL([
        "Define UML and explain why it is used in OOAD.",
        "Explain the difference between a modelling language and a development methodology.",
        "Explain what UML can and cannot do.",
        "Identify the major building blocks — things, relationships and diagrams.",
        "Explain structural, behavioural, grouping and annotational elements.",
        "Identify major UML diagram categories and explain their purposes.",
        "Explain UML rules, well-formedness, syntax and semantics.",
        "Explain the common mechanisms — specifications, adornments, common divisions and extensibility.",
        "Explain stereotypes, tagged values and constraints.",
        "Explain the four-layer UML architecture (M0–M3) and why it matters.",
        "Apply UML concepts to a university registration system.",
    ])

    # 3. what is UML -----------------------------------------------------------
    s.append(H1("3.  What Is UML?"))
    s += [P("UML stands for <b>Unified Modeling Language</b>. Break the name into three parts: "
            "<b>Unified</b> — it brought together ideas from several earlier object-oriented modelling "
            "approaches; <b>Modeling</b> — it is used to create representations of systems; "
            "<b>Language</b> — it provides defined concepts and notation for communicating those "
            "representations.")]
    s.append(CALLOUT("DEFINITION",
        ["UML is a standardised modelling language used to represent, communicate and document systems."]))
    s += [P("<b>What problem does UML solve?</b> Imagine five people developing a university system — a "
            "business analyst, a software architect, a programmer, a database designer and an administrator. "
            "The analyst says “The Student is associated with a Course.” The programmer asks what "
            "“associated” means; the administrator thought a student could register for many courses; the "
            "database designer asks whether it is one-to-many or many-to-many. A UML diagram makes the "
            "intended structure <b>visible</b>, giving the team something concrete to discuss.")]

    # 4. what UML is NOT --------------------------------------------------------
    s.append(H1("4.  What UML Is Not"))
    s.append(H2("4.1  Not a Programming Language"))
    s += [P("Students sometimes hear “language” and assume UML is like Java, Python, C++ or JavaScript. It is "
            "not. A programming language tells a computer how to execute instructions; UML tells humans and "
            "modelling tools how to represent and communicate the structure and behaviour of a system.")]
    s.append(H2("4.2  Not a Development Methodology"))
    s += [P("A modelling language answers <b>“How do I represent the system?”</b>. A development methodology "
            "answers <b>“What activities should we perform, in what order, and how should the system be "
            "developed?”</b> UML itself does not prescribe one complete software development process; "
            "processes such as the Unified Process (UP) can use UML.")]
    s.append(CALLOUT("KEY DISTINCTION",
        ["UML = modelling language.     UP / USDP = development process (studied in Weeks 12–13)."]))
    s.append(H2("4.3  Not Only for Software"))
    s += [P("Although UML is heavily associated with software engineering, it can also model business "
            "processes, organisational structures, workflows and non-software systems. A hospital workflow "
            "can be modelled before deciding exactly what software will implement it.")]

    # 5. why UML matters ---------------------------------------------------------
    s.append(H1("5.  Why UML Is Important in OOAD"))
    s += BUL([
        "<b>Understand requirements</b> — use cases represent what users expect.",
        "<b>Model structure</b> — class diagrams show classes and relationships.",
        "<b>Model behaviour</b> — state and activity diagrams represent change and workflows.",
        "<b>Model interactions</b> — sequence and communication diagrams show how objects communicate.",
        "<b>Communicate designs</b> — all stakeholders discuss the same model.",
        "<b>Document systems</b> — models become technical documentation.",
        "<b>Support maintenance</b> — future developers read the models to understand the system.",
    ])
    s.append(CALLOUT("ONE DIAGRAM CANNOT EXPLAIN EVERYTHING",
        ["A single diagram cannot show all classes, users, workflows, interactions, databases, servers, states "
         "and requirements at once. UML therefore provides <b>different diagram types for different "
         "perspectives</b> — a principle known as using multiple views/models."]))

    # 6. building blocks ----------------------------------------------------------
    s.append(H1("6.  The Building Blocks of UML"))
    s += [P("The classic conceptual way of learning UML (the framework of Booch, Rumbaugh and Jacobson) is to "
            "think in terms of three building blocks: <b>Things</b>, <b>Relationships</b> and <b>Diagrams</b>.")]
    s += FIG("w3_three_blocks.png", "Figure 1 — The three conceptual building blocks of UML")

    # 7. things ----------------------------------------------------------------------
    s.append(H1("7.  Building Block 1 — Things"))
    s += [P("A <b>thing</b> is an important modelling element or abstraction. For teaching purposes, things "
            "are grouped into <b>structural</b>, <b>behavioural</b>, <b>grouping</b> and <b>annotational</b>.")]
    s += FIG("w3_things.png", "Figure 2 — The four kinds of UML things")

    s.append(H2("7.1  Structural Things"))
    s += [P("Structural things answer <b>“What exists?”</b> and include classes, interfaces, objects, "
            "components and nodes."),
          P("A <b>class</b> represents a set/type of objects sharing common characteristics and behaviour — "
            "shown as a three-compartment box: name, attributes and operations.")]
    s += FIG("w3_class_example.png", "Figure 3 — A UML class with its three compartments and visibility adornments")
    s += [P("An <b>interface</b> specifies a set of operations that a class or component can provide; "
            "different providers can implement it differently (BankPayment, MobileMoneyPayment, CardPayment "
            "all realising PaymentService). An <b>object</b> is a particular instance (student001 : Student). "
            "A <b>component</b> is a modular, replaceable part of a system. A <b>node</b> is a computational "
            "or physical resource — a server, device or execution environment — used in deployment diagrams.")]
    s += FIG("w3_interface.png", "Figure 4 — An interface and three alternative realizations")

    s.append(H2("7.2  Behavioural, Grouping and Annotational Things"))
    s += [P("<b>Behavioural things</b> answer <b>“What happens?”</b> — interactions, activities and state "
            "machines. <b>Grouping things</b> organise other elements; the most important is the "
            "<b>package</b>, which groups related elements (Student Management, Finance, Examination "
            "packages). <b>Annotational things</b> add extra information — the simplest is a <b>note</b>, "
            "used to explain a business rule, constraint or design decision.")]
    s += FIG("w3_package.png", "Figure 5 — Packages group model elements and manage large models")

    # 8. relationships ------------------------------------------------------------------
    s.append(H1("8.  Building Block 2 — Relationships"))
    s += [P("Relationships connect modelling elements. The four important UML relationships are "
            "<b>association</b>, <b>dependency</b>, <b>generalization</b> and <b>realization</b> "
            "(with include/extend in use cases and aggregation/composition in structural modelling coming later).")]
    s += FIG("w3_relationships.png", "Figure 6 — The four main UML relationship types")
    s += [P("<b>Association</b> is a structural relationship between classifiers "
            "(Student — registers for — Course). <b>Dependency</b> (dashed open arrow) means one element "
            "depends on another. <b>Generalization</b> (hollow triangle to the general classifier) is a "
            "general-to-specific relationship — Student and Lecturer are specialised types of User. "
            "<b>Realization</b> (dashed hollow triangle) means a classifier fulfils a contract, commonly an "
            "interface.")]
    s.append(H2("8.1  Multiplicity"))
    s += [P("An association can specify how many instances participate. "
            "<b>Student 1 ——— 0..* Course</b> means one Student can be associated with zero or many Courses.")]
    s += FIG("w3_multiplicity.png", "Figure 7 — Multiplicity notation and its meaning")

    # 9. diagrams ------------------------------------------------------------------------
    s.append(H1("9.  Building Block 3 — Diagrams"))
    s += [P("A <b>diagram</b> provides a visual representation of selected parts of a model. The important "
            "point: <b>a diagram is a view of a model, not necessarily the entire model</b> — which is why "
            "large systems require multiple diagrams.")]
    s += FIG("w3_diagram_map.png", "Figure 8 — The UML diagram families")
    s += FIG("w3_chart_diagram_counts.png", "Figure 9 — Diagram types per family (per OMG UML 2.5.1)")
    s.append(DTABLE(
        ["Diagram", "Main question"],
        [["Use Case", "What does the user want to accomplish?"],
         ["Class", "What structural elements exist?"],
         ["Object", "What are particular instances?"],
         ["Sequence", "How do participants communicate over time?"],
         ["Communication", "Which objects communicate and how?"],
         ["Activity", "What workflow occurs?"],
         ["State Machine", "How does an entity change state?"],
         ["Component", "What major software components exist?"],
         ["Deployment", "Where does the software run?"],
         ["Package", "How are model elements organised?"]],
        widths=[0.34 * DOC_W, 0.66 * DOC_W]))
    s.append(H2("9.1  Example Diagrams"))
    s += FIG("w3_use_case.png", "Figure 10 — Use-case diagram: what users can accomplish")
    s += FIG("w3_sequence.png", "Figure 11 — Sequence diagram: who communicates, in what order")
    s += FIG("w3_activity.png", "Figure 12 — Activity diagram: the workflow of a process")
    s += FIG("w3_state_machine.png", "Figure 13 — State machine: how an object changes state")
    s += FIG("w3_component.png", "Figure 14 — Component diagram: major software components")
    s += FIG("w3_deployment.png", "Figure 15 — Deployment diagram: where software runs")

    # 10. rules of UML ---------------------------------------------------------------------
    s.append(H1("10.  Rules of UML"))
    s += [P("UML is not simply a collection of shapes — there are rules governing what elements mean, how "
            "they relate, how notation is used, and what constitutes a well-formed model."),
          P("<b>Syntax</b> concerns how something is represented (<i>how is it drawn?</i>); <b>semantics</b> "
            "concerns what it means (<i>what does the representation mean?</i>). A diagram can look "
            "attractive yet communicate the wrong meaning.")]
    s.append(CALLOUT("WELL-FORMEDNESS",
        ["A model is <b>well-formed</b> when it satisfies the relevant rules of the modelling language. You "
         "cannot arbitrarily connect unrelated elements and claim the result has the intended UML meaning."]))
    s.append(CALLOUT("FOUR QUESTIONS WHEN CHECKING A MODEL",
        ["1. Is the notation correct?   2. Does the relationship make semantic sense?   "
         "3. Does the model satisfy the requirements?   4. Can another person understand it?  — All four matter."]))

    # 11. common mechanisms -------------------------------------------------------------------
    s.append(H1("11.  UML Common Mechanisms"))
    s += FIG("w3_mechanisms.png", "Figure 16 — The four common mechanisms")
    s += [P("<b>Specifications:</b> a graphical symbol is not the complete definition — behind the Student "
            "box lies a specification of name, attributes, operations, visibility, relationships and "
            "constraints. <b>Adornments:</b> extra information on a symbol (the − and + visibility markers, "
            "stereotypes, multiplicity, constraints). <b>Common divisions:</b> paired distinctions such as "
            "class↔object and interface↔implementation. <b>Extensibility:</b> mechanisms for customising UML "
            "for particular domains.")]
    s.append(H2("11.1  Extensibility — Stereotypes, Tagged Values, Constraints"))
    s += [P("A <b>stereotype</b> gives an element a more specialised meaning — "
            "<font name='Mono'>«entity»</font> Student, <font name='Mono'>«controller»</font> "
            "RegistrationController, <font name='Mono'>«boundary»</font> RegistrationPage. A <b>tagged "
            "value</b> provides additional property information — {author = \"Analysis Team\"}, "
            "{location = \"Data Centre\"}. A <b>constraint</b> is a condition that must be satisfied — "
            "{age ≥ 18}, {balance ≥ 0}, or {student must satisfy prerequisite}. Constraints make rules "
            "explicit: Student—registers—Course alone does not say that the prerequisite must have been "
            "passed; {PrerequisiteSatisfied = true} does.")]

    # 12. UML architecture -----------------------------------------------------------------------
    s.append(H1("12.  UML Architecture — the Four Layers"))
    s += [P("“UML architecture” here means the architectural organisation of the UML language itself — its "
            "layered meta-modelling structure — <b>not</b> three-tier or client-server software architecture. "
            "The four commonly discussed levels are M3 → M2 → M1 → M0.")]
    s += FIG("w3_architecture.png", "Figure 17 — The four-layer meta-modelling stack")
    s += [P("<b>M0 — instances:</b> actual things — Francis : Student, Grace : Student, BICT 3202 : Course. "
            "<b>M1 — model:</b> your UML model (Student, Course, Registration). <b>M2 — metamodel:</b> the "
            "UML concepts themselves (Class, Property, Operation, Association, Generalization, UseCase, "
            "Actor, State, Activity). <b>M3 — meta-metamodel:</b> the language/framework used to define "
            "metamodels — the Meta Object Facility (MOF).")]
    s.append(CALLOUT("WHY IT MATTERS",
        ["The layers explain why UML is a formal language, why tools can validate models, why UML has "
         "consistent semantics, and how modelling languages themselves are defined. For introductory "
         "modelling you can draw class diagrams without mastering this — but understanding it helps in "
         "advanced model-driven engineering. <b>Do not confuse UML architecture with software "
         "architecture</b> — a common examination trap."]))

    # 13. worked example + activities -----------------------------------------------------------
    s.append(H1("13.  Worked Example — University Registration"))
    s += [P("For the requirement “Students should be able to register for courses online,” the same system can "
            "be shown from five UML perspectives: a <b>use-case</b> diagram (Student — Register Course), a "
            "<b>class</b> model (Student, Course with attributes and the registers relationship), a "
            "<b>sequence</b> diagram (Student → System → Course), an <b>activity</b> diagram (Login → Select "
            "Course → Check Prerequisite → Eligible? → Register → Confirm), and a <b>state</b> diagram "
            "(Draft → Submitted → Approved → Completed). Each answers a different question.")]
    s.append(H2("13.1  Practical Session — Introduction to UML Modelling"))
    s += [P("Using a UML CASE tool, a web-based UML tool or diagramming software with UML support, create a "
            "class diagram containing Student, Course, Lecturer and Registration. Then add attributes "
            "(Student: studentID, name, programme; Course: courseCode, courseName, credits; Lecturer: "
            "lecturerID, name, department; Registration: registrationID, date, status), add relationships "
            "(Student—Registration, Course—Registration, Lecturer—Course), and finally add multiplicities — "
            "reasoning about whether Student 1 ——— 0..* Registration and Course 1 ——— 0..* Registration make "
            "sense.")]
    s.append(H2("13.2  Tutorial — “Which Diagram Should I Use?”"))
    s.append(DTABLE(
        ["Scenario", "Expected diagram"],
        [["What functions can a student perform?", "Use Case"],
         ["What classes and relationships exist?", "Class"],
         ["The order in which student, system and database communicate?", "Sequence"],
         ["The steps involved in registering a course?", "Activity"],
         ["The different states of an application?", "State Machine"],
         ["Where application components are deployed?", "Deployment"]],
        widths=[0.62 * DOC_W, 0.38 * DOC_W]))

    # 14. independent learning --------------------------------------------------------------------
    s.append(H1("14.  Independent Learning (10 Hours)"))
    s += BUL([
        "<b>Read</b> — the OMG UML 2.5.1 specification (the authoritative formal reference; it is not a beginner textbook — read it non-sequentially as the introduction advises).",
        "<b>Tabulate</b> — create a table of at least 10 UML diagram types: what it represents, the question it answers, when it is useful, and a university example.",
        "<b>Map</b> — take the Week 1–2 University Registration System and identify which diagram you would use for requirements, structure, workflow, interaction, lifecycle and deployment.",
    ])

    # 15. summary ------------------------------------------------------------------------------------
    s.append(H1("15.  Week 3 Summary"))
    s.append(DTABLE(
        ["Concept", "Meaning"],
        [["UML", "Unified Modeling Language — a standardised modelling language for visualising, specifying and documenting systems."],
         ["UML is not", "a programming language, a database, a development methodology, or a replacement for requirements analysis."],
         ["Building blocks", "Things · Relationships · Diagrams."],
         ["Things", "Structural, behavioural, grouping (package) and annotational (note)."],
         ["Relationships", "Association, dependency, generalization, realization."],
         ["Diagrams", "Different views of the same system."],
         ["Rules", "Syntax, semantics and well-formedness."],
         ["Common mechanisms", "Specifications, adornments, common divisions, extensibility."],
         ["Extensibility", "Stereotypes, tagged values, constraints."],
         ["Architecture", "M3 meta-metamodel → M2 metamodel → M1 model → M0 instances."]],
        widths=[0.26 * DOC_W, 0.74 * DOC_W]))
    s.append(CALLOUT("THE MOST IMPORTANT LESSON",
        ["UML is not about drawing pretty diagrams — it is a standardised language for communicating models "
         "of a system. Different diagrams answer different questions: what exists, how things relate, what "
         "users can do, what happens, how objects communicate, how an object changes state, what components "
         "exist, and where software runs. This prepares us for Week 4, which goes deeper into UML building "
         "blocks, rules, mechanisms and architecture before formal object/class modelling in Week 5."]))

    # 16. examination questions -----------------------------------------------------------------------
    s.append(H1("16.  Examination-Style Questions"))
    s += [P("<b>Question 1.</b> Define UML and explain its importance in OOAD (mention: Unified Modeling "
            "Language, modelling language, standardisation, visualisation, specification, documentation, "
            "communication, structure and behaviour)."),
          P("<b>Question 2.</b> Differentiate between a modelling language and a software development "
            "methodology, using UML and UP as examples."),
          P("<b>Question 3.</b> Explain the three conceptual building blocks of UML."),
          P("<b>Question 4.</b> Explain structural, behavioural, grouping and annotational elements, with examples."),
          P("<b>Question 5.</b> Differentiate between syntax and semantics in UML."),
          P("<b>Question 6.</b> Explain the four common mechanisms of UML."),
          P("<b>Question 7.</b> Explain the UML four-layer architecture using a practical example."),
          P("<b>Challenge.</b> A university wants a mobile registration application (log in, view courses, "
            "register, drop, view status) that talks to a server and database. For each requirement, choose "
            "the most appropriate UML diagram and justify your choice.")]

    # 17. references -----------------------------------------------------------------------------------
    s.append(H1("17.  References and Further Reading"))
    s.append(H2("Authoritative / current sources"))
    s += BUL([
        "Object Management Group. (2017). <i>OMG Unified Modeling Language (OMG UML), Version 2.5.1.</i> OMG.",
        "Object Management Group. (n.d.). <i>Unified Modeling Language (UML)</i>; <i>What is UML?</i>; <i>Introduction to OMG Specifications.</i> OMG.",
        "Object Management Group. (2017). <i>Meta Object Facility (MOF), Version 2.5.1.</i> OMG.",
    ])
    s.append(H2("Classic OOAD reference"))
    s += BUL([
        "Booch, G., Rumbaugh, J., & Jacobson, I. (1999). <i>The Unified Modeling Language User Guide.</i> Addison-Wesley.",
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
