BICT 3202 — Object-Oriented Analysis and Design

WEEK 5: OBJECT-ORIENTED ANALYSIS — OBJECT MODELLING I

Programme: BSc in Information Communication and Technology
Year: 3
Course Code: BICT 3202
Week: 5 of 16
Module: Object-Oriented Analysis and Design
Lecture: 2 hours
Tutorial: 1 hour
Practical: 1 hour
Independent Learning: 10 hours


---

1. Introduction to Week 5

So far, we have built the foundation:

Week 1: Business needs and business software needs

Week 2: Object-oriented technology and principles

Week 3: Introduction to UML

Week 4: UML building blocks, rules, mechanisms and architecture


Now we begin the actual Object-Oriented Analysis (OOA) process.

This is an important transition.

Students should now move from:

> "I know what a UML class diagram is."



to:

> "Given a real-world problem, I can identify objects/classes and represent their relationships correctly."



The course outline divides Object-Oriented Analysis/Object Modelling into two parts.

Week 5 — Object Modelling I

Object/Class

Notation

Links and Association

Generalisation/Specialisation

CASE Tool


Week 6 — Object Modelling II

Aggregation

Inheritance

Polymorphism

Grouping


Therefore, Week 5 is primarily about learning how to identify and represent classes/objects and their basic relationships before moving into more advanced object modelling in Week 6.


---

2. Week 5 Learning Outcomes

By the end of this week, students should be able to:

1. Explain object-oriented analysis.


2. Explain the difference between an object and a class.


3. Identify candidate objects/classes from a problem description.


4. Distinguish relevant objects from irrelevant nouns.


5. Identify attributes of objects.


6. Identify operations/responsibilities of objects.


7. Draw a UML class using correct notation.


8. Draw an object diagram.


9. Explain links between objects.


10. Explain associations between classes.


11. Identify association names and roles.


12. Explain multiplicity.


13. Use multiplicity correctly in a class diagram.


14. Explain generalization.


15. Explain specialization.


16. Draw a generalization relationship.


17. Distinguish generalization from ordinary association.


18. Apply object modelling to a real-world system.


19. Use a CASE/UML modelling tool to create a basic class diagram.


20. Critically evaluate whether a proposed object model makes sense.




---

3. What Is Object-Oriented Analysis?

Let's begin with the word analysis.

Analysis means studying a problem to understand:

what exists;

what users need;

what activities occur;

what information is involved;

what rules apply;

how different parts relate to one another.


In Object-Oriented Analysis, we examine the problem domain in terms of:

> objects, classes, responsibilities, relationships and behaviour.



For example, suppose a university wants a student registration system.

A traditional analysis might begin with:

Input → Process → Output

Object-oriented analysis instead asks:

Who/what are the important objects?

Student
Course
Registration
Lecturer
Programme

Then:

> How are these objects related?



Student ─── Registration ─── Course
                    |
                    |
                 Semester


---

4. The Key Question in Object Modelling

Whenever students receive a case study, teach them to ask:

> "What important things exist in this problem domain?"



For a banking system:

Customer
Account
Transaction
Bank
Loan
Card

For a hospital:

Patient
Doctor
Nurse
Appointment
Prescription
MedicalRecord

For an online university:

Student
Lecturer
Course
Assignment
Submission
Grade

These become candidate classes.

But be careful:

> Not every noun in a problem description should automatically become a class.



That is one of the most important lessons in object-oriented analysis.


---

5. Object vs Class

This distinction must be completely clear.

Class

A class is a description or specification of a group/type of objects that share common characteristics and behaviour.

Example:

Student

It describes what students generally have and can do.

Object

An object is an individual instance of a class.

For example:

Francis : Student

Here:

Student = class

Francis = object



---

6. Real-World Analogy

Think about cars.

Car

is a general concept/class.

Individual cars might be:

Toyota Corolla ABC123
Honda Civic DEF456
Mazda Demio GHI789

So:

CLASS
              Car
               |
       ┌───────┼────────┐
       ↓       ↓        ↓
     Object  Object   Object
     Car 1   Car 2    Car 3

The class describes common characteristics.

Each object has its own values.


---

7. Class and Object Example

Consider:

Student

The class could have:

studentID
name
programme
yearOfStudy

An actual object could be:

student001 : Student

with values:

studentID = "ST001"
name = "John Banda"
programme = "BSc ICT"
yearOfStudy = 3

Another object:

student002 : Student

could contain:

studentID = "ST002"
name = "Mary Phiri"
programme = "BSc ICT"
yearOfStudy = 2

Both objects belong to the same class.


---

8. UML Class Notation

The standard UML class notation is generally represented by a rectangle divided into compartments.

A basic class:

┌─────────────────────────┐
│        Student          │
├─────────────────────────┤
│                         │
├─────────────────────────┤
│                         │
└─────────────────────────┘

The three compartments are commonly used for:

1. Class name


2. Attributes


3. Operations



For example:

┌─────────────────────────────┐
│          Student            │
├─────────────────────────────┤
│ - studentID : String        │
│ - name : String             │
│ - programme : String        │
│ - year : Integer            │
├─────────────────────────────┤
│ + registerCourse()          │
│ + viewResults()             │
└─────────────────────────────┘


---

9. Class Name

The first compartment contains the class name:

Student

Good class names normally represent meaningful concepts in the problem domain.

Examples:

Student
Course
Account
Payment
Employee
Product
Order

Poor examples include:

Thing
Data
Information
Stuff
Object1
ClassA

A class name should communicate meaning.


---

10. Attributes

An attribute describes a property or characteristic of an object.

For Student:

studentID
name
programme
yearOfStudy

For Course:

courseCode
courseName
creditHours

For Account:

accountNumber
accountType
balance


---

11. Attribute Notation

A common UML form is:

visibility name : type

For example:

- studentID : String
- name : String
- yearOfStudy : Integer

The notation tells us:

- studentID : String

means:

- = visibility

studentID = attribute name

String = data type



---

12. Operations

An operation represents behaviour/responsibility associated with a class.

For example:

Student
-------------------
registerCourse()
dropCourse()
viewResults()

A BankAccount might have:

deposit()
withdraw()
checkBalance()

A Course might have:

addStudent()
removeStudent()
assignLecturer()

The exact operation names should come from the requirements and responsibilities discovered during analysis.


---

13. Attributes vs Operations

Students commonly confuse these.

Attribute

Describes what the object has/knows.

Example:

Student
name
studentID
programme

Operation

Describes what the object can do.

Example:

Student
registerCourse()
viewResults()

Easy memory trick:

> Attributes = information



> Operations = behaviour




---

14. Object Notation

An object is commonly shown as a rectangle with its name underlined.

For example:

┌─────────────────────┐
│ Francis : Student   │
├─────────────────────┤
│ studentID = ST001   │
│ name = Francis      │
│ year = 3            │
└─────────────────────┘

The key distinction is that a class describes possible structure, while an object shows a specific instance and its values.


---

15. Object Modelling Process

A simple beginner-friendly process is:

Problem Description
       ↓
Identify Candidate Objects
       ↓
Identify Candidate Classes
       ↓
Identify Attributes
       ↓
Identify Responsibilities/Operations
       ↓
Identify Relationships
       ↓
Validate Model
       ↓
Draw UML Class Diagram

Do not teach students to simply underline every noun and call it a class.

That is too simplistic.


---

16. Identifying Candidate Classes

Consider this sentence:

> "A student registers for a course. The course is taught by a lecturer."



Potential nouns:

student
course
lecturer

These are strong candidate classes:

Student
Course
Lecturer

Now consider:

> "A student registers for a course on Monday."



Possible nouns:

student
course
Monday

Should Monday automatically become a class?

No.

It is more likely an attribute/value associated with a date or registration.


---

17. The Noun Technique — With a Warning

One useful starting technique is:

> Look for important nouns in the problem description.



Example:

> "A customer places an order. The order contains products."



Candidate nouns:

Customer
Order
Product

Candidate relationships:

Customer → Order
Order → Product

But noun identification is only a starting point.

Students must still ask:

Is this concept relevant?

Does the system need to store it?

Does it have meaningful properties?

Does it participate in relationships?

Does it have behaviour/responsibility?



---

18. Identifying Attributes

Suppose the requirement says:

> "Each student has a student ID, name, programme and year of study."



Then:

Student
-----------------------
studentID
name
programme
yearOfStudy

The words describing Student become candidate attributes.


---

19. Identifying Operations

Now suppose the requirement says:

> "Students can register for courses, drop courses and view their results."



Then:

Student
-----------------------
+ registerCourse()
+ dropCourse()
+ viewResults()

These are candidate operations.

But again, do not automatically put every action into the Student class.

You need to consider responsibility allocation, which we will develop further as the module progresses.


---

20. Links

Now we move to an important Week 5 concept:

Links

A link represents a connection between particular objects.

Suppose we have:

Francis : Student
BICT3202 : Course

and Francis is registered for BICT3202.

We could represent the connection:

Francis : Student ───────── BICT3202 : Course

This is a link between object instances.


---

21. Association

An association describes a relationship between classes.

For example:

Student ───────── Course

This means instances of Student can be related to instances of Course.

Think of the distinction:

CLASS LEVEL
Student ───────── Course
     Association

OBJECT LEVEL
Francis ───────── BICT3202
       Link

This distinction is extremely important.


---

22. Link vs Association

Concept	Level	Example

Association	Class	Student — Course
Link	Object	Francis — BICT3202


Easy way to remember:

> Association connects classes.



> Link connects objects.




---

23. Naming an Association

An association can be given a meaningful name.

Instead of:

Student ───────── Course

we can write:

Student ─── registers for ─── Course

Another example:

Lecturer ─── teaches ─── Course

Another:

Customer ─── places ─── Order

The name helps people understand the meaning of the relationship.


---

24. Association Roles

An association can also indicate the role that an object/class plays.

For example:

Student ───────── Course
         registers for

At the Course side, the role could be:

registeredCourse

At the Student side:

student

Roles are particularly useful when a relationship needs clarification.


---

25. Multiplicity

This is one of the most important topics in class diagrams.

Multiplicity tells us how many instances can participate in a relationship.

For example:

Student 1 ───────── 0..* Course

This can mean:

> One Student can be associated with zero or many Courses.




---

26. Common Multiplicities

Notation	Meaning

1	Exactly one
0..1	Zero or one
*	Many
0..*	Zero or many
1..*	One or many
2..5	Between two and five


Students should not memorize these without understanding them.


---

27. Understanding 0..*

Suppose:

Student 1 ───── 0..* Course

Read it carefully.

At the Course end:

0..*

means a Student can have:

> zero, one, two, three, or any number of Courses.



Why zero?

Because a newly admitted student may not yet have registered for any course.


---

28. Understanding 1..*

Suppose:

Department 1 ───── 1..* Lecturer

This could mean:

> A Department must have at least one Lecturer and can have many Lecturers.



The difference is:

0..*

allows zero.

1..*

requires at least one.


---

29. One-to-One Relationship

Example:

> Each student has one university student ID card, and each ID card belongs to one student.



Conceptually:

Student 1 ───────── 1 IDCard

This is a one-to-one relationship.


---

30. One-to-Many Relationship

Example:

> One lecturer teaches many courses.



Lecturer 1 ───────── 0..* Course

This is one-to-many.

One lecturer can teach many courses.


---

31. Many-to-Many Relationship

Example:

> A student can register for many courses, and a course can have many students.



Conceptually:

Student 0..* ───────── 0..* Course

This is many-to-many.

However, this relationship often leads us to an important modelling question:

> Does the relationship itself have information?



If registration has:

registrationDate
semester
status
grade

then we may introduce:

Student
    |
Registration
    |
Course

This is something students will revisit in greater depth when we discuss more advanced object modelling.


---

32. Example: University Registration Model

Let's construct one step by step.

Requirement

> "A student can register for many courses. A course can have many students. Each course is taught by a lecturer."



Candidate classes:

Student
Course
Lecturer
Registration

Potential model:

Student
    |
    | registers through
    |
Registration
    |
    | for
    |
Course
    |
    | taught by
    |
Lecturer

This is already much more informative than simply drawing four unrelated boxes.


---

33. Generalization

Now we move to the next major Week 5 topic.

Generalization represents a relationship between a more general class and a more specific class.

For example:

User
                  △
                  |
        ┌─────────┴─────────┐
        ↓                   ↓
     Student             Lecturer

Here:

User

is the general class.

Student
Lecturer

are specialized classes.


---

34. Generalization in Plain English

We can read:

Student ─────▷ User

as:

> A Student is a User.



And:

Lecturer ─────▷ User

as:

> A Lecturer is a User.



This is often called an "is-a" relationship.


---

35. Generalization vs Association

This distinction is extremely important.

Generalization

Student ─────▷ User

means:

> Student is a User.



Association

Student ───── Course

means:

> Student is related to Course.



Do not confuse these.


---

36. Everyday Example

Consider:

Vehicle
                    △
                    |
          ┌─────────┴─────────┐
          ↓                   ↓
        Car               Motorcycle

Read it:

> A Car is a Vehicle.



> A Motorcycle is a Vehicle.



But:

Car ───────── Driver

is not generalization.

A car is not a driver.

It is a relationship between two different concepts.


---

37. Generalization and Shared Features

Suppose:

User

has:

userID
name
email
login()
logout()

Both Student and Lecturer may need these.

Instead of duplicating:

Student
userID
name
email
login()
logout()

Lecturer
userID
name
email
login()
logout()

we can place common features in:

User

and specialize:

Student
programme
yearOfStudy

Lecturer
department
academicRank

Conceptually:

User
                  △
                  |
       ┌──────────┴──────────┐
       ↓                     ↓
    Student               Lecturer

This supports reuse and reduces unnecessary duplication.


---

38. Generalization Vocabulary

Students should know these terms:

General class

Also called the:

parent;

superclass;

generalized class.


Example:

User

Specialized class

Also called:

child;

subclass;

derived class.


Example:

Student


---

39. Specialization

Specialization is the process of creating more specific concepts from a general concept.

Start with:

Employee

Then:

Employee
   ↓
Lecturer
Administrator
Technician

We have specialized the general Employee concept.


---

40. Generalization and Specialization Are Opposite Perspectives

Suppose:

Vehicle
  ↑
 Car

From the bottom upward:

> Car is generalized into Vehicle.



From the top downward:

> Vehicle is specialized into Car.



The structure is the same; the viewpoint differs.


---

41. Generalization Example: University

Consider:

UniversityUser
                       △
                       |
          ┌────────────┼────────────┐
          ↓            ↓            ↓
       Student       Lecturer      Admin

The general class contains common features.

Specialized classes contain their own additional characteristics.


---

42. When Should We Use Generalization?

Ask:

> Is the relationship genuinely an "is-a" relationship?



For example:

Dog is an Animal.

Yes.

Student is a User.

Potentially yes.

Car is a Driver.

No.

Student is a Course.

No.

Student is related to Course.

Yes — association.


---

43. The "Is-A" Test

This is a very useful beginner technique.

Take:

Student → User

Ask:

> "Is a Student a User?"



Yes.

So generalization may be appropriate.

Now:

Student → Course

Ask:

> "Is a Student a Course?"



No.

Therefore:

> Don't use generalization.



Instead:

> Use an appropriate association.




---

44. The "Has-A" Test

Another useful conceptual test is:

> Does one thing contain or have another?



For example:

Car has an Engine.

This may lead toward aggregation/composition modelling, which is covered in Week 6.

For now, students should recognize that this is different from:

Car is a Vehicle.

The first is a has-a/whole-part idea.

The second is an is-a/generalization idea.


---

45. A Complete Class Example

Let's construct a university model.

┌─────────────────────────────┐
│            User             │
├─────────────────────────────┤
│ - userID : String           │
│ - name : String             │
│ - email : String            │
├─────────────────────────────┤
│ + login()                   │
│ + logout()                  │
└─────────────────────────────┘
               △
               |
        ┌──────┴───────┐
        ↓              ↓
┌───────────────┐  ┌────────────────┐
│    Student    │  │    Lecturer    │
├───────────────┤  ├────────────────┤
│ programme     │  │ department     │
│ yearOfStudy   │  │ academicRank   │
├───────────────┤  ├────────────────┤
│ register()    │  │ assignGrade()  │
└───────────────┘  └────────────────┘

This diagram communicates:

common features belong to User;

Student and Lecturer are specialized Users;

each has additional attributes/operations.



---

46. Practical Case Study

System: University Library

Consider the following requirement:

> "A university library allows students and lecturers to borrow books. Every library member has a membership number and name. A student has a programme, while a lecturer has a department. A book has a title, ISBN and publication year. A member can borrow several books."




---

Step 1 — Candidate Classes

Identify:

Member
Student
Lecturer
Book
Borrowing


---

Step 2 — Generalization

Student and Lecturer share:

membershipNumber
name

Therefore:

Member
                   △
                   |
          ┌────────┴────────┐
          ↓                 ↓
       Student           Lecturer


---

Step 3 — Attributes

Member

membershipNumber
name

Student

programme

Lecturer

department

Book

ISBN
title
publicationYear


---

Step 4 — Relationship

A Member borrows a Book.

Member ───── borrows ───── Book

Multiplicity might be:

Member 0..* ───────── 0..* Book

depending on the business rules.


---

47. Important Modelling Question

Suppose the university says:

> "A member can borrow a maximum of five books at one time."



Can we represent this simply using:

0..*

?

Not completely.

0..* means unlimited in the multiplicity notation.

The business rule is:

0..5

if the model is expressing the number of books that can be borrowed concurrently.

This demonstrates why understanding requirements is important.


---

48. CASE Tools

The course outline requires:

> CASE Tool: Select Enterprise Demonstration



CASE means:

> Computer-Aided Software Engineering.



A CASE tool can support activities such as:

modelling;

diagram creation;

documentation;

requirements management;

design;

code-related workflows.


For UML, a modelling tool allows students to create classes and relationships graphically rather than drawing everything manually.


---

49. Examples of UML/Modelling Tools

Examples include:

Enterprise Architect

Visual Paradigm

StarUML

PlantUML

diagrams.net/draw.io

Modelio


For the Week 5 practical, the lecturer can demonstrate Enterprise Architect if that is the selected CASE tool.

The important point is not the brand of the tool.

Students need to understand:

> A CASE tool assists modelling; it does not replace analysis.




---

50. CASE Tool Does Not Think for the Analyst

Suppose the software asks:

> "Create a class."



The tool can create:

┌───────────────┐
│    Student    │
└───────────────┘

But the tool does not know whether:

Student

should actually be a class.

That decision comes from:

requirements;

domain knowledge;

analysis;

business rules.


Therefore:

> The analyst makes modelling decisions. The CASE tool helps represent and manage those decisions.




---

51. Practical Lab — Create Your First Class Diagram

Students should use the selected UML CASE tool.

Task

Create the following classes:

Student
Course
Lecturer
Registration

Student

Attributes:

studentID : String
name : String
programme : String
yearOfStudy : Integer

Operations:

registerCourse()
dropCourse()
viewResults()


---

Course

Attributes:

courseCode : String
courseName : String
creditHours : Integer

Operations:

addStudent()
removeStudent()


---

Lecturer

Attributes:

lecturerID : String
name : String
department : String

Operations:

assignGrade()
viewClassList()


---

Registration

Attributes:

registrationID : String
registrationDate : Date
status : String

Operations:

confirm()
cancel()


---

52. Add Associations

Create:

Student ───── Registration
Registration ───── Course
Lecturer ───── Course

Name the relationships:

Student ─── makes ─── Registration

Registration ─── is for ─── Course

Lecturer ─── teaches ─── Course


---

53. Add Multiplicities

Students should make reasonable assumptions and document them.

For example:

Student 1 ───── 0..* Registration

and:

Course 1 ───── 0..* Registration

For Lecturer/Course:

Lecturer 1 ───── 0..* Course

However, students should understand that the correct multiplicity ultimately depends on the actual requirements.


---

54. Add Generalization

Now add:

User
                  △
                  |
          ┌───────┴───────┐
          ↓               ↓
       Student          Lecturer

This creates an opportunity to discuss whether the original attributes should remain duplicated or be moved to User.


---

55. Tutorial Activity

Divide the class into groups.

Give each group a different system:

Group A

Banking system.

Group B

Hospital system.

Group C

Library system.

Group D

Online shopping system.

Group E

Hotel management system.

Each group must identify:

1. At least five candidate classes.


2. At least three attributes per major class.


3. At least two operations where appropriate.


4. At least five associations.


5. Appropriate multiplicities.


6. At least one generalization relationship.


7. At least two possible links between actual objects.




---

56. Example: Online Shopping

A possible answer:

Customer
Product
Order
OrderItem
Payment
Delivery

Associations:

Customer ─── places ─── Order

Order ─── contains ─── Product

Order ─── has ─── Payment

Order ─── has ─── Delivery

Potential generalization:

Payment
                    △
                    |
          ┌─────────┴─────────┐
          ↓                   ↓
    MobilePayment        CardPayment

This is only a candidate model; students should justify their decisions.


---

57. Validation of a Class Diagram

After creating a diagram, do not immediately submit it.

Perform a model review.

Ask:

1. Does every class have a purpose?

If not, remove or reconsider it.

2. Does every attribute belong to the correct class?

For example:

studentName

probably belongs to Student.

3. Are operations meaningful?

Don't add random methods simply to fill the box.

4. Are relationships logically correct?

5. Are multiplicities supported by requirements?

6. Are generalizations genuine "is-a" relationships?

7. Is the diagram readable?


---

58. Common Student Mistakes

Mistake 1: Confusing class and object

Wrong conceptual thinking:

> "John is the Student class."



Correct:

Student = class
John : Student = object


---

Mistake 2: Using generalization everywhere

Wrong:

Student ─────▷ Course

A Student is not a Course.


---

Mistake 3: Forgetting multiplicities

Students often draw:

Student ───────── Course

and stop.

But requirements often require us to know:

How many?


---

Mistake 4: Making every noun a class

Not every noun is a class.


---

Mistake 5: Adding operations randomly

Students sometimes write:

Student
----------------
eat()
sleep()
walk()

because students can physically do these things.

But OOAD is about system-relevant responsibilities, not everything a human can do.


---

59. Another Important Issue: Analysis vs Implementation

At this stage, students should not become obsessed with programming syntax.

For example:

public void registerCourse()

is implementation-oriented.

At the analysis level, we may simply model:

registerCourse()

The purpose is to understand the system first.

Implementation details become increasingly important during design.


---

60. Object Modelling Exercise

Scenario

> "A hospital has doctors, nurses and patients. A patient can have multiple appointments. Each appointment is with a doctor. A doctor belongs to a department. A patient has a patient number, name and date of birth."



Task 1

Identify candidate classes.

Suggested:

Patient
Doctor
Nurse
Appointment
Department

Task 2

Identify attributes.

Patient:

patientNumber
name
dateOfBirth

Task 3

Identify relationships.

Patient ─── has ─── Appointment

Appointment ─── with ─── Doctor

Doctor ─── belongs to ─── Department

Task 4

Identify multiplicity.

For example:

Patient 1 ───── 0..* Appointment


---

61. Advanced Discussion: Why "Object Identification" Is Difficult

A real system does not come with labels saying:

THIS IS A CLASS.
THIS IS AN ATTRIBUTE.
THIS IS AN OPERATION.
THIS IS AN ASSOCIATION.

The analyst has to determine these.

For example:

> "The customer places an order."



Could produce:

Customer
Order

But then:

> "The customer uses a shopping cart."



Now:

Customer
ShoppingCart
Order

But should the shopping cart be a class?

Usually, potentially yes, if it has meaningful state and behaviour.

For example:

ShoppingCart
---------------------
items
total
---------------------
addItem()
removeItem()
calculateTotal()

The point is:

> Object modelling requires reasoning, not just drawing.




---

62. Object-Oriented Analysis Is Iterative

Students should not expect to produce the perfect class diagram on the first attempt.

A typical process might look like:

First Model
     ↓
Review Requirements
     ↓
Identify Missing Class
     ↓
Remove Unnecessary Class
     ↓
Correct Relationship
     ↓
Adjust Multiplicity
     ↓
Review Again
     ↓
Improved Model

This iterative approach is normal.


---

63. Week 5 Assessment Activity

Individual Assignment

Scenario

Design the object model for a University Accommodation Management System.

The system should manage:

students;

rooms;

hostels;

accommodation applications;

payments;

wardens.


Students apply for rooms.

A hostel contains several rooms.

A student can occupy one room at a time.

A warden manages a hostel.

Students make accommodation payments.


---

Students Must Produce

Part A — Classes

Identify at least:

Student
Hostel
Room
Application
Payment
Warden

Part B — Attributes

Provide at least three meaningful attributes for each major class.

Part C — Operations

Provide appropriate operations.

Part D — Associations

Show relationships between classes.

Part E — Multiplicity

Show how many objects participate.

Part F — Generalization

Identify whether any generalization is justified.

Part G — Explanation

Write 500–700 words explaining why you chose each major class and relationship.


---

64. Suggested Marking Scheme

Component	Marks

Identification of appropriate classes	15
Attributes	10
Operations	10
Associations	15
Multiplicity	10
Generalization/specialization	10
Correct UML notation	15
Explanation/justification	10
Diagram readability	5
Total	100



---

65. Week 5 Revision Questions

Question 1

What is Object-Oriented Analysis?

Question 2

Define a class.

Question 3

Define an object.

Question 4

Differentiate between an object and a class.

Question 5

What is an attribute?

Question 6

What is an operation?

Question 7

Differentiate between an attribute and an operation.

Question 8

What is a link?

Question 9

What is an association?

Question 10

Differentiate between a link and an association.

Question 11

What is multiplicity?

Question 12

Explain:

0..1
1
0..*
1..*

Question 13

What is generalization?

Question 14

What is specialization?

Question 15

Explain the "is-a" test.

Question 16

Differentiate between association and generalization.

Question 17

What is a CASE tool?

Question 18

Why can a CASE tool not replace an analyst?


---

66. Examination-Style Question

Consider the following scenario:

> A university has students and lecturers. Each student has a student ID, name, programme and year of study. Each lecturer has a staff ID, name and department. Students register for courses. Each course has a course code, title and credit hours. Lecturers teach courses. A student may register for many courses, while each course may have many students.



Required:

a) Identify the candidate classes. [5 marks]

b) Identify appropriate attributes. [10 marks]

c) Identify operations that could reasonably belong to the classes. [5 marks]

d) Draw a UML class diagram showing the associations. [10 marks]

e) Add appropriate multiplicities. [5 marks]

f) Identify whether generalization is appropriate and justify your answer. [5 marks]

Total: 40 marks


---

67. Week 5 Key Terms

Term	Simple meaning

Object	A particular instance
Class	Description of a type of object
Attribute	Property/information held by an object
Operation	Behaviour/responsibility
Link	Connection between object instances
Association	Relationship between classes
Multiplicity	How many instances can participate
Generalization	General-to-specific relationship
Specialization	Creating a more specific class
Superclass	General/parent class
Subclass	Specialized/child class
CASE	Computer-Aided Software Engineering
Object model	Representation of objects/classes and their relationships



---

68. Week 5 — The Big Picture

Students should leave this week understanding this progression:

REAL-WORLD PROBLEM
        ↓
Read requirements
        ↓
Identify important concepts
        ↓
Candidate objects/classes
        ↓
Identify attributes
        ↓
Identify responsibilities/operations
        ↓
Identify links/associations
        ↓
Determine multiplicities
        ↓
Identify genuine generalization
        ↓
Create UML class diagram
        ↓
Validate against requirements

The most important lesson is:

> Object-Oriented Analysis is not primarily about drawing boxes. It is about understanding a problem domain and deciding what objects/classes, properties, behaviours and relationships are necessary to represent that domain.




---

69. Connection to Week 6

Week 5 has given students the foundation for object modelling:

Class
Object
Attribute
Operation
Link
Association
Multiplicity
Generalization
Specialization

Next, Week 6: Object-Oriented Analysis — Object Modelling II will extend this model with:

Aggregation

Inheritance

Polymorphism

Grouping


We will therefore move from:

> "What objects/classes exist and how are they related?"



to more sophisticated questions such as:

> "Is this a whole-part relationship?"



> "What behaviour can be inherited?"



> "Can different objects respond differently to the same operation?"



> "How can related classes be organized into manageable groups?"



That is where the object model begins to become much more powerful.


---

References and Further Reading

Primary UML standard

Object Management Group (OMG). (2017). Unified Modeling Language (UML), Version 2.5.1. OMG. This remains the formal UML 2.5.1 specification and is the most authoritative source for UML notation, semantics, relationships, classes, objects, generalization and other modelling concepts. [OMG UML 2.5.1 Specification](https://www.omg.org/spec/UML/2.5.1/?utm_source=chatgpt.com)

OMG UML Resources

The OMG UML page provides the UML specification together with related machine-readable modelling artifacts, including the UML abstract syntax metamodel. [OMG — Unified Modeling Language](https://www.omg.org/spec/UML/?utm_source=chatgpt.com)

Prescribed texts

Mach, E. (2019). Object Oriented Analysis & Design Cookbook: Introduction to Practical System Modeling.

Reddy, V., & Korra, S. (2018). Object-Oriented Analysis and Design Using UML.

The Art of Service. (2021). Object Oriented Analysis and Design: A Complete Guide.


Recommended texts

Wixom, B., & Dennis, A. (2018). Systems Analysis and Design.

Blokdyk, G. (2021). Object-Oriented Analysis and Design Standard Requirements.

Wixom, B., & Dennis, A. (2020). Systems Analysis and Design: An Object-Oriented Approach with UML.


Teaching note: For this module, the OMG UML specification should be treated as the authoritative source for whether a particular UML notation or relationship has a particular formal meaning, while the prescribed textbooks can be used for pedagogical explanations and worked OOAD examples.
