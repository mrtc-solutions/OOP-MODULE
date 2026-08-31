"""
Week 7 PPTX content — OBJECT-ORIENTED ANALYSIS: DYNAMIC MODELLING.
"""
from pptxengine import build

CFG = {
    "week": 7,
    "title": "Object-Oriented Analysis — Dynamic Modelling",
    "filename": "Week7_Presentation_BICT3202_OOAD.pptx",
}


def slides(d):
    # 2. learning outcomes
    s = d.slide()
    d.header(s, "Learning Outcomes", "By the end of this week, you should be able to…")
    d.bullets(s, 0.9, 1.6, 11.6, 5.0, [
        ("Define ", "dynamic modelling and explain why behaviour must be modelled."),
        ("Define ", "events and states, and tell them apart."),
        ("Explain ", "transitions, initial/final states and guards."),
        ("Explain ", "entry, exit and do behaviour."),
        ("Distinguish ", "operations from events, and explain state change."),
        ("Explain ", "concurrency and model concurrent states."),
        ("Relate ", "structural and dynamic models."),
        ("Use ", "a CASE tool to build and inspect a state machine."),
    ], size=17, gap=12)
    d.takeaway(s, "Week 7 moves from \u201cwhat exists\u201d to \u201cwhat happens over time.\u201d")

    # 3. structural vs dynamic
    s = d.slide()
    d.header(s, "Structural vs Dynamic Modelling", "What exists vs what happens")
    d.pic(s, "w7_structural_vs_dynamic.png", y=1.6, w=10.6)
    d.takeaway(s, "Structural = classes, attributes, associations · Dynamic = events, states, transitions.")

    # 4. car analogy
    s = d.slide()
    d.header(s, "The Car Analogy", "Design/parts vs behaviour")
    d.pic(s, "w7_car_analogy.png", y=1.6, w=10.6)
    d.takeaway(s, "The class diagram tells us the parts; the state machine tells us what happens.")

    # 5. events
    s = d.slide()
    d.header(s, "What Is an Event?", "Something that happens — to which the system responds")
    d.pic(s, "w7_events.png", y=1.6, w=10.6)
    d.takeaway(s, "User · system · external · data events — e.g. click Login, timer expires, payment received.")

    # 6. event vs state
    s = d.slide()
    d.header(s, "Event vs State", "A common mistake")
    d.pic(s, "w7_event_vs_state.png", y=1.6, w=10.4)
    d.takeaway(s, "Event = something happens · State = something is. PaymentReceived ≠ Paid.")

    # 7. order lifecycle
    s = d.slide()
    d.header(s, "The Order Lifecycle", "An object changes state as events occur")
    d.pic(s, "w7_order_states.png", y=1.6, w=10.6)
    d.takeaway(s, "Pending → Paid → Processing → Shipped → Delivered — read it as a story.")

    # 8. notation
    s = d.slide()
    d.header(s, "State-Machine Notation", "Initial · states · transitions · final")
    d.pic(s, "w7_notation.png", y=1.6, w=10.6)
    d.takeaway(s, "Filled circle begins the lifecycle; the bull's-eye ends it; arrows carry events.")

    # 9. guards
    s = d.slide()
    d.header(s, "Guards", "Conditions on transitions")
    d.pic(s, "w7_guards.png", y=1.6, w=10.6)
    d.takeaway(s, "[balance sufficient] → Cash Dispensed · [balance insufficient] → Insufficient Funds.")

    # 10. entry / exit / do
    s = d.slide()
    d.header(s, "Entry, Exit and Do Behaviour", "Behaviour attached to a state")
    d.pic(s, "w7_entry_exit_do.png", y=1.6, w=10.6)
    d.takeaway(s, "entry / on arrival · exit / on leaving · do / while inside the state.")

    # 11. payment state machine
    s = d.slide()
    d.header(s, "A Complete State Machine — Payment", "Read it as a story")
    d.pic(s, "w7_payment_states.png", y=1.6, w=10.6)
    d.takeaway(s, "Pending → Processing → (success: Paid | failure: Failed).")

    # 12. operation vs event
    s = d.slide()
    d.header(s, "Operation vs Event", "Another common confusion")
    d.pic(s, "w7_operation_vs_event.png", y=1.6, w=10.4)
    d.takeaway(s, "Operation = can be invoked (calculateTotal()) · Event = occurs (PaymentReceived).")

    # 13. operation state change
    s = d.slide()
    d.header(s, "Operations Can Change State", "An ATM's operations move it between states")
    d.pic(s, "w7_operation_state_change.png", y=1.6, w=10.6)
    d.takeaway(s, "insertCard(): Idle → Card Inserted · ejectCard(): Card Inserted → Idle.")

    # 14. concurrency
    s = d.slide()
    d.header(s, "Sequential vs Concurrent", "One-after-another vs at-the-same-time")
    d.pic(s, "w7_concurrency.png", y=1.6, w=10.6)
    d.takeaway(s, "After placing an order: payment, preparation and driver assignment can overlap.")

    # 15. airport
    s = d.slide()
    d.header(s, "Concurrency in Real Life — Airport", "Two activities at once")
    d.pic(s, "w7_airport.png", y=1.6, w=10.6)
    d.takeaway(s, "Security screening and baggage processing run concurrently, then join before boarding.")

    # 16. concurrent regions
    s = d.slide()
    d.header(s, "UML Concurrent Regions", "A composite state with parallel regions")
    d.pic(s, "w7_concurrent_regions.png", y=1.6, w=10.6)
    d.takeaway(s, "Order Processing = Payment region + Delivery region, joining at Completed.")

    # 17. structure + dynamic
    s = d.slide()
    d.header(s, "Two Models That Complement Each Other", "The ATM")
    d.pic(s, "w7_atm_both.png", y=1.6, w=10.6)
    d.takeaway(s, "Neither replaces the other — structure + behaviour = complete understanding.")

    # 18. dynamic reveals problems
    s = d.slide()
    d.header(s, "Dynamic Models Reveal Problems", "Impossible transitions surface requirements gaps")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("A class diagram ", "shows Order with cancelOrder() — but when is it allowed?"),
        ("The state machine ", "shows Delivered → Cancelled, which may not make business sense."),
        ("Correct rule: ", "Pending/Paid/Processing → Cancelled; Shipped/Delivered → Return process."),
        ("",""),
        ("Modelling behaviour ", "exposes requirements problems before implementation."),
    ], size=17, gap=14)
    d.takeaway(s, "That is a key reason analysts model behaviour, not just structure.")

    # 19. hospital example
    s = d.slide()
    d.header(s, "Complete Example — Hospital Appointment", "A full state machine")
    d.pic(s, "w7_hospital.png", y=1.6, w=10.6)
    d.takeaway(s, "Requested → Confirmed → Checked In → Waiting → With Doctor → Completed (or Cancelled).")

    # 20. state vs class vs object
    s = d.slide()
    d.header(s, "State vs Class vs Object", "Three distinct ideas")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Class ", "— a blueprint/type: Order."),
        ("Object ", "— a specific instance: order1024."),
        ("State ", "— the condition of that object: Paid."),
        ("Event ", "— something that happens: PaymentReceived."),
        ("",""),
        ("Order #1001 → Paid · #1002 → Pending · #1003 → Shipped", "— same class, different states."),
    ], size=17, gap=13)
    d.takeaway(s, "A state describes the current condition of an object during its lifecycle.")

    # 21. state machine vs flowchart
    s = d.slide()
    d.header(s, "State Machine vs Flowchart", "They are not the same")
    d.bullets(s, 0.9, 1.6, 5.7, 4.9, [
        ("Flowchart thinking ", "— procedural flow:"),
        "Calculate total", "Check payment", "Print receipt",
        "","",
    ], size=16, gap=10)
    d.bullets(s, 6.9, 1.6, 5.4, 4.9, [
        ("State-machine thinking ", "— lifecycle of an object:"),
        "Pending → (PaymentReceived) → Paid", "Paid → (Dispatched) → Shipped",
        "focuses on states + events", "",
    ], size=16, gap=10)
    d.takeaway(s, "A state machine is about an entity's states and event-driven transitions — not procedural steps.")

    # 22. traffic light
    s = d.slide()
    d.header(s, "The Traffic Light", "A simple state machine — and intersection concurrency")
    d.pic(s, "w7_traffic_light.png", y=1.6, w=10.6)
    d.takeaway(s, "Red → Green → Yellow → Red; at an intersection, two controllers coordinate concurrently.")

    # 23. practical
    s = d.slide()
    d.header(s, "Practical Lab — Online Order", "Build a full state machine")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("States: ", "New · Pending Payment · Paid · Processing · Shipped · Delivered · Cancelled · Returned."),
        ("Events: ", "placeOrder · paymentConfirmed · dispatchOrder · deliverOrder · cancelOrder · requestReturn."),
        ("Guards: ", "requestReturn [within return period]."),
        ("Entry behaviour: ", "entry / sendNotification() on Paid · entry / notifyCustomer() on Shipped."),
    ], size=16, gap=13)
    d.takeaway(s, "Add guards and entry behaviour — then explain what happens on entering each state.")

    # 24. common mistakes
    s = d.slide()
    d.header(s, "Common Student Mistakes", "Avoid these five")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Event as a state ", "— PaymentReceived is an event, not [PaymentReceived]."),
        ("Operation as a state ", "— processPayment() is an operation, not [ProcessPayment]."),
        ("Forgetting the object ", "— whose state are we describing?"),
        ("Impossible transitions ", "— Delivered → Paid may make no sense."),
        ("A state for every action ", "— \u201cClick Button\u201d is an event, not a state."),
    ], size=16, gap=12)
    d.takeaway(s, "If you cannot explain the diagram in words, you probably don't understand the model.")

    # 25. summary
    s = d.slide()
    d.header(s, "Week 7 Summary", "The essentials")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Dynamic modelling ", "— behaviour and change over time."),
        ("Event ", "— something that happens; can trigger a transition."),
        ("State ", "— a condition of an object over time."),
        ("Transition + guard ", "— movement between states, gated by a condition."),
        ("Operation ", "— behaviour/service that can change state."),
        ("Concurrency ", "— activities in parallel or overlapping."),
        ("Structure + dynamic ", "— together, a complete object-oriented model."),
    ], size=16, gap=12)
    d.takeaway(s, "Object → state → event → transition → new state — the heart of dynamic modelling.")

    # 26. closing
    d.closing("REVISION & NEXT STEPS", [
        "Draw the ATM-withdrawal and bank-account state machines with guards, entry and exit behaviour.",
        "Read every state machine you draw aloud as a story — then check the transitions make sense.",
        "Build the online-order state machine in your CASE tool and add concurrent regions.",
        "Next week: Behavioural Modelling — use cases, sequence, collaboration and activity diagrams.",
    ])


def build_pptx():
    return build(CFG, slides)


if __name__ == "__main__":
    print("Built:", build_pptx())
