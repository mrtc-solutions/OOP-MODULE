BICT 3202 — OBJECT-ORIENTED ANALYSIS AND DESIGN

WEEK 9: THE UNIFIED SOFTWARE DEVELOPMENT PROCESS (USDP / UNIFIED PROCESS)

Programme: BSc in Information Communication and Technology
Year: 3
Course Code: BICT 3202
Week: 9 of 16
Lectures: 2 hours
Tutorial: 1 hour
Practical: 1 hour
Independent Learning: 10 hours
Module: Object-Oriented Analysis and Design


---

1. Where Week 9 Fits in the Course

We have now moved from understanding and modelling the system to understanding how an OO system can be developed systematically.

The progression is:

WEEKS 4–6
OBJECT MODELLING
"What objects/classes exist?"
        ↓
WEEK 7
DYNAMIC MODELLING
"How do objects change and respond to events?"
        ↓
WEEK 8
BEHAVIOURAL MODELLING
"How do users and objects interact?"
        ↓
WEEK 9
UNIFIED SOFTWARE DEVELOPMENT PROCESS
"How do we organise the development of the software?"
        ↓
WEEK 10+
OBJECT-ORIENTED DESIGN
"How do we turn the analysis into a software design?"

This distinction is extremely important.

UML tells us how to model a system.

The Unified Process tells us how to organise the work of developing that system.

The Unified Process (UP) is an iterative and incremental software-development process associated strongly with object-oriented development and UML. The Open University describes it as a process that organises development into short, timeboxed iterations and adapts to change. 


---

2. Week 9 Topics from the Official Course Outline

This week's outline contains:

1. The Unified Software Development Process


2. Aspects of the Unified Software Development Process (USDP)


3. Characteristics of USDP / UP


4. Phases and interactions of the UP


5. Process workflows


6. Artefacts of the UP


7. Importance and guidelines of reuse


8. Concurrency


9. Generalisation


10. Inheritance



We will cover all of these.


---

3. Learning Outcomes

By the end of Week 9, students should be able to:

define the Unified Software Development Process;

explain why UP is suitable for object-oriented development;

explain iterative and incremental development;

explain the major characteristics of UP;

distinguish between a phase and an iteration;

explain the four major UP phases;

explain Inception;

explain Elaboration;

explain Construction;

explain Transition;

explain milestones;

explain process workflows/disciplines;

identify important UP artefacts;

explain the relationship between workflows and phases;

explain requirements-driven development;

explain architecture-centred development;

explain risk-driven development;

explain reuse in OO development;

identify opportunities for software reuse;

explain guidelines for effective reuse;

explain concurrency;

explain generalisation;

explain inheritance;

distinguish generalisation from inheritance;

explain how these concepts support object-oriented design.



---

PART A — WHAT IS A SOFTWARE DEVELOPMENT PROCESS?

4. Before Understanding UP

Imagine that a university says:

> "We need an online learning management system."



You have:

business managers;

users;

analysts;

designers;

programmers;

testers;

database specialists;

system administrators.


If everyone simply starts coding, what happens?

Probably:

Analyst: "I thought the system should do X."

Programmer: "I thought it should do Y."

Tester: "I don't know what requirements I'm testing."

Client: "This isn't what we requested."

Manager: "Why are we six months late?"

😂

This is one reason software development needs a process.


---

5. Definition of a Software Development Process

A software development process is an organised set of:

activities;

roles;

responsibilities;

practices;

work products;

decisions;


used to develop and maintain software.

In simple language:

> A software development process tells a development team what work needs to be done, when it should be done, who should do it, and what should be produced.




---

PART B — WHAT IS THE UNIFIED PROCESS?

6. Definition

The Unified Process (UP) is an iterative and incremental software development process designed around object-oriented development.

It became closely associated with UML and use-case-driven software development.

The Open University identifies UP as an iterative and incremental process for building enterprise systems using an object-oriented approach and UML. 

A commercial and particularly well-known implementation of UP is the Rational Unified Process (RUP).


---

7. UP vs RUP

Students often see these terms together.

Unified Process

A general software development process framework.

Rational Unified Process

A specific, commercial implementation of the Unified Process developed by Rational and later associated with IBM.

Therefore:

Unified Process (UP)
        ↓
General process concept
        ↓
Rational Unified Process (RUP)
        ↓
A specific implementation

The Open University notes that RUP is a commercial version/implementation of UP and that there are other implementations. 


---

8. Why Is UP Important in OOAD?

The traditional approach might try to do:

Requirements
      ↓
Analysis
      ↓
Design
      ↓
Coding
      ↓
Testing
      ↓
Deployment

and treat these as largely separate stages.

UP instead encourages repeated cycles:

Requirements
   ↓
Analysis
   ↓
Design
   ↓
Implementation
   ↓
Testing
   ↓
Feedback
   ↓
Improved Requirements
   ↓
Improved Design
   ↓
More Implementation

This happens repeatedly.

That is the heart of iteration.


---

PART C — ITERATIVE AND INCREMENTAL DEVELOPMENT

9. What Does "Iterative" Mean?

Iterative means:

> The team repeats development activities in multiple cycles and improves the system from one cycle to the next.



Think about writing an essay.

You don't necessarily:

Write sentence 1
Write sentence 2
Write sentence 3
...
Submit final essay

Instead, you might:

Draft
 ↓
Review
 ↓
Improve
 ↓
Review
 ↓
Improve
 ↓
Final version

Software can work similarly.


---

10. What Does "Incremental" Mean?

Incremental means:

> The system grows by adding usable functionality over time.



For example, an e-learning system could be developed as:

Increment 1

Login

Increment 2

Login
+
Course registration

Increment 3

Login
+
Course registration
+
Assignment submission

Increment 4

Login
+
Course registration
+
Assignment submission
+
Results

Each increment adds capability.


---

11. Iterative vs Incremental

This is an important distinction.

Iterative	Incremental

Repeatedly refine/improve	Add new functionality
Focuses on learning and improvement	Focuses on growth of system capability
Same area may be revisited	New features are added
Feedback drives refinement	Each increment adds value


In practice, UP uses both.

Therefore:

> UP is iterative AND incremental.



The Open University specifically describes UP as iterative and incremental and notes that its iterations are normally short and timeboxed. 


---

12. What Is an Iteration?

An iteration is a planned development cycle in which the team performs some combination of:

requirements work;

analysis;

design;

implementation;

testing;

evaluation.


At the end of the iteration, the team should have a measurable result.

IBM's current Rational tooling documentation describes iterations as planned, measured intervals and notes that phases can be divided into iterations to deliver incremental value. 


---

13. Example of Iterations

Suppose we are developing:

> University Online Registration System



We might have:

Iteration 1
---------
Login
User registration
Basic database


Iteration 2
---------
Course catalogue
Course search


Iteration 3
---------
Course registration
Prerequisite checking


Iteration 4
---------
Payments
Receipts


Iteration 5
---------
Reports
Administration

Notice that we aren't waiting until the very end to discover whether the system works.

We continuously build and evaluate it.


---

PART D — MAJOR CHARACTERISTICS OF THE UNIFIED PROCESS

14. Four Major Characteristics

A useful way to remember UP is:

UNIFIED PROCESS
                    |
       ┌────────────┼────────────┐
       ↓            ↓            ↓
 Use-Case       Architecture   Iterative
  Driven          Centred     & Incremental
       \            |            /
        \           |           /
             Risk-Driven

The commonly emphasised characteristics include:

1. Use-case driven


2. Architecture-centred


3. Iterative and incremental


4. Risk-focused




---

15. Characteristic 1 — Use-Case Driven

What does this mean?

The system's development is strongly organised around use cases.

Remember Week 8.

We learned:

> A use case describes a goal that an actor wants to achieve using the system.



For example:

Student
   |
   ↓
(Register Course)

The development team can use that use case to drive:

Requirements
     ↓
Analysis
     ↓
Design
     ↓
Implementation
     ↓
Testing


---

16. Example

Suppose:

> UC-01: Register Course



The team identifies:

Requirements

What should registration do?

Analysis

What objects participate?

Student
Course
Registration

Design

What classes/components are needed?

RegistrationController
CourseService
Student
Course

Implementation

Program the functionality.

Testing

Test:

Course available
Course full
Prerequisite missing
Student already registered

Therefore:

> The use case becomes a thread running through multiple development activities.




---

17. Characteristic 2 — Architecture-Centred

UP does not say:

> "Just build features and worry about architecture later."



Instead, the development team establishes and validates a strong architectural foundation early, especially during Elaboration.

IBM's description of RUP states that Elaboration focuses on establishing a stable architecture and addressing high-risk elements. 


---

18. What Is Software Architecture?

Software architecture describes the high-level organisation of a software system.

For example:

+---------------------------+
|       User Interface      |
+---------------------------+
             ↓
+---------------------------+
|      Business Logic       |
+---------------------------+
             ↓
+---------------------------+
|       Data Access         |
+---------------------------+
             ↓
+---------------------------+
|          Database         |
+---------------------------+

This is an architectural view.


---

19. Why Architecture Matters

Suppose you build a university system for:

100 students

and later discover that:

100,000 students

must use it simultaneously.

If your architecture was poorly designed, the system may collapse.

Therefore, UP tries to identify major architectural risks early.


---

20. Characteristic 3 — Iterative and Incremental

We have already covered this.

The system is developed through repeated cycles.

Iteration 1
     ↓
Feedback
     ↓
Iteration 2
     ↓
Feedback
     ↓
Iteration 3
     ↓
Feedback

Each iteration improves or extends the system.


---

21. Characteristic 4 — Risk-Driven

This is extremely important.

A common mistake is:

> "Let's build the easiest things first."



UP encourages teams to identify and address significant risks early.

The PMI explanation of RUP notes that risk identification is pushed early in the lifecycle so that risks can be addressed while there is still opportunity to mitigate them. 


---

22. What Is a Software Risk?

A risk is a potential problem that could negatively affect the project.

Examples:

Technical risk
Security risk
Performance risk
Financial risk
Schedule risk
Requirement risk
Integration risk


---

23. Example of Risk-Driven Development

Suppose we are developing:

> Mobile Banking System



We discover:

> "The system must process 5,000 transactions per second."



That is a major technical risk.

Instead of leaving it until the end, we should test the architecture early.

Similarly:

> "The application must use biometric authentication."



That may be another technical risk.

The team can investigate it during an early iteration.


---

PART E — THE FOUR UP PHASES

24. The Four Major Phases

The Unified Process/RUP lifecycle is commonly represented by four phases:

INCEPTION
    ↓
ELABORATION
    ↓
CONSTRUCTION
    ↓
TRANSITION

Then a new development cycle can begin for future releases.

IBM documentation identifies these four RUP phases as Inception, Elaboration, Construction and Transition. 


---

25. Phase 1 — INCEPTION

Main question:

> "Should we build this system, and what exactly are we trying to build?"



The Inception phase establishes the project's business case, scope and high-level requirements.

IBM's RUP guidance describes Inception as establishing the business case and delimiting project scope, including identifying actors and major use cases. 


---

26. Activities During Inception

The team may:

identify stakeholders;

understand the business problem;

define project scope;

identify major actors;

identify major use cases;

estimate cost;

estimate schedule;

identify major risks;

establish success criteria;

create an initial project plan.



---

27. Example

Suppose a university wants:

> Online Student Registration System



During Inception, we ask:

Who will use it?

Students
Lecturers
Administrators
Finance Officers

What are the major goals?

Register courses
Drop courses
Pay fees
View results
Generate reports

Is it feasible?

Questions include:

Do we have developers?
Do we have funding?
Do we have servers?
Can the system integrate with existing databases?
Can the project be completed on time?


---

28. Inception Deliverables/Artefacts

Typical outputs can include:

Vision document;

initial use-case model;

initial business case;

initial risk assessment;

project plan;

initial glossary;

prototypes where necessary.


IBM's RUP best-practices documentation lists these kinds of outputs and describes the end of Inception as the Lifecycle Objectives Milestone. 


---

29. Lifecycle Objectives Milestone

At the end of Inception, the organisation asks:

> "Do we understand enough about the project to continue?"



If the answer is no:

STOP
or
REDESIGN
or
RETHINK

If yes:

Proceed to Elaboration

This is sometimes called a go/no-go decision.


---

30. Phase 2 — ELABORATION

Main question:

> "Can we build this system successfully, and what architecture should we use?"



Elaboration is one of the most important phases.

Its focus includes:

refining requirements;

analysing the problem domain;

establishing architecture;

addressing major technical risks;

developing a more detailed plan.


IBM describes Elaboration as focusing on a sound architectural foundation and eliminating high-risk elements. 


---

31. Example of Elaboration

Imagine we discover:

> "The system must support 50,000 simultaneous users."



The team investigates:

Database architecture
Server architecture
Network architecture
Security architecture
Caching
Load balancing

They may build a prototype.


---

32. Architectural Prototype

An architectural prototype is a working or partially working implementation used to test important architectural decisions.

For example:

Login
   ↓
Authentication Server
   ↓
Database

The team might build a small prototype to determine:

performance;

security;

scalability;

integration feasibility.


The goal isn't to build the entire system.

The goal is to answer:

> "Will our proposed architecture actually work?"



IBM RUP documentation describes an executable architectural prototype as a way to test architectural feasibility and performance. 


---

33. Lifecycle Architecture Milestone

At the end of Elaboration:

> The team should have enough confidence in the architecture and major requirements to proceed with full-scale construction.



If major risks remain unresolved, the project should not blindly continue.


---

34. Phase 3 — CONSTRUCTION

Main question:

> "Can we build the complete system?"



This is where most detailed implementation takes place.

Activities include:

Analysis
Design
Coding
Integration
Testing
Refinement

The team develops the remaining functionality through iterations.

IBM describes Construction as the phase where the system is built and the remaining use cases are implemented and tested. 


---

35. Example

Our university system might now implement:

Iteration 1
Course registration

Iteration 2
Payments

Iteration 3
Results

Iteration 4
Reports

Iteration 5
Administration

Each iteration produces a more complete system.


---

36. Phase 4 — TRANSITION

Main question:

> "Can real users successfully use the system in the real environment?"



The software moves from:

Development environment
        ↓
Production environment

Activities may include:

deployment;

installation;

user training;

data migration;

beta testing;

fixing defects;

configuration;

user feedback;

final adjustments.


The PMI description of Transition includes deployment preparation, user training, defect correction and final adjustments. 


---

37. Example

Suppose the university system is finished.

The team now:

Install system
      ↓
Import student data
      ↓
Train administrators
      ↓
Train lecturers
      ↓
Pilot with selected students
      ↓
Fix problems
      ↓
Full deployment

That's Transition.


---

38. The Four Phases Compared

Phase	Main Question	Main Focus

Inception	Should we build it?	Scope, business case, major requirements, risks
Elaboration	Can we build it?	Architecture, detailed requirements, major risks
Construction	Can we build the complete product?	Implementation, integration, testing
Transition	Can users successfully use it?	Deployment, training, acceptance, fixes



---

PART F — PHASE ≠ WATERFALL STAGE

39. Important Warning

Students may look at:

Inception → Elaboration → Construction → Transition

and think:

> "This is just waterfall with different names."



No.

The key difference is iteration.

A phase contains one or more iterations.

IBM explicitly describes phases as being divided into iterations, with iterations providing planned intervals for incremental delivery. 


---

40. Visualising UP

Instead of:

Inception
    ↓
Elaboration
    ↓
Construction
    ↓
Transition

think:

UNIFIED PROCESS

        ┌───────────────────────────┐
        │        INCEPTION          │
        │   Iteration 1             │
        │   Iteration 2             │
        └─────────────┬─────────────┘
                      ↓
        ┌───────────────────────────┐
        │       ELABORATION         │
        │   Iteration 1             │
        │   Iteration 2             │
        │   Iteration 3             │
        └─────────────┬─────────────┘
                      ↓
        ┌───────────────────────────┐
        │       CONSTRUCTION        │
        │   Iteration 1             │
        │   Iteration 2             │
        │   Iteration 3             │
        │   ...                     │
        └─────────────┬─────────────┘
                      ↓
        ┌───────────────────────────┐
        │        TRANSITION         │
        │   Iteration 1             │
        │   Iteration 2             │
        └───────────────────────────┘


---

PART G — PROCESS WORKFLOWS / DISCIPLINES

41. What Is a Workflow?

A workflow is a set of related activities performed to achieve a particular development objective.

For example:

> Requirements workflow



contains activities concerned with discovering, documenting and managing requirements.


---

42. Common UP/RUP Workflows

A common RUP representation includes:

Core technical disciplines

1. Business Modeling


2. Requirements


3. Analysis & Design


4. Implementation


5. Test


6. Deployment



Supporting disciplines

7. Configuration & Change Management


8. Project Management


9. Environment



These disciplines are documented in IBM/RUP materials and secondary references on the process. 


---

43. Business Modelling Workflow

Question:

> "How does the organisation/business operate?"



For example, in a university:

Student
   ↓
Apply
   ↓
Admission
   ↓
Registration
   ↓
Learning
   ↓
Assessment
   ↓
Graduation

The analyst needs to understand the business before designing software.


---

44. Requirements Workflow

Question:

> "What does the system need to do?"



Activities include:

identify stakeholders;

gather requirements;

identify actors;

identify use cases;

document functional requirements;

document non-functional requirements;

manage changing requirements.



---

45. Analysis & Design Workflow

Question:

> "How should the system be structured to satisfy the requirements?"



This is directly related to our course.

Activities include:

Class modelling
Object modelling
Interaction modelling
Architecture
Detailed design

This is where the models students have been learning become increasingly important.


---

46. Implementation Workflow

Question:

> "How do we build the software?"



Activities include:

coding;

component development;

integration;

builds;

implementation testing.



---

47. Test Workflow

Question:

> "Does the software work correctly?"



Testing may include:

Unit testing
Integration testing
System testing
Acceptance testing
Performance testing
Security testing


---

48. Deployment Workflow

Question:

> "How do we make the software available to users?"



Activities include:

installation;

configuration;

deployment;

user training;

migration;

release.



---

49. Configuration and Change Management

Question:

> "How do we control changes to the project?"



Example:

Developer A changes:

Login.java

Developer B changes:

Login.java

Without version/change management:

😂:

Which version is correct?

Configuration management helps control versions, changes and project baselines.


---

50. Project Management

This includes:

planning;

scheduling;

budgeting;

risk management;

monitoring;

reporting;

resource management.



---

51. Environment

This supports the development organisation itself.

Examples:

Development tools
UML tools
Coding standards
Process guidelines
Templates
Development platforms


---

PART H — WORKFLOWS DO NOT HAPPEN ONLY ONCE

52. Important Concept

A common student misconception is:

> "First requirements happen, then design, then implementation, then testing."



UP is more flexible.

During an iteration, you can have:

Requirements
   ↓
Analysis
   ↓
Design
   ↓
Implementation
   ↓
Testing
   ↓
Feedback
   ↓
Requirements refinement

Then the next iteration repeats relevant work.

The intensity of each discipline changes across phases rather than each discipline being completely isolated to one phase. IBM's RUP materials illustrate different disciplines having different levels of activity across the four phases and iterations. 


---

53. Example

During Inception:

Requirements ██████████
Design       ██
Coding       █
Testing      █

During Elaboration:

Requirements ███████
Analysis     █████████
Design       ██████████
Coding       ████
Testing      ████

During Construction:

Requirements ███
Design       █████
Coding       ██████████
Testing      █████████

During Transition:

Coding       ███
Testing      █████████
Deployment   ██████████
Training     ███████

The activities overlap.


---

PART I — ARTEFACTS OF THE UNIFIED PROCESS

54. What Is an Artefact?

An artefact is a work product created, modified or used during software development.

In simple terms:

> An artefact is something the development team produces or uses as evidence of its work.




---

55. Examples

Vision Document
Requirements Specification
Use-Case Model
Risk List
Project Plan
Glossary
Class Diagram
Sequence Diagram
Architecture Document
Source Code
Test Plan
Test Cases
Deployment Package
User Manual


---

56. Why Are Artefacts Important?

Imagine the project manager asks:

> "What exactly have we completed?"



You can show:

Requirements document
       +
Use-case model
       +
Architecture model
       +
Source code
       +
Test results

These provide evidence.


---

57. Artefacts Across the Phases

Inception

Possible artefacts:

Vision
Business Case
Initial Use-Case Model
Risk Assessment
Project Plan

Elaboration

Possible artefacts:

Detailed Requirements
Architecture Document
Domain Model
Architectural Prototype
Updated Risk Assessment
Updated Project Plan

Construction

Possible artefacts:

Source Code
Components
Test Cases
Test Results
Working Builds
Updated Models

Transition

Possible artefacts:

Deployment Package
User Documentation
Training Materials
Release Notes
Acceptance Results


---

PART J — REUSE IN OBJECT-ORIENTED DEVELOPMENT

58. What Is Software Reuse?

Software reuse means:

> Using an existing software asset again instead of creating the same functionality from scratch.



Assets may include:

classes;

components;

libraries;

frameworks;

services;

APIs;

design patterns;

architectural components;

documentation.



---

59. Simple Example

Suppose you need:

> User authentication.



Instead of writing authentication completely from scratch, you might reuse an established authentication library or service.

Instead of:

Build authentication from zero

you may:

Existing authentication component
             ↓
        Configure
             ↓
         Integrate
             ↓
          Test


---

60. Why Reuse Matters

Reuse can potentially:

reduce development time;

reduce development cost;

improve consistency;

reduce duplicated code;

leverage tested components;

improve maintainability.


But reuse is not automatically good.


---

61. Problems with Reuse

Suppose someone says:

> "Let's reuse this old library."



You should ask:

Is it secure?
Is it maintained?
Does it fit our requirements?
Is it compatible?
Is its licence acceptable?
Is its performance adequate?
Can we modify it?
Does it introduce dependencies?

Therefore:

> Reuse should be evaluated, not blindly adopted.




---

62. Guidelines for Reuse

Before reusing an existing component, consider:

1. Functional suitability

Does it actually do what we need?

2. Quality

Is it reliable?

3. Security

Does it introduce vulnerabilities?

4. Compatibility

Does it work with our technology stack?

5. Maintainability

Can the organisation maintain it?

6. Licence

Are we legally permitted to use it?

7. Performance

Can it handle the expected workload?

8. Cost

Is reuse actually cheaper?


---

PART K — GENERALISATION

63. What Is Generalisation?

Generalisation is a relationship in which a more general concept represents characteristics shared by more specialised concepts.

Example:

Vehicle
                △
              /   \
             /     \
           Car     Truck

Vehicle is the general concept.

Car and Truck are specialised concepts.


---

64. Real-Life Example

Consider university users:

User
             /    \
            /      \
       Student    Lecturer

Both are Users.

User may have:

userID
name
email
login()
logout()

Student may additionally have:

programme
registerCourse()

Lecturer may have:

employeeNumber
enterMarks()


---

PART L — INHERITANCE

65. What Is Inheritance?

Inheritance is an object-oriented programming mechanism through which a specialised class can acquire accessible attributes and operations from a more general class.

Example:

class User
    name
    email
    login()
    logout()
        ↑
        |
-------------------
        |
class Student
    programme
    registerCourse()

Student inherits relevant features from User.


---

66. Generalisation vs Inheritance

This distinction is important.

Generalisation

Primarily a modelling/design relationship:

Student IS-A User

Inheritance

A programming-language implementation mechanism that can implement such a relationship.

Therefore:

Generalisation
      ↓
Conceptual/design relationship

Inheritance
      ↓
Programming mechanism

Do not simply write:

> "They are the same."



They are closely related, but they are not identical concepts.


---

67. IS-A Test

A useful test for generalisation is:

> "Is X a Y?"



Examples:

Student is a User
Car is a Vehicle
Dog is an Animal
Manager is an Employee

Good candidates for generalisation.

But:

Student has a Course

is not inheritance.

That is a different relationship.


---

PART M — CONCURRENCY

68. What Is Concurrency?

Concurrency means that multiple activities or operations can make progress during overlapping periods.

In simple language:

> More than one thing can be happening at the same time or during overlapping time periods.




---

69. Everyday Example

When ordering food through an application:

Payment processing
        +
Restaurant preparing food

can happen concurrently.

The system doesn't necessarily have to wait for every activity to finish before another begins.


---

70. Software Example

After payment succeeds:

Update Inventory
       +
Generate Receipt
       +
Notify Warehouse
       +
Send Email

Some of these can happen independently.


---

71. Why Concurrency Matters in OOAD

Concurrency affects:

system architecture;

performance;

responsiveness;

resource management;

thread/process design;

synchronisation;

data consistency.


For example:

> What happens if two students attempt to register for the last available place in a course at exactly the same time?



This is a concurrency problem.


---

72. Concurrency Example

Suppose:

Course capacity = 1

Two students:

Student A → Register
Student B → Register

Both systems check:

Available seats = 1

If both then register without proper synchronisation:

Student A → SUCCESS
Student B → SUCCESS

Now:

Registered students = 2
Capacity = 1

That's a serious system error.

Therefore concurrency must sometimes be addressed at the analysis/design level.


---

PART N — HOW EVERYTHING CONNECTS

73. One System, One Process

Let's put everything together.

Suppose we are developing:

> University E-Learning System




---

Inception

Ask:

Why do we need the system?
Who will use it?
What is the scope?
Is the project feasible?
What are the major risks?


---

Elaboration

Ask:

What are the important requirements?
What architecture should we use?
Can our architecture support 50,000 users?
How will authentication work?
How will data be protected?


---

Construction

Build:

Login
Course Management
Assignment Submission
Assessment
Results
Reports

through multiple iterations.


---

Transition

Deploy:

Install
 ↓
Migrate data
 ↓
Train users
 ↓
Pilot
 ↓
Fix problems
 ↓
Release


---

74. Connecting UP to the UML Work We Already Studied

This is very important for students.

We learned in previous weeks:

Class/Object Models
Dynamic Models
Behavioural Models

These models do not exist in isolation.

Within UP, they become artefacts used during development.

For example:

Requirement
    ↓
Use Case
    ↓
Use-Case Diagram
    ↓
Activity Diagram
    ↓
Sequence Diagram
    ↓
Class/Object Model
    ↓
Design
    ↓
Implementation

Therefore:

> The Unified Process provides the development process, while UML provides many of the modelling languages used within that process.



OMG maintains UML as a formal specification; the current official OMG page identifies UML 2.5.1 as the formal version adopted in December 2017. 


---

PART O — CASE STUDY FOR WEEK 9

75. Case Study: Mzuni Online Student Registration System

Let's use a realistic university example.

Problem

A university currently handles course registration manually.

Students complain about:

long queues;

registration errors;

lost forms;

delays;

inaccurate records.


The university wants an online registration system.


---

76. Inception

Business goal

Create an online system that allows students to register for courses.

Major actors

Student
Registrar
Finance Officer
Payment Gateway

Major use cases

Login
Register Course
Drop Course
Pay Fees
View Registration
Generate Reports

Major risks

System security
Payment integration
Database performance
Data migration
User adoption


---

77. Elaboration

The team investigates:

Authentication architecture
Database architecture
Payment integration
Security
Scalability

They build a prototype.

For example:

Student
   ↓
Web Application
   ↓
Authentication Service
   ↓
Database

They test whether the architecture works.


---

78. Construction

Iteration 1:

Login

Iteration 2:

Course catalogue

Iteration 3:

Registration

Iteration 4:

Payments

Iteration 5:

Reports


---

79. Transition

The university:

Installs system
      ↓
Migrates student records
      ↓
Trains administrators
      ↓
Pilot test
      ↓
Collects feedback
      ↓
Fixes defects
      ↓
Launches system

That is the Unified Process in practice.


---

PART P — WEEK 9 PRACTICAL

80. Practical Exercise

Scenario

Exploits University wants to develop an:

> Online Student Management System



The system must allow:

Students

register;

view courses;

pay fees;

view results.


Lecturers

view classes;

upload materials;

enter marks.


Administrators

manage students;

manage courses;

generate reports.



---

81. Practical Task 1

Create an initial:

Business Case

Answer:

1. What problem exists?


2. Why is the system needed?


3. Who are the stakeholders?


4. What benefits are expected?


5. What are the major risks?




---

82. Practical Task 2

Create an initial:

Use-Case Model

Identify:

actors;

major use cases;

relationships.


This connects directly to Week 8.


---

83. Practical Task 3

Create a simple:

Phase Plan

Inception
   ↓
Elaboration
   ↓
Construction
   ↓
Transition

Then specify at least two iterations for each phase.


---

84. Practical Task 4

Identify at least:

Five possible artefacts

For example:

Vision Document
Use-Case Model
Architecture Document
Source Code
Test Plan

Students must explain why each artefact is useful.


---

85. Practical Task 5

Identify:

Five risks

Then classify them:

Risk	Type	Possible Mitigation

Payment integration fails	Technical	Build prototype early
Users reject system	Organisational	User involvement
Database too slow	Performance	Load testing
Requirements change	Requirements	Iterative development
Data breach	Security	Security controls/testing



---

PART Q — TUTORIAL QUESTIONS

86. Question 1

Define the Unified Process.


---

87. Question 2

Explain the difference between:

a. Iterative development

and

b. Incremental development.

Give a practical example.


---

88. Question 3

Explain the four phases:

Inception
Elaboration
Construction
Transition

For each phase provide:

main objective;

major activities;

typical outputs;

major question answered.



---

89. Question 4

Why is UP described as:

a. Use-case driven?

b. Architecture-centred?

c. Risk-driven?

d. Iterative and incremental?


---

90. Question 5

Explain:

> Why is Elaboration particularly important for managing architectural and technical risks?




---

91. Question 6

Differentiate:

Phase
Iteration
Workflow
Artefact


---

92. Question 7

Explain the difference between:

Generalisation
Inheritance

Use:

Vehicle
Car

as your example.


---

93. Question 8

What is concurrency?

Use the following scenario:

> Two students attempt to register for the final available place in a course at exactly the same time.



Explain the possible problem.


---

PART R — EXAMINATION QUESTIONS

94. Essay Question

> Discuss the Unified Software Development Process and explain how its four phases contribute to successful object-oriented software development.



[25 marks]

Students should discuss:

definition;

iterative nature;

incremental nature;

use-case driven development;

architecture;

risk management;

Inception;

Elaboration;

Construction;

Transition;

milestones;

artefacts.



---

95. Scenario Question

A hospital intends to develop an online patient management system.

The system must:

register patients;

book appointments;

process payments;

store medical records;

generate reports.


The hospital is particularly concerned about:

security;

performance;

integration with existing systems.


Required:

a. Explain how UP could be used to develop the system.
b. Explain what should happen during Inception.
c. Explain why Elaboration is particularly important.
d. Give three architectural risks.
e. Suggest three artefacts.
f. Explain how iterations could be used during Construction.
g. Explain what activities would take place during Transition.


---

PART S — WEEK 9 INDEPENDENT LEARNING — 10 HOURS

Activity 1 — Research

Research:

> Unified Process vs Waterfall vs Agile



Prepare a comparison covering:

development cycle;

requirements;

change;

iterations;

customer feedback;

risk;

delivery;

documentation.



---

Activity 2 — Case Study

Choose one:

Banking System
Hospital System
E-Learning System
Supermarket System
Mobile Money System

Then create a four-phase UP plan.


---

Activity 3 — Artefact Mapping

Create a table:

Phase	Artefact	Purpose

Inception	Vision	Defines overall direction
Inception	Business Case	Justifies project
Elaboration	Architecture Document	Defines architecture
Construction	Source Code	Implements system
Transition	Deployment Package	Releases system


Add at least 10 artefacts in total.


---

PART T — COMMON STUDENT MISUNDERSTANDINGS

96. Misunderstanding 1

"UP is the same as Waterfall."

Incorrect.

UP has four phases, but the phases contain iterations and development activities overlap.


---

97. Misunderstanding 2

"Inception means collecting every requirement."

Not necessarily.

Inception establishes the:

business case;

scope;

major requirements;

major actors/use cases;

major risks.


Requirements are refined throughout subsequent iterations.


---

98. Misunderstanding 3

"Coding only happens in Construction."

Coding can occur earlier, particularly when prototypes are needed to address technical risks.

Elaboration can include implementation of architectural prototypes. 


---

99. Misunderstanding 4

"Testing starts after all coding is finished."

No.

Testing occurs throughout iterative development.

A team may test:

Iteration 1 → Test
Iteration 2 → Test
Iteration 3 → Test

rather than waiting until the entire project is finished.


---

100. Misunderstanding 5

"Generalisation and inheritance are exactly the same."

They are closely related but should be distinguished.

Generalisation
→ modelling/design relationship

Inheritance
→ programming mechanism


---

101. Misunderstanding 6

"Reuse means copy and paste code."

No.

Reuse can involve:

Classes
Libraries
Components
Services
Frameworks
APIs
Architectures
Design patterns

Good reuse requires evaluation of quality, compatibility, security, licence and maintainability.


---

PART U — WEEK 9 REVISION SUMMARY

Concept	Simple Meaning

Unified Process	Organised OO software-development process
UP	Unified Process
RUP	Rational implementation of UP
Iterative	Repeat and improve
Incremental	Add functionality progressively
Use-case driven	Use cases guide development
Architecture-centred	Build and validate important architecture
Risk-driven	Address important risks early
Inception	Establish business case and scope
Elaboration	Refine requirements and establish architecture
Construction	Build the system
Transition	Deploy and move to users
Phase	Major lifecycle period
Iteration	Development cycle within a phase
Workflow	Related development activities
Artefact	Work product/document/output
Reuse	Use existing software assets
Generalisation	General-to-specific modelling relationship
Inheritance	Programming mechanism for acquiring inherited features
Concurrency	Overlapping execution of activities



---

102. The Most Important Diagram for Week 9

Students should remember this:

UNIFIED PROCESS
                               |
        ┌──────────────────────┼──────────────────────┐
        ↓                      ↓                      ↓
   USE-CASE DRIVEN      ARCHITECTURE CENTRED    RISK DRIVEN
        \                      |                      /
         \                     |                     /
          └──────── ITERATIVE & INCREMENTAL ────────┘
                               |
                 ┌─────────────┴─────────────┐
                 ↓                           ↓
             PHASES                      ITERATIONS
                 |
      ┌──────────┼──────────┬──────────┐
      ↓          ↓          ↓          ↓
 Inception  Elaboration Construction Transition
      ↓          ↓          ↓          ↓
   Scope     Architecture   Build     Deploy
   Business  Risk reduction  Test     Train
   Case      Requirements    Refine   Release


---

103. Connecting Week 8 → Week 9

This is particularly important because your students should not feel that Week 9 is a completely new subject.

In Week 8, we asked:

> "What does the system do?"



We produced:

Use Cases
Use-Case Diagrams
Activity Diagrams
Sequence Diagrams
Communication Diagrams

In Week 9, we ask:

> "How do we organise the development of the system represented by those models?"



Therefore:

WEEK 8
Behavioural Analysis
       ↓
"What should the system do?"
       ↓
WEEK 9
Unified Process
       ↓
"How should the development team organise the work?"
       ↓
WEEK 10+
Object-Oriented Design
       ↓
"How should we design the actual software?"

That connection is essential to understanding OOAD as a complete discipline, rather than as a collection of UML diagrams.


---

104. Final Week 9 Takeaway

If students remember only five things, they should remember:

1. UP is iterative and incremental.

The system grows through repeated development cycles.

2. UP is use-case driven.

Use cases help organise requirements, analysis, design, implementation and testing.

3. UP is architecture-centred.

Important architectural decisions and technical risks are addressed early.

4. UP has four major phases.

Inception → Elaboration → Construction → Transition

5. Phases contain iterations.

This is what makes UP fundamentally different from simply treating the four phases as four rigid sequential stages.

IBM's current documentation continues to describe RUP projects in terms of phases and iterations, while the classic RUP guidance defines the four phases and their corresponding objectives/milestones. 


---

References

Primary / Authoritative

Object Management Group (OMG). (2017). OMG Unified Modeling Language (OMG UML), Version 2.5.1. OMG. The official OMG specification page identifies UML 2.5.1 as the formal specification adopted in December 2017. 

[OMG — UML 2.5.1 Official Specification](https://www.omg.org/spec/UML/2.5.1/?utm_source=chatgpt.com)

Unified Process / RUP

IBM. Project Planning — Phases and Iterations. IBM Rational documentation. This provides current documentation on using phases and iterations and identifies the four RUP phases. 

IBM Rational. Rational Unified Process: Best Practices for Software Development Teams. IBM. 

Project Management Institute (PMI). Project Management and the Rational Unified Process for Software Development Projects. PMI. 

Open University. Approaches to Software Development — Introducing the Unified Process. The Open University. 

Course Prescribed/Recommended Texts

Mach, E. (2019). Object Oriented Analysis & Design Cookbook: Introduction to Practical System Modeling.

Reddy, V., & Korra, S. (2018). Object-Oriented Analysis and Design Using UML.

The Art of Service. (2021). Object Oriented Analysis and Design: A Complete Guide.

Wixom, B., & Dennis, A. (2018). Systems Analysis and Design.

Blokdyk, G. (2021). Object-Oriented Analysis and Design Standard Requirements.

Wixom, B., & Dennis, A. (2020). Systems Analysis and Design: An Object-Oriented Approach with UML
