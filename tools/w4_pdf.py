"""
Week 4 PDF content — UML BUILDING BLOCKS, RULES, MECHANISMS AND ARCHITECTURE.
"""
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph
from pdfengine import (H1, H2, P, BUL, FIG, CALLOUT, DTABLE, build, DOC_W,
                      C_MAROON, C_SOFT)

CFG = {
    "week": 4,
    "title": "UML Building Blocks, Rules, Mechanisms and Architecture",
    "filename": "Week4_Module_BICT3202_OOAD.pdf",
}


def story():
    s = []

    # 1. introduction --------------------------------------------------------
    s.append(H1("1.  Week 4 Introduction"))
    s += [P("Week 3 introduced UML and answered the basic question: <b>what is UML and why do we need "
            "it?</b> UML is a standardised modelling language used to visualise, specify and document "
            "systems; the current formal OMG specification is <b>UML 2.5.1</b>, which defines the language "
            "through abstract syntax, semantics, notation and examples."),
          P("This week we go one level deeper. The course outline specifically requires the <b>building "
            "blocks of UML</b>, the <b>rules of UML</b>, the <b>mechanisms of UML</b> and <b>UML "
            "architecture</b>. By the end of Week 4, students should understand what UML is made of, how "
            "its notation works, how models are governed by rules, and how UML is organised conceptually.")]

    # 2. learning outcomes -----------------------------------------------------
    s.append(H1("2.  Learning Outcomes"))
    s += [P("By the end of this week, a student should be able to:")]
    s += BUL([
        "Explain the building blocks of UML and identify different types of UML elements.",
        "Explain structural, behavioural, grouping and annotational things.",
        "Explain relationships and distinguish association, dependency, generalization and realization.",
        "Explain the role of UML diagrams and the structural vs behavioural distinction.",
        "Explain UML notation (syntax), semantics and well-formedness.",
        "Explain specifications, adornments and common divisions.",
        "Explain extensibility mechanisms — stereotypes, tagged values, constraints and profiles.",
        "Explain UML's layered architecture and distinguish M0, M1, M2 and M3.",
        "Apply these concepts to a practical university information system.",
        "Identify common mistakes students make when drawing UML.",
    ])

    # 3. five questions ----------------------------------------------------------
    s.append(H1("3.  A Simple Way to Understand UML"))
    s += [P("Before technical definitions, imagine we want to build a University Student Management "
            "System. We need to answer several questions: <b>what exists?</b> (Student, Lecturer, Course, "
            "Registration, Payment, Result); <b>how are things related?</b> (Student — registers for — "
            "Course); <b>what can users do?</b> (Register Course, View Results, Pay Fees); <b>what "
            "happens?</b> (Login → Select → Check Prerequisite → Register → Confirmation); and <b>how do "
            "objects communicate?</b> (Student → Registration System → Database).")]
    s += FIG("w4_five_questions.png", "Figure 1 — Five questions UML helps you answer")

    # 4. building blocks -----------------------------------------------------------
    s.append(H1("4.  UML Building Blocks"))
    s += [P("A useful way to understand UML is to divide its building blocks into <b>Things</b>, "
            "<b>Relationships</b> and <b>Diagrams</b>. The traditional treatment further divides "
            "“things” into <b>structural</b>, <b>behavioural</b>, <b>grouping</b> and <b>annotational</b> "
            "things — a classification that prevents students from seeing UML as a collection of random "
            "shapes.")]

    # 5. structural things -----------------------------------------------------------
    s.append(H1("5.  Structural Things"))
    s += [P("Structural things represent the relatively static parts of a system — ask <b>“What exists in "
            "the system?”</b> Examples include <b>class</b>, <b>interface</b>, <b>object</b>, "
            "<b>component</b> and <b>node</b>."),
          P("A <b>class</b> describes a type of object, shown as a three-section box (name, attributes, "
            "operations). An <b>object</b> is a particular instance of a class — written "
            "<font name='Mono'>student001 : Student</font> with an underlined name. An <b>interface</b> "
            "defines a set of operations that another element agrees to provide; different implementations "
            "(BankPayment, MobileMoney, CardPayment) can realise it. A <b>component</b> is a modular part "
            "of a system with a clear responsibility (connecting to Week 2's modularity). A <b>node</b> is "
            "a computational resource or execution environment — a mobile phone, an application server or "
            "a database server — used in deployment diagrams.")]
    s += FIG("w4_structural_things.png", "Figure 2 — The five structural things")
    s += FIG("w4_class_vs_object.png", "Figure 3 — Class vs object: the cake-mould analogy")

    # 6. behavioural, grouping, annotational ----------------------------------------
    s.append(H1("6.  Behavioural, Grouping and Annotational Things"))
    s += [P("<b>Behavioural things</b> answer <b>“What happens?”</b> and include <b>interactions</b> "
            "(communication between elements — who communicates with whom and what messages are "
            "exchanged), <b>activities</b> (workflows, such as course registration from Login to "
            "Confirmation) and <b>state machines</b> (how an object changes state — Draft → Submitted → "
            "Under Review → Approved → Completed, where a <b>state</b> plus an <b>event</b> causes a "
            "<b>transition</b>)."),
          P("<b>Grouping things</b> organise other elements. The most important is the <b>package</b>: a "
            "university model with 150 classes is grouped into Student Management, Finance and Examination "
            "packages, making a large model manageable."),
          P("<b>Annotational things</b> provide explanatory information — the simplest is a <b>note</b>, "
            "which does not represent a new business object but explains something about the model (for "
            "example, “Student must satisfy all course prerequisites before registration”).")]

    # 7. relationships ------------------------------------------------------------------
    s.append(H1("7.  Relationships in UML"))
    s += [P("A relationship tells us how model elements are connected. The four important relationships "
            "are <b>association</b>, <b>dependency</b>, <b>generalization</b> and <b>realization</b> — "
            "and they must not be confused with one another."),
          P("<b>Association</b> — “these elements are related” (Student ——— Course, named “registers "
            "for”). <b>Dependency</b> — “this element uses that element” (ReportGenerator - - - > "
            "Payment); if Payment changes, ReportGenerator may be affected. <b>Generalization</b> — “this "
            "is a specialised type of that” (Student and Lecturer are specialised forms of User; a Car is "
            "a Vehicle but a Vehicle is not necessarily a Car). <b>Realization</b> — “this element fulfils "
            "the contract” (MobilePayment realises the PaymentService interface; the interface is the "
            "contract, the implementation fulfils it).")]
    s += FIG("w4_relationships.png", "Figure 4 — The four relationship types with their notation")
    s.append(CALLOUT("AN IMPORTANT OOAD INSIGHT",
        ["Student 1 ——— 0..* Course says one Student relates to zero or many Courses. But in a realistic "
         "system the relationship may need its own <b>Registration</b> class, because registration has "
         "information of its own — registrationDate, status, semester, grade. <b>When a relationship has "
         "important data or behaviour, it may need to become a class.</b>"]))
    s += FIG("w4_association_class.png", "Figure 5 — When a relationship deserves its own class")

    # 8. diagrams --------------------------------------------------------------------------
    s.append(H1("8.  UML Diagrams"))
    s += [P("A diagram is a particular visual view of a model — <b>not necessarily the whole system</b>. "
            "Structural diagrams (class, object, component, composite structure, package, deployment) ask "
            "<b>“What exists?”</b>; behavioural diagrams (use case, activity, state machine) ask "
            "<b>“What happens?”</b>; interaction diagrams (sequence, communication, interaction overview, "
            "timing) are a specialised behavioural family.")]
    s += FIG("w4_model_vs_diagram.png", "Figure 6 — One model, many diagrams")

    # 9. rules of UML --------------------------------------------------------------------------
    s.append(H1("9.  Rules of UML"))
    s += [P("Students sometimes think “if I draw boxes and arrows, I have created UML.” Not necessarily — "
            "UML has defined concepts, notation and semantics. <b>Syntax</b> concerns how something is "
            "represented (how a class box is drawn); <b>semantics</b> concerns what it means (a line "
            "between Student and Course is not decoration but a specific relationship)."),
          P("If a student draws <font name='Mono'>Student ◇──── Course</font> and says “the diamond means "
            "they are connected”, the lecturer must ask whether they understand what that diamond means — "
            "it has a specific UML meaning (aggregation/composition). Symbols should never be chosen "
            "because “they look nice”. UML notation must be learned together with its meaning.")]
    s.append(CALLOUT("WELL-FORMED MODELS",
        ["A well-formed model follows the relevant rules. A model can fail as a <b>notation error</b> (the "
         "symbol is drawn incorrectly), a <b>semantic error</b> (the symbol is recognisable but "
         "communicates the wrong meaning), or a <b>requirement error</b> (valid UML, but not what the "
         "system actually needs). A perfectly drawn diagram can still describe the wrong system."]))
    s += FIG("w4_wellformed.png", "Figure 7 — Three ways a model can fail")
    s += FIG("w4_checklist.png", "Figure 8 — The seven-question UML quality checklist")

    # 10. mechanisms ----------------------------------------------------------------------------
    s.append(H1("10.  Mechanisms of UML"))
    s += [P("Traditional UML teaching introduces four common mechanisms: <b>specifications</b>, "
            "<b>adornments</b>, <b>common divisions</b> and <b>extensibility mechanisms</b>."),
          P("<b>Specification:</b> a diagram is a view of a richer underlying model — the Student box does "
            "not show every property; behind it lies the full specification (name, attributes, operations, "
            "relationships). <b>Adornments:</b> extra information attached to a basic element — the − and + "
            "visibility markers, multiplicity, constraints and modifiers. <b>Common divisions:</b> paired "
            "distinctions such as class↔object (type vs instance — a cake mould vs an individual cake) and "
            "interface↔implementation (contract vs behaviour).")]
    s += FIG("w4_visibility.png", "Figure 9 — Adornments: visibility symbols")
    s.append(CALLOUT("VISIBILITY SYMBOLS", ["+ public · − private · # protected · ~ package"]))
    s += [P("<b>Extensibility mechanisms</b> let UML be customised for domains such as banking, "
            "healthcare, telecommunications, education, manufacturing and cybersecurity. Three important "
            "concepts are <b>stereotypes</b>, <b>tagged values</b> and <b>constraints</b>.")]
    s += FIG("w4_stereotypes.png", "Figure 10 — Stereotypes: «entity», «controller», «boundary»")
    s += [P("A <b>stereotype</b> gives an element a specialised meaning, written in guillemets — "
            "<font name='Mono'>«entity»</font> Student, <font name='Mono'>«controller»</font> "
            "RegistrationController, <font name='Mono'>«boundary»</font> RegistrationPage. A <b>tagged "
            "value</b> adds property/metadata — {location = \"Main Data Centre\"}, {author = \"Analysis "
            "Team\"}. A <b>constraint</b> states a condition that must hold — {age ≥ 18}, "
            "{prerequisiteSatisfied = true}. Without the constraint, a Student—Course diagram shows the "
            "relationship but not the rule governing it.")]
    s += FIG("w4_extensibility.png", "Figure 11 — Stereotype vs tagged value vs constraint")
    s.append(CALLOUT("UML PROFILES",
        ["A <b>profile</b> tailors UML for a particular domain or purpose (real-time systems, business "
         "processes, security, enterprise architecture), defining stereotypes and associated extensions. "
         "<b>UML = general modelling language; profile = customised UML vocabulary/rules for a domain.</b> "
         "UML 2.5.1 includes a standard profile as a normative machine-readable artefact."]))

    # 11. architecture ---------------------------------------------------------------------------
    s.append(H1("11.  UML Architecture — a Deeper Look"))
    s += [P("Week 3 introduced the four layers M0–M3. This week we make them clearer."),
          P("<b>M0 — instance level:</b> actual objects — Francis : Student, Grace : Student, John : Student.<br/>"
            "<b>M1 — model level:</b> the model we create for our system — Student, with studentID and name.<br/>"
            "<b>M2 — metamodel level:</b> the UML concepts themselves — Class, Property, Operation, Association, Generalization.<br/>"
            "<b>M3 — meta-metamodel:</b> the foundation used to define metamodels — the Meta Object Facility (MOF).",
            style="bodyL")]
    s += FIG("w4_architecture_analogy.png", "Figure 12 — The M0–M3 language analogy and context-dependent levels")
    s += [P("Students often ask “Is Student M0, M1 or M2?” The answer depends on context: "
            "<font name='Mono'>Student : Class</font> is an M1 model element, but <font name='Mono'>Class</font> "
            "as a UML concept belongs to the M2 metamodel, while <font name='Mono'>Francis : Student</font> is "
            "an M0 instance. The same word can live at different levels.")]
    s.append(CALLOUT("EXAMINATION TRAP",
        ["<b>UML architecture ≠ software architecture.</b> UML architecture is the M3/M2/M1/M0 meta-modelling "
         "hierarchy of the language itself; software architecture is how software is organised "
         "(Presentation → Business Logic → Data Access → Database). They are different concepts."]))

    # 12. model vs diagram + views ----------------------------------------------------------------
    s.append(H1("12.  Model vs Diagram — Multiple Views"))
    s += [P("A <b>UML model</b> is the underlying collection of elements and relationships; a <b>UML "
            "diagram</b> is a visual view of selected elements. One model can support many views — which "
            "is why UML suits complex systems.")]
    s += FIG("w4_multiview.png", "Figure 13 — One banking system, five views")
    s += [P("UML is also a <b>communication tool</b>: when a client says “Students should register for "
            "courses”, the analyst draws (Student) ——— (Register Course); the developer asks “what if the "
            "course is full?”, the analyst updates the model, and another rule is added. A model gives "
            "stakeholders something to discuss <b>before</b> expensive implementation begins."),
          P("UML connects directly to <b>abstraction</b>: a real university has 10,000 students, 500 "
            "courses, 300 lecturers and 50 departments, but we model just Student, Course, Lecturer and "
            "Department — a manageable representation. UML also connects to <b>complexity management</b>: "
            "rather than putting 13+ classes in one unreadable diagram, we divide them into Student "
            "Management, Finance, Examination, Library and Accommodation packages.")]
    s += FIG("w4_chart_abstraction.png", "Figure 14 — The power of abstraction")
    s += FIG("w4_chart_packages.png", "Figure 15 — Grouping classes into packages")

    # 13. common mistakes ---------------------------------------------------------------------------
    s.append(H1("13.  Common Student Mistakes"))
    mistakes = [
        ("Mistake 1 — Generalization arrow points the wrong way.",
         "If Student is a specialised type of User, the hollow triangle must point to User (the general class). A very common beginner error."),
        ("Mistake 2 — Choosing symbols by appearance.",
         "A diamond has a specific meaning (aggregation/composition). “It looks nice” is never a valid reason."),
        ("Mistake 3 — Everything becomes a class.",
         "Name, StudentID, CourseName and RegistrationDate are not automatically classes. Object identification is analysis, not a grammar exercise — ask whether it has attributes, behaviour, relationships, and whether the system needs to store it."),
        ("Mistake 4 — Overloading the diagram.",
         "Putting Student, Course, Library, Book, Hostel, Food and Transport in one diagram makes it unreadable. Separate related areas into packages/models."),
    ]
    for head, fix in mistakes:
        s.append(CALLOUT(head, [fix], bg=HexColor("#FBF3F3"), bar=C_SOFT, tcol=C_MAROON))
    s += FIG("w4_generalization_mistake.png", "Figure 16 — Correct vs incorrect generalization direction")

    # 14. case study -----------------------------------------------------------------------------------
    s.append(H1("14.  Case Study — University E-Learning System"))
    s += [P("Imagine a university wants an online learning platform. Students can log in, view courses, "
            "download notes, submit assignments and view grades; lecturers can upload notes, create "
            "assignments, mark assignments and publish grades."),
          P("<b>Possible classes:</b> Student, Lecturer, Course, Assignment, Submission, Grade, "
            "LearningMaterial. <b>Relationships:</b> Student—Submission, Student—Course, Lecturer—Course, "
            "Course—Assignment, Assignment—Submission. <b>Behaviour to model:</b> Submit Assignment, Mark "
            "Assignment, Publish Grade. <b>State changes</b> (for a submission): Draft → Submitted → "
            "Marked → Returned.")]
    s += FIG("w4_elearning.png", "Figure 17 — E-learning system: classes, relationships and the Submission lifecycle")

    # 15. activities -----------------------------------------------------------------------------------
    s.append(H1("15.  Practical & Tutorial Activities"))
    s.append(H2("15.1  Practical — University Course Registration"))
    s += [P("Build a small model in steps: <b>(1)</b> identify classes (Student, Course, Lecturer, "
            "Registration); <b>(2)</b> identify attributes (Student: studentID, name, programme, year; "
            "Course: courseCode, courseName, creditHours; Lecturer: lecturerID, name, department; "
            "Registration: registrationID, date, status); <b>(3)</b> identify operations "
            "(registerCourse(), dropCourse(), viewResults(); assignGrade(), viewClassList()); "
            "<b>(4)</b> add relationships (Student—Registration, Registration—Course, Lecturer—Course); "
            "<b>(5)</b> add multiplicity (Student 1 ——— 0..* Registration, Course 1 ——— 0..* "
            "Registration); <b>(6)</b> add a constraint {prerequisiteSatisfied = true}; <b>(7)</b> add a "
            "stereotype where appropriate («entity» Student).")]
    s.append(H2("15.2  Practical — Identify the Relationship"))
    s.append(DTABLE(
        ["Statement", "Relationship"],
        [["A Student is a type of User.", "Generalization (Student ▷ User)"],
         ["A Registration uses information from Course.", "Dependency (if genuinely usage)"],
         ["A Student registers for a Course.", "Association"],
         ["MobilePayment implements PaymentService.", "Realization"]],
        widths=[0.58 * DOC_W, 0.42 * DOC_W]))
    s.append(H2("15.3  Tutorial — Find the Mistake"))
    s += [P("Given a diagram where Student points (hollow triangle) down to User, students must identify "
            "that the generalization arrow should point toward the general class — User at the top, "
            "Student below. This is the most common beginner mistake.")]

    # 16. independent learning ----------------------------------------------------------------------------
    s.append(H1("16.  Independent Learning (10 Hours)"))
    s += BUL([
        "<b>2 hours — Reading:</b> the relevant sections of the OMG UML 2.5.1 specification (a reference, read non-sequentially).",
        "<b>3 hours — Diagram practice:</b> create 2 class diagrams, 2 use-case diagrams, 1 activity diagram and 1 sequence diagram.",
        "<b>2 hours — Relationship practice:</b> association, dependency, generalization, realization.",
        "<b>2 hours — Case study:</b> model a small University Library Management System.",
        "<b>1 hour — Revision:</b> answer the examination questions without looking at notes.",
    ])

    # 17. summary --------------------------------------------------------------------------------------------
    s.append(H1("17.  Week 4 Summary"))
    s.append(DTABLE(
        ["Term", "Meaning"],
        [["UML", "Unified Modeling Language."],
         ["Class / Object", "Description of a type of object / an instance of a class."],
         ["Interface", "Contract defining available operations."],
         ["Component / Node", "Modular system element / computational or execution resource."],
         ["Association", "Structural relationship."],
         ["Dependency", "Usage/dependency relationship."],
         ["Generalization", "General-to-specific relationship."],
         ["Realization", "Implementation of a contract."],
         ["Package / Note", "Grouping mechanism / annotation."],
         ["Stereotype / Tagged value / Constraint", "Specialised meaning / extra metadata / condition or rule."],
         ["Profile", "UML customisation mechanism."],
         ["Syntax / Semantics", "Form and notation / meaning."],
         ["M3 / M2 / M1 / M0", "Meta-metamodel / metamodel / model / instance levels."]],
        widths=[0.34 * DOC_W, 0.66 * DOC_W]))
    s.append(CALLOUT("THE BIG PICTURE — WEEKS 1–4",
        ["Week 1 answered <b>why</b> the organisation needs the system; Week 2 answered <b>what objects "
         "exist</b> and how they relate; Week 3 asked <b>how we communicate</b> these models; Week 4 "
         "establishes <b>UML's foundations</b> — its elements, symbols, rules, extension mechanisms and "
         "organisation. Week 4 is the bridge between understanding UML conceptually and actually using it "
         "to perform Object-Oriented Analysis, which begins in Week 5."]))

    # 18. examination questions -------------------------------------------------------------------------------
    s.append(H1("18.  Examination-Style Questions"))
    s += [P("<b>Question 1 (Short essay).</b> Explain the major building blocks of UML and give an example of each."),
          P("<b>Question 2 (Comparison).</b> Differentiate between association, dependency, generalization and "
            "realization, using diagrams in your answer."),
          P("<b>Question 3 (Application).</b> A university has Students, Lecturers, Courses and Departments; "
            "students register for courses and lecturers teach courses. Draw a UML class diagram showing "
            "classes, attributes, relationships and multiplicities."),
          P("<b>Question 4 (Extensibility).</b> Explain stereotype, tagged value, constraint and UML profile, "
            "with a practical example of each."),
          P("<b>Question 5 (Architecture).</b> Explain the four levels M3, M2, M1 and M0 using a university "
            "registration system as your example.")]

    # 19. references --------------------------------------------------------------------------------------------
    s.append(H1("19.  References and Further Reading"))
    s.append(H2("Primary authoritative reference"))
    s += BUL([
        "Object Management Group. (2017). <i>Unified Modeling Language (UML), Version 2.5.1.</i> OMG. (Adopted December 2017 — the formal version listed by OMG.)",
        "Object Management Group. <i>UML 2.5.1 — Formal Specification</i> (abstract syntax, semantics, notation, examples) and <i>UML 2.5.1 Abstract Syntax Metamodel</i> (with the UML standard profile and diagram interchange metamodel).",
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
