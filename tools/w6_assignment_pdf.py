"""
Week 6 Assignment PDF content — OBJECT-ORIENTED ANALYSIS: OBJECT MODELLING II.
"""
from pdfengine import (H1, H2, P, BUL, build, DOC_W, DTABLE)

CFG = {
    "week": 6,
    "title": "Assignment: Object-Oriented Analysis — Object Modelling II",
    "filename": "Week6_Assignment_BICT3202_OOAD.pdf",
}


def story():
    s = []

    s.append(H1("ASSIGNMENT INSTRUCTIONS"))
    s += BUL([
        "Answer ALL questions in Sections A, B and C.",
        "Read the Week 6 module and your lecture notes before attempting each question.",
        "Draw diagrams neatly (by hand or using a UML/CASE tool) with correct UML notation.",
        "Use a hollow diamond for aggregation and a filled diamond for composition.",
        "Justify every modelling decision — marks are awarded for reasoning, not only notation.",
        "Submit by the date given by your lecturer. Total: 50 marks.",
    ])

    s.append(H1("Section A — Short-Answer Questions (20 marks)"))
    questions_a = [
        ("Define aggregation and explain the whole-part relationship.", "2"),
        ("Differentiate between ordinary association and aggregation, with an example of each.", "3"),
        ("Differentiate between aggregation and composition, with an example of each.", "3"),
        ("What is inheritance? How does it relate to UML generalization?", "2"),
        ("What features does a subclass inherit from its superclass? Give an example.", "2"),
        ("Differentiate between inheritance (is-a) and aggregation (has-a).", "2"),
        ("Define polymorphism and give one real-world example.", "2"),
        ("Explain method overriding and how it relates to polymorphism.", "2"),
        ("Why does polymorphism support extensibility in a software system?", "2"),
    ]
    for i, (q, m) in enumerate(questions_a, 1):
        s.append(H2(f"Question A{i}"))
        s.append(P(f"{q} [{m} marks]"))

    s.append(H1("Section B — Application Questions (20 marks)"))
    s.append(H2("Question B1 (12 marks)"))
    s.append(P("'A university has departments and lecturers. Each department has many lecturers, and a "
                "lecturer belongs to one department. A lecturer can move to another department. A course is "
                "made up of course materials such as slides, notes and assessments, which belong to that "
                "course alone.'",
                style="bodyL"))
    s += BUL([
        "(a) Model Department and Lecturer, and explain whether aggregation or association is appropriate. [3 marks]",
        "(b) Model Course and CourseMaterial, and explain whether aggregation or composition is appropriate. [3 marks]",
        "(c) Add multiplicities to both relationships. [2 marks]",
        "(d) Draw both relationships using correct UML notation (diamonds). [4 marks]",
    ])
    s.append(H2("Question B2 (8 marks)"))
    s.append(P("Consider the hierarchy Animal -> Dog, Cat and Bird, where each animal makes a sound."))
    s += BUL([
        "(a) Draw the class hierarchy using generalization. [2 marks]",
        "(b) Explain how polymorphism applies to the operation makeSound(). [2 marks]",
        "(c) Explain how method overriding is used to give each animal its own sound. [2 marks]",
        "(d) Explain what happens if a new class, Lion, is added to the hierarchy. [2 marks]",
    ])

    s.append(H1("Section C — Case Study (10 marks)"))
    s.append(P("'An online store has customers, orders, order items and products. Payments can be made "
                "by card, mobile money or bank transfer. Each order contains one or more order items. The "
                "system is organised into customer, order, product and payment management areas.'",
                style="bodyL"))
    s.append(P("As an object-oriented analyst:"))
    s += BUL([
        "(a) Identify the candidate classes, including a Payment hierarchy. [3 marks]",
        "(b) Model Order and OrderItem and justify aggregation or composition. [3 marks]",
        "(c) Explain how polymorphism applies to processPayment() and why it supports extensibility. [2 marks]",
        "(d) Propose a package structure (grouping) for the system. [2 marks]",
    ])

    s.append(H1("Marking Scheme"))
    s.append(DTABLE(
        ["Section", "Content", "Marks"],
        [["A", "Short-answer questions (9 questions)", "20"],
         ["B", "Application questions (12 + 8)", "20"],
         ["C", "Case study — online store", "10"],
         ["", "TOTAL", "50"]],
        widths=[0.25 * DOC_W, 0.55 * DOC_W, 0.20 * DOC_W]))

    s.append(H1("Submission & Academic Integrity"))
    s += BUL([
        "Submit a typed document (or neatly handwritten, as directed by your lecturer).",
        "This assignment is individual work. Plagiarism or copying will attract a penalty under university regulations.",
        "Diagrams must use correct UML notation — hollow diamond for aggregation, filled diamond for composition.",
        "Cite any sources you consult using the format used in the Week 6 module references.",
    ])

    return s


if __name__ == "__main__":
    print("Built:", build(CFG, story))
