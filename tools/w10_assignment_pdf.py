"""
Week 10 Assignment PDF content — OBJECT-ORIENTED DESIGN.
"""
from pdfengine import (H1, H2, H3, P, BUL, FIG, CALLOUT, DTABLE, build, DOC_W,
                      C_MAROON, C_SOFT, C_GOLD, C_CREAM, S)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch

CFG = {
    "week": 10,
    "title": "Assignment: Object-Oriented Design",
    "filename": "Week10_Assignment_BICT3202_OOAD.pdf",
}


def story():
    s = []

    # Assignment Instructions
    s.append(H1("ASSIGNMENT INSTRUCTIONS"))
    s += BUL([
        "Answer ALL questions in Sections A, B and C.",
        "Read the Week 10 module and your lecture notes before attempting each question.",
        "Use the university student registration case study for your examples.",
        "Diagrams (class, sequence, state) must be neat, complete and correctly labelled.",
        "Cite the OMG UML 2.5.1 specification and IBM design/analysis model guidance where relevant.",
        "Submit by the date given by your lecturer. Total: 50 marks.",
    ])

    # Section A
    s.append(H1("Section A — Short-Answer Questions (20 marks)"))
    s.append(H2("Question A1"))
    s.append(P("Define software design and object-oriented design. [3 marks]"))
    s.append(H2("Question A2"))
    s.append(P("Differentiate object-oriented analysis from object-oriented design, with an example. [3 marks]"))
    s.append(H2("Question A3"))
    s.append(P("State four goals of good object-oriented design. [2 marks]"))
    s.append(H2("Question A4"))
    s.append(P("Define cohesion and coupling. [2 marks]"))
    s.append(H2("Question A5"))
    s.append(P("Explain why good design generally seeks high cohesion and low coupling. [2 marks]"))
    s.append(H2("Question A6"))
    s.append(P("Differentiate abstraction from encapsulation using a BankAccount example. [3 marks]"))
    s.append(H2("Question A7"))
    s.append(P("Explain the Object, Dynamic and Behavioural models. [3 marks]"))
    s.append(H2("Question A8"))
    s.append(P("What is traceability, and why is it valuable? [2 marks]"))

    # Section B
    s.append(H1("Section B — Application Questions (20 marks)"))
    s.append(H2("Question B1 (12 marks)"))
    s.append(P("Exploits University wants an Online Student Registration System. Students will log in, "
                "search for courses, register for courses, drop courses and view registered courses."))
    s += BUL([
        "(a) Identify five possible classes for the system. [2 marks]",
        "(b) Assign at least two responsibilities to each class. [3 marks]",
        "(c) Draw a class diagram showing attributes, operations, associations and multiplicities. [3 marks]",
        "(d) Explain how the Object, Dynamic and Behavioural models support one another. [4 marks]",
    ])
    s.append(H2("Question B2 (8 marks)"))
    s.append(P("Consider the requirement 'a student registers for a course'."))
    s += BUL([
        "(a) Draw a sequence diagram for the course registration flow. [4 marks]",
        "(b) Draw a state diagram for the Registration object. [2 marks]",
        "(c) Identify one cohesion and one coupling problem that could arise, and suggest a fix. [2 marks]",
    ])

    # Section C
    s.append(H1("Section C — Case Study (10 marks)"))
    s.append(P("A bank wants a mobile banking application allowing customers to check balances, "
                "transfer money, pay bills and buy airtime. The system must be secure, support many "
                "simultaneous users, and allow new payment methods to be added in future.",
                style="bodyL"))
    s.append(P("As an object-oriented designer:"))
    s += BUL([
        "(a) Identify five classes and their responsibilities. [3 marks]",
        "(b) Explain how the three models (object, dynamic, behavioural) would be combined. [3 marks]",
        "(c) Explain how an interface and a design pattern could support adding new payment methods. [4 marks]",
    ])

    # Marking Scheme
    s.append(H1("Marking Scheme"))
    s.append(DTABLE(
        ["Section", "Content", "Marks"],
        [["A", "Short-answer questions (8 questions)", "20"],
         ["B", "Application questions (12 + 8)", "20"],
         ["C", "Case study — mobile banking system", "10"],
         ["", "TOTAL", "50"]],
        widths=[0.25 * DOC_W, 0.55 * DOC_W, 0.20 * DOC_W]))

    # Submission & Academic Integrity
    s.append(H1("Submission & Academic Integrity"))
    s += BUL([
        "Submit a typed document (or neatly handwritten, as directed by your lecturer).",
        "This assignment is individual work. Plagiarism or copying will attract a penalty under university regulations.",
        "Hand-drawn diagrams must use a ruler and correct UML notation; software-drawn diagrams are welcome.",
        "Where you describe cohesion, coupling, abstraction or encapsulation, illustrate with the given scenario rather than definitions only.",
        "Cite any sources you consult using the format used in the Week 10 module references.",
    ])

    return s


if __name__ == "__main__":
    print("Built:", build(CFG, story))
