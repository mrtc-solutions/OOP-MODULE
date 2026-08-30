BICT 3202 — Object-Oriented Analysis and Design

WEEK 3: MODELLING LANGUAGE — UML

Programme: BSc Information Communication and Technology
Year: 3
Course Code: BICT 3202
Week: 3 of 16
Lecture: 2 hours
Tutorial: 1 hour
Practical: 1 hour
Independent Learning: 10 hours


---

1. Week 3 Overview

In Week 1, we learned how to move from a business problem to business needs and software requirements.

In Week 2, we learned how to think about the problem in terms of:

objects;

classes;

attributes;

behaviour;

relationships;

abstraction;

encapsulation;

modularity; and

complexity management.


Now we have a problem:

> How do we communicate all these models in a standard way so that analysts, developers, clients and other stakeholders can understand them?



This is where UML — Unified Modeling Language comes in.

The official course outline places the following topics in this section:

1. An Overview of UML


2. The Building Blocks of UML


3. Rules of UML


4. Mechanisms of UML


5. UML Architecture



These are not merely topics to memorize. They form the conceptual foundation students need before they start drawing formal UML diagrams.

The Object Management Group (OMG) describes UML as a standard language for visualizing, specifying and documenting software and systems, including their structures, behaviours and processes. 

The current formal UML specification listed by OMG is UML 2.5.1, adopted in December 2017. 


---

2. Learning Outcomes for Week 3

By the end of this week, students should be able to:

1. Define UML.


2. Explain why UML is used in OOAD.


3. Explain the difference between a modelling language and a software development methodology.


4. Explain what UML can and cannot do.


5. Identify the major building blocks of UML.


6. Explain things, relationships and diagrams as conceptual building blocks.


7. Explain structural, behavioural, grouping and annotational elements.


8. Identify major UML diagram categories.


9. Explain the purpose of different UML diagrams.


10. Explain UML rules and well-formedness.


11. Explain UML common mechanisms.


12. Explain specifications, adornments, common divisions and extensibility.


13. Explain UML stereotypes, tagged values and constraints.


14. Explain the four-layer UML architecture.


15. Distinguish between M0, M1, M2 and M3.


16. Apply UML concepts to a simple university registration system.


17. Explain why UML is important for communication among software development stakeholders.




---

3. What Is UML?

3.1 Full Meaning

UML stands for:

> Unified Modeling Language



Break the name into three parts.

Unified

It brought together ideas from several earlier object-oriented modelling approaches.

Modeling

It is used to create representations of systems.

Language

It provides defined concepts and notation for communicating those representations.

Therefore:

> UML is a standardized modelling language used to represent, communicate and document systems.



OMG currently describes UML as a standard for visualizing, specifying and documenting software and systems. 


---

4. What Problem Does UML Solve?

Imagine five people are developing a university system:

a business analyst;

a software architect;

a programmer;

a database designer;

a university administrator.


The analyst says:

> "The Student is associated with a Course."



The programmer asks:

> "What exactly does associated mean?"



The administrator says:

> "I thought a student could register for many courses."



The database designer asks:

> "Is this one-to-many or many-to-many?"



Everyone may have a different mental picture.

A UML diagram can make the intended structure visible.

For example:

┌─────────────┐          ┌─────────────┐
│   Student   │          │   Course    │
├─────────────┤          ├─────────────┤
│ studentID   │          │ courseCode  │
│ name        │          │ courseName  │
└─────────────┘          └─────────────┘
       │                        │
       └────── registers ──────┘

Now the team has something concrete to discuss.


---

5. UML Is a Language, Not a Programming Language

Students sometimes hear "language" and assume UML is like:

Java;

Python;

C++;

JavaScript.


It is not.

A programming language tells a computer how to execute instructions.

UML tells humans and modelling tools how to represent and communicate the structure and behaviour of a system.

Programming language

Java
Python
C#
C++

Used primarily to implement software.

Modelling language

UML

Used to model and communicate software/system concepts.


---

6. UML Is Also Not a Development Methodology

This distinction is extremely important.

A modelling language tells you:

> How do I represent the system?



A development methodology/process tells you:

> What activities should we perform, in what order, and how should the system be developed?



UML itself does not prescribe one complete software development process. OMG presents UML as a language, while development processes such as the Unified Process can use UML. 


---

Example

UML

Provides notation such as:

Class
Actor
Use Case
Association
State
Activity
Sequence
Component
Node

Development process

Could tell a team:

Gather requirements
      ↓
Analyse
      ↓
Design
      ↓
Implement
      ↓
Test
      ↓
Deploy

Therefore:

> UML = modelling language



> UP/USDP = development process



We will study the Unified Software Development Process in Weeks 12–13.


---

7. Why Is UML Important in OOAD?

UML provides a common visual language.

Imagine someone draws this:

Student → Course

Even without seeing the code, we can discuss the intended relationship.

UML can help:

1. Understand requirements

Use cases can represent what users expect from a system.

2. Model structure

Class diagrams can show classes and relationships.

3. Model behaviour

State and activity diagrams can represent changes and workflows.

4. Model interactions

Sequence and communication diagrams can show how objects communicate.

5. Communicate designs

Developers, analysts and stakeholders can discuss the same model.

6. Document systems

Models can become part of technical documentation.

7. Support maintenance

Future developers can use models to understand an existing system.

OMG explicitly identifies UML as a language for visualizing, specifying and documenting software and systems. 


---

8. UML Is Not Only for Software

This is another interesting point.

Although UML is heavily associated with software engineering, it can also be used for modelling:

business processes;

organizational structures;

workflows;

non-software systems.


OMG notes that UML can be used for business modelling and other non-software systems as well. 

For example, a hospital workflow can be modelled even before deciding exactly what software will implement it.


---

9. A Very Important Principle: One Diagram Cannot Explain Everything

Suppose we have a university registration system.

Can one diagram show:

all classes;

all users;

all workflows;

every interaction;

every database;

every server;

every state;

every requirement?


It would become extremely complicated.

Instead, UML gives us different diagram types for different perspectives.

This is called using multiple views/models.

The formal UML specification itself separates concepts for structural modelling, behavioural modelling and interactions. 


---

10. The Three Major Conceptual Building Blocks

A classic conceptual way of learning UML is to think in terms of:

1. Things


2. Relationships


3. Diagrams



This three-part conceptual model is associated with the foundational UML teaching approach of Booch, Rumbaugh and Jacobson. 

Think of it like this:

UML
              |
      ┌───────┼────────┐
      ↓       ↓        ↓
   Things  Relationships  Diagrams

Let's examine each.


---

11. Building Block 1: Things

A thing is an important modelling element or abstraction in a UML model.

For teaching purposes, things can be grouped into:

1. Structural things


2. Behavioural things


3. Grouping things


4. Annotational things



This classification is part of the traditional conceptual introduction to UML. 


---

12. Structural Things

Structural things represent the relatively static parts of a model.

Think:

> What exists?



Examples include:

Class

Interface

Object

Component

Node



---

13. Class

A class represents a set/type of objects sharing common characteristics and behaviour.

Example:

┌────────────────────────┐
│        Student         │
├────────────────────────┤
│ studentID              │
│ name                   │
│ programme              │
│ year                   │
├────────────────────────┤
│ registerCourse()       │
│ viewResults()          │
└────────────────────────┘

The top section is the class name.

The middle section contains attributes.

The bottom section contains operations.

We will study class diagram notation extensively in Week 5.


---

14. Interface

An interface specifies a set of operations that a class/component can provide.

Imagine a payment system.

We might define:

«interface»
PaymentService
------------------------
processPayment()
refundPayment()
checkStatus()

Different payment providers could implement the interface differently.

For example:

PaymentService
       |
       ├── BankPayment
       ├── MobileMoneyPayment
       └── CardPayment

The user of the interface does not necessarily need to know the internal implementation.


---

15. Object

An object represents a particular instance.

Suppose the class is:

Student

A particular object might be:

student001 : Student

with:

studentID = "ST001"
name = "Francis"
programme = "BSc ICT"

Remember from Week 2:

> Class = general definition



> Object = specific instance




---

16. Component

A component represents a modular, replaceable part of a system.

For example:

University System
      |
      ├── Authentication Component
      ├── Registration Component
      ├── Finance Component
      └── Reporting Component

Components become particularly useful when discussing software architecture.


---

17. Node

A node represents a computational or physical resource on which software may execute.

For example:

[Mobile Device]
      |
      ↓
[Application Server]
      |
      ↓
[Database Server]

A node could represent a:

server;

device;

execution environment;

hardware resource.


Deployment diagrams use nodes.


---

18. Behavioural Things

Structural things answer:

> What exists?



Behavioural things answer:

> What happens?



Examples include:

interactions;

activities;

state machines.


The formal UML specification contains dedicated concepts for state machines, activities and interactions. 


---

19. Interaction

An interaction represents communication between elements.

Imagine a student logging into a university system.

Student → Login Page → Authentication Service → Database

The interaction describes how the participants communicate.

A sequence diagram is commonly used to show such interactions.


---

20. Activity

An activity represents a workflow or sequence of actions.

For example:

Start
  ↓
Login
  ↓
Select Course
  ↓
Check Prerequisite
  ↓
[Eligible?]
  ↓ Yes
Register Course
  ↓
Display Confirmation
  ↓
End

This is particularly useful for modelling business processes and workflows.

We will study activity diagrams in detail in Week 11.


---

21. State Machine

A state machine describes how an object changes from one state to another as events occur.

Consider an application:

Submitted
    ↓
Under Review
    ↓
Approved
    ↓
Completed

An event causes the transition.

For example:

Application submitted
        ↓
Submitted

and:

Reviewer approves
        ↓
Approved

We will study dynamic/state modelling in Weeks 7 and 8.


---

22. Grouping Things

Grouping elements organize other model elements.

The most important example is:

Package

A package groups related modelling elements.

For example:

University System
│
├── Student Management Package
│     ├── Student
│     ├── Programme
│     └── Registration
│
├── Finance Package
│     ├── Payment
│     └── Invoice
│
└── Examination Package
      ├── Exam
      └── Result

Packages help manage large models.

This directly connects to our Week 2 discussion of complexity management.


---

23. Annotational Things

An annotational element provides additional information about a model.

The simplest example is a:

Note

For example:

┌─────────────────────┐
│ Student             │
└─────────────────────┘
          |
          |--------------------\
                               \
                    ┌──────────────────────┐
                    │ Note:                 │
                    │ Student must satisfy  │
                    │ prerequisites before  │
                    │ registration.         │
                    └──────────────────────┘

A note can explain a business rule, constraint or design decision.


---

24. Building Block 2: Relationships

The second major UML building block is:

> Relationships



Relationships connect modelling elements.

Important UML relationships include:

1. Association


2. Dependency


3. Generalization


4. Realization



Later we will also encounter relationships such as include/extend in use cases and aggregation/composition in structural modelling.


---

25. Association

An association represents a structural relationship between classifiers.

Example:

Student ───────── Course

We could name the association:

Student ─── registers for ─── Course

This means students have a relationship with courses.


---

26. Multiplicity

An association can specify how many instances participate in a relationship.

For example:

Student 1 ───────── 0..* Course

Meaning:

> One Student can be associated with zero or many Courses.



Common multiplicities include:

Notation	Meaning

1	Exactly one
0..1	Zero or one
*	Many
0..*	Zero or many
1..*	One or many
2..5	Between two and five


We will study multiplicity in detail during class modelling.


---

27. Dependency

A dependency indicates that one element depends on another.

Conceptually:

ReportGenerator - - - - > Payment

The dashed arrow indicates dependency.

For example, a report generation component may depend on payment information.

If the supplier element changes, the dependent element may be affected.


---

28. Generalization

Generalization represents a general-to-specific relationship.

Example:

User
                  △
                  |
        ┌─────────┴─────────┐
        |                   |
     Student             Lecturer

Student and Lecturer are specialized types of User.

The hollow triangle points toward the more general classifier.


---

29. Realization

Realization indicates that one classifier fulfills a contract specified by another, commonly an interface.

For example:

PaymentProcessor
     △
     |  «realize»
     |
MobileMoneyProcessor

The implementation class provides the operations specified by the interface.


---

30. Building Block 3: Diagrams

The third major conceptual building block is:

> Diagrams



A diagram provides a visual representation of selected parts of a model.

The important point is:

> A diagram is a view of a model, not necessarily the entire model.



This is why large systems require multiple diagrams.


---

31. UML Diagram Categories

The UML 2.x family contains diagrams that can broadly be understood as:

Structural diagrams

Show relatively static structure.

Behaviour diagrams

Show behaviour.

Interaction diagrams

Show interactions, which are a specialized form of behaviour modelling.

OMG currently lists the following structural diagrams:

Class

Object

Component

Composite Structure

Package

Deployment


Behaviour diagrams include:

Use Case

Activity

State Machine


Interaction diagrams include:

Sequence

Communication

Timing

Interaction Overview. 



---

32. UML Diagram Map

A useful way for students to remember the diagram families is:

UML DIAGRAMS
                              |
                ┌─────────────┴─────────────┐
                ↓                           ↓
          STRUCTURAL                    BEHAVIOURAL
                |                           |
       ┌────────┼────────┐          ┌───────┼────────┐
       ↓        ↓        ↓          ↓       ↓        ↓
     Class    Object   Component  Use Case Activity State
       |
   Package
       |
 Deployment
                              |
                              ↓
                       INTERACTION
                              |
             ┌────────┬──────┼──────┐
             ↓        ↓      ↓      ↓
         Sequence Communication Timing Interaction
                              Overview

The exact classification and notation should be learned from the UML specification rather than relying on informal diagrams from random websites. OMG's UML 2.5.1 specification provides the normative language definition. 


---

33. What Is a Class Diagram Used For?

A class diagram answers questions such as:

> What classes exist?



> What attributes do they have?



> What operations do they have?



> How are the classes related?



Example:

┌───────────────┐
│    Student    │
├───────────────┤
│ studentID     │
│ name          │
└───────────────┘
        |
        |
   registers
        |
        ↓
┌───────────────┐
│    Course     │
├───────────────┤
│ courseCode    │
│ courseName    │
└───────────────┘


---

34. What Is a Use-Case Diagram Used For?

A use-case diagram focuses on:

> What should users be able to accomplish with the system?



Example:

Student
          |
          |
      (Register Course)
          |
          |
      (View Results)

Use cases help capture system functionality from the user's perspective.

We will study these deeply in Week 9.


---

35. What Is a Sequence Diagram Used For?

A sequence diagram answers:

> Who communicates with whom, and in what order?



Example:

Student       System        Database
   |             |              |
   | Login       |              |
   |------------>|              |
   |             | Verify       |
   |             |------------->|
   |             |<-------------|
   | Confirmation|              |
   |<------------|              |

The vertical direction generally represents progression through time.


---

36. What Is an Activity Diagram Used For?

It models workflow.

Example:

Start
  ↓
Login
  ↓
Select Course
  ↓
Check Eligibility
  ↓
 ┌───────────────┐
 │ Eligible?     │
 └───────┬───────┘
       Yes│
          ↓
    Register Course
          ↓
         End

It is particularly useful for business processes.


---

37. What Is a State Machine Diagram Used For?

It models how an entity changes state.

Example:

submit
Draft ───────────→ Submitted
                      |
                   approve
                      ↓
                   Approved
                      |
                  complete
                      ↓
                  Completed

This is useful when an object has a meaningful lifecycle.


---

38. What Is a Component Diagram Used For?

It shows major software components and their dependencies.

Example:

[Mobile App]
      |
      ↓
[API Component]
      |
 ┌────┴─────┐
 ↓          ↓
[Auth]    [Registration]
              |
              ↓
         [Database]

This is more closely associated with design and architecture than early requirements analysis.


---

39. What Is a Deployment Diagram Used For?

It represents the physical/execution environment where software is deployed.

Example:

┌────────────────────┐
│ Mobile Device      │
│ [Mobile App]       │
└─────────┬──────────┘
          │
          ↓
┌────────────────────┐
│ Application Server │
│ [API]              │
└─────────┬──────────┘
          │
          ↓
┌────────────────────┐
│ Database Server    │
│ [Database]         │
└────────────────────┘

Deployment modelling becomes useful when discussing physical system architecture.


---

40. Rules of UML

The course outline specifically includes:

> Rules of UML



This means students need to understand that UML is not simply a collection of shapes.

There are rules governing:

what elements mean;

how elements relate;

how notation is used;

what constitutes a meaningful/well-formed model.



---

41. UML Syntax and Semantics

Two important terms are:

Syntax

The rules concerning how something is represented.

Think:

> How is it written/drawn?



Semantics

The meaning of what has been represented.

Think:

> What does it mean?




---

42. Simple Example of Syntax vs Semantics

Suppose we draw:

Student ───── Course

Syntax

The line and boxes follow a particular notation.

Semantics

The relationship represented by the line has a particular meaning.

If we say:

Student ─── registers for ─── Course

the model communicates a specific business relationship.

Therefore:

> A diagram can look attractive but still communicate the wrong meaning.




---

43. Well-Formedness

A model is well-formed when it satisfies the relevant rules of the modelling language.

For example, if a particular UML relationship requires specific kinds of elements at its ends, you cannot arbitrarily connect unrelated elements and claim the resulting model has the intended UML meaning.

The formal UML specification explicitly defines concepts, abstract syntax, semantics and notation; its specification clauses include rules and examples for the various modelling formalisms. 


---

44. Four Questions When Checking a UML Model

Students can use this simple checklist:

Question 1

Is the notation correct?

Question 2

Does the relationship make semantic sense?

Question 3

Does the model satisfy the system requirements?

Question 4

Can another person understand the model?

All four matter.


---

45. UML Common Mechanisms

The traditional conceptual model of UML describes four mechanisms that apply throughout the language:

1. Specifications


2. Adornments


3. Common divisions


4. Extensibility mechanisms



These mechanisms are part of the classic conceptual explanation of UML and remain useful pedagogically even though students should ultimately consult the formal UML specification for normative details. 

Let's explain them carefully.


---

46. Mechanism 1: Specifications

A UML graphical symbol is not necessarily the complete definition of a model element.

For example:

┌──────────────┐
│   Student    │
└──────────────┘

This simple box doesn't show everything about Student.

Behind it is a conceptual specification that can include:

name;

attributes;

operations;

visibility;

relationships;

constraints;

other properties.


Therefore:

> The diagram is a visual representation of a deeper model.



The formal UML specification defines the underlying language concepts rather than treating diagrams as the entire language. 


---

47. Mechanism 2: Adornments

An adornment adds additional information to a basic graphical element.

For example:

┌────────────────────────┐
│        Student         │
├────────────────────────┤
│ - studentID: String    │
│ + name: String         │
├────────────────────────┤
│ + registerCourse()     │
└────────────────────────┘

The symbols:

-
+

provide additional information about visibility.

Other adornments can indicate:

stereotypes;

properties;

multiplicity;

constraints;

modifiers.



---

48. Mechanism 3: Common Divisions

UML repeatedly separates concepts into useful paired distinctions.

One familiar example is:

Class ↔ Object

A class describes a type.

An object is an instance.

Another distinction:

Interface ↔ Implementation

The interface describes a contract.

The implementation provides the actual behaviour.

Another useful distinction:

Specification ↔ Instance

These divisions help students understand different levels of abstraction.


---

49. Mechanism 4: Extensibility

UML provides mechanisms for extending or customizing the modelling language for particular domains.

Important concepts include:

1. Stereotypes


2. Tagged values


3. Constraints



These are extremely important in advanced UML.


---

50. Stereotype

A stereotype allows a modeller to give an element a more specialized meaning.

Example:

«entity»
Student

The word:

«entity»

is a stereotype.

Another:

«controller»
RegistrationController

Another:

«boundary»
RegistrationPage

The stereotype provides additional modelling meaning.


---

51. Tagged Values

A tagged value provides additional property information.

Conceptually:

Student
{author = "Analysis Team"}

or:

Server
{location = "Data Centre"}

Tagged values can provide metadata about a model element.


---

52. Constraints

A constraint is a condition that must be satisfied.

For example:

{age >= 18}

or:

{balance >= 0}

or in a university:

{student must satisfy prerequisite}

A constraint makes a rule explicit in the model.


---

53. Why Constraints Matter

Consider:

Student ─── registers ─── Course

This alone doesn't tell us:

> "The student must have passed the prerequisite."



We can express an additional constraint:

{PrerequisiteSatisfied = true}

The model now contains more precise information.


---

54. UML Architecture

Now we reach the final major topic for Week 3:

> UML Architecture



This is potentially one of the most confusing topics for beginners.

Don't worry—we'll break it down slowly.


---

55. What Does "UML Architecture" Mean?

In this context, we are talking about the architectural organization of the UML modelling language itself.

It is not the same as:

> "Three-tier software architecture"



or:

> "Client-server architecture."



Instead, UML has a layered meta-modelling structure.

The commonly discussed architecture has four levels:

M3
↓
M2
↓
M1
↓
M0


---

56. The Four UML Layers

A simplified explanation is:

Layer	Name	Simple meaning

M3	Meta-metamodel	Defines the language used to define metamodels
M2	Metamodel	Defines UML concepts
M1	Model	Your actual UML model
M0	Instances	Real/runtime instances


This four-layer architecture is a standard way of describing UML's meta-modelling infrastructure. 


---

57. M0 — The Real World / Instance Level

Start at the bottom.

M0 contains actual instances.

Imagine our university system has:

Student:
ID = ST001
Name = Francis

and:

Student:
ID = ST002
Name = Grace

These are actual instances.

Think:

> M0 = actual things/instances




---

58. M1 — The Model Level

Now we create a UML model:

┌─────────────────┐
│     Student     │
├─────────────────┤
│ studentID       │
│ name            │
│ programme       │
└─────────────────┘

This defines the structure of Student objects.

This is our actual user/system modelling level.

Think:

> M1 = the UML model created by analysts/designers




---

59. M2 — The Metamodel Level

Now ask:

> "What makes something a valid UML Class?"



The UML language itself defines concepts such as:

Class;

Property;

Operation;

Association;

Generalization;

UseCase;

Actor;

State;

Activity.


These concepts form part of the UML metamodel.

Think:

> M2 = definitions of UML modelling concepts




---

60. M3 — The Meta-Metamodel Level

Now we ask:

> "What language/framework is used to define the UML metamodel?"



This is where MOF — Meta Object Facility enters the picture.

M3 provides the meta-metamodelling foundation.

Think:

> M3 = language/framework used to define metamodels



OMG maintains MOF as an OMG specification alongside UML. 


---

61. The Four Layers Using a Simple Analogy

Imagine a dictionary.

M3

Rules for defining languages.

M2

Definitions such as:

> Class, Attribute, Association



M1

Your actual model:

> Student, Course, Registration



M0

Actual instances:

> Francis, BICT3202, Registration #12345



So:

M3 → Defines how modelling languages are defined

M2 → Defines UML concepts

M1 → Defines your system

M0 → Contains actual instances


---

62. University Example of M0–M3

Let's make it concrete.

M0 — Actual instances

Francis : Student
Grace : Student
BICT3202 : Course

M1 — Your model

Student
Course
Registration

M2 — UML concepts

Class
Attribute
Association
Operation

M3 — Meta-modelling foundation

MOF

Diagrammatically:

┌──────────────────────────────┐
│ M3                           │
│ Meta-metamodel / MOF         │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ M2                           │
│ UML Metamodel                │
│ Class, Attribute, Association│
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ M1                           │
│ University UML Model         │
│ Student, Course, Registration│
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ M0                           │
│ Actual Instances             │
│ Francis, BICT3202, etc.      │
└──────────────────────────────┘

The four-layer idea is useful because it separates the language, models written in that language, and the instances represented by those models. 


---

63. Why Does This Architecture Matter?

A student may ask:

> "Why should I care about M0–M3? I'm just trying to draw a class diagram."



Good question.

For introductory modelling, students can use UML without deeply understanding the meta-level architecture.

However, understanding the layers helps explain:

1. Why UML is a language

UML has formal definitions.

2. Why UML tools can validate models

Tools can work against formal modelling concepts.

3. Why UML has consistent semantics

Its constructs are formally defined.

4. How modelling languages themselves are defined

This becomes important in advanced model-driven engineering and metamodeling.


---

64. UML Architecture vs Software Architecture

Do not confuse these.

UML architecture

M3
M2
M1
M0

Describes the organization of the modelling language and its abstraction levels.

Software architecture

Could be:

Presentation Layer
        ↓
Business Logic Layer
        ↓
Data Access Layer
        ↓
Database

These are completely different concepts.

This distinction is extremely important in examinations.


---

65. UML and CASE Tools

The syllabus later mentions:

> CASE Tool: Select Enterprise Demonstration



UML is commonly supported by modelling/CASE tools.

Examples include tools that allow users to:

create UML diagrams;

maintain models;

check relationships;

document requirements;

generate code in some workflows;

reverse-engineer code in some tools;

collaborate on designs.


A UML tool should not be confused with UML itself.

UML

The modelling language/standard.

UML Tool

Software used to create and manage UML models.

This distinction will become useful when we perform practical modelling.


---

66. A Complete Week 3 Example

Let's combine everything.

System: University Registration System

Requirement

> Students should be able to register for courses online.




---

UML Perspective 1 — Use Case

Student
           |
           |
    (Register Course)

This focuses on user functionality.


---

UML Perspective 2 — Class Model

┌───────────────┐
│    Student    │
├───────────────┤
│ studentID     │
│ name          │
└───────────────┘
       |
       | registers
       |
┌───────────────┐
│    Course     │
├───────────────┤
│ courseCode    │
│ courseName    │
└───────────────┘

This focuses on structure.


---

UML Perspective 3 — Sequence

Student        System        Course
   |              |             |
   | register     |             |
   |------------->|             |
   |              | check       |
   |              |------------>|
   |              |<------------|
   | confirmation |             |
   |<-------------|             |

This focuses on interaction.


---

UML Perspective 4 — Activity

Start
  ↓
Login
  ↓
Select Course
  ↓
Check Prerequisite
  ↓
Eligible?
 /     \
No      Yes
 |       |
End   Register
          ↓
     Confirmation
          ↓
         End

This focuses on workflow.


---

UML Perspective 5 — State

A Registration object might move through:

Draft
  ↓
Submitted
  ↓
Approved
  ↓
Completed

This focuses on lifecycle.


---

67. Why Multiple UML Diagrams Are Better

Each diagram answers a different question.

Diagram	Main question

Use Case	What does the user want to accomplish?
Class	What structural elements exist?
Object	What are particular instances?
Sequence	How do participants communicate over time?
Communication	Which objects communicate and how?
Activity	What workflow occurs?
State Machine	How does an entity change state?
Component	What major software components exist?
Deployment	Where does the software run?
Package	How are model elements organized?


This is why UML is powerful:

> Different diagrams provide different views of the same system.




---

68. Common Student Confusions

Confusion 1: UML = Flowchart

No.

A flowchart is one type of process representation.

UML is a broad modelling language containing many diagram types.


---

Confusion 2: UML = Programming

No.

UML models the system.

Programming implements the system.


---

Confusion 3: UML = Software Development Method

No.

UML is a modelling language.

A process such as UP defines development activities.


---

Confusion 4: Every UML diagram describes the same thing

No.

Each diagram emphasizes a particular aspect.


---

Confusion 5: UML diagrams are just pictures

No.

The graphical notation represents formal modelling concepts with defined semantics and rules. The UML specification defines the language's abstract syntax and semantics in addition to its notation. 


---

Confusion 6: UML 2.5.1 means 25 different UML versions

No.

It is a version number:

> 2.5.1



The OMG specification history shows UML 2.5.1 was adopted in December 2017. 


---

69. Practical Session — Week 3

Practical Title

Introduction to UML Modelling

Students should use a UML modelling tool or an appropriate diagramming environment.

Possible tools include:

desktop UML CASE tools;

web-based UML tools;

diagramming software with UML support.


The specific tool is less important at this stage than understanding the UML concepts and notation.


---

Practical Task 1

Create a simple class diagram containing:

Student
Course
Lecturer
Registration


---

Practical Task 2

Add attributes.

Student

studentID
name
programme

Course

courseCode
courseName
credits

Lecturer

lecturerID
name
department

Registration

registrationID
date
status


---

Practical Task 3

Add relationships:

Student ───── Registration
Course ────── Registration
Lecturer ───── Course


---

Practical Task 4

Add multiplicities.

Students should reason about whether:

Student 1 ─── 0..* Registration

makes sense.

They should also determine whether:

Course 1 ─── 0..* Registration

is appropriate.


---

70. Tutorial Activity

"Which Diagram Should I Use?"

Give students the following situations.

Scenario A

> "We want to know what functions a student can perform."



Expected: Use Case Diagram.


---

Scenario B

> "We want to know the classes and relationships in the system."



Expected: Class Diagram.


---

Scenario C

> "We want to show the order in which a student, system and database communicate."



Expected: Sequence Diagram.


---

Scenario D

> "We want to show the steps involved in registering a course."



Expected: Activity Diagram.


---

Scenario E

> "We want to show the different states of an application."



Expected: State Machine Diagram.


---

Scenario F

> "We want to show where application components are deployed."



Expected: Deployment Diagram.

This exercise teaches students to choose a diagram based on the question they are trying to answer, rather than memorizing diagrams blindly.


---

71. Independent Learning — 10 Hours

Activity 1

Study the official OMG UML 2.5.1 specification. It is the authoritative formal specification for the UML version used in this module. 

[OMG UML 2.5.1 Specification](https://www.omg.org/spec/UML/2.5.1/PDF?utm_source=chatgpt.com)

Students do not need to read all 700+ pages at this stage. The specification is a formal reference, not a beginner textbook. Its own introduction notes that it is intended to be read non-sequentially and organized around abstract syntax, semantics, notation and examples. 


---

Activity 2

Create a table containing at least 10 UML diagram types and explain:

1. What the diagram represents.


2. What question it answers.


3. When it is useful.


4. A university example.




---

Activity 3

Take the University Registration System from Weeks 1 and 2 and identify which UML diagram you would use for each:

requirements;

structure;

workflow;

interaction;

lifecycle;

deployment.



---

72. Examination Questions

Question 1

> Define UML and explain its importance in Object-Oriented Analysis and Design.



A strong answer should mention:

Unified Modeling Language;

modelling language;

standardization;

visualization;

specification;

documentation;

communication;

structure and behaviour.



---

Question 2

> Differentiate between a modelling language and a software development methodology. Use UML and UP as examples.




---

Question 3

> Explain the three conceptual building blocks of UML.



Expected:

1. Things


2. Relationships


3. Diagrams




---

Question 4

> Explain structural, behavioural, grouping and annotational elements in UML. Give examples.




---

Question 5

> Differentiate between syntax and semantics in UML.




---

Question 6

> Explain the four common mechanisms of UML.



Expected:

1. Specifications


2. Adornments


3. Common divisions


4. Extensibility mechanisms




---

Question 7

> Explain the UML four-layer architecture using a practical example.



Expected:

M3 → Meta-metamodel
M2 → Metamodel
M1 → Model
M0 → Instances


---

73. Examination Challenge

Scenario

A university wants to develop a mobile student registration application.

The application should allow students to:

log in;

view courses;

register courses;

drop courses;

view registration status.


The system will communicate with a university server and database.

Task

Identify the most appropriate UML diagram for each requirement:

Requirement	Appropriate diagram

Show what students can do	?
Show Student and Course classes	?
Show login communication	?
Show registration workflow	?
Show registration states	?
Show application/server/database deployment	?


Students should explain why they selected each diagram.


---

74. Week 3 Summary

Let's bring everything together.

UML

Unified Modeling Language is a standardized modelling language for visualizing, specifying and documenting systems. 

UML is not:

a programming language;

a database;

a development methodology;

a replacement for requirements analysis.


UML building blocks

Things
Relationships
Diagrams

Things

Can be understood conceptually as:

Structural
Behavioural
Grouping
Annotational

Relationships

Important examples include:

Association
Dependency
Generalization
Realization

Diagrams

Provide different views of a system.

Rules

Define how UML elements can be used meaningfully and consistently.

Common mechanisms

Specifications
Adornments
Common divisions
Extensibility mechanisms

Extensibility

Includes:

Stereotypes
Tagged values
Constraints

UML Architecture

M3 → Meta-metamodel
M2 → UML metamodel
M1 → User/system model
M0 → Actual instances

OMG's current formal UML catalogue lists UML 2.5.1 as the formal UML specification, adopted in December 2017. 


---

75. The Most Important Lesson of Week 3

Students should leave this week understanding one fundamental idea:

> UML is not about drawing pretty diagrams. UML is a standardized language for communicating models of a system.



A good UML model should answer questions such as:

> What exists?



> How are things related?



> What can users do?



> What happens?



> How do objects communicate?



> How does an object change state?



> What software components exist?



> Where does the software run?



And different UML diagrams answer different questions.

The progression so far is therefore:

WEEK 1
Business problem
      ↓
Business needs
      ↓
Requirements

WEEK 2
Requirements
      ↓
Objects
      ↓
Attributes + Behaviour + Relationships
      ↓
Object Model

WEEK 3
Object Model
      ↓
UML
      ↓
Standard notation
      ↓
Different UML views

That prepares us for Week 4, where we will go deeper into the UML building blocks, UML rules, common mechanisms and architecture, with much more attention to the actual notation and how the different UML concepts fit together. This will give students the foundation needed before we begin formal Object-Oriented Analysis and Object/Class Modelling in Week 5.


---

References

Authoritative / Current Sources

Object Management Group. (2017). OMG Unified Modeling Language (OMG UML), Version 2.5.1. OMG. 

Object Management Group. (n.d.). Unified Modeling Language (UML). OMG. 

Object Management Group. (n.d.). What is UML? OMG. 

Object Management Group. (n.d.). Introduction to OMG Specifications. OMG. 

Object Management Group. (2017). Meta Object Facility (MOF), Version 2.5.1. OMG. 


Classic OOAD Reference

Booch, G., Rumbaugh, J., & Jacobson, I. (1999). The Unified Modeling Language User Guide. Addison-Wesley.


The classic UML teaching framework emphasizes understanding UML through its building blocks, rules and common mechanisms before learning its more detailed diagramming features. 

Prescribed Texts from the Module Outline

Mach, E. (2019). Object Oriented Analysis & Design Cookbook: Introduction to Practical System Modeling.

Reddy, V., & Korra, S. (2018). Object-Oriented Analysis and Design Using UML.

The Art of Service. (2021). Object Oriented Analysis and Design: A Complete Guide.


Recommended Texts

Wixom, B., & Dennis, A. (2018). Systems Analysis and Design.

Blokdyk, G. (2021). Object-Oriented Analysis and Design Standard Requirements.

Wixom, B., & Dennis, A. (2020). Systems Analysis and Design: An Object-Oriented Approach with UML.
