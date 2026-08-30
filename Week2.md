BICT 3202 — Object-Oriented Analysis and Design

WEEK 2: PRINCIPLES OF OBJECT MODELLING

Programme: BSc in Information Communication and Technology
Year: 3
Course Code: BICT 3202
Week: 2 of 16
Lecture: 2 hours
Tutorial: 1 hour
Practical: 1 hour
Independent Learning: 10 hours


---

1. Week 2 Overview

In Week 1, we established an important foundation:

> Business problem → Business need → Requirements → Understanding the problem domain → Candidate objects



This week moves one step further.

The official course outline identifies the following Week 2 topics:

1. Principles of Object Modelling


2. Definition of an Object Model


3. Identification of Objects in a System


4. Standards for Objects


5. Managing Complexity


6. Modelling



The purpose of this week is to teach students how to think about a system as a collection of meaningful objects and relationships, before we formally introduce the complete UML language in Weeks 3 and 4.

A model is deliberately simpler than the real system. The Object Management Group explains that modelling helps people work at a higher level of abstraction by hiding unnecessary detail and focusing attention on particular aspects of a system. 

This idea is absolutely central to OOAD.


---

2. Learning Outcomes for Week 2

By the end of this week, students should be able to:

1. Explain the meaning of object modelling.


2. Define an object model.


3. Explain why object models are useful in systems analysis.


4. Explain the relationship between an object, class and object model.


5. Identify potential objects in a given problem domain.


6. Distinguish useful objects from irrelevant nouns.


7. Identify attributes and behaviours associated with objects.


8. Identify relationships between objects.


9. Explain object identity.


10. Explain abstraction and encapsulation in relation to modelling.


11. Explain how object models help manage system complexity.


12. Explain the importance of consistency and standards in modelling.


13. Construct a simple conceptual object model from a textual problem description.


14. Evaluate whether a proposed object model adequately represents the business problem.




---

3. What Is Object Modelling?

3.1 Simple Explanation

Imagine that you want to explain a university to somebody who has never seen it.

You could try to describe everything:

every student;

every lecturer;

every classroom;

every chair;

every computer;

every document;

every tree;

every road;

every employee;

every department;

every activity.


That would be overwhelming.

Instead, you create a simplified representation showing only the things relevant to your purpose.

For a student registration system, you might focus on:

Student
Course
Programme
Lecturer
Registration
Department
Payment

That simplified representation is a model.

When we organize the model around objects and their relationships, we are performing object modelling.


---

4. Definition of an Object Model

An object model is a representation of a system or problem domain in terms of objects, their characteristics, behaviour and relationships.

In simple terms:

> An object model is a simplified picture of how important objects in a system exist and relate to one another.



For example:

Student ───── registers for ───── Course

This tells us something important about the university registration domain.

We could expand it:

Student
----------------
studentID
name
programme

       |
       | registers for
       ↓

Course
----------------
courseCode
courseName
credits

The model doesn't describe every detail of the university.

It describes the parts relevant to the particular system being analysed.


---

5. Why Do We Need Object Models?

Suppose a university tells a developer:

> "Build us an online student registration system."



The statement is too broad.

The developer needs to understand:

Who registers?

What is being registered?

Who approves registration?

What courses are available?

What programme does the student belong to?

What happens when a student registers?

What information does registration contain?

Are prerequisites required?

Does payment affect registration?

Who can change registration?


Object modelling helps transform a vague description into a structured representation.


---

6. Object Modelling Is a Form of Simplification

This is a critical concept.

The real world is enormously complicated.

A university contains thousands of people, processes, rules and physical resources.

A software model cannot—and should not—represent every single detail.

Instead:

> We select the details that matter to the system.



This is called abstraction.

OMG explains that models allow developers and analysts to raise the level of abstraction by hiding or masking details and focusing on the important view of a system. 


---

7. Real World → Model → Software

Think about the relationship this way:

REAL WORLD
University
   ↓
We identify important concepts
   ↓
OBJECT MODEL
Student
Course
Lecturer
Registration
Payment
   ↓
DETAILED ANALYSIS
Attributes
Relationships
Behaviour
Rules
   ↓
DESIGN
Classes
Interfaces
Components
Database structures
   ↓
IMPLEMENTATION
Actual software

The model is therefore an intermediate representation between the real-world problem and the eventual software solution.


---

8. Principle 1: Abstraction

8.1 What Is Abstraction?

Abstraction means focusing on the essential characteristics of something while ignoring details that are not relevant to the current purpose.

Consider a car.

A driver cares about:

steering;

speed;

fuel;

brakes;

gear;

accelerator.


The driver usually doesn't need to know:

the exact internal combustion process;

every electrical connection;

the internal implementation of the braking system.


The car hides enormous complexity behind a simpler interface.


---

9. Abstraction in Object Modelling

Suppose we're modelling a university Student Registration System.

A Student has hundreds of real-world characteristics:

height;

weight;

hair colour;

favourite food;

shoe size;

family history;

social media accounts;

hobbies;

academic programme;

student number;

registered courses.


Should we put all of these into our model?

No.

For a registration system, the important attributes may include:

Student
----------------
studentID
name
programme
year
status

The student's shoe size is irrelevant to course registration.

Therefore, abstraction allows us to say:

> "For this particular system, these characteristics matter and those characteristics do not."




---

10. Abstraction Depends on the Purpose of the Model

This is an important university-level point.

The same real-world entity can be modelled differently depending on the system.

Example: Student

For a Student Registration System:

Student
studentID
name
programme
year

For a University Hostel System:

Student
studentID
name
roomNumber
hostel
checkInDate

For a University Medical System:

Student
studentID
name
medicalRecordNumber
allergies
emergencyContact

The person is the same.

The model is different because the purpose is different.


---

11. Principle 2: Encapsulation

11.1 What Is Encapsulation?

Encapsulation means keeping an object's relevant data and operations together while controlling access to its internal state.

Think of a bank account.

BankAccount
--------------------
balance
--------------------
deposit()
withdraw()
checkBalance()

The account owns the information about its balance and provides operations through which the balance is managed.

Instead of allowing every part of the system to manipulate the balance arbitrarily, the object can enforce rules.


---

12. Example of Encapsulation

Suppose:

Account balance = MWK 100,000

A poorly designed system might allow another component to do:

balance = -MWK 500,000

without checking anything.

An encapsulated design might require:

withdraw(500000)

The account can then check:

1. Is the account active?


2. Is the amount valid?


3. Is sufficient money available?


4. Is the transaction allowed?


5. Should the transaction be recorded?



Encapsulation therefore helps protect an object's state.


---

13. Principle 3: Identity

Objects have identity.

Consider two students:

Student A
ID: ST001
Name: Francis

Student B
ID: ST002
Name: Francis

Even if they have the same name, they are different objects.

The identity distinguishes them.

In a software system, identity might be represented using:

Student ID;

Account Number;

Employee ID;

Product ID;

UUID;

Database primary key.



---

14. Identity vs Attributes

This distinction is important.

Suppose:

Student
ID: ST001
Name: Francis
Programme: BSc ICT

The student's:

name;

programme;


are attributes.

The student's:

identity distinguishes that particular student from other students.


Two students could have:

Name = John Banda

but still be different students because their identifiers differ.


---

15. Principle 4: State

The state of an object is the collection of values describing its current condition.

Example:

Student
---------------------
ID = ST001
Name = Francis
Year = 3
Status = Active

The state can change.

Initially:

Status = Applicant

Later:

Status = Active Student

Eventually:

Status = Graduated

Therefore:

> Object state represents what is true about an object at a particular moment.




---

16. Principle 5: Behaviour

An object's behaviour describes what it can do or how it responds to requests.

For example:

Student
-------------------
registerCourse()
dropCourse()
viewResults()
payFees()

A BankAccount might have:

deposit()
withdraw()
transfer()
checkBalance()

A Book might have:

borrow()
returnBook()
reserve()

This gives us a useful formula:

OBJECT
   |
   ├── Identity
   ├── State
   └── Behaviour


---

17. Principle 6: Relationships

Objects rarely exist independently.

They interact with and relate to other objects.

For example:

Student ───── registers for ───── Course

or:

Lecturer ───── teaches ───── Course

or:

Customer ───── owns ───── Account

or:

Customer ───── places ───── Order

Relationships allow us to represent how objects are connected.


---

18. Principle 7: Modularity

Modularity means dividing a large system into manageable parts.

Imagine a university information system:

University Information System
          |
   ┌──────┼─────────┬─────────┐
   ↓      ↓         ↓         ↓
Student  Finance  Exams    Library
Module   Module   Module    Module

Each module can contain related objects.

For example:

Finance
  |
  ├── Invoice
  ├── Payment
  ├── Account
  └── Receipt

Modularity helps developers and analysts manage complexity.


---

19. Principle 8: Hierarchy

Hierarchy means organizing concepts according to levels.

For example:

Person
                   |
          ┌────────┴────────┐
          ↓                 ↓
       Student           Employee
                              |
                    ┌─────────┴─────────┐
                    ↓                   ↓
                Lecturer          Administrator

The general concept is:

Person

More specialized concepts include:

Student and Employee.

Employee can then be specialized into:

Lecturer and Administrator.

This idea will later connect directly to generalization, specialization and inheritance.


---

20. Principle 9: Reuse

Good object models can support reuse.

Suppose we have a general:

Person

with:

name
phone
email

Different parts of a system may use this concept.

Instead of defining the same information repeatedly, the model can organize common characteristics appropriately.

However, students should remember:

> Reuse does not mean "always use inheritance."



Composition, delegation, interfaces, services and other techniques can also support reuse.

This becomes increasingly important when we reach object-oriented design.


---

21. What Is Object Identification?

The next major topic is:

> Identification of Objects in a System



Object identification means determining which entities or concepts in the problem domain should be represented as objects/classes in the system model.

This sounds easy.

It isn't.


---

22. Example: Identifying Objects from a Sentence

Consider this requirement:

> "A student registers for courses. The lecturer teaches the courses, and the finance department records the student's payments."



What objects might we identify?

Potential candidates:

Student
Course
Lecturer
Finance Department
Payment
Registration

But we should not automatically accept every noun.

This is where proper analysis begins.


---

23. The Noun Technique

A traditional starting technique is to examine the problem statement and identify important nouns.

Example:

> "A student registers for a course. A lecturer teaches the course. The student pays fees."



Potential nouns:

student;

course;

lecturer;

fees.


These become candidate concepts.

But:

> Candidate ≠ final object.



This distinction is very important.


---

24. Why Every Noun Should NOT Become a Class

Consider:

> "The student uses a mobile phone to register for a course."



Nouns include:

student;

mobile;

phone;

course.


Should Phone automatically become a class?

Probably not.

If the system is concerned with course registration, the phone may simply be an external device used to access the system.

Similarly:

> "The student registers for a course at the university."



Possible nouns:

student;

course;

university.


But perhaps University is outside the scope if the system models only a particular registration subsystem.

Therefore:

> Object identification requires judgement, not just grammar.




---

25. Candidate Object Classification

When identifying candidate objects, we can classify them.

1. People

Examples:

Student

Lecturer

Customer

Employee

Doctor


2. Physical things

Examples:

Book

Vehicle

ATM

Computer


3. Places

Examples:

Branch

Department

Classroom

Warehouse


4. Events

Examples:

Registration

Payment

Appointment

Transaction


5. Documents

Examples:

Invoice

Receipt

Application

Certificate


6. Conceptual entities

Examples:

Account

Course

Programme

Membership

Policy



---

26. Events Can Be Objects

Students frequently make this mistake:

> "An object must be a person or physical thing."



No.

Consider:

Payment

Payment is an event/transactional concept.

It may have:

paymentID
amount
date
method
status

and behaviour such as:

process()
cancel()
refund()

Therefore, Payment can be a meaningful object/class.


---

27. How to Decide Whether Something Should Be an Object

Ask these questions:

Question 1

Does the concept have information that the system needs to remember?

Question 2

Does it have meaningful behaviour?

Question 3

Does it have a distinct identity?

Question 4

Does it participate in important relationships?

Question 5

Does the business care about it?

Question 6

Does the system need to create, modify, retrieve or track it?

Question 7

Is it within the scope of the system?

If several answers are yes, it is a strong candidate.


---

28. Example: University Registration

Suppose:

> "A student selects a course and submits registration. The lecturer approves the registration."



Potential candidates:

Candidate	Keep?	Reason

Student	Yes	Important business entity
Course	Yes	Important business entity
Registration	Yes	Must be tracked
Lecturer	Yes	Performs approval
Approval	Possibly	Depends on modelling purpose
Chair	No	Not relevant
Building	Probably no	Not relevant
Keyboard	No	Implementation detail
Internet	No	External infrastructure


This demonstrates why object identification requires analysis.


---

29. Object vs Attribute

Another common source of confusion is deciding whether something should be an object or simply an attribute.

Suppose we have:

Student
-----------------
name
phone
email

Should Phone be a class?

Not necessarily.

If the system only needs:

phoneNumber = +265...

then phoneNumber may simply be an attribute.

But if the system needs to manage multiple phone numbers, phone verification, ownership, type and status, then a separate concept may become useful:

Student
     |
     | has
     ↓
Phone
----------------
number
type
verified
status

Therefore, the decision depends on requirements and modelling purpose.


---

30. Object vs Attribute Example

Scenario

A supermarket system records:

Product
---------
productID
name
price
weight

Is price an object?

Usually, no.

It is an attribute.

But consider a more sophisticated financial system where a price has:

currency;

amount;

effective date;

tax;

discount;

price history.


Then a richer model might represent Price as a separate value concept.

The important lesson is:

> Do not mechanically turn every noun into an object. Analyse its significance and behaviour.




---

31. Identifying Attributes

Once candidate objects are identified, ask:

> "What information does the system need to know about this object?"



Example:

Student

studentID
name
dateOfBirth
programme
year
status

Course

courseCode
courseName
creditHours
level
description

Payment

paymentID
amount
date
method
status

These are attributes.


---

32. Identifying Behaviour

Then ask:

> "What does this object do?"



Student

register()
dropCourse()
viewResults()

Course

Potential behaviour might include:

checkAvailability()

Payment

process()
refund()
verify()

The actual behaviour should be derived from the requirements rather than invented randomly.


---

33. Object Responsibility

An important object-modelling question is:

> What responsibility should each object have?



For example, in a banking system:

Should a Customer calculate the interest on an Account?

Probably not.

A better responsibility might belong to:

Account

because Account contains information about:

balance;

account type;

interest rules.


This leads to an important OO design principle:

> Give an object responsibilities that logically belong to it.



We will explore responsibilities much more deeply in later design topics.


---

34. Cohesion — Introduction

Cohesion refers to how closely related the responsibilities of a component or class are.

Imagine:

Student
--------------------
registerCourse()
viewResults()
payFees()
repairComputer()
cookFood()
manageUniversityNetwork()

This is poor cohesion.

Why?

Because the responsibilities are unrelated.

A better Student class might contain:

registerCourse()
dropCourse()
viewResults()
updateProfile()

These are closely related to the Student concept.


---

35. Coupling — Introduction

Coupling refers broadly to the degree of dependency between components/classes.

Imagine:

Student
  ↓
Registration
  ↓
Course
  ↓
Finance
  ↓
Database
  ↓
Notification
  ↓
External API

If every class depends heavily on every other class, changes become difficult.

A well-designed system generally seeks:

> High cohesion + manageable/low coupling



These concepts become particularly important during object-oriented design.


---

36. Managing Complexity

The official syllabus specifically includes:

> Managing Complexity



Why is complexity a problem?

Consider a system with:

10 classes

It may be relatively easy to understand.

Now imagine:

500 classes

and each class has multiple relationships with other classes.

The number of possible interactions can become enormous.

Therefore, OO modelling uses techniques to control complexity.


---

37. Technique 1: Abstraction

Instead of representing every detail:

University

we might focus only on:

Student
Course
Registration

for the particular problem.


---

38. Technique 2: Decomposition

Break a large system into smaller parts.

University System
       |
       ├── Registration
       ├── Finance
       ├── Examination
       ├── Library
       └── Accommodation

Each subsystem can then be analysed separately.


---

39. Technique 3: Hierarchy

Use general and specialized concepts.

Person
  |
  ├── Student
  └── Employee

This avoids repeating common characteristics unnecessarily.


---

40. Technique 4: Encapsulation

Hide unnecessary internal details.

For example:

BankAccount
------------------
deposit()
withdraw()

The rest of the system doesn't necessarily need to know exactly how the bank account calculates its internal balance.


---

41. Technique 5: Modularity

Separate responsibilities into manageable components.

For example:

Authentication Module
Registration Module
Finance Module
Reporting Module

This makes the system easier to understand and maintain.


---

42. Technique 6: Separation of Concerns

Don't put unrelated responsibilities together.

For example, avoid a class like:

UniversitySystem
-------------------------
registerStudent()
calculateSalary()
printInvoice()
repairComputer()
sendSMS()
calculateExamMarks()
manageLibrary()

This becomes a "God object"—one component trying to do everything.

Instead, responsibilities should be distributed appropriately.


---

43. Technique 7: Levels of Abstraction

A complex system can be viewed at multiple levels.

High level

University System

Medium level

Registration
Finance
Examination

Detailed level

Student
Course
Registration
Payment
Invoice
Result

Implementation level

Java classes
Database tables
APIs
Services

This allows different stakeholders to understand the system at the level appropriate to them.


---

44. Modelling Viewpoints

A single model may not be enough to understand a complex system.

For example, we may want to understand:

Structural view

What things exist?

Student
Course
Lecturer

Behavioural view

What happens?

Student registers
Lecturer approves
System records registration

Interaction view

How do objects communicate?

Student → Registration System → Course

Deployment/architectural view

Where do components run?

Mobile App
     ↓
Web/API Server
     ↓
Database

UML supports multiple perspectives of software systems rather than forcing all information into one diagram. OMG describes UML as a language for specifying, visualizing and documenting software/system models, including structure, behaviour and design. 


---

45. Standards for Objects and Modelling

The course outline says:

> Standards for Objects



Students should understand that software modelling should not be based entirely on everyone's personal drawing style.

Standard modelling notation improves communication.

For OOAD, the major standard students will encounter is:

UML — Unified Modeling Language

The Object Management Group maintains the UML specification. The currently published formal UML specification is UML 2.5.1, adopted in December 2017. 

We will study UML extensively in Weeks 3 and 4.


---

46. Why Standards Matter

Imagine three analysts draw a relationship differently:

Analyst A:
Student ---- Course

Analyst B:
Student <--> Course

Analyst C:
Student ===== Course

What do the symbols mean?

If everyone invents their own notation, communication becomes difficult.

A standardized language provides agreed meanings.

UML is specifically intended to provide a standard graphical language for specifying, visualizing and documenting software systems. 


---

47. Standards Do Not Replace Thinking

This is important.

A UML diagram can be perfectly drawn according to the UML specification and still represent a bad system analysis.

For example:

Student ───── owns ───── Toilet

The notation might be syntactically correct.

But the model could be meaningless for a university registration system.

Therefore:

> Correct notation does not guarantee correct analysis.



Good modelling requires:

1. understanding the business;


2. understanding requirements;


3. selecting appropriate concepts;


4. creating meaningful relationships;


5. using correct notation.




---

48. Object Model Example — University Registration

Let's build our first conceptual object model.

Step 1: Identify candidate objects

From the requirements:

Student
Course
Lecturer
Registration
Programme
Payment

Step 2: Identify important attributes

Student
----------------
studentID
name
programme
year

Course
----------------
courseCode
courseName
credits

Registration
----------------
registrationID
date
status

Step 3: Identify relationships

Student ───── Registration
Course  ───── Registration
Lecturer ───── Course
Programme ──── Student

Step 4: Identify behaviour

Student
registerCourse()

Registration
submit()
approve()
cancel()

Payment
process()
refund()

We now have the beginning of an object model.


---

49. A Conceptual Model

A simplified representation could be:

Programme
                     |
                     |
                   Student
                     |
                     |
                Registration
                  /       \
                 /         \
                /           \
            Course         Payment
              |
              |
           Lecturer

This is still a conceptual model.

In Week 3 and Week 4, we will learn how to represent such structures using formal UML notation.


---

50. Worked Example: Mobile Money System

Let's apply the principles to a familiar system.

Suppose we are modelling a mobile money system.

Business domain

A customer can:

deposit money;

withdraw money;

send money;

receive money;

pay bills.


Candidate objects

Customer
Wallet
Transaction
Agent
Merchant
Bill


---

Customer

Identity

customerID

State

name
phoneNumber
status

Behaviour

register()
sendMoney()
receiveMoney()


---

Wallet

Identity

walletID

State

balance
status

Behaviour

deposit()
withdraw()
transfer()


---

Transaction

Identity

transactionID

State

amount
date
type
status

Behaviour

process()
reverse()


---

51. Candidate Objects vs Final Objects

This distinction deserves emphasis.

Suppose our initial analysis identifies:

Customer
Phone
Money
Wallet
Transaction
Agent
Network
SMS

We should not automatically create eight classes.

We investigate each.

Customer

Clearly relevant.

Wallet

Clearly relevant.

Transaction

Clearly relevant.

Phone

Could be relevant, but perhaps phoneNumber is simply an attribute.

Money

Usually represented as an amount/currency value rather than necessarily a business entity.

Network

May be external infrastructure rather than part of the core domain model.

SMS

Could be an external service rather than a domain object.

Thus:

> Object identification is analytical reasoning, not simply noun extraction.




---

52. Traceability from Requirements to Objects

An excellent analyst should be able to answer:

> "Where did this object come from?"



Suppose the requirement says:

> "Students must be able to register courses."



This can lead to:

Requirement
    ↓
Student
    ↓
Course
    ↓
Registration

Another requirement:

> "The system must prevent students from registering for courses whose prerequisites have not been satisfied."



This could lead to:

Course
   |
   └── prerequisite relationship

Therefore, requirements provide evidence for why model elements exist.

Requirements engineering standards emphasize the importance of developing, analysing, documenting and managing requirements throughout the lifecycle. 


---

53. Object Model Quality

A good object model should be:

1. Relevant

It represents concepts important to the problem.

2. Understandable

Another analyst should be able to interpret it.

3. Consistent

The same concept should not have contradictory meanings.

4. Sufficient

Important requirements should be represented.

5. Not unnecessarily detailed

The model should avoid irrelevant information.

6. Traceable

Model elements should be connected to requirements or business concepts.

7. Maintainable

The model should be understandable when requirements change.


---

54. Poor Model vs Good Model

Poor model

UniversitySystem
------------------------
Student
Course
Payment
Library
Hostel
Transport
Payroll
Cafeteria
Security
Maintenance
EverythingElse()

Everything is thrown into one place.

Better model

University
    |
    ├── Academic
    │      ├── Student
    │      ├── Course
    │      └── Registration
    │
    ├── Finance
    │      ├── Payment
    │      └── Invoice
    │
    └── Examination
           ├── Examination
           └── Result

The second approach gives us better separation and makes complexity easier to manage.


---

55. Relationship Between Object Modelling and UML

Students may wonder:

> "If we're already modelling objects, why do we need UML?"



Because:

Object modelling = the conceptual activity

while

UML = a standardized language for expressing the model.

Think about writing.

Concept

You want to explain an idea.

Language

You use English to express the idea.

Similarly:

Object model

You understand the system in terms of objects and relationships.

UML

You use standardized graphical notation to communicate that model.

OMG describes UML as a standard language for visualizing, specifying and documenting software and systems. 


---

56. Week 2 Mini Case Study

Let's work through a complete example.

Problem

A university wants an online library system.

Students should be able to search for books, borrow available books and return them. Librarians should manage books and monitor overdue loans.


---

Step 1 — Business need

The university needs:

> A faster and more reliable way to manage library resources and student borrowing.




---

Step 2 — Candidate objects

From the description:

Student
Book
Librarian
Loan
Library


---

Step 3 — Attributes

Student

studentID
name
programme

Book

ISBN
title
author
availability

Loan

loanID
borrowDate
dueDate
returnDate
status


---

Step 4 — Behaviour

Student

searchBook()
borrowBook()
returnBook()

Librarian

addBook()
removeBook()
updateBook()

Loan

createLoan()
closeLoan()
calculateFine()


---

Step 5 — Relationships

Student ───── makes ───── Loan
Loan ───────── concerns ───────── Book
Librarian ───── manages ───── Book


---

57. But Is "Library" an Object?

This is an excellent analytical question.

Possibly.

But it depends on the system.

If the system manages:

multiple libraries;

library branches;

locations;

opening hours;

library staff;


then Library may be a meaningful entity.

If we're simply modelling a single library's borrowing process, Library may not need to be represented as a separate class.

Again:

> Scope and purpose determine the model.




---

58. A Useful Object Identification Checklist

When students are given a scenario in an examination, use this process:

Step 1

Read the scenario carefully.

Step 2

Underline important nouns.

Step 3

List candidate objects.

Step 4

Remove irrelevant concepts.

Step 5

Combine duplicate concepts.

Step 6

Identify attributes.

Step 7

Identify behaviours.

Step 8

Identify relationships.

Step 9

Check whether each object has a reason to exist.

Step 10

Check the model against the requirements.


---

59. Practical Session — Week 2

Practical Title

Identifying Objects and Building a Conceptual Object Model

Scenario

A hospital wants an electronic appointment management system.

Patients should be able to request appointments with doctors. Doctors have specialties. Receptionists manage appointments. The system should record appointment dates and statuses.


---

Task 1 — Identify candidate objects

Students should identify at least:

Patient
Doctor
Appointment
Receptionist
Specialty

They should explain why each is relevant.


---

Task 2 — Identify attributes

For example:

Patient

patientID
name
phone

Doctor

doctorID
name
specialty

Appointment

appointmentID
date
time
status


---

Task 3 — Identify behaviours

For example:

Patient

requestAppointment()
cancelAppointment()

Doctor

viewAppointments()

Receptionist

scheduleAppointment()
rescheduleAppointment()


---

Task 4 — Identify relationships

Students should determine relationships such as:

Patient ───── requests ───── Appointment

Doctor ───── attends ───── Appointment

Doctor ───── has ───── Specialty

Receptionist ───── manages ───── Appointment


---

60. Tutorial Activity

Group Exercise: "Is It an Object?"

Give students the following candidates:

Student
Name
Course
Mobile Phone
Payment
Money
University
Registration
Keyboard
Invoice
Lecturer
Internet

Each group must classify each as:

likely object/class;

likely attribute;

external entity/infrastructure;

depends on scope;

probably irrelevant.


Then require students to justify every decision.

This is much better than simply asking students to memorize definitions.


---

61. Tutorial Challenge

Consider the following statement:

> "A customer uses a mobile phone to purchase a product from an online shop. The customer adds the product to a shopping cart and pays using mobile money. The system generates an invoice."



Identify:

Potential objects

Possible attributes

Possible behaviours

Relationships

External systems

Students should specifically consider whether:

Mobile Phone

Mobile Money

Invoice

Shopping Cart


should be represented as objects/classes.

There is no value in accepting answers without justification. The reasoning is the important part.


---

62. Independent Learning — 10 Hours

Activity 1 — Object Identification

Choose one system:

supermarket;

bank;

hospital;

mobile money;

university;

hotel;

library.


Write a one-page description of the system.

Identify:

15 candidate objects;

10 attributes;

10 behaviours;

10 relationships.



---

Activity 2 — Object Filtering

From your 15 candidates, classify them:

Candidate	Keep/Remove	Reason

Student	Keep	Core business entity
Keyboard	Remove	Implementation detail
Registration	Keep	Business transaction
...	...	...


This teaches students that object identification requires judgement.


---

Activity 3 — Complexity Analysis

Choose a large system and identify how abstraction, decomposition, modularity and hierarchy could reduce its complexity.


---

63. Examination-Style Questions

Question 1

Define object modelling and explain its importance in object-oriented analysis.


---

Question 2

Explain five principles of object modelling and illustrate each using a university management system.


---

Question 3

A university wants to develop an online course registration system.

Identify:

a. Ten candidate objects
b. Five attributes for appropriate objects
c. Five behaviours
d. Five relationships
e. Three examples of information that should be excluded through abstraction


---

Question 4

> "Every noun in a requirements document should become an object."



Do you agree?

Explain your answer with examples.

This is an excellent examination question because it tests understanding rather than memorization.


---

Question 5

Explain how the following techniques help manage complexity:

1. abstraction;


2. decomposition;


3. modularity;


4. hierarchy;


5. encapsulation;


6. separation of concerns.




---

64. Week 2 Summary

Let's summarize the most important ideas.

Object modelling

Represents a system/problem domain using objects and their characteristics, behaviour and relationships.

Object

An identifiable entity with state and behaviour.

Class

A specification describing a type of object.

Abstraction

Focus on relevant information while hiding unnecessary detail.

Encapsulation

Keep data and related operations together while controlling access to internal state.

Identity

Allows one object to be distinguished from another.

State

Describes the object's current condition.

Behaviour

Describes what the object can do or how it responds.

Relationship

Describes how objects are connected or interact.

Modularity

Divides a system into manageable parts.

Hierarchy

Organizes concepts from general to specialized.

Object identification

The analytical process of deciding which domain concepts should be represented in the model.

UML

A standardized language used to visualize, specify and document models; the OMG's published UML specification is version 2.5.1. 


---

65. The Most Important Lesson of Week 2

Students should remember this:

> Object modelling is not the process of turning every noun in a paragraph into a class.



Instead:

> Object modelling is the disciplined process of identifying the important concepts in a problem domain, determining their relevant information and behaviour, and representing how they relate to one another.



The analyst therefore moves from:

Problem domain
      ↓
Candidate concepts
      ↓
Relevant objects
      ↓
Attributes
      ↓
Behaviour
      ↓
Relationships
      ↓
Object model

Then, in the next stage, we need a standard language to communicate these models.

That leads directly into Week 3: Modelling Language — An Overview of UML, the Building Blocks of UML, Rules of UML, Mechanisms of UML and the role of UML in OOAD.


---

References

Standards and authoritative sources

International Organization for Standardization. (2018). ISO/IEC/IEEE 29148:2018 — Systems and software engineering — Life cycle processes — Requirements engineering. ISO. The standard covers requirements processes and the information produced during requirements engineering; ISO indicates that the 2018 edition was reviewed and confirmed in 2024 and remains current. 

Object Management Group. (2017). OMG Unified Modeling Language (OMG UML), Version 2.5.1. OMG. The formal UML specification and its machine-readable metamodels are published by OMG. 

Object Management Group. Unified Modeling Language (UML). OMG describes UML as a standard language for visualizing, specifying and documenting software, systems and business processes. 


Prescribed texts from the university syllabus

Mach, E. (2019). Object Oriented Analysis & Design Cookbook: Introduction to Practical System Modeling.

Reddy, V., & Korra, S. (2018). Object-Oriented Analysis and Design Using UML.

The Art of Service. (2021). Object Oriented Analysis and Design: A Complete Guide.


Recommended texts from the university syllabus

Wixom, B., & Dennis, A. (2018). Systems Analysis and Design.

Blokdyk, G. (2021). Object-Oriented Analysis and Design Standard Requirements.

Wixom, B., & Dennis, A. (2020). Systems Analysis and Design: An Object-Oriented Approach with UML.
