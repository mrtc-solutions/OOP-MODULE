"""
Week 12 Assignment PDF content — INTEGRATED OBJECT-ORIENTED MODELLING AND DESIGN.
"""
from pdfengine import (H1, H2, P, BUL, build, DOC_W, DTABLE)

CFG = {
    "week": 12,
    "title": "Assignment: Integrated Object-Oriented Modelling and Design",
    "filename": "Week12_Assignment_BICT3202_OOAD.pdf",
}


def story():
    s = []

    s.append(H1("ASSIGNMENT INSTRUCTIONS"))
    s += BUL([
        "Answer ALL questions in Sections A, B and C.",
        "Read the Week 12 module and your lecture notes before attempting each question.",
        "Where you draw UML diagrams, use correct notation — actors, multiplicities, states, messages.",
        "Show how your models are consistent: every class in a sequence diagram must exist in the class model.",
        "Cite the OMG UML 2.5.1 specification where relevant.",
        "Submit by the date given by your lecturer. Total: 50 marks.",
    ])

    s.append(H1("Section A — Short-Answer Questions (20 marks)"))
    questions_a = [
        ("Define integrated object-oriented modelling.", "2"),
        ("Explain why the different UML models of a system must be consistent.", "3"),
        ("State the main question answered by each of the use-case, class, sequence, activity and state models.", "3"),
        ("Define model consistency and give one example.", "2"),
        ("Explain traceability and why it is valuable in integrated modelling.", "2"),
        ("What is a design pattern and how does it support reuse?", "2"),
        ("Differentiate between a class diagram and an object diagram.", "2"),
        ("Explain how sequence diagrams and class diagrams complement each other.", "2"),
    ]
    for i, (q, m) in enumerate(questions_a, 1):
        s.append(H2(f"Question A{i}"))
        s.append(P(f"{q} [{m} marks]"))

    s.append(H1("Section B — Application Questions (20 marks)"))
    s.append(H2("Question B1 (12 marks)"))
    s.append(P("Consider a simplified student registration system with Student, Course and Registration.",
                style="bodyL"))
    s += BUL([
        "(a) Draw a class diagram showing classes, attributes and operations. [4 marks]",
        "(b) Draw a sequence diagram for 'register for course'. [4 marks]",
        "(c) Draw a state diagram for Registration. [4 marks]",
    ])
    s.append(H2("Question B2 (8 marks)"))
    s.append(P("Consider the same registration system."))
    s += BUL([
        "(a) Explain how the three models are consistent. [4 marks]",
        "(b) Explain how they tell different parts of the story. [4 marks]",
    ])

    s.append(H1("Section C — Case Study (10 marks)"))
    s.append(P("Consider a complete university management system with all models from Weeks 1-12.",
                style="bodyL"))
    s.append(P("As an object-oriented analyst:"))
    s += BUL([
        "(a) Explain how all models fit together to describe the complete system. [4 marks]",
        "(b) Identify potential inconsistencies and how to resolve them. [3 marks]",
        "(c) Explain the value of integrated modelling for understanding and maintaining the system. [3 marks]",
    ])

    s.append(H1("Marking Scheme"))
    s.append(DTABLE(
        ["Section", "Content", "Marks"],
        [["A", "Short-answer questions (8 questions)", "20"],
         ["B", "Application questions (12 + 8)", "20"],
         ["C", "Case study — complete system", "10"],
         ["", "TOTAL", "50"]],
        widths=[0.25 * DOC_W, 0.55 * DOC_W, 0.20 * DOC_W]))

    s.append(H1("Submission & Academic Integrity"))
    s += BUL([
        "Submit a typed document (or neatly handwritten, as directed by your lecturer).",
        "This assignment is individual work. Plagiarism or copying will attract a penalty under university regulations.",
        "Ensure your diagrams are consistent with each other.",
        "Cite any sources you consult using the format used in the Week 12 module references.",
    ])

    return s


if __name__ == "__main__":
    print("Built:", build(CFG, story))
