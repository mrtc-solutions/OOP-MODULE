"""
Week 9 PPTX content — THE UNIFIED SOFTWARE DEVELOPMENT PROCESS (USDP / UP).
"""
from pptxengine import build

CFG = {
    "week": 9,
    "title": "The Unified Software Development Process (USDP / Unified Process)",
    "filename": "Week9_Presentation_BICT3202_OOAD.pptx",
}


def slides(d):
    # 2. learning outcomes
    s = d.slide()
    d.header(s, "Learning Outcomes", "By the end of this week, you should be able to…")
    d.bullets(s, 0.9, 1.6, 11.6, 5.0, [
        ("Define ", "the Unified Process and explain why it suits OO development."),
        ("Explain ", "iterative vs incremental development."),
        ("Explain ", "the four characteristics (use-case driven, architecture-centred, iterative & incremental, risk-driven)."),
        ("Distinguish ", "phase vs iteration; explain the four phases and milestones."),
        ("Explain ", "process workflows, artefacts and reuse guidelines."),
        ("Explain ", "concurrency, generalisation and inheritance."),
        ("Connect ", "UP to the UML models already studied."),
    ], size=16, gap=11)
    d.takeaway(s, "UML = how to model · UP = how to organise the work.")

    # 3. progression
    s = d.slide()
    d.header(s, "Where Week 9 Fits", "From modelling the system to organising the work")
    d.pic(s, "w9_progression.png", y=1.6, w=10.6)
    d.takeaway(s, "UP is an iterative and incremental process for OO development using UML.")

    # 4. why process
    s = d.slide()
    d.header(s, "Why Software Needs a Process", "Without it, everyone builds something different")
    d.pic(s, "w9_why_process.png", y=1.6, w=10.6)
    d.takeaway(s, "A process tells the team WHAT work, WHEN, WHO does it, and WHAT to produce.")

    # 5. UP vs RUP
    s = d.slide()
    d.header(s, "UP vs RUP", "A general framework vs a specific implementation")
    d.pic(s, "w9_up_vs_rup.png", y=1.6, w=10.4)
    d.takeaway(s, "UP = general framework · RUP = Rational's commercial implementation of UP.")

    # 6. waterfall vs UP
    s = d.slide()
    d.header(s, "Waterfall vs UP", "Separate stages vs repeated cycles")
    d.pic(s, "w9_waterfall_vs_up.png", y=1.6, w=10.6)
    d.takeaway(s, "UP repeats the cycle — each iteration improves the system.")

    # 7. iterative vs incremental
    s = d.slide()
    d.header(s, "Iterative vs Incremental", "Refine and improve vs add functionality")
    d.pic(s, "w9_iterative_incremental.png", y=1.6, w=10.6)
    d.takeaway(s, "UP is BOTH iterative AND incremental — short, timeboxed iterations.")

    # 8. increments
    s = d.slide()
    d.header(s, "Incremental Growth", "Each increment adds usable capability")
    d.pic(s, "w9_increments.png", y=1.6, w=10.6)
    d.takeaway(s, "Login -> + registration -> + assignment -> + results.")

    # 9. characteristics
    s = d.slide()
    d.header(s, "Four Characteristics of UP", "Use-case driven · architecture-centred · iterative & incremental · risk-driven")
    d.pic(s, "w9_characteristics.png", y=1.6, w=10.6)
    d.takeaway(s, "Remember these four — they are a favourite examination question.")

    # 10. use-case driven
    s = d.slide()
    d.header(s, "Use-Case Driven", "A use case threads through the whole lifecycle")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("UC-01 Register Course ", "drives the work:"),
        ("Requirements: ", "what should registration do?"),
        ("Analysis: ", "Student · Course · Registration"),
        ("Design: ", "RegistrationController · CourseService"),
        ("Implementation: ", "program the functionality"),
        ("Testing: ", "available · full · prerequisite missing · already registered"),
    ], size=17, gap=12)
    d.takeaway(s, "The use case becomes a thread running through every activity.")

    # 11. architecture
    s = d.slide()
    d.header(s, "Architecture-Centred", "Validate the high-level design early")
    d.pic(s, "w9_architecture.png", y=1.6, w=10.4)
    d.takeaway(s, "A system for 100 students may collapse with 100,000 — test the architecture early.")

    # 12. risk-driven
    s = d.slide()
    d.header(s, "Risk-Driven", "Address significant risks early")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Common mistake: ", "\u201cLet's build the easiest things first.\u201d"),
        ("UP instead ", "identifies and addresses significant risks early."),
        ("Risk types: ", "technical · security · performance · financial · schedule · requirements · integration."),
        ("Example: ", "\u201c5,000 transactions per second\u201d — test the architecture in an early iteration."),
    ], size=17, gap=14)
    d.takeaway(s, "Attack the riskiest parts while there is still time to mitigate them.")

    # 13. phases
    s = d.slide()
    d.header(s, "The Four UP Phases", "Inception -> Elaboration -> Construction -> Transition")
    d.pic(s, "w9_phases.png", y=1.6, w=10.6)
    d.takeaway(s, "A phase is NOT a waterfall stage — each phase contains iterations.")

    # 14. phase questions
    s = d.slide()
    d.header(s, "The Four Phases Compared", "Each has its own question and focus")
    d.pic(s, "w9_phase_questions.png", y=1.6, w=10.6)
    d.takeaway(s, "Inception = scope · Elaboration = architecture · Construction = build · Transition = deploy.")

    # 15. phases contain iterations
    s = d.slide()
    d.header(s, "Phases Contain Iterations", "What makes UP different from waterfall")
    d.pic(s, "w9_phases_iterations.png", y=1.6, w=10.6)
    d.takeaway(s, "Iterations deliver incremental value within each phase.")

    # 16. milestones
    s = d.slide()
    d.header(s, "Milestones", "Go / no-go decision points")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("End of Inception: ", "Lifecycle Objectives Milestone — \u201cdo we understand enough to continue?\u201d"),
        ("End of Elaboration: ", "Lifecycle Architecture Milestone — \u201ccan the architecture support the requirements?\u201d"),
        ("End of Construction: ", "Initial Operational Capability — the system is ready for users."),
        ("End of Transition: ", "Product Release — the system is in production."),
    ], size=17, gap=14)
    d.takeaway(s, "If major risks remain unresolved, the project should not blindly continue.")

    # 17. workflows
    s = d.slide()
    d.header(s, "Process Workflows / Disciplines", "Core technical + supporting disciplines")
    d.pic(s, "w9_workflows.png", y=1.6, w=10.6)
    d.takeaway(s, "Business Modeling · Requirements · Analysis & Design · Implementation · Test · Deployment + 3 supporting.")

    # 18. workflow intensity
    s = d.slide()
    d.header(s, "Workflow Intensity Across Phases", "Disciplines overlap — they do not happen once")
    d.pic(s, "w9_workflow_intensity.png", y=1.6, w=10.6)
    d.takeaway(s, "Coding is heavy in Construction, but prototypes appear in Elaboration too.")

    # 19. artefacts
    s = d.slide()
    d.header(s, "Artefacts", "Work products across the phases")
    d.pic(s, "w9_artefacts.png", y=1.6, w=10.6)
    d.takeaway(s, "An artefact is evidence of the team's work — the use-case model, code, tests…")

    # 20. reuse
    s = d.slide()
    d.header(s, "Reuse in OO Development", "Use existing assets — but evaluate")
    d.pic(s, "w9_reuse.png", y=1.6, w=10.6)
    d.takeaway(s, "Reuse is not automatically good — check security, compatibility, licence, quality.")

    # 21. generalisation vs inheritance
    s = d.slide()
    d.header(s, "Generalisation vs Inheritance", "Closely related, not identical")
    d.pic(s, "w9_gen_vs_inheritance.png", y=1.6, w=10.4)
    d.takeaway(s, "Generalisation = modelling relationship · Inheritance = programming mechanism.")

    # 22. concurrency
    s = d.slide()
    d.header(s, "Concurrency — a Real Problem", "Two students, one remaining seat")
    d.pic(s, "w9_concurrency.png", y=1.6, w=10.6)
    d.takeaway(s, "Without synchronisation, two registrations succeed for one seat — concurrency matters.")

    # 23. connecting UP to UML
    s = d.slide()
    d.header(s, "Connecting UP to the UML Models", "The models become artefacts in the process")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Requirement -> ", "use case -> use-case diagram -> activity -> sequence -> class model -> design -> implementation."),
        ("",""),
        ("UP provides ", "the development process; UML provides the modelling languages used within it."),
        ("Case study: ", "Mzuni Online Registration — Inception, Elaboration, Construction, Transition."),
    ], size=16, gap=13)
    d.takeaway(s, "The models of Weeks 4–8 do not exist in isolation — they are UP artefacts.")

    # 24. misunderstandings
    s = d.slide()
    d.header(s, "Common Misunderstandings", "Avoid these")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("\u201cUP is the same as Waterfall\u201d ", "— no: phases contain iterations."),
        ("\u201cInception collects every requirement\u201d ", "— no: scope + major requirements only."),
        ("\u201cCoding only happens in Construction\u201d ", "— prototypes are coded in Elaboration."),
        ("\u201cTesting starts after coding\u201d ", "— testing happens every iteration."),
        ("\u201cGeneralisation = inheritance\u201d ", "— closely related, but one is a relationship, the other a mechanism."),
    ], size=15, gap=11)
    d.takeaway(s, "These five are classic traps in examination answers.")

    # 25. summary
    s = d.slide()
    d.header(s, "Week 9 Summary", "Five things to remember")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("1. ", "UP is iterative and incremental."),
        ("2. ", "UP is use-case driven."),
        ("3. ", "UP is architecture-centred."),
        ("4. ", "UP has four phases — Inception, Elaboration, Construction, Transition."),
        ("5. ", "Phases contain iterations — that is what makes UP different from waterfall."),
    ], size=17, gap=14)
    d.takeaway(s, "Week 8 = what the system does · Week 9 = how to organise the work · Week 10+ = design.")

    # 26. closing
    d.closing("REVISION & NEXT STEPS", [
        "Explain iterative vs incremental with a concrete example, then draw the four phases with iterations.",
        "Compare UP against waterfall — list what changes for requirements, risk, delivery and documentation.",
        "Map the Week 8 models onto UP phases and artefacts for the registration system.",
        "Next week: Object-Oriented Design — turning the analysis into a software design.",
    ])


def build_pptx():
    return build(CFG, slides)


if __name__ == "__main__":
    print("Built:", build_pptx())
