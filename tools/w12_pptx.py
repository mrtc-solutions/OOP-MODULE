"""
Week 12 PPTX content — INTEGRATED OBJECT-ORIENTED MODELLING AND DESIGN.
"""
from pptxengine import build

CFG = {
    "week": 12,
    "title": "Integrated Object-Oriented Modelling and Design",
    "filename": "Week12_Presentation_BICT3202_OOAD.pptx",
}


def slides(d):
    # 2. learning outcomes
    s = d.slide()
    d.header(s, "Learning Outcomes", "By the end of this week, you should be able to…")
    d.bullets(s, 0.9, 1.6, 11.6, 5.0, [
        ("Explain ", "integrated modelling and why models must be consistent."),
        ("Relate ", "the use-case, class, interaction, state and activity models."),
        ("Trace ", "a requirement through classes, interactions and operations."),
        ("Apply ", "multiplicity and packages to organise a model."),
        ("Think ", "at component and architecture level."),
        ("Detect ", "contradictions between models and validate a design."),
        ("Distinguish ", "a model from a diagram."),
    ], size=16, gap=11)
    d.takeaway(s, "Every model should contribute to the same understanding of the system.")

    # 3. progression
    s = d.slide()
    d.header(s, "Week 11 -> 12 -> 13", "From detailed design elements to one coherent system")
    d.pic(s, "w12_progression.png", y=1.6, w=10.6)
    d.takeaway(s, "Week 12 brings every model together into one consistent system design.")

    # 4. house analogy
    s = d.slide()
    d.header(s, "Integrated Modelling: The House Analogy", "Different drawings must describe the SAME house")
    d.pic(s, "w12_house_analogy.png", y=1.6, w=10.6)
    d.takeaway(s, "Software models must collectively tell a coherent story.")

    # 5. model views
    s = d.slide()
    d.header(s, "Different Models, Different Questions", "Many views of the same system")
    d.pic(s, "w12_model_views.png", y=1.6, w=10.6)
    d.takeaway(s, "UML groups structural and behavioural modelling into different parts of its specification.")

    # 6. big picture
    s = d.slide()
    d.header(s, "The Big Picture", "Requirements -> models -> integrated design -> implementation")
    d.pic(s, "w12_big_picture.png", y=1.5, w=10.4)
    d.takeaway(s, "That is the central idea of Week 12.")

    # 7. consistency
    s = d.slide()
    d.header(s, "Model Consistency", "The models must agree — here they do not")
    d.pic(s, "w12_consistency.png", y=1.6, w=10.6)
    d.takeaway(s, "The class model lacks Course and Registration — inconsistent with the use case.")

    # 8. traceability
    s = d.slide()
    d.header(s, "Traceability", "Where did this design element come from?")
    d.pic(s, "w12_traceability.png", y=1.5, w=10.6)
    d.takeaway(s, "A traceable design links every element back to a requirement.")

    # 9. sequence
    s = d.slide()
    d.header(s, "Registration Sequence", "How objects collaborate to accomplish the task")
    d.pic(s, "w12_sequence.png", y=1.6, w=10.6)
    d.takeaway(s, "If the sequence uses a class, that class must exist in the class model.")

    # 10. state machine
    s = d.slide()
    d.header(s, "Registration State Model", "How a registration changes state")
    d.pic(s, "w12_state_machine.png", y=1.6, w=10.6)
    d.takeaway(s, "The state model makes business rules explicit (e.g. can CANCELLED become CONFIRMED?).")

    # 11. activity
    s = d.slide()
    d.header(s, "Registration Activity", "What activities and decisions occur in the workflow?")
    d.pic(s, "w12_activity.png", y=1.5, w=10.4)
    d.takeaway(s, "Activity = the workflow; sequence = who talks to whom.")

    # 12. views compare
    s = d.slide()
    d.header(s, "Comparing the Behavioural Views", "Know which model answers which question")
    d.pic(s, "w12_views_compare.png", y=1.6, w=10.6)
    d.takeaway(s, "Use case = what · sequence = how over time · activity = workflow · state = object lifecycle.")

    # 13. multiplicity
    s = d.slide()
    d.header(s, "Multiplicity", "Precise numbers on each side of a relationship")
    d.pic(s, "w12_multiplicity.png", y=1.6, w=10.6)
    d.takeaway(s, "Student 1 — 0..* Registration — Course gives precise information.")

    # 14. packages
    s = d.slide()
    d.header(s, "Packages", "Organising a large model into related groups")
    d.pic(s, "w12_packages.png", y=1.5, w=10.6)
    d.takeaway(s, "Authentication · Academic · Finance · Library · Notification.")

    # 15. architecture
    s = d.slide()
    d.header(s, "Architectural Integration", "Organising classes into a layered system")
    d.pic(s, "w12_architecture.png", y=1.5, w=10.4)
    d.takeaway(s, "Layers give responsibilities clearer boundaries.")

    # 16. components
    s = d.slide()
    d.header(s, "Component Thinking", "Meaningful, replaceable, understandable parts")
    d.pic(s, "w12_components.png", y=1.6, w=10.6)
    d.takeaway(s, "Beyond classes: how is the software divided into components?")

    # 17. validation
    s = d.slide()
    d.header(s, "Design Validation", "Does the design represent what the system must do?")
    d.pic(s, "w12_validation.png", y=1.6, w=10.6)
    d.takeaway(s, "A sequence with no checkCapacity() fails the \u201cfull course\u201d requirement.")

    # 18. integrated example
    s = d.slide()
    d.header(s, "The Complete Integrated Example", "Requirement R01 through every model")
    d.pic(s, "w12_integrated_example.png", y=1.5, w=10.6)
    d.takeaway(s, "Use case · classes · sequence · activity · state · architecture.")

    # 19. model vs diagram
    s = d.slide()
    d.header(s, "Model vs Diagram", "The Google Maps analogy")
    d.pic(s, "w12_model_vs_diagram.png", y=1.6, w=10.6)
    d.takeaway(s, "A diagram is a visual representation; a model is the underlying structure.")

    # 20. design review questions
    s = d.slide()
    d.header(s, "Design Review", "Questions a design team should ask")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Requirement coverage? ", "every important requirement represented."),
        ("Use-case coverage? ", "every major use case has supporting design elements."),
        ("Class / interaction / state coverage? ", "the required data and behaviour exist."),
        ("Architecture? ", "responsibilities divided appropriately."),
        ("Coupling / cohesion? ", "no unnecessary dependencies; each part has a focus."),
        ("Reuse / maintainability? ", "components reusable; change is manageable."),
    ], size=16, gap=13)
    d.takeaway(s, "Run this review before implementation.")

    # 21. confusions
    s = d.slide()
    d.header(s, "Common Confusions", "Don't mix these up")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Use case vs sequence: ", "what the user wants vs how objects communicate."),
        ("Activity vs state: ", "activities in a process vs states of one object."),
        ("Class vs object diagram: ", "blueprint (Student) vs instance (student:Student)."),
    ], size=17, gap=14)
    d.takeaway(s, "Class = blueprint · object = actual thing created from the blueprint.")

    # 22. summary
    s = d.slide()
    d.header(s, "Week 12 Summary", "The central principle")
    d.pic(s, "w12_summary_flow.png", y=1.5, w=10.4)
    d.takeaway(s, "Tell the same system's story through different models — and make them agree.")

    # 23. closing
    d.closing("REVISION & NEXT STEPS", [
        "Build a full integrated model for \u201cpatient books an appointment\u201d (use case -> class -> sequence -> activity -> state).",
        "Audit one use case for missing links (requirement -> class -> operation -> test).",
        "Explain model vs diagram using the Google Maps analogy.",
        "Next week: multilayer architecture, reusable/adaptable components, and architectural design.",
    ])


def build_pptx():
    return build(CFG, slides)


if __name__ == "__main__":
    print("Built:", build_pptx())
