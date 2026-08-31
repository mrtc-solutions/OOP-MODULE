BICT 3202 — OBJECT-ORIENTED ANALYSIS AND DESIGN

WEEK 12: INTEGRATED OBJECT-ORIENTED MODELLING AND DESIGN

Programme: BSc in Information Communication and Technology
Year: 3
Course Code: BICT 3202
Week: 12 of 16
Lecture: 2 hours
Tutorial: 1 hour
Practical: 1 hour
Independent Learning: 10 hours
Credits: 10


---

1. WHERE WEEK 12 FITS IN THE COURSE

We need to be very clear about the progression.

In Week 10, we introduced Object-Oriented Design.

We asked:

> What does it mean to move from analysis into design?



In Week 11, we went deeper into design refinement.

We asked:

> How do we take our analysis models and make them detailed enough for implementation?



Now in Week 12, we take the next step:

> How do we bring all these different models together into ONE coherent system design?



This is important because a real OOAD project does not normally consist of a class diagram sitting separately from a use-case diagram, sequence diagram and state diagram.

They should describe the same system from different perspectives.

UML is specifically intended for visualising, specifying and documenting software and systems, and the current formal UML specification listed by OMG is UML 2.5.1. 


---

2. WEEK 12 TOPICS

This week covers:

1. Meaning of integrated modelling


2. Why models must be consistent


3. The relationship between UML models


4. From requirements to an integrated design


5. Use-case model


6. Behavioural model


7. Dynamic model


8. Object/class model


9. Interaction model


10. State model


11. Activity model


12. Component-level thinking


13. Architecture and packages


14. Model consistency


15. Detecting contradictions between models


16. Traceability


17. Design validation


18. Complete case study


19. Practical UML integration exercise




---

PART A — WHAT IS INTEGRATED MODELLING?

3. Meaning of Integrated Modelling

Let's start with a simple example.

Imagine we are building a house.

We might have:

an architectural drawing;

an electrical plan;

a plumbing plan;

a structural plan.


Each drawing shows something different.

But they must describe the same house.

You cannot have:

> Architectural drawing: 3 bedrooms



while:

> Electrical drawing: 5 bedrooms



and:

> Plumbing drawing: 2 bedrooms.



😂

The drawings would contradict each other.

Software models work in much the same way.


---

4. Different UML Models Describe Different Views

For example:

Use-case model

Answers:

> What does the user want to accomplish?



Class model

Answers:

> What objects/classes make up the system?



Sequence diagram

Answers:

> How do objects communicate to accomplish a task?



State machine

Answers:

> How does an object change state?



Activity diagram

Answers:

> What activities and decisions occur in a process?



Component/deployment views

Answers:

> How is the software organised and deployed?



UML itself groups structural modelling and behavioural modelling into different parts of its specification. 


---

5. The Big Picture

Students should understand the following:

REQUIREMENTS
                         |
                         ↓
                  USE-CASE MODEL
                         |
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
    OBJECT MODEL    DYNAMIC MODEL   BEHAVIOURAL MODEL
          |              |              |
          ↓              ↓              ↓
    CLASS DIAGRAM    STATE MODEL    SEQUENCE/
                                   ACTIVITY MODEL
          \              |              /
           \             |             /
            └────────────┼────────────┘
                         ↓
                 INTEGRATED DESIGN
                         |
                         ↓
                  IMPLEMENTATION

This is the central idea of Week 12.


---

PART B — WHY DO MODELS NEED TO AGREE?

6. Model Consistency

Suppose the requirement says:

> "A student can register for a course."



The use-case diagram contains:

Student → Register for Course

Good.

But our class diagram contains only:

Student
Teacher
Department

There is no:

Course
Registration

We have a problem.


---

7. Why Is This a Problem?

The use-case model says the system must support course registration.

The class model doesn't contain obvious objects needed to support it.

Therefore:

> The models are inconsistent or incomplete.



This is why OOAD isn't simply about drawing diagrams.

The diagrams must collectively tell a coherent story.


---

PART C — A COMMON CASE STUDY

To make this week easy to understand, we will use one system throughout the lecture.

8. Case Study: University Course Registration System

Imagine a university wants to develop an online course registration system.

The system should allow students to:

1. log in;


2. view available courses;


3. register for a course;


4. drop a course;


5. view their registered courses.



The system should also:

check course capacity;

check prerequisites;

store registration information;

notify the student when registration succeeds.



---

9. Step 1 — Identify the Actor

Who interacts with the system?

Student

Other possible actors could eventually include:

Administrator
Lecturer
Finance Officer

But let's initially concentrate on the student.


---

10. Step 2 — Identify Use Cases

The student needs to:

Login
View Courses
Register for Course
Drop Course
View Registered Courses

So:

UNIVERSITY REGISTRATION SYSTEM

Student ─────── Login

Student ─────── View Courses

Student ─────── Register for Course

Student ─────── Drop Course

Student ─────── View Registered Courses

This is our use-case view.


---

PART D — CONNECTING THE USE CASE TO CLASSES

11. What Classes Are Needed?

Now ask:

> "What things must exist in the software for these use cases to work?"



Possible domain classes:

Student
Course
Registration

And design/service classes:

AuthenticationService
RegistrationService
CourseRepository
RegistrationRepository


---

12. Initial Class Model

A simplified domain model could be:

+----------------+
| Student        |
+----------------+
| studentId      |
| name           |
| email          |
+----------------+

        |
        | registers
        |
        ↓

+----------------+
| Registration   |
+----------------+
| registrationId |
| date           |
| status         |
+----------------+

        |
        | for
        |
        ↓

+----------------+
| Course         |
+----------------+
| courseCode     |
| title          |
| credits        |
| capacity       |
+----------------+

Now we have a structural explanation of the system.


---

PART E — RELATIONSHIP BETWEEN MODELS

13. Use Case → Classes

Take:

> Register for Course



Which classes support it?

Potentially:

Student
Course
Registration
RegistrationService

So we can trace:

Register for Course
        ↓
RegistrationService
        ↓
Student
        ↓
Course
        ↓
Registration

This is an example of model traceability.


---

14. What Is Traceability?

Traceability means being able to answer:

> "Where did this design element come from?"



and:

> "Which requirement does this design element support?"



For example:

Requirement R01
"Students can register for courses."
             ↓
Use Case
"Register for Course"
             ↓
Sequence Diagram
"Registration interaction"
             ↓
Classes
Student
Course
Registration
RegistrationService
             ↓
Operations
register()
checkCapacity()
checkPrerequisite()

That is a traceable design.


---

PART F — SEQUENCE DIAGRAM

15. Why Do We Need a Sequence Diagram?

Our use case says:

> Student registers for a course.



But it doesn't tell us exactly how the interaction happens.

The sequence diagram provides that detail.


---

16. Registration Sequence

Conceptually:

Student       RegistrationService       Course       Registration
   |                  |                    |               |
   | register(course) |                    |               |
   |----------------->|                    |               |
   |                  | checkCapacity()    |               |
   |                  |------------------->|               |
   |                  |<-------------------|               |
   |                  |                    |               |
   |                  | checkPrerequisite()|               |
   |                  |------------------->|               |
   |                  |<-------------------|               |
   |                  |                    |               |
   |                  | createRegistration()               |
   |                  |----------------------------------->|
   |                  |                    |               |
   |<-----------------| confirmation       |               |

Now we have behaviour.


---

17. Checking Consistency

Look at the sequence diagram.

It uses:

Student
RegistrationService
Course
Registration

Therefore, those elements should exist in the relevant class model.

If the sequence diagram suddenly says:

PaymentProcessor

but our system has no payment requirement, we should ask:

> "Why is PaymentProcessor here?"



Maybe:

the requirement was forgotten;

the class is unnecessary;

or the model needs updating.


That's model validation.


---

PART G — STATE MODELLING

18. Why Do We Need a State Model?

Consider a Registration.

A registration isn't always in the same condition.

It may go through:

Requested
Validated
Confirmed
Cancelled
Rejected

So:

Register
                   |
                   ↓
              [REQUESTED]
                   |
              validation
                   |
            ┌──────┴───────┐
            ↓              ↓
        Valid           Invalid
            |              |
            ↓              ↓
       [CONFIRMED]     [REJECTED]
            |
        cancellation
            ↓
       [CANCELLED]

This is the dynamic view.


---

19. Why Is This Useful?

Suppose someone says:

> "A cancelled registration can become confirmed again."



Is that allowed?

Our state model forces us to make the decision.

Maybe:

[CONFIRMED]
      ↓
[CANCELLED]

is final.

Or perhaps the business allows:

[CANCELLED]
      ↓
[REQUESTED]
      ↓
[CONFIRMED]

The model makes the business rule explicit.


---

PART H — ACTIVITY DIAGRAM

20. Activity Diagram vs Sequence Diagram

Students often confuse these.

Sequence diagram

Focuses on:

> Who communicates with whom, and in what order?



Activity diagram

Focuses on:

> What activities occur in a workflow?




---

21. Registration Activity

START
  |
  ↓
Student logs in
  |
  ↓
Display courses
  |
  ↓
Student selects course
  |
  ↓
Check prerequisites
  |
  ↓
Prerequisites satisfied?
  |
  ├── NO → Display error → END
  |
  └── YES
        |
        ↓
   Check capacity
        |
        ↓
   Space available?
        |
     ┌──┴───┐
     NO     YES
     |       |
     ↓       ↓
  Reject   Create registration
            |
            ↓
        Confirm registration
            |
            ↓
           END


---

22. Comparing the Three Behavioural Views

Model	Main question

Use case	What does the actor want to accomplish?
Sequence	How do objects interact over time?
Activity	What workflow/activities take place?
State machine	How does an object change state?


This distinction is extremely important.


---

PART I — INTEGRATING THE FOUR MODELS

23. Putting Everything Together

For:

> Register for Course



we now have:

Use case

Student → Register for Course

Activity

Login
 ↓
Select course
 ↓
Check prerequisite
 ↓
Check capacity
 ↓
Create registration
 ↓
Confirm

Sequence

Student
 ↓
RegistrationService
 ↓
Course
 ↓
Registration

State

Requested
   ↓
Validated
   ↓
Confirmed

Class model

Student
Course
Registration
RegistrationService

These models now describe the same functionality from different viewpoints.


---

PART J — MODEL CONSISTENCY CHECKING

24. What Is a Consistency Check?

A consistency check asks:

> "Do all our models agree?"



We can create a simple checklist.


---

25. Consistency Checklist

Check 1 — Actors

Does every important actor in the requirements/use cases appear appropriately elsewhere?


---

Check 2 — Use cases

Does every important use case have supporting behaviour?


---

Check 3 — Classes

Do the classes required by interactions exist?


---

Check 4 — Operations

If a sequence diagram says:

course.checkCapacity()

does Course have a corresponding operation in the design?


---

Check 5 — Attributes

If a requirement needs:

> course capacity



does Course have something representing capacity?


---

Check 6 — States

If the business process distinguishes:

Pending
Approved
Rejected

does the relevant object/state model represent them?


---

Check 7 — Relationships

If the system says:

> A student registers for many courses.



Does the class model represent the appropriate multiplicity?

For example:

Student 1 -------- 0..* Registration
Course  1 -------- 0..* Registration


---

PART K — MULTIPLICITY

26. Why Multiplicity Matters

Suppose:

Student -------- Course

That's not enough.

How many courses can one student take?

Maybe:

1 Student → 0..* Courses

How many students can take one course?

Maybe:

1 Course → 0..* Students

But if Registration is the entity representing the relationship, we may model:

Student 1 -------- 0..* Registration
Course  1 -------- 0..* Registration

This gives us much more precise information.


---

27. Common Multiplicity Symbols

Symbol	Meaning

1	Exactly one
0..1	Zero or one
0..*	Zero or many
1..*	One or many
2..5	Between two and five



---

PART L — PACKAGES AND ORGANISING A LARGE MODEL

28. Why Do We Need Packages?

Imagine a large university system has:

Student
Course
Registration
Payment
Invoice
Lecturer
Department
LibraryBook
Borrowing
Notification
User
Role
Permission
Report

Putting everything into one giant diagram becomes difficult to understand.

We can group related elements.


---

29. Example Package Structure

University System
│
├── Authentication
│   ├── User
│   ├── Role
│   └── Permission
│
├── Academic
│   ├── Student
│   ├── Course
│   ├── Programme
│   └── Registration
│
├── Finance
│   ├── Payment
│   └── Invoice
│
├── Library
│   ├── Book
│   └── Borrowing
│
└── Notification
    ├── Email
    └── SMS

This makes the model easier to navigate.

UML supports package and other structural modelling constructs as part of its standard modelling language. 


---

PART M — ARCHITECTURAL INTEGRATION

30. Moving Beyond Individual Classes

At this point we should start thinking:

> "How will these classes actually be organised into a software system?"



One useful approach is layered architecture.

+--------------------------------------+
| PRESENTATION                         |
| Web / Mobile / Desktop               |
+--------------------------------------+
                  ↓
+--------------------------------------+
| APPLICATION                          |
| RegistrationService                  |
| AuthenticationService                |
+--------------------------------------+
                  ↓
+--------------------------------------+
| DOMAIN                               |
| Student | Course | Registration      |
+--------------------------------------+
                  ↓
+--------------------------------------+
| DATA ACCESS                          |
| StudentRepository                    |
| CourseRepository                     |
| RegistrationRepository               |
+--------------------------------------+
                  ↓
+--------------------------------------+
| DATABASE                             |
+--------------------------------------+


---

31. Why Separate These Layers?

Imagine we put everything inside one class:

StudentRegistrationSystem

It handles:

HTML;

database queries;

business rules;

authentication;

course registration;

email;

reports.


That becomes difficult to maintain.

Instead:

Presentation
      ↓
Application
      ↓
Domain
      ↓
Data Access
      ↓
Database

gives responsibilities clearer boundaries.


---

PART N — COMPONENT THINKING

32. What Is a Component?

At a high level, a component represents a modular part of a system that provides or requires functionality.

For example:

University System
│
├── Authentication Component
├── Registration Component
├── Payment Component
├── Notification Component
└── Reporting Component

This is different from simply asking:

> "What classes exist?"



Now we're asking:

> "How can the software be divided into meaningful, replaceable or independently understandable parts?"




---

33. Component Example

Consider payment.

+------------------------+
| Payment Component      |
+------------------------+
| processPayment()       |
| refundPayment()        |
+------------------------+

It could communicate with:

Bank Gateway
Mobile Money Gateway
Card Gateway

through an abstraction.

That allows the larger system to remain less dependent on a specific payment implementation.


---

PART O — MODEL VALIDATION

34. What Is Design Validation?

Validation asks:

> "Does our design actually represent what the system is supposed to do?"



Suppose the requirement says:

> "Students cannot register for a full course."



But our sequence diagram says:

Student
 ↓
RegistrationService
 ↓
Create Registration

There is no:

checkCapacity()

Then our design is incomplete.


---

35. Another Validation Example

Requirement:

> "Students must satisfy prerequisites."



Sequence diagram:

Student
 ↓
RegistrationService
 ↓
Create Registration

Again, something is missing.

We should have something like:

Student
 ↓
RegistrationService
 ↓
Course.checkPrerequisite()
 ↓
Create Registration

The design now better reflects the requirement.


---

PART P — DESIGN REVIEW

36. Questions a Design Team Should Ask

Before implementation, ask:

Requirement coverage

> Have we represented every important requirement?



Use-case coverage

> Does every major use case have supporting design elements?



Class coverage

> Do our classes provide the required data and behaviour?



Interaction coverage

> Can our objects actually collaborate to perform each use case?



State coverage

> Have we represented important lifecycle changes?



Architecture

> Are responsibilities divided appropriately?



Coupling

> Are components unnecessarily dependent?



Cohesion

> Does each class/component have a meaningful focus?



Reuse

> Can appropriate components be reused?



Maintainability

> What happens if the requirements change?




---

PART Q — AN IMPORTANT DISTINCTION

37. Model vs Diagram

Students sometimes use:

> "model"



and:

> "diagram"



as though they mean exactly the same thing.

They don't.

A diagram is a visual representation.

A model is the underlying structured representation of the system being described.

You might have multiple diagrams representing different aspects of the same model/system.

OMG's UML specification explicitly describes UML as a modelling language and organises its formalism across structural and behavioural modelling concepts. 


---

38. Simple Analogy

Think about Google Maps.

You can view:

satellite imagery;

roads;

terrain;

traffic;

public transport.


Different views can represent the same geographical reality.

Similarly:

Use Case Diagram
Class Diagram
Sequence Diagram
State Diagram
Activity Diagram

provide different perspectives on the same software system.


---

PART R — COMPLETE INTEGRATED EXAMPLE

39. Requirement

> R01: Students should be able to register for available courses online.




---

40. Use Case

Student ─────── Register for Course


---

41. Classes

Student
Course
Registration
RegistrationService


---

42. Attributes

Student
------------------
studentId
name
email

Course
------------------
courseCode
title
capacity

Registration
------------------
registrationId
date
status


---

43. Operations

Student
------------------
registerCourse()

Course
------------------
hasAvailableSpace()
checkPrerequisite()

Registration
------------------
confirm()
cancel()

RegistrationService
------------------
register()


---

44. Sequence

Student
   |
   | register(course)
   ↓
RegistrationService
   |
   | checkPrerequisite()
   ↓
Course
   |
   | available?
   ↓
RegistrationService
   |
   | create()
   ↓
Registration
   |
   | confirm()
   ↓
Student


---

45. Activity

START
 ↓
Login
 ↓
Select course
 ↓
Check prerequisite
 ↓
[Pass?]
 ├── NO → Reject
 |
 YES
 ↓
Check capacity
 ↓
[Space?]
 ├── NO → Reject
 |
 YES
 ↓
Create registration
 ↓
Confirm
 ↓
END


---

46. State

[REQUESTED]
     |
 validation
     ↓
[VALIDATED]
     |
 confirmation
     ↓
[CONFIRMED]
     |
 cancellation
     ↓
[CANCELLED]


---

47. Architecture

Presentation
      ↓
RegistrationService
      ↓
Student / Course / Registration
      ↓
Repositories
      ↓
Database


---

48. The Result

We now have:

REQUIREMENT
                  ↓
              USE CASE
                  ↓
      ┌───────────┼───────────┐
      ↓           ↓           ↓
   ACTIVITY   SEQUENCE      STATE
      \           |           /
       \          |          /
        └─────────┼─────────┘
                  ↓
             CLASS MODEL
                  ↓
             ARCHITECTURE
                  ↓
             IMPLEMENTATION

That is integrated OO modelling and design.


---

PART S — TUTORIAL — 1 HOUR

Tutorial Exercise 1

A hospital wants a system allowing patients to book appointments.

The requirement is:

> "A patient can select a doctor, choose an available date and time, and book an appointment."



Students must identify:

1. Actors.


2. Use cases.


3. Classes.


4. Attributes.


5. Operations.


6. Relationships.


7. Possible states of an appointment.




---

Tutorial Exercise 2

Explain the difference between:

A. Use Case Diagram

B. Class Diagram

C. Sequence Diagram

D. Activity Diagram

E. State Machine Diagram

For each, answer:

> What question does this model answer?



This is an excellent examination preparation technique.


---

Tutorial Exercise 3 — Model Consistency

Suppose a sequence diagram contains:

PaymentService
Payment
Invoice

but the class diagram only contains:

Student
Course
Registration

Questions:

1. What inconsistency exists?


2. What should the analyst/designer do?


3. Why should the sequence and class models agree?




---

PART T — PRACTICAL — 1 HOUR

49. Practical Assignment

Students will create a complete integrated UML model for:

> Online University Course Registration System



Deliverable 1 — Use Case Diagram

Include:

Student
Administrator

and appropriate use cases.


---

Deliverable 2 — Class Diagram

At minimum:

Student
Course
Registration
Programme
User
RegistrationService

Include:

attributes;

operations;

visibility;

relationships;

multiplicities.



---

Deliverable 3 — Sequence Diagram

Model:

> Student registers for a course.




---

Deliverable 4 — Activity Diagram

Model:

> Complete course registration workflow.




---

Deliverable 5 — State Diagram

Model:

> Registration lifecycle.




---

Deliverable 6 — Package Diagram

Organise classes into:

Authentication
Academic
Registration
Administration


---

Deliverable 7 — Architecture

Show:

Presentation
Application
Domain
Data Access
Database


---

PART U — INDEPENDENT LEARNING — 10 HOURS

Activity 1 — Model Integration

Take one system of your choice:

banking;

hospital;

library;

e-commerce;

university;

mobile money.


Develop:

1. Use Case Diagram


2. Class Diagram


3. Sequence Diagram


4. Activity Diagram


5. State Diagram



Then write 1–2 pages explaining how the diagrams are connected.


---

Activity 2 — Consistency Audit

Choose one use case and create a table:

Requirement	Use Case	Class	Operation	Sequence	State

Register course	Register Course	Registration	register()	Yes	Requested → Confirmed


Students should identify missing links.


---

Activity 3 — Research

Research:

> "The role of UML in software analysis, design and documentation."



Students should consult authoritative sources and recent academic literature.

OMG's UML resources remain a useful primary reference because UML is maintained as a formal specification rather than simply being an informal collection of diagramming conventions. 


---

PART V — EXAMINATION QUESTIONS

Question 1 — 25 Marks

> Explain the concept of integrated object-oriented modelling. Using an Online University Registration System, demonstrate how the use-case, class, sequence, activity and state models can be integrated into a coherent design.




---

Question 2 — 20 Marks

> Different UML diagrams represent different views of the same software system. Explain this statement with appropriate examples.




---

Question 3 — 20 Marks

> A sequence diagram contains the operation checkAvailability(), but the corresponding class diagram contains no such operation.

a) Identify the modelling problem.
b) Explain why consistency between models is important.
c) Describe how the designer should resolve the problem.




---

Question 4 — 25 Marks

> Design an integrated UML model for an online hospital appointment system. Your answer should include:

1. actors;


2. use cases;


3. classes;


4. relationships;


5. sequence of interactions;


6. activities;


7. appointment states;


8. explanation of how the models are consistent.






---

PART W — COMMON STUDENT CONFUSIONS

50. "Use Case vs Sequence Diagram"

Use case:

> What does the user want to achieve?



Sequence:

> How do system objects communicate to achieve it?




---

51. "Activity vs State Diagram"

Activity diagram:

> What activities happen during a process?



State diagram:

> What states does a particular object pass through?



Example:

Activity

Select Course
 ↓
Check Prerequisite
 ↓
Check Capacity
 ↓
Register

State

Requested
 ↓
Validated
 ↓
Confirmed


---

52. "Class Diagram vs Object Diagram"

Class diagram

Shows types/classes:

Student
Course
Registration

Object diagram

Shows specific instances:

student:Student
course:Course
registration:Registration

Think:

> Class = blueprint



> Object = actual thing created from the blueprint




---

PART X — WEEK 12 SUMMARY

By the end of this week, students should understand that OOAD involves multiple connected models, not isolated diagrams.

The central principle is:

> Every model should contribute to the same understanding of the system.



A useful mental model is:

REQUIREMENTS
     ↓
USE CASES
     ↓
WHAT THE SYSTEM MUST DO
     ↓
BEHAVIOURAL MODELS
     ↓
HOW THE BEHAVIOUR OCCURS
     ↓
OBJECT/CLASS MODEL
     ↓
WHAT STRUCTURE SUPPORTS THE BEHAVIOUR
     ↓
ARCHITECTURE
     ↓
HOW THE SOFTWARE IS ORGANISED
     ↓
IMPLEMENTATION

UML 2.5.1 provides formal constructs covering structural modelling, behavioural modelling, use cases and related modelling mechanisms; therefore, the integration we have practised is consistent with UML's intended role as a standard modelling language. 


---

53. WEEK 11 → WEEK 12 → WEEK 13

The progression is now:

WEEK 11 — DESIGN REFINEMENT

> "How do I turn analysis models into detailed design elements?"



We studied:

design classes;

responsibilities;

interfaces;

abstraction;

cohesion;

coupling;

encapsulation;

dependencies;

reuse;

layering.


WEEK 12 — INTEGRATED MODELLING

> "How do all these models work together as one system?"



We studied:

requirements;

use cases;

classes;

sequence;

activities;

states;

packages;

components;

architecture;

consistency;

traceability.


WEEK 13 — NEXT STEP

We will move from integrated modelling toward the syllabus requirement of:

> "Express the value of designing a multilayer system built of reusable and adaptable components."



So Week 13 will focus heavily on multilayer architecture, reusable components, adaptability, componentisation, interfaces, dependencies and architectural design, with a substantial practical case study showing students why these ideas matter rather than simply defining them.


---

References

1. Object Management Group (OMG). Unified Modeling Language Specification, Version 2.5.1. OMG's formal UML specification and machine-readable UML artefacts. 


2. Object Management Group. UML® — Unified Modeling Language. Overview of UML's purpose in visualising, specifying and documenting software and systems. 


3. Object Management Group. UML 2.5.1 Specification — Technical Specification. Structural and behavioural modelling clauses and UML diagram concepts. 


4. Mach, E. (2019). Object Oriented Analysis & Design Cookbook: Introduction to Practical System Modeling.


5. Reddy, V. & Korra, S. (2018). Object-Oriented Analysis and Design Using UML.


6. The Art of Service (2021). Object Oriented Analysis and Design: A Complete Guide.


7. Wixom, B. & Dennis, A. (2018). Systems Analysis and Design.


8. Blokdyk, G. (2021). Object-Oriented Analysis and Design Standard Requirements.



Key takeaway for students: Don't memorise UML diagrams as independent pictures. Learn to tell the same system's story through different models—and make sure those models agree.
