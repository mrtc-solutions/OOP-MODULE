"""
Week 1 Assignment PDF content — BUSINESS NEEDS, SOFTWARE NEEDS AND OBJECT TECHNOLOGY.
"""
from pdfengine import (H1, H2, P, BUL, build, DOC_W, DTABLE)

CFG = {
    "week": 1,
    "title": "Assignment: Business Needs, Software Needs and Object Technology",
    "filename": "Week1_Assignment_BICT3202_OOAD.pdf",
}


def story():
    s = []

    # Assignment Instructions
    s.append(H1("ASSIGNMENT INSTRUCTIONS"))
    s += BUL([
        "Answer ALL questions in Sections A, B and C.",
        "Read the Week 1 module and your lecture notes before attempting each question.",
        "Use real-world examples from business, banking, or university systems.",
        "Cite ISO/IEC/IEEE 29148:2018 where relevant.",
        "Submit by the date given by your lecturer. Total: 50 marks.",
    ])

    # Section A
    s.append(H1("Section A — Short-Answer Questions (20 marks)"))
    questions_a = [
        ("Define a business need.", "2"),
        ("What is a business problem?", "2"),
        ("Differentiate between a business problem and a business need.", "3"),
        ("What is a business objective?", "2"),
        ("Define a stakeholder.", "2"),
        ("What is a functional requirement?", "2"),
        ("What is a non-functional requirement?", "2"),
        ("What is a business rule?", "2"),
        ("Define object technology.", "2"),
        ("What is an object?", "1"),
    ]
    for i, (q, m) in enumerate(questions_a, 1):
        s.append(H2(f"Question A{i}"))
        s.append(P(f"{q} [{m} marks]"))

    # Section B
    s.append(H1("Section B — Application Questions (20 marks)"))
    s.append(H2("Question B1 (10 marks)"))
    s.append(P("A hospital has patients waiting several hours before being attended to."))
    s.append(P("Identify:"))
    s += BUL([
        "(a) The business problem [2 marks]",
        "(b) Two business needs [2 marks]",
        "(c) Two business objectives [2 marks]",
        "(d) Five stakeholders [2 marks]",
        "(e) Five functional requirements [2 marks]",
    ])
    s.append(H2("Question B2 (10 marks)"))
    s.append(P("A university wants an online examination management system."))
    s.append(P("Identify:"))
    s += BUL([
        "(a) The business need [2 marks]",
        "(b) Five stakeholders [2 marks]",
        "(c) Five functional requirements [2 marks]",
        "(d) Five non-functional requirements [2 marks]",
        "(e) Five candidate objects [2 marks]",
    ])

    # Section C
    s.append(H1("Section C — Case Study (10 marks)"))
    s.append(P("'A retail organization currently records sales using handwritten receipts. Management "
                "wants to introduce a computerized sales management system.'", style="bodyL"))
    s.append(P("As an object-oriented systems analyst, explain how you would move from understanding the "
                "business need to identifying potential objects for the proposed system."))
    s.append(P("Your answer should discuss:"))
    s += BUL([
        "Current business problem;",
        "Business objectives;",
        "Business needs;",
        "Stakeholders;",
        "Requirements elicitation;",
        "Functional requirements;",
        "Non-functional requirements;",
        "Business rules;",
        "Candidate objects;",
        "State and behaviour of the candidate objects.",
    ])

    # Marking Scheme
    s.append(H1("Marking Scheme"))
    s.append(DTABLE(
        ["Section", "Content", "Marks"],
        [["A", "Short-answer questions (10 questions)", "20"],
         ["B", "Application questions (10 + 10)", "20"],
         ["C", "Case study", "10"],
         ["", "TOTAL", "50"]],
        widths=[0.25 * DOC_W, 0.55 * DOC_W, 0.20 * DOC_W]))

    # Submission & Academic Integrity
    s.append(H1("Submission & Academic Integrity"))
    s += BUL([
        "Submit a typed document (or neatly handwritten, as directed by your lecturer).",
        "This assignment is individual work. Plagiarism or copying will attract a penalty under university regulations.",
        "Cite any sources you consult using the format used in the Week 1 module references.",
    ])

    return s


if __name__ == "__main__":
    print("Built:", build(CFG, story))
