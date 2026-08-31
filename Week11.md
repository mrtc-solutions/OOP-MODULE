BICT 3202 — OBJECT-ORIENTED ANALYSIS AND DESIGN

WEEK 11: REFINING THE OBJECT-ORIENTED DESIGN

Programme: BSc in Information Communication and Technology
Year: 3
Course Code: BICT 3202
Week: 11 of 16
Lecture: 2 hours
Tutorial: 1 hour
Practical: 1 hour
Independent Learning: 10 hours
Credits: 10


---

1. WHERE WEEK 11 FITS IN OUR 16-WEEK PLAN

In Week 10, we introduced Object-Oriented Design and learned that:

> Analysis asks what the system needs; design asks how the software should be organised to satisfy those needs.



We also learned how the three major views/models work together:

OBJECT MODEL
"What things/classes exist?"
        +
DYNAMIC MODEL
"How do things change over time?"
        +
BEHAVIOURAL MODEL
"How do users and objects interact?"
        ↓
INTEGRATED SYSTEM UNDERSTANDING
        ↓
OBJECT-ORIENTED DESIGN

Week 11 now goes one step deeper.

We are going to take the models from Week 10 and ask:

> "How do we refine these models into a design that developers can actually implement, maintain, test and extend?"



This is a natural continuation of the Object-Oriented Design section of your syllabus.

The UML standard provides the formal modelling language underpinning many of the diagrams we use in this process; OMG currently lists UML 2.5.1 as its formal UML specification. 


---

2. WEEK 11 TOPICS

This week will cover:

1. Meaning of design refinement


2. Analysis model → design model


3. Identifying design classes


4. Refining class attributes


5. Refining class operations


6. Assigning responsibilities


7. Designing relationships


8. Choosing association vs inheritance


9. Interfaces


10. Abstract classes


11. Dependency management


12. Cohesion


13. Coupling


14. Encapsulation


15. Information hiding


16. Separation of concerns


17. Designing for maintainability


18. Designing for reuse


19. Design traceability


20. Integrated case study


21. Practical UML exercise




---

PART A — WHAT DOES "REFINEMENT" MEAN?

3. The Meaning of Design Refinement

The word refinement simply means:

> Taking something general and making it more detailed and precise.



Imagine saying:

> "I want to build a house."



That's not enough information for a construction team.

You eventually need:

Number of rooms
Room dimensions
Door locations
Window locations
Electrical layout
Water pipes
Materials
Foundation
Roof

You started with a general idea and progressively added detail.

Software design works in the same way.


---

4. Software Design Refinement

Suppose during analysis we identified:

Student
Course
Registration

That's useful, but a programmer still needs more information.

We refine it into:

Student
--------------------------------
studentId : String
name : String
email : String
status : StudentStatus
--------------------------------
registerCourse()
dropCourse()

Now we're giving the developer much more information.

The design model becomes increasingly precise as it moves toward implementation.


---

5. Analysis Class vs Design Class

This distinction is very important for examinations.

Analysis class

Usually represents an important concept in the problem domain.

For example:

Student
Course
Registration

Design class

Adds details required to implement the solution.

For example:

+----------------------------------+
| Student                          |
+----------------------------------+
| -studentId : String              |
| -name : String                   |
| -email : String                  |
| -status : StudentStatus          |
+----------------------------------+
| +registerCourse(c : Course)      |
| +dropCourse(c : Course)          |
| +getRegisteredCourses()          |
+----------------------------------+

Notice what happened?

We moved from:

> "There is a Student concept."



to:

> "Here is how the software will represent and manipulate Student."




---

PART B — IDENTIFYING DESIGN CLASSES

6. What Is a Design Class?

A design class is a class defined with enough structural and behavioural detail to contribute to the implementation of the system.

It may contain:

attributes;

operations;

visibility;

types;

parameters;

return values;

relationships;

interfaces;

constraints.


UML provides formal constructs for representing classes, properties, operations and relationships. 


---

7. Example: University System

Suppose our requirement is:

> "Students can register for courses online."



During analysis, we identify:

Student
Course
Registration

But during design, we may discover that we also need:

RegistrationService
StudentRepository
CourseRepository
RegistrationRepository
AuthenticationService

Why?

Because the design must answer not just:

> "What concepts exist?"



but also:

> "What software components are required to make the system work?"




---

8. Entity, Boundary and Control Classes

A useful way of thinking about analysis/design classes is to distinguish different roles.

Entity class

Represents information or concepts that are important to the business/domain.

Examples:

Student
Course
Registration
Payment
Invoice


---

Boundary class

Handles interaction between the system and external actors.

Examples:

LoginPage
RegistrationForm
StudentDashboard
PaymentScreen


---

Control class

Coordinates activities or use-case logic.

Examples:

RegistrationController
PaymentController
LoginController

So we could have:

Student
    ↓
RegistrationPage
    ↓
RegistrationController
    ↓
Registration
    ↓
Course


---

PART C — REFINING ATTRIBUTES

9. What Is an Attribute?

An attribute represents information maintained by an object.

Example:

Student
----------------
studentId
name
email
programme

But a design should eventually specify types.

Student
----------------------------
studentId : String
name : String
email : String
programme : String


---

10. Choosing Appropriate Attributes

Suppose someone proposes:

Student
------------------
name
age
address
everything

😂

everything obviously isn't a useful attribute.

A good designer asks:

> "What information does the object actually need to fulfil its responsibilities?"




---

11. Attribute Example

For a Course:

Course
--------------------------
courseCode : String
title : String
credits : Integer
capacity : Integer

Possible operations:

hasAvailableSpace()
addStudent()
removeStudent()


---

PART D — REFINING OPERATIONS

12. What Is an Operation?

An operation represents something an object can do.

For example:

Student
----------------
registerCourse()
dropCourse()

In a design model we can become more precise:

registerCourse(course : Course) : Registration

This tells us:

operation name = registerCourse

input = Course

return value = Registration



---

13. Why Are Operation Signatures Important?

Compare:

register()

with:

registerCourse(course : Course) : Registration

The second tells the developer much more.

It communicates:

> "This operation expects a Course object and produces a Registration."



That's design refinement.


---

PART E — RESPONSIBILITY-DRIVEN DESIGN

14. What Is Responsibility Assignment?

A major design question is:

> Which object should perform a particular operation?



Suppose we need to check whether a course has available spaces.

Should we write:

Student.checkCourseAvailability()

or:

Course.hasAvailableSpace()

The second is usually more logical because availability is a property of the course.

Therefore:

Course
----------------
capacity
currentEnrollment
----------------
hasAvailableSpace()


---

15. Another Example

Requirement:

> "A student should be able to register for a course."



Possible responsibility:

Student.registerCourse()

But as the system becomes more complex, registration may involve:

prerequisite checking;

timetable conflicts;

financial restrictions;

course capacity;

registration deadlines.


We may therefore introduce:

RegistrationService

which coordinates the process.

Student
   |
   | requests registration
   ↓
RegistrationService
   |
   ├── checks Student
   ├── checks Course
   ├── checks prerequisites
   └── creates Registration

This is a design decision.


---

PART F — COHESION

16. Reminder: What Is Cohesion?

Cohesion asks:

> "How closely related are the responsibilities inside this class or component?"



Good design generally aims for high cohesion.

Research into OO design quality continues to identify cohesion and coupling as important design-quality considerations. 


---

17. High Cohesion

Course
---------------------
courseCode
title
capacity
credits
---------------------
hasSpace()
addStudent()
removeStudent()

Everything is about the course.

Therefore:

> High cohesion.




---

18. Low Cohesion

Course
---------------------
courseCode
title
---------------------
registerStudent()
sendEmail()
calculateSalary()
generatePDF()
compressImage()
backupDatabase()

What does salary calculation have to do with a course?

Nothing.

Therefore:

> Low cohesion.




---

PART G — COUPLING

19. What Is Coupling?

Coupling describes the degree of dependency between software components.

Think of two houses.

House A

Every house system is connected directly to every other system.

Electricity ↔ Plumbing
     ↕            ↕
Heating ↔ Security
     ↕            ↕
Kitchen ↔ Bathroom

Changing one thing becomes difficult.


---

House B

Systems have clear boundaries.

Software should similarly avoid unnecessary dependencies.


---

20. High Coupling

Imagine:

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
Reports

Changing the database might affect payment, email, reports and student logic.

That's undesirable.


---

21. Lower Coupling Through Interfaces

Instead:

PaymentService
      |
      ↓
PaymentGateway
      ↑
 ┌────┴──────┐
 ↓           ↓
Bank       MobileMoney

PaymentService doesn't need to know every implementation detail.

It depends on the abstraction.

This kind of dependency management is closely related to established OO design principles such as Dependency Inversion and Interface Segregation. 


---

PART H — INTERFACES

22. What Is an Interface?

An interface is essentially a contract.

It says:

> "Any class implementing me must provide these operations."



Example:

<<interface>>
PaymentGateway
-------------------------
processPayment()
refundPayment()

Then:

PaymentGateway
                    △
                    |
          ┌─────────┴─────────┐
          ↓                   ↓
     BankGateway        MobileGateway


---

23. Why Are Interfaces Useful?

Imagine a university initially accepts bank payments.

BankGateway

Later it adds mobile money.

Without good design, developers might have to modify many parts of the application.

With an interface:

PaymentGateway
      ↑
 ┌────┴─────┐
 ↓          ↓
Bank       Mobile

the rest of the system can communicate with the common contract.


---

24. Real-World Analogy

Think about a wall socket.

Your phone charger doesn't care whether electricity was generated by:

hydro;

solar;

thermal;

wind.


It cares about the interface provided by the electrical system.

Similarly:

Application
     ↓
PaymentGateway

The application doesn't necessarily need to care which concrete payment provider implements the gateway.


---

PART I — ABSTRACT CLASSES

25. What Is an Abstract Class?

An abstract class is a class intended to provide common structure/behaviour for subclasses but is generally not instantiated directly.

Example:

Payment
--------------------
amount
date
process()

Then:

Payment
                △
                |
       ┌────────┴────────┐
       ↓                 ↓
 BankPayment      MobilePayment


---

26. Abstract Class vs Interface

This is another comparison students must understand clearly.

Subtopic: Abstract Classes vs Interfaces

Abstract Class	Interface

Can provide shared implementation	Primarily defines a contract
Can contain state	Typically focuses on required operations
Represents a common base abstraction	Represents a capability/contract
Subclasses inherit from it	Classes implement it
Useful when classes share substantial behaviour	Useful when different classes must conform to the same contract


The exact implementation possibilities depend on the programming language, so students should not assume Java, C#, C++ and other languages treat these constructs identically.


---

PART J — INHERITANCE REFINEMENT

27. Inheritance in Design

We already studied inheritance in Week 6.

Now we revisit it from the design perspective.

Suppose:

Person
   △
   |
Student

This says:

> Student is a kind of Person.



The subclass can inherit appropriate characteristics from the superclass.


---

28. Don't Abuse Inheritance

A common beginner mistake is:

> "I have two classes, so maybe one should inherit from the other."



No.

Inheritance should represent a meaningful generalisation/specialisation relationship.

Ask:

> "Is B genuinely a kind of A?"



Example:

Person
   ↑
Student

Yes.

Course
   ↑
Student

No.

A Student is not a kind of Course.


---

PART K — ASSOCIATION VS INHERITANCE

29. Association

Association means objects/classes are related.

Student -------- Course

Meaning:

> A Student is associated with a Course.




---

30. Inheritance

Inheritance means one class is a specialised form of another.

Person
  △
  |
Student

Meaning:

> Student is a type of Person.




---

31. The Easy Test

Association:

> "HAS/USES/KNOWS/INTERACTS WITH"



Student HAS/TAKES Course

Inheritance:

> "IS-A"



Student IS-A Person

This simple test helps students avoid many modelling mistakes.


---

PART L — ENCAPSULATION AND INFORMATION HIDING

32. Encapsulation

Suppose we have:

BankAccount
----------------------
-balance : Decimal
----------------------
+deposit()
+withdraw()
+getBalance()

The - means private visibility in UML notation.

The balance should not necessarily be freely manipulated from outside.

Instead:

account.withdraw(500)

allows the object to enforce rules.

For example:

if balance < 500
    reject withdrawal


---

33. Why Is This Important?

Imagine:

account.balance = -500000

😬

If external code can directly modify internal state, the object cannot properly protect itself.

Encapsulation allows the class to control how its state changes.


---

PART M — DEPENDENCIES

34. What Is a Dependency?

A dependency exists when one component relies on another.

Example:

RegistrationService
        |
        | depends on
        ↓
CourseRepository

If RegistrationService directly creates and controls a specific repository implementation, coupling can become unnecessarily strong.


---

35. Dependency Injection

A modern design technique is dependency injection.

Instead of:

RegistrationService
    creates
CourseRepository

we can conceptually do:

CourseRepository
       ↓
RegistrationService

The dependency is provided to the service.

For example:

RegistrationService(repository)

Now the service doesn't have to construct the repository itself.

This can improve:

testability;

flexibility;

substitution;

maintainability.


Modern OO design resources continue to discuss dependency injection alongside modularity, boundaries, testing, coupling and cohesion. 


---

PART N — DESIGN FOR TESTABILITY

36. Why Should Design Consider Testing?

Suppose we have:

RegistrationService

and it directly connects to:

RealUniversityDatabase

Testing becomes difficult.

You don't want every automated test to:

connect to production;

create real students;

create real registrations;

modify real data.


Instead, design can allow a test implementation.

RegistrationService
       |
       ↓
RegistrationRepository
       ↑
 ┌─────┴────────┐
 ↓              ↓
RealRepository  FakeRepository

The real repository is used in production.

The fake/test repository can be used during testing.


---

PART O — SEPARATION OF CONCERNS

37. What Is Separation of Concerns?

A concern is a responsibility or area of functionality.

For example:

Authentication
Payments
Registration
Reporting
Notifications

A well-designed system should avoid mixing unrelated concerns unnecessarily.


---

38. University System Example

Instead of:

StudentController
-------------------------
login()
registerCourse()
payFees()
sendSMS()
generateReport()
calculateResults()

we could have:

AuthenticationService
RegistrationService
PaymentService
NotificationService
ReportingService
ResultService

Now each area has a clearer purpose.


---

PART P — LAYERED DESIGN

39. What Is Layered Design?

A layered design divides the system into logical levels.

For example:

+--------------------------------+
| Presentation Layer             |
| Web / Mobile / Desktop         |
+--------------------------------+
               ↓
+--------------------------------+
| Application/Service Layer      |
| Use-case coordination          |
+--------------------------------+
               ↓
+--------------------------------+
| Domain Layer                   |
| Student, Course, Registration  |
+--------------------------------+
               ↓
+--------------------------------+
| Data Access Layer              |
| Repositories / Persistence     |
+--------------------------------+
               ↓
+--------------------------------+
| Database                       |
+--------------------------------+


---

40. Why Use Layers?

Suppose the university changes:

Web application

to:

Mobile application

If the business rules are properly separated from the user interface, much of the underlying logic can remain usable.

This is one reason separation of concerns and modularity matter.


---

PART Q — DESIGN FOR REUSE

41. What Is Reuse?

Reuse means designing software elements so that they can be used again rather than rebuilt unnecessarily.

Examples:

AuthenticationService
PaymentGateway
NotificationService
ReportGenerator

These may potentially be reused by several applications.


---

42. Example

Suppose a university has:

Student Portal
Staff Portal
Mobile App
Library System

All require authentication.

Instead of implementing authentication independently in all four:

Student Portal → Authentication
Staff Portal   → Authentication
Mobile App     → Authentication
Library        → Authentication

we could potentially provide a reusable authentication service/component.


---

PART R — DESIGN FOR CHANGE

43. Why Must Software Be Designed for Change?

Requirements change.

Imagine the university initially says:

> "Students only use email."



Six months later:

> "Add SMS."



Later:

> "Add WhatsApp notifications."



Poor design:

Student
  ↓
Email
  ↓
SMS
  ↓
WhatsApp

Every new notification method requires changing the Student class.

Better:

NotificationService
                     |
              Notification
                Interface
                     △
          ┌──────────┼──────────┐
          ↓          ↓          ↓
        Email        SMS      WhatsApp

The architecture is more adaptable.


---

PART S — DESIGN QUALITY

44. How Do We Judge a Design?

We can ask:

Is it correct?

Does it meet the requirements?

Is it understandable?

Can another developer understand it?

Is it maintainable?

Can it be changed?

Is it testable?

Can individual components be tested?

Is it reusable?

Can useful components be used elsewhere?

Is it flexible?

Can requirements evolve without massive redesign?

Is it appropriately coupled?

Are unnecessary dependencies avoided?

Is it cohesive?

Does each component have a focused purpose?

These qualities are consistent with established research into OO design quality, which identifies maintainability, testability, coupling and cohesion among important considerations. 


---

PART T — DESIGN TRACEABILITY

45. What Is Traceability?

Traceability means being able to follow a requirement through the models and eventually into implementation and testing.

Consider:

Requirement
    ↓
Use Case
    ↓
Activity Diagram
    ↓
Sequence Diagram
    ↓
Class Diagram
    ↓
Design Classes
    ↓
Code
    ↓
Test


---

46. Example

Requirement:

> R01: Students must be able to register for courses.



Traceability:

R01
 ↓
Register Course Use Case
 ↓
Registration Activity Diagram
 ↓
Registration Sequence Diagram
 ↓
Student
Course
Registration
 ↓
RegistrationService
 ↓
registerCourse()
 ↓
Automated Test

If someone asks:

> "Where in the software is Requirement R01 implemented?"



we should be able to trace it.


---

PART U — INTEGRATED CASE STUDY

Now let's put everything together.

47. Scenario

Exploits University wants a system that allows students to register for courses.

The system must:

1. authenticate the student;


2. display available courses;


3. allow the student to select a course;


4. check course availability;


5. check prerequisites;


6. create a registration;


7. confirm the registration;


8. allow the student to view registered courses.




---

48. Step 1 — Use Case

+----------------------+
        | University System    |
        |                      |
Student → Register Course      |
        |                      |
        +----------------------+


---

49. Step 2 — Identify Classes

Possible domain classes:

Student
Course
Registration

Possible design/service classes:

RegistrationService
AuthenticationService
CourseRepository
RegistrationRepository


---

50. Step 3 — Class Design

Student

+--------------------------------+
| Student                        |
+--------------------------------+
| -studentId : String            |
| -name : String                 |
| -email : String                |
+--------------------------------+
| +registerCourse()              |
| +dropCourse()                  |
+--------------------------------+

Course

+--------------------------------+
| Course                         |
+--------------------------------+
| -courseCode : String           |
| -title : String                |
| -capacity : Integer            |
+--------------------------------+
| +hasAvailableSpace()           |
| +checkPrerequisite()           |
+--------------------------------+

Registration

+--------------------------------+
| Registration                   |
+--------------------------------+
| -registrationId : String       |
| -date : Date                   |
| -status : RegistrationStatus   |
+--------------------------------+
| +confirm()                     |
| +cancel()                      |
+--------------------------------+


---

51. Step 4 — Service

+--------------------------------------+
| RegistrationService                  |
+--------------------------------------+
| +register(student, course)           |
| +cancelRegistration(registration)    |
+--------------------------------------+

Why do we need it?

Because registration involves multiple objects.

RegistrationService
        |
        ├── Student
        |
        ├── Course
        |
        └── Registration


---

52. Step 5 — Sequence

Student      RegistrationService       Course       Registration
   |                  |                  |               |
   | register()       |                  |               |
   |----------------->|                  |               |
   |                  | hasSpace()      |               |
   |                  |----------------->|               |
   |                  |<-----------------|               |
   |                  |                  |               |
   |                  | checkPrerequisite()              |
   |                  |----------------->|               |
   |                  |<-----------------|               |
   |                  |                                  |
   |                  | create Registration              |
   |                  |--------------------------------->|
   |                  |                                  |
   |<-----------------|                                  |
   |       confirmation                                  |

Now our behavioural model, object model and design model are working together.


---

53. Step 6 — State Model

The Registration object can have:

create
                   ↓
              [REQUESTED]
                   |
             validation
                   ↓
              [VALIDATED]
                   |
              confirmation
                   ↓
              [CONFIRMED]

Alternative:

[REQUESTED]
     |
 validation fails
     ↓
 [REJECTED]


---

54. Step 7 — Architecture

+----------------------------------+
| Student Web/Mobile Interface     |
+----------------------------------+
                ↓
+----------------------------------+
| RegistrationService              |
| AuthenticationService            |
+----------------------------------+
                ↓
+----------------------------------+
| Student | Course | Registration  |
+----------------------------------+
                ↓
+----------------------------------+
| Repositories                     |
+----------------------------------+
                ↓
+----------------------------------+
| University Database              |
+----------------------------------+

Now we have a much more complete design.


---

PART V — COMMON DESIGN MISTAKES

55. Mistake 1: One Giant Class

UniversitySystem

containing:

login;

payments;

registration;

results;

SMS;

reports;

database access.


Problem

Low cohesion and potentially high coupling.


---

56. Mistake 2: Everything Inherits from Everything

For example:

Student extends Course

❌ Wrong.

There is no meaningful "IS-A" relationship.


---

57. Mistake 3: Direct Database Access Everywhere

Bad:

Student → Database
Course → Database
Payment → Database
Registration → Database

Better:

Student
Course
Payment
Registration
       ↓
Repositories/Data Access
       ↓
Database


---

58. Mistake 4: Exposing Everything

Bad:

public balance
public password
public databaseConnection

This can undermine encapsulation and information hiding.


---

59. Mistake 5: Designing Only for Today's Requirements

A system that works today but becomes extremely expensive to change tomorrow is often poorly designed.

Good design considers reasonable future change without trying to predict everything.


---

PART W — TUTORIAL — 1 HOUR

60. Tutorial Question 1

Explain the difference between:

> Analysis class



and

> Design class.



Use a university system as your example.


---

61. Tutorial Question 2

Consider:

StudentSystem
-------------------------
login()
register()
payFees()
sendEmail()
sendSMS()
generateResults()
connectDatabase()

Questions:

1. Is the class highly cohesive?


2. Explain why.


3. Identify at least five possible classes/services.


4. Explain how your redesign improves the system.




---

62. Tutorial Question 3

Explain the difference between:

Association

and

Inheritance.

Use:

Student
Course
Person

in your answer.


---

63. Tutorial Question 4

Why are interfaces useful in OO design?

Give a payment-system example.


---

PART X — PRACTICAL — 1 HOUR

64. Practical Assignment

Using any UML tool available to you, model:

> An Online University Course Registration System.



Students must produce:

A. Class Diagram

At minimum:

Student
Course
Registration
RegistrationService


---

B. Sequence Diagram

Model:

> Student registers for a course.




---

C. State Diagram

Model:

> Registration lifecycle.



Use at least:

Requested
Validated
Confirmed
Rejected
Cancelled


---

D. Architecture Diagram

Show:

Presentation
Application/Service
Domain
Data Access
Database


---

E. Design Explanation

Students must explain:

1. Why each class exists.


2. Why each responsibility belongs to its assigned class.


3. Where cohesion is high.


4. Where coupling has been reduced.


5. Where encapsulation is used.


6. Where abstraction is used.


7. How the design can accommodate future changes.




---

PART Y — INDEPENDENT LEARNING — 10 HOURS

Activity 1 — Design Critique

Find an existing software system or design example and identify:

classes;

responsibilities;

relationships;

interfaces;

dependencies;

possible cohesion problems;

possible coupling problems.



---

Activity 2 — Redesign

Take this:

HospitalSystem
--------------------------
registerPatient()
diagnosePatient()
prescribeMedicine()
makePayment()
sendSMS()
generateReport()
connectDatabase()

Redesign it into a better OO structure.

Students should explain their decisions.


---

Activity 3 — Research

Research:

> "How do cohesion and coupling affect object-oriented software quality?"



Students should produce a short academic report with references.


---

PART Z — EXAMINATION QUESTIONS

65. Question 1 — 25 Marks

> Explain the process of refining an analysis model into an object-oriented design model. Use an Online Student Registration System to illustrate your answer.



Your answer should discuss:

analysis classes;

design classes;

attributes;

operations;

responsibilities;

relationships;

interfaces;

cohesion;

coupling;

encapsulation;

architecture;

traceability.



---

66. Question 2 — 20 Marks

> "A good object-oriented design should have high cohesion and low coupling." Discuss this statement using suitable examples.




---

67. Question 3 — 20 Marks

> Explain the difference between association, inheritance and interface implementation. Use UML examples to support your answer.




---

68. Question 4 — 25 Marks

A university wants to introduce an online payment system.

The system should support:

bank payments;

mobile-money payments;

card payments.


Design an OO solution that allows new payment methods to be added in the future with minimal changes to existing code.

Students should provide:

1. class/interface model;


2. relationships;


3. responsibilities;


4. explanation of coupling;


5. explanation of how the design supports reuse and change.




---

PART AA — WEEK 11 REVISION TABLE

Concept	Simple explanation

Design refinement	Adding detail to an existing model
Design class	A class detailed enough to support implementation
Attribute	Data/state belonging to an object
Operation	Something an object can do
Responsibility	What an object knows or does
Cohesion	How closely related responsibilities within a component are
Coupling	How strongly components depend on one another
Interface	A contract for behaviour
Abstract class	A common base abstraction
Encapsulation	Keeping internal state controlled
Information hiding	Hiding unnecessary implementation details
Dependency	A relationship where one element relies on another
Layering	Organising software into logical levels
Reuse	Designing components that can be used again
Traceability	Following requirements through models and implementation



---

69. THE MOST IMPORTANT IDEA OF WEEK 11

Students should leave this week understanding that drawing a UML class diagram is not the same as completing an OO design.

We are moving through:

REQUIREMENT
                  ↓
               ANALYSIS
                  ↓
        "Student, Course, etc."
                  ↓
            REFINEMENT
                  ↓
     Attributes + Operations
                  ↓
          Responsibilities
                  ↓
       Interfaces + Dependencies
                  ↓
     Cohesion + Coupling Decisions
                  ↓
             ARCHITECTURE
                  ↓
          IMPLEMENTABLE DESIGN

The goal is not simply to create more diagrams.

The goal is to create a design that is:

> correct, understandable, maintainable, testable, reusable and adaptable.



Research on OO design quality similarly connects design quality with issues such as coupling, cohesion, maintainability and testability. 


---

70. WEEK 10 → WEEK 11 → WEEK 12

The progression should now be very clear:

WEEK 10
OBJECT-ORIENTED DESIGN
"What is design?"
        ↓
WEEK 11
DESIGN REFINEMENT
"How do we turn our models into
a detailed, implementable design?"
        ↓
WEEK 12
INTEGRATED OO DESIGN
"How do we put all the models,
relationships and design decisions
together into a complete system?"

This also keeps us aligned with the original syllabus rather than introducing unrelated material.

References

Object Management Group (OMG). Unified Modeling Language (UML) Specification, Version 2.5.1. OMG identifies UML 2.5.1 as the formal UML specification. 

Noback, M. (2018). Principles of Package Design: Creating Reusable Software Components. Apress/Springer. The work connects reusable component design with cohesion, coupling and SOLID principles. 

Gonzalez, P. (2025). Clean Apex Code: Software Design for Salesforce Developers. Springer. Discusses OO design, modularity, coupling, cohesion, testing, dependency injection and maintainability. 

Recognising Object-Oriented Software Design Quality: A Practitioner-Based Questionnaire Survey. Software Quality Journal, Springer. Discusses OO design quality, coupling, cohesion, maintainability, testability and SOLID principles. 

Mach, E. (2019). Object Oriented Analysis & Design Cookbook: Introduction to Practical System Modeling.

Reddy, V. & Korra, S. (2018). Object-Oriented Analysis and Design Using UML.

The Art of Service (2021). Object Oriented Analysis and Design: A Complete Guide.

Wixom, B. & Dennis, A. (2018). Systems Analysis and Design.

Blokdyk, G. (2021). Object-Oriented Analysis and Design Standard Requirements.
