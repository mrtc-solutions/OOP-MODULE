"""
Week 14 Assignment PDF content — INTEGRATING OBJECT, DYNAMIC AND BEHAVIOURAL MODELS INTO OOD.
"""
from pdfengine import (H1, H2, P, BUL, build, DOC_W, DTABLE)

CFG = {
    "week": 14,
    "title": "Assignment: Integrating OOAD Models into Design",
    "filename": "Week14_Assignment_BICT3202_OOAD.pdf",
}


def story():
    s = []

    s.append(H1("ASSIGNMENT INSTRUCTIONS"))
    s += BUL([
        "Answer ALL questions in Sections A, B and C.",
        "Read the Week 14 module and your lecture notes before attempting each question.",
        "Use the university course registration case study for your examples.",
        "Design classes must show visibility, data types, parameters and return types.",
        "Show how your models are consistent: messages must match operations.",
        "Submit by the date given by your lecturer. Total: 50 marks.",
    ])

    s.append(H1("Section A — Short-Answer Questions (20 marks)"))
    questions_a = [
        ("Define object-oriented design and differentiate it from object-oriented analysis.", "3"),
        ("Explain why analysis models must be transformed into design models.", "2"),
        ("Define a design class and list four details it adds over an analysis class.", "3"),
        ("What is visibility and why is it important in design classes?", "2"),
        ("Define a parameter and explain its role in design operations.", "2"),
        ("Explain the purpose of return types in design.", "2"),
        ("What is a design pattern and how does it support good design?", "2"),
        ("Explain how object, dynamic and behavioural models integrate in design.", "2"),
    ]
    for i, (q, m) in enumerate(questions_a, 1):
        s.append(H2(f"Question A{i}"))
        s.append(P(f"{q} [{m} marks]"))

    s.append(H1("Section B — Application Questions (20 marks)"))
    s.append(H2("Question B1 (12 marks)"))
    s.append(P("Consider integrating the Object, Dynamic and Behavioural models for a registration system.",
                style="bodyL"))
    s += BUL([
        "(a) Show how the class diagram provides structure. [3 marks]",
        "(b) Show how the state diagram adds state behaviour. [3 marks]",
        "(c) Show how the sequence diagram adds interaction detail. [3 marks]",
        "(d) Explain how these models together provide a complete design. [3 marks]",
    ])
    s.append(H2("Question B2 (8 marks)"))
    s.append(P("Consider a Student class with analysis attributes and operations."))
    s += BUL([
        "(a) Transform it into a design class with visibility and types. [4 marks]",
        "(b) Explain how this transformation supports implementation. [4 marks]",
    ])

    s.append(H1("Section C — Case Study (10 marks)"))
    s.append(P("Consider the complete university management system with all three models.",
                style="bodyL"))
    s.append(P("As an object-oriented designer:"))
    s += BUL([
        "(a) Explain how to integrate all three models into a cohesive design. [4 marks]",
        "(b) Identify potential inconsistencies and how to resolve them. [3 marks]",
        "(c) Explain the value of integrated modelling for implementation. [3 marks]",
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
        "Ensure your design models are complete and consistent.",
        "Cite any sources you consult using the format used in the Week 14 module references.",
    ])

    return s


if __name__ == "__main__":
    print("Built:", build(CFG, story))
