"""
Week 5 PDF content — OBJECT-ORIENTED ANALYSIS: OBJECT MODELLING I.
"""
from pdfengine import (H1, H2, P, BUL, FIG, CALLOUT, DTABLE, build, DOC_W,
                      C_MAROON, C_SOFT)

CFG = {
    "week": 5,
    "title": "Object-Oriented Analysis — Object Modelling I",
    "filename": "Week5_Module_BICT3202_OOAD.pdf",
}


def story():
    s = []

    # 1. introduction --------------------------------------------------------
    s.append(H1("1.  Week 5 Introduction"))
    s += [P("Weeks 1–4 built the foundation: Week 1 examined business needs and business software "
            "needs; Week 2 introduced object-oriented technology and principles; Week 3 introduced UML; "
            "and Week 4 explained UML's building blocks, rules, mechanisms and architecture. This week "
            "marks an important transition — <b>we begin the actual Object-Oriented Analysis (OOA) "
            "process</b>."),
          P("Students should now move from thinking <i>“I know what a UML class diagram is”</i> to "
            "thinking <i>“Given a real-world problem, I can identify objects/classes and represent their "
            "relationships correctly.”</i> The course outline divides Object-Oriented Analysis (Object "
            "Modelling) into two parts: <b>Week 5 — Object Modelling I</b> (object/class, notation, links "
            "and association, generalization/specialization, CASE tool) and <b>Week 6 — Object Modelling "
            "II</b> (aggregation, inheritance, polymorphism, grouping).")]

    # 2. learning outcomes -----------------------------------------------------
    s.append(H1("2.  Learning Outcomes"))
    s += [P("By the end of this week, a student should be able to:")]
    s += BUL([
        "Explain object-oriented analysis.",
        "Explain the difference between an object and a class.",
        "Identify candidate objects/classes from a problem description.",
        "Distinguish relevant objects from irrelevant nouns.",
        "Identify attributes, operations and responsibilities of objects.",
        "Draw a UML class and an object diagram using correct notation.",
        "Explain links between objects and associations between classes.",
        "Identify association names, roles and multiplicity.",
        "Use multiplicity correctly in a class diagram.",
        "Explain generalization and specialization, and draw them correctly.",
        "Distinguish generalization from ordinary association.",
        "Apply object modelling to a real-world system and evaluate the result.",
    ])

    # 3. what is OOA -------------------------------------------------------------
    s.append(H1("3.  What Is Object-Oriented Analysis?"))
    s += [P("<b>Analysis</b> means studying a problem to understand: what exists; what users need; what "
            "activities occur; what information is involved; what rules apply; and how different parts "
            "relate to one another. In <b>Object-Oriented Analysis</b>, we examine the problem domain in "
            "terms of <b>objects, classes, responsibilities, relationships and behaviour</b>."),
          P("Consider a university that wants a student registration system. A traditional analysis might "
            "begin with <i>Input → Process → Output</i>. Object-oriented analysis instead asks: <b>who/what "
            "are the important objects?</b> — Student, Course, Registration, Lecturer, Programme — and "
            "then: <b>how are these objects related?</b>")]
    s += FIG("w5_ooa_whatis.png", "Figure 1 — Traditional analysis vs object-oriented analysis")

    # 4. key question ---------------------------------------------------------------
    s.append(H1("4.  The Key Question in Object Modelling"))
    s += [P("Whenever students receive a case study, teach them to ask: <b>“What important things exist "
            "in this problem domain?”</b> For a banking system — Customer, Account, Transaction, Bank, "
            "Loan, Card; for a hospital — Patient, Doctor, Nurse, Appointment, Prescription, "
            "MedicalRecord; for an online university — Student, Lecturer, Course, Assignment, Submission, "
            "Grade. These become <b>candidate classes</b>. But be careful: <b>not every noun in a problem "
            "description should automatically become a class.</b>")]

    # 5. object vs class --------------------------------------------------------------
    s.append(H1("5.  Object vs Class"))
    s += [P("A <b>class</b> is a description or specification of a group/type of objects that share common "
            "characteristics and behaviour — for example, <b>Student</b> describes what students generally "
            "have and can do. An <b>object</b> is an individual instance of a class — for example, "
            "<font name='Mono'>Francis : Student</font>. Here <i>Student</i> is the class and "
            "<i>Francis</i> is the object."),
          P("Think about cars: <b>Car</b> is a general concept/class, while individual cars — Toyota "
            "Corolla ABC123, Honda Civic DEF456, Mazda Demio GHI789 — are objects. The class describes "
            "common characteristics; each object has its own values. Two objects, "
            "<font name='Mono'>student001 : Student</font> (John Banda, BSc ICT, year 3) and "
            "<font name='Mono'>student002 : Student</font> (Mary Phiri, BSc ICT, year 2), both belong to "
            "the same class.")]
    s += FIG("w5_class_vs_object.png", "Figure 2 — Class vs object: the car and student analogies")

    # 6. UML class notation --------------------------------------------------------------
    s.append(H1("6.  UML Class Notation"))
    s += [P("The standard UML class notation is a rectangle divided into compartments. The three "
            "compartments are commonly used for: (1) <b>class name</b>, (2) <b>attributes</b>, and "
            "(3) <b>operations</b>. A good class name represents a meaningful concept in the problem "
            "domain — Student, Course, Account, Payment, Employee, Product, Order. Poor names include "
            "Thing, Data, Information, Stuff, Object1, ClassA."),
          P("An <b>attribute</b> describes a property or characteristic of an object: for Student — "
            "studentID, name, programme, yearOfStudy; for Course — courseCode, courseName, creditHours; "
            "for Account — accountNumber, accountType, balance. A common attribute notation is "
            "<font name='Mono'>visibility name : type</font> — e.g. <font name='Mono'>- studentID : "
            "String</font>, where − is the visibility, <i>studentID</i> is the name and <i>String</i> is "
            "the data type."),
          P("An <b>operation</b> represents behaviour/responsibility associated with a class: Student — "
            "registerCourse(), dropCourse(), viewResults(); BankAccount — deposit(), withdraw(), "
            "checkBalance(); Course — addStudent(), removeStudent(), assignLecturer(). Operation names "
            "should come from the requirements and responsibilities discovered during analysis.")]
    s += FIG("w5_uml_class_notation.png", "Figure 3 — UML class notation: the three compartments")
    s += FIG("w5_attr_vs_op.png", "Figure 4 — Attributes vs operations")

    # 7. object notation --------------------------------------------------------------------
    s.append(H1("7.  Object Notation"))
    s += [P("An object is commonly shown as a rectangle with its <b>name underlined</b>, followed by its "
            "attribute values. The key distinction: a class describes possible structure, while an object "
            "shows a specific instance and its values.")]
    s += FIG("w5_object_notation.png", "Figure 5 — Object notation: underlined name and attribute values")

    # 8. process ---------------------------------------------------------------------------------
    s.append(H1("8.  The Object Modelling Process"))
    s += [P("A simple, beginner-friendly process is: Problem Description → Identify Candidate Objects → "
            "Identify Candidate Classes → Identify Attributes → Identify Responsibilities/Operations → "
            "Identify Relationships → Validate the Model → Draw the UML Class Diagram. <b>Do not simply "
            "underline every noun and call it a class</b> — that is too simplistic.")]
    s += FIG("w5_process.png", "Figure 6 — The object modelling process (iterative)")

    # 9. identifying candidate classes -----------------------------------------------------------
    s.append(H1("9.  Identifying Candidate Classes"))
    s += [P("Consider the sentence: <i>“A student registers for a course. The course is taught by a "
            "lecturer.”</i> The potential nouns — student, course, lecturer — are strong candidate "
            "classes. Now consider: <i>“A student registers for a course on Monday.”</i> The noun "
            "<b>Monday</b> should not automatically become a class — it is more likely an attribute/value "
            "associated with a date or registration."),
          P("The <b>noun technique</b> — look for important nouns in the problem description — is a useful "
            "starting point, but students must still ask: Is this concept relevant? Does the system need "
            "to store it? Does it have meaningful properties? Does it participate in relationships? Does "
            "it have behaviour/responsibility?")]
    s += FIG("w5_noun_technique.png", "Figure 7 — The noun technique, with its warning")

    # 10. links and associations ----------------------------------------------------------------------
    s.append(H1("10.  Links and Associations"))
    s += [P("A <b>link</b> represents a connection between particular objects — if Francis : Student is "
            "registered for BICT3202 : Course, we draw "
            "<font name='Mono'>Francis : Student ───── BICT3202 : Course</font>. An <b>association</b> "
            "describes a relationship between classes — <font name='Mono'>Student ───── Course</font> "
            "means instances of Student can be related to instances of Course."),
          P("The distinction is extremely important: <b>association connects classes; link connects "
            "objects.</b>")]
    s += FIG("w5_link_vs_association.png", "Figure 8 — Link vs association: class level vs object level")

    # 11. naming and roles --------------------------------------------------------------------------------
    s.append(H1("11.  Naming an Association & Roles"))
    s += [P("An association can be given a meaningful name: instead of a bare line, write "
            "<font name='Mono'>Student ─── registers for ─── Course</font>, or "
            "<font name='Mono'>Lecturer ─── teaches ─── Course</font>, or "
            "<font name='Mono'>Customer ─── places ─── Order</font>. The name helps people understand the "
            "meaning of the relationship."),
          P("An association can also indicate the <b>role</b> each class plays — at the Course side the "
            "role could be <i>registeredCourse</i>; at the Student side, <i>student</i>. Roles are "
            "particularly useful when a relationship needs clarification.")]
    s += FIG("w5_association_naming.png", "Figure 9 — Association names and roles")

    # 12. multiplicity ---------------------------------------------------------------------------------------
    s.append(H1("12.  Multiplicity"))
    s += [P("<b>Multiplicity</b> tells us how many instances can participate in a relationship. "
            "<font name='Mono'>Student 1 ───── 0..* Course</font> means one Student can be associated with "
            "zero or many Courses. Why zero? Because a newly admitted student may not yet have registered "
            "for any course."),
          P("<font name='Mono'>Department 1 ───── 1..* Lecturer</font> means a Department must have at "
            "least one Lecturer and can have many. The difference is that <b>0..* allows zero</b>, while "
            "<b>1..* requires at least one</b>. Students should not memorise these without understanding "
            "them.")]
    s += FIG("w5_multiplicity.png", "Figure 10 — Reading multiplicity at the far end")
    s.append(DTABLE(
        ["Notation", "Meaning"],
        [["1", "Exactly one"],
         ["0..1", "Zero or one"],
         ["*", "Many"],
         ["0..*", "Zero or many"],
         ["1..*", "One or many"],
         ["2..5", "Between two and five"]],
        widths=[0.3 * DOC_W, 0.7 * DOC_W]))
    s += FIG("w5_chart_multiplicity.png", "Figure 11 — Common multiplicities")

    # 13. cardinality ---------------------------------------------------------------------------------------------
    s.append(H1("13.  One-to-One, One-to-Many, Many-to-Many"))
    s += [P("<b>One-to-one:</b> “Each student has one ID card, and each ID card belongs to one student” — "
            "<font name='Mono'>Student 1 ───── 1 IDCard</font>. <b>One-to-many:</b> “One lecturer teaches "
            "many courses” — <font name='Mono'>Lecturer 1 ───── 0..* Course</font>. <b>Many-to-many:</b> "
            "“A student can register for many courses, and a course can have many students” — "
            "<font name='Mono'>Student 0..* ───── 0..* Course</font>."),
          P("A many-to-many relationship often leads to an important modelling question: <b>does the "
            "relationship itself have information?</b> If registration has registrationDate, semester, "
            "status and grade, we may introduce a <b>Registration</b> class — this is revisited in greater "
            "depth later in the module.")]
    s += FIG("w5_cardinality.png", "Figure 12 — The three relationship shapes")

    # 14. generalization ----------------------------------------------------------------------------------------------
    s.append(H1("14.  Generalization"))
    s += [P("<b>Generalization</b> represents a relationship between a more general class and a more "
            "specific class. For example, <b>User</b> is the general class, while <b>Student</b> and "
            "<b>Lecturer</b> are specialised classes. We read <font name='Mono'>Student ─────▷ User</font> "
            "as “A Student is a User” — often called an <b>“is-a”</b> relationship."),
          P("Placing common features (userID, name, email, login(), logout()) in <b>User</b> and letting "
            "Student and Lecturer specialise avoids duplicating those features in every subclass — this "
            "supports reuse and reduces duplication.")]
    s += FIG("w5_generalization.png", "Figure 13 — Generalization: a general class and its specializations")
    s += FIG("w5_complete_example.png", "Figure 14 — A complete class example with shared features")

    # 15. generalization vs association -----------------------------------------------------------------------------------
    s.append(H1("15.  Generalization vs Association"))
    s += [P("This distinction is extremely important. Generalization "
            "(<font name='Mono'>Student ─────▷ User</font>) means <b>Student is a User</b>. Association "
            "(<font name='Mono'>Student ───── Course</font>) means <b>Student is related to Course</b>. "
            "Consider vehicles: a Car is a Vehicle (generalization), but <b>Car ───── Driver</b> is not "
            "generalization — a car is not a driver; it is a relationship between two different concepts.")]
    s += FIG("w5_gen_vs_assoc.png", "Figure 15 — Generalization vs association")

    # 16. specialization and vocabulary -----------------------------------------------------------------------------------
    s.append(H1("16.  Specialization, Vocabulary and the Tests"))
    s += [P("<b>Specialization</b> is the process of creating more specific concepts from a general "
            "concept — from Employee we may specialise Lecturer, Administrator and Technician. "
            "Generalization and specialization are <b>opposite perspectives</b> on the same structure: "
            "from the bottom upward, “Car is generalized into Vehicle”; from the top downward, “Vehicle "
            "is specialized into Car.”"),
          P("Vocabulary: the general class is also called the <b>parent</b>, <b>superclass</b> or "
            "<b>generalized class</b>; the specialised class is also called the <b>child</b>, "
            "<b>subclass</b> or <b>derived class</b>."),
          P("Two useful tests: the <b>“is-a” test</b> — “Is a Student a User?” Yes → generalization may be "
            "appropriate; “Is a Student a Course?” No → use an association. The <b>“has-a” test</b> — "
            "“Car has an Engine” points toward aggregation/composition (Week 6), which is different from "
            "“Car is a Vehicle” (generalization).")]
    s += FIG("w5_isa_hasa.png", "Figure 16 — The is-a and has-a tests")

    # 17. CASE tools ------------------------------------------------------------------------------------------------------
    s.append(H1("17.  CASE Tools"))
    s += [P("The course outline requires a CASE tool demonstration (Select Enterprise). <b>CASE</b> means "
            "<b>Computer-Aided Software Engineering</b>. A CASE tool can support modelling, diagram "
            "creation, documentation, requirements management, design and code-related workflows. Common "
            "UML/modelling tools include Enterprise Architect, Visual Paradigm, StarUML, PlantUML, "
            "diagrams.net/draw.io and Modelio."),
          P("The important point is not the brand of the tool. <b>A CASE tool assists modelling; it does "
            "not replace analysis.</b> The tool can create a Student box, but it does not know whether "
            "Student should actually be a class — that decision comes from requirements, domain knowledge, "
            "analysis and business rules. <b>The analyst makes modelling decisions; the CASE tool helps "
            "represent and manage those decisions.</b>")]
    s += FIG("w5_case_tools.png", "Figure 17 — CASE tools assist modelling, never replace analysis")

    # 18. practical lab ------------------------------------------------------------------------------------------------------
    s.append(H1("18.  Practical Lab — Create Your First Class Diagram"))
    s += [P("Using the selected UML CASE tool, create four classes — Student, Course, Lecturer, "
            "Registration — with the following attributes and operations, then add associations and "
            "multiplicities.")]
    s.append(DTABLE(
        ["Class", "Attributes", "Operations"],
        [["Student", "studentID : String · name : String · programme : String · yearOfStudy : Integer",
          "registerCourse() · dropCourse() · viewResults()"],
         ["Course", "courseCode : String · courseName : String · creditHours : Integer",
          "addStudent() · removeStudent()"],
         ["Lecturer", "lecturerID : String · name : String · department : String",
          "assignGrade() · viewClassList()"],
         ["Registration", "registrationID : String · registrationDate : Date · status : String",
          "confirm() · cancel()"]],
        widths=[0.2 * DOC_W, 0.44 * DOC_W, 0.36 * DOC_W]))
    s += BUL([
        "Add associations: Student ─── makes ─── Registration · Registration ─── is for ─── Course · Lecturer ─── teaches ─── Course.",
        "Add multiplicities (document your assumptions): Student 1 ── 0..* Registration · Course 1 ── 0..* Registration · Lecturer 1 ── 0..* Course.",
        "Add generalization: User ▷ Student and User ▷ Lecturer, then discuss which attributes should move up to User.",
    ])

    # 19. validation -----------------------------------------------------------------------------------------------------------
    s.append(H1("19.  Validating a Class Diagram"))
    s += [P("After creating a diagram, do not submit it immediately — perform a model review. Ask:")]
    s += BUL([
        "Does every class have a purpose? If not, remove or reconsider it.",
        "Does every attribute belong to the correct class? (studentName probably belongs to Student.)",
        "Are operations meaningful? Don't add random methods simply to fill the box.",
        "Are relationships logically correct?",
        "Are multiplicities supported by requirements?",
        "Are generalizations genuine “is-a” relationships?",
        "Is the diagram readable?",
    ])

    # 20. common mistakes ---------------------------------------------------------------------------------------------------------
    s.append(H1("20.  Common Student Mistakes"))
    mistakes = [
        ("Mistake 1 — Confusing class and object.",
         "“John is the Student class” is wrong thinking. Student = class; John : Student = object."),
        ("Mistake 2 — Using generalization everywhere.",
         "Student ─────▷ Course is wrong — a Student is not a Course."),
        ("Mistake 3 — Forgetting multiplicities.",
         "Drawing Student ───── Course and stopping; requirements often require us to know “how many?”"),
        ("Mistake 4 — Making every noun a class.",
         "Not every noun is a class."),
        ("Mistake 5 — Adding operations randomly.",
         "eat(), sleep(), walk() are not system-relevant responsibilities — OOAD is about what the system needs, not everything a human can do."),
    ]
    for head, fix in mistakes:
        s.append(CALLOUT(head, [fix], bar=C_SOFT, tcol=C_MAROON))
    s += [P("<b>Analysis vs implementation:</b> at this stage, do not become obsessed with programming "
            "syntax. <font name='Mono'>public void registerCourse()</font> is implementation-oriented; at "
            "the analysis level we simply model <font name='Mono'>registerCourse()</font>. Understand the "
            "system first; implementation details grow in importance during design.")]

    # 21. case study / exercise ----------------------------------------------------------------------------------------------------
    s.append(H1("21.  Object Modelling Exercise — Hospital"))
    s += [P("Scenario: <i>“A hospital has doctors, nurses and patients. A patient can have multiple "
            "appointments. Each appointment is with a doctor. A doctor belongs to a department. A patient "
            "has a patient number, name and date of birth.”</i>")]
    s += BUL([
        "<b>Task 1 — Candidate classes:</b> Patient, Doctor, Nurse, Appointment, Department.",
        "<b>Task 2 — Attributes:</b> Patient — patientNumber, name, dateOfBirth.",
        "<b>Task 3 — Relationships:</b> Patient ─── has ─── Appointment · Appointment ─── with ─── Doctor · Doctor ─── belongs to ─── Department.",
        "<b>Task 4 — Multiplicity:</b> Patient 1 ───── 0..* Appointment.",
    ])
    s.append(CALLOUT("WHY OBJECT IDENTIFICATION IS DIFFICULT",
        ["A real system does not come with labels saying THIS IS A CLASS, THIS IS AN ATTRIBUTE, THIS IS "
         "AN OPERATION. The analyst has to determine these. “The customer uses a shopping cart” — should "
         "ShoppingCart be a class? Usually yes, if it has meaningful state (items, total) and behaviour "
         "(addItem(), removeItem(), calculateTotal()). <b>Object modelling requires reasoning, not just "
         "drawing.</b> It is also iterative: the first model is rarely the final model."]))

    # 22. summary and big picture ---------------------------------------------------------------------------------------------------
    s.append(H1("22.  Week 5 Summary and Key Terms"))
    s.append(DTABLE(
        ["Term", "Simple meaning"],
        [["Object", "A particular instance"],
         ["Class", "Description of a type of object"],
         ["Attribute", "Property/information held by an object"],
         ["Operation", "Behaviour/responsibility"],
         ["Link", "Connection between object instances"],
         ["Association", "Relationship between classes"],
         ["Multiplicity", "How many instances can participate"],
         ["Generalization", "General-to-specific relationship"],
         ["Specialization", "Creating a more specific class"],
         ["Superclass / Subclass", "General/parent class · specialized/child class"],
         ["CASE", "Computer-Aided Software Engineering"],
         ["Object model", "Representation of objects/classes and their relationships"]],
        widths=[0.34 * DOC_W, 0.66 * DOC_W]))
    s.append(CALLOUT("THE BIG PICTURE",
        ["The progression is: real-world problem → read requirements → identify important concepts → "
         "candidate objects/classes → attributes → responsibilities/operations → links/associations → "
         "multiplicities → genuine generalization → UML class diagram → validate against requirements. "
         "<b>Object-Oriented Analysis is not primarily about drawing boxes — it is about understanding a "
         "problem domain and deciding what objects/classes, properties, behaviours and relationships are "
         "necessary to represent it.</b> Week 6 extends this model with aggregation, inheritance, "
         "polymorphism and grouping."]))

    # 23. examination questions ------------------------------------------------------------------------------------------------------
    s.append(H1("23.  Examination-Style Question"))
    s += [P("<b>Scenario:</b> A university has students and lecturers. Each student has a student ID, name, "
            "programme and year of study. Each lecturer has a staff ID, name and department. Students "
            "register for courses. Each course has a course code, title and credit hours. Lecturers teach "
            "courses. A student may register for many courses, while each course may have many students."),
          P("<b>Required:</b> (a) identify the candidate classes [5]; (b) identify appropriate attributes "
            "[10]; (c) identify operations that could reasonably belong to the classes [5]; (d) draw a UML "
            "class diagram showing the associations [10]; (e) add appropriate multiplicities [5]; "
            "(f) identify whether generalization is appropriate and justify your answer [5]. "
            "<b>Total: 40 marks.</b>")]

    # 24. references -------------------------------------------------------------------------------------------------------------------
    s.append(H1("24.  References and Further Reading"))
    s.append(H2("Primary authoritative reference"))
    s += BUL([
        "Object Management Group. (2017). <i>Unified Modeling Language (UML), Version 2.5.1.</i> OMG — the formal UML specification and the most authoritative source for notation, semantics, classes, objects, relationships and generalization.",
        "Object Management Group. <i>UML</i> — the UML specification together with machine-readable artefacts, including the UML abstract syntax metamodel.",
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
