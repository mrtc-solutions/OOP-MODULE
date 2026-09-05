"""
Week 16 Assignment PDF content — COMPREHENSIVE REVISION, INTEGRATED CASE STUDY AND EXAMINATION PREPARATION.
"""
from pdfengine import (H1, H2, P, BUL, build, DOC_W, DTABLE)

CFG = {
    "week": 16,
    "title": "Assignment: Comprehensive Revision and Examination Preparation",
    "filename": "Week16_Assignment_BICT3202_OOAD.pdf",
}


def story():
    s = []

    s.append(H1("ASSIGNMENT INSTRUCTIONS"))
    s += BUL([
        "Answer ALL questions in Sections A, B and C.",
        "Read the Week 16 module and your lecture notes before attempting each question.",
        "This assignment doubles as your examination revision.",
        "Draw UML diagrams in correct notation, and check that your models are consistent.",
        "Submit by the date given by your lecturer. Total: 50 marks.",
    ])

    s.append(H1("Section A — Short-Answer Questions (20 marks)"))
    questions_a = [
        ("Define object-oriented analysis and object-oriented design.", "3"),
        ("Distinguish an object from a class.", "2"),
        ("Define encapsulation and abstraction, with one example each.", "3"),
        ("Define inheritance and polymorphism.", "2"),
        ("Explain the business-to-software chain from Week 1.", "3"),
        ("State the four principles of object modelling.", "2"),
        ("What is UML and what is its current specification version?", "2"),
        ("Explain the relationship between the Object, Dynamic and Behavioural models.", "3"),
    ]
    for i, (q, m) in enumerate(questions_a, 1):
        s.append(H2(f"Question A{i}"))
        s.append(P(f"{q} [{m} marks]"))

    s.append(H1("Section B — Application Questions (20 marks)"))
    s.append(H2("Question B1 (12 marks)"))
    s.append(P("Consider the university course registration system as a comprehensive case study.",
                style="bodyL"))
    s += BUL([
        "(a) Apply the business-to-software chain to this system. [4 marks]",
        "(b) Identify all objects, attributes, behaviours and relationships. [4 marks]",
        "(c) Draw the complete object model. [4 marks]",
    ])
    s.append(H2("Question B2 (8 marks)"))
    s.append(P("Consider the integration of all 16 weeks of OOAD concepts."))
    s += BUL([
        "(a) Explain how all concepts fit together. [4 marks]",
        "(b) Identify the most important lessons from the module. [4 marks]",
    ])

    s.append(H1("Section C — Case Study (10 marks)"))
    s.append(P("Consider a new system of your choice (e.g., e-commerce, hospital, banking).",
                style="bodyL"))
    s.append(P("As an object-oriented analyst/designer:"))
    s += BUL([
        "(a) Apply OOAD concepts from Weeks 1-16 to analyse and design this system. [5 marks]",
        "(b) Explain how the concepts support a complete and effective design. [3 marks]",
        "(c) Identify lessons learned from the OOAD module. [2 marks]",
    ])

    s.append(H1("Marking Scheme"))
    s.append(DTABLE(
        ["Section", "Content", "Marks"],
        [["A", "Short-answer questions (8 questions)", "20"],
         ["B", "Application questions (12 + 8)", "20"],
         ["C", "Case study — comprehensive system", "10"],
         ["", "TOTAL", "50"]],
        widths=[0.25 * DOC_W, 0.55 * DOC_W, 0.20 * DOC_W]))

    s.append(H1("Submission & Academic Integrity"))
    s += BUL([
        "Submit a typed document (or neatly handwritten, as directed by your lecturer).",
        "This assignment is individual work. Plagiarism or copying will attract a penalty under university regulations.",
        "Ensure your answers demonstrate comprehensive understanding of OOAD.",
        "Cite any sources you consult using the format used in the Week 16 module references.",
    ])

    return s


if __name__ == "__main__":
    print("Built:", build(CFG, story))
