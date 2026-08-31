Absolutely. We are at Week 14 of 16. I’m keeping the sequence we established from your original syllabus, so Week 14 now focuses on the Object-Oriented Design part of the outline—especially the overview of design and combining the Object, Dynamic and Behavioural Models. I’ll also keep the explanations beginner-friendly, with concrete examples rather than simply saying “X versus Y.”

BICT 3202 — OBJECT-ORIENTED ANALYSIS AND DESIGN

WEEK 14: INTEGRATING OBJECT, DYNAMIC AND BEHAVIOURAL MODELS INTO OBJECT-ORIENTED DESIGN

Programme: BSc in Information Communication and Technology
Year: Three
Course Code: BICT 3202
Week: 14 of 16
Module: Object-Oriented Analysis and Design
Lecture Hours: 2
Tutorial Hours: 1
Practical Hours: 1
Independent Learning: 10 hours
Credits: 10


---

1. POSITION OF WEEK 14 IN THE 16-WEEK COURSE

By now, students have travelled quite a long way.

They started with:

> What problem does the organisation have?



Then:

> What does the system need to do?



Then:

> What objects exist?



Then:

> How do those objects relate?



Then:

> How do the objects behave over time?



Then:

> How do users and objects interact?



Then:

> How should the software be organised into layers and reusable components?



Now we reach a critical question:

> How do we combine all these models into one coherent software design?



That is the purpose of Week 14.

The official UML specification treats structural modelling, behavioural modelling, use cases, deployments and related modelling concepts as parts of the same overall modelling language. 

So students should not think of UML diagrams as independent drawings.

Instead:

> Each diagram provides a different view of the same system.




---

2. WEEK 14 LEARNING OUTCOMES

By the end of this week, students should be able to:

1. Define object-oriented design.


2. Explain the difference between analysis and design.


3. Explain why analysis models must be transformed into design models.


4. Explain design classes.


5. Identify responsibilities of design classes.


6. Assign operations to appropriate classes.


7. Explain the relationship between attributes and operations.


8. Integrate the object model with the dynamic model.


9. Integrate the object model with behavioural models.


10. Trace a requirement from a use case to classes and operations.


11. Use sequence diagrams to refine class responsibilities.


12. Use state diagrams to identify state-dependent behaviour.


13. Use activity diagrams to clarify business workflows.


14. Identify design inconsistencies between UML models.


15. Refine an analysis model into a design model.


16. Produce an integrated OOAD design for a small system.




---

PART A — WHAT IS OBJECT-ORIENTED DESIGN?

3. Simple Definition

Object-oriented design (OOD) is the process of transforming the understanding of a system developed during analysis into a detailed design that can guide implementation.

In simple language:

> Analysis tells us what the system needs and what exists.



> Design decides how the software will actually be organised to provide it.




---

4. A Simple Real-Life Example

Imagine someone tells an architect:

> "I need a house with three bedrooms, a kitchen, two bathrooms and a garage."



That is similar to requirements and analysis.

The architect then decides:

where the rooms will be;

where doors will go;

where electricity will run;

where pipes will go;

what materials are required.


That is similar to design.

The same idea applies to software.


---

5. Analysis vs Design

Students must understand this properly.

Analysis asks:

> What does the system need?



Example:

> A student must be able to register for a course.



Analysis may identify:

Student
Course
Registration

Design asks:

> How will the software implement that requirement?



Design may introduce:

RegistrationController
RegistrationService
RegistrationRepository
RegistrationValidator

The design therefore becomes more implementation-oriented.


---

6. Analysis Model → Design Model

The transformation can be represented as:

Requirements
     ↓
Use Cases
     ↓
Analysis Model
     ↓
Design Decisions
     ↓
Design Model
     ↓
Implementation

The important point is:

> We should not randomly invent design classes.



They should be justified by the requirements and analysis.


---

PART B — THE THREE MAJOR MODELS

7. Object Model

The object model describes the structural/static view of the system.

It answers:

> What things exist in the system and how are they related?



Typical elements include:

classes;

objects;

attributes;

operations;

associations;

generalisation;

aggregation/composition.


Example:

Student
----------------
studentId
name
email
----------------
register()
dropCourse()

and:

Course
----------------
courseCode
courseName
credits
----------------
checkCapacity()


---

8. Dynamic Model

The dynamic model focuses on how objects behave and change over time.

It asks:

> What happens to the objects as events occur?



For example:

Course

Available
   ↓
Full
   ↓
Closed

An event might be:

> Student registers.



Another event:

> Course reaches maximum capacity.




---

9. Behavioural Model

The behavioural model focuses on what the system does from the perspective of users and interactions.

Examples include:

use cases;

use case diagrams;

sequence diagrams;

collaboration/communication diagrams;

activity diagrams.


For example:

Student
   |
   | Register for Course
   ↓
Registration System


---

10. Why Do We Need All Three?

Suppose we only create a class diagram:

Student
Course
Registration

We know the structure.

But we don't necessarily know:

> What happens when the student registers?



Now add a sequence diagram:

Student
  ↓
RegistrationUI
  ↓
RegistrationService
  ↓
Course
  ↓
RegistrationRepository

Now we understand the interaction.

Now add a state model:

Course
Available → Full → Closed

Now we understand state-dependent behaviour.

Therefore:

> Different UML models answer different questions.




---

PART C — THE CENTRAL IDEA OF WEEK 14

11. One System, Multiple Views

This is perhaps the most important concept in this lesson.

Imagine we are modelling a University Course Registration System.

Use case diagram

Tells us:

> Who uses the system and what they want to accomplish.



Class diagram

Tells us:

> What structural elements exist.



Sequence diagram

Tells us:

> How objects interact during a particular scenario.



Activity diagram

Tells us:

> How a workflow progresses.



State machine diagram

Tells us:

> How an object changes state.



Component diagram

Tells us:

> How software functionality is modularised.



These are not six unrelated systems.

They are:

> six different views of one system.




---

PART D — FROM USE CASE TO DESIGN

12. Start With a Use Case

Consider:

Use Case: Register for Course

Actor:

Student

Goal:

> Register for a course.




---

13. Basic Use Case Flow

1. Student logs in.
2. Student selects a course.
3. System checks whether the course exists.
4. System checks prerequisites.
5. System checks course capacity.
6. System creates registration.
7. System confirms registration.

Now the designer asks:

> Which objects should perform these responsibilities?




---

14. Identifying Candidate Classes

From the scenario we can identify:

Student
Course
Registration

But we may also need design classes:

RegistrationController
RegistrationService
CourseRepository
RegistrationRepository

This is where analysis becomes design.


---

PART E — RESPONSIBILITY ASSIGNMENT

15. What Is a Responsibility?

A responsibility is something a class is responsible for knowing or doing.

For example:

Student

May know:

studentId
name
programme

Course

May know:

courseCode
courseName
capacity

Registration

May know:

registrationDate
status


---

16. Responsibilities Include "Knowing" and "Doing"

A class may have a responsibility to:

Know something

Example:

Course knows its capacity.

Do something

Example:

Course checks whether space is available.


---

17. Bad Responsibility Assignment

Imagine:

Student
----------------------
registerAnyCourse()
calculateCourseCapacity()
sendEmail()
generatePaymentReceipt()
connectToDatabase()

This Student class is doing far too much.

It has poor cohesion.

We discussed cohesion in Week 13.


---

18. Better Responsibility Assignment

Instead:

Student
   ↓
RegistrationService
   ↓
Course
   ↓
RegistrationRepository

Each class has a more focused purpose.


---

PART F — DESIGN CLASSES

19. What Is a Design Class?

A design class is a class defined with sufficient detail to support implementation.

Compared with an early analysis class, a design class may include:

precise attributes;

data types;

operations;

parameter types;

return types;

visibility;

relationships;

interfaces;

dependencies.



---

20. Analysis Class

We might initially have:

Student
----------------
name
email
register()

At design stage, we can refine it:

Student
--------------------------------
- studentId : String
- name : String
- email : String
- programme : Programme
--------------------------------
+ register(course : Course) : Registration
+ drop(course : Course) : void

The design is now much more precise.


---

PART G — VISIBILITY

21. Visibility in Design Classes

Students should understand:

+
-
#
~

Common UML meanings:

Symbol	Meaning

+	Public
-	Private
#	Protected
~	Package visibility


Example:

Student
-------------------------
- studentId : String
- name : String
-------------------------
+ getName() : String
+ register() : void

The UML specification provides the formal modelling foundation for these kinds of structural elements. 


---

PART H — ATTRIBUTES AND OPERATIONS

22. Attributes

Attributes represent information held by an object.

Example:

Student
-----------------
studentId
name
email
dateOfBirth


---

23. Operations

Operations represent behaviour.

Example:

Student
-----------------
register()
dropCourse()
viewCourses()

A useful rule:

> Attributes describe what an object knows.



> Operations describe what an object can do.




---

24. Example

Consider:

BankAccount
-------------------------
- accountNumber : String
- balance : Decimal
-------------------------
+ deposit(amount) : void
+ withdraw(amount) : boolean
+ getBalance() : Decimal

The attributes store information.

The operations perform actions.


---

PART I — SEQUENCE DIAGRAM → CLASS DESIGN

25. This Is Extremely Important

A sequence diagram is not only something we draw for presentation.

It can help us discover:

> Which objects need which operations?



Suppose our sequence is:

Student
   |
   | register(course)
   ↓
RegistrationService
   |
   | checkCapacity()
   ↓
Course
   |
   | createRegistration()
   ↓
Registration

Now we can infer operations.


---

26. From Messages to Operations

If the sequence diagram contains:

Course → checkCapacity()

then the Course class should probably have:

checkCapacity()

If:

RegistrationService → registerStudent()

then:

RegistrationService
----------------------
registerStudent()

may be required.

Therefore:

> Messages in interaction diagrams can help refine operations in the class model.




---

PART J — MAINTAINING CONSISTENCY

27. What Does "Model Consistency" Mean?

It means the different diagrams should agree with one another.

For example, suppose the class diagram says:

Course
----------------
checkCapacity()

but the sequence diagram says:

Course → verifyCapacity()

We have an inconsistency.

Which operation is correct?

The development team must resolve the discrepancy.


---

28. Another Example

Class diagram:

Student
----------------
register()

Sequence diagram:

Student → enrol()

Again:

> Are these supposed to be the same operation?



If yes, standardise the terminology.

This is why models should be cross-checked.


---

PART K — OBJECT MODEL + DYNAMIC MODEL

29. Combining Structure and Behaviour

Suppose:

Course
-----------------
capacity
status
-----------------
registerStudent()

The class diagram shows the structure.

The state machine shows:

Available
     ↓
Full
     ↓
Closed

Now we connect them.

For example:

registerStudent()

may cause:

Available → Full

when the final available seat is taken.

That is integration between the object and dynamic models.


---

30. Example

Suppose:

Course capacity = 50
Current registrations = 49

A student registers.

After successful registration:

49 → 50

The course state changes:

Available → Full

Therefore:

> The operation registerStudent() has a relationship with the state of the Course object.




---

PART L — OBJECT MODEL + ACTIVITY MODEL

31. Activity Diagram

Suppose the registration workflow is:

Start
  ↓
Select Course
  ↓
Check Prerequisite
  ↓
Check Capacity
  ↓
[Available?]
 /       \
No        Yes
|          |
Reject    Create Registration
             ↓
       Send Confirmation
             ↓
            End

Now ask:

> Which objects perform these activities?




---

32. Responsibility Mapping

Activity	Possible Responsible Class

Select course	RegistrationController
Check prerequisite	Course / RegistrationService
Check capacity	Course
Create registration	RegistrationService
Save registration	RegistrationRepository
Send confirmation	NotificationService


This transforms a behavioural model into design responsibilities.


---

PART M — OBJECT MODEL + USE CASE MODEL

33. Use Case

Student → Register Course

The use case tells us:

> What the user wants.



The class model tells us:

> What objects are available.



The sequence diagram tells us:

> How those objects cooperate to fulfil the use case.



Therefore:

Use Case
   ↓
Scenario
   ↓
Sequence Diagram
   ↓
Responsibilities
   ↓
Class Operations
   ↓
Design Classes

This is one of the most useful workflows in OOAD.


---

PART N — TRACEABILITY

34. What Is Traceability?

Traceability means being able to follow a requirement through the development process.

For example:

Requirement
     ↓
Use Case
     ↓
Scenario
     ↓
Sequence Diagram
     ↓
Class
     ↓
Operation
     ↓
Code


---

35. Example Traceability

Requirement:

> "Students must be able to register for courses."



↓

Use case:

Register for Course

↓

Sequence:

Student
 ↓
RegistrationService
 ↓
Course
 ↓
RegistrationRepository

↓

Classes:

Student
RegistrationService
Course
Registration
RegistrationRepository

↓

Operations:

registerCourse()
checkCapacity()
checkPrerequisite()
saveRegistration()

Now we can trace the requirement all the way to implementation.


---

PART O — DESIGNING THE CONTROLLER

36. What Is a Controller?

In many OO designs, a controller coordinates a system operation initiated by an external actor.

For example:

RegistrationController

may receive:

registerCourse(studentId, courseId)

and coordinate the process.


---

37. Controller Does Not Mean "Do Everything"

This is another common student mistake.

Bad:

RegistrationController
 ├── check database
 ├── calculate fees
 ├── validate course
 ├── apply business rules
 ├── create HTML
 └── send SMS

The controller has become a "God class."

Instead:

RegistrationController
          ↓
RegistrationService
     ↙         ↘
 Course       Repository

The controller coordinates rather than owning every responsibility.


---

PART P — DESIGNING THE SERVICE

38. What Is a Service?

A service provides a particular application capability.

Example:

RegistrationService

could provide:

registerStudent()
dropStudent()
getRegistration()


---

39. Example Implementation Thinking

Conceptually:

registerStudent(student, course)

    ↓

check prerequisite

    ↓

check course capacity

    ↓

create Registration

    ↓

save Registration

    ↓

send confirmation

The service coordinates these steps.


---

PART Q — DOMAIN OBJECTS SHOULD CONTAIN DOMAIN KNOWLEDGE

40. Example

Suppose:

Course

has:

capacity = 50
registered = 50

A question arises:

> Where should we determine whether another student can register?



One reasonable design is to place course-specific knowledge with the Course domain object:

Course
-----------------------
isAvailable()
hasCapacity()

rather than scattering the same rule throughout the UI.

This is an example of assigning responsibilities to the object that has the information needed to perform them.


---

PART R — DESIGN REFINEMENT

41. From Simple to Detailed

Analysis:

Student
Course
Registration

Design:

Student
RegistrationController
RegistrationService
Course
Registration
CourseRepository
RegistrationRepository
NotificationService

The design model is therefore often richer than the initial analysis model.


---

42. Why Add New Classes?

Because implementation may require technical responsibilities that were not obvious during early analysis.

For example:

> "Save registration."



Analysis might only identify:

Registration

Design may introduce:

RegistrationRepository

to handle persistence.

This does not mean the original analysis was wrong.

It means:

> Design is a refinement of the understanding developed during analysis.




---

PART S — DESIGNING FOR CHANGE

43. Ask This Question

A good designer should ask:

> "What is likely to change?"



For example:

Likely to change:

database;

payment provider;

notification channel;

user interface;

external API.


Less likely to change:

core business concept of Student;

concept of Course;

registration rules.


We can design boundaries around things likely to change.


---

44. Example — Payment

Bad:

RegistrationService
        ↓
AirtelMoneyAPI

Now registration is tightly connected to one provider.

Better:

RegistrationService
        ↓
PaymentGateway
        ↑
   ┌────┴────┐
   ↓         ↓
Provider A  Provider B

Now the specific implementation can potentially change.


---

PART T — INTRODUCTION TO DESIGN PATTERNS

Although design patterns are not explicitly listed as a separate heading in the supplied syllabus, they naturally support the design stage and can be introduced here as design techniques, not as a separate examinable block unless the university later expands the syllabus.

45. What Is a Design Pattern?

A design pattern is a reusable solution structure for a recurring design problem.

It is not simply a piece of code that students copy.

Think of it as:

> A proven way of organising a solution to a common design problem.




---

46. Example — Strategy Pattern

Suppose a university accepts:

Mobile Money
Bank
Card

Instead of:

if payment == mobile money
    ...
else if payment == bank
    ...
else if payment == card
    ...

everywhere, we can define a common abstraction:

PaymentStrategy
      |
      ├── MobileMoneyPayment
      ├── BankPayment
      └── CardPayment

The registration system can work with the abstraction.

This supports adaptability.


---

47. Important Warning About Patterns

Students should not think:

> "Professional programmers must use design patterns everywhere."



No.

Patterns should be used when they solve an actual recurring design problem.

Otherwise:

> The pattern itself can become unnecessary complexity.




---

PART U — INTEGRATED CASE STUDY

48. University Course Registration System

Let's now bring everything together.

Requirement

> Students must be able to register for available courses.




---

49. Use Case Model

┌───────────────────────┐
             │ University System      │
             │                       │
Student ────→│ Register for Course   │
             │                       │
             └───────────────────────┘


---

50. Analysis Class Model

Student
    |
    | registers
    ↓
Registration
    |
    | for
    ↓
Course


---

51. Sequence Model

Student
   |
   | register(course)
   ↓
RegistrationController
   |
   ↓
RegistrationService
   |
   | checkCapacity()
   ↓
Course
   |
   | create
   ↓
Registration
   |
   | save
   ↓
RegistrationRepository


---

52. Dynamic Model

Course:

Available
    |
    | final seat taken
    ↓
Full
    |
    | registration period ends
    ↓
Closed


---

53. Activity Model

Start
 ↓
Select Course
 ↓
Check Prerequisite
 ↓
Check Capacity
 ↓
Available?
 ├── No → Display Error
 |
 └── Yes
       ↓
 Create Registration
       ↓
 Save Registration
       ↓
 Send Confirmation
       ↓
      End


---

54. Design Model

Now we combine everything:

┌─────────────────────────┐
│ RegistrationController  │
│ + registerCourse()      │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ RegistrationService     │
│ + registerStudent()     │
│ + dropCourse()          │
└───────┬──────────┬──────┘
        ↓          ↓
┌────────────┐ ┌──────────────────┐
│ Course     │ │ Registration     │
│            │ │                  │
│ capacity   │ │ date             │
│ status     │ │ status           │
│            │ │                  │
│ isAvailable│ │ confirm()        │
└────────────┘ └────────┬─────────┘
                        ↓
              ┌────────────────────┐
              │ RegistrationRepo   │
              │ + save()           │
              │ + find()           │
              └────────────────────┘

This is what it means to integrate the models.


---

PART V — MODEL VALIDATION

55. How Do We Know Our Models Are Correct?

We can ask several questions.

Question 1

Does every important use case have supporting classes?

Question 2

Does every important sequence message correspond to an operation?

Question 3

Do operations belong to sensible classes?

Question 4

Do state changes correspond to actual events or operations?

Question 5

Do activity flows agree with use-case descriptions?

Question 6

Do class relationships support the required interactions?

Question 7

Are there duplicated responsibilities?

Question 8

Are any classes doing too much?


---

56. Example of Inconsistency

Suppose the use case says:

> Students can drop courses.



But the class diagram contains:

Student
Course
Registration

and none has an operation related to dropping.

Then we should ask:

> How will the requirement actually be implemented?



Perhaps:

RegistrationService
+ dropCourse()

needs to be introduced.


---

PART W — DESIGN QUALITY CHECKLIST

Before approving a design, ask:

Structure

Are classes clearly identified?

Are relationships meaningful?

Are responsibilities appropriate?


Behaviour

Do sequence diagrams make sense?

Do state transitions make sense?

Are important events represented?


Requirements

Can every major requirement be traced to the design?


Architecture

Are layers clearly separated?

Are dependencies controlled?


Reuse

Are appropriate components reusable?


Adaptability

Can likely changes be accommodated?


Maintainability

Is the system understandable?



---

PART X — COMMON STUDENT MISTAKES

Mistake 1: Treating UML diagrams as independent drawings

Incorrect thinking:

> "I finished my class diagram, now I'll draw a random sequence diagram."



Correct thinking:

> "My sequence diagram should explain how the classes from my class model cooperate."




---

Mistake 2: Putting every operation into one class

Example:

System
---------
login()
register()
pay()
sendEmail()
generateReport()
createStudent()
deleteCourse()

This is usually a sign of poor responsibility assignment.


---

Mistake 3: Confusing analysis and design

Analysis:

> Student needs to register.



Design:

> RegistrationController receives the request and RegistrationService coordinates registration.




---

Mistake 4: Adding classes without justification

Students sometimes create:

Manager
Helper
Processor
System
Utility

without explaining their responsibilities.

Every design class should have a reason for existing.


---

Mistake 5: Ignoring consistency

If the class diagram says:

register()

and the sequence diagram says:

enrolStudent()

students should explain whether these are different operations or simply inconsistent naming.


---

PART Y — TUTORIAL — 1 HOUR

Tutorial Exercise 1: Analyse and Design

Given:

> A student selects a course. The system checks whether the student has completed prerequisites. It then checks whether space is available. If everything is valid, a registration record is created and the student receives confirmation.



Students must identify:

A. Actors

B. Use case

C. Analysis classes

D. Design classes

E. Operations

F. Sequence of interactions

G. Course states


---

Tutorial Exercise 2 — Model Integration

Give students these three pieces:

Class model

Student
Course
Registration

Sequence message

RegistrationService → verifyPrerequisite()

State model

Course:
Available → Full

Ask:

> What changes should be made to the class model to make these models consistent?



Expected discussion:

RegistrationService
+ verifyPrerequisite()

Course
+ isAvailable()

and the relationships should support these interactions.


---

Tutorial Exercise 3 — Find the Responsibility Problem

Give students:

Student
-------------------------
registerCourse()
sendEmail()
saveToDatabase()
calculateFees()
checkCourseCapacity()
generateReport()

Ask:

> Redesign this class.



Possible answer:

Student
RegistrationService
NotificationService
RegistrationRepository
Course
FinanceService
ReportService

Students must justify their decisions.


---

PART Z — PRACTICAL — 1 HOUR

57. Practical Assignment

Continue using the University Course Registration System from Weeks 12 and 13.

Students must produce an integrated design package.

Task 1 — Refine the class diagram

For every major class, specify:

attributes;

data types;

operations;

visibility;

relationships.



---

Task 2 — Select one major use case

Use:

> Register for Course




---

Task 3 — Produce a sequence diagram

Show at least:

Student
RegistrationController
RegistrationService
Course
Registration
RegistrationRepository


---

Task 4 — Produce a state model

Model the lifecycle of:

> Course



For example:

Created
  ↓
Available
  ↓
Full
  ↓
Closed

Students should identify the events causing each transition.


---

Task 5 — Produce an activity diagram

Model:

> Course Registration Process




---

Task 6 — Cross-check the models

Students must identify at least three consistency relationships, such as:

Sequence message → Class operation
State transition → Event/operation
Activity → Responsibility
Use case → Design classes


---

PART AA — INDEPENDENT LEARNING — 10 HOURS

Assignment: Integrated OOAD Design

Students choose one system:

1. Banking system


2. Hospital system


3. E-commerce system


4. Library system


5. University system


6. Mobile money system



They must submit:

1. Requirements summary

At least five functional requirements.

2. Use case diagram

At least four use cases.

3. Class diagram

At least eight classes.

4. Sequence diagram

For one major use case.

5. Activity diagram

For the same use case.

6. State machine diagram

For one important object.

7. Design refinement

Identify:

analysis classes;

design classes;

controllers;

services;

repositories where appropriate.


8. Model integration explanation

Students must explicitly explain:

> How does the class diagram support the sequence diagram?



> How does the state model relate to the operations?



> How does the activity diagram relate to responsibilities?



> How does the use case lead to the design?



This final section is extremely important.


---

PART AB — EXAMINATION QUESTIONS

Question 1 — 20 Marks

> Define object-oriented design and explain how it differs from object-oriented analysis. Use a University Course Registration System to illustrate your answer.




---

Question 2 — 25 Marks

> Explain how a sequence diagram can be used to identify and refine operations in a class diagram. Use a practical example.




---

Question 3 — 25 Marks

> Explain how the object, dynamic and behavioural models complement one another during object-oriented design.




---

Question 4 — 30 Marks

> A university wants to develop an online course registration system. A student selects a course, the system verifies prerequisites and capacity, creates a registration record and sends confirmation.

Design an OO solution by identifying:

a. The relevant classes
b. Their responsibilities
c. Major operations
d. Object interactions
e. Relevant course states
f. How the different UML models should remain consistent.




---

PART AC — QUICK REVISION TABLE

Concept	Simple meaning	Example

Analysis	Understand the problem	Student needs registration
Design	Decide how software will implement it	RegistrationService
Object model	What exists	Student, Course
Dynamic model	How things change	Available → Full
Behavioural model	What the system does/interactions	Register Course
Responsibility	What a class knows/does	Course checks capacity
Attribute	Information held	courseCode
Operation	Action performed	register()
Controller	Coordinates a request	RegistrationController
Service	Provides application capability	RegistrationService
Repository	Handles persistence	CourseRepository
Traceability	Follow requirement through design	Requirement → Code
Model consistency	Diagrams agree	sequence message matches operation



---

PART AD — THE MOST IMPORTANT CONCEPT TO TAKE HOME

Students should remember this chain:

REQUIREMENT
                     ↓
              "Student registers"
                     ↓
                 USE CASE
                     ↓
          "Register for Course"
                     ↓
              SCENARIO
                     ↓
        "What happens step-by-step?"
                     ↓
           SEQUENCE DIAGRAM
                     ↓
        "Which objects interact?"
                     ↓
              CLASS MODEL
                     ↓
        "What does each object do?"
                     ↓
            RESPONSIBILITIES
                     ↓
            DESIGN CLASSES
                     ↓
         COMPONENT / ARCHITECTURE
                     ↓
              IMPLEMENTATION

And alongside that:

CLASS MODEL
    ↕
DYNAMIC MODEL
    ↕
BEHAVIOURAL MODEL

The models must support one another, not contradict one another.

That is the central lesson of Week 14.


---

PART AE — CONNECTION TO WEEK 13

Last week we taught students:

> How should we organise software into layers and reusable components?



This week we go one level deeper:

> What exactly should those components contain, what responsibilities should classes have, and how do our structural and behavioural models work together?



So:

WEEK 13
Architecture
   ↓
Layers
   ↓
Components
   ↓
Reuse
   ↓
Adaptability

             ↓

WEEK 14
Design
   ↓
Design Classes
   ↓
Responsibilities
   ↓
Operations
   ↓
Object Model
   ↕
Dynamic Model
   ↕
Behavioural Model
   ↓
Integrated Design

This creates a smooth progression rather than teaching Week 14 as an unrelated topic.


---

REFERENCES AND FURTHER READING

Primary standards

1. Object Management Group (OMG). Unified Modeling Language Specification, Version 2.5.1. UML 2.5.1 remains the formal UML specification listed by OMG. 


2. Object Management Group (OMG). Unified Modeling Language, Version 2.5.1. The specification organises UML concepts into structural, behavioural, use-case, deployment and related modelling areas. 


3. Object Management Group (OMG). Introduction to OMG Specifications. Provides an overview of UML diagram categories, including class, component, deployment, use-case, sequence, statechart, activity and package diagrams. 



Prescribed texts from the course outline

4. Mach, E. (2019). Object Oriented Analysis & Design Cookbook: Introduction to Practical System Modeling.


5. Reddy, V. & Korra, S. (2018). Object-Oriented Analysis and Design Using UML.


6. The Art of Service (2021). Object Oriented Analysis and Design: A Complete Guide.



Recommended texts

7. Wixom, B. & Dennis, A. (2018). Systems Analysis and Design.


8. Blokdyk, G. (2021). Object-Oriented Analysis and Design Standard Requirements.


9. Wixom, B. & Dennis, A. (2020). Systems Analysis and Design: An Object-Oriented Approach with UML.




---

WEEK 14 IN ONE SENTENCE

> Object-oriented design takes the requirements and analysis models we have developed in previous weeks and systematically refines them into a coherent set of classes, responsibilities, interactions, behaviours, components and architectural decisions that can guide actual software implementation.
