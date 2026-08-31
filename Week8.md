BICT 3202 — OBJECT-ORIENTED ANALYSIS AND DESIGN

WEEK 8: OBJECT-ORIENTED ANALYSIS — BEHAVIOURAL MODELLING

Programme: BSc in Information Communication and Technology
Year of Study: 3
Course Code: BICT 3202
Week: 8 of 16
Lectures: 2 hours
Tutorial: 1 hour
Practical: 1 hour
Independent Learning: 10 hours


---

1. Where Week 8 Fits in the Module

We are now at Week 8, and yes, this follows directly from Week 7.

The progression is important:

WEEK 4–6
OBJECT MODELLING
"What things exist?"
        ↓
WEEK 7
DYNAMIC MODELLING
"How do objects change state over time?"
        ↓
WEEK 8
BEHAVIOURAL MODELLING
"How do users and objects interact to accomplish tasks?"
        ↓
WEEK 9
UNIFIED SOFTWARE DEVELOPMENT PROCESS
"How do we organise the development process?"
        ↓
WEEK 10+
OBJECT-ORIENTED DESIGN
"How do we turn our analysis into a software design?"

This week is therefore not simply another collection of UML diagrams.

The major idea is:

> Behavioural modelling describes what the system does, how users interact with it, how objects communicate, and how activities flow to achieve a goal.



OMG describes UML as a standard for visualizing, specifying and documenting systems, including their structures and behaviours. 

The official UML 2.5.1 specification includes use cases, sequence diagrams, communication diagrams, activity diagrams and other behavioural/interaction constructs. 


---

2. Week 8 Topics from the Course Outline

The official outline gives us:

1. Use Cases


2. Use Case Diagrams


3. Interaction Diagrams


4. Sequence Diagrams


5. Collaboration Diagrams


6. Activity Diagrams


7. Full Analysis Documentation



We will cover every one of these.


---

3. Week 8 Learning Outcomes

By the end of this week, students should be able to:

1. Define behavioural modelling.


2. Explain why behavioural modelling is important in OOAD.


3. Define a use case.


4. Identify actors in a system.


5. Identify appropriate use cases from requirements.


6. Distinguish actors from users.


7. Construct a use case diagram.


8. Explain the system boundary.


9. Explain include relationships.


10. Explain extend relationships.


11. Explain use-case generalisation.


12. Write a detailed use-case specification.


13. Explain interaction diagrams.


14. Construct sequence diagrams.


15. Identify lifelines and messages.


16. Explain activation bars.


17. Explain synchronous and asynchronous messages at an introductory level.


18. Construct communication/collaboration diagrams.


19. Explain the difference between sequence and communication diagrams.


20. Construct activity diagrams.


21. Model decisions and alternative flows.


22. Model parallel/concurrent activities.


23. Use swimlanes.


24. Connect use cases, activity diagrams and interaction diagrams.


25. Produce coherent behavioural analysis documentation.




---

PART A — WHAT IS BEHAVIOURAL MODELLING?

4. Definition

Behavioural modelling is the process of representing how a system behaves in response to users, events, inputs and other objects.

In simple language:

> Behavioural modelling tells us what the system does and how things interact while the system is doing it.



For example, imagine a university e-learning system.

A student might:

Login
   ↓
Select course
   ↓
Open assignment
   ↓
Upload assignment
   ↓
Submit
   ↓
Receive confirmation

That is behaviour.


---

5. Why Do We Need Behavioural Models?

Suppose we tell a programmer:

> "Build a university registration system."



That statement is far too vague.

We need to know:

Who uses it?

What can students do?

What can lecturers do?

What can administrators do?

What happens when a student registers?

What happens when payment fails?

What happens when a course is full?

What happens when a student cancels registration?

What messages pass between objects?

Which activities happen in parallel?


Behavioural models help answer these questions.


---

6. The Behavioural Modelling Family

For this course, think about behavioural modelling as a family:

BEHAVIOURAL MODELLING
                         |
       ┌─────────────────┼──────────────────┐
       ↓                 ↓                  ↓
   USE CASES        INTERACTIONS        ACTIVITIES
       |                 |                  |
       ↓                 ↓                  ↓
Use Case Diagram   Sequence Diagram   Activity Diagram
                   Communication
                   Diagram

Each diagram answers a slightly different question.


---

7. What Question Does Each Diagram Answer?

This is very important for examinations.

Model	Main question

Use Case	What does the system provide to its users?
Use Case Diagram	Who interacts with the system and what do they do?
Sequence Diagram	Who sends what message to whom, and in what order?
Communication Diagram	Which objects communicate, and how are their messages organised?
Activity Diagram	What activities happen, in what workflow, including decisions and parallel activities?


Microsoft's UML guidance similarly describes sequence diagrams as showing participants and events in time sequence, activity diagrams as modelling internal behaviour/flow, use-case diagrams as describing user activities and motivations, and communication diagrams as showing interactions through sequenced messages. 


---

PART B — USE CASES

8. What Is a Use Case?

A use case describes a goal-oriented interaction between an actor and a system that produces a result of value to the actor.

In very simple terms:

> A use case describes something a user wants to accomplish using the system.



Examples:

Login
Register for Course
Make Payment
Withdraw Money
Place Order
Track Order
Generate Report
Submit Assignment
Book Appointment


---

9. The Important Question

When identifying a use case, ask:

> "What does the actor want to accomplish?"



For example:

A student says:

> "I want to register for a course."



The use case is:

Register for Course

Not:

Click Register Button

Why?

Because:

> "Register for Course" is the user's goal.



The button click is only one interface action.


---

10. Use Case Example: ATM

Consider an ATM.

A customer may want to:

Withdraw Cash
Check Balance
Deposit Money
Transfer Money
Change PIN

These are use cases.

The actor is:

Customer


---

11. Use Case vs Function

Students often confuse these.

Consider:

Withdraw Cash

This is a use case.

Inside the use case, the system may perform:

Read card
Validate PIN
Check balance
Check withdrawal limit
Dispense cash
Update account
Print receipt

These are activities/functions involved in achieving the goal.

So:

> Use case = user's goal.



> Functions/actions = steps used to achieve the goal.




---

12. What Is an Actor?

An actor is an external role that interacts with the system.

The actor is outside the system boundary.

Examples:

Student
Lecturer
Administrator
Customer
Bank
Payment Gateway
Email Service

An actor does not have to be a human.


---

13. Actor as a Role

Suppose one person is both:

Student
and
Teaching Assistant

In a particular interaction, what matters is the role being played.

Therefore:

> An actor represents a role played by something external to the system.




---

14. Human Actor

Example:

Student

interacts with:

University Registration System


---

15. Non-Human Actor

Suppose an online store uses a payment service.

Customer → Online Store → Payment Gateway

The Payment Gateway can be an actor because it is external to the system being modelled.

This is important:

> An actor is not necessarily a person.




---

PART C — USE CASE DIAGRAMS

16. What Is a Use Case Diagram?

A use case diagram provides a high-level view of:

actors;

use cases;

system boundary;

relationships between actors and use cases.


It answers:

> Who interacts with the system and what goals can they accomplish?



The UML specification defines a UseCase as a specification of behaviour used to capture system requirements, involving actors and the subject/system under consideration. 


---

17. Basic Notation

A simple actor:

O
  /|\
  / \
Student

A use case:

( Register for Course )

Association:

Student ───────── (Register for Course)


---

18. System Boundary

A system boundary is represented by a rectangle.

For example:

+------------------------------------------+
|       UNIVERSITY REGISTRATION SYSTEM     |
|                                          |
|    (Register for Course)                 |
|                                          |
|    (Drop Course)                         |
|                                          |
|    (View Timetable)                      |
|                                          |
|    (Pay Fees)                            |
|                                          |
+------------------------------------------+
        ↑
        |
     Student

The rectangle represents the system being analysed.

The actor is outside.

The use cases are inside.


---

19. Complete Example

Imagine:

> University Student Management System



Actors:

Student
Lecturer
Administrator
Payment Gateway

Use cases:

Login
Register Course
Drop Course
View Results
Submit Assignment
Enter Marks
Generate Reports
Make Payment

Conceptually:

Student
    |
    +------ (Login)
    |
    +------ (Register Course)
    |
    +------ (Drop Course)
    |
    +------ (View Results)
    |
    +------ (Make Payment)


 Lecturer
    |
    +------ (Login)
    |
    +------ (Enter Marks)


 Administrator
    |
    +------ (Generate Reports)


---

PART D — USE CASE RELATIONSHIPS

20. Why Do We Need Relationships?

A large system can have dozens or hundreds of use cases.

Some use cases share behaviour.

For example:

Register Student

and:

Register Lecturer

might both require:

Verify Identity

UML provides relationships to help model such situations.

Important relationships include:

1. Association


2. include


3. extend


4. Generalisation




---

21. Association

An association simply shows that an actor participates in a use case.

Example:

Student ───────── (Register Course)

Meaning:

> A Student participates in the Register Course use case.




---

22. include

An include relationship is used when one use case incorporates another behaviour as part of its execution.

Think:

> "This behaviour is always needed."



Example:

(Register Course)
       |
       | <<include>>
       ↓
(Authenticate Student)

Meaning:

> Register Course includes Authenticate Student.



In our simplified example, authentication is a required part of registration.


---

23. Real-Life Example of include

Suppose an online banking system has:

Withdraw Money
Transfer Money
Check Balance

Suppose each requires authentication.

We could model:

(Withdraw Money)
       |
       | <<include>>
       ↓
(Authenticate User)

(Transfer Money)
       |
       | <<include>>
       ↓
(Authenticate User)

The important idea is:

> The included use case represents behaviour that is reused as part of another use case.




---

24. extend

An extend relationship is different.

It represents additional behaviour that occurs under particular circumstances.

Think:

> "Sometimes this extra behaviour happens."



Example:

(Withdraw Cash)
       ^
       |
  <<extend>>
       |
(Report Suspicious Transaction)

The suspicious-transaction behaviour only happens when a condition is met.


---

25. include vs extend

This is an examination favourite.

include	extend

Reused behaviour	Additional/optional behaviour
Part of the base use case	Occurs under specified conditions
Think always required	Think sometimes added
Helps factor common behaviour	Helps model optional/exceptional behaviour


A simple memory trick:

> INCLUDE = "I need this as part of the job."



> EXTEND = "I might add this under a condition."




---

26. Generalisation

Generalisation means that a more specialised actor/use case inherits characteristics from a more general one.

For example:

User
                  △
                 / \
                /   \
               /     \
          Student   Lecturer

Both Student and Lecturer are specialised types of User.


---

PART E — USE CASE SPECIFICATIONS

27. Is the Diagram Enough?

No.

A use case diagram gives us a high-level view.

For serious analysis, we normally need a use-case specification.

A specification describes what happens inside the use case.


---

28. Example Use Case Specification

Use Case: Register for Course

Use Case ID: UC-01
Name: Register for Course
Primary Actor: Student

Goal

The student wants to register for an available course.

Preconditions

The student:

has a valid account;

is authenticated;

is eligible to register.


Main Success Scenario

1. Student selects Register for Course.


2. System displays available courses.


3. Student selects a course.


4. System checks prerequisites.


5. System checks course capacity.


6. System displays registration details.


7. Student confirms registration.


8. System creates the registration.


9. System updates the student's course list.


10. System displays confirmation.



Alternative Flow A — Course Full

At Step 5:

1. System determines that the course is full.


2. System informs the student.


3. System offers a waitlist option.


4. Student may join the waitlist.



Alternative Flow B — Prerequisite Missing

At Step 4:

1. System determines that the student has not met the prerequisite.


2. System informs the student.


3. Registration is not completed.



Postcondition

If successful:

> The student is registered for the selected course.




---

29. Why Use-Case Specifications Matter

Imagine telling a programmer only:

> "Build course registration."



They don't know:

what happens first;

what happens if the course is full;

what happens if payment fails;

what happens if prerequisites aren't met.


The detailed use-case specification captures these requirements.

This is why behavioural analysis connects requirements to later design work. Modern OOAD teaching also emphasizes using behavioural models to expose alternative and exception paths rather than modelling only the "happy path." 


---

PART F — INTERACTION DIAGRAMS

30. What Is an Interaction?

An interaction describes how participants communicate with one another by exchanging messages.

For example:

Student
   |
   | login()
   ↓
System
   |
   | validateCredentials()
   ↓
Database

There is an interaction among:

Student
System
Database


---

31. What Are Interaction Diagrams?

Interaction diagrams model communication among objects/participants.

In this module, focus on:

Sequence Diagram
Communication/Collaboration Diagram

UML 2.5.1 explicitly includes sequence and communication diagrams as interaction diagram types. 


---

PART G — SEQUENCE DIAGRAMS

32. What Is a Sequence Diagram?

A sequence diagram shows interactions between participants in time order.

Simple definition:

> A sequence diagram shows who communicates with whom, what messages are exchanged, and the order in which those messages occur.



This is one of the most useful diagrams in OOAD.

Microsoft describes sequence diagrams as showing participating actors/objects and the events they generate arranged in time sequence. 


---

33. Why Is "Sequence" Important?

Look at:

Student → System: Login
System → Database: Validate
Database → System: Valid
System → Student: Login successful

The order matters.

You can't normally:

System → Student: Login successful

before validating the credentials.


---

34. Sequence Diagram Components

Students need to know:

1. Actor


2. Object


3. Lifeline


4. Activation bar


5. Message


6. Return message


7. Time/order


8. Combined fragments such as alt, opt, loop at an introductory level




---

35. Lifeline

A lifeline represents a participant in an interaction.

Example:

Student
   |
   |
   |
   |

The vertical dashed line represents the participant's existence during the interaction.


---

36. Activation Bar

An activation bar shows a period during which a participant is performing an operation.

Conceptually:

Student          System
  |                |
  | login()        |
  |--------------->|
  |                | ███
  |                | ███
  |                | ███
  |                |


---

37. Messages

A message represents communication from one participant to another.

For example:

Student → System
login()

Then:

System → Database
validateCredentials()


---

38. Complete Login Example

Student        System        Database
   |              |              |
   | login()      |              |
   |------------->|              |
   |              | validate()   |
   |              |------------->|
   |              |              |
   |              |   valid      |
   |              |<-------------|
   | confirmation |              |
   |<-------------|              |
   |              |              |

Read it from top to bottom.

That represents time progressing downward.


---

39. How to Read a Sequence Diagram

Always ask:

Who starts the interaction?

Student

Who receives the first message?

System

What happens next?

System validates credentials.

Who performs the validation?

Database

What does the system return?

Login confirmation.

This approach helps students understand diagrams rather than merely memorising symbols.


---

40. Sequence Diagram for Course Registration

Let's make it more realistic.

Participants:

Student
Registration UI
Registration Controller
Course Database

Interaction:

Student
   |
   | selectCourse()
   ↓
Registration UI
   |
   | submitRegistration()
   ↓
Registration Controller
   |
   | checkAvailability()
   ↓
Course Database
   |
   | available
   ↓
Registration Controller
   |
   | createRegistration()
   ↓
Course Database
   |
   | confirmation
   ↓
Registration Controller
   |
   | displayConfirmation()
   ↓
Registration UI
   |
   | confirmation
   ↓
Student

Notice something important.

We are beginning to move from:

> analysis of requirements



toward:

> understanding which software objects/components will participate.




---

PART H — ALTERNATIVE SEQUENCES

41. What If Something Goes Wrong?

Real systems do not always follow the happy path.

Suppose the course is full.

Our sequence could include:

Student → UI: register()
UI → Controller: submitRegistration()
Controller → Database: checkAvailability()
Database → Controller: FULL
Controller → UI: showCourseFull()
UI → Student: displayMessage()

This is an alternative scenario.


---

42. alt Fragment

Sequence diagrams can represent alternatives.

Conceptually:

+---------------------------------------+
| alt                                   |
|                                       |
| [course available]                    |
|    Controller → DB: register()        |
|                                       |
| [course full]                         |
|    Controller → UI: showFull()        |
|                                       |
+---------------------------------------+

The important idea:

> Only the branch whose guard is true is executed.




---

43. loop Fragment

Suppose a system processes several students.

+-----------------------------------+
| loop [for each student]           |
|                                   |
| System → Student: sendResult()    |
|                                   |
+-----------------------------------+

The behaviour repeats.


---

44. opt Fragment

Suppose sending an SMS is optional.

+----------------------------------+
| opt [SMS notification enabled]   |
|                                  |
| System → SMS Service: sendSMS()  |
|                                  |
+----------------------------------+

The behaviour occurs only if the condition is true.


---

PART I — COMMUNICATION/COLLABORATION DIAGRAMS

45. What Is a Communication Diagram?

The course outline uses the older term:

> Collaboration Diagram



In UML 2.x, the corresponding standard term is generally:

> Communication Diagram



This is worth teaching students because they may encounter both names in textbooks, lecture notes or software.

The UML 2.5.1 specification contains a dedicated section for communication diagrams and their graphical elements. 


---

46. What Does a Communication Diagram Show?

A communication diagram focuses on:

> Which objects communicate with each other and what messages they exchange.



It does not emphasize vertical time progression as strongly as a sequence diagram.


---

47. Example

Suppose:

Student

interacts with:

Registration System

which interacts with:

Course Database

A communication diagram might conceptually look like:

Student
           |
      1: register()
           |
           ↓
   Registration System
           |
     2: checkCourse()
           |
           ↓
     Course Database
           |
     3: availability
           |
           ↓
   Registration System
           |
     4: confirmation
           |
           ↓
        Student

The numbers:

1
2
3
4

help show message order.


---

48. Sequence vs Communication Diagram

This is another important examination question.

Sequence Diagram	Communication Diagram

Emphasises time	Emphasises object relationships
Messages arranged vertically	Objects arranged around the interaction
Easy to see chronological order	Easy to see who communicates with whom
Lifelines are prominent	Links between objects are prominent


The same interaction can often be represented using either form, but each gives the reader a different visual emphasis.


---

PART J — ACTIVITY DIAGRAMS

49. What Is an Activity Diagram?

An activity diagram models a workflow or flow of activities.

In simple English:

> It shows the steps involved in carrying out a process, including decisions and parallel activities.



Microsoft describes activity diagrams as useful for representing internal behaviour and flow driven by actions. 


---

50. Example: Online Shopping

Suppose a customer buys a product.

The workflow is:

Start
  ↓
Select Product
  ↓
Add to Cart
  ↓
Checkout
  ↓
Make Payment
  ↓
Payment Successful?
  ↓
  Yes
  ↓
Create Order
  ↓
Send Confirmation
  ↓
End

This is naturally represented using an activity diagram.


---

51. Activity Diagram Notation

Important elements include:

Initial node

●

Action

┌──────────────────┐
│ Select Product   │
└──────────────────┘

Decision

◇

Merge

◇

Final node

◎

Flow

──────→

Fork/Join

Usually represented by a thick bar.


---

52. Simple Activity Diagram

●
             |
             ↓
     [Select Product]
             |
             ↓
       [Add to Cart]
             |
             ↓
         [Checkout]
             |
             ↓
       [Make Payment]
             |
             ↓
            ◇
        /         \
 [Successful]    [Failed]
      |              |
      ↓              ↓
[Create Order]  [Show Error]
      |              |
      ↓              |
[Send Receipt] ←─────┘
      |
      ↓
      ◎


---

53. Decision Node

The diamond represents a decision.

For example:

Payment
             |
             ↓
             ◇
           /   \
 [successful] [failed]
      ↓          ↓
   Continue     Error

The outgoing paths normally have guard conditions.

For example:

[balance sufficient]

and:

[balance insufficient]


---

PART K — CONCURRENCY IN ACTIVITY DIAGRAMS

54. Fork

A fork splits one flow into multiple concurrent flows.

For example, after an order is confirmed:

[Order Confirmed]
                     |
                     ↓
                ═════════
                 /      \
                ↓        ↓
        [Prepare Food] [Assign Driver]
                |        |
                ↓        ↓
                 \      /
                ═════════
                     |
                     ↓
               [Deliver Order]

The thick bars represent fork/join concepts.


---

55. Why Is This Useful?

Suppose an online shop receives an order.

After payment:

Update inventory
+
Prepare invoice
+
Notify warehouse
+
Send customer confirmation

Some of these tasks can occur independently.

Activity diagrams can make this concurrency visible.


---

PART L — SWIMLANES

56. What Is a Swimlane?

A swimlane divides an activity diagram according to responsibility.

For example:

+----------------------+----------------------+
|       Student        |       System         |
+----------------------+----------------------+
|                      |                      |
| Select course        |                      |
|--------------------->|                      |
|                      | Check prerequisites  |
|                      |----------------------|
|                      |                      |
|                      | Check availability   |
|                      |----------------------|
| Confirm              |                      |
|--------------------->| Create registration  |
|                      |----------------------|
|                      | Display confirmation |
+----------------------+----------------------+

This answers:

> Who is responsible for performing each activity?




---

57. Why Swimlanes Matter

Without swimlanes:

Check prerequisites
Confirm registration
Update database
Select course

we might not know who performs what.

With swimlanes:

Student:
Select course
Confirm

System:
Check prerequisites
Update database
Display confirmation

Responsibilities become clearer.


---

PART M — USE CASE → ACTIVITY → SEQUENCE

58. How These Models Work Together

This is perhaps the most important concept of Week 8.

Suppose our requirement is:

> "A student should be able to register for a course."



We start with a use case:

Register for Course

Then we can model the workflow using an activity diagram:

Select course
      ↓
Check prerequisite
      ↓
Check availability
      ↓
Confirm
      ↓
Create registration

Then we can model the object interactions using a sequence diagram:

Student
   ↓
Registration UI
   ↓
Registration Controller
   ↓
Course Database

So:

REQUIREMENT
                  ↓
              USE CASE
                  ↓
          ACTIVITY DIAGRAM
                  ↓
         SEQUENCE DIAGRAM
                  ↓
        OBJECT RESPONSIBILITIES
                  ↓
             DESIGN

This is a very useful way to teach students how behavioural models fit together.

Research on use-case modelling similarly describes use cases being elaborated through interaction models, activity models and state models to describe behaviour at increasing levels of detail. 


---

59. A Full Example

Let's take:

> Online Student Assignment Submission System



Step 1 — Use Case

Student
   |
   +---- (Submit Assignment)


---

Step 2 — Use Case Specification

Main flow

1. Student logs in.


2. Student opens course.


3. Student selects assignment.


4. Student uploads file.


5. System validates file.


6. Student clicks Submit.


7. System records submission.


8. System displays confirmation.



Alternative flow

If file type is invalid:

System rejects file
        ↓
Student receives error
        ↓
Student uploads another file


---

60. Step 3 — Activity Diagram

●
             |
             ↓
        [Login]
             |
             ↓
      [Open Course]
             |
             ↓
     [Select Assignment]
             |
             ↓
      [Upload File]
             |
             ↓
            ◇
        /       \
 [Valid File] [Invalid]
      |           |
      ↓           ↓
   [Submit]   [Show Error]
      |
      ↓
[Record Submission]
      |
      ↓
[Display Confirmation]
      |
      ↓
      ◎


---

61. Step 4 — Sequence Diagram

Participants:

Student
Web Interface
Assignment Controller
Database

Interaction:

Student       Web UI       Controller       Database
   |             |              |               |
   | upload()    |              |               |
   |------------>|              |               |
   |             | submit()     |               |
   |             |------------->|               |
   |             |              | validate()    |
   |             |              |-------------->|
   |             |              | valid         |
   |             |              |<--------------|
   |             |              | save()        |
   |             |              |-------------->|
   |             | confirmation  |               |
   |             |<-------------|               |
   | confirmation|              |               |
   |<------------|              |               |

Now we have:

Use Case
   +
Activity Diagram
   +
Sequence Diagram

All describing the same requirement from different perspectives.


---

PART N — FULL ANALYSIS DOCUMENTATION

62. What Is Analysis Documentation?

Analysis documentation is the collection of models and written descriptions that explain what the proposed system must do.

It can contain:

problem statement;

business requirements;

functional requirements;

non-functional requirements;

actors;

use cases;

use-case diagrams;

use-case specifications;

activity diagrams;

sequence diagrams;

communication diagrams;

class diagrams;

state-machine diagrams;

assumptions;

constraints;

business rules;

glossary.



---

63. Why Documentation Matters

Imagine a project with:

Client
Analyst
Designer
Programmer
Tester
Project Manager

Everyone needs to understand the same system.

Models provide a common language.

For example:

Client:
"I want students to register courses."

Analyst:
"Register Course is UC-03."

Designer:
"Here is the sequence diagram."

Programmer:
"These are the participating objects."

Tester:
"These are the scenarios I need to test."

Therefore, analysis documentation creates traceability.


---

64. Traceability

A useful concept for students is:

Requirement
    ↓
Use Case
    ↓
Activity / Scenario
    ↓
Sequence Diagram
    ↓
Classes / Objects
    ↓
Design
    ↓
Test Cases

For example:

REQ-05
Student must register for courses.
        ↓
UC-05
Register Course
        ↓
Activity Model
Registration workflow
        ↓
Sequence Model
Student → UI → Controller → Database
        ↓
Design
Registration classes/services
        ↓
Testing
Successful/failed registration tests

This demonstrates why behavioural modelling is not just "drawing diagrams."


---

PART O — COMMON STUDENT CONFUSIONS

65. Confusion 1: Use Case vs Use Case Diagram

They are not the same.

Use Case

A description of one goal/behaviour.

Register Course

Use Case Diagram

A visual representation of actors, use cases and their relationships.

Student ─── (Register Course)


---

66. Confusion 2: Use Case vs Activity Diagram

Use Case

Answers:

> What goal does the actor want to accomplish?



Activity Diagram

Answers:

> What workflow happens while accomplishing that goal?




---

67. Confusion 3: Activity vs Sequence

Activity Diagram

Focus:

> Workflow/process



Example:

Check stock
↓
Process payment
↓
Create order

Sequence Diagram

Focus:

> Messages between participants over time



Example:

Customer → OrderUI: checkout()
OrderUI → PaymentService: pay()
PaymentService → Bank: authorize()


---

68. Confusion 4: Sequence vs Communication

Both can represent similar interactions.

But:

Sequence Diagram
→ emphasises TIME and MESSAGE ORDER

while:

Communication Diagram
→ emphasises PARTICIPATING OBJECTS and THEIR LINKS


---

69. Confusion 5: Actor vs Class

An actor is:

> External to the system being modelled.



A class is:

> A type/structure inside the model/system domain.



For example:

Student → Actor
StudentAccount → Class

However, context matters: the same real-world entity can be represented differently depending on the system boundary and modelling purpose.


---

PART P — WEEK 8 PRACTICAL

70. Practical Assignment

Students will model:

> University Online Course Registration System



Actors

Identify at least:

Student
Lecturer
Administrator
Payment Gateway

Use Cases

Identify at least:

Login
Register Course
Drop Course
View Timetable
Make Payment
View Results
Enter Marks
Generate Report


---

71. Practical Task 1 — Use Case Diagram

Students must create a complete use-case diagram containing:

system boundary;

at least 4 actors;

at least 8 use cases;

associations;

at least one include;

at least one extend;

at least one generalisation where justified.



---

72. Practical Task 2 — Use Case Specification

Students select:

> Register Course



and produce a complete specification containing:

use-case ID;

name;

primary actor;

goal;

preconditions;

postconditions;

main success scenario;

at least two alternative flows;

exception conditions.



---

73. Practical Task 3 — Activity Diagram

Create an activity diagram for:

> Register Course



It must include:

initial node;

actions;

decision;

at least two alternative paths;

final node;

swimlanes.



---

74. Practical Task 4 — Sequence Diagram

Create a sequence diagram for the successful registration scenario.

Participants should include:

Student
Registration Interface
Registration Controller
Course Database

At least 8 messages should be shown.


---

75. Practical Task 5 — Communication Diagram

Represent the same registration scenario as a communication diagram.

Students should number the messages:

1:
2:
3:
4:
...

Then compare it with their sequence diagram.


---

PART Q — TUTORIAL ACTIVITIES

76. Tutorial Question 1

Consider:

> ATM System



Identify:

Actors

At least three.

Use Cases

At least six.

External systems

At least one.


---

77. Tutorial Question 2

Explain the difference between:

1. include


2. extend


3. generalisation



Give one practical example for each.


---

78. Tutorial Question 3

Given:

Customer places order
System checks stock
System processes payment
System creates order
System sends confirmation

Ask students:

> Which UML behavioural model would best represent the overall workflow?



Expected:

> Activity diagram.



Then ask:

> Which model would best represent the messages between Customer, Order System, Payment Service and Inventory System?



Expected:

> Sequence diagram.




---

79. Tutorial Question 4

Explain:

> Why should a sequence diagram normally be developed for a specific scenario/use case rather than attempting to model the entire system in one enormous diagram?



Expected reasoning:

Because a sequence diagram is intended to show a particular interaction scenario, and an enormous diagram becomes difficult to read, analyse and maintain. Multiple focused diagrams can represent different main, alternative and exception scenarios more clearly. This aligns with practical behavioural-modelling guidance emphasizing simple scenario-specific interaction diagrams. 


---

PART R — EXAMINATION QUESTIONS

80. Question 1 — Definitions

Define:

a. Behavioural modelling
b. Use case
c. Actor
d. Interaction diagram
e. Sequence diagram
f. Communication diagram
g. Activity diagram

[14 marks]


---

81. Question 2 — Comparison

Differentiate between:

a. Use case and use case diagram

b. Activity diagram and sequence diagram

c. Sequence diagram and communication diagram

d. include and extend

[20 marks]


---

82. Question 3 — Design

A university wants to develop an online examination system.

Students should be able to:

log in;

view available examinations;

start an examination;

answer questions;

submit answers;

receive confirmation.


Lecturers should be able to:

create examinations;

enter questions;

view submissions;

generate results.


Required:

1. Identify the actors.


2. Identify the use cases.


3. Draw a use-case diagram.


4. Write a use-case specification for Start Examination.


5. Draw an activity diagram for Submit Examination.


6. Draw a sequence diagram for Start Examination.




---

PART S — WEEK 8 INDEPENDENT LEARNING

Students have 10 hours of independent learning.

Activity 1 — Use Case Analysis

Choose one:

mobile banking;

e-learning;

hospital management;

online shopping;

hotel booking.


Identify:

5+ actors
10+ use cases
3+ relationships


---

Activity 2 — Detailed Use Case

Select one use case and write:

Use Case ID
Name
Actor
Goal
Preconditions
Main Flow
Alternative Flow
Exception Flow
Postconditions


---

Activity 3 — Behavioural Models

For the selected use case, produce:

1. Use-case diagram
2. Activity diagram
3. Sequence diagram
4. Communication diagram


---

Activity 4 — Written Analysis

Write 700–1,000 words answering:

> How do use-case, activity, sequence and communication diagrams complement one another during object-oriented analysis?




---

PART T — WEEK 8 REVISION TABLE

Concept	Meaning	Simple Example

Behavioural modelling	Models system behaviour	Registration process
Use case	User/system goal	Register Course
Actor	External role	Student
System boundary	Defines system scope	Registration System rectangle
Association	Actor participates in use case	Student — Register
include	Required/reused behaviour	Register → Authenticate
extend	Conditional additional behaviour	Withdraw → Report Suspicious Activity
Generalisation	Specialised/general relationship	Student → User
Sequence diagram	Messages in time order	Student → System → DB
Lifeline	Participant over interaction	Student vertical line
Message	Communication	login()
Communication diagram	Objects + messages	1: login, 2: validate
Activity diagram	Workflow	Register → Pay → Confirm
Decision	Chooses a path	Payment successful?
Fork	Starts parallel flows	Prepare + Notify
Join	Synchronises parallel flows	Both complete
Swimlane	Shows responsibility	Student/System
Use-case specification	Detailed textual behaviour	Register Course document



---

83. THE BIG PICTURE STUDENTS SHOULD REMEMBER

Give students this mental model:

USER NEED
                       ↓
              "I want to register."
                       ↓
                   USE CASE
                Register Course
                       ↓
             USE CASE DIAGRAM
              Who does what?
                       ↓
              ACTIVITY DIAGRAM
             What steps happen?
                       ↓
             SEQUENCE DIAGRAM
         Who talks to whom, and when?
                       ↓
        COMMUNICATION DIAGRAM
        Which objects collaborate?
                       ↓
             ANALYSIS MODEL
                       ↓
                 DESIGN

This is much better than teaching students UML diagrams as isolated symbols.


---

84. Week 8 Final Takeaway

The central idea of Week 8 is:

> A system is not just a collection of classes. It is a collection of behaviours performed by users and software objects working together to achieve goals.



Students should therefore be able to move from:

"I need a registration system."

to:

Who?
  ↓
Student

What goal?
  ↓
Register Course

What workflow?
  ↓
Activity Diagram

Which objects interact?
  ↓
Sequence Diagram

How are those objects connected during the interaction?
  ↓
Communication Diagram

What does the complete requirement say?
  ↓
Full Analysis Documentation

The official UML 2.5.1 specification is still the key normative reference for these UML constructs; OMG lists Version 2.5.1 as the formal specification adopted in December 2017 and provides both the normative specification and machine-readable UML artefacts. 


---

References

Primary UML Standard

Object Management Group (OMG). (2017). OMG Unified Modeling Language (OMG UML), Version 2.5.1. OMG. 

[Official OMG UML Specification and Resources](https://www.omg.org/spec/UML?utm_source=chatgpt.com)

Additional Current Reference

Object Management Group. Unified Modeling Language (UML) — official UML resources, specifications and guidance. 

[OMG Unified Modeling Language (UML)](https://www.omg.org/uml/?utm_source=chatgpt.com)

Additional Behavioural Modelling References

Microsoft Support. UML diagrams in Visio — overview of sequence, activity, state-machine, use-case and communication diagrams. 

NILUS Consulting. (2026). Object-Oriented Analysis and Design Using UML — Behavioral Modeling with Sequence, Activity, and State Diagrams. 

Prescribed Texts from the Module Outline

Mach, E. (2019). Object Oriented Analysis & Design Cookbook: Introduction to Practical System Modeling.

Reddy, V., & Korra, S. (2018). Object-Oriented Analysis and Design Using UML.

The Art of Service. (2021). Object Oriented Analysis and Design: A Complete Guide.


Recommended Texts

Wixom, B., & Dennis, A. (2018). Systems Analysis and Design.

Blokdyk, G. (2021). Object-Oriented Analysis and Design Standard Requirements.

Wixom, B., & Dennis, A. (2020). Systems Analysis and Design: An Object-Oriented Approach with UML.


**Week 9 will move from modelling individual behaviours to the broader development process: The Unified Software Development Process (USDP/Unified Process) — including its characteristics, phases, iterations, workflows, artefacts, reuse, concurrency, generalisation and inheritance.**
