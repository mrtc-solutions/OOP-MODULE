BICT 3202 — OBJECT-ORIENTED ANALYSIS AND DESIGN

WEEK 13: MULTILAYER SYSTEMS, REUSABLE COMPONENTS AND ARCHITECTURAL DESIGN

Programme: BSc in Information Communication and Technology
Year: Three
Course Code: BICT 3202
Week: 13 of 16
Module: Object-Oriented Analysis and Design
Lecture: 2 hours
Tutorial: 1 hour
Practical: 1 hour
Independent Learning: 10 hours
Credits: 10


---

1. WHERE WEEK 13 FITS INTO THE COURSE

We are now entering an important part of the original syllabus.

Recall the learning outcome:

> "Express the value of designing a multilayer system built of reusable and adaptable components."



This is the main focus of Week 13.

The progression is intentional:

Earlier weeks

Students learned:

> What is a system?



> What are its requirements?



> How can we identify objects?



> How can we model those objects?



> How do objects behave and interact?



Week 10–11

We moved into:

> Object-Oriented Design



We started turning analysis models into a design that could actually be implemented.

Week 12

We asked:

> How do all the different models fit together?



We integrated:

use cases;

classes;

sequences;

activities;

states;

packages;

architecture.


Week 13

Now we ask:

> How should we organise the software so that it is easier to maintain, reuse, replace and adapt?



That leads us to:

architectural layers;

components;

interfaces;

dependencies;

reusable components;

adaptable components;

separation of concerns;

coupling;

cohesion;

package organisation;

component diagrams;

deployment thinking.


UML provides structural diagram types including class, component, package and deployment diagrams, which are particularly relevant to today's lesson. 


---

2. WEEK 13 LEARNING OUTCOMES

By the end of this week, students should be able to:

1. Explain the meaning of software architecture in OOAD.


2. Explain multilayer architecture.


3. Identify common software layers.


4. Explain separation of concerns.


5. Explain the relationship between layers and objects.


6. Define a software component.


7. Explain component interfaces.


8. Explain reusable components.


9. Explain adaptable components.


10. Explain coupling and cohesion in architectural design.


11. Identify inappropriate dependencies.


12. Draw a basic UML component diagram.


13. Explain package organisation.


14. Explain how components interact across layers.


15. Explain the benefits and limitations of multilayer architecture.


16. Integrate component and architectural thinking into an OOAD solution.




---

PART A — WHAT IS SOFTWARE ARCHITECTURE?

3. Start With a Simple Question

Imagine that a university tells a programmer:

> "Build us an online registration system."



The programmer could create hundreds of classes.

But there is another question:

> How should those classes be organised?



For example:

Should the class responsible for displaying a web page also:

validate passwords?

calculate fees?

communicate directly with the database?

send emails?

create student registrations?


It could technically be programmed that way.

But it would become difficult to understand and maintain.

Therefore, OOAD does not only ask:

> "What objects do we need?"



It also asks:

> "How should those objects and components be organised?"



That is where software architecture becomes important.


---

4. Simple Definition of Software Architecture

Software architecture is the high-level organisation of a software system, including its major parts, their responsibilities, relationships and interactions.

Think of architecture as the overall plan of the software.

For example:

University Registration System
            |
    ┌───────┼────────┐
    ↓       ↓        ↓
 Student  Course  Registration

At a higher level, however:

User Interface
      ↓
Application Services
      ↓
Business/Domain Logic
      ↓
Data Access
      ↓
Database

The second diagram is describing architecture.


---

5. Architecture vs Class Design

This distinction is important.

Class design asks:

> What classes do we need?



Example:

Student
Course
Registration
Payment

Architecture asks:

> How should these classes and other software elements be organised?



For example:

Presentation Layer
       ↓
Registration Service
       ↓
Registration Domain
       ↓
Repository
       ↓
Database

Therefore:

> Architecture is broader than individual class design.




---

PART B — MULTILAYER ARCHITECTURE

6. What Is a Layer?

A layer is a logical grouping of related responsibilities.

Think of a school building.

You might have:

3rd Floor → Administration
2nd Floor → Classrooms
1st Floor → Library
Ground    → Reception

Each floor has a different purpose.

Similarly, software can be divided into layers.


---

7. Basic Four-Layer Architecture

A common conceptual structure is:

+----------------------------------+
| PRESENTATION LAYER              |
+----------------------------------+
                ↓
+----------------------------------+
| APPLICATION / SERVICE LAYER     |
+----------------------------------+
                ↓
+----------------------------------+
| DOMAIN / BUSINESS LAYER          |
+----------------------------------+
                ↓
+----------------------------------+
| DATA ACCESS / INFRASTRUCTURE     |
+----------------------------------+
                ↓
+----------------------------------+
| DATABASE                         |
+----------------------------------+

Let's understand every layer rather than simply memorising the names.


---

PART C — PRESENTATION LAYER

8. What Is the Presentation Layer?

This is the part of the application that interacts with the user.

Examples:

web pages;

mobile screens;

desktop windows;

forms;

buttons;

menus;

dashboards.


For example:

+--------------------------------+
| University Registration        |
|                                |
| Course: BICT 3202              |
|                                |
| [ Register ]                   |
+--------------------------------+

This belongs to the presentation side.


---

9. What Should the Presentation Layer Do?

It should primarily handle:

displaying information;

collecting user input;

basic input formatting;

sending requests to application services;

displaying responses.


It should not normally contain all the business rules.

For example, don't put:

if course.capacity > registeredStudents

throughout every user interface.

Why?

Because you might have:

web application;

Android application;

iOS application;

desktop application.


If every interface contains the same business logic, changing one rule could require changing several applications.


---

PART D — APPLICATION/SERVICE LAYER

10. What Is the Application Layer?

This layer coordinates application operations.

For example:

RegistrationService

could provide:

registerStudent()
dropCourse()
getRegisteredCourses()

It receives a request from the presentation layer and coordinates the necessary objects.


---

11. Example

Student clicks:

> Register



The flow might be:

Web Page
   ↓
RegistrationController
   ↓
RegistrationService
   ↓
Course
   ↓
Student
   ↓
Registration

The UI does not need to know every internal detail.


---

PART E — DOMAIN/BUSINESS LAYER

12. What Is the Domain Layer?

This is where the core business concepts and rules live.

For our university system:

Student
Course
Registration
Programme
Semester

The domain layer might contain rules such as:

> A student cannot register for a course if the student has not satisfied its prerequisite.



Another rule:

> A course cannot accept registrations after reaching its capacity.



These are business rules.


---

13. Why Is This Separation Important?

Imagine the university changes its rule.

Old rule:

> Students can register for a maximum of 6 courses.



New rule:

> Students can register for a maximum of 8 courses.



If the business rule is properly centralised, the change may be made in one appropriate place.

If the rule is duplicated across:

website;

mobile app;

desktop application;

reports;


the developer has much more work.

This is one reason separation of responsibilities matters.


---

PART F — DATA ACCESS LAYER

14. What Does the Data Access Layer Do?

This layer handles communication with data storage.

Examples:

StudentRepository
CourseRepository
RegistrationRepository

For example:

RegistrationService
        ↓
RegistrationRepository
        ↓
Database

The service asks:

> "Give me this student's registrations."



The repository handles the mechanics of retrieving them.


---

15. Why Not Let Every Class Access the Database?

Imagine:

Student → Database
Course → Database
Registration → Database
Payment → Database
Report → Database

Now many parts of the application depend directly on the database.

Changing the database technology could affect many classes.

Instead:

Student
Course
Registration
      ↓
Repositories
      ↓
Database

reduces direct dependencies.


---

PART G — THE COMPLETE MULTILAYER MODEL

16. University Registration Example

┌─────────────────────────────────────────┐
│           PRESENTATION                   │
│ Web UI / Mobile UI / Desktop UI         │
└────────────────────┬────────────────────┘
                     ↓
┌─────────────────────────────────────────┐
│           APPLICATION                   │
│ RegistrationService                     │
│ AuthenticationService                   │
│ CourseService                           │
└────────────────────┬────────────────────┘
                     ↓
┌─────────────────────────────────────────┐
│             DOMAIN                      │
│ Student                                 │
│ Course                                  │
│ Registration                            │
│ Programme                               │
└────────────────────┬────────────────────┘
                     ↓
┌─────────────────────────────────────────┐
│          DATA ACCESS                    │
│ StudentRepository                       │
│ CourseRepository                        │
│ RegistrationRepository                  │
└────────────────────┬────────────────────┘
                     ↓
┌─────────────────────────────────────────┐
│             DATABASE                    │
└─────────────────────────────────────────┘

This is the central example for today's lecture.


---

PART H — SEPARATION OF CONCERNS

17. What Is Separation of Concerns?

This means:

> Different parts of the system should concentrate on different responsibilities.



For example:

Presentation → User interaction
Application  → Use-case coordination
Domain       → Business rules
Data Access  → Data persistence

Instead of one huge class doing everything:

EverythingSystem.java

😂


---

18. Bad Example

Imagine:

StudentRegistration.java

contains:

displayHTML()
validatePassword()
connectDatabase()
calculateFees()
registerCourse()
sendEmail()
generatePDF()
checkPrerequisite()

This class has too many responsibilities.

It becomes difficult to:

test;

modify;

reuse;

understand.



---

19. Better Design

Separate responsibilities:

StudentController
RegistrationService
Course
Registration
PaymentService
EmailService
RegistrationRepository

Now each part has a clearer purpose.


---

PART I — COHESION

20. What Is Cohesion?

Cohesion asks:

> "How closely related are the responsibilities within one class or component?"



High cohesion is generally desirable.

For example:

RegistrationService

containing registration-related operations is reasonably cohesive.

But:

RegistrationService

containing:

registration;

payroll;

image editing;

email;

weather forecasting;


would have poor cohesion.

😂


---

21. Simple Rule

Tell students:

> A good class should have a clear reason for existing.



If you need five minutes to explain what a class does, its responsibilities may be too broad.


---

PART J — COUPLING

22. What Is Coupling?

Coupling describes how strongly one software element depends on another.

Imagine:

Class A → Class B

Class A depends on Class B.

If A depends heavily on B's internal implementation, changing B can cause problems in A.


---

23. High Coupling

Consider:

WebPage
   ↓
MySQLDatabase
   ↓
SQL statements

The web page knows:

database technology;

table names;

SQL syntax;

connection details.


That creates strong coupling.


---

24. Lower Coupling

Instead:

WebPage
   ↓
RegistrationService
   ↓
RegistrationRepository
   ↓
Database

The web page doesn't need to know how the database works.

This provides a cleaner separation.


---

25. Coupling and Cohesion Together

A useful OO design principle is:

> Aim for high cohesion and appropriately low coupling.



In simple language:

High cohesion

> "Keep related responsibilities together."



Low coupling

> "Avoid unnecessary dependencies between different parts."




---

PART K — WHAT IS A SOFTWARE COMPONENT?

26. Definition

A software component is a modular part of a system that encapsulates functionality and interacts with other parts through defined interfaces.

Microsoft's current UML guidance describes component diagrams as a way to partition a system into cohesive components, while deployment diagrams show how software and hardware are configured at runtime. 


---

27. Component vs Class

Students often ask:

> "Is a component just a class?"



No.

A class is typically a programming/model element representing objects with:

attributes;

operations;

relationships.


A component is a larger modular unit.

For example:

Classes:

Student
Course
Registration

could collectively contribute to:

Registration Component


---

28. Think About a Car

A car has components such as:

Engine
Transmission
Braking System
Entertainment System

The engine itself contains many parts.

Similarly:

Payment Component

could internally contain:

PaymentService
Payment
PaymentRepository
PaymentValidator

The external system doesn't necessarily need to know every internal class.


---

PART L — COMPONENT INTERFACES

29. Why Do Components Need Interfaces?

Imagine your university system has a payment component.

You want it to support:

processPayment()

The registration system doesn't necessarily care whether payment is processed through:

bank;

mobile money;

debit card;

credit card.


It cares about the service it can request.


---

30. Interface Example

┌──────────────────────┐
             │ Payment Interface    │
             │                      │
             │ processPayment()     │
             │ refundPayment()      │
             └──────────┬───────────┘
                        ↑
                implemented by
                        |
       ┌────────────────┼────────────────┐
       ↓                ↓                ↓
 MobileMoney       BankGateway       CardGateway

Now the system can potentially replace one payment implementation with another without rewriting every client.


---

31. Why Interfaces Promote Reuse

Suppose the university initially uses:

MobileMoneyPayment

Later, it adds:

BankPayment

If both implement the same interface:

PaymentGateway

the registration application can work with the abstraction.

That is an important OO design principle.


---

PART M — REUSABLE COMPONENTS

32. What Does "Reusable" Mean?

A reusable component is a software component designed so that it can be used in more than one context without rebuilding it from scratch.

For example:

Authentication Component

could potentially be used by:

University Portal
Library System
Student Mobile App
Staff Portal


---

33. Example

Suppose we develop:

AuthenticationService

with functionality for:

login()
logout()
changePassword()
resetPassword()

Rather than rewriting authentication for every application, we could design it as a reusable service/component.


---

34. Benefits of Reuse

Reuse can provide:

reduced development effort;

reduced duplication;

consistency;

easier maintenance;

faster development;

potentially fewer defects when mature components are reused appropriately.


However, reuse is not automatically beneficial.

A component that is extremely difficult to adapt may cost more to reuse than to rebuild.


---

PART N — ADAPTABLE COMPONENTS

35. What Is Adaptability?

An adaptable component can be modified, configured or extended to work in different situations.

For example:

NotificationComponent

could support:

Email
SMS
Push Notification

instead of being hard-coded for email only.


---

36. Poorly Adaptable Design

Imagine:

EmailNotification.java

contains everything:

sendEmail()

and assumes:

Gmail
HTML
specific sender
specific message format

If the university wants SMS, developers may have to rewrite much of it.


---

37. More Adaptable Design

Instead:

NotificationService
        |
        +---- EmailNotification
        |
        +---- SMSNotification
        |
        +---- PushNotification

The system can potentially support additional notification methods.


---

PART O — REUSE AND INHERITANCE

38. Is Inheritance Always the Best Way to Reuse Code?

No.

This is an important design lesson.

Students sometimes learn:

> "Inheritance means reuse."



Then conclude:

> "Therefore, whenever I want reuse, I should use inheritance."



That is incorrect.

Inheritance represents an is-a relationship.

Example:

Administrator
      is a
       ↓
      User

But:

RegistrationService
      is a
       ↓
Database

doesn't make sense.

That's not inheritance.


---

39. Composition for Reuse

Sometimes composition is better.

For example:

RegistrationService
        |
        | uses
        ↓
NotificationService

The registration service has/uses a notification service.

It isn't a type of notification service.

This is an important OO design distinction.


---

PART P — COMPONENT DIAGRAM

40. What Is a Component Diagram?

A UML component diagram shows the organisation and relationships of software components.

OMG identifies the component diagram as one of UML's structural diagram types. 


---

41. University System Component Diagram

A simplified representation:

┌─────────────────────┐
│ Web Application     │
└──────────┬──────────┘
           |
           ↓
┌─────────────────────┐
│ Authentication      │
│ Component           │
└──────────┬──────────┘
           |
           ↓
┌─────────────────────┐
│ Registration        │
│ Component           │
└──────┬─────────┬────┘
       |         |
       ↓         ↓
┌───────────┐ ┌───────────────┐
│ Course    │ │ Notification  │
│ Component │ │ Component     │
└─────┬─────┘ └───────────────┘
      |
      ↓
┌─────────────────────┐
│ Database Component  │
└─────────────────────┘

This is a conceptual diagram, but students should learn to represent the same idea using proper UML component notation in a CASE tool.


---

PART Q — PACKAGES

42. What Is a UML Package?

A package groups related model elements.

For example:

+--------------------------+
| Academic                 |
|--------------------------|
| Student                  |
| Course                   |
| Programme                |
| Registration             |
+--------------------------+

Packages help organise large models.

OMG's UML specification defines a package as a namespace that can contain or import model elements. 


---

43. Package Structure

For our university system:

UniversitySystem
│
├── Authentication
│
├── Academic
│
├── Registration
│
├── Finance
│
├── Notification
│
└── Reporting

This makes the system easier to navigate.


---

PART R — PACKAGE VS COMPONENT

44. Students Must Know This Difference

Package

Primarily helps organise model elements.

Example:

Academic
 ├── Student
 ├── Course
 └── Programme

Component

Represents a modular software unit with functionality and interfaces.

Example:

RegistrationComponent

So:

> Package = organisation/grouping



> Component = modular functionality



They can be used together.


---

PART S — DEPENDENCY

45. What Is a Dependency?

A dependency exists when one element relies on another.

For example:

RegistrationService
        |
        | depends on
        ↓
RegistrationRepository

If the repository changes its interface, the service may need to change.


---

46. Too Many Dependencies

Imagine:

A → B
A → C
A → D
A → E
A → F
A → G

A is strongly connected to many elements.

Changing one of those elements may affect A.

A good architectural design tries to control unnecessary dependencies.


---

PART T — DEPENDENCY DIRECTION

47. A Simple Architectural Rule

We generally want dependencies to move in a controlled direction.

For example:

Presentation
      ↓
Application
      ↓
Domain
      ↓
Infrastructure

Instead of:

Presentation ↔ Database
      ↕
Domain ↔ UI
      ↕
Infrastructure ↔ Controllers

where everything depends on everything.

That would become difficult to maintain.


---

PART U — WHY MULTILAYER ARCHITECTURE MATTERS

48. Benefit 1 — Maintainability

Suppose the user interface changes.

If presentation logic is separated from business logic, you can modify the UI without rewriting the entire business layer.


---

49. Benefit 2 — Reuse

A service can potentially support:

Web
Mobile
Desktop

rather than each interface implementing its own business logic.


---

50. Benefit 3 — Testability

A business service can potentially be tested independently from the graphical interface.

For example:

RegistrationService

can be tested with automated tests without manually clicking buttons on a web page.


---

51. Benefit 4 — Adaptability

Suppose the university moves from:

MySQL

to:

PostgreSQL

A well-designed data-access boundary can reduce the amount of application code that must change.


---

52. Benefit 5 — Team Development

Different teams can work on different areas.

For example:

Team A → Presentation
Team B → Application
Team C → Domain
Team D → Data Access

Clear boundaries can make collaboration easier.


---

PART V — LIMITATIONS OF MULTILAYER ARCHITECTURE

53. Is More Layers Always Better?

No.

This is important.

Students shouldn't leave this lecture thinking:

> "The more layers, the better the system."



Not necessarily.


---

54. Problem 1 — Additional Complexity

Instead of:

Controller → Database

you may have:

Controller
 ↓
Service
 ↓
Domain
 ↓
Repository
 ↓
Database

This introduces additional abstractions.


---

55. Problem 2 — Performance Overhead

Every additional abstraction or network boundary can introduce overhead, depending on the implementation.


---

56. Problem 3 — Overengineering

A tiny application may not need:

15 layers
40 interfaces
100 packages

😂

Architecture should match the problem.


---

57. Problem 4 — Incorrect Layer Responsibilities

If developers start putting business logic randomly into:

controllers;

repositories;

UI components;


the architecture may look layered on paper but be poorly designed in practice.


---

PART W — COMPONENT REUSE CASE STUDY

58. University System

Suppose we have:

Registration Component
Notification Component
Authentication Component
Payment Component

Now the university develops a mobile application.

Instead of rebuilding:

Authentication
Notification
Payment

from scratch, the mobile application could potentially interact with the existing services/components.

Conceptually:

┌───────────────┐
                 │ Web App       │
                 └───────┬───────┘
                         |
                         ↓
              ┌─────────────────────┐
              │ Shared Services     │
              ├─────────────────────┤
              │ Authentication      │
              │ Registration        │
              │ Payment             │
              │ Notification        │
              └─────────┬───────────┘
                        ↑
                 ┌──────┴───────┐
                 │ Mobile App   │
                 └──────────────┘

This illustrates the value of reusable services/components.


---

PART X — ADAPTABILITY CASE STUDY

59. Notification Example

Requirement:

> "The university wants to notify students when registration succeeds."



Initially:

Email

Later:

> "We also want SMS."



Later:

> "We also want mobile push notifications."



A rigid architecture may require major changes.

An adaptable architecture could use:

Notification
    |
    +---- Email
    |
    +---- SMS
    |
    +---- Push

The application asks:

notifyStudent()

rather than being tightly tied to one communication technology.


---

PART Y — COMPONENT DIAGRAM EXERCISE

60. Design This System

Students should model:

> Online Banking System



Possible components:

Customer Interface
Authentication
Account Management
Transaction
Payment
Notification
Database

Conceptual structure:

Customer Interface
        ↓
Authentication
        ↓
Account Management
        ↓
Transaction
     ↙       ↘
Payment    Notification
        ↓
     Database

Students should convert this into a proper UML component diagram.


---

PART Z — PRACTICAL UML NOTATION

61. Important Component Diagram Elements

Students should become familiar with:

component;

interface;

provided interface;

required interface;

dependency;

connector;

port.


They do not need to memorise symbols without understanding them.

For example:

> If Component A requires a service from Component B, the diagram should communicate that dependency.




---

62. Component Interface Example

Conceptually:

┌─────────────────────┐
│ Registration        │
│ Component           │
│                     │
│ registerStudent()   │
│ dropCourse()        │
└──────────┬──────────┘
           |
           | requires
           ↓
     Payment Interface

The point is not merely drawing the interface.

The point is understanding:

> What functionality does one component offer, and what functionality does another component require?




---

PART AA — COMPLETE INTEGRATED ARCHITECTURE

63. Bringing Week 12 and Week 13 Together

Our Week 12 models:

Use Case
Class
Sequence
Activity
State

now connect to Week 13 architecture:

Use Cases
   ↓
Classes
   ↓
Services
   ↓
Components
   ↓
Layers
   ↓
Deployment

A complete conceptual flow:

USER REQUIREMENTS
                     ↓
                USE CASES
                     ↓
             BEHAVIOURAL MODELS
                     ↓
                CLASS MODEL
                     ↓
             DESIGN CLASSES
                     ↓
               COMPONENTS
                     ↓
                ARCHITECTURE
                     ↓
              DEPLOYMENT MODEL
                     ↓
                IMPLEMENTATION

That is the bigger picture students should now understand.


---

PART AB — DEPLOYMENT THINKING

64. From Logical Architecture to Physical Deployment

We have been talking about logical organisation.

Now consider:

> Where does the software actually run?



For example:

Student's Phone
       |
       ↓
Internet
       |
       ↓
Web/Application Server
       |
       ↓
Database Server

This is deployment thinking.

A UML deployment diagram is used to represent the runtime arrangement of software artifacts on nodes. Microsoft similarly describes deployment diagrams as showing how hardware and software elements are configured and deployed. 


---

65. Example

┌───────────────────────┐
│ Student Smartphone    │
│                       │
│ Mobile Application    │
└───────────┬───────────┘
            |
         Internet
            |
            ↓
┌───────────────────────┐
│ Application Server    │
│                       │
│ Registration Service  │
│ Authentication        │
└───────────┬───────────┘
            |
            ↓
┌───────────────────────┐
│ Database Server       │
│                       │
│ University Database   │
└───────────────────────┘

Now students can see the difference between:

Logical architecture

> How software is organised.



Deployment architecture

> Where software executes.




---

PART AC — REUSABILITY DESIGN PRINCIPLES

66. Principle 1 — Clear Interfaces

A component is easier to reuse when other parts interact with it through a well-defined interface.


---

67. Principle 2 — Minimise Unnecessary Dependencies

A reusable component shouldn't depend unnecessarily on one specific application.

Bad:

NotificationComponent
      ↓
Only UniversityRegistrationPage

Better:

NotificationComponent
      ↑
     API
      ↑
Multiple applications


---

68. Principle 3 — Encapsulation

Hide internal implementation details.

For example:

PaymentComponent

might expose:

processPayment()

while hiding:

databaseConnection()
APIKeyHandling()
retryLogic()

from clients.


---

69. Principle 4 — Configuration

Where appropriate, make components configurable rather than hard-coded.

For example:

NotificationComponent

could receive:

channel = SMS

rather than having SMS permanently embedded into the component.


---

PART AD — REUSABILITY DOES NOT MEAN "USE EVERYWHERE"

70. Important Warning

A component should not be made reusable simply because:

> "Reusable is always better."



Suppose we have:

SmallCalculator

and spend three weeks making it into an extremely configurable framework.

That may be unnecessary.

Good design considers:

current requirements;

likely changes;

maintenance cost;

complexity;

reuse opportunities.


Therefore:

> Design for appropriate reuse, not reuse at any cost.




---

PART AE — TUTORIAL — 1 HOUR

Tutorial Exercise 1: Layer Identification

Consider the following:

Student clicks "Register"

RegistrationService checks prerequisites

CourseRepository retrieves course

Course object applies business rule

Database stores registration

Web page displays confirmation

Students must classify each activity into:

Activity	Layer

Student clicks Register	Presentation
RegistrationService	Application
Course business rule	Domain
CourseRepository	Data Access
Database storage	Database
Confirmation display	Presentation



---

Tutorial Exercise 2 — Find the Bad Design

Consider:

StudentController
 ├── HTML generation
 ├── SQL queries
 ├── password validation
 ├── course registration
 ├── email sending
 ├── fee calculation
 └── PDF generation

Ask students:

1. What is wrong?


2. Is cohesion high or low?


3. Is coupling likely to be high or low?


4. Which responsibilities should be moved?


5. Propose a better architecture.




---

Tutorial Exercise 3 — Reusability

A university has:

Web Application
Mobile Application
Desktop Application

All three need:

Login
Logout
Password Reset

Question:

> Should authentication be implemented separately in every application?



Ask students to discuss the advantages and disadvantages of creating a shared authentication component/service.


---

PART AF — PRACTICAL — 1 HOUR

71. Practical Assignment

Students will extend the University Course Registration System from Week 12.

They must now create:

Part A — Package Diagram

Create packages:

Authentication
Academic
Registration
Finance
Notification


---

Part B — Component Diagram

Create components:

Web Application
Mobile Application
Authentication Component
Registration Component
Payment Component
Notification Component
Database

Show their relationships.


---

Part C — Layered Architecture

Organise the system into:

Presentation
Application
Domain
Data Access
Database


---

Part D — Reuse

Identify at least three components that could potentially be reused.

For example:

Authentication
Notification
Payment

Students must explain why each is reusable.


---

Part E — Adaptability

Explain how the system could be changed if:

> The university introduces a mobile application.



Students should identify which components could be reused rather than rebuilt.


---

PART AG — INDEPENDENT LEARNING — 10 HOURS

Assignment

Choose one:

1. Banking System


2. Hospital Management System


3. E-Commerce System


4. University Management System


5. Mobile Money System


6. Library Management System



Design a multilayer object-oriented architecture.

Your submission must contain:

1. System description

Approximately 500 words.

2. Layered architecture

Show:

Presentation
Application
Domain
Data Access
Database

3. Component diagram

At least six components.

4. Package diagram

At least four packages.

5. Reusable components

Identify at least three.

6. Adaptable components

Identify at least two.

7. Explanation

Explain:

why the architecture is layered;

why the components were separated;

how reuse is achieved;

how adaptability is achieved;

how coupling is controlled;

how cohesion is improved.



---

PART AH — EXAMINATION QUESTIONS

Question 1 — 25 Marks

> Explain multilayer architecture in object-oriented design. Using a University Course Registration System as an example, describe the responsibilities of the Presentation, Application, Domain and Data Access layers.




---

Question 2 — 20 Marks

> Differentiate between a UML package and a UML component. Explain how both can be used when designing a large object-oriented system.




---

Question 3 — 25 Marks

> A software company has developed an application in which the user interface directly accesses the database and contains most of the business rules.

a) Identify four problems with this architecture.
b) Propose a multilayer architecture.
c) Explain how your proposed architecture improves maintainability and reuse.




---

Question 4 — 30 Marks

> Design a component-oriented architecture for an online banking system. Your answer should identify the major components, their responsibilities, interfaces and dependencies. Explain how your design promotes reuse and adaptability.




---

PART AI — COMMON STUDENT CONFUSIONS

72. Layer vs Component

These are not the same thing.

A layer is a logical architectural level.

A component is a modular software unit.

For example:

DOMAIN LAYER
   |
   ├── Student Component
   ├── Course Component
   └── Registration Component


---

73. Component vs Class

A class is generally a finer-grained modelling/programming construct.

A component is a modular unit that can encapsulate multiple implementation elements.

Think:

Class
 ↓
Small building block

while:

Component
 ↓
Larger modular building block


---

74. Package vs Layer

A package is primarily an organisational namespace/grouping mechanism.

A layer is an architectural separation based on responsibility.

A package can contain elements associated with a particular architectural layer, but the concepts should not be treated as synonyms.


---

75. Reuse vs Inheritance

Inheritance can support reuse, but:

> Reuse does not automatically require inheritance.



Other approaches include:

composition;

interfaces;

services;

libraries;

frameworks;

configurable components.



---

76. High Cohesion vs Low Coupling

Remember this sentence:

> "Keep related things together and unnecessary dependencies apart."



That's a very useful way of remembering the two concepts.


---

PART AJ — WEEK 13 SUMMARY

This week addressed one of the most important practical aspects of object-oriented design.

We moved from:

> "What classes do I have?"



to:

> "How should I organise those classes into a maintainable software system?"



Students should now understand:

OO DESIGN
                      |
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
     CLASSES       LAYERS       COMPONENTS
        |             |             |
        ↓             ↓             ↓
   Responsibilities  Separation   Modularity
                      |
                      ↓
               REUSE + ADAPTABILITY

The key ideas are:

Multilayer architecture

Divide responsibilities into logical layers.

Separation of concerns

Don't make one part of the system responsible for everything.

High cohesion

Keep closely related responsibilities together.

Low unnecessary coupling

Avoid excessive dependencies between unrelated parts.

Components

Create meaningful modular units of functionality.

Interfaces

Define how components communicate without exposing unnecessary internal details.

Reuse

Design suitable components so they can serve multiple applications or contexts.

Adaptability

Design components so they can accommodate appropriate changes without requiring the entire system to be redesigned.

Packages

Organise large models into understandable groups.

Deployment

Think about where the software will actually execute.


---

77. THE BIGGER 16-WEEK JOURNEY

At this point, students should see the progression clearly:

WEEK 1
Business Needs
      ↓
WEEK 2
Business Software Needs
      ↓
WEEK 3
Object Technology
      ↓
WEEK 4
Principles of Object Modelling
      ↓
WEEK 5
Modelling & UML
      ↓
WEEK 6
UML Building Blocks / Rules / Mechanisms
      ↓
WEEK 7
Object Modelling I
      ↓
WEEK 8
Object Modelling II
      ↓
WEEK 9
Dynamic Modelling
      ↓
WEEK 10
Behavioural Modelling
      ↓
WEEK 11
Unified Software Development Process
      ↓
WEEK 12
Object-Oriented Design & Integrated Modelling
      ↓
★ WEEK 13
MULTILAYER ARCHITECTURE &
REUSABLE/ADAPTABLE COMPONENTS
      ↓
WEEK 14
Design Integration / Advanced OO Design
      ↓
WEEK 15
Complete OOAD Case Study & CASE Tools
      ↓
WEEK 16
Revision, Integration & Examination Preparation

This means Week 13 is directly addressing one of the explicit learning outcomes in the original course outline, rather than being an unrelated additional topic.

The official OMG UML material confirms that UML includes structural views such as class, component, package and deployment diagrams, while behavioural and interaction diagrams provide complementary perspectives. 


---

REFERENCES

1. Object Management Group (OMG). Unified Modeling Language (UML) Specification, Version 2.5.1. The current formal UML specification listed by OMG. 


2. Object Management Group (OMG). What is UML? Overview of UML structural, behavioural and interaction diagrams. 


3. Microsoft Support. UML diagrams in Visio. Current guidance covering class, component, deployment, sequence, activity and state-machine diagrams. 


4. Microsoft Support. Create a UML deployment diagram. Current guidance on deployment diagrams and runtime arrangement of software artifacts. 


5. Sparx Systems. Enterprise Architect UML Package Documentation. Explanation of UML packages and their role in organising model elements. 


6. Mach, E. (2019). Object Oriented Analysis & Design Cookbook: Introduction to Practical System Modeling.


7. Reddy, V. & Korra, S. (2018). Object-Oriented Analysis and Design Using UML.


8. The Art of Service (2021). Object Oriented Analysis and Design: A Complete Guide.


9. Wixom, B. & Dennis, A. (2018). Systems Analysis and Design.


10. Blokdyk, G. (2021). Object-Oriented Analysis and Design Standard Requirements.



Core message for students: A good OO designer does not simply produce many UML diagrams. The designer decides how responsibilities, objects, components and layers should work together, while keeping the system understandable, reusable, adaptable and maintainable.
