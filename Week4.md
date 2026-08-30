BICT 3202 — Object-Oriented Analysis and Design

WEEK 4: UML BUILDING BLOCKS, RULES, MECHANISMS AND ARCHITECTURE

Programme: BSc Information Communication and Technology
Year: 3
Course Code: BICT 3202
Week: 4 of 16
Lectures: 2 hours
Tutorial: 1 hour
Practical: 1 hour
Independent Learning: 10 hours
Credits: 10


---

1. Week 4 Introduction

In Week 3, we introduced UML and answered the basic question:

> What is UML and why do we need it?



We learned that UML is a standardized modelling language used to visualize, specify and document systems. The current formal OMG specification available for UML is UML 2.5.1. It defines the language formally through concepts such as abstract syntax, semantics, notation and examples. 

This week we go one level deeper.

The course outline specifically requires:

The Building Blocks of UML

Rules of UML

Mechanisms of UML

UML Architecture


So, by the end of Week 4, students should not simply know that UML exists. They should understand what UML is made of, how its notation works, how UML models are governed by rules, and how UML is organized conceptually.


---

2. Week 4 Learning Outcomes

By the end of this week, a student should be able to:

1. Explain the building blocks of UML.


2. Identify different types of UML elements.


3. Explain structural things.


4. Explain behavioural things.


5. Explain grouping things.


6. Explain annotational things.


7. Explain relationships between UML elements.


8. Distinguish association, dependency, generalization and realization.


9. Explain the role of UML diagrams.


10. Explain UML notation and semantics.


11. Explain UML well-formedness.


12. Explain specifications and adornments.


13. Explain common divisions in UML.


14. Explain UML extensibility mechanisms.


15. Explain stereotypes.


16. Explain tagged values.


17. Explain constraints.


18. Explain UML profiles at an introductory level.


19. Explain UML's layered architecture.


20. Distinguish M0, M1, M2 and M3.


21. Apply these concepts to a practical university information system.


22. Identify common mistakes students make when drawing UML.




---

3. A Simple Way to Understand UML

Before going into technical definitions, imagine that we want to build a University Student Management System.

We need to answer several questions.

Question 1: What exists?

For example:

Student
Lecturer
Course
Registration
Payment
Result

Question 2: How are these things related?

For example:

Student ───── registers for ───── Course

Question 3: What can users do?

For example:

Student → Register Course
Student → View Results
Student → Pay Fees

Question 4: What happens?

For example:

Login
 ↓
Select Course
 ↓
Check Prerequisite
 ↓
Register
 ↓
Confirmation

Question 5: How do objects communicate?

For example:

Student → Registration System → Database

UML gives us different modelling elements and diagrams to answer these different questions.


---

4. UML Building Blocks

A useful way to understand UML is to divide its building blocks into:

UML BUILDING BLOCKS
                         |
        ┌────────────────┼────────────────┐
        ↓                ↓                ↓
      Things        Relationships      Diagrams

The traditional conceptual treatment of UML further divides "things" into:

Structural Things
Behavioural Things
Grouping Things
Annotational Things

This is a very useful classification for students because it prevents them from seeing UML as just a collection of random shapes.


---

5. Structural Things

Structural things represent the relatively static parts of a system.

Ask:

> What exists in the system?



Examples include:

Class

Interface

Object

Component

Node



---

6. Class

A class describes a type of object.

For example:

┌──────────────────────────┐
│         Student          │
├──────────────────────────┤
│ studentID                │
│ name                     │
│ programme                │
│ yearOfStudy              │
├──────────────────────────┤
│ registerCourse()         │
│ viewResults()            │
└──────────────────────────┘

The three major sections are:

Section 1 — Name

Student

Section 2 — Attributes

studentID
name
programme
yearOfStudy

Section 3 — Operations

registerCourse()
viewResults()

The class therefore tells us:

> "A Student object has these characteristics and can perform these operations."




---

7. Object

An object is a particular instance of a class.

Suppose we have:

Student

That is the class.

A particular student could be:

student001 : Student

with:

studentID = "ST001"
name = "Francis"
programme = "BSc ICT"

Therefore:

> Class = general definition



> Object = particular instance



Think of the relationship this way:

CLASS
Student
   ↓
creates/represents
   ↓
OBJECTS
Francis : Student
Grace : Student
John : Student

This distinction is extremely important in OOAD.


---

8. Interface

An interface defines a set of operations that another element agrees to provide.

For example:

«interface»
PaymentService
----------------------
processPayment()
refundPayment()
checkPaymentStatus()

We could have different implementations:

PaymentService
                       △
                       |
          ┌────────────┼────────────┐
          ↓            ↓            ↓
      BankPayment   MobileMoney   CardPayment

The important idea is:

> An interface defines what services are available, while an implementation determines how those services are performed.




---

9. Component

A component represents a modular part of a system.

For example:

University System
│
├── Authentication Component
├── Student Component
├── Registration Component
├── Finance Component
└── Examination Component

A component should ideally have a clear responsibility.

This connects directly to one of the major OO principles from Week 2:

> Modularity



Instead of building one enormous system as one piece, we divide it into manageable components.


---

10. Node

A node represents a computational resource or execution environment.

For example:

┌──────────────────────┐
│ Mobile Phone         │
│ Student App          │
└──────────┬───────────┘
           │
           ↓
┌──────────────────────┐
│ Application Server   │
│ University API       │
└──────────┬───────────┘
           │
           ↓
┌──────────────────────┐
│ Database Server      │
│ Student Database     │
└──────────────────────┘

Nodes become particularly important when we discuss deployment diagrams.


---

11. Behavioural Things

Structural things answer:

> What exists?



Behavioural things answer:

> What happens?



Examples include:

interactions;

activities;

state machines.


The official UML specification organizes modelling concepts into structural and behavioural areas; its clauses cover such subjects as classes, activities, state machines, interactions, use cases and deployments. 


---

12. Interaction

An interaction describes communication between elements.

Imagine a student logging into the university system:

Student
   |
   | username + password
   ↓
Login System
   |
   | verify credentials
   ↓
Database
   |
   | result
   ↓
Login System
   |
   | success
   ↓
Student

The important question is:

> Who communicates with whom, and what messages are exchanged?



This leads naturally to sequence diagrams and communication diagrams.


---

13. Activity

An activity represents a workflow.

For example, course registration:

START
          ↓
        Login
          ↓
    Select Course
          ↓
 Check Prerequisites
          ↓
     Is student
      eligible?
       /     \
     No       Yes
     ↓         ↓
   Reject    Register
               ↓
        Confirmation
               ↓
              END

An activity diagram is therefore useful when we want to understand:

> What steps happen in a process?




---

14. State Machine

A state machine represents changes in the state of an object.

Consider a university application:

Draft
  |
  | submit
  ↓
Submitted
  |
  | review
  ↓
Under Review
  |
  | approve
  ↓
Approved
  |
  | complete
  ↓
Completed

The important concepts are:

State

Event

Transition


For example:

Submitted
     |
     | Reviewer approves
     ↓
Approved

Submitted = state

Reviewer approves = event

Arrow = transition


---

15. Grouping Things

Large UML models can become very complicated.

Imagine a university has 150 classes.

Putting everything into one diagram would be difficult to understand.

We can group related elements into packages.

Example:

University System
│
├── Student Management
│   ├── Student
│   ├── Programme
│   └── Registration
│
├── Finance
│   ├── Payment
│   ├── Invoice
│   └── Account
│
└── Examination
    ├── Exam
    ├── Result
    └── Grade

This makes a large model easier to manage.


---

16. Annotational Things

An annotation provides explanatory information.

The simplest example is a note.

For example:

┌──────────────┐
│   Student    │
└──────────────┘
       |
       |  - - - - - - - - - - - - - - - - - -
       |                                   
       ↓
┌─────────────────────────────────────────┐
│ Note: Student must satisfy all course   │
│ prerequisites before registration.      │
└─────────────────────────────────────────┘

The note does not represent a new business object.

It explains something about the model.


---

17. Relationships in UML

Now we move to the second major building block:

> Relationships



A relationship tells us how model elements are connected.

Important relationships include:

1. Association


2. Dependency


3. Generalization


4. Realization



These must not be confused with one another.


---

18. Association

An association represents a relationship between model elements.

Example:

Student ───────── Course

We can give the relationship a meaningful name:

Student ─── registers for ─── Course

This tells us that Student and Course have a structural relationship.


---

19. Association Example

Suppose:

> A student can register for courses.



We could model:

Student 1 ───────── 0..* Course

This says one Student can be associated with zero or many Course instances.

However, in a realistic university system, we may discover that the relationship needs a separate Registration class because registration has information of its own:

Student
   |
   |
Registration
   |
   |
Course

Registration might have:

registrationDate
status
semester
grade

This is an important OOAD insight:

> When a relationship has important information or behaviour of its own, it may need to be represented as a class.



We will develop this idea further in later object modelling weeks.


---

20. Dependency

A dependency means one element relies on another.

Conceptually:

ReportGenerator - - - - - - > Payment

The dashed arrow represents dependency.

For example:

> The ReportGenerator uses Payment information to generate a financial report.



If Payment changes in a way that affects what ReportGenerator expects, ReportGenerator may also be affected.

Think:

> Dependency = "I need/use that other element."




---

21. Generalization

Generalization represents a general-to-specific relationship.

Example:

User
                  △
                  |
        ┌─────────┴─────────┐
        ↓                   ↓
     Student             Lecturer

Here:

User

is more general.

Student
Lecturer

are specialized forms of User.

The hollow triangle points toward the more general element.

This is extremely important.

Remember:

> Triangle points to the parent/general class.




---

22. Generalization Example in Everyday Life

Think about vehicles:

Vehicle
                   △
                   |
          ┌────────┴────────┐
          ↓                 ↓
        Car              Motorcycle

A Car is a Vehicle.

A Motorcycle is a Vehicle.

But Vehicle is not necessarily a Car.

This relationship represents specialization.


---

23. Realization

Realization commonly occurs when a class implements an interface.

Example:

«interface»
              PaymentService
                    △
                    |
                    |
              MobilePayment

The interface says:

processPayment()

The implementing class provides the actual implementation.

Think:

> Interface = contract



> Implementation = fulfils the contract




---

24. Association vs Dependency vs Generalization vs Realization

This is a common examination area.

Relationship	Simple meaning

Association	"These elements are related."
Dependency	"This element uses/depends on that element."
Generalization	"This is a specialized type of that."
Realization	"This element fulfils the contract specified by that."


Example

Student ───── Course

Association.

ReportGenerator - - - > Payment

Dependency.

Student ─────▷ User

Generalization, where the triangle points to User.

MobilePayment - - -▷ PaymentService

Realization of an interface.


---

25. UML Diagrams

The third major building block is:

> Diagrams



A diagram gives us a particular visual view of a model.

The important idea is:

> A diagram is not necessarily the whole system.



Instead, different diagrams emphasize different aspects.

The official UML 2.5.1 specification explicitly has a section devoted to UML diagrams and separates structural, behavioural and other modelling concepts. 


---

26. Structural vs Behavioural Diagrams

A simple way to remember the distinction:

Structural

> What exists?



Behavioural

> What happens?



For example:

Class Diagram

asks:

> What classes exist and how are they related?



Whereas:

Activity Diagram

asks:

> What steps occur in this process?




---

27. Structural UML Diagrams

Important structural diagrams include:

Class Diagram

Object Diagram

Component Diagram

Composite Structure Diagram

Package Diagram

Deployment Diagram



---

28. Behavioural UML Diagrams

Important behavioural diagrams include:

Use Case Diagram

Activity Diagram

State Machine Diagram


Interaction diagrams are a specialized family of behavioural modelling and include:

Sequence Diagram

Communication Diagram

Interaction Overview Diagram

Timing Diagram


The UML 2.5.1 specification organizes these concepts formally and includes a dedicated diagram section. 


---

29. Rules of UML

Now we move to the second major Week 4 topic:

Rules of UML

Students sometimes think:

> "If I draw boxes and arrows, I have created UML."



Not necessarily.

UML has defined concepts, notation and semantics.

The official specification distinguishes between abstract syntax, semantics and notation, and provides examples for modelling concepts. 


---

30. Syntax

Syntax concerns how something is represented.

For example, a UML class is represented using a classifier notation such as:

┌─────────────────┐
│     Student     │
└─────────────────┘

The notation has rules.


---

31. Semantics

Semantics concerns meaning.

Suppose we draw:

Student ───── Course

The line is not simply decoration.

It represents a specific UML relationship.

Therefore:

> Syntax tells us how something is represented.



> Semantics tells us what that representation means.




---

32. Why Syntax and Semantics Matter

Imagine a student creates:

Student ◇──── Course

and says:

> "This means Student registers for Course."



The lecturer needs to ask:

> "Do you understand what that diamond means?"



The diamond has UML meaning.

If the student uses it simply because:

> "It looks nice,"



the model is wrong.

This is why UML notation should be learned together with its meaning.


---

33. Well-Formed UML Models

A well-formed model follows the relevant rules of the modelling language.

A model can fail in different ways.

Problem 1 — Notation error

The symbol is drawn incorrectly.

Problem 2 — Semantic error

The symbol is technically recognizable but communicates the wrong meaning.

Problem 3 — Requirement error

The diagram may be syntactically valid but does not represent what the actual system requires.

That third one is especially important.

A perfectly drawn UML diagram can still describe the wrong system.


---

34. UML Quality Checklist

Before accepting a UML diagram, ask:

Question 1

Are the correct UML symbols being used?

Question 2

Are relationships represented correctly?

Question 3

Are names meaningful?

Question 4

Are multiplicities correct?

Question 5

Does the model correspond to requirements?

Question 6

Can another person understand the model?

Question 7

Have unnecessary details been removed?


---

35. Mechanisms of UML

The course outline also requires:

> Mechanisms of UML



Traditional UML teaching introduces four important common mechanisms:

1. Specifications


2. Adornments


3. Common divisions


4. Extensibility mechanisms



Let's examine each carefully.


---

36. Specification

A UML diagram is a visual representation of an underlying model.

For example:

┌──────────────────────┐
│       Student        │
└──────────────────────┘

The box does not necessarily show every property of Student.

The underlying model could contain:

Name:
Student

Attributes:
studentID
name
programme

Operations:
registerCourse()
viewResults()

Relationships:
Registration
Programme

Therefore:

> The graphical notation is a view of a richer underlying specification.



This is consistent with the formal UML specification, which separates the formal language concepts from their graphical notation. 


---

37. Adornments

An adornment adds extra information to a UML element.

For example:

┌──────────────────────────┐
│ Student                  │
├──────────────────────────┤
│ - studentID : String     │
│ + name : String          │
└──────────────────────────┘

Here:

-
+

provide visibility information.

Other information can also be added.

For example:

Student
----------------
+ name : String

The + tells us that the attribute is public.

The exact notation and semantics should follow the UML specification rather than informal conventions. 


---

38. Visibility Adornments

Common visibility symbols include:

Symbol	Meaning

+	Public
-	Private
#	Protected
~	Package


Example:

┌─────────────────────┐
│ Student             │
├─────────────────────┤
│ - studentID:String  │
│ + name:String       │
│ # programme:String  │
└─────────────────────┘

So:

-studentID

means private.

+name

means public.

#programme

means protected.


---

39. Common Divisions

UML frequently distinguishes between related concepts.

One important example is:

Class ↔ Object

Class

Describes a type.

Object

Represents an instance.

Another:

Interface ↔ Implementation

Interface

Defines a contract.

Implementation

Provides behaviour that fulfils that contract.

These distinctions help us avoid mixing levels of abstraction.


---

40. Type vs Instance

This is worth emphasizing.

Consider:

Student

This is a type/class.

Now:

Francis : Student

is an instance.

Think of a mould for making cakes.

Cake mould = Class
Individual cake = Object

The mould describes the general shape.

Each cake is an individual instance produced according to that general form.


---

41. Extensibility Mechanisms

UML is designed to be usable across many domains.

For example:

banking;

healthcare;

telecommunications;

education;

manufacturing;

cybersecurity.


Different domains may need specialized terminology.

UML provides mechanisms for extending/customizing its vocabulary.

Three important concepts are:

1. Stereotypes


2. Tagged values


3. Constraints




---

42. Stereotypes

A stereotype provides a specialized meaning to a UML element.

It is normally written inside guillemets:

«entity»
Student

or:

«controller»
RegistrationController

or:

«boundary»
RegistrationPage

The stereotype tells the reader:

> "Treat this element as a specialized kind of UML element."




---

43. Why Use Stereotypes?

Suppose we simply write:

Student

We know it is a class.

But suppose we write:

«entity»
Student

Now we are giving additional modelling information about its intended role.

Likewise:

«boundary»
RegistrationPage

suggests that the element plays a boundary/UI role.

Stereotypes are part of UML's profile/extensibility mechanisms; the formal UML specification defines stereotype-related concepts and constraints. 


---

44. Tagged Values

Tagged values allow additional property information to be attached to model elements.

Conceptually:

Server
{location = "Main Data Centre"}

Another example:

Student
{author = "Analysis Team"}

The tagged information provides additional metadata.


---

45. Constraints

A constraint specifies a condition or rule.

For example:

Student
{age >= 18}

Or:

Registration
{prerequisiteSatisfied = true}

The purpose is to communicate a rule that should hold.


---

46. Real University Example

Suppose a university says:

> A student cannot register for a course unless the prerequisite has been passed.



We could express this conceptually as:

Registration
{prerequisiteSatisfied = true}

This makes the business rule visible in the model.

Without the constraint, the class diagram might show:

Student ───── Course

but not explain the condition governing registration.


---

47. Stereotype vs Tagged Value vs Constraint

Students often confuse these.

Concept	Main purpose	Example

Stereotype	Gives specialized meaning/type	«entity» Student
Tagged value	Adds property/metadata	{author="Francis"}
Constraint	Specifies a condition/rule	{balance >= 0}


Easy memory trick:

Stereotype = What special kind?

Tagged value = What extra information?

Constraint = What condition must hold?


---

48. UML Profiles

A UML profile provides a way of tailoring UML for a particular domain or purpose.

For example, an organization may define modelling conventions for:

real-time systems;

business processes;

security;

enterprise architecture;

particular development environments.


A profile can define stereotypes and associated extensions.

Think:

> UML = general modelling language



> Profile = customized UML vocabulary/rules for a particular domain



The official UML 2.5.1 specification includes a standard profile as one of its normative machine-readable artifacts. 


---

49. UML Architecture — A Deeper Look

We introduced M0–M3 in Week 3.

This week we will make it clearer.

M3 ─ Meta-metamodel
 ↓
M2 ─ Metamodel
 ↓
M1 ─ Model
 ↓
M0 ─ Instances


---

50. M0 — Instance Level

This is where actual objects/instances exist.

Example:

Francis : Student
Grace : Student
John : Student

These are individual instances.

Think:

> M0 = actual data/instances




---

51. M1 — Model Level

This is the model we create for our system.

For example:

┌───────────────┐
│    Student    │
├───────────────┤
│ studentID     │
│ name          │
└───────────────┘

This says what a Student should look like in our model.

Think:

> M1 = our system model




---

52. M2 — Metamodel Level

Now we ask:

> What is a Class?



> What is an Attribute?



> What is an Association?



These are concepts in the UML metamodel.

For example:

Class
Attribute
Operation
Association
Generalization

Think:

> M2 = concepts used to construct UML models



The OMG UML specification provides a machine-readable UML abstract syntax metamodel in addition to the formal specification document. 


---

53. M3 — Meta-Metamodel

At the highest level we need a language/framework for describing metamodels.

This is associated with the Meta Object Facility (MOF).

Think:

> M3 = foundation used to define metamodels



Therefore:

M3
↓
defines metamodel concepts

M2
↓
defines UML modelling concepts

M1
↓
defines our university system

M0
↓
contains actual instances


---

54. A Very Simple Analogy

Imagine teaching a language.

M3

Rules for creating languages.

M2

The grammar/vocabulary definitions.

M1

A sentence written using the language.

M0

The real-world things that the sentence refers to.

The analogy is not a formal definition, but it helps beginners understand the hierarchy.


---

55. Why Students Find M0–M3 Difficult

Because students often see:

Student

and ask:

> "Is that M0, M1 or M2?"



The answer depends on what Student represents in the particular context.

For example:

Student : Class

could be a class in an M1 university model.

But:

Class

as a UML modelling concept belongs to the UML metamodel level.

So the same word may refer to different levels depending on context.


---

56. A Complete M0–M3 Example

Let's model a university.

M3

MOF / meta-metamodelling foundation

M2

UML Class
UML Property
UML Association
UML Operation

M1

Student
Course
Registration

M0

Francis : Student
BICT3202 : Course
REG001 : Registration

Diagram:

┌─────────────────────────────┐
│ M3                          │
│ Meta-metamodel foundation   │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│ M2                          │
│ UML Class, Property, etc.   │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│ M1                          │
│ Student, Course,            │
│ Registration                │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│ M0                          │
│ Francis, BICT3202, REG001   │
└─────────────────────────────┘


---

57. Important Distinction: UML Architecture vs Software Architecture

This is a likely examination trap.

UML architecture

M3
M2
M1
M0

This concerns levels of modelling and metamodeling.

Software architecture

For example:

Presentation Layer
       ↓
Business Logic Layer
       ↓
Data Access Layer
       ↓
Database

This concerns how software is organized.

They are not the same thing.


---

58. UML Model vs UML Diagram

Another important distinction.

UML model

The underlying collection of model elements and relationships.

UML diagram

A visual representation/view of selected model elements.

Think:

MODEL
  |
  ├── Class Diagram
  ├── Sequence Diagram
  ├── Activity Diagram
  └── State Diagram

One model can support multiple views.

This is one reason UML is useful for complex systems.


---

59. Example: One System, Multiple Views

Consider an online banking system.

Class view

Customer
Account
Transaction
Bank

Use case view

Customer
  |
  ├── Withdraw Money
  ├── Deposit Money
  └── Transfer Money

Sequence view

Customer
   ↓
ATM
   ↓
Bank Server
   ↓
Database

Activity view

Insert Card
    ↓
Enter PIN
    ↓
Select Transaction
    ↓
Enter Amount
    ↓
Validate
    ↓
Complete

State view

Account
  ↓
Active
  ↓
Blocked
  ↓
Closed

These are not necessarily five separate systems.

They are different views of the same system.


---

60. UML as a Communication Tool

Suppose a client tells the analyst:

> "Students should be able to register for courses."



The analyst creates:

(Student) ─── (Register Course)

The developer can ask:

> "What happens if the course is full?"



The analyst updates the model.

Then another question:

> "What if the student has not passed the prerequisite?"



Another rule is added.

This demonstrates an important purpose of modelling:

> A UML model provides something stakeholders can discuss before expensive implementation begins.




---

61. UML and Abstraction

Remember abstraction from Week 2.

Suppose the real university has:

10,000 students;

500 courses;

300 lecturers;

50 departments;

millions of database records.


We don't draw all 10,000 students in a class diagram.

Instead, we abstract:

Student
Course
Lecturer
Department

This gives us a manageable representation.

Therefore:

> UML is closely connected to abstraction.




---

62. UML and Complexity Management

A good model reduces unnecessary complexity.

Imagine:

Student
Course
Lecturer
Department
Payment
Invoice
Exam
Result
Library
Book
Borrowing
Accommodation
Room
...

Trying to place all of these into one diagram could produce a huge, unreadable model.

Instead:

Student Management Package
Finance Package
Examination Package
Library Package
Accommodation Package

We divide complexity into manageable pieces.


---

63. Practical Session — UML Modelling Exercise

System: University Course Registration

Students will build a small model.

Step 1 — Identify classes

Start with:

Student
Course
Lecturer
Registration


---

Step 2 — Identify attributes

Student

studentID
name
programme
year

Course

courseCode
courseName
creditHours

Lecturer

lecturerID
name
department

Registration

registrationID
date
status


---

Step 3 — Identify operations

Student:

registerCourse()
dropCourse()
viewResults()

Lecturer:

assignGrade()
viewClassList()


---

Step 4 — Add relationships

Student ───── Registration
Registration ───── Course
Lecturer ───── Course


---

Step 5 — Add multiplicity

For example:

Student 1 ───── 0..* Registration

and:

Course 1 ───── 0..* Registration


---

Step 6 — Identify possible constraints

For example:

{prerequisiteSatisfied = true}


---

Step 7 — Add a stereotype where appropriate

For example:

«entity»
Student


---

64. Practical Exercise 2 — Identify the Relationship

Give students the following statements.

A

> A Student is a type of User.



Answer:

Generalization

Student ─────▷ User


---

B

> A Registration uses information from Course.



Answer:

Dependency, if the relationship is genuinely usage/dependency rather than a structural association.


---

C

> A Student registers for a Course.



Answer:

Association.


---

D

> MobilePayment implements PaymentService.



Answer:

Realization.


---

65. Tutorial Exercise — Find the Mistake

Give students:

Student
                    △
                    |
                    |
                  User

Ask:

> Is this correct if Student is a specialized type of User?



No.

The generalization arrow should point toward the general class:

User
                  △
                  |
               Student

This is a very common beginner mistake.


---

66. Another Common Mistake

Students may draw:

Student ◇──────── Course

and say:

> "The diamond means they are connected."



That is not enough.

The diamond has a specific UML meaning associated with aggregation/composition notation.

Students should never choose UML symbols based on appearance alone.


---

67. Another Common Mistake: Everything Becomes a Class

A beginner may produce:

Student
Name
StudentID
Course
CourseName
Registration
RegistrationDate

and make every noun a class.

But OOAD requires analysis.

For example:

> "University"



does not automatically need to become a class in every model.

Ask:

Does it have important attributes?

Does it have behaviour?

Does it participate in relationships?

Does the system need to store/manage it?

Is it relevant to the current problem?


This is why object identification is an analysis activity, not simply a grammar exercise.


---

68. Another Common Mistake: Overloading the Diagram

A student may create:

Student
Course
Lecturer
Department
Faculty
University
Payment
Bank
MobileMoney
Library
Book
Hostel
Room
Food
Transport
...

all in one diagram.

The diagram becomes difficult to understand.

A better approach is:

Student Management Model

and separate related areas into packages/models where appropriate.


---

69. Case Study for Week 4

MRTC University E-Learning System

Imagine a university wants an online learning platform.

Students can:

log in;

view courses;

download notes;

submit assignments;

view grades.


Lecturers can:

upload notes;

create assignments;

mark assignments;

publish grades.



---

Question 1

Identify possible classes.

Suggested:

Student
Lecturer
Course
Assignment
Submission
Grade
LearningMaterial


---

Question 2

Identify possible relationships.

Student ───── Submission
Student ───── Course
Lecturer ───── Course
Course ───── Assignment
Assignment ───── Submission


---

Question 3

What behaviour needs modelling?

Examples:

Submit Assignment
Mark Assignment
Publish Grade


---

Question 4

What state changes might exist?

For a submission:

Draft
  ↓
Submitted
  ↓
Marked
  ↓
Returned


---

70. Independent Learning — 10 Hours

Students should divide their independent study approximately as follows.

2 hours — Reading

Read the relevant UML sections of the official UML 2.5.1 specification.

The OMG specification itself explains that it is a reference specification, intended to be read non-sequentially, with sections covering abstract syntax, semantics, notation and examples. 

[OMG UML 2.5.1 Specification](https://www.omg.org/spec/UML/2.5.1/PDF?utm_source=chatgpt.com)

3 hours — Diagram practice

Create:

2 class diagrams;

2 use-case diagrams;

1 activity diagram;

1 sequence diagram.


2 hours — Relationship practice

Practice:

association;

dependency;

generalization;

realization.


2 hours — Case study

Model a small:

> University Library Management System



1 hour — Revision

Answer the examination questions below without looking at the notes.


---

71. Week 4 Tutorial Questions

Question 1

Define a UML building block.

Question 2

Explain four categories of UML things.

Question 3

Differentiate between:

class and object;

association and dependency;

generalization and realization.


Question 4

Explain syntax and semantics.

Question 5

What is a UML stereotype?

Question 6

What is a tagged value?

Question 7

What is a constraint?

Question 8

Explain the purpose of a UML profile.

Question 9

Explain:

M3
M2
M1
M0

Question 10

Why should one system be represented using multiple UML diagrams?


---

72. Examination Questions

Question 1 — Short Essay

Explain the major building blocks of UML and provide an example of each.


---

Question 2 — Comparison

Differentiate between association, dependency, generalization and realization. Use diagrams in your answer.


---

Question 3 — Application

A university has:

Students;

Lecturers;

Courses;

Departments.


Students register for courses and lecturers teach courses.

Required:

Draw a UML class diagram showing:

classes;

attributes;

relationships;

multiplicities.



---

Question 4 — Extensibility

Explain:

1. stereotype;


2. tagged value;


3. constraint;


4. UML profile.



Give a practical example for each.


---

Question 5 — Architecture

Explain the four levels of UML architecture:

M3
M2
M1
M0

Use a university registration system as your example.


---

73. Week 4 Key Terms

Students should be able to explain these without memorizing blindly:

Term	Meaning

UML	Unified Modeling Language
Class	Description of a type of object
Object	Instance of a class
Interface	Contract defining available operations
Component	Modular system element
Node	Computational/execution resource
Association	Structural relationship
Dependency	Usage/dependency relationship
Generalization	General-to-specific relationship
Realization	Implementation of a contract
Activity	Workflow/behaviour
Interaction	Communication among elements
State	Condition/status of an object
Package	Grouping mechanism
Note	Annotation
Stereotype	Specialized UML meaning
Tagged value	Additional metadata/property
Constraint	Condition/rule
Profile	UML customization mechanism
Syntax	Form/notation
Semantics	Meaning
M3	Meta-metamodel level
M2	Metamodel level
M1	Model level
M0	Instance level



---

74. Week 4 Summary

Let's connect everything.

UML building blocks

UML
                     |
          ┌──────────┼──────────┐
          ↓          ↓          ↓
        Things   Relationships Diagrams

Things

Structural
Behavioural
Grouping
Annotational

Relationships

Association
Dependency
Generalization
Realization

Mechanisms

Specifications
Adornments
Common divisions
Extensibility

Extensibility

Stereotypes
Tagged Values
Constraints
Profiles

Architecture

M3 → Meta-metamodel
 ↓
M2 → Metamodel
 ↓
M1 → Model
 ↓
M0 → Instances


---

75. The Big Picture: Weeks 1–4

At this point, students should see the progression of the module.

WEEK 1
BUSINESS NEEDS
     ↓
Why does the organization need the system?

WEEK 2
OBJECT-ORIENTED THINKING
     ↓
What objects/classes exist?
What do they know?
What can they do?
How are they related?

WEEK 3
INTRODUCTION TO UML
     ↓
How can we communicate these models?

WEEK 4
UML FOUNDATIONS
     ↓
What are UML's elements?
What do the symbols mean?
What are the rules?
How can UML be extended?
How is UML organized?

WEEK 5
OBJECT-ORIENTED ANALYSIS
     ↓
Now we begin building formal object/class models.

That final transition is important.

Week 4 is the bridge between understanding UML conceptually and actually using UML to perform Object-Oriented Analysis.

From Week 5 onward, students will increasingly move from "What is this UML symbol?" to "Given a real system, how do I decide what to model and how do I model it correctly?"


---

References and Further Reading

Primary authoritative reference

Object Management Group (OMG). (2017). Unified Modeling Language (UML), Version 2.5.1. OMG. UML 2.5.1 remains the formal version listed by OMG, with the specification adopted in December 2017. 

[OMG — UML Specification 2.5.1](https://www.omg.org/spec/UML/2.5.1/?utm_source=chatgpt.com)

Additional authoritative material

Object Management Group. Unified Modeling Language 2.5.1 — Formal Specification. The specification explicitly organizes UML concepts into formal abstract syntax, semantics, notation and examples, making it especially useful when students need to distinguish "what a symbol looks like" from "what it actually means." 

Object Management Group. UML 2.5.1 Abstract Syntax Metamodel. The OMG UML page provides the normative machine-readable abstract syntax metamodel, alongside the UML standard profile and diagram interchange metamodel. 

Prescribed texts from the Exploits University outline

Mach, E. (2019). Object Oriented Analysis & Design Cookbook: Introduction to Practical System Modeling.

Reddy, V., & Korra, S. (2018). Object-Oriented Analysis and Design Using UML.

The Art of Service. (2021). Object Oriented Analysis and Design: A Complete Guide.


Recommended texts

Wixom, B., & Dennis, A. (2018). Systems Analysis and Design.

Blokdyk, G. (2021). Object-Oriented Analysis and Design Standard Requirements.

Wixom, B., & Dennis, A. (2020). Systems Analysis and Design: An Object-Oriented Approach with UML.
