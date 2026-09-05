"""
Week 8 Assignment PDF content — OBJECT-ORIENTED ANALYSIS: BEHAVIOURAL MODELLING.
"""
from pdfengine import (H1, H2, P, BUL, build, DOC_W, DTABLE)

CFG = {
    "week": 8,
    "title": "Assignment: Object-Oriented Analysis — Behavioural Modelling",
    "filename": "Week8_Assignment_BICT3202_OOAD.pdf",
}


def story():
    s = []

    s.append(H1("ASSIGNMENT INSTRUCTIONS"))
    s += BUL([
        "Answer ALL questions in Sections A, B and C.",
        "Read the Week 8 module and your lecture notes before attempting each question.",
        "Draw diagrams neatly (by hand or using a UML/CASE tool) with correct notation.",
        "Label all actors, use cases, relationships and multiplicities.",
        "Submit by the date given by your lecturer. Total: 50 marks.",
    ])

    s.append(H1("Section A — Short-Answer Questions (20 marks)"))
    questions_a = [
        ("Define a use case and explain its purpose in requirements capture.", "2"),
        ("Define an actor and differentiate it from a user.", "2"),
        ("Explain the difference between a primary actor and a secondary actor.", "2"),
        ("What is a use-case diagram? What are its main elements?", "2"),
        ("Define an interaction diagram and name the two main types.", "2"),
        ("Explain the purpose of a sequence diagram.", "2"),
        ("What is a collaboration diagram? How does it differ from a sequence diagram?", "3"),
        ("Define an activity diagram and explain when it should be used.", "2"),
        ("Explain the relationship between use cases and scenarios.", "3"),
    ]
    for i, (q, m) in enumerate(questions_a, 1):
        s.append(H2(f"Question A{i}"))
        s.append(P(f"{q} [{m} marks]"))

    s.append(H1("Section B — Application Questions (20 marks)"))
    s.append(H2("Question B1 (12 marks)"))
    s.append(P("'A university wants an online course registration system. Students search for courses, "
                "select courses, submit registration and receive confirmation.'",
                style="bodyL"))
    s += BUL([
        "(a) Identify the actors. [2 marks]",
        "(b) Identify the use cases. [2 marks]",
        "(c) Draw a use-case diagram. [4 marks]",
        "(d) Write the main scenario for 'Register for Course'. [4 marks]",
    ])
    s.append(H2("Question B2 (8 marks)"))
    s.append(P("Consider a student registering for a course with prerequisites."))
    s += BUL([
        "(a) Draw a sequence diagram for successful registration. [4 marks]",
        "(b) Explain what happens if prerequisites are not met. [4 marks]",
    ])

    s.append(H1("Section C — Case Study (10 marks)"))
    s.append(P("'A library wants a book borrowing system. Members search for books, reserve books, "
                "borrow books and return books. Librarians manage the book collection.'",
                style="bodyL"))
    s.append(P("As an object-oriented analyst:"))
    s += BUL([
        "(a) Draw a use-case diagram for the library system. [4 marks]",
        "(b) Draw a sequence diagram for the 'Borrow Book' use case. [3 marks]",
        "(c) Explain how these diagrams help in understanding system behaviour. [3 marks]",
    ])

    s.append(H1("Marking Scheme"))
    s.append(DTABLE(
        ["Section", "Content", "Marks"],
        [["A", "Short-answer questions (9 questions)", "20"],
         ["B", "Application questions (12 + 8)", "20"],
         ["C", "Case study — library system", "10"],
         ["", "TOTAL", "50"]],
        widths=[0.25 * DOC_W, 0.55 * DOC_W, 0.20 * DOC_W]))

    s.append(H1("Submission & Academic Integrity"))
    s += BUL([
        "Submit a typed document (or neatly handwritten, as directed by your lecturer).",
        "This assignment is individual work. Plagiarism or copying will attract a penalty under university regulations.",
        "Diagrams must use correct UML notation.",
        "Cite any sources you consult using the format used in the Week 8 module references.",
    ])

    return s


if __name__ == "__main__":
    print("Built:", build(CFG, story))
