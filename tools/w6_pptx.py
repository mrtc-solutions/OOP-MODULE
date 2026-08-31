"""
Week 6 PPTX content — OBJECT-ORIENTED ANALYSIS: OBJECT MODELLING II.
"""
from pptxengine import build

CFG = {
    "week": 6,
    "title": "Object-Oriented Analysis — Object Modelling II",
    "filename": "Week6_Presentation_BICT3202_OOAD.pptx",
}


def slides(d):
    # 2. learning outcomes
    s = d.slide()
    d.header(s, "Learning Outcomes", "By the end of this week, you should be able to…")
    d.bullets(s, 0.9, 1.6, 11.6, 5.0, [
        ("Define ", "aggregation and explain whole-part relationships."),
        ("Distinguish ", "ordinary association, aggregation and composition."),
        ("Explain ", "inheritance and its link to UML generalization."),
        ("Distinguish ", "is-a (inheritance) from has-a (aggregation)."),
        ("Explain ", "polymorphism and method overriding with examples."),
        ("Explain ", "why polymorphism supports extensibility."),
        ("Group ", "related classes into packages."),
        ("Evaluate ", "whether aggregation, inheritance or polymorphism fits a problem."),
    ], size=17, gap=12)
    d.takeaway(s, "Week 6 makes the object model reusable, extensible and organised.")

    # 3. progression
    s = d.slide()
    d.header(s, "Where Week 6 Fits", "Building on Week 5")
    d.pic(s, "w6_progression.png", y=1.6, w=10.6)
    d.takeaway(s, "Week 5 = what exists & how related · Week 6 = whole-part, inheritance, polymorphism, grouping.")

    # 4. aggregation intro
    s = d.slide()
    d.header(s, "Aggregation — Whole-Part", "One object represents a whole; others are its parts")
    d.pic(s, "w6_whole_part.png", y=1.6, w=10.6)
    d.takeaway(s, "University <>-- Department · Library <>-- Book · the hollow diamond sits on the whole.")

    # 5. agg vs assoc
    s = d.slide()
    d.header(s, "Aggregation vs Association", "A general relationship vs whole-part")
    d.pic(s, "w6_agg_vs_assoc.png", y=1.6, w=10.4)
    d.takeaway(s, "Association = related-to · Aggregation = has/contains (whole-part).")

    # 6. agg vs composition
    s = d.slide()
    d.header(s, "Aggregation vs Composition", "Hollow diamond vs filled diamond")
    d.pic(s, "w6_agg_vs_comp.png", y=1.6, w=10.6)
    d.takeaway(s, "Hollow = parts can exist independently · Filled = the composite owns its parts.")

    # 7. football
    s = d.slide()
    d.header(s, "Weak Aggregation", "The parts can outlive the whole")
    d.pic(s, "w6_football.png", y=1.6, w=10.6)
    d.takeaway(s, "Aggregation does NOT mean \u201cthe part dies when the whole dies\u201d — that's composition.")

    # 8. agg multiplicity
    s = d.slide()
    d.header(s, "Aggregation with Multiplicity", "Whole-part relationships still use multiplicity")
    d.pic(s, "w6_agg_multiplicity.png", y=1.6, w=10.4)
    d.takeaway(s, "University 1 <>-- 1..* Department · Department 1 <>-- 0..* Lecturer.")

    # 9. inheritance
    s = d.slide()
    d.header(s, "Inheritance", "A specific class acquires features from a general class")
    d.pic(s, "w6_inheritance.png", y=1.6, w=10.6)
    d.takeaway(s, "A Car inherits Vehicle's features — drawn as UML generalization.")

    # 10. gen vs inheritance
    s = d.slide()
    d.header(s, "Generalization vs Inheritance", "Same idea, different vocabulary")
    d.pic(s, "w6_gen_vs_inheritance.png", y=1.6, w=10.4)
    d.takeaway(s, "UML says generalization · OOP says inheritance — one implements the other.")

    # 11. what inherited
    s = d.slide()
    d.header(s, "What Does the Child Inherit?", "No duplication of common features")
    d.pic(s, "w6_what_inherited.png", y=1.6, w=10.6)
    d.takeaway(s, "Manager gains employeeID, name, email, login(), logout() from Employee — automatically.")

    # 12. animal
    s = d.slide()
    d.header(s, "An Inheritance Hierarchy", "Animal → Dog, Cat, Bird")
    d.pic(s, "w6_animal.png", y=1.6, w=10.6)
    d.takeaway(s, "Each subclass adds its own behaviour — bark(), meow(), fly().")

    # 13. is-a vs has-a
    s = d.slide()
    d.header(s, "IS-A vs HAS-A", "A classic exam question")
    d.pic(s, "w6_isa_hasa.png", y=1.6, w=10.4)
    d.takeaway(s, "Car -> Vehicle (is-a) = inheritance · Car <>-- Engine (has-a) = aggregation.")

    # 14. polymorphism
    s = d.slide()
    d.header(s, "Polymorphism — \u201cMany Forms\u201d", "The same request, different behaviour")
    d.pic(s, "w6_polymorphism.png", y=1.6, w=10.6)
    d.takeaway(s, "makeSound() → bark / meow / moo — the object decides how to respond.")

    # 15. payment polymorphism
    s = d.slide()
    d.header(s, "Polymorphism in Practice — Payments", "One processPayment(), several implementations")
    d.pic(s, "w6_payment_polymorphism.png", y=1.6, w=10.6)
    d.takeaway(s, "The system requests processPayment() without treating each payment type as unrelated.")

    # 16. notification
    s = d.slide()
    d.header(s, "A Modern Example — Notifications", "Email, SMS and Push all implement send()")
    d.pic(s, "w6_notification.png", y=1.6, w=10.6)
    d.takeaway(s, "Add WhatsAppNotification later — the code that requests send() stays unchanged.")

    # 17. overriding
    s = d.slide()
    d.header(s, "Method Overriding", "The programming mechanism behind polymorphism")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("The general class defines ", "makeSound()."),
        ("Each subclass provides ", "a specialised version that overrides the inherited operation."),
        ("Java: ", "Animal a = new Dog();  a.makeSound();  →  Bark"),
        ("      ", "a = new Cat();  a.makeSound();  →  Meow"),
        ("",""),
        ("In OOAD, ", "model the idea first — leave programming syntax for design."),
    ], size=17, gap=14)
    d.takeaway(s, "The variable is typed Animal, but the actual object decides the behaviour.")

    # 18. grouping
    s = d.slide()
    d.header(s, "Grouping — Packages", "Organise classes the way folders organise files")
    d.pic(s, "w6_grouping.png", y=1.6, w=10.6)
    d.takeaway(s, "60 classes in one diagram is confusing — packages restore readability and modularity.")

    # 19. online shopping
    s = d.slide()
    d.header(s, "Complete Example — Online Shopping", "All four concepts together")
    d.pic(s, "w6_online_shopping.png", y=1.6, w=10.6)
    d.takeaway(s, "Composition (Order ◆ OrderItem) + inheritance (Payment) + polymorphism + grouping.")

    # 20. university example
    s = d.slide()
    d.header(s, "Complete Example — University System", "Building a larger model")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Inheritance: ", "User ▷ Student · User ▷ Lecturer."),
        ("Aggregation: ", "Department <>-- Lecturer."),
        ("Association: ", "Student — Registration — Course."),
        ("Composition: ", "Course ◆-- CourseMaterial (strongly owned parts)."),
        ("Polymorphism: ", "Assessment.calculateMark() → Assignment, Exam, Quiz, Project."),
    ], size=17, gap=14)
    d.takeaway(s, "Choose the relationship that best represents the requirements — not every possible symbol.")

    # 21. evaluating a model
    s = d.slide()
    d.header(s, "Evaluating a Model", "Ask before you submit")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Whole-part? ", "is the aggregation really whole-part, or just an association?"),
        ("Independent or owned? ", "do the parts outlive the whole (aggregation) or not (composition)?"),
        ("Genuine is-a? ", "is every generalization a real is-a relationship?"),
        ("Common meaning? ", "does the polymorphic operation mean the same across subclasses?"),
        ("Readable? ", "is the model organised into sensible packages?"),
    ], size=16, gap=13)
    d.takeaway(s, "The goal is a model that best represents the requirements — not one that uses every symbol.")

    # 22. summary
    s = d.slide()
    d.header(s, "Week 6 Summary", "The essentials")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Aggregation ", "— whole-part, hollow diamond, parts independent."),
        ("Composition ", "— strong whole-part, filled diamond, composite owns parts."),
        ("Inheritance ", "— is-a; UML generalization implemented in code."),
        ("Polymorphism ", "— one operation name, different behaviour; supports extensibility."),
        ("Grouping ", "— packages organise related classes."),
    ], size=17, gap=14)
    d.takeaway(s, "These four ideas make the object model reusable, extensible and understandable.")

    # 23. closing
    d.closing("REVISION & NEXT STEPS", [
        "Draw Department <>-- Lecturer and Order ◆-- OrderLine — justify each choice.",
        "Model the Payment hierarchy with processPayment(), then add a new payment type without breaking the design.",
        "Organise the university system into packages using your CASE tool.",
        "Next week: Dynamic Modelling — events, states, operations and concurrency.",
    ])


def build_pptx():
    return build(CFG, slides)


if __name__ == "__main__":
    print("Built:", build_pptx())
