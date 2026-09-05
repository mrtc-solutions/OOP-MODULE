"""
Week 7 Assignment PDF content — OBJECT-ORIENTED ANALYSIS: DYNAMIC MODELLING.
"""
from pdfengine import (H1, H2, P, BUL, build, DOC_W, DTABLE)

CFG = {
    "week": 7,
    "title": "Assignment: Object-Oriented Analysis — Dynamic Modelling",
    "filename": "Week7_Assignment_BICT3202_OOAD.pdf",
}


def story():
    s = []

    s.append(H1("ASSIGNMENT INSTRUCTIONS"))
    s += BUL([
        "Answer ALL questions in Sections A, B and C.",
        "Read the Week 7 module and your lecture notes before attempting each question.",
        "Draw state-machine diagrams neatly (by hand or using a UML/CASE tool) with correct notation.",
        "Use a filled circle for the initial state and a bull's-eye for the final state; label every transition.",
        "Justify guards and every transition you include.",
        "Submit by the date given by your lecturer. Total: 50 marks.",
    ])

    s.append(H1("Section A — Short-Answer Questions (20 marks)"))
    questions_a = [
        ("Define dynamic modelling and explain why it is needed in an object-oriented system.", "2"),
        ("Define an event and give two examples from different categories.", "2"),
        ("Define a state and differentiate it from an event.", "3"),
        ("What is a transition? What is a guard condition? Give an example of each.", "3"),
        ("Explain entry, exit and do behaviour, with one example of each.", "3"),
        ("Define an operation and differentiate it from an event.", "2"),
        ("What is concurrency? Differentiate sequential from concurrent behaviour.", "3"),
        ("Explain why a class diagram alone is insufficient for modelling a complex Order object.", "2"),
    ]
    for i, (q, m) in enumerate(questions_a, 1):
        s.append(H2(f"Question A{i}"))
        s.append(P(f"{q} [{m} marks]"))

    s.append(H1("Section B — Application Questions (20 marks)"))
    s.append(H2("Question B1 (12 marks)"))
    s.append(P("'A bank account can be Active, Blocked or Closed. The events that occur are login, "
                "wrongPIN, blockAccount, unblockAccount and closeAccount.'",
                style="bodyL"))
    s += BUL([
        "(a) Identify the states and the events. [2 marks]",
        "(b) Draw the state-machine diagram with an initial state. [4 marks]",
        "(c) Add a guard that blocks the account after three wrong PIN entries. [2 marks]",
        "(d) Identify any transition that should NOT be allowed, and justify your answer. [4 marks]",
    ])
    s.append(H2("Question B2 (8 marks)"))
    s.append(P("Consider an online payment with states Pending, Processing, Paid and Failed, and events "
                "submitPayment, paymentSuccessful and paymentFailed."))
    s += BUL([
        "(a) Draw the state-machine diagram. [3 marks]",
        "(b) Add guards to distinguish the successful and failed outcomes. [2 marks]",
        "(c) Add entry behaviour to the Paid state (e.g. send a confirmation email). [1 mark]",
        "(d) Explain, in words, what the diagram says as a story. [2 marks]",
    ])

    s.append(H1("Section C — Case Study (10 marks)"))
    s.append(P("'A food delivery application performs the following after an order is placed: payment "
                "processing, restaurant order preparation, driver assignment and customer notification. An "
                "order moves from Placed to Preparing, then to Out for Delivery, then to Delivered (or "
                "Cancelled).'",
                style="bodyL"))
    s.append(P("As an object-oriented analyst:"))
    s += BUL([
        "(a) Identify the states and events of the Order. [3 marks]",
        "(b) Draw the Order state-machine diagram. [3 marks]",
        "(c) Explain which activities could occur concurrently and why. [4 marks]",
    ])

    s.append(H1("Marking Scheme"))
    s.append(DTABLE(
        ["Section", "Content", "Marks"],
        [["A", "Short-answer questions (8 questions)", "20"],
         ["B", "Application questions (12 + 8)", "20"],
         ["C", "Case study — food delivery", "10"],
         ["", "TOTAL", "50"]],
        widths=[0.25 * DOC_W, 0.55 * DOC_W, 0.20 * DOC_W]))

    s.append(H1("Submission & Academic Integrity"))
    s += BUL([
        "Submit a typed document (or neatly handwritten, as directed by your lecturer).",
        "This assignment is individual work. Plagiarism or copying will attract a penalty under university regulations.",
        "State-machine diagrams must use correct UML notation — initial state, states, labelled transitions, guards, final state.",
        "Cite any sources you consult using the format used in the Week 7 module references.",
    ])

    return s


if __name__ == "__main__":
    print("Built:", build(CFG, story))
