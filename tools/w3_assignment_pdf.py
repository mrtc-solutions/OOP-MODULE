"""
Week 3 Assignment PDF content — MODELLING LANGUAGE: UML.
"""
from pdfengine import (H1, H2, P, BUL, build, DOC_W, DTABLE)

CFG = {
    "week": 3,
    "title": "Assignment: Modelling Language - UML",
    "filename": "Week3_Assignment_BICT3202_OOAD.pdf",
}


def story():
    s = []

    # Assignment Instructions
    s.append(H1("ASSIGNMENT INSTRUCTIONS"))
    s += BUL([
        "Answer ALL questions in Sections A, B and C.",
        "Read the Week 3 module and your lecture notes before attempting each question.",
        "Draw diagrams neatly (by hand or using a UML/diagramming tool) with correct notation.",
        "Cite OMG UML 2.5.1 and MOF where relevant.",
        "Submit by the date given by your lecturer. Total: 50 marks.",
    ])

    # Section A
    s.append(H1("Section A — Short-Answer Questions (20 marks)"))
    questions_a = [
        ("Define UML and state what each part of the name means.", "3"),
        ("Explain the difference between a modelling language and a development methodology, using UML and UP as examples.", "2"),
        ("Name the three conceptual building blocks of UML.", "2"),
        ("List and give one example each of the four kinds of UML 'things'.", "2"),
        ("Name the four main UML relationship types.", "2"),
        ("Differentiate between syntax and semantics in UML.", "2"),
        ("Explain the four common mechanisms of UML.", "2"),
        ("Define a stereotype, a tagged value and a constraint, with an example of each.", "3"),
        ("Explain the four UML layers M3, M2, M1 and M0.", "2"),
    ]
    for i, (q, m) in enumerate(questions_a, 1):
        s.append(H2(f"Question A{i}"))
        s.append(P(f"{q} [{m} marks]"))

    # Section B
    s.append(H1("Section B — Application Questions (20 marks)"))
    s.append(H2("Question B1 (12 marks)"))
    s.append(P("A university wants a mobile student registration application. Students can log in, view "
                "courses, register courses, drop courses and view their registration status. The application "
                "communicates with a university server and a database.", style="bodyL"))
    s.append(P("For each requirement below, state the most appropriate UML diagram and justify your choice:"))
    s += BUL([
        "(a) Show what functions students can perform. [2 marks]",
        "(b) Show the Student and Course classes and their relationship. [2 marks]",
        "(c) Show the login communication between the app, server and database. [2 marks]",
        "(d) Show the steps in the course-registration workflow. [2 marks]",
        "(e) Show the states of a registration (Draft → Submitted → Approved). [2 marks]",
        "(f) Show where the app, server and database are deployed. [2 marks]",
    ])
    s.append(H2("Question B2 (8 marks)"))
    s.append(P("Draw a simple UML class diagram for the university registration system containing Student, "
                "Course, Lecturer and Registration."))
    s += BUL([
        "(a) Show the four classes with two attributes each. [2 marks]",
        "(b) Add the relationships Student—Registration, Course—Registration and Lecturer—Course. [2 marks]",
        "(c) Add sensible multiplicities to two of the relationships. [2 marks]",
        "(d) Add one constraint or note expressing a business rule (e.g. prerequisites). [2 marks]",
    ])

    # Section C
    s.append(H1("Section C — Case Study (10 marks)"))
    s.append(P("'An online banking system allows customers to view balances, transfer money between "
                "accounts and pay bills. The system authenticates customers, communicates with a core banking "
                "server and a database, and must encrypt all transfers.'", style="bodyL"))
    s.append(P("As an object-oriented analyst:"))
    s += BUL([
        "(a) Explain how UML would help the analyst, developer, database designer and bank manager communicate about this system. [3 marks]",
        "(b) Identify which UML diagrams you would use to show: the functions a customer can perform; the Account and Transaction classes; the order of a transfer; the states of a transaction. [4 marks]",
        "(c) Use the four-layer architecture (M0–M3) to explain where 'Customer', 'Account', 'Class' and 'MOF' belong. [3 marks]",
    ])

    # Marking Scheme
    s.append(H1("Marking Scheme"))
    s.append(DTABLE(
        ["Section", "Content", "Marks"],
        [["A", "Short-answer questions (9 questions)", "20"],
         ["B", "Application questions (12 + 8)", "20"],
         ["C", "Case study", "10"],
         ["", "TOTAL", "50"]],
        widths=[0.25 * DOC_W, 0.55 * DOC_W, 0.20 * DOC_W]))

    # Submission & Academic Integrity
    s.append(H1("Submission & Academic Integrity"))
    s += BUL([
        "Submit a typed document (or neatly handwritten, as directed by your lecturer).",
        "This assignment is individual work. Plagiarism or copying will attract a penalty under university regulations.",
        "Cite any sources you consult using the format used in the Week 3 module references.",
    ])

    return s


if __name__ == "__main__":
    print("Built:", build(CFG, story))
