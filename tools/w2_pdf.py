"""
Week 2 PDF content — PRINCIPLES OF OBJECT MODELLING.
"""
from pdfengine import (H1, H2, P, BUL, FIG, CALLOUT, DTABLE, build, DOC_W)

CFG = {
    "week": 2,
    "title": "Principles of Object Modelling",
    "filename": "Week2_Module_BICT3202_OOAD.pdf",
}


def story():
    s = []

    # 1. overview -----------------------------------------------------------
    s.append(H1("1.  Week 2 Overview"))
    s += [P("Week 1 established the foundation: "
            "<b>business problem → business need → requirements → understanding the problem domain → "
            "candidate objects</b>. This week moves one step further."),
          P("The official course outline identifies six Week 2 topics: <b>Principles of Object Modelling</b>, "
            "<b>Definition of an Object Model</b>, <b>Identification of Objects in a System</b>, "
            "<b>Standards for Objects</b>, <b>Managing Complexity</b> and <b>Modelling</b>."),
          P("The purpose is to teach students how to think about a system as a collection of meaningful "
            "objects and relationships, before the complete UML language is introduced in Weeks 3 and 4."),
          P("A model is deliberately simpler than the real system. The Object Management Group (OMG) "
            "explains that modelling helps people work at a higher level of abstraction by hiding "
            "unnecessary detail and focusing attention on particular aspects of a system — an idea that is "
            "absolutely central to OOAD.")]
    s += FIG("w2_real_to_software.png",
             "Figure 1 — The object model is the bridge between the real-world problem and the software solution")

    # 2. learning outcomes ---------------------------------------------------
    s.append(H1("2.  Learning Outcomes"))
    s += [P("By the end of this week, students should be able to:")]
    s += BUL([
        "Explain the meaning of object modelling and define an object model.",
        "Explain why object models are useful in systems analysis.",
        "Explain the relationship between an object, a class and an object model.",
        "Identify potential objects in a given problem domain.",
        "Distinguish useful objects from irrelevant nouns.",
        "Identify attributes, behaviours and relationships associated with objects.",
        "Explain object identity, abstraction and encapsulation in relation to modelling.",
        "Explain how object models help manage system complexity.",
        "Explain the importance of consistency and standards in modelling.",
        "Construct a simple conceptual object model from a textual problem description.",
        "Evaluate whether a proposed object model adequately represents the business problem.",
    ])

    # 3. what is object modelling -------------------------------------------
    s.append(H1("3.  What Is Object Modelling?"))
    s += [P("Imagine explaining a university to somebody who has never seen it. You could try to describe "
            "everything — every student, lecturer, classroom, chair, computer, document, tree, road, employee, "
            "department and activity. That would be overwhelming."),
          P("Instead, you create a <b>simplified representation</b> showing only the things relevant to your "
            "purpose. For a student registration system you might focus on <b>Student, Course, Programme, "
            "Lecturer, Registration, Department and Payment</b>."),
          P("That simplified representation is a <b>model</b>. When we organise the model around objects and "
            "their relationships, we are performing <b>object modelling</b>.")]
    s.append(CALLOUT("DEFINITION",
        ["An <b>object model</b> is a representation of a system or problem domain in terms of objects, their "
         "characteristics, behaviour and relationships."]))
    s += FIG("w2_object_model.png",
             "Figure 2 — A first object model: Student — registers for — Course, with key attributes")

    # 4. why do we need object models ----------------------------------------
    s.append(H1("4.  Why Do We Need Object Models?"))
    s += [P("“Build us an online student registration system” is too broad a statement. The developer must "
            "understand <b>who</b> registers, <b>what</b> is being registered, <b>who</b> approves, "
            "<b>which</b> courses are available, <b>what</b> information registration contains, whether "
            "prerequisites apply, whether payment affects registration, and who may change a registration."),
          P("Object modelling transforms a vague description into a structured, communicable representation.")]
    s += [P("<b>Object modelling is a form of simplification.</b> The real world is enormously complicated; a "
            "software model cannot — and should not — represent every detail. We select the details that "
            "matter. This is <b>abstraction</b>.")]

    # 5. principles -----------------------------------------------------------
    s.append(H1("5.  The Principles of Object Modelling"))
    s += FIG("w2_principles.png",
             "Figure 3 — Nine guiding principles of object modelling")

    s.append(H2("5.1  Abstraction"))
    s += [P("Abstraction means focusing on the essential characteristics of something while ignoring details "
            "not relevant to the current purpose. A driver cares about steering, speed, fuel, brakes and gear — "
            "not the internal combustion process or every electrical connection."),
          P("A Student has hundreds of real-world characteristics (height, weight, hair colour, favourite food, "
            "shoe size, hobbies…). For a registration system the important attributes may be just "
            "<b>studentID, name, programme, year, status</b> — shoe size is irrelevant to course registration.")]
    s += FIG("w2_abstraction.png",
             "Figure 4 — Abstraction depends on purpose: the same Student is modelled differently for each system")

    s.append(H2("5.2  Encapsulation"))
    s += [P("Encapsulation keeps an object's relevant data and operations together while controlling access to "
            "its internal state. A BankAccount owns its balance and provides deposit(), withdraw() and "
            "checkBalance() — instead of letting every part of the system write "
            "<font name='Mono'>balance = -500000</font> without any checks.")]
    s.append(H2("5.3  Identity"))
    s += [P("Objects have <b>identity</b>. Two students may share the name “Francis” but remain different "
            "objects because their identifiers differ. Identity may be a student ID, account number, employee "
            "ID, product ID, UUID or database primary key.")]
    s += FIG("w2_identity.png", "Figure 5 — Identity separates objects even when attribute values are identical")

    s.append(H2("5.4  State"))
    s += [P("The <b>state</b> of an object is the collection of values describing its current condition "
            "(ID = ST001, Name = Francis, Year = 3, Status = Active). State can change over time — from "
            "Applicant, to Active Student, to Graduated. State represents what is true about an object at a "
            "particular moment.")]
    s.append(H2("5.5  Behaviour"))
    s += [P("An object's <b>behaviour</b> describes what it can do or how it responds to requests — a Student "
            "has registerCourse(), dropCourse(), viewResults(), payFees(); a BankAccount has deposit(), "
            "withdraw(), transfer(). So an object combines <b>identity + state + behaviour</b>.")]
    s.append(H2("5.6  Relationships"))
    s += [P("Objects rarely exist independently. Relationships connect them: "
            "<b>Student — registers for — Course</b>, <b>Lecturer — teaches — Course</b>, "
            "<b>Customer — owns — Account</b>, <b>Customer — places — Order</b>.")]
    s.append(H2("5.7  Modularity"))
    s += [P("Modularity divides a large system into manageable parts. A university information system can be "
            "split into Student, Finance, Exams and Library modules, each containing related objects "
            "(Finance holds Invoice, Payment, Account, Receipt).")]
    s.append(H2("5.8  Hierarchy"))
    s += [P("Hierarchy organises concepts into levels from general to specialised: <b>Person → Student / "
            "Employee → Lecturer / Administrator</b>. This connects directly to generalisation, "
            "specialisation and inheritance in later weeks.")]
    s.append(H2("5.9  Reuse"))
    s += [P("Good object models support reuse — a general Person (name, phone, email) can be shared by many "
            "parts of the system. But remember: <b>reuse does not mean “always use inheritance.”</b> "
            "Composition, delegation, interfaces and services can also support reuse.")]

    # 6. object identification -------------------------------------------------
    s.append(H1("6.  Object Identification"))
    s += [P("<b>Object identification</b> means determining which entities or concepts in the problem domain "
            "should be represented as objects/classes in the system model. It sounds easy — it isn't."),
          P("From “A student registers for courses. The lecturer teaches the courses, and the finance "
            "department records the student's payments,” we might identify Student, Course, Lecturer, Finance "
            "Department, Payment and Registration — but we must not automatically accept every noun.")]
    s.append(H2("6.1  The Noun Technique"))
    s += [P("A traditional starting point is to examine the problem statement and underline important nouns. "
            "These become <b>candidate</b> concepts — but <b>candidate ≠ final object</b>.")]
    s.append(CALLOUT("KEY POINT",
        ["“The student uses a mobile phone to register for a course.” Should Phone be a class? Probably not — "
         "it may simply be an external device. Object identification requires <b>judgement, not just grammar</b>."]))
    s.append(H2("6.2  Classifying Candidate Objects"))
    s += FIG("w2_classification.png",
             "Figure 6 — Six common families of candidate concepts")
    s += [P("<b>Events can be objects.</b> Payment is an event/transactional concept with paymentID, amount, "
            "date, method, status and behaviour such as process(), cancel(), refund() — a perfectly valid "
            "object even though it is not physical.")]
    s.append(H2("6.3  How to Decide"))
    s += FIG("w2_decision_questions.png",
             "Figure 7 — Seven questions that test whether a concept deserves to be an object")
    s.append(H2("6.4  Object vs Attribute"))
    s += [P("Deciding whether something is an object or merely an attribute is a common source of confusion. "
            "If the system only needs <font name='Mono'>phoneNumber = +265…</font>, then phoneNumber is an "
            "attribute. If it must manage multiple numbers, verification, ownership, type and status, a "
            "separate Phone concept may become useful. The decision depends on requirements and purpose.")]
    s += FIG("w2_object_vs_attribute.png",
             "Figure 8 — The same concept can be an attribute in one system and an object in another")

    # 7. attributes, behaviour, responsibility ----------------------------------
    s.append(H1("7.  Attributes, Behaviour & Responsibility"))
    s += [P("Once candidates are identified, ask: <b>“What information must the system know about this "
            "object?”</b> (its attributes) and <b>“What does this object do?”</b> (its behaviour)."),
          P("For Student: studentID, name, dateOfBirth, programme, year, status — with register(), "
            "dropCourse(), viewResults(). For Payment: paymentID, amount, date, method, status — with "
            "process(), refund(), verify(). Behaviour should be derived from the requirements, not invented.")]
    s.append(CALLOUT("OBJECT RESPONSIBILITY",
        ["Should a Customer calculate the interest on an Account? Probably not — Account is a better owner of "
         "that responsibility because it holds balance, account type and interest rules. "
         "<b>Give an object responsibilities that logically belong to it.</b>"]))
    s.append(H2("7.1  Cohesion and Coupling"))
    s += [P("<b>Cohesion</b> measures how closely related an object's responsibilities are. A Student with "
            "registerCourse(), viewResults(), payFees(), <b>repairComputer(), cookFood() and "
            "manageUniversityNetwork()</b> has poor cohesion."),
          P("<b>Coupling</b> is the degree of dependency between components. Well-designed systems aim for "
            "<b>high cohesion + manageable/low coupling</b>.")]
    s += FIG("w2_cohesion.png", "Figure 9 — Poor cohesion mixes unrelated duties; good cohesion stays focused")

    # 8. managing complexity -----------------------------------------------------
    s.append(H1("8.  Managing Complexity"))
    s += [P("A system with 10 classes is easy to understand; a system with 500 classes and many relationships "
            "is not. Object-oriented modelling uses several techniques to control this complexity.")]
    s += FIG("w2_complexity.png",
             "Figure 10 — Six techniques for managing complexity")
    s += FIG("w2_chart_interactions.png",
             "Figure 11 — Illustrative growth of possible interactions as classes are added")
    s += [P("<b>Separation of concerns</b> deserves emphasis: avoid the “God object” — one component trying to "
            "do everything (registerStudent(), calculateSalary(), printInvoice(), repairComputer(), sendSMS(), "
            "calculateExamMarks(), manageLibrary()). Responsibilities should be distributed appropriately.")]
    s += FIG("w2_poor_vs_good.png",
             "Figure 12 — A poor model throws everything into one box; a good model separates concerns")

    # 9. modelling viewpoints -------------------------------------------------------
    s.append(H1("9.  Modelling Viewpoints"))
    s += [P("A single model is often not enough to understand a complex system. We may want a <b>structural</b> "
            "view (what exists), a <b>behavioural</b> view (what happens), an <b>interaction</b> view (how "
            "objects communicate) and a <b>deployment</b> view (where components run).")]
    s += FIG("w2_viewpoints.png",
             "Figure 13 — UML supports several perspectives rather than forcing one diagram")

    # 10. standards ------------------------------------------------------------------
    s.append(H1("10.  Standards for Objects & Modelling"))
    s += [P("Software modelling should not be based on everyone's personal drawing style. Standard notation "
            "improves communication. For OOAD the major standard is the <b>Unified Modeling Language (UML)</b>, "
            "maintained by the Object Management Group; the currently published formal specification is "
            "<b>UML 2.5.1</b> (adopted December 2017).")]
    s.append(H2("10.1  Why Standards Matter"))
    s += [P("If three analysts draw a relationship as <font name='Mono'>Student ---- Course</font>, "
            "<font name='Mono'>Student &lt;--&gt; Course</font> and <font name='Mono'>Student ==== Course</font>, "
            "nobody knows what the symbols mean. A standardised language provides agreed meanings.")]
    s.append(CALLOUT("IMPORTANT",
        ["<b>Standards do not replace thinking.</b> A UML diagram can be perfectly drawn and still represent bad "
         "analysis — “Student owns Toilet” is syntactically correct but meaningless for a registration system. "
         "Correct notation does not guarantee correct analysis: understand the business, the requirements, "
         "select appropriate concepts, create meaningful relationships, then use correct notation."]))

    # 11. worked examples ---------------------------------------------------------------
    s.append(H1("11.  Worked Examples"))
    s.append(H2("11.1  University Registration"))
    s += [P("Building our first conceptual object model from requirements proceeds in steps: "
            "<b>(1)</b> identify candidate objects (Student, Course, Lecturer, Registration, Programme, "
            "Payment); <b>(2)</b> identify attributes (Student: studentID, name, programme, year); "
            "<b>(3)</b> identify relationships (Student—Registration, Course—Registration, Lecturer—Course, "
            "Programme—Student); <b>(4)</b> identify behaviour (Student.registerCourse(); "
            "Registration.submit()/approve()/cancel(); Payment.process()/refund()).")]
    s.append(H2("11.2  Mobile Money System"))
    s += [P("For a mobile money system the candidate objects include <b>Customer, Wallet, Transaction, Agent, "
            "Merchant, Bill</b> — each with identity, state and behaviour.")]
    s += FIG("w2_mobile_money.png", "Figure 14 — Mobile money: candidates, attributes, behaviour and a first model")
    s.append(CALLOUT("CANDIDATE vs FINAL",
        ["Initial analysis may list Customer, Phone, Money, Wallet, Transaction, Agent, Network and SMS — but we "
         "do not automatically create eight classes. Phone may be an attribute; Money is usually a value; Network "
         "is infrastructure; SMS may be an external service. <b>Object identification is analytical reasoning, "
         "not noun extraction.</b>"]))
    s.append(H2("11.3  Mini Case Study — Online Library"))
    s += [P("A university wants an online library system: students search for, borrow and return books; "
            "librarians manage books and monitor overdue loans.")]
    s += FIG("w2_library_model.png", "Figure 15 — Library conceptual object model")
    s += [P("<b>Is “Library” an object?</b> Possibly — but it depends on scope. If the system manages multiple "
            "libraries, branches, locations, hours and staff, then Library is meaningful; for a single library's "
            "borrowing process it may not be needed. <b>Scope and purpose determine the model.</b>")]

    # 12. quality & checklist -----------------------------------------------------------
    s.append(H1("12.  Object-Model Quality & Checklists"))
    s += [P("A good object model should be <b>relevant</b>, <b>understandable</b>, <b>consistent</b>, "
            "<b>sufficient</b>, <b>not unnecessarily detailed</b>, <b>traceable</b> to requirements, and "
            "<b>maintainable</b> as requirements change.")]
    s += FIG("w2_checklist.png",
             "Figure 16 — The ten-step object-identification checklist for examination scenarios")
    s.append(H2("12.1  Traceability from Requirements to Objects"))
    s += [P("A good analyst can answer: <b>“Where did this object come from?”</b> The requirement “Students must "
            "be able to register courses” leads to Student, Course and Registration; “the system must prevent "
            "registration when prerequisites are not satisfied” leads to a Course–prerequisite relationship. "
            "Requirements provide evidence for why model elements exist.")]

    # 13. activities ---------------------------------------------------------------------
    s.append(H1("13.  Practical & Tutorial Activities"))
    s.append(H2("13.1  Practical — Hospital Appointment System"))
    s += [P("<b>Scenario:</b> a hospital wants an electronic appointment system. Patients request appointments "
            "with doctors; doctors have specialties; receptionists manage appointments; the system records dates "
            "and statuses."),
          P("<b>Task 1</b> — identify candidate objects (Patient, Doctor, Appointment, Receptionist, "
            "Specialty) and justify each.<br/>"
            "<b>Task 2</b> — identify attributes (Patient: patientID, name, phone; Doctor: doctorID, name, "
            "specialty; Appointment: appointmentID, date, time, status).<br/>"
            "<b>Task 3</b> — identify behaviours (Patient.requestAppointment()/cancelAppointment(); "
            "Doctor.viewAppointments(); Receptionist.scheduleAppointment()/rescheduleAppointment()).<br/>"
            "<b>Task 4</b> — identify relationships (Patient—requests—Appointment, Doctor—attends—"
            "Appointment, Doctor—has—Specialty, Receptionist—manages—Appointment).", "bodyL")]
    s.append(H2("13.2  Tutorial — “Is It an Object?”"))
    s += [P("For each candidate — Student, Name, Course, Mobile Phone, Payment, Money, University, Registration, "
            "Keyboard, Invoice, Lecturer, Internet — classify it as <b>likely object/class</b>, <b>likely "
            "attribute</b>, <b>external entity/infrastructure</b>, <b>depends on scope</b>, or <b>probably "
            "irrelevant</b>, and justify every decision.")]
    s.append(CALLOUT("TUTORIAL CHALLENGE",
        ["“A customer uses a mobile phone to purchase a product from an online shop, adds it to a shopping cart, "
         "pays using mobile money, and the system generates an invoice.” Identify objects, attributes, "
         "behaviours, relationships and external systems — and decide whether Mobile Phone, Mobile Money, "
         "Invoice and Shopping Cart should be objects. <b>The reasoning is the important part.</b>"]))

    # 14. independent learning --------------------------------------------------------------
    s.append(H1("14.  Independent Learning (10 Hours)"))
    s += BUL([
        "<b>Object identification</b> — choose a system (supermarket, bank, hospital, mobile money, university, hotel, library); write a one-page description and identify 15 candidate objects, 10 attributes, 10 behaviours and 10 relationships.",
        "<b>Object filtering</b> — from your 15 candidates, classify each as Keep/Remove with a reason (Student = keep, core entity; Keyboard = remove, implementation detail).",
        "<b>Complexity analysis</b> — for a large system, explain how abstraction, decomposition, modularity and hierarchy could reduce its complexity.",
    ])

    # 15. summary -----------------------------------------------------------------------------
    s.append(H1("15.  Week 2 Summary"))
    s.append(DTABLE(
        ["Term", "Meaning"],
        [["Object modelling", "Representing a system/problem domain using objects and their characteristics, behaviour and relationships."],
         ["Object", "An identifiable entity with state and behaviour."],
         ["Class", "A specification describing a type of object."],
         ["Abstraction", "Focus on relevant information while hiding unnecessary detail."],
         ["Encapsulation", "Keep data and related operations together while controlling access."],
         ["Identity", "Allows one object to be distinguished from another."],
         ["State", "The object's current condition."],
         ["Behaviour", "What the object can do or how it responds."],
         ["Relationship", "How objects are connected or interact."],
         ["Modularity / Hierarchy", "Divide the system into parts / organise concepts general→specialised."],
         ["Object identification", "Deciding which domain concepts belong in the model."],
         ["UML", "Standardised modelling language; current OMG specification is UML 2.5.1."]],
        widths=[0.30 * DOC_W, 0.70 * DOC_W]))
    s.append(CALLOUT("THE MOST IMPORTANT LESSON",
        ["Object modelling is <b>not</b> turning every noun into a class. It is the disciplined process of "
         "identifying the important concepts in a problem domain, determining their relevant information and "
         "behaviour, and representing how they relate — moving from problem domain → candidate concepts → "
         "relevant objects → attributes → behaviour → relationships → an object model. Next, we need a standard "
         "language to communicate these models — which leads directly into <b>Week 3: UML</b>."]))

    # 16. examination questions ------------------------------------------------------------------
    s.append(H1("16.  Examination-Style Questions"))
    s += [P("<b>Question 1.</b> Define object modelling and explain its importance in object-oriented analysis."),
          P("<b>Question 2.</b> Explain five principles of object modelling, illustrating each using a university "
            "management system."),
          P("<b>Question 3.</b> A university wants an online course registration system. Identify: (a) ten "
            "candidate objects, (b) five attributes for appropriate objects, (c) five behaviours, (d) five "
            "relationships, (e) three examples of information to be excluded through abstraction."),
          P("<b>Question 4.</b> “Every noun in a requirements document should become an object.” Do you agree? "
            "Explain with examples."),
          P("<b>Question 5.</b> Explain how abstraction, decomposition, modularity, hierarchy, encapsulation and "
            "separation of concerns help manage complexity.")]

    # 17. references --------------------------------------------------------------------------------
    s.append(H1("17.  References and Further Reading"))
    s.append(H2("Standards and authoritative sources"))
    s += BUL([
        "International Organization for Standardization. (2018). <i>ISO/IEC/IEEE 29148:2018 — Systems and software engineering — Life cycle processes — Requirements engineering.</i> ISO. (Current edition; reviewed and confirmed 2024.)",
        "Object Management Group. (2017). <i>OMG Unified Modeling Language (OMG UML), Version 2.5.1.</i> OMG.",
        "Object Management Group. <i>Unified Modeling Language (UML).</i> OMG — UML as a standard language for visualising, specifying and documenting software, systems and business processes.",
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
