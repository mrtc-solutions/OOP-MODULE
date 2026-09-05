"""
Week 9 Assignment PDF content — THE UNIFIED SOFTWARE DEVELOPMENT PROCESS (USDP / UP).
"""
from pdfengine import (H1, H2, P, BUL, build, DOC_W, DTABLE)

CFG = {
    "week": 9,
    "title": "Assignment: The Unified Software Development Process",
    "filename": "Week9_Assignment_BICT3202_OOAD.pdf",
}


def story():
    s = []

    s.append(H1("ASSIGNMENT INSTRUCTIONS"))
    s += BUL([
        "Answer ALL questions in Sections A, B and C.",
        "Read the Week 9 module and your lecture notes before attempting each question.",
        "Use clear examples from the university registration case study where possible.",
        "Diagrams (phases, iterations, workflows) must be neat and correctly labelled.",
        "Cite the OMG UML 2.5.1 specification and RUP references where relevant.",
        "Submit by the date given by your lecturer. Total: 50 marks.",
    ])

    s.append(H1("Section A — Short-Answer Questions (20 marks)"))
    questions_a = [
        ("Define the Unified Software Development Process.", "2"),
        ("Differentiate between the Unified Process and the Rational Unified Process.", "2"),
        ("Explain the difference between iterative and incremental development, with an example of each.", "3"),
        ("State and explain the four major characteristics of the Unified Process.", "4"),
        ("List the four UP phases and state the main question answered by each.", "3"),
        ("Differentiate between a phase, an iteration, a workflow and an artefact.", "2"),
        ("What is software reuse? Give two guidelines for evaluating a reusable component.", "2"),
        ("Differentiate between generalisation and inheritance.", "2"),
    ]
    for i, (q, m) in enumerate(questions_a, 1):
        s.append(H2(f"Question A{i}"))
        s.append(P(f"{q} [{m} marks]"))

    s.append(H1("Section B — Application Questions (20 marks)"))
    s.append(H2("Question B1 (12 marks)"))
    s.append(P("Exploits University wants an Online Student Management System. Students will register, "
                "view courses, pay fees and view results; lecturers will view classes, upload materials and "
                "enter marks; administrators will manage students and courses and generate reports.",
                style="bodyL"))
    s += BUL([
        "(a) Explain what would happen during Inception, listing its major activities and outputs. [3 marks]",
        "(b) Explain why Elaboration is particularly important, and give two architectural risks. [3 marks]",
        "(c) Describe three iterations that could occur during Construction. [3 marks]",
        "(d) Describe the activities of Transition. [3 marks]",
    ])
    s.append(H2("Question B2 (8 marks)"))
    s.append(P("Consider the requirement 'students must register for courses'."))
    s += BUL([
        "(a) Explain how UP is use-case driven, using this requirement. [3 marks]",
        "(b) Explain how the Week 8 models (use case, activity, sequence) become artefacts in UP. [3 marks]",
        "(c) Identify two reusable assets that could support this system and evaluate each. [2 marks]",
    ])

    s.append(H1("Section C — Case Study (10 marks)"))
    s.append(P("'A hospital intends to develop an online patient management system to register patients, "
                "book appointments, process payments, store medical records and generate reports. The "
                "hospital is particularly concerned about security, performance and integration with "
                "existing systems.'",
                style="bodyL"))
    s.append(P("As an object-oriented analyst:"))
    s += BUL([
        "(a) Explain how UP could be used to develop the system. [3 marks]",
        "(b) Explain what should happen during Inception and why Elaboration is particularly important. [3 marks]",
        "(c) Give three architectural risks and suggest three artefacts for the project. [4 marks]",
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
        "Where you describe UP phases, iterations and artefacts, relate them to the given scenario rather than reciting definitions only.",
        "Cite any sources you consult using the format used in the Week 9 module references.",
    ])

    return s


if __name__ == "__main__":
    print("Built:", build(CFG, story))
