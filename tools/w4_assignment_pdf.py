"""
Week 4 Assignment PDF content — THE BUILDING BLOCKS OF UML.
"""
from pdfengine import (H1, H2, P, BUL, build, DOC_W, DTABLE)

CFG = {
    "week": 4,
    "title": "Assignment: The Building Blocks of UML",
    "filename": "Week4_Assignment_BICT3202_OOAD.pdf",
}


def story():
    s = []

    s.append(H1("ASSIGNMENT INSTRUCTIONS"))
    s += BUL([
        "Answer ALL questions in Sections A, B and C.",
        "Read the Week 4 module and your lecture notes before attempting each question.",
        "Draw diagrams neatly with correct UML notation.",
        "Cite OMG UML 2.5.1 where relevant.",
        "Submit by the date given by your lecturer. Total: 50 marks.",
    ])

    s.append(H1("Section A — Short-Answer Questions (20 marks)"))
    questions_a = [
        ("Define a structural thing in UML.", "2"),
        ("Define a behavioural thing in UML.", "2"),
        ("Define a grouping thing in UML.", "2"),
        ("Define an annotation thing in UML.", "2"),
        ("What is an association relationship?", "2"),
        ("What is a generalisation relationship?", "2"),
        ("Differentiate aggregation from composition.", "3"),
        ("What is a dependency relationship?", "2"),
        ("Define multiplicity and give three examples.", "2"),
        ("Explain how relationships help manage complexity in object models.", "1"),
    ]
    for i, (q, m) in enumerate(questions_a, 1):
        s.append(H2(f"Question A{i}"))
        s.append(P(f"{q} [{m} marks]"))

    s.append(H1("Section B — Application Questions (20 marks)"))
    s.append(H2("Question B1 (12 marks)"))
    s.append(P("A university library system has Books, Members, Librarians and Loans."))
    s += BUL([
        "(a) Draw a class diagram showing these four classes with attributes. [4 marks]",
        "(b) Add associations between the classes with multiplicities. [4 marks]",
        "(c) Add one aggregation and one composition relationship with explanations. [4 marks]",
    ])
    s.append(H2("Question B2 (8 marks)"))
    s.append(P("Consider the relationship between Student and Course in a registration system."))
    s += BUL([
        "(a) What type of relationship is this? [2 marks]",
        "(b) What multiplicity would you assign and why? [2 marks]",
        "(c) How would this relationship appear in a class diagram? [2 marks]",
        "(d) What attributes might be needed to implement this relationship? [2 marks]",
    ])

    s.append(H1("Section C — Case Study (10 marks)"))
    s.append(P("'A hospital management system needs to model Patients, Doctors, Appointments, "
                "Departments and Medical Records.'", style="bodyL"))
    s.append(P("As an object-oriented analyst:"))
    s += BUL([
        "(a) Identify all structural things. [2 marks]",
        "(b) Identify the relationships between these elements. [3 marks]",
        "(c) Draw a class diagram showing the complete structure. [3 marks]",
        "(d) Explain the business meaning of each relationship. [2 marks]",
    ])

    s.append(H1("Marking Scheme"))
    s.append(DTABLE(
        ["Section", "Content", "Marks"],
        [["A", "Short-answer questions (10 questions)", "20"],
         ["B", "Application questions (12 + 8)", "20"],
         ["C", "Case study", "10"],
         ["", "TOTAL", "50"]],
        widths=[0.25 * DOC_W, 0.55 * DOC_W, 0.20 * DOC_W]))

    s.append(H1("Submission & Academic Integrity"))
    s += BUL([
        "Submit a typed document (or neatly handwritten, as directed by your lecturer).",
        "This assignment is individual work. Plagiarism or copying will attract a penalty under university regulations.",
        "Cite any sources you consult using the format used in the Week 4 module references.",
    ])

    return s


if __name__ == "__main__":
    print("Built:", build(CFG, story))
