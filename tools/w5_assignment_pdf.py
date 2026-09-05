"""
Week 5 Assignment PDF content — OBJECT-ORIENTED ANALYSIS: OBJECT MODELLING I.
"""
from pdfengine import (H1, H2, P, BUL, build, DOC_W, DTABLE)

CFG = {
    "week": 5,
    "title": "Assignment: Object-Oriented Analysis — Object Modelling I",
    "filename": "Week5_Assignment_BICT3202_OOAD.pdf",
}


def story():
    s = []

    # Assignment Instructions
    s.append(H1("ASSIGNMENT INSTRUCTIONS"))
    s += BUL([
        "Answer ALL questions in Sections A, B and C.",
        "Read the Week 5 module and your lecture notes before attempting each question.",
        "Draw diagrams neatly (by hand or using a UML/CASE tool) with correct UML notation.",
        "For every association, show a meaningful name and multiplicities where required.",
        "Cite OMG UML 2.5.1 where relevant.",
        "Submit by the date given by your lecturer. Total: 50 marks.",
    ])

    # Section A
    s.append(H1("Section A — Short-Answer Questions (20 marks)"))
    questions_a = [
        ("Define Object-Oriented Analysis.", "2"),
        ("Differentiate between a class and an object, giving one example of each.", "3"),
        ("What is an attribute? Give two attributes of the class Course.", "2"),
        ("What is an operation? Give two operations of the class Student.", "2"),
        ("Differentiate between a link and an association.", "2"),
        ("What is multiplicity? Explain the meaning of 0..1, 1, 0..* and 1..*.", "3"),
        ("Define generalization and specialization.", "2"),
        ("Explain the 'is-a' test and use it to decide whether Student → Course is a generalization.", "2"),
        ("What is a CASE tool, and why can it not replace an analyst?", "2"),
    ]
    for i, (q, m) in enumerate(questions_a, 1):
        s.append(H2(f"Question A{i}"))
        s.append(P(f"{q} [{m} marks]"))

    # Section B
    s.append(H1("Section B — Application Questions (20 marks)"))
    s.append(H2("Question B1 (20 marks)"))
    s.append(P("'A university has students and lecturers. Each student has a student ID, name, programme "
                "and year of study. Each lecturer has a staff ID, name and department. Students register for "
                "courses. Each course has a course code, title and credit hours. Lecturers teach courses. A "
                "student may register for many courses, while each course may have many students.'",
                style="bodyL"))
    s += BUL([
        "(a) Identify the candidate classes. [3 marks]",
        "(b) Identify at least two attributes for each class. [4 marks]",
        "(c) Identify one or two operations that could reasonably belong to each class. [3 marks]",
        "(d) Draw a UML class diagram showing the associations, with meaningful names. [5 marks]",
        "(e) Add appropriate multiplicities to the associations. [3 marks]",
        "(f) State whether generalization is appropriate, and justify your answer. [2 marks]",
    ])

    # Section C
    s.append(H1("Section C — Case Study (10 marks)"))
    s.append(P("'A university wants an Accommodation Management System to manage students, rooms, "
                "hostels, accommodation applications, payments and wardens. Students apply for rooms. A "
                "hostel contains several rooms. A student can occupy one room at a time. A warden manages a "
                "hostel. Students make accommodation payments.'",
                style="bodyL"))
    s.append(P("As an object-oriented analyst:"))
    s += BUL([
        "(a) Identify the candidate classes (at least six). [3 marks]",
        "(b) Provide at least two attributes for each major class. [3 marks]",
        "(c) Draw the associations between the classes and add multiplicities. [4 marks]",
    ])

    # Marking Scheme
    s.append(H1("Marking Scheme"))
    s.append(DTABLE(
        ["Section", "Content", "Marks"],
        [["A", "Short-answer questions (9 questions)", "20"],
         ["B", "Application — class diagram (parts a-f)", "20"],
         ["C", "Case study — accommodation system", "10"],
         ["", "TOTAL", "50"]],
        widths=[0.25 * DOC_W, 0.55 * DOC_W, 0.20 * DOC_W]))

    # Submission & Academic Integrity
    s.append(H1("Submission & Academic Integrity"))
    s += BUL([
        "Submit a typed document (or neatly handwritten, as directed by your lecturer).",
        "This assignment is individual work. Plagiarism or copying will attract a penalty under university regulations.",
        "Diagrams must use correct UML notation — marks are awarded for notation, association names and multiplicities.",
        "Cite any sources you consult using the format used in the Week 5 module references.",
    ])

    return s


if __name__ == "__main__":
    print("Built:", build(CFG, story))
