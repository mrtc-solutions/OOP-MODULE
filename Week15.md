BICT 3202 — OBJECT-ORIENTED ANALYSIS AND DESIGN

WEEK 15: COMPLETE OOAD CASE STUDY, MODEL INTEGRATION AND CASE TOOL IMPLEMENTATION

Programme: BSc in Information Communication and Technology
Year: Three
Course Code: BICT 3202
Week: 15 of 16
Module: Object-Oriented Analysis and Design
Lecture Hours: 2
Tutorial Hours: 1
Practical Hours: 1
Independent Learning: 10 hours
Credits: 10

> Position in the course: Week 15 is the integration and application week. Students now take the concepts developed from Weeks 1–14 and apply them to a complete system. The emphasis is not simply on drawing UML diagrams, but on demonstrating that the diagrams tell a consistent story and can guide implementation.



The UML standard groups structural modelling and behavioural modelling into related but distinct parts of UML, which is important for this week's emphasis on integrating multiple views of the same system. 


---

1. WEEK 15 THEME

Complete Object-Oriented Analysis and Design: From Requirements to an Integrated Design

The central question for this week is:

> "If I am given a real software problem today, can I use everything I have learned to analyse it, model it, design it and communicate the design to another developer?"



By Week 15, students should no longer see:

use-case diagrams,

class diagrams,

sequence diagrams,

activity diagrams,

state diagrams,

component diagrams,


as separate examination topics.

Instead, they should understand them as different views of one software system.


---

2. LEARNING OUTCOMES

By the end of Week 15, students should be able to:

1. Analyse a complete software problem using object-oriented techniques.


2. Identify stakeholders and system actors.


3. Extract functional and non-functional requirements.


4. Identify appropriate use cases.


5. Construct a use-case model.


6. Identify candidate classes and objects.


7. Develop a conceptual/domain class model.


8. Refine the analysis model into a design model.


9. Identify class responsibilities.


10. Define attributes and operations.


11. Model associations, inheritance and composition where appropriate.


12. Develop interaction models for important use cases.


13. Develop sequence diagrams.


14. Develop activity diagrams.


15. Develop state-machine diagrams for state-dependent objects.


16. Develop a component-level view of the system.


17. Check consistency between UML models.


18. Document a complete OOAD solution.


19. Use a CASE/UML modelling tool to create and organise models.


20. Explain how the final design could be implemented.




---

PART A — WHAT HAVE WE BEEN LEARNING?

3. Looking Back at the Entire Module

Before starting the case study, students should see the entire journey.

The OOAD process can be simplified as:

Business Problem
       ↓
Requirements
       ↓
Use Cases
       ↓
Object Identification
       ↓
Class Model
       ↓
Dynamic Model
       ↓
Behavioural Model
       ↓
Analysis Documentation
       ↓
Design
       ↓
Architecture / Components
       ↓
Integrated Design
       ↓
Implementation

The important word here is:

> INTEGRATION




---

4. Why Integration Matters

Imagine that a team creates these models:

Use-case diagram

Student → Register Course

But the class diagram has no:

Registration

class.

Then the models are incomplete.

Or imagine:

Class diagram

Course
---------
checkCapacity()

But the sequence diagram calls:

verifySeats()

There is a consistency problem.

Or:

Activity diagram

says:

Check payment

but there is no payment-related class, operation or component anywhere else.

Again:

> Something is missing.



Therefore:

> A good OOAD model must be internally consistent.




---

PART B — THE COMPLETE CASE STUDY

5. Case Study: University Online Course Registration System

For this week's major case study, we will use a system familiar to students:

> University Online Course Registration System



The university wants students to register for courses online instead of filling out paper forms.


---

6. Business Problem

The university currently has problems such as:

long registration queues;

lost registration forms;

duplicate registrations;

students registering for courses without prerequisites;

courses exceeding capacity;

delays in confirming registration;

difficulty producing registration reports.


The university therefore wants an online system.


---

7. Business Goal

The goal is to develop a system that allows:

> Students to search for courses, check eligibility, register for courses and receive confirmation electronically.



Academic administrators should also be able to:

create courses;

modify courses;

set course capacity;

view registrations;

close registration;

generate reports.



---

PART C — REQUIREMENTS

8. Functional Requirements

A functional requirement describes something the system must do.

For example:

> "The system shall allow students to log in."



That describes functionality.

For our system:

FR1 — Student Login

The system shall allow students to authenticate.

FR2 — View Courses

The system shall allow students to view available courses.

FR3 — Search Courses

Students shall be able to search for courses.

FR4 — Check Eligibility

The system shall check whether the student satisfies prerequisites.

FR5 — Register

Students shall be able to register for eligible courses.

FR6 — Prevent Duplicate Registration

The system shall prevent a student from registering for the same course twice.

FR7 — Check Capacity

The system shall prevent registration when a course has reached its maximum capacity.

FR8 — Drop Course

Students shall be able to drop a course within the permitted period.

FR9 — Confirmation

The system shall provide registration confirmation.

FR10 — Administration

Administrators shall be able to manage courses.


---

9. Non-Functional Requirements

These describe how well the system should operate.

Examples:

Security

Only authorised users should access protected functionality.

Performance

The system should respond to normal requests within an acceptable time.

Availability

The system should be available during registration periods.

Usability

Students should be able to complete registration without extensive training.

Maintainability

The system should be designed so that future changes can be made without rewriting the entire application.


---

PART D — IDENTIFYING ACTORS

10. What Is an Actor?

An actor is an external role that interacts with the system.

It does not necessarily mean a human being.

An actor can be:

a student;

administrator;

lecturer;

payment service;

email service;

another software system.



---

11. Actors in Our System

We identify:

Student
Administrator
Lecturer
Notification Service

Potentially:

Payment Gateway

if students pay registration fees online.


---

PART E — USE CASE MODEL

12. Student Use Cases

A student might:

Login
View Courses
Search Courses
Register Course
Drop Course
View Registration
Download Registration Confirmation


---

13. Administrator Use Cases

An administrator might:

Login
Create Course
Update Course
Delete Course
Set Course Capacity
View Registrations
Close Registration
Generate Report


---

14. Simplified Use-Case Diagram

Conceptually:

UNIVERSITY SYSTEM
                 ┌─────────────────────────────┐
                 │                             │
Student ─────────┤ Login                       │
                 │ View Courses                 │
Student ─────────┤ Search Courses              │
                 │ Register Course              │
Student ─────────┤ Drop Course                  │
                 │ View Registration             │
                 │                             │
Administrator ───┤ Create Course                │
                 │ Update Course                │
Administrator ───┤ View Registrations           │
                 │ Generate Report              │
                 └─────────────────────────────┘

The exact graphical notation should be produced using a UML tool in the practical session.

The OMG UML specification formally defines UML's modelling constructs, while the UML 2.5.1 specification remains the formal UML reference maintained by OMG. 


---

PART F — FULL USE CASE SPECIFICATION

15. Use Case: Register for Course

Students should not stop at the diagram.

A complete OOAD analysis should document important use cases.

Use Case Name

Register for Course

Primary Actor

Student

Goal

Register for an available course.

Preconditions

Student is authenticated.

Registration period is open.

Student account is active.


Main Success Scenario

1. Student selects "Register Course".


2. System displays available courses.


3. Student selects a course.


4. System checks whether the course exists.


5. System checks prerequisites.


6. System checks course capacity.


7. System checks whether the student is already registered.


8. System creates registration.


9. System updates course enrolment.


10. System displays confirmation.




---

16. Alternative Flow

Suppose the course is full.

Student selects course
       ↓
System checks capacity
       ↓
Course FULL
       ↓
System rejects registration
       ↓
System displays:
"Course is currently full."


---

17. Another Alternative Flow

Suppose the student has not completed the prerequisite.

Student selects course
       ↓
System checks prerequisite
       ↓
Prerequisite NOT satisfied
       ↓
Registration rejected

This becomes important later when we construct the sequence diagram.


---

PART G — IDENTIFYING OBJECTS

18. Candidate Classes

From the requirements, we can identify:

Student
Course
Registration
Programme
Prerequisite
Administrator

Potential technical/application classes include:

RegistrationController
RegistrationService
CourseRepository
RegistrationRepository
NotificationService
AuthenticationService


---

19. Domain Classes vs Technical Classes

This distinction is important.

Domain class

Represents something from the problem domain.

Example:

Student
Course
Registration

Technical/application class

Supports implementation.

Example:

RegistrationController
RegistrationRepository
NotificationService

Students should not confuse these.


---

PART H — CLASS MODEL

20. Student

Student
--------------------------------
- studentId : String
- name : String
- email : String
- programme : Programme
--------------------------------
+ registerCourse()
+ dropCourse()
+ viewRegistration()


---

21. Course

Course
--------------------------------
- courseCode : String
- courseName : String
- credits : Integer
- capacity : Integer
- status : CourseStatus
--------------------------------
+ isAvailable()
+ checkCapacity()
+ addStudent()
+ removeStudent()


---

22. Registration

Registration
--------------------------------
- registrationId : String
- registrationDate : Date
- status : RegistrationStatus
--------------------------------
+ confirm()
+ cancel()


---

23. RegistrationService

RegistrationService
--------------------------------
+ registerStudent()
+ dropStudent()
+ checkEligibility()
+ checkDuplicate()


---

24. RegistrationRepository

RegistrationRepository
--------------------------------
+ save()
+ findByStudent()
+ findByCourse()
+ delete()

Notice what has happened.

We have moved from:

"Register a course"

to a much more detailed design:

Controller
     ↓
Service
     ↓
Domain objects
     ↓
Repository


---

PART I — ASSOCIATIONS

25. Student and Registration

A student can have many registrations.

Student 1 ───────── 0..*
Registration

Meaning:

> One student may have zero or many registration records.




---

26. Course and Registration

A course can have many registrations:

Course 1 ───────── 0..*
Registration

Therefore:

Student
   1
   |
   | 0..*
Registration
   0..*
   |
   | 1
Course

This is more meaningful than simply drawing lines between classes.

Students must understand the multiplicity.


---

PART J — INHERITANCE

27. Should We Use Inheritance?

Suppose the system has:

User
 |
 ├── Student
 ├── Administrator
 └── Lecturer

We might model:

User
----------------
userId
name
email
login()
logout()
        △
        |
 ┌──────┼────────┐
 ↓      ↓        ↓
Student Admin  Lecturer

But students must ask:

> Is inheritance genuinely appropriate?



Do not use inheritance simply because UML allows it.


---

28. Why Inheritance Might Be Useful Here

All three may share:

user ID;

name;

email;

authentication behaviour.


But they have different responsibilities.

Therefore a general User abstraction may be reasonable.


---

PART K — SEQUENCE DIAGRAM

29. Register Course Interaction

Now we ask:

> What happens when the student actually registers?



A simplified interaction:

Student
   |
   | register(course)
   ↓
RegistrationController
   |
   | registerStudent()
   ↓
RegistrationService
   |
   | checkEligibility()
   ↓
Student
   |
   | eligible
   ↓
Course
   |
   | checkCapacity()
   ↓
RegistrationService
   |
   | createRegistration()
   ↓
Registration
   |
   | save()
   ↓
RegistrationRepository


---

30. Why Is This Diagram Important?

Because it tells the developer:

> Which object talks to which other object, and in what order?



The class diagram told us:

> What classes exist.



The sequence diagram tells us:

> How those classes cooperate.



That distinction should be very clear to students.


---

PART L — STATE MACHINE

31. Course Lifecycle

A course can have different states.

Created
   ↓
Available
   ↓
Full
   ↓
Closed


---

32. State Transitions

Created → Available

Event:

> Administrator opens registration.



Available → Full

Event:

> Last available seat is taken.



Full → Available

Event:

> A student drops the course and a seat becomes available.



Available → Closed

Event:

> Registration period ends.



Full → Closed

Event:

> Registration period ends.




---

33. Why Not Just Put "Status" in the Class Diagram?

We can have:

status : CourseStatus

in the class.

But that doesn't explain:

> What causes the status to change?



The state machine provides that dynamic information.

This demonstrates why multiple models are useful.


---

PART M — ACTIVITY DIAGRAM

34. Registration Workflow

Start
  ↓
Login
  ↓
View Courses
  ↓
Select Course
  ↓
Check Prerequisite
  ↓
Prerequisite satisfied?
 ┌───────────┴───────────┐
No                       Yes
↓                         ↓
Reject              Check Capacity
                         ↓
                    Space available?
                    ┌─────┴─────┐
                   No           Yes
                   ↓             ↓
                 Reject      Create Registration
                                  ↓
                             Save Registration
                                  ↓
                            Send Confirmation
                                  ↓
                                 End

The activity diagram therefore describes the workflow.


---

PART N — COMPONENT DESIGN

35. From Classes to Components

At design level, we can group related functionality.

For example:

┌─────────────────────────────┐
│ Student Management          │
│ Component                   │
└─────────────────────────────┘

┌─────────────────────────────┐
│ Course Registration         │
│ Component                   │
└─────────────────────────────┘

┌─────────────────────────────┐
│ Authentication              │
│ Component                   │
└─────────────────────────────┘

┌─────────────────────────────┐
│ Notification                │
│ Component                   │
└─────────────────────────────┘

UML includes component modelling among its formal modelling constructs. 


---

36. Possible Layered Architecture

The system could be organised as:

┌──────────────────────────┐
│ Presentation Layer       │
│ Web / Mobile Interface   │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Application Layer        │
│ Controllers / Services   │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Domain Layer             │
│ Student / Course /       │
│ Registration             │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Persistence Layer        │
│ Repositories / Database  │
└──────────────────────────┘

This connects directly with the design and architectural concepts covered previously.


---

PART O — MODEL TRACEABILITY

37. Requirement → Use Case

Requirement:

> Student must register for courses.



↓

Use case:

Register Course


---

38. Use Case → Sequence

Register Course
       ↓
Student
       ↓
RegistrationController
       ↓
RegistrationService
       ↓
Course
       ↓
Registration


---

39. Sequence → Classes

The sequence reveals:

RegistrationController
RegistrationService
Course
Registration


---

40. Sequence → Operations

Messages become candidate operations:

registerStudent()
checkEligibility()
checkCapacity()
createRegistration()
save()


---

41. Operations → Implementation

Eventually developers can implement these operations in a programming language such as:

Java
C#
Python
C++
Kotlin
TypeScript

The exact language does not change the OOAD principle.


---

PART P — CONSISTENCY CHECK

42. Students Should Perform a Model Audit

Give students this checklist.

Use Case ↔ Class Model

Does every major use case have supporting classes?

Class Model ↔ Sequence Diagram

Does every important message correspond to an operation?

Sequence ↔ State Model

Do messages cause appropriate state transitions?

Activity ↔ Sequence

Does the workflow correspond to the interaction?

Class ↔ Component

Are classes sensibly allocated to components?

Requirements ↔ Design

Can we trace each important requirement into the design?


---

43. Example of a Defect

Suppose the activity diagram says:

Check Payment

But:

Class diagram

contains no payment-related class.

Ask:

> How is payment being checked?



Possible solution:

PaymentService
Payment
PaymentGateway

may need to be introduced.

This is model validation.


---

PART Q — FULL ANALYSIS DOCUMENTATION

44. What Should a Complete OOAD Document Contain?

A professional analysis/design document could contain:

Section 1 — Introduction

background;

problem statement;

purpose.


Section 2 — Requirements

functional requirements;

non-functional requirements.


Section 3 — Actors

Identify external roles.

Section 4 — Use Cases

Describe system functionality.

Section 5 — Use-Case Diagram

Visual representation.

Section 6 — Domain/Class Model

Identify important classes.

Section 7 — Interaction Models

Sequence/collaboration diagrams.

Section 8 — Dynamic Model

State diagrams.

Section 9 — Activity Model

Workflows.

Section 10 — Design

Refined classes and responsibilities.

Section 11 — Architecture

Layers/components.

Section 12 — Model Validation

Check consistency.

Section 13 — Conclusion

Summarise the proposed solution.


---

PART R — CASE TOOLS

45. What Is a CASE Tool?

CASE means:

> Computer-Aided Software Engineering.



A CASE tool provides software support for activities such as:

requirements analysis;

modelling;

UML diagram creation;

documentation;

project management;

code-related development activities.


For this course, the important part is:

> Using a tool to create and manage UML models.




---

46. Why Use a CASE Tool?

Imagine drawing 15 UML diagrams manually.

You discover:

> "The class name is wrong in six diagrams."



You have to correct everything manually.

A modelling tool can make model management much easier.

CASE tools can also provide:

diagram editing;

model repositories;

documentation;

consistency support;

project organisation;

sometimes code engineering capabilities.



---

47. Examples of UML/CASE Tools

Examples students may encounter include:

Enterprise Architect;

Visual Paradigm;

StarUML;

Modelio;

diagrams.net/draw.io.


The exact tool is less important than understanding the modelling principles.

For example, the course outline specifically mentions:

> CASE Tool: Select Enterprise Demonstration



Therefore, the practical session should demonstrate a CASE/UML modelling environment rather than teaching students to draw UML only on paper.


---

PART S — CASE TOOL PRACTICAL

48. Practical Demonstration

The lecturer should demonstrate the creation of:

1. Project

University Course Registration

2. Package

Requirements
Analysis
Design

3. Use-case diagram

Add:

Student
Administrator

and use cases.

4. Class diagram

Add:

Student
Course
Registration

etc.

5. Sequence diagram

Model:

> Register Course



6. Activity diagram

Model:

> Registration Process



7. State diagram

Model:

> Course Lifecycle



8. Component diagram

Model:

> System Architecture




---

PART T — HOW STUDENTS SHOULD THINK WHEN USING A CASE TOOL

49. The Tool Does Not Do the Thinking

This is extremely important.

Students should not think:

> "If I learn Enterprise Architect, I know OOAD."



No.

The tool is like Microsoft Word for documentation.

Knowing Word does not mean knowing what to write.

Similarly:

> Knowing a CASE tool does not mean understanding object-oriented analysis and design.



The student must first understand:

Problem
 ↓
Model
 ↓
Design

Then use the CASE tool to represent that model.


---

PART U — COMMON CASE TOOL MISTAKES

50. Mistake 1: Drawing Diagrams Without Requirements

Students sometimes open the tool and immediately start drawing classes.

Correct process:

Requirements
     ↓
Understand system
     ↓
Identify actors
     ↓
Identify use cases
     ↓
Identify objects/classes
     ↓
Create diagrams


---

51. Mistake 2: Creating Too Many Classes

A student might produce:

StudentManager
StudentProcessor
StudentHandler
StudentHelper
StudentUtility
StudentController
StudentService
StudentSystem

without clear justification.

The question should always be:

> What responsibility does this class have?




---

52. Mistake 3: Copying Diagrams From the Internet

A diagram may look professional but still be wrong for the given system.

Students should understand:

> UML notation is standard, but the model must represent your system.




---

53. Mistake 4: Inconsistent Naming

For example:

Class: Registration

but:

Sequence: Enrollment

and:

Database: CourseSignup

Different names can cause confusion.

Establish a consistent vocabulary.


---

PART V — COMPLETE INTEGRATED MODEL

54. The Big Picture

Our system can now be represented as:

UNIVERSITY REGISTRATION SYSTEM
                                      │
                  ┌───────────────────┴──────────────────┐
                  │                                      │
                Student                              Administrator
                  │                                      │
                  ↓                                      ↓
             Use Cases                               Use Cases
                  │                                      │
                  └──────────────────┬───────────────────┘
                                     ↓
                               Analysis Model
                                     │
                     ┌───────────────┼───────────────┐
                     ↓               ↓               ↓
                 Class Model    Dynamic Model   Behaviour Model
                     │               │               │
                     ↓               ↓               ↓
                  Classes          States        Interactions
                     │               │               │
                     └───────────────┼───────────────┘
                                     ↓
                              Design Model
                                     ↓
                              Architecture
                                     ↓
                              Components
                                     ↓
                              Implementation

This is the complete OOAD journey.


---

PART W — TUTORIAL SESSION

55. Tutorial Activity — 1 Hour

Scenario

A college wants an Online Library Management System.

Students should be able to:

search books;

borrow books;

return books;

view borrowed books.


Librarians should be able to:

add books;

remove books;

register members;

view overdue books.



---

Task 1

Identify:

actors;

use cases;

candidate classes.


Task 2

Create a use-case diagram.

Task 3

Create a class diagram.

Task 4

Select:

> Borrow Book



and create a sequence diagram.

Task 5

Create an activity diagram for borrowing.

Task 6

Create a state diagram for:

> Book Copy



Possible states:

Available
    ↓
Borrowed
    ↓
Returned
    ↓
Available

Task 7

Explain how the five diagrams relate.


---

PART X — PRACTICAL SESSION

56. Practical — 1 Hour

Students should use a UML/CASE tool to implement the University Registration case study.

Minimum deliverables

Diagram 1: Use-case diagram

Diagram 2: Class diagram

Diagram 3: Sequence diagram

Diagram 4: Activity diagram

Diagram 5: State-machine diagram

Diagram 6: Component diagram


---

57. Practical Quality Requirements

Students should ensure:

Naming consistency

Registration should not randomly become Enrollment.

Relationships

Every relationship must have a reason.

Multiplicity

Use:

1
0..1
0..*
1..*

where appropriate.

Operations

Sequence messages should correspond to class operations.

Behaviour

State transitions should be triggered by meaningful events.

Requirements

Every major requirement should be represented somewhere in the model.


---

PART Y — INDEPENDENT LEARNING — 10 HOURS

58. Major Week 15 Assignment

Students must select one real-world information system.

Examples:

1. Banking system


2. Hospital management system


3. E-commerce system


4. Library management system


5. Hotel reservation system


6. University registration system


7. Mobile money system


8. Airline reservation system




---

59. Deliverable 1 — Problem Definition

Write:

background;

problem statement;

objectives;

scope.



---

60. Deliverable 2 — Requirements

Provide:

at least 10 functional requirements;

at least 5 non-functional requirements.



---

61. Deliverable 3 — Use Cases

Identify:

actors;

major use cases;

use-case relationships where appropriate.



---

62. Deliverable 4 — Use-Case Diagram

Produce a complete diagram.


---

63. Deliverable 5 — Class Model

At least:

> 10 meaningful classes



Each should have appropriate:

attributes;

operations;

visibility;

relationships.



---

64. Deliverable 6 — Sequence Diagrams

Create at least:

> Two sequence diagrams



for important use cases.


---

65. Deliverable 7 — Activity Diagram

Create at least:

> One activity diagram



for a major workflow.


---

66. Deliverable 8 — State Diagram

Choose an object whose behaviour changes over time.

Examples:

Order
Ticket
Account
Book
Course
Application
Payment


---

67. Deliverable 9 — Component Diagram

Group the system into major components.

For example:

Authentication
Student Management
Course Management
Registration
Notification
Reporting
Database


---

68. Deliverable 10 — Integration Analysis

This is the most important part.

Students must write a section answering:

Question 1

How does the use-case model relate to the class model?

Question 2

How does the sequence diagram relate to class operations?

Question 3

How does the state diagram relate to object behaviour?

Question 4

How does the activity diagram relate to the system workflow?

Question 5

How does the component diagram relate to the classes?

Question 6

How does the complete model support the requirements?


---

PART Z — ASSESSMENT RUBRIC

Area	Marks

Problem definition	5
Requirements	10
Use-case model	10
Class model	15
Sequence diagrams	15
Activity diagram	10
State model	10
Component/design model	10
Model consistency/integration	10
Documentation/presentation	5
Total	100



---

PART AA — EXAMINATION QUESTIONS

Question 1 — 20 Marks

> Explain the purpose of CASE tools in object-oriented analysis and design. Discuss at least five ways in which CASE tools can support software development.




---

Question 2 — 25 Marks

> Using an Online Library Management System as an example, explain how requirements can be transformed into use cases, classes, interactions and a final object-oriented design.




---

Question 3 — 25 Marks

> Explain why UML diagrams should not be developed independently. Using a practical example, demonstrate how a use-case diagram, class diagram, sequence diagram, activity diagram and state-machine diagram can describe different aspects of the same system.




---

Question 4 — 30 Marks

> A university wants an online course registration system. Students can search for courses and register if they have satisfied prerequisites and the course has available capacity. Administrators can manage courses and view registrations.

Develop an object-oriented analysis and design for the system. Your answer should include:

a. Actors
b. Use cases
c. Candidate classes
d. Class relationships
e. Major operations
f. Sequence of registration interactions
g. Course states
h. Registration workflow
i. Components
j. Explanation of how the models remain consistent.




---

PART AB — IMPORTANT DISTINCTIONS STUDENTS MUST KNOW

Concept	What it answers

Requirements	What does the stakeholder need?
Use case	What goal does an actor accomplish?
Class diagram	What structural elements exist?
Object model	What objects/classes and relationships exist?
Sequence diagram	How do objects communicate over time?
Activity diagram	How does a workflow proceed?
State diagram	How does one object change state?
Component diagram	How is functionality organised into components?
Design model	How should the system be structured for implementation?
CASE tool	What software can help us create/manage the models?


This distinction is particularly important because students often lose marks by simply writing:

> "A class diagram shows the system and a sequence diagram shows interaction."



That is too vague.

They should be able to say:

> A class diagram models the structural/static aspects of the system by representing classes, their attributes, operations and relationships, whereas a sequence diagram models a particular interaction scenario by showing the ordered exchange of messages between participating objects.



That is the level expected at Year 3.


---

PART AC — THE "16-YEAR-OLD" EXPLANATION

If I had to explain the whole Week 15 to a 16-year-old:

Imagine you want to build a school management app.

First you ask:

> "What does the school need?"



That's requirements.

Then:

> "Who will use the app and what will they do?"



That's use cases.

Then:

> "What things do we need inside the app?"



That's classes/objects.

Then:

> "How will these things talk to each other?"



That's sequence/interaction modelling.

Then:

> "What happens step by step?"



That's activity modelling.

Then:

> "What happens when an object changes condition?"



That's state modelling.

Then:

> "How do we organise all these pieces into software components?"



That's design/architecture.

Finally:

> "Let's put all of this into a professional UML/CASE tool and make sure everything agrees."



That's Week 15.

So the student should remember:

WHAT?
 ↓
Requirements

WHO?
 ↓
Actors / Use Cases

WHAT THINGS?
 ↓
Classes / Objects

HOW DO THEY TALK?
 ↓
Sequence / Interaction

WHAT HAPPENS STEP-BY-STEP?
 ↓
Activity

HOW DOES SOMETHING CHANGE?
 ↓
State

HOW DO WE ORGANISE THE SOFTWARE?
 ↓
Design / Components

DOES EVERYTHING AGREE?
 ↓
Model Integration

CAN ANOTHER DEVELOPER UNDERSTAND IT?
 ↓
Complete OOAD Documentation


---

PART AD — CONNECTION TO WEEK 14

Week 14 taught:

> How to combine the Object, Dynamic and Behavioural Models into an object-oriented design.



Week 15 now asks:

> Can you actually do it on a complete system?



Therefore:

WEEK 14
Understanding + Integration
        ↓
WEEK 15
Complete Application
        ↓
Requirements
        ↓
Use Cases
        ↓
Classes
        ↓
Interactions
        ↓
Activities
        ↓
States
        ↓
Components
        ↓
Design
        ↓
CASE Tool
        ↓
Complete OOAD Documentation

This progression is intentional. We are not introducing another disconnected topic in Week 15.


---

PART AE — CONNECTION TO WEEK 16

Week 15 is effectively the final major application/project week.

Week 16 should therefore not introduce another large new theoretical topic.

Instead, it should consolidate the entire module through:

comprehensive revision;

examination-oriented questions;

UML notation revision;

common student mistakes;

integrated case-study examination;

practical modelling exercise;

review of the entire 16-week learning journey.


That preserves the original agreement we made at the beginning: 16 weeks, with the final weeks used to consolidate everything rather than rushing the syllabus beyond what was provided.


---

REFERENCES AND CURRENT AUTHORITATIVE SOURCES

1. Object Management Group — UML Specification

The Object Management Group (OMG) maintains the formal UML specification. UML 2.5.1 is listed by OMG as a formal specification, with its adoption dating to December 2017. 

[OMG — Unified Modeling Language Specification](https://www.omg.org/spec/UML/?utm_source=chatgpt.com)

2. UML 2.5.1 Specification

The UML 2.5.1 specification organises UML concepts into structural modelling clauses, behavioural modelling clauses and supplementary concepts including use cases and deployments. This supports the approach used in this week's integrated case study. 

[OMG UML 2.5.1 Specification](https://www.omg.org/spec/UML/2.5.1/PDF?utm_source=chatgpt.com)

3. IBM — Unified Process / RUP

IBM documentation describes the Rational Unified Process as having four major phases—Inception, Elaboration, Construction and Transition—and describes iterations as planned intervals within phases. This reinforces the process concepts covered earlier in the module. 

4. IBM Rational Unified Process Best Practices

IBM's RUP material describes Inception as establishing the business case and project scope, while Elaboration focuses on analysing the problem domain, establishing the architectural foundation and addressing high-risk areas. 


---

PRESCRIBED TEXTS FROM THE COURSE OUTLINE

Mach, E. (2019). Object Oriented Analysis & Design Cookbook: Introduction to Practical System Modeling.

Reddy, V. & Korra, S. (2018). Object-Oriented Analysis and Design Using UML.

The Art of Service (2021). Object Oriented Analysis and Design: A Complete Guide.


RECOMMENDED TEXTS

Wixom, B. & Dennis, A. (2018). Systems Analysis and Design.

Blokdyk, G. (2021). Object-Oriented Analysis and Design Standard Requirements.

Wixom, B. & Dennis, A. (2020). Systems Analysis and Design: An Object-Oriented Approach with UML.



---

WEEK 15 — FINAL TAKEAWAY

The single most important lesson is:

> OOAD is not about drawing many UML diagrams. It is about building a coherent model of a software system where requirements, use cases, objects, classes, interactions, behaviour and design decisions all support one another.



A student who can take a completely new problem, move from:

Requirement → Use Case → Class → Interaction → Behaviour → Design → Components → Integrated UML Documentation

has genuinely understood Object-Oriented Analysis and Design.

And that is exactly what Week 15 is designed to test.
