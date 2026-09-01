"""
Week 14 PPTX content — INTEGRATING OBJECT, DYNAMIC AND BEHAVIOURAL MODELS INTO OOD.
"""
from pptxengine import build

CFG = {
    "week": 14,
    "title": "Integrating Object, Dynamic and Behavioural Models into Object-Oriented Design",
    "filename": "Week14_Presentation_BICT3202_OOAD.pptx",
}


def slides(d):
    # 2. learning outcomes
    s = d.slide()
    d.header(s, "Learning Outcomes", "By the end of this week, you should be able to…")
    d.bullets(s, 0.9, 1.6, 11.6, 5.0, [
        ("Define ", "OOD and explain analysis vs design."),
        ("Explain ", "why analysis models must become design models."),
        ("Explain ", "design classes, responsibilities, attributes and operations."),
        ("Integrate ", "the object model with the dynamic and behavioural models."),
        ("Trace ", "a requirement from a use case to classes and operations."),
        ("Use ", "sequence, state and activity diagrams to refine class responsibilities."),
        ("Identify ", "design inconsistencies and refine an analysis model."),
    ], size=16, gap=11)
    d.takeaway(s, "Each diagram is a different view of the SAME system.")

    # 3. progression
    s = d.slide()
    d.header(s, "Week 13 -> Week 14", "From architecture to the contents of the components")
    d.pic(s, "w14_progression.png", y=1.6, w=10.6)
    d.takeaway(s, "Week 14 combines all the models into one coherent software design.")

    # 4. analysis vs design
    s = d.slide()
    d.header(s, "Analysis vs Design", "What the system needs vs how the software provides it")
    d.pic(s, "w14_analysis_vs_design.png", y=1.6, w=10.6)
    d.takeaway(s, "Analysis = Student/Course/Registration · Design = Controller/Service/Repository/Validator.")

    # 5. transformation
    s = d.slide()
    d.header(s, "Analysis Model -> Design Model", "Design classes must be justified")
    d.pic(s, "w14_transformation.png", y=1.5, w=10.4)
    d.takeaway(s, "Requirements -> use cases -> analysis -> design decisions -> design -> implementation.")

    # 6. three models
    s = d.slide()
    d.header(s, "The Three Major Models", "Each answers a different question")
    d.pic(s, "w14_three_models.png", y=1.6, w=10.6)
    d.takeaway(s, "Object = what exists · Dynamic = what changes · Behavioural = what happens.")

    # 7. multiple views
    s = d.slide()
    d.header(s, "One System, Multiple Views", "Six views — not six systems")
    d.pic(s, "w14_multiple_views.png", y=1.6, w=10.6)
    d.takeaway(s, "Use case · class · sequence · activity · state · component.")

    # 8. use case flow
    s = d.slide()
    d.header(s, "From Use Case to Design", "Basic flow and candidate classes")
    d.pic(s, "w14_use_case_flow.png", y=1.5, w=10.6)
    d.takeaway(s, "Which objects should perform these responsibilities?")

    # 9. responsibility
    s = d.slide()
    d.header(s, "Responsibility Assignment", "A class KNOWS things and DOES things")
    d.pic(s, "w14_responsibility.png", y=1.6, w=10.6)
    d.takeaway(s, "Assign each responsibility to the object with the information to perform it.")

    # 10. design class
    s = d.slide()
    d.header(s, "Analysis Class -> Design Class", "Precise attributes, types, visibility, operations")
    d.pic(s, "w14_design_class.png", y=1.6, w=10.6)
    d.takeaway(s, "The design class is much more precise.")

    # 11. visibility
    s = d.slide()
    d.header(s, "Visibility", "UML visibility symbols")
    d.pic(s, "w14_visibility.png", y=1.6, w=10.6)
    d.takeaway(s, "+ public · - private · # protected · ~ package.")

    # 12. attributes & operations
    s = d.slide()
    d.header(s, "Attributes & Operations", "Know vs do")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Attributes = ", "what an object knows (studentId, name, email, balance)."),
        ("Operations = ", "what an object can do (register(), withdraw(), getBalance())."),
        ("Example: ", "BankAccount -accountNumber, -balance; +deposit(), +withdraw(), +getBalance()."),
    ], size=17, gap=14)
    d.takeaway(s, "Attributes store information; operations perform actions.")

    # 13. sequence -> class
    s = d.slide()
    d.header(s, "Sequence Diagram -> Class Design", "Messages reveal operations")
    d.pic(s, "w14_sequence_to_class.png", y=1.6, w=10.6)
    d.takeaway(s, "Course -> checkCapacity() means Course needs checkCapacity().")

    # 14. consistency
    s = d.slide()
    d.header(s, "Model Consistency", "The diagrams must agree")
    d.pic(s, "w14_consistency.png", y=1.6, w=10.6)
    d.takeaway(s, "checkCapacity() vs verifyCapacity() — resolve the discrepancy.")

    # 15. object + dynamic
    s = d.slide()
    d.header(s, "Object Model + Dynamic Model", "Operations relate to state changes")
    d.pic(s, "w14_object_dynamic.png", y=1.6, w=10.6)
    d.takeaway(s, "registerStudent() causes Available -> Full at the final seat.")

    # 16. activity mapping
    s = d.slide()
    d.header(s, "Object Model + Activity Model", "Map activities to responsible classes")
    d.pic(s, "w14_activity_mapping.png", y=1.6, w=10.6)
    d.takeaway(s, "This turns a behavioural model into design responsibilities.")

    # 17. controller
    s = d.slide()
    d.header(s, "The Controller", "Coordinates — does not do everything")
    d.pic(s, "w14_controller.png", y=1.6, w=10.6)
    d.takeaway(s, "Avoid the God class: the controller delegates to the service.")

    # 18. domain knowledge
    s = d.slide()
    d.header(s, "Domain Objects Own Domain Knowledge", "Course knows if it is available")
    d.pic(s, "w14_domain_knowledge.png", y=1.6, w=10.6)
    d.takeaway(s, "Course.isAvailable() / hasCapacity() instead of rules in every UI.")

    # 19. design for change
    s = d.slide()
    d.header(s, "Designing for Change", "Boundaries around what is likely to change")
    d.pic(s, "w14_design_change.png", y=1.6, w=10.6)
    d.takeaway(s, "RegistrationService -> PaymentGateway, not -> AirtelMoneyAPI.")

    # 20. strategy pattern
    s = d.slide()
    d.header(s, "Design Patterns (outline): Strategy", "One abstraction, many implementations")
    d.pic(s, "w14_strategy.png", y=1.6, w=10.6)
    d.takeaway(s, "Use patterns only when they solve an actual recurring problem.")

    # 21. integrated design
    s = d.slide()
    d.header(s, "The Integrated Design Model", "Controller -> Service -> Domain -> Repository")
    d.pic(s, "w14_integrated_design.png", y=1.5, w=10.4)
    d.takeaway(s, "That is what it means to integrate the models.")

    # 22. validation
    s = d.slide()
    d.header(s, "Model Validation", "Eight questions to check your models")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Does every use case ", "have supporting classes?"),
        ("Does every sequence message ", "correspond to an operation?"),
        ("Do operations ", "belong to sensible classes?"),
        ("Do state changes ", "correspond to actual events/operations?"),
        ("Do activity flows ", "agree with the use case? Any duplicated responsibilities or God classes?"),
    ], size=16, gap=13)
    d.takeaway(s, "If \u201cdrop courses\u201d has no drop operation, introduce RegistrationService.dropCourse().")

    # 23. mistakes
    s = d.slide()
    d.header(s, "Common Mistakes", "Avoid these")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Treating diagrams as independent ", "— the sequence explains how classes cooperate."),
        ("One class does everything ", "— poor responsibility assignment."),
        ("Confusing analysis and design ", "— what is needed vs how it is implemented."),
        ("Classes without justification ", "— every design class needs a reason."),
        ("Ignoring consistency ", "— register() vs enrolStudent() must be reconciled."),
    ], size=15, gap=11)
    d.takeaway(s, "Five classic traps in examination answers.")

    # 24. summary
    s = d.slide()
    d.header(s, "Week 14 Summary", "The most important concept")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("1. ", "Requirement -> use case -> scenario -> sequence -> classes -> responsibilities -> design -> implementation."),
        ("2. ", "Class model <- dynamic model <- behavioural model."),
        ("3. ", "The models must support one another, not contradict one another."),
    ], size=17, gap=14)
    d.takeaway(s, "That is the central lesson of Week 14.")

    # 25. closing
    d.closing("REVISION & NEXT STEPS", [
        "Refine Student/Course/Registration into full design classes with visibility and signatures.",
        "Draw the sequence and state models for \u201cRegister for Course\u201d and cross-check them.",
        "Map each registration activity to a responsible class.",
        "Next week: complete OOAD case study, model integration and CASE-tool implementation.",
    ])


def build_pptx():
    return build(CFG, slides)


if __name__ == "__main__":
    print("Built:", build_pptx())
