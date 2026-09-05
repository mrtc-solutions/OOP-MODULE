"""
Week 15 Assignment PDF content — COMPLETE OOAD CASE STUDY, MODEL INTEGRATION AND CASE TOOL IMPLEMENTATION.
"""
from pdfengine import (H1, H2, P, BUL, build, DOC_W, DTABLE)

CFG = {
    "week": 15,
    "title": "Assignment: OOAD Case Study and CASE Tool Implementation",
    "filename": "Week15_Assignment_BICT3202_OOAD.pdf",
}


def story():
    s = []

    s.append(H1("ASSIGNMENT INSTRUCTIONS"))
    s += BUL([
        "Answer ALL questions in Sections A, B and C.",
        "Read the Week 15 module and your lecture notes before attempting each question.",
        "Use the university course registration case study for your examples.",
        "Show that your models are consistent: messages must match operations.",
        "Draw UML diagrams in correct notation, or with a CASE/UML tool.",
        "Submit by the date given by your lecturer. Total: 50 marks.",
    ])

    s.append(H1("Section A — Short-Answer Questions (20 marks)"))
    questions_a = [
        ("Define a CASE tool and state three ways it supports software development.", "3"),
        ("Differentiate functional from non-functional requirements, with one example each.", "3"),
        ("Define an actor and explain why an actor need not be a human being.", "2"),
        ("Explain the relationship between requirements and use cases.", "2"),
        ("What is model integration and why is it important?", "2"),
        ("Define traceability and explain its value in OOAD.", "2"),
        ("Explain how CASE tools support model consistency.", "2"),
        ("State three benefits of using CASE tools in OOAD.", "2"),
    ]
    for i, (q, m) in enumerate(questions_a, 1):
        s.append(H2(f"Question A{i}"))
        s.append(P(f"{q} [{m} marks]"))

    s.append(H1("Section B — Application Questions (20 marks)"))
    s.append(H2("Question B1 (12 marks)"))
    s.append(P("Consider the university course registration system as a complete case study.",
                style="bodyL"))
    s += BUL([
        "(a) Integrate all models (object, dynamic, behavioural) into a complete design. [4 marks]",
        "(b) Show how the models are consistent with each other. [4 marks]",
        "(c) Explain how CASE tools could support this integration. [4 marks]",
    ])
    s.append(H2("Question B2 (8 marks)"))
    s.append(P("Consider implementing the registration system with a CASE tool."))
    s += BUL([
        "(a) Identify three CASE tool features that would be valuable. [4 marks]",
        "(b) Explain how these features support the development process. [4 marks]",
    ])

    s.append(H1("Section C — Case Study (10 marks)"))
    s.append(P("Consider a complete OOAD project for a banking system.",
                style="bodyL"))
    s.append(P("As an object-oriented analyst/designer:"))
    s += BUL([
        "(a) Explain how you would use CASE tools throughout the project lifecycle. [4 marks]",
        "(b) Identify potential challenges and how CASE tools help address them. [3 marks]",
        "(c) Explain the value of model integration for project success. [3 marks]",
    ])

    s.append(H1("Marking Scheme"))
    s.append(DTABLE(
        ["Section", "Content", "Marks"],
        [["A", "Short-answer questions (8 questions)", "20"],
         ["B", "Application questions (12 + 8)", "20"],
         ["C", "Case study — banking system", "10"],
         ["", "TOTAL", "50"]],
        widths=[0.25 * DOC_W, 0.55 * DOC_W, 0.20 * DOC_W]))

    s.append(H1("Submission & Academic Integrity"))
    s += BUL([
        "Submit a typed document (or neatly handwritten, as directed by your lecturer).",
        "This assignment is individual work. Plagiarism or copying will attract a penalty under university regulations.",
        "Ensure your models are complete and consistent.",
        "Cite any sources you consult using the format used in the Week 15 module references.",
    ])

    return s


if __name__ == "__main__":
    print("Built:", build(CFG, story))
