"""
Week 7 PDF content — OBJECT-ORIENTED ANALYSIS: DYNAMIC MODELLING.
"""
from pdfengine import (H1, H2, P, BUL, FIG, CALLOUT, DTABLE, build, DOC_W,
                      C_MAROON, C_SOFT)

CFG = {
    "week": 7,
    "title": "Object-Oriented Analysis — Dynamic Modelling",
    "filename": "Week7_Module_BICT3202_OOAD.pdf",
}


def story():
    s = []

    # 1. introduction --------------------------------------------------------
    s.append(H1("1.  Week 7 Introduction"))
    s += [P("Previous weeks mainly asked: <b>“What things exist in the system and how are they "
            "structurally related?”</b> Week 7 asks a different question: <b>“What happens to those things "
            "over time, and how do they respond to events?”</b> That distinction is fundamental to "
            "object-oriented modelling. The OMG UML specification separates UML into structural and "
            "behavioural semantic areas — state machines, activities and interactions are behavioural "
            "modelling constructs, while classes, classifiers and packages belong to structural "
            "modelling."),
          P("This week's official topics are: <b>event, state, operations, concurrency, the relation of "
            "structure and dynamic models, and CASE tool support</b> — all six are covered, not simply "
            "“state diagrams”.")]

    # 2. learning outcomes -----------------------------------------------------
    s.append(H1("2.  Learning Outcomes"))
    s += [P("By the end of this week, a student should be able to:")]
    s += BUL([
        "Define dynamic modelling and explain why dynamic behaviour must be modelled.",
        "Define an event and identify different types of events.",
        "Define a state and distinguish a state from an event.",
        "Explain state transitions, initial and final states, and guards.",
        "Explain entry, exit and do-activity behaviour.",
        "Define an operation and distinguish an operation from an event.",
        "Construct a UML state-machine diagram.",
        "Explain concurrency and distinguish sequential from concurrent behaviour.",
        "Explain the relationship between structural and dynamic models.",
        "Use a CASE tool to create and inspect dynamic models.",
    ])

    # ============ PART A — DYNAMIC MODELLING ============
    s.append(H1("PART A — WHAT IS DYNAMIC MODELLING?"))
    s.append(H1("3.  What Does \"Dynamic\" Mean?"))
    s += [P("Dynamic means <b>something that changes over time</b>. In a student registration system, a "
            "student moves from <b>Not Registered</b> to <b>Registration Pending</b> (after submitting) "
            "to <b>Registered</b> (after payment is confirmed). That changing behaviour is what dynamic "
            "modelling describes."),
          P("<b>Structural modelling asks “what exists?”</b> — Student, Course, Lecturer, Registration — "
            "and how they relate. <b>Dynamic modelling asks “what happens?”</b> — Student selects course, "
            "registration is submitted, payment is made, registration is confirmed. The formal "
            "specification describes behavioural semantics in terms of behaviour and state changes built "
            "upon the structural model.")]
    s += FIG("w7_structural_vs_dynamic.png", "Figure 1 — Structural vs dynamic modelling")
    s += FIG("w7_car_analogy.png", "Figure 2 — The car analogy: design/parts vs behaviour")

    # ============ PART B — EVENTS ============
    s.append(H1("PART B — EVENTS"))
    s.append(H1("4.  What Is an Event?"))
    s += [P("An <b>event</b> is something that occurs and can cause a change in behaviour or state — in "
            "simple English, <b>something that happens to which the system can respond</b>. Examples: a "
            "user clicks Login, a customer places an Order, an ATM card is inserted, a payment is "
            "received, a temperature exceeds a limit, a student submits an assignment."),
          P("Events fall into broad categories: <b>user-generated</b> (click Login, submit form, select "
            "product, upload file), <b>system-generated</b> (timer expires, backup completed, session "
            "timeout), <b>external</b> (payment gateway confirmation, bank transaction response, sensor "
            "detects movement), and <b>data-related</b> (payment received, stock reaches zero, balance "
            "falls below threshold).")]
    s += FIG("w7_events.png", "Figure 3 — Categories and examples of events")

    s.append(H1("5.  Events Are NOT States"))
    s += [P("This is a common student mistake. An <b>event</b> is something that happens — “Customer "
            "clicks Pay”. A <b>state</b> is a condition that exists for some period of time — “Payment "
            "Pending”. So: event → something happens; state → something is/exists. An event can trigger a "
            "<b>transition</b>: in <font name='Mono'>[Locked] —Correct PIN→ [Unlocked]</font>, Locked and "
            "Unlocked are states and “Correct PIN” is the event/trigger.")]
    s += FIG("w7_event_vs_state.png", "Figure 4 — Event vs state")

    # ============ PART C — STATES ============
    s.append(H1("PART C — STATES"))
    s.append(H1("6.  States and the UML State Diagram"))
    s += [P("A <b>state</b> represents a condition or situation in which an object exists during some "
            "period of its behaviour. An Order can be Pending, Paid, Processing, Shipped, Delivered or "
            "Cancelled. In a state-machine diagram, the <b>filled circle</b> (●) is the initial "
            "pseudostate, the <b>bull's-eye</b> (◎) is the final state, rounded rectangles are states, "
            "and labelled arrows are transitions carrying the trigger/event.")]
    s += FIG("w7_order_states.png", "Figure 5 — The Order lifecycle")
    s += FIG("w7_notation.png", "Figure 6 — State-machine notation")

    s.append(H1("7.  Transitions and Guards"))
    s += [P("A <b>transition</b> describes movement from a source state to a target state — "
            "<font name='Mono'>Pending ──payment received──→ Paid</font>. Sometimes an event alone is not "
            "enough: the system may need a <b>condition</b>. A <b>guard</b> is written in square "
            "brackets, e.g. <font name='Mono'>payment received [amount ≥ total]</font>, and means the "
            "transition can happen only if the condition is true. One state can have several possible "
            "transitions — an ATM withdrawal with sufficient balance dispenses cash, while insufficient "
            "balance leads to “Insufficient Funds”.")]
    s += FIG("w7_guards.png", "Figure 7 — Guards on transitions (ATM withdrawal)")

    s.append(H1("8.  Entry, Exit and Do Behaviour"))
    s += [P("A state can carry behaviour: <b>entry</b> — action performed when the state is entered "
            "(<font name='Mono'>entry / sendConfirmationEmail()</font>); <b>exit</b> — action performed "
            "when the state is left (<font name='Mono'>exit / updateTransactionLog()</font>); and "
            "<b>do</b> — behaviour that occurs while the object remains in the state "
            "(<font name='Mono'>do / processOrder()</font>), which is different from an instantaneous "
            "transition trigger. The UML specification recognises entry, exit and do-activity behaviours "
            "associated with states.")]
    s += FIG("w7_entry_exit_do.png", "Figure 8 — Entry, exit and do behaviour")
    s += FIG("w7_payment_states.png", "Figure 9 — A complete state machine (online payment)")

    # ============ PART D — OPERATIONS ============
    s.append(H1("PART D — OPERATIONS"))
    s.append(H1("9.  Operations and State Change"))
    s += [P("An <b>operation</b> is a service or behaviour that an object/class provides — Order has "
            "calculateTotal(), submitOrder() and cancelOrder(). Students often confuse operations with "
            "events: an operation is something the object can <b>perform or provide</b> (it can be "
            "invoked), while an event is something that <b>occurs</b> and can trigger behaviour. "
            "Operations can participate in dynamic behaviour — invoking "
            "<font name='Mono'>insertCard()</font> moves an ATM from Idle to Card Inserted, and "
            "<font name='Mono'>ejectCard()</font> returns it to Idle.")]
    s += FIG("w7_operation_vs_event.png", "Figure 10 — Operation vs event")
    s += FIG("w7_operation_state_change.png", "Figure 11 — Operations causing state change")

    # ============ PART E — CONCURRENCY ============
    s.append(H1("PART E — CONCURRENCY"))
    s.append(H1("10.  Concurrency"))
    s += [P("<b>Concurrency</b> means multiple activities or behaviours can occur during the same period "
            "rather than strictly one after another. After placing a food order, the restaurant prepares "
            "food <b>while</b> a driver is assigned <b>while</b> payment is processed — they need not "
            "happen in a strict sequence. <b>Sequential</b> behaviour runs one thing after another "
            "(Enter PIN → Validate PIN → Display account); <b>concurrent</b> behaviour runs activities in "
            "parallel (Order Placed splits into Process Payment and Prepare Order)."),
          P("A real-life example: when a passenger checks in at an airport, security screening and baggage "
            "processing can happen concurrently, then both complete before boarding. In UML, a composite "
            "state can contain <b>concurrent regions</b> — Order Processing can split into a Payment "
            "region and a Delivery region that execute concurrently and join when both finish. Modern "
            "systems — banking, e-commerce, social media, mobile apps — routinely perform several "
            "activities simultaneously, so analysts must understand non-sequential behaviour.")]
    s += FIG("w7_concurrency.png", "Figure 12 — Sequential vs concurrent behaviour")
    s += FIG("w7_airport.png", "Figure 13 — Concurrency at the airport")
    s += FIG("w7_concurrent_regions.png", "Figure 14 — UML concurrent regions")

    # ============ PART F — STRUCTURE & DYNAMIC ============
    s.append(H1("PART F — RELATIONSHIP BETWEEN STRUCTURAL AND DYNAMIC MODELS"))
    s.append(H1("11.  Why Do We Need Both?"))
    s += [P("A class diagram tells us the structure of an Order, but not what sequence of behaviour is "
            "allowed — can an order go directly from Pending to Shipped without payment? The dynamic model "
            "makes such rules visible. <b>Structural model</b> = “what is the system made of?”; <b>dynamic "
            "model</b> = “how does the system behave?”; together they give <b>complete understanding</b>. "
            "Neither replaces the other."),
          P("Dynamic models can also <b>reveal requirements problems</b>: if the model shows a Delivered "
            "order moving to Cancelled, that may not make business sense — perhaps the correct rule is "
            "that Pending, Paid and Processing orders can be cancelled, while Shipped and Delivered orders "
            "enter a Return process. That is an important reason analysts model behaviour.")]
    s += FIG("w7_atm_both.png", "Figure 15 — ATM: structural and dynamic models together")

    # ============ PART G — CASE TOOL ============
    s.append(H1("PART G — CASE TOOL SUPPORT"))
    s.append(H1("12.  Using a CASE Tool for Dynamic Models"))
    s += [P("CASE (<b>Computer-Aided Software Engineering</b>) tools help analysts create class, "
            "state-machine, activity, sequence, use-case and package diagrams. When a lecturer says "
            "“change Customer to User”, a CASE tool makes updating 30 classes and 20 transitions far "
            "easier than manual drawing. Examples include Enterprise Architect, Visual Paradigm, IBM "
            "Rational tools, StarUML, PlantUML and diagrams.net/draw.io; the course outline specifies a "
            "Select Enterprise demonstration. Students should be able to create a project, add states, "
            "transitions, event labels, guards, entry/exit behaviour and final states, then modify the "
            "model when requirements change.")]

    # ============ COMPLETE EXAMPLE ============
    s.append(H1("PART H — COMPLETE EXAMPLE"))
    s.append(H1("13.  Hospital Patient Dynamic Model"))
    s += [P("Model a patient appointment with states Appointment Requested, Confirmed, Checked In, "
            "Waiting, With Doctor, Completed and Cancelled, and events requestAppointment, "
            "confirmAppointment, patientArrives, joinQueue, doctorCallsPatient, consultationComplete and "
            "cancelAppointment. <b>Read the diagram as a story</b>: an appointment begins Requested; when "
            "confirmed it moves to Confirmed; when the patient arrives it becomes Checked In; the patient "
            "waits until the doctor calls them; the appointment enters With Doctor; when the consultation "
            "finishes it becomes Completed — or it can be cancelled before completion. If a student cannot "
            "explain the diagram in words, they probably do not understand the model."),
          P("Add guards where business rules apply — <font name='Mono'>confirmAppointment [doctor "
            "available]</font> leads to Confirmed, while <font name='Mono'>[doctor unavailable]</font> "
            "leads to Waitlisted. Add operations to the Appointment class (request(), confirm(), cancel(), "
            "checkIn(), complete()) — the dynamic model explains <b>when</b> those behaviours are "
            "allowed.")]
    s += FIG("w7_hospital.png", "Figure 16 — Hospital appointment state machine")

    # ============ DISTINCTIONS ============
    s.append(H1("14.  State vs Class vs Object — and State Machine vs Flowchart"))
    s += [P("<b>Class</b> is a blueprint/type (Order); <b>object</b> is a specific instance (order1024); "
            "<b>state</b> is the condition of that object (Paid); <b>event</b> is something that happens "
            "(PaymentReceived). Different objects of the same class can be in different states: Order "
            "#1001 → Paid, #1002 → Pending, #1003 → Shipped. <b>A state describes the current condition "
            "of an object during its lifecycle.</b>"),
          P("A state machine is <b>not</b> a flowchart: a flowchart represents procedural flow "
            "(calculate total → check payment → print receipt), while a state machine focuses on the "
            "states of an entity and the transitions between them in response to events. Dynamic modelling "
            "is especially useful when an object has several meaningful states, changes state during its "
            "lifecycle, responds to events, has business rules governing transitions, or has concurrent "
            "behaviour — Order, BankAccount, ATM, TrafficLight, PatientAppointment, LoanApplication, "
            "Booking, InsuranceClaim, StudentRegistration.")]

    s.append(H1("15.  The Traffic Light Example"))
    s += [P("The traffic light is excellent for beginners because the states are obvious: Red, Green, "
            "Yellow — timer expiry drives each transition. A modern intersection has a North/South "
            "controller and an East/West controller whose behaviour must coordinate, introducing "
            "concurrent state-machine regions whose transitions must be coordinated safely.")]
    s += FIG("w7_traffic_light.png", "Figure 17 — Traffic light state machine and intersection concurrency")

    # ============ PRACTICAL & MISTAKES ============
    s.append(H1("16.  Practical Lab and Tutorial"))
    s += [P("<b>Practical — Online Shopping Order:</b> create a state-machine diagram with states New, "
            "Pending Payment, Paid, Processing, Shipped, Delivered, Cancelled and Returned; events "
            "placeOrder, makePayment, paymentConfirmed, dispatchOrder, deliverOrder, cancelOrder, "
            "requestReturn, approveReturn; add guards such as "
            "<font name='Mono'>requestReturn [within return period]</font>; and add entry behaviour such "
            "as <font name='Mono'>entry / sendNotification()</font> to Paid and "
            "<font name='Mono'>entry / notifyCustomer()</font> to Shipped."),
          P("<b>Tutorial:</b> (1) a bank account with states Active, Blocked, Closed and events login, "
            "wrongPIN, blockAccount, unblockAccount, closeAccount — draw the machine, add guards, and "
            "identify which transitions should not be allowed; (2) explain the difference between an event "
            "and a state; (3) explain why a class diagram alone is insufficient for a complex Order "
            "object.")]

    s.append(H1("17.  Common Student Mistakes"))
    mistakes = [
        ("Mistake 1 — Treating an event as a state.",
         "“PaymentReceived” is an instantaneous event, not a state — model Pending ──PaymentReceived──→ Paid."),
        ("Mistake 2 — Confusing an operation with a state.",
         "processPayment() is an operation — model [Pending] ──processPayment()──→ [Processing]."),
        ("Mistake 3 — Forgetting the object being modelled.",
         "A state machine should have a clear context (Order, Payment, ATM, StudentRegistration) — not a collection of random states."),
        ("Mistake 4 — Creating impossible transitions.",
         "Delivered → Paid may make no sense — use domain requirements, not arbitrary arrows."),
        ("Mistake 5 — A state for every small action.",
         "“Click Button” is normally an event; “Processing” is a meaningful state."),
    ]
    for head, fix in mistakes:
        s.append(CALLOUT(head, [fix], bar=C_SOFT, tcol=C_MAROON))

    # ============ SUMMARY ============
    s.append(H1("18.  Week 7 Summary and Key Terms"))
    s.append(DTABLE(
        ["Concept", "Simple meaning", "Example"],
        [["Dynamic modelling", "Behaviour/change over time", "Order lifecycle"],
         ["Event", "Something that happens", "Payment received"],
         ["State", "Condition of an object", "Paid"],
         ["Transition", "Movement between states", "Pending → Paid"],
         ["Guard", "Condition controlling a transition", "[payment valid]"],
         ["Operation", "Behaviour/service of an object", "cancelOrder()"],
         ["Initial / final state", "Starting point / end point", "● / ◎"],
         ["Entry / exit / do", "Behaviour on entering / leaving / within a state", "sendEmail()"],
         ["Concurrency", "Activities in parallel/overlapping", "Payment + preparation"],
         ["Structural / dynamic model", "What exists / what happens", "Classes / states"]],
        widths=[0.26 * DOC_W, 0.4 * DOC_W, 0.34 * DOC_W]))
    s.append(CALLOUT("THE MOST IMPORTANT PICTURE",
        ["An object exists → it is in a state → an event occurs → a transition happens → the object "
         "enters another state. That is the heart of dynamic modelling. Whenever you face a "
         "dynamic-modelling problem, ask four questions: <b>What object am I modelling? What states can "
         "it be in? What events cause it to change? What conditions determine which transition "
         "occurs?</b> Answer those four questions and you are already thinking like an object-oriented "
         "analyst."]))

    # ============ EXAM QUESTIONS ============
    s.append(H1("19.  Examination-Style Questions"))
    s += [P("<b>Question 1 (Definitions).</b> Define dynamic modelling, event, state, transition, guard "
            "condition, operation and concurrency. [14 marks]"),
          P("<b>Question 2 (Differences).</b> Explain the difference between: event and state; operation "
            "and event; structural model and dynamic model; sequential and concurrent behaviour. "
            "[16 marks]"),
          P("<b>Question 3 (State machine).</b> A university student registration can move through Not "
            "Registered, Registration Pending, Payment Pending, Registered and Cancelled, with events "
            "submitRegistration, makePayment, paymentConfirmed and cancelRegistration. Draw an appropriate "
            "UML state-machine diagram. [15 marks]"),
          P("<b>Question 4 (Analysis).</b> Explain why dynamic modelling is important when analysing an "
            "online banking system, including at least four examples of objects whose states change over "
            "time. [10 marks]"),
          P("<b>Question 5 (Concurrency).</b> A food delivery application performs payment processing, "
            "restaurant order preparation, driver assignment and customer notification after an order is "
            "placed. Explain which activities could occur concurrently and why. [10 marks]")]

    # ============ REFERENCES ============
    s.append(H1("20.  References and Further Reading"))
    s.append(H2("Primary authoritative reference"))
    s += BUL([
        "Object Management Group. (2017). <i>OMG Unified Modeling Language (UML), Version 2.5.1.</i> OMG — the formal reference for UML, including the structural and behavioural semantic foundations and state machines.",
        "Object Management Group. <i>UML 2.5.1 — State Machines and Behavioural Semantics</i> (states, transitions, events, behaviours and related state-machine concepts).",
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
