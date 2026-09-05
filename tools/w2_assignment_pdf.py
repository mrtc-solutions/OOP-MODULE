"""
Week 2 Assignment PDF content — PRINCIPLES OF OBJECT MODELLING.
"""
from pdfengine import (H1, H2, P, BUL, build, DOC_W, DTABLE)

CFG = {
    "week": 2,
    "title": "Assignment: Principles of Object Modelling",
    "filename": "Week2_Assignment_BICT3202_OOAD.pdf",
}


def story():
    s = []

    # Assignment Instructions
    s.append(H1("ASSIGNMENT INSTRUCTIONS"))
    s += BUL([
        "Answer ALL questions in Sections A, B and C.",
        "Read the Week 2 module and your lecture notes before attempting each question.",
        "Where a question asks you to 'identify', write clear, specific items and justify each choice.",
        "Cite ISO/IEC/IEEE 29148:2018 and OMG UML 2.5.1 where relevant.",
        "Submit by the date given by your lecturer. Total: 50 marks.",
    ])

    # Section A
    s.append(H1("Section A — Short-Answer Questions (20 marks)"))
    questions_a = [
        ("Define object modelling.", "2"),
        ("Define an object model.", "2"),
        ("Why are object models useful in systems analysis?", "2"),
        ("Explain the relationship between an object, a class and an object model.", "2"),
        ("Define abstraction and give one example from object modelling.", "2"),
        ("Define encapsulation and explain why it matters for a bank account.", "2"),
        ("What is object identity? How does it differ from an attribute?", "2"),
        ("Distinguish between object state and object behaviour.", "2"),
        ("What is object identification? Why should not every noun become a class?", "2"),
        ("Name the standard language used to express object models, and state the current published specification version.", "2"),
    ]
    for i, (q, m) in enumerate(questions_a, 1):
        s.append(H2(f"Question A{i}"))
        s.append(P(f"{q} [{m} marks]"))

    # Section B
    s.append(H1("Section B — Application Questions (20 marks)"))
    s.append(H2("Question B1 (12 marks)"))
    s.append(P("'A customer uses a mobile phone to purchase a product from an online shop. The customer "
                "adds the product to a shopping cart and pays using mobile money. The system generates an "
                "invoice.'", style="bodyL"))
    s.append(P("Identify:"))
    s += BUL([
        "(a) six candidate objects; [3 marks]",
        "(b) two attributes for three of the objects; [3 marks]",
        "(c) two behaviours for two of the objects; [2 marks]",
        "(d) three relationships; [2 marks]",
        "(e) two external systems, and state whether 'Mobile Phone', 'Mobile Money' and 'Invoice' should be objects — with reasons. [2 marks]",
    ])
    s.append(H2("Question B2 (8 marks)"))
    s.append(P("A hospital wants an electronic appointment management system. Patients request "
                "appointments with doctors; doctors have specialties; receptionists manage appointments."))
    s += BUL([
        "(a) five candidate objects; [2 marks]",
        "(b) attributes for Patient and Appointment; [2 marks]",
        "(c) three behaviours; [2 marks]",
        "(d) two relationships, and one piece of information to be excluded through abstraction. [2 marks]",
    ])

    # Section C
    s.append(H1("Section C — Case Study (10 marks)"))
    s.append(P("'A university wants to develop an online course registration system. Students select "
                "courses and submit a registration; lecturers approve registrations; the system enforces "
                "prerequisites and records payments.'", style="bodyL"))
    s.append(P("As an object-oriented analyst:"))
    s += BUL([
        "(a) Identify ten candidate objects. [2 marks]",
        "(b) Give five attributes for appropriate objects and five behaviours. [3 marks]",
        "(c) Give five relationships between objects. [2 marks]",
        "(d) Explain how abstraction, encapsulation and modularity would help you keep this model simple and maintainable. [3 marks]",
    ])

    # Marking Scheme
    s.append(H1("Marking Scheme"))
    s.append(DTABLE(
        ["Section", "Content", "Marks"],
        [["A", "Short-answer questions (10 × 2)", "20"],
         ["B", "Application questions (12 + 8)", "20"],
         ["C", "Case study", "10"],
         ["", "TOTAL", "50"]],
        widths=[0.25 * DOC_W, 0.55 * DOC_W, 0.20 * DOC_W]))

    # Submission & Academic Integrity
    s.append(H1("Submission & Academic Integrity"))
    s += BUL([
        "Submit a typed document (or neatly handwritten, as directed by your lecturer).",
        "This assignment is individual work. Plagiarism or copying will attract a penalty under university regulations.",
        "Cite any sources you consult using the format used in the Week 2 module references.",
    ])

    return s


if __name__ == "__main__":
    print("Built:", build(CFG, story))
