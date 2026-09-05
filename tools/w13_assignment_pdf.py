"""
Week 13 Assignment PDF content — MULTILAYER SYSTEMS, REUSABLE COMPONENTS AND ARCHITECTURAL DESIGN.
"""
from pdfengine import (H1, H2, P, BUL, build, DOC_W, DTABLE)

CFG = {
    "week": 13,
    "title": "Assignment: Multilayer Systems and Architectural Design",
    "filename": "Week13_Assignment_BICT3202_OOAD.pdf",
}


def story():
    s = []

    s.append(H1("ASSIGNMENT INSTRUCTIONS"))
    s += BUL([
        "Answer ALL questions in Sections A, B and C.",
        "Read the Week 13 module and your lecture notes before attempting each question.",
        "Use the university course registration case study for your examples.",
        "Component, package and deployment diagrams must use correct UML notation.",
        "Where you critique an architecture, propose a concrete improvement.",
        "Submit by the date given by your lecturer. Total: 50 marks.",
    ])

    s.append(H1("Section A — Short-Answer Questions (20 marks)"))
    questions_a = [
        ("Define software architecture and distinguish it from class design.", "3"),
        ("Define a software layer and list the layers of a common multilayer architecture.", "3"),
        ("Explain the responsibilities of the Presentation and Domain layers.", "2"),
        ("Define a reusable component and give one example.", "2"),
        ("Explain how multilayer architecture supports separation of concerns.", "2"),
        ("What is a component diagram and when should it be used?", "2"),
        ("Define a package and explain its purpose in UML.", "2"),
        ("Explain the relationship between components and packages.", "2"),
    ]
    for i, (q, m) in enumerate(questions_a, 1):
        s.append(H2(f"Question A{i}"))
        s.append(P(f"{q} [{m} marks]"))

    s.append(H1("Section B — Application Questions (20 marks)"))
    s.append(H2("Question B1 (12 marks)"))
    s.append(P("Consider a university management system with Presentation, Business Logic and Data layers.",
                style="bodyL"))
    s += BUL([
        "(a) Explain what belongs in each layer. [4 marks]",
        "(b) Draw a component diagram showing the layers. [4 marks]",
        "(c) Explain how this architecture supports reuse. [4 marks]",
    ])
    s.append(H2("Question B2 (8 marks)"))
    s.append(P("Consider the Registration component."))
    s += BUL([
        "(a) Identify reusable components within Registration. [4 marks]",
        "(b) Explain how these components could be reused in another system. [4 marks]",
    ])

    s.append(H1("Section C — Case Study (10 marks)"))
    s.append(P("Consider a hospital management system with multiple layers and reusable components.",
                style="bodyL"))
    s.append(P("As an object-oriented architect:"))
    s += BUL([
        "(a) Design a multilayer architecture for the system. [4 marks]",
        "(b) Identify reusable components and explain their value. [3 marks]",
        "(c) Explain how this architecture supports maintainability and scalability. [3 marks]",
    ])

    s.append(H1("Marking Scheme"))
    s.append(DTABLE(
        ["Section", "Content", "Marks"],
        [["A", "Short-answer questions (8 questions)", "20"],
         ["B", "Application questions (12 + 8)", "20"],
         ["C", "Case study — hospital system", "10"],
         ["", "TOTAL", "50"]],
        widths=[0.25 * DOC_W, 0.55 * DOC_W, 0.20 * DOC_W]))

    s.append(H1("Submission & Academic Integrity"))
    s += BUL([
        "Submit a typed document (or neatly handwritten, as directed by your lecturer).",
        "This assignment is individual work. Plagiarism or copying will attract a penalty under university regulations.",
        "Diagrams must use correct UML notation for components and packages.",
        "Cite any sources you consult using the format used in the Week 13 module references.",
    ])

    return s


if __name__ == "__main__":
    print("Built:", build(CFG, story))
