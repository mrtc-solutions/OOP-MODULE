"""
Week 11 Assignment PDF content — REFINING THE OBJECT-ORIENTED DESIGN.
"""
from pdfengine import (H1, H2, P, BUL, build, DOC_W, DTABLE)

CFG = {
    "week": 11,
    "title": "Assignment: Refining the Object-Oriented Design",
    "filename": "Week11_Assignment_BICT3202_OOAD.pdf",
}


def story():
    s = []

    s.append(H1("ASSIGNMENT INSTRUCTIONS"))
    s += BUL([
        "Answer ALL questions in Sections A, B and C.",
        "Read the Week 11 module and your lecture notes before attempting each question.",
        "Use the university course registration case study for your examples.",
        "UML notation must be correct — visibility (-, +), types, parameters and return values.",
        "Where you critique a design, propose a concrete improvement, not just a description.",
        "Submit by the date given by your lecturer. Total: 50 marks.",
    ])

    s.append(H1("Section A — Short-Answer Questions (20 marks)"))
    questions_a = [
        ("Define design refinement and explain its purpose.", "2"),
        ("Differentiate an analysis class from a design class, with an example.", "3"),
        ("Define entity, boundary and control classes, giving one example of each.", "3"),
        ("Explain the purpose of adding visibility to attributes and operations.", "2"),
        ("What is a parameter? Differentiate it from an attribute.", "2"),
        ("Define a return type and explain why it matters in design.", "2"),
        ("Explain the relationship between analysis and design models.", "2"),
        ("What is traceability and why is it important in refinement?", "2"),
    ]
    for i, (q, m) in enumerate(questions_a, 1):
        s.append(H2(f"Question A{i}"))
        s.append(P(f"{q} [{m} marks]"))

    s.append(H1("Section B — Application Questions (20 marks)"))
    s.append(H2("Question B1 (12 marks)"))
    s.append(P("Consider the analysis class Student with attributes and operations.", style="bodyL"))
    s += BUL([
        "(a) Refine Student into a design class with typed attributes. [3 marks]",
        "(b) Add typed parameters and return types to operations. [3 marks]",
        "(c) Add visibility markers to attributes and operations. [3 marks]",
        "(d) Explain your visibility decisions. [3 marks]",
    ])
    s.append(H2("Question B2 (8 marks)"))
    s.append(P("Consider the analysis relationship Student — registers for — Course."))
    s += BUL([
        "(a) Draw this as a design class diagram with visibility. [4 marks]",
        "(b) Add an association class Registration if appropriate. [4 marks]",
    ])

    s.append(H1("Section C — Case Study (10 marks)"))
    s.append(P("Consider the university course registration system with Student, Course, Lecturer and Registration.",
                style="bodyL"))
    s.append(P("As an object-oriented designer:"))
    s += BUL([
        "(a) Refine the analysis model into a design model with typed attributes and operations. [4 marks]",
        "(b) Add visibility and explain your decisions. [3 marks]",
        "(c) Show how the design model maintains traceability to the analysis model. [3 marks]",
    ])

    s.append(H1("Marking Scheme"))
    s.append(DTABLE(
        ["Section", "Content", "Marks"],
        [["A", "Short-answer questions (8 questions)", "20"],
         ["B", "Application questions (12 + 8)", "20"],
         ["C", "Case study — registration system", "10"],
         ["", "TOTAL", "50"]],
        widths=[0.25 * DOC_W, 0.55 * DOC_W, 0.20 * DOC_W]))

    s.append(H1("Submission & Academic Integrity"))
    s += BUL([
        "Submit a typed document (or neatly handwritten, as directed by your lecturer).",
        "This assignment is individual work. Plagiarism or copying will attract a penalty under university regulations.",
        "Where you refine models, show the before and after versions clearly.",
        "Cite any sources you consult using the format used in the Week 11 module references.",
    ])

    return s


if __name__ == "__main__":
    print("Built:", build(CFG, story))
