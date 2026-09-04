"""
Week 8 PPTX content — OBJECT-ORIENTED ANALYSIS: BEHAVIOURAL MODELLING.
"""
from pptxengine import build

CFG = {
    "week": 8,
    "title": "Object-Oriented Analysis — Behavioural Modelling",
    "filename": "Week8_Presentation_BICT3202_OOAD.pptx",
}


def slides(d):
    # 2. learning outcomes
    s = d.slide()
    d.header(s, "Learning Outcomes", "By the end of this week, you should be able to…")
    d.bullets(s, 0.9, 1.6, 11.6, 5.0, [
        ("Define ", "behavioural modelling and why it matters."),
        ("Identify ", "use cases and actors; build a use case diagram."),
        ("Explain ", "the system boundary and include/extend/generalisation."),
        ("Write ", "a detailed use-case specification."),
        ("Construct ", "sequence diagrams (lifelines, activation bars, messages)."),
        ("Construct ", "communication diagrams and activity diagrams (decisions, swimlanes)."),
        ("Connect ", "use cases, activities and interactions into analysis documentation."),
    ], size=17, gap=12)
    d.takeaway(s, "Week 8: how users and objects interact to accomplish tasks.")

    # 3. family
    s = d.slide()
    d.header(s, "The Behavioural Modelling Family", "Each diagram answers a different question")
    d.pic(s, "w8_family.png", y=1.6, w=10.6)
    d.takeaway(s, "Use cases = goals · interactions = messages · activities = workflow.")

    # 4. questions
    s = d.slide()
    d.header(s, "What Question Does Each Diagram Answer?", "Very important for examinations")
    d.pic(s, "w8_questions.png", y=1.6, w=10.6)
    d.takeaway(s, "Choose the diagram by the question you are trying to answer.")

    # 5. use case
    s = d.slide()
    d.header(s, "What Is a Use Case?", "A goal, not a function")
    d.pic(s, "w8_use_case_goal.png", y=1.6, w=10.6)
    d.takeaway(s, "\u201cRegister for Course\u201d is the goal — \u201cClick Register Button\u201d is only an interface action.")

    # 6. actors
    s = d.slide()
    d.header(s, "Actors", "Roles outside the system — not always people")
    d.pic(s, "w8_actor_human.png", y=1.6, w=10.6)
    d.takeaway(s, "A Payment Gateway external to the system is an actor too.")

    # 7. use case diagram
    s = d.slide()
    d.header(s, "A Use Case Diagram", "Actors · use cases · system boundary")
    d.pic(s, "w8_use_case_diagram.png", y=1.6, w=10.6)
    d.takeaway(s, "The rectangle is the system boundary — actors outside, use cases inside.")

    # 8. relationships
    s = d.slide()
    d.header(s, "Use Case Relationships", "Association · include · extend · generalisation")
    d.pic(s, "w8_relationships.png", y=1.6, w=10.6)
    d.takeaway(s, "include = required · extend = conditional · generalisation = is-a.")

    # 9. include vs extend
    s = d.slide()
    d.header(s, "include vs extend", "An examination favourite")
    d.pic(s, "w8_include_extend.png", y=1.6, w=10.4)
    d.takeaway(s, "INCLUDE = \u201cI need this as part of the job\u201d · EXTEND = \u201cI might add this.\u201d")

    # 10. specification
    s = d.slide()
    d.header(s, "Use Case Specifications", "The diagram is not enough")
    d.pic(s, "w8_specification.png", y=1.6, w=10.6)
    d.takeaway(s, "Capture the main scenario AND the alternative/exception paths.")

    # 11. sequence components
    s = d.slide()
    d.header(s, "Sequence Diagram Components", "Lifelines · activation bars · messages")
    d.pic(s, "w8_sequence_components.png", y=1.6, w=10.6)
    d.takeaway(s, "Read top to bottom — time flows downward.")

    # 12. login sequence
    s = d.slide()
    d.header(s, "Sequence Diagram — Login", "Who communicates with whom, in what order")
    d.pic(s, "w8_sequence_login.png", y=1.6, w=10.6)
    d.takeaway(s, "Order matters — you cannot confirm login before validating credentials.")

    # 13. fragments
    s = d.slide()
    d.header(s, "Combined Fragments — alt, loop, opt", "Alternatives, repetition, optional")
    d.pic(s, "w8_fragments.png", y=1.6, w=10.6)
    d.takeaway(s, "alt = branch by guard · loop = repeat · opt = run only if true.")

    # 14. communication
    s = d.slide()
    d.header(s, "Communication (Collaboration) Diagram", "Objects + numbered messages")
    d.pic(s, "w8_communication.png", y=1.6, w=10.6)
    d.takeaway(s, "Numbers 1, 2, 3, 4 show order; older name = collaboration diagram.")

    # 15. sequence vs communication
    s = d.slide()
    d.header(s, "Sequence vs Communication", "Same interaction, different emphasis")
    d.pic(s, "w8_seq_vs_comm.png", y=1.6, w=10.4)
    d.takeaway(s, "Sequence = time/order · Communication = objects and their links.")

    # 16. activity notation
    s = d.slide()
    d.header(s, "Activity Diagram Notation", "Initial · actions · decision · fork/join · final")
    d.pic(s, "w8_activity_notation.png", y=1.6, w=10.6)
    d.takeaway(s, "The diamond is a decision; thick bars are fork (split) and join (synchronise).")

    # 17. activity example
    s = d.slide()
    d.header(s, "Activity Diagram — Online Shopping", "A workflow with a decision")
    d.pic(s, "w8_activity_example.png", y=1.6, w=10.6)
    d.takeaway(s, "After payment: [successful] -> Create Order · [failed] -> Show Error.")

    # 18. swimlanes
    s = d.slide()
    d.header(s, "Swimlanes", "Who is responsible for each activity?")
    d.pic(s, "w8_swimlanes.png", y=1.6, w=10.6)
    d.takeaway(s, "Student selects/confirms; System checks prerequisites and creates the registration.")

    # 19. models together
    s = d.slide()
    d.header(s, "How the Models Work Together", "Requirement -> design, with traceability")
    d.pic(s, "w8_traceability.png", y=1.6, w=10.6)
    d.takeaway(s, "Use case -> activity -> sequence -> communication -> analysis model -> design.")

    # 20. full example
    s = d.slide()
    d.header(s, "A Full Example — Assignment Submission", "Four models, one requirement")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Use case: ", "Submit Assignment (actor: Student)."),
        ("Specification: ", "log in -> open course -> select assignment -> upload -> validate -> submit -> confirm."),
        ("Activity: ", "Login -> Open Course -> Upload File -> (valid? Submit : Show Error) -> Confirm."),
        ("Sequence: ", "Student -> Web UI -> Assignment Controller -> Database."),
        ("Communication: ", "1: upload, 2: submit, 3: validate, 4: save, 5: confirmation."),
    ], size=16, gap=12)
    d.takeaway(s, "The same requirement described from different perspectives — that is behavioural analysis.")

    # 21. documentation
    s = d.slide()
    d.header(s, "Full Analysis Documentation", "Everything that explains what the system must do")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Contents: ", "problem statement, requirements, actors, use cases + specifications, activity, sequence, communication, class and state diagrams, assumptions, constraints, business rules, glossary."),
        ("Why it matters: ", "client, analyst, designer, programmer, tester and manager all need a common language."),
        ("Traceability: ", "REQ-05 -> UC-05 -> activity model -> sequence model -> design -> test cases."),
    ], size=16, gap=14)
    d.takeaway(s, "Documentation creates traceability from requirement to test.")

    # 22. common confusions
    s = d.slide()
    d.header(s, "Common Confusions", "Five distinctions to master")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Use case vs diagram ", "— a goal vs the visual representation."),
        ("Use case vs activity ", "— what goal vs what workflow."),
        ("Activity vs sequence ", "— workflow vs messages over time."),
        ("Sequence vs communication ", "— time/order vs objects/links."),
        ("Actor vs class ", "— external role vs a type inside the system."),
    ], size=16, gap=13)
    d.takeaway(s, "These distinctions are examination favourites.")

    # 23. practical
    s = d.slide()
    d.header(s, "Practical Lab — Course Registration", "Five tasks, one system")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("1. Use case diagram ", "— boundary, 4+ actors, 8+ use cases, include/extend/generalisation."),
        ("2. Specification ", "— full document for Register Course."),
        ("3. Activity diagram ", "— decisions, alternatives, swimlanes."),
        ("4. Sequence diagram ", "— 8+ messages: Student -> UI -> Controller -> Database."),
        ("5. Communication diagram ", "— the same scenario, numbered messages."),
    ], size=16, gap=12)
    d.takeaway(s, "Then compare the sequence and communication diagrams — what changed in emphasis?")

    # 24. summary
    s = d.slide()
    d.header(s, "Week 8 Summary", "The essentials")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Use case ", "— the actor's goal; the diagram shows actors, use cases and the boundary."),
        ("include / extend ", "— required/reused vs conditional/additional behaviour."),
        ("Sequence diagram ", "— messages in time order."),
        ("Communication diagram ", "— objects and numbered messages."),
        ("Activity diagram ", "— workflow with decisions, forks/joins and swimlanes."),
        ("Documentation ", "— all models together, with traceability."),
    ], size=16, gap=12)
    d.takeaway(s, "A system is behaviours performed by users and objects working together to reach goals.")

    # 25. closing
    d.closing("REVISION & NEXT STEPS", [
        "Model the ATM system: actors, use cases, include/extend, one specification, activity and sequence diagrams.",
        "Practise include vs extend until the memory trick is automatic.",
        "Draw sequence and communication diagrams for the same scenario and compare them.",
        "Next week: The Unified Software Development Process (USDP/UP) — phases, workflows and artefacts.",
    ])


def build_pptx():
    return build(CFG, slides)


if __name__ == "__main__":
    print("Built:", build_pptx())
