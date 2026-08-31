Absolutely. Week 10 is the correct next step after Week 9.

Week 9 dealt with how software development is organised through the Unified Process. Week 10 now moves into the actual Object-Oriented Design part of the syllabus:

> Object-Oriented Design → Overview of Design → Combining the Object, Dynamic and Behavioural Models



I’ll keep the same approach as before: detailed explanations, very simple examples, explicit identification of which subtopic each comparison belongs to, practical/UML examples, tutorial questions, practical work, examination questions, and current/authoritative references. IBM's current design-model guidance describes design as building on the analysis model and adding implementation-level detail, while UML remains formally specified by OMG. 

BICT 3202 — OBJECT-ORIENTED ANALYSIS AND DESIGN

WEEK 10: OBJECT-ORIENTED DESIGN

Programme: BSc in Information Communication and Technology
Year: Three
Course Code: BICT 3202
Week: 10 of 16
Lecture: 2 hours
Tutorial: 1 hour
Practical: 1 hour
Independent Learning: 10 hours
Credits: 10


---

1. WHERE WEEK 10 FITS IN THE COURSE

Students should understand that we are not starting another unrelated topic.

Look at our journey:

WEEK 1
Business Needs
       ↓
WEEK 2
Object Modelling Principles
       ↓
WEEK 3
UML
       ↓
WEEKS 4–6
Object Modelling
       ↓
WEEK 7
Dynamic Modelling
       ↓
WEEK 8
Behavioural Modelling
       ↓
WEEK 9
Unified Software Development Process
       ↓
WEEK 10
OBJECT-ORIENTED DESIGN
       ↓
WEEKS 11–16
Further design, integration, application and consolidation

The most important transition is:

ANALYSIS
"What does the system need?"

             ↓

DESIGN
"How are we going to build it?"

That distinction is fundamental to OOAD.

IBM's design-model guidance similarly describes the design model as building upon the analysis model and adding greater detail about the system's structure and implementation. 


---

2. WEEK 10 TOPICS FROM THE COURSE OUTLINE

The official outline gives us two major areas:

1. Overview of Design

2. Combining:

Object Model

Dynamic Model

Behavioural Model


We therefore need to understand:

what software design means;

what object-oriented design means;

analysis versus design;

why design is necessary;

design goals;

design principles;

design decisions;

design constraints;

design architecture;

refinement;

traceability;

cohesion;

coupling;

abstraction;

encapsulation;

separation of concerns;

interfaces;

responsibilities;

combining UML models;

consistency between models;

transforming analysis models into design models;

an integrated case study.



---

PART A — WHAT IS SOFTWARE DESIGN?

3. The Simple Meaning of Design

Before software, think about constructing a house.

A client tells an architect:

> "I want a three-bedroom house."



That's a requirement.

The architect then decides:

where the bedrooms go;

where the kitchen goes;

where the bathroom goes;

how electricity will be arranged;

where pipes will run;

what materials will be used;

how the building will be supported.


That is design.

Software is similar.

A customer might say:

> "I want a university student registration system."



That's a requirement.

The designer then decides:

what classes are needed;

what components are needed;

how classes communicate;

where business logic belongs;

how data is stored;

how authentication works;

how the system is divided into layers;

how the system handles errors;

how objects collaborate.


That is software design.


---

4. Definition of Software Design

Software design is the process of determining the structure, components, interfaces, interactions and implementation decisions needed to transform requirements and analysis results into a system that can be implemented.

A useful student-friendly definition is:

> Software design is the process of deciding how a software system will be organised and how its parts will work together to satisfy its requirements.



IBM describes the design model as providing greater detail about the system's structure and implementation, including design classes, interfaces, packages and architectural elements. 


---

5. What Is Object-Oriented Design?

Object-Oriented Design, commonly abbreviated OOD, is the process of designing software around:

objects;

classes;

responsibilities;

relationships;

interfaces;

collaborations;

inheritance where appropriate;

encapsulated data and behaviour.


For example:

Student
----------------
studentID
name
email
----------------
registerCourse()
dropCourse()
viewResults()

The designer asks:

> "What should the Student object know?"



and:

> "What should the Student object be responsible for doing?"




---

6. Analysis vs Design

This is one of the most important Week 10 examination areas.

Students often say:

> "Analysis and design are the same thing."



They are related, but they are not identical.


---

Analysis

Analysis primarily asks:

> What does the system need to accomplish?



We investigate:

business requirements;

user needs;

domain concepts;

system behaviour;

objects;

relationships;

use cases.



---

Design

Design asks:

> How should the software be structured and implemented to accomplish those requirements?



We decide:

classes;

interfaces;

components;

architecture;

responsibilities;

object collaborations;

data access;

security mechanisms;

persistence;

technologies.


IBM's analysis-model guidance describes analysis as identifying the application's logical structure without focusing on how it will be implemented, while its design-model guidance says design adds implementation-oriented detail. 


---

7. A Very Simple Example

Imagine the requirement:

> "A student should be able to register for a course."



Analysis asks:

Who?
Student

What?
Register Course

What concepts are involved?
Student
Course
Registration

We might have:

Student -------- Course
       \
        Registration


---

Design asks:

> "How will the software actually make this happen?"



We might introduce:

Student
Course
Registration
RegistrationService
CourseRepository
StudentRepository

Then:

Student
   ↓
RegistrationService
   ↓
CourseRepository
   ↓
Database

Now we're making implementation-oriented decisions.


---

8. Analysis Model vs Design Model

Analysis Model	Design Model

Focuses on understanding the problem	Focuses on solving the problem
Describes what the system needs	Describes how the system will be built
More conceptual	More technical
Domain-oriented	Implementation-oriented
Identifies important concepts/classes	Refines classes for implementation
Less technology-specific	More technology-specific


IBM explicitly describes the analysis model as the foundation of the design model and notes that the analysis model describes the logical structure rather than implementation details. 


---

PART B — WHY DO WE NEED DESIGN?

9. Why Can't We Just Start Coding?

Imagine the lecturer says:

> "Build a university management system."



And the programmer immediately opens VS Code and starts writing:

student.java

😂

After three months:

student.java = 15,000 lines

Inside it:

login;

payments;

course registration;

reports;

database queries;

email;

SMS;

authentication;

examination results.


Now changing one feature breaks five others.

This is exactly why design matters.


---

10. Good Design Makes Systems Easier to:

understand;

implement;

test;

maintain;

modify;

extend;

reuse;

debug;

scale.


Modern software-design literature continues to emphasise design principles, trade-offs, architecture, UML, components and larger reusable structures such as frameworks and microservices. 


---

PART C — DESIGN GOALS

11. What Makes a Good Object-Oriented Design?

A good design should generally aim for:

1. Correctness

It satisfies the requirements.

2. Maintainability

Developers can modify it without destroying unrelated functionality.

3. Reusability

Useful components can be reused.

4. Flexibility

The system can adapt to changing requirements.

5. Understandability

Developers can understand how it works.

6. Testability

Individual parts can be tested effectively.

7. Scalability

The system can accommodate increased demand where required.

8. Security

Security requirements are incorporated into the design.


---

12. Example of Poor vs Good Design

Poor design

UniversitySystem
-----------------------------
login()
registerCourse()
payFees()
sendEmail()
generateReports()
connectDatabase()
calculateResults()
uploadAssignment()

Everything is placed into one huge class.


---

Better design

AuthenticationService
RegistrationService
PaymentService
EmailService
ReportService
ResultService
AssignmentService

Each component has a more focused responsibility.


---

PART D — RESPONSIBILITY

13. What Is Responsibility?

A responsibility is something an object or class is responsible for knowing or doing.

For example:

Student

Should know:

studentID
name
programme

Should do:

registerCourse()
dropCourse()


---

Course

Should know:

courseCode
title
credits
capacity

Should do:

hasSpace()


---

Payment

Should know:

amount
date
status

Should do:

process()
refund()


---

14. Responsibility Assignment

One of the central design questions is:

> "Which object should be responsible for this operation?"



Suppose we need to calculate a student's total fees.

Who should do it?

Possibility 1:

Student.calculateFees()

Possibility 2:

FeeAccount.calculateTotal()

Possibility 3:

PaymentService.calculateFees()

The designer must choose based on the responsibilities and relationships of the objects.


---

PART E — COHESION

15. What Is Cohesion?

Cohesion describes how closely related the responsibilities inside a class or module are.

Simple definition:

> High cohesion means a class focuses on closely related responsibilities.




---

16. High Cohesion Example

Course
----------------
courseCode
title
credits
capacity
----------------
hasSpace()
addStudent()
removeStudent()

These responsibilities are closely related to a course.

That's good cohesion.


---

17. Low Cohesion Example

Imagine:

Student
----------------
name
email
----------------
registerCourse()
payFees()
sendSMS()
generatePDF()
connectDatabase()
calculateTax()
compressImage()

This class is doing too many unrelated things.

That's low cohesion.


---

18. Easy Way to Remember Cohesion

Ask:

> "Does everything inside this class belong together?"



If yes:

HIGH COHESION ✓

If no:

LOW COHESION ✗


---

PART F — COUPLING

19. What Is Coupling?

Coupling describes how strongly one class/module depends on other classes/modules.

Simple definition:

> Coupling measures the degree of dependency between software components.



Generally, good OO design aims for:

> Low coupling.




---

20. High Coupling Example

Suppose:

Student
   ↓
Payment
   ↓
Database
   ↓
Email
   ↓
SMS
   ↓
Report

If every class directly depends on every other class, changing one part becomes dangerous.


---

21. Lower Coupling

Instead:

Student
   ↓
RegistrationService
   ↓
Interfaces
   ↓
Specific implementations

Components communicate through clearly defined interfaces.

That makes substitution and testing easier.


---

22. Cohesion vs Coupling

Students must not confuse these.

Cohesion

Looks inside a component.

> "How closely related are the responsibilities within this class?"



Coupling

Looks between components.

> "How strongly does this class depend on other classes?"



Therefore:

GOOD DESIGN

HIGH COHESION
      +
LOW COUPLING

This distinction is foundational to software design.


---

PART G — ABSTRACTION

23. What Is Abstraction?

Abstraction means focusing on the important characteristics of something while hiding unnecessary details.

Example:

When you use an ATM:

Insert card
Enter PIN
Select withdrawal
Enter amount
Receive money

You don't need to know:

How the bank's database works
How encryption works
How the ATM communicates with the bank
How the cash dispenser operates internally

Those details are hidden.


---

24. Abstraction in OO Design

Consider:

PaymentProcessor
----------------
processPayment()

The rest of the application only needs to know:

> "Call processPayment()."



It doesn't necessarily need to know the internal details.


---

PART H — ENCAPSULATION

25. What Is Encapsulation?

Encapsulation means keeping data and the operations that manage that data together while controlling access to the internal state.

Example:

BankAccount
----------------
-balance
----------------
+deposit()
+withdraw()
+getBalance()

The balance is not freely modified from outside.

Instead:

account.deposit(500)

rather than:

account.balance = 500

This helps protect the object's state.


---

26. Abstraction vs Encapsulation

Abstraction

Focuses on:

> What should the user see?



Encapsulation

Focuses on:

> What should the object hide/protect internally?



Example:

ABSTRACTION
----------------
withdraw()
deposit()
getBalance()

ENCAPSULATION
----------------
-hide internal balance
-hide transaction logic
-hide validation rules


---

PART I — SEPARATION OF CONCERNS

27. What Is Separation of Concerns?

Separation of concerns means dividing a system so that different concerns are handled by appropriate parts.

For example:

Presentation
     ↓
Business Logic
     ↓
Data Access
     ↓
Database

Rather than mixing everything together.


---

28. Example

Bad:

LoginScreen
    |
    ├── SQL queries
    ├── password hashing
    ├── authentication logic
    ├── HTML generation
    └── database connection

Better:

Login UI
   ↓
Authentication Service
   ↓
User Repository
   ↓
Database

Each layer has a clearer responsibility.


---

PART J — DESIGN ARCHITECTURE

29. What Is Architecture?

Software architecture is the high-level organisation of a software system.

It determines major:

components;

layers;

interfaces;

dependencies;

communication mechanisms;

deployment decisions.



---

30. Three-Layer Example

A common conceptual structure is:

+-----------------------------+
| Presentation Layer          |
| Web / Mobile / Desktop UI   |
+-----------------------------+
              ↓
+-----------------------------+
| Business Logic Layer        |
| Rules / Services             |
+-----------------------------+
              ↓
+-----------------------------+
| Data Layer                  |
| Repositories / Database     |
+-----------------------------+


---

31. Example: Student Registration

Presentation

Student clicks:

> Register Course



Business Logic

Checks:

Is student active?
Is course available?
Has student met prerequisites?
Does student have outstanding restrictions?
Is there space?

Data Layer

Retrieves:

Student information
Course information
Registration records


---

PART K — DESIGN REFINEMENT

32. What Is Refinement?

Refinement means taking a high-level model and progressively adding detail.

For example:

Analysis class

Student

We then refine it.

Design class

Student
--------------------------------
studentId: String
name: String
email: String
programme: Programme
status: StudentStatus
--------------------------------
registerCourse()
dropCourse()
getRegisteredCourses()

Then implementation might become:

Student.java

or:

Student.cs

or:

Student.ts

depending on the chosen technology.


---

33. Analysis → Design → Code

Think of it as:

REAL-WORLD PROBLEM
        ↓
ANALYSIS MODEL
        ↓
DESIGN MODEL
        ↓
IMPLEMENTATION
        ↓
RUNNING SOFTWARE

IBM describes the design model as an abstraction that can eventually be transformed into application code. 


---

PART L — COMBINING THE THREE MODELS

This is the core of Week 10.

34. The Three OOAD Models

We previously studied:

1. Object Model

Describes the structure of the system.

2. Dynamic Model

Describes how objects change over time and respond to events.

3. Behavioural Model

Describes what the system does and how actors/objects interact.

Now we must combine them.


---

35. Object Model

The Object Model answers:

> "What things/classes exist?"



Example:

Student
Course
Registration
Payment


---

36. Dynamic Model

The Dynamic Model answers:

> "How does the system/object behave over time?"



For example:

Registration

Requested
    ↓
Pending
    ↓
Confirmed

or:

Pending
   ↓
Rejected


---

37. Behavioural Model

The Behavioural Model answers:

> "What does the user/system do?"



Example:

Student
   |
   ↓
Register Course
   |
   ↓
Validate Registration
   |
   ↓
Confirm Registration


---

38. Why Do We Need All Three?

Imagine designing a car.

Knowing:

Wheel
Engine
Brake
Steering

is not enough.

You also need to know:

> What happens when the driver presses the brake?



And:

> How do the brake, wheel and engine-related systems interact?



Similarly, in software:

STRUCTURE
+
BEHAVIOUR
+
TIME/STATE

must fit together.


---

PART M — INTEGRATING THE MODELS

39. Case Study: Online Course Registration

Let's develop a system step-by-step.


---

Requirement

> "A student should be able to register for an available course."




---

40. Step 1 — Behavioural Model

Use case:

Student
   |
   ↓
Register Course


---

41. Step 2 — Identify Objects

We identify:

Student
Course
Registration


---

42. Step 3 — Object Model

We create:

+----------------+
| Student        |
+----------------+
| studentID      |
| name           |
+----------------+

+----------------+
| Course         |
+----------------+
| courseCode     |
| title          |
| capacity       |
+----------------+

+----------------+
| Registration   |
+----------------+
| date           |
| status         |
+----------------+


---

43. Step 4 — Relationships

We might have:

Student 1 -------- 0..* Registration
                         |
                         |
                         |
                       Course

Meaning:

> One student can have zero or many registrations.



And:

> A registration is associated with a course.




---

44. Step 5 — Dynamic Model

Registration might have states:

Requested
    ↓
Validated
    ↓
Confirmed

Possible alternative:

Requested
    ↓
Rejected


---

45. Step 6 — Sequence

Now we ask:

> "How do the objects collaborate?"



Student
   |
   | registerCourse()
   ↓
RegistrationService
   |
   | checkCourse()
   ↓
Course
   |
   | available?
   ↓
Registration
   |
   | confirm()
   ↓
Student


---

46. Step 7 — Design

Now we turn this into an implementable structure:

Student
Course
Registration
RegistrationService
CourseRepository
RegistrationRepository

Now we have moved from analysis toward design.


---

PART N — MODEL CONSISTENCY

47. What Is Model Consistency?

The different models should not contradict each other.

Suppose the class model says:

Course
---------
courseCode
title
capacity

But the sequence diagram says:

Course.checkPrerequisite()

Where is checkPrerequisite()?

If that operation belongs to Course, it should be represented appropriately in the design model.

Otherwise, we have inconsistency.


---

48. Another Example

Use case:

> Student registers for course.



But the sequence diagram shows:

Lecturer → registerCourse()

That's suspicious.

Why?

Because our use case says the actor is:

Student

The models need to agree.


---

49. Traceability

Traceability means being able to follow a requirement through the development artefacts.

For example:

Requirement
"Student can register course"
        ↓
Use Case
"Register Course"
        ↓
Activity Diagram
Registration workflow
        ↓
Sequence Diagram
Object interaction
        ↓
Class Model
Student
Course
Registration
        ↓
Design Classes
RegistrationService
Repositories
        ↓
Code
        ↓
Test Case

This is extremely valuable.

If the requirement changes, developers can identify what models and code may be affected.


---

PART O — SEQUENCE DIAGRAMS IN DESIGN

50. Why Sequence Diagrams Matter

Sequence diagrams show the order of interactions between objects.

OMG classifies sequence diagrams as interaction diagrams, alongside communication, timing and interaction overview diagrams. 

Example:

Student       RegistrationService       Course
   |                  |                   |
   | register()       |                   |
   |----------------->|                   |
   |                  | checkAvailability()|
   |                  |------------------>|
   |                  |<------------------|
   |                  |                   |
   |<-----------------|                   |

This tells us much more than simply saying:

Student
Course
Registration

exist.

It shows how they work together.


---

PART P — CLASS DIAGRAMS IN DESIGN

51. Design Class Diagram

The analysis class:

Student

might become a richer design class:

+--------------------------------+
| Student                        |
+--------------------------------+
| -studentId: String             |
| -name: String                  |
| -email: String                 |
| -status: StudentStatus         |
+--------------------------------+
| +registerCourse(c: Course)     |
| +dropCourse(c: Course)         |
| +getCourses(): List<Course>    |
+--------------------------------+

Notice the additional implementation-oriented information:

visibility;

types;

parameter types;

return types;

operations.


UML 2.5.1 formally defines properties and other modelling constructs used to represent such structural information. 


---

PART Q — INTERFACES

52. What Is an Interface?

An interface defines a set of operations that a class/component agrees to provide.

For example:

+-------------------------+
| <<interface>>           |
| PaymentProcessor        |
+-------------------------+
| +processPayment()       |
+-------------------------+

Then:

PaymentProcessor
              △
              |
       ┌──────┴───────┐
       ↓              ↓
MobileMoney       BankPayment

Different implementations can provide the same interface.


---

53. Why Interfaces Matter

Suppose our university system originally uses:

BankPayment

Later the university wants:

MobileMoneyPayment

If the application depends directly on the concrete bank implementation everywhere, changing it is difficult.

With an interface:

PaymentProcessor
      ↑
      |
BankPayment

and:

PaymentProcessor
      ↑
      |
MobileMoneyPayment

the application can depend on the abstraction.

This reduces unnecessary coupling.


---

PART R — DESIGN PATTERNS

Although design patterns are not explicitly listed as a separate Week 10 topic in the outline, they are useful in understanding modern OO design.

A design pattern is a reusable solution structure for a recurring design problem.

Examples:

Factory;

Observer;

Strategy;

Adapter;

Singleton.


IBM's design guidance notes that design models can be refined using design patterns for recurring or complex structures and processes. 


---

54. Example: Strategy Pattern

Suppose the university accepts:

Bank
Mobile Money
Card

Instead of:

if paymentType == "bank"
   ...
else if paymentType == "mobile"
   ...
else if paymentType == "card"
   ...

everywhere, we can conceptualise:

PaymentStrategy
       ↑
 ┌─────┼─────────┐
 ↓     ↓         ↓
Bank  Mobile    Card

The application can use the appropriate strategy.

This is an example of how design can support flexibility.


---

PART S — MODERN DESIGN PRINCIPLES

55. SOLID

At this level, students should be introduced to the idea that OO design has principles that help us produce maintainable systems.

A popular group is SOLID:

S — Single Responsibility Principle
O — Open/Closed Principle
L — Liskov Substitution Principle
I — Interface Segregation Principle
D — Dependency Inversion Principle

These principles are commonly taught as guidelines for class design and relate closely to cohesion, coupling, abstraction and dependency management. 

We should not treat them as magical rules.

They are design guidelines.


---

56. Single Responsibility Principle

A class should have a focused responsibility rather than accumulating unrelated responsibilities.

Bad:

Student
---------
register()
pay()
sendEmail()
generateReport()
backupDatabase()

Better:

Student
RegistrationService
PaymentService
EmailService
ReportService
BackupService


---

57. Open/Closed Principle

A useful formulation is:

> Software entities should generally be open for extension but closed for modification.



Example:

Instead of modifying a huge payment class every time a new payment method is added, design an abstraction that allows new payment implementations.

PaymentProcessor
       ↑
 ┌─────┼─────────┐
 ↓     ↓         ↓
Bank  Mobile     Card


---

PART T — COMBINING EVERYTHING

58. Complete OO Design Process

For our student registration system:

REQUIREMENT
"Student registers for course"
             ↓
       USE CASE MODEL
             ↓
     BEHAVIOURAL MODEL
             ↓
    Identify interactions
             ↓
       OBJECT MODEL
             ↓
 Student — Registration — Course
             ↓
      DYNAMIC MODEL
             ↓
 Requested → Validated → Confirmed
             ↓
       DESIGN MODEL
             ↓
RegistrationService
CourseRepository
RegistrationRepository
             ↓
        ARCHITECTURE
             ↓
Presentation
Business Logic
Data Access
             ↓
       IMPLEMENTATION
             ↓
            CODE

That is the central lesson of Week 10.


---

PART U — PRACTICAL CLASS

59. Practical Exercise: Design an Online Student Registration System

Students will work in groups or individually.

Requirement

> "A student logs into the university system, searches for a course, selects the course, and registers if all conditions are satisfied."




---

Task 1 — Identify Classes

Students should identify at least:

Student
Course
Registration

Then justify each class.


---

Task 2 — Add Responsibilities

For example:

Student

login()
registerCourse()
dropCourse()

Course

checkAvailability()
checkPrerequisite()

Registration

create()
confirm()
cancel()


---

Task 3 — Create a Class Diagram

Students should show:

classes;

attributes;

operations;

associations;

multiplicities.



---

Task 4 — Create a Sequence Diagram

Show:

Student
   ↓
RegistrationService
   ↓
Course
   ↓
Registration

Students must show the correct order of messages.


---

Task 5 — Create a State Machine

For Registration:

Requested
    ↓
Validated
    ↓
Confirmed

Alternative:

Requested
    ↓
Rejected


---

60. Task 6 — Identify Cohesion and Coupling Problems

Give students this class:

StudentSystem
--------------------------------
login()
registerCourse()
payFees()
sendSMS()
generateReport()
connectDatabase()
calculateResults()
uploadAssignment()

Ask:

1. Is cohesion high or low?


2. Why?


3. Is coupling likely to become high?


4. How could the class be redesigned?




---

PART V — TUTORIAL QUESTIONS

61. Question 1

Define Object-Oriented Design.


---

62. Question 2

Differentiate:

> Object-Oriented Analysis



from:

> Object-Oriented Design.



Give an example.


---

63. Question 3

Explain why a software development team should not immediately begin coding after receiving a requirement.


---

64. Question 4

Explain:

cohesion;

coupling.


Then explain why good OO design generally seeks:

> High cohesion and low coupling.




---

65. Question 5

Differentiate:

abstraction;

encapsulation.


Use a BankAccount example.


---

66. Question 6

Explain the three models:

Object Model
Dynamic Model
Behavioural Model


---

67. Question 7

Explain why the three models must be consistent.


---

68. Question 8

Suppose a use case is:

> "Customer withdraws money."



Identify:

possible classes;

responsibilities;

interactions;

possible states.



---

PART W — EXAMINATION QUESTIONS

69. Essay Question — 25 Marks

> Explain the role of Object-Oriented Design in software development. In your answer, distinguish OO analysis from OO design and discuss how the Object, Dynamic and Behavioural Models can be combined to produce a design suitable for implementation.



Students should include:

definition of design;

analysis vs design;

purpose of design;

design model;

object model;

dynamic model;

behavioural model;

integration;

consistency;

traceability;

example.



---

70. Scenario Question — 20 Marks

A university wants an online student registration system.

The system must allow students to:

log in;

search for courses;

register for courses;

drop courses;

view registered courses.


Required:

a. Identify five possible classes.
b. Assign at least two responsibilities to each.
c. Draw a class diagram.
d. Draw a sequence diagram for course registration.
e. Draw a state diagram for the Registration object.
f. Explain how the three models support one another.


---

71. Short Questions

1.

What is cohesion?

2.

What is coupling?

3.

What is encapsulation?

4.

What is abstraction?

5.

What is a design model?

6.

What is traceability?

7.

What is an interface?

8.

Why are sequence diagrams useful during design?

9.

What is responsibility assignment?

10.

What is the difference between analysis and design?


---

PART X — INDEPENDENT LEARNING — 10 HOURS

Activity 1 — Research

Research:

> "Analysis Model vs Design Model in Object-Oriented Development."



Students should produce approximately 1,500 words.


---

Activity 2 — Case Study

Choose:

Banking system;

Hospital system;

E-learning system;

Mobile money system;

Supermarket system.


Then produce:

Use Case
   ↓
Class Model
   ↓
Sequence Model
   ↓
State Model
   ↓
Design Model


---

Activity 3 — Design Critique

Students should analyse:

class UniversitySystem {
    login();
    registerStudent();
    registerCourse();
    payFees();
    sendSMS();
    sendEmail();
    generateResults();
    printReport();
    connectDatabase();
}

Answer:

1. What is wrong with this design?


2. Is cohesion high or low?


3. What coupling problems might arise?


4. How can it be redesigned?


5. Propose at least five classes/services.




---

PART Y — COMMON STUDENT MISUNDERSTANDINGS

72. "Analysis is just drawing diagrams."

❌ Incorrect.

Analysis involves understanding:

requirements;

domain;

users;

problems;

objects;

behaviour.


UML diagrams are tools for representing the analysis.


---

73. "Design means coding."

❌ Incorrect.

Coding is implementation.

Design determines what the implementation should look like.


---

74. "A class diagram is enough."

❌ Not necessarily.

A class diagram mainly shows structure.

You may also need:

Sequence diagrams
State machines
Activity diagrams
Component diagrams
Deployment diagrams

OMG classifies UML diagrams into structural, behavioural and interaction categories. 


---

75. "More classes always mean better OO design."

❌ Incorrect.

Creating unnecessary classes can make a system unnecessarily complicated.

The objective is not:

> "Create as many classes as possible."



The objective is:

> Create an appropriate structure that clearly represents responsibilities and supports the requirements.




---

76. "Inheritance should always be used."

❌ Definitely not.

Inheritance is useful when a genuine generalisation relationship exists.

Don't use:

Student extends Course

just because both are classes.

😂

Ask the:

> IS-A question.



Is a Student a Course?

No.

Therefore inheritance is inappropriate.


---

PART Z — WEEK 10 MASTER DIAGRAM

Students should understand this diagram thoroughly:

REQUIREMENTS
                              |
                              ↓
                         USE CASES
                              |
                              ↓
                    ┌─────────────────┐
                    │    ANALYSIS     │
                    └────────┬────────┘
                             |
            ┌────────────────┼────────────────┐
            ↓                ↓                ↓
       OBJECT MODEL     DYNAMIC MODEL   BEHAVIOURAL MODEL
            |                |                |
            |                |                |
       "WHAT EXISTS?"   "WHAT CHANGES?"  "WHAT HAPPENS?"
            \                |                /
             \               |               /
              └──────────────┼──────────────┘
                             ↓
                      INTEGRATED MODEL
                             |
                             ↓
                          DESIGN
                             |
            ┌────────────────┼─────────────────┐
            ↓                ↓                 ↓
       ARCHITECTURE      CLASSES          INTERFACES
            ↓                ↓                 ↓
         COMPONENTS     RESPONSIBILITIES    SERVICES
            \                |                 /
             \               |                /
              └──────────────┼───────────────┘
                             ↓
                       IMPLEMENTATION
                             |
                             ↓
                            CODE


---

77. WEEK 10 — THE BIG IDEA

If students remember only one thing from this week, it should be this:

> Analysis tells us what the system needs; design determines how the software will be organised to satisfy those needs.



And the three models we studied earlier are not competing models.

They complement one another:

OBJECT MODEL
"What objects/classes exist?"
        +
DYNAMIC MODEL
"How do objects change over time?"
        +
BEHAVIOURAL MODEL
"How do users and objects interact?"
        ↓
INTEGRATED UNDERSTANDING
        ↓
OBJECT-ORIENTED DESIGN
        ↓
IMPLEMENTABLE SOFTWARE

IBM's design documentation makes this same progression explicit: the analysis model captures the logical structure of the application, while the design model explores architecture and implementation choices and can include design classes, interfaces, packages, sequence/state diagrams, components and deployment views. 


---

78. WEEK 10 QUICK REVISION TABLE

Concept	Student-friendly meaning

Software Design	Deciding how the software will be structured
OO Design	Designing software around objects/classes and their responsibilities
Analysis	Understanding the problem
Design	Planning the software solution
Design Model	More detailed, implementation-oriented model
Responsibility	What a class knows or does
Cohesion	How closely related responsibilities inside a component are
Coupling	How strongly components depend on each other
Abstraction	Showing important things while hiding unnecessary detail
Encapsulation	Protecting internal data/implementation
Interface	Contract describing operations a component provides
Architecture	High-level organisation of the system
Refinement	Adding detail to an existing model
Traceability	Following a requirement through models and implementation
Object Model	Describes system structure
Dynamic Model	Describes states/events over time
Behavioural Model	Describes interactions and system behaviour
Design Pattern	Reusable solution structure for a recurring design problem



---

79. REFERENCES

Authoritative and Current Online Sources

Object Management Group (OMG). Unified Modeling Language (UML) Version 2.5.1. OMG's official UML specification and current UML resources. 

[OMG — UML Official Resources](https://www.omg.org/uml/?utm_source=chatgpt.com)

IBM. Capturing solution architecture in a design model. IBM documentation explaining how the design model builds on the analysis model and incorporates design classes, interfaces, packages, sequence diagrams, state machines, components and deployment views. 

[IBM — Design Model Guidance](https://www.ibm.com/docs/en/dma?topic=approaches-design-model&utm_source=chatgpt.com)

IBM. Capturing application domain in an analysis model. IBM documentation explaining the role of the analysis model as the logical foundation for subsequent design. 

[IBM — Analysis Model Guidance](https://www.ibm.com/docs/en/dma?topic=approaches-analysis-model&utm_source=chatgpt.com)

Hu, C. (2023). An Introduction to Software Design: Concepts, Principles, Methodologies, and Techniques. Springer. The book covers software design principles, UML, design trade-offs, patterns, components, frameworks and microservices. 

[Springer — An Introduction to Software Design](https://link.springer.com/book/10.1007/978-3-031-28311-6?utm_source=chatgpt.com)

IBM Rational. Rational Unified Process for System z. IBM Redbooks. Useful for understanding how analysis/design fits into iterative development and how disciplines evolve across UP phases. 


---

Prescribed Course Texts

Mach, E. (2019). Object Oriented Analysis & Design Cookbook: Introduction to Practical System Modeling.

Reddy, V., & Korra, S. (2018). Object-Oriented Analysis and Design Using UML.

The Art of Service. (2021). Object Oriented Analysis and Design: A Complete Guide.


Recommended Texts

Wixom, B., & Dennis, A. (2018). Systems Analysis and Design.

Blokdyk, G. (2021). Object-Oriented Analysis and Design Standard Requirements.

Wixom, B., & Dennis, A. (2020). Systems Analysis and Design: An Object-Oriented Approach with UML.



---

WEEK 10 IN ONE SENTENCE

> Object-Oriented Design takes the requirements and analysis models developed in earlier weeks and transforms them into a coherent, detailed, maintainable software structure by combining objects/classes, behaviour, states, interactions, responsibilities, architecture and interfaces.
