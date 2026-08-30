BICT 3202 — Object-Oriented Analysis and Design

WEEK 1: Business Needs, Software Needs and Object Technology for Business

Programme: BSc Information Communication and Technology
Year: 3
Course Code: BICT 3202
Week: 1 of 16
Lecture: 2 hours
Tutorial: 1 hour
Practical: 1 hour
Independent Learning: 10 hours


---

1. Week 1 Overview

Topics from the official course outline

This week covers the first three topics listed under the module's Topics of Study:

1. Business Needs


2. Aspects of Business Software Needs


3. Object Technology for Business



These topics are deliberately placed at the beginning of OOAD. Before students can create classes, objects, use cases or UML diagrams, they must first understand why an organization needs software and what problem the software is supposed to solve.

A common mistake among beginners is to think:

> "Object-Oriented Analysis and Design starts by drawing a class diagram."



It does not.

A good OOAD process starts by understanding the problem, business objectives, stakeholders and requirements. Requirements engineering is concerned with discovering, analysing, documenting, validating and managing what a system needs to accomplish. ISO/IEC/IEEE 29148:2018 provides an internationally recognized framework for requirements engineering and remains the current published edition as of 2026. 

So the logical journey is:

Business problem → Business need → Software need → Requirements → Analysis → Models → Design → Implementation


---

2. Learning Outcomes for Week 1

By the end of this week, students should be able to:

1. Define a business need.


2. Explain why organizations develop or acquire software systems.


3. Distinguish between a business problem, business need, requirement, and software solution.


4. Identify stakeholders associated with a business system.


5. Explain functional and non-functional software needs.


6. Explain the relationship between business objectives and software requirements.


7. Describe the basic idea behind object technology.


8. Explain what an object is in an object-oriented context.


9. Explain the relationship between objects, state and behaviour.


10. Explain why real-world entities can be useful when analysing software systems.


11. Describe major advantages and limitations of object-oriented approaches.


12. Apply these concepts to a simple real-world business case.




---

3. Introduction: Why Do We Need OOAD?

Imagine that a university tells a software developer:

> "We need a new student management system."



The developer immediately starts programming.

They create:

a login page,

a student table,

a lecturer table,

a payment page,

an examination page,

a dashboard.


After six months, the university tests the system and says:

> "This isn't what we asked for."



The developer responds:

> "But you told us to build a student management system."



The university replies:

> "Yes, but students should register courses before paying fees. Lecturers should approve registration. Students should only register for courses offered by their programme. Finance should see outstanding balances. Students should receive notifications. We also need to prevent registration if prerequisites haven't been met."



The developer has a problem.

The problem was not necessarily programming ability.

The problem was insufficient analysis of the business needs before designing the software.

This is one of the fundamental reasons OOAD exists.


---

4. Subtopic 1: Business Needs

4.1 What is a Business Need?

A business need is a problem, opportunity, objective or desired improvement that an organization must address in order to achieve its goals.

In simple language:

> A business need explains why an organization needs to change something.



For example:

A university currently records student registration using paper forms.

Students spend several hours waiting in queues.

The university therefore identifies a need:

> Reduce the time required for student registration and improve the accuracy of registration records.



Notice something important.

The business need is not yet software.

The university has not said:

> "We need a Java application."



It has identified a business problem and desired improvement.


---

4.2 Business Problem vs Business Need

These two concepts are related but not identical.

Business problem

A business problem describes an undesirable current situation.

Business need

A business need describes what the organization needs to achieve or improve in response to that situation.

Example

Business problem:

> Students wait up to three hours to register for courses.



Business need:

> The university needs a faster and more reliable student registration process.



Possible software solution:

> An online student registration system.



The distinction is extremely important.

Remember:

Problem = What is wrong?

Need = What must improve?

Solution = How might we improve it?


---

5. Business Needs Are Not Automatically Software Needs

This is one of the most important lessons of Week 1.

Suppose a hospital says:

> "Patients wait too long before seeing a doctor."



Is the solution automatically:

> "Build hospital software"?



No.

There could be several causes.

Perhaps:

there are too few doctors;

patients are incorrectly assigned to queues;

registration takes too long;

patient files are difficult to locate;

appointment scheduling is inefficient;

emergency cases are mixed with normal appointments.


Software may solve some of these problems, but not necessarily all of them.

Therefore, an analyst must investigate the underlying business problem before proposing technology.


---

6. Business Objectives

A business objective is a specific result that an organization wants to achieve.

Examples include:

increase sales;

reduce operating costs;

improve customer satisfaction;

reduce processing time;

improve data accuracy;

comply with regulations;

increase security;

expand services;

improve decision-making.


Example: Bank

Suppose a bank's objective is:

> Reduce the average time required to open a customer account from 45 minutes to 10 minutes.



That objective can lead to a business need:

> The bank needs a faster account-opening process.



That need can lead to requirements for a software system.

For example:

customers should submit information electronically;

staff should verify identity digitally;

the system should validate required information;

the system should notify customers about application status.


The software requirements therefore emerge from the business objective and business need.


---

7. The Business-to-Software Chain

Students should understand this chain very clearly:

BUSINESS OBJECTIVE
       ↓
BUSINESS PROBLEM / OPPORTUNITY
       ↓
BUSINESS NEED
       ↓
STAKEHOLDER NEEDS
       ↓
SYSTEM / SOFTWARE REQUIREMENTS
       ↓
ANALYSIS MODELS
       ↓
DESIGN
       ↓
IMPLEMENTATION

Example: University

Business objective:
Improve student registration

        ↓

Business problem:
Manual registration is slow and error-prone

        ↓

Business need:
Provide a faster and more accurate registration process

        ↓

Stakeholder needs:
Students need convenient registration
Lecturers need approval mechanisms
Finance needs fee information
Registry needs accurate records

        ↓

Software requirements:
The system shall allow students to register courses
The system shall validate prerequisites
The system shall allow authorized lecturers to approve registration
...

        ↓

OO analysis:
Identify Student, Course, Lecturer, Registration, Payment...

        ↓

UML models

        ↓

OO design

        ↓

Implementation

This chain will become extremely important throughout the entire 16-week module.


---

8. Subtopic 2: Stakeholders

8.1 What is a Stakeholder?

A stakeholder is a person, group or organization that has an interest in, is affected by, influences, or interacts with a system.

Consider a university student registration system.

Possible stakeholders include:

students;

lecturers;

registry officers;

finance officers;

department heads;

administrators;

ICT staff;

university management;

external regulators.


Notice that not every stakeholder necessarily uses the software directly.

For example, the Vice Chancellor may never log into the registration system but may still be affected by its performance and reports.


---

9. Primary and Secondary Stakeholders

Primary stakeholders

These directly interact with the system or are directly affected by it.

For example:

Student

Lecturer

Registrar

Finance Officer


Secondary stakeholders

These may not directly use the system but have an interest in its outcomes.

For example:

University management

Auditors

Regulators

ICT administrators



---

10. Why Stakeholders Matter in OOAD

Imagine that developers interview only students when developing a registration system.

Students might say:

> "We need online registration."



But Finance might say:

> "Students with outstanding fees should not be allowed to register."



Registry might say:

> "Students must meet programme requirements."



Lecturers might say:

> "Some courses require lecturer approval."



ICT might say:

> "Only authorized staff should access administrative functions."



Management might say:

> "We need reports showing registration statistics."



Therefore, if the analyst ignores stakeholders, important requirements can be missed.


---

11. Stakeholder Example

System: University Student Registration System

Stakeholder	Interest/Need

Student	Register courses
Lecturer	Approve or monitor registration
Registrar	Maintain academic registration records
Finance Officer	Verify financial eligibility
Department Head	Monitor programme registration
ICT Administrator	Maintain system and security
Management	Obtain reports


The analyst uses these stakeholder needs to understand what the system should accomplish.


---

12. Subtopic 3: Aspects of Business Software Needs

The second major topic in Week 1 is Aspects of Business Software Needs.

A business does not simply need "software."

It usually needs software to satisfy several categories of needs.

The most important distinction students should understand is:

Functional needs

versus

Non-functional needs


---

13. Functional Software Needs

A functional requirement describes what the system should do.

Think:

> FUNCTION = ACTION



Examples:

The system shall register students.

The system shall calculate fees.

The system shall generate invoices.

The system shall send notifications.

The system shall allow users to reset passwords.

The system shall generate examination reports.


Example

For an online banking system:

> The system shall allow customers to transfer money between accounts.



That is a functional requirement because it describes something the system must do.


---

14. Non-Functional Software Needs

A non-functional requirement describes a quality, constraint or condition under which the system must operate.

Think:

> NON-FUNCTIONAL = HOW WELL / UNDER WHAT CONDITIONS



Examples:

security;

performance;

availability;

usability;

reliability;

scalability;

maintainability;

accessibility.


Example

Functional requirement:

> The system shall allow customers to transfer money.



Non-functional requirement:

> The transfer request shall normally be processed within two seconds.



Another:

> The system shall encrypt sensitive customer information in transit.




---

15. Functional vs Non-Functional Requirements

Do not simply memorize "what versus how."

Understand the actual distinction.

Aspect	Functional Requirement	Non-Functional Requirement

Main question	What must the system do?	What quality/constraint must it satisfy?
Example	Register student	Registration page should load within 2 seconds
Example	Generate invoice	Invoice must be available 99.9% of the time
Example	Transfer money	Transfers must be encrypted
Example	Search products	Search results should appear quickly


Easy memory trick

Functional = behaviour

Non-functional = quality/constraint


---

16. Example: E-Commerce System

Suppose we are developing an online shopping system.

Functional requirements

The system shall:

1. allow customers to create accounts;


2. allow customers to search products;


3. allow customers to add products to a cart;


4. calculate order totals;


5. accept payments;


6. generate order confirmations.



Non-functional requirements

The system shall:

1. protect customer information;


2. support many concurrent users;


3. respond quickly;


4. be available continuously;


5. provide an accessible interface;


6. maintain reliable transaction records.



The system therefore needs both functional and non-functional requirements.


---

17. Business Rules

Another important aspect of software needs is the business rule.

A business rule is a policy, restriction or condition that governs how an organization operates.

University example

> A student may not register for a course unless the student has satisfied the course prerequisite.



That is a business rule.

The software must implement the rule.

Another example

> A customer may withdraw a maximum of MWK 500,000 per day.



That is a business rule.

Another

> An employee cannot approve their own expense claim.



Again, a business rule.


---

18. Business Rule vs Functional Requirement

These are often confused.

Business rule

> Students must pass BICT 2101 before registering for BICT 3202.



Functional requirement

> The system shall check whether a student has passed the prerequisite before allowing registration for BICT 3202.



The business rule comes from the organization.

The functional requirement describes what the software must do to enforce or support that rule.


---

19. Constraints

Software also operates under constraints.

A constraint is a limitation or condition that restricts the possible solution.

Examples:

available budget;

existing hardware;

legal requirements;

organizational policies;

required programming platform;

integration with an existing database;

internet availability;

deployment environment.


Example

A university may say:

> "The new system must work with our existing student database."



That is a constraint.


---

20. The Analyst's Job

At this point, students should begin seeing what an analyst actually does.

An analyst does not simply ask:

> "What software do you want?"



Instead, the analyst investigates:

1. What problem exists?

2. Why does it exist?

3. Who is affected?

4. What does the organization want to achieve?

5. What processes currently exist?

6. What information is required?

7. What rules govern the process?

8. What should the new system do?

9. What constraints exist?

10. How will we know that the solution is successful?

These questions form the foundation for later OO analysis.


---

21. Requirements Elicitation

Requirements elicitation is the process of discovering and documenting stakeholder needs and requirements.

ISO/IEC/IEEE 29148 describes requirements elicitation as using systematic techniques to proactively identify and document customer and end-user needs. It also places requirements engineering within activities such as discovering, eliciting, developing, analysing, verifying, validating, communicating, documenting and managing requirements. 

Common elicitation techniques

1. Interviews

The analyst talks directly to stakeholders.

Example:

> "How do you currently register students?"



2. Questionnaires

Useful when many users need to provide information.

3. Observation

The analyst watches users perform their work.

Example:

A developer observes how registry officers process student registration.

4. Document analysis

The analyst studies existing:

forms;

reports;

policies;

spreadsheets;

databases;

manuals.


5. Workshops

Multiple stakeholders discuss requirements together.

6. Prototyping

A basic version of the proposed system is shown to users so they can provide feedback.


---

22. Worked Example: Student Registration

Suppose Exploits University wants a new registration system.

Step 1 — Identify the business problem

Current registration is:

paper-based;

slow;

difficult to monitor;

vulnerable to data-entry errors.


Step 2 — Identify the business need

The university needs:

> A faster, more accurate and traceable student registration process.



Step 3 — Identify stakeholders

students;

lecturers;

registry;

finance;

ICT;

management.


Step 4 — Identify functional requirements

The system should:

authenticate students;

display available courses;

check prerequisites;

register courses;

remove courses;

submit registration for approval;

generate registration reports.


Step 5 — Identify non-functional requirements

The system should:

protect student information;

be available during registration periods;

respond quickly;

support many simultaneous users;

maintain reliable records.


Step 6 — Identify business rules

For example:

> A student cannot register for a course without satisfying its prerequisite.



Step 7 — Identify possible objects

Now we can begin thinking in object-oriented terms:

Student

Course

Lecturer

Registration

Programme

Payment

Department


Notice: We haven't designed the classes yet.

We are simply beginning to identify important concepts in the problem domain.

That distinction becomes critical in later weeks.


---

23. Subtopic 3: Object Technology for Business

Now we reach the third topic in the syllabus:

> Object Technology for Business




---

24. What is Object Technology?

Object technology is an approach to analysing, designing and developing systems around objects and their relationships.

Instead of viewing a system simply as a collection of procedures, object-oriented thinking asks:

> What entities exist in this problem domain?



> What information does each entity have?



> What can each entity do?



> How do the entities interact?



Oracle's object-oriented programming documentation describes a software object as a combination of related state and behaviour. State is represented through data, while behaviour is provided through methods. 


---

25. What is an Object?

An object is a distinct entity in a software system that has:

1. Identity


2. State


3. Behaviour



Let's explain each carefully.


---

25.1 Identity

Identity means that the object can be distinguished from other objects.

Imagine a university has:

Student A: Francis

Student B: Grace

Student C: John


All are students, but they are different individuals.

A system may distinguish them using:

student ID;

registration number;

UUID;

database identifier.


For example:

Student
ID: ST001
Name: Francis

and

Student
ID: ST002
Name: Grace

Both belong to the same general type, Student, but they are separate objects.


---

26. State

The state of an object refers to the data or characteristics describing its current condition.

For a Student object:

Student ID = ST001
Name = Francis Fweta
Programme = BSc ICT
Year = 3
Status = Active

These values describe the object's current state.

State can change.

For example:

Status = Active

could later become:

Status = Graduated


---

27. Behaviour

Behaviour describes what an object can do.

A Student object might:

registerCourse();

dropCourse();

viewResults();

payFees();

updateProfile().


Therefore:

Student
-------------------
State:
studentID
name
programme
year
status

Behaviour:
registerCourse()
dropCourse()
viewResults()
payFees()

This is the basic idea behind object-oriented thinking.


---

28. The Three-Part Object Model

Students should remember:

OBJECT
                |
       ┌────────┼────────┐
       ↓        ↓        ↓
   Identity    State   Behaviour

Example

Object: Student

Identity: ST001

State:

Name = Francis

Year = 3

Programme = BSc ICT


Behaviour:

Register course

View results

Pay fees



---

29. What is a Class?

A class is a blueprint or specification from which objects can be created.

Think about a house.

An architect can create one blueprint:

HOUSE BLUEPRINT
----------------
Bedrooms: 3
Kitchen: 1
Bathroom: 2

From that blueprint, many houses can be built.

Similarly:

STUDENT CLASS
----------------
studentID
name
programme
year
status

registerCourse()
viewResults()
payFees()

From that class, the system can create many Student objects.

Oracle describes a class as a blueprint/prototype from which objects are created. 


---

30. Class vs Object

This distinction is extremely important.

Class

A general definition.

Object

A specific instance of that definition.

Example:

CLASS:
Student

Objects:

student1 = Francis
student2 = Grace
student3 = John

Therefore:

> Student is a class; Francis is an object of the Student class.




---

31. Another Real-World Analogy

Think about a vehicle registration system.

Class

Vehicle

It might define:

registrationNumber;

make;

model;

colour;

start();

stop().


Objects

Vehicle 1:
Registration = MA 1234
Make = Toyota
Model = Corolla

Vehicle 2:
Registration = BT 5678
Make = Honda
Model = Fit

Both objects belong to the Vehicle class.


---

32. Why Object Technology Is Useful in Business

Organizations deal with real-world entities all the time.

A bank deals with:

customers;

accounts;

transactions;

loans;

employees;

branches.


A hospital deals with:

patients;

doctors;

nurses;

appointments;

prescriptions;

medical records.


A university deals with:

students;

lecturers;

courses;

programmes;

departments;

payments.


Object-oriented analysis allows analysts to represent these important concepts as elements of a software model.


---

33. Object Technology and the Real World

This is one of the strongest ideas students should take away from Week 1.

Consider a bank.

Real world:

Customer
   |
   ↓
Bank Account
   |
   ↓
Transaction

The software can model these concepts.

For example:

Customer
---------
customerID
name
phone

openAccount()
updateDetails()

Account
---------
accountNumber
balance
accountType

deposit()
withdraw()
transfer()

Transaction
------------
transactionID
amount
date
type

process()
reverse()

The system therefore represents important business concepts as software objects/classes.


---

34. Object Technology Does NOT Mean "Everything Is a Physical Object"

This is a common beginner mistake.

Students may say:

> "We can model a Student because a student is a physical person."



Correct.

Then they ask:

> "But how can we model a Registration? Registration isn't a physical object."



Good question.

In object-oriented analysis, an object does not have to be physically tangible.

We can model conceptual entities.

For example:

Registration

Invoice

Payment

Account

Order

Appointment

Booking

Transaction


These may be conceptual/business entities, but they can still be represented as software objects.


---

35. Object Technology and Modularity

One major benefit of object-oriented approaches is modularity.

A large software system can be divided into smaller components.

For example:

University System
       |
       ├── Student Management
       ├── Registration
       ├── Finance
       ├── Examination
       └── Reporting

Each part can contain related objects/classes.

Oracle's documentation identifies modularity, information hiding, reuse and easier replacement/debugging among benefits associated with organizing software around objects. 


---

36. Encapsulation — Introduction

Students will study this more deeply later, but we introduce it now.

Encapsulation means combining data and the operations that work on that data while controlling how the internal state is accessed.

For example:

BankAccount
----------------
- balance

+ deposit()
+ withdraw()
+ getBalance()

We don't necessarily want every part of the application directly changing:

balance = -500000

Instead, the account object controls how its balance changes.

Oracle's documentation similarly describes encapsulation as hiding internal state and allowing interaction through an object's methods. 


---

37. Why Encapsulation Matters in Business

Consider a banking system.

Without appropriate control, another part of the application might directly modify:

balance = 1000000

without performing a legitimate transaction.

With encapsulation:

withdraw(50000)

The account object can check:

1. Is the account active?


2. Is the amount valid?


3. Is sufficient balance available?


4. Is the transaction permitted?


5. Should the transaction be recorded?



The object therefore protects its own business rules.


---

38. Reusability

Another major advantage of object-oriented approaches is reuse.

Suppose developers have created a well-designed:

EmailNotification

component.

Other parts of the system may reuse it.

For example:

Student System → EmailNotification
Bank System    → EmailNotification
Hospital System → EmailNotification

Instead of rebuilding notification functionality repeatedly, developers can reuse appropriate components.

Inheritance is another mechanism associated with reuse; a subclass can inherit common state and behaviour from a superclass. 


---

39. Inheritance — Basic Introduction

Suppose we have:

User

with:

userID
name
email
login()
logout()

We could have:

Student
Lecturer
Administrator

all sharing common characteristics.

Conceptually:

User
               |
       ┌───────┼────────┐
       ↓       ↓        ↓
    Student  Lecturer  Admin

The specialized classes can reuse appropriate characteristics of the general class.

This is called inheritance.

We will study inheritance in much greater detail in Week 6.


---

40. Polymorphism — Basic Introduction

Polymorphism means that related objects can respond differently to the same operation.

Imagine:

User
  |
  ├── Student
  └── Lecturer

Suppose both have:

displayDashboard()

A Student might see:

Courses
Fees
Results

A Lecturer might see:

Courses Taught
Students
Marks
Attendance

The operation has the same general purpose:

> displayDashboard()



but different objects provide different behaviour.

Polymorphism is one of the core concepts associated with object-oriented programming. 


---

41. Abstraction — Basic Introduction

Abstraction means focusing on the important characteristics of something while leaving out unnecessary detail.

Consider an ATM.

When a customer withdraws money, the customer sees:

Insert card
Enter PIN
Select withdrawal
Enter amount
Receive cash

The customer does not need to see:

database queries;

network protocols;

encryption algorithms;

transaction locking;

server communication.


The ATM provides a simplified view of a complex system.

In object-oriented modelling, abstraction helps analysts focus on the important characteristics and behaviour of entities rather than every possible detail.

Microsoft's current C# documentation similarly describes abstraction as modelling relevant attributes and interactions as classes to define an abstract representation of a system. 


---

42. Four Major OO Principles — Preview

Students will encounter these repeatedly throughout the course:

Principle	Simple meaning

Abstraction	Focus on important characteristics
Encapsulation	Protect and control internal state
Inheritance	Create specialized classes from existing ones
Polymorphism	Related objects can provide different implementations


These are not the entire OOAD methodology, but they are fundamental object-oriented concepts.

Microsoft's current C# documentation identifies these four as the basic principles of object-oriented programming. 


---

43. Strengths of Object-Oriented Approaches

The course learning outcomes specifically ask students to discuss the strengths and limitations of the object-oriented approach.

43.1 Modularity

Systems can be divided into related components.

43.2 Reusability

Existing components/classes can potentially be reused.

43.3 Maintainability

Well-designed classes can isolate changes.

43.4 Encapsulation

Implementation details can be hidden behind controlled interfaces.

43.5 Extensibility

Systems can be extended by adding or modifying appropriate components.

43.6 Better representation of complex domains

Business concepts such as:

Customer;

Account;

Product;

Order;

Student;

Course;


can naturally appear in the system model.

43.7 Supports multiple levels of abstraction

Analysts can move from high-level concepts toward detailed designs.


---

44. Limitations and Challenges

Object orientation is powerful, but it is not magic.

44.1 Complexity

Large object-oriented systems can contain thousands of classes and relationships.

Poor design can therefore make a system extremely difficult to understand.

44.2 Learning curve

Students and developers must understand:

objects;

classes;

relationships;

inheritance;

interfaces;

polymorphism;

encapsulation;

design principles.


44.3 Poor modelling can create unnecessary complexity

Not everything should automatically become a class.

For example, creating:

StudentName
StudentAge
StudentColour
StudentChair
StudentShoes
StudentPhone

as separate classes would be ridiculous for most university registration systems.

The analyst must determine what is actually important to the system.

44.4 Inheritance can be misused

A developer might create deep inheritance hierarchies simply because inheritance exists.

This can make software difficult to modify.

44.5 Initial modelling effort

OOAD requires careful analysis before implementation.

That may appear slower at the beginning, but the goal is to reduce misunderstandings and design problems later.


---

45. Object-Oriented Analysis vs Object-Oriented Programming

Students often confuse these.

Object-Oriented Analysis (OOA)

Focuses on:

> Understanding the problem and modelling what the system needs.



Object-Oriented Design (OOD)

Focuses on:

> Designing how the software will satisfy those requirements.



Object-Oriented Programming (OOP)

Focuses on:

> Implementing the design in an object-oriented programming language.




---

Example

Suppose we are building a university registration system.

Analysis

We identify:

Student
Course
Lecturer
Registration
Programme

and determine their relationships and required behaviour.

Design

We decide:

what classes should exist;

their responsibilities;

interfaces;

database interaction;

architectural layers;

communication between components.


Programming

We implement the design using a language such as:

Java;

C#;

C++;

Python;

Kotlin;

TypeScript, where object-oriented features are used.



---

46. Very Important: Analysis Is Not Coding

A student might say:

> "I know Java, so I can do OOAD."



Not necessarily.

Programming knowledge helps, but OOAD requires the ability to:

understand business problems;

communicate with stakeholders;

identify requirements;

identify domain concepts;

model relationships;

represent system behaviour;

evaluate alternative designs.


A person can be an excellent programmer but a poor analyst.


---

47. Case Study for the Entire Module

To make this course practical, we will use a continuing example:

University Student Management and Registration System

Imagine that a university wants to replace its manual registration system.

Current situation

Students:

1. collect forms;


2. fill in personal information;


3. select courses;


4. obtain approvals;


5. visit finance;


6. submit forms;


7. wait for data entry.



Problems

long queues;

duplicate records;

lost forms;

incorrect course registration;

slow reporting;

difficulty checking prerequisites;

limited visibility of registration status.


Business objective

> Improve the efficiency, accuracy, transparency and accessibility of student registration.



Business need

> The university needs an integrated student registration process.



Potential software solution

> An online student management and registration system.




---

48. Initial Identification of Business Objects

From the case study, we can identify potential domain concepts:

Student
Course
Programme
Department
Lecturer
Registration
Payment
Result
User
Notification

At this stage, these are candidate objects/classes.

We should not immediately assume that every candidate will become a final class.

That decision belongs to analysis and design.

This distinction will become particularly important when we study object identification in Week 5.


---

49. A First Look at the System

We can conceptually represent the system like this:

UNIVERSITY SYSTEM
                        |
       ┌────────────────┼────────────────┐
       ↓                ↓                ↓
   Students          Courses          Finance
       |                |                |
       ↓                ↓                ↓
 Registration      Course Data       Payments
       |
       ↓
  Approvals
       |
       ↓
   Reporting

This is not yet a formal UML diagram.

It is simply a conceptual representation to help us understand the business domain.

Formal UML modelling comes in later weeks. UML is standardized by the Object Management Group (OMG); the OMG currently publishes UML 2.5.1 as the formal specification. 


---

50. Worked Example: ATM System

Let's apply Week 1 concepts to another system.

Business problem

Customers have to visit bank branches to perform simple transactions.

Business need

The bank needs to provide convenient self-service banking.

Business objective

Reduce branch workload while providing customers with 24/7 access to basic transactions.

Potential software solution

ATM system.

Stakeholders

Customer

Bank

Bank employee

Security administrator

Payment network


Functional needs

The system should:

authenticate customers;

display account balance;

allow cash withdrawal;

allow deposits;

allow PIN changes;

print receipts.


Non-functional needs

The system should:

be secure;

be reliable;

respond quickly;

be available 24/7;

protect customer information.


Potential objects

Customer
Card
Account
Transaction
ATM
Receipt

Notice how we have moved from:

business problem → business need → requirements → objects.

That is exactly the thinking students need to develop.


---

51. Practical Activity — Week 1

Practical: Identify Business Needs and Candidate Objects

Scenario

A college currently uses a manual library system.

Students:

physically search shelves;

fill out borrowing forms;

wait for librarians to check records;

sometimes lose borrowing slips;

cannot easily determine whether a book is available.


The college wants to improve the process.

Student Task 1 — Identify the business problem

Write at least five problems.

Student Task 2 — Identify business needs

Write at least three business needs.

Student Task 3 — Identify stakeholders

Identify at least six stakeholders.

Student Task 4 — Identify functional requirements

Write at least eight functional requirements.

Student Task 5 — Identify non-functional requirements

Write at least five non-functional requirements.

Student Task 6 — Identify candidate objects

Identify at least eight possible objects/classes.

Possible answers might include:

Student
Book
Librarian
Library
Borrowing
Return
Fine
Reservation

Students must explain why they selected each candidate.


---

52. Tutorial Activity

Group Exercise

Divide the class into groups.

Each group selects one of the following:

1. Mobile money system


2. Hospital management system


3. Online shopping system


4. Hotel booking system


5. University registration system



For the selected system, produce:

A. Business problem

What is currently wrong?

B. Business need

What does the organization need to improve?

C. Business objective

What measurable result should be achieved?

D. Stakeholders

Who is affected?

E. Functional needs

What should the software do?

F. Non-functional needs

What qualities must it have?

G. Business rules

What policies or restrictions must it enforce?

H. Candidate objects

What important entities exist in the problem domain?

Each group presents its findings to the class.


---

53. Independent Learning — 10 Hours

Students should spend their independent study time doing the following.

Activity 1 — Read

Study:

business needs;

requirements;

functional requirements;

non-functional requirements;

stakeholders;

object technology.


Activity 2 — Observation

Choose a system that you use regularly.

Examples:

mobile banking;

mobile money;

university registration;

supermarket;

hospital;

library.


Observe how the system operates.

Write:

1. the business problem;


2. business objectives;


3. business needs;


4. stakeholders;


5. functional requirements;


6. non-functional requirements;


7. business rules;


8. possible objects.



Activity 3 — Object observation

Look around your environment.

Identify 10 real-world objects.

For each object, write:

Object	State	Behaviour

Phone	battery, model, volume	call, charge, restart
Student	name, programme, year	register, study, graduate
Car	speed, fuel, gear	start, accelerate, brake


This exercise helps students begin thinking in terms of state and behaviour, which are fundamental concepts in object-oriented thinking. 


---

54. Common Student Mistakes

Mistake 1

> "Business need means software requirement."



Correction: A business need describes what the organization needs to achieve; a software requirement describes what the system must provide to support that need.


---

Mistake 2

> "Every business problem requires software."



Correction: Some problems are organizational, financial, human-resource, procedural or infrastructural rather than technological.


---

Mistake 3

> "Functional means important and non-functional means unimportant."



Correction: Both are important. Functional requirements describe system behaviour; non-functional requirements describe qualities and constraints.


---

Mistake 4

> "An object must be a physical thing."



Correction: Software can model conceptual/business entities such as Payment, Registration, Order and Transaction.


---

Mistake 5

> "A class and an object are the same thing."



Correction: A class defines a type/blueprint; an object is a particular instance.


---

Mistake 6

> "OOAD means programming in Java."



Correction: OOAD is concerned primarily with analysing and designing systems using object-oriented concepts. Programming is the implementation stage.


---

Mistake 7

> "We should immediately create classes from every noun."



Correction: Nouns can provide candidate concepts, but analysis is required to determine which concepts actually belong in the model.


---

55. Week 1 Summary

Let's bring everything together.

Business Needs

A business need describes a problem, opportunity or desired improvement that an organization needs to address.

Business Objective

Describes the result the organization wants to achieve.

Stakeholder

A person, group or organization that has an interest in or is affected by the system.

Functional Requirement

Describes what the system should do.

Non-Functional Requirement

Describes qualities, constraints or conditions under which the system must operate.

Business Rule

A policy or condition that governs how an organization operates.

Object

A software entity with:

identity;

state;

behaviour.


Class

A specification/blueprint from which objects can be created.

Object Technology

An approach that represents a problem domain using objects, their attributes/state, behaviour and relationships.


---

56. The Most Important Concept of Week 1

Students should be able to explain this entire sequence without memorizing it mechanically:

> An organization has a business objective.



↓

> There may be a business problem preventing that objective from being achieved.



↓

> The organization identifies a business need.



↓

> Stakeholders help identify what is required.



↓

> Requirements are identified and documented.



↓

> Analysts study the problem domain.



↓

> Important entities and their behaviour can be represented using object-oriented concepts.



↓

> These models eventually become the foundation for system design and implementation.



That is the foundation upon which the remaining 15 weeks will build.


---

57. Revision Questions

Short-answer questions

1. Define a business need.


2. What is a business problem?


3. Differentiate between a business problem and a business need.


4. What is a business objective?


5. Define a stakeholder.


6. What is a functional requirement?


7. What is a non-functional requirement?


8. What is a business rule?


9. Define object technology.


10. What is an object?


11. What is a class?


12. Differentiate between a class and an object.


13. What is object state?


14. What is object behaviour?


15. Explain encapsulation.


16. What is abstraction?


17. What is inheritance?


18. What is polymorphism?


19. Give four advantages of object-oriented approaches.


20. Give three limitations or challenges of object-oriented approaches.



Application questions

Question 1

A hospital has patients waiting several hours before being attended to.

Identify:

a. The business problem
b. Two business needs
c. Two business objectives
d. Five stakeholders
e. Five functional requirements
f. Five non-functional requirements
g. Five candidate objects


---

Question 2

A university wants an online examination management system.

Identify:

a. The business need
b. Stakeholders
c. Functional requirements
d. Non-functional requirements
e. Business rules
f. Candidate objects


---

Question 3

Explain the difference between:

Business need → Requirement → Software solution

Use a real-world example.


---

58. Examination-Style Question

> "A retail organization currently records sales using handwritten receipts. Management wants to introduce a computerized sales management system. As an object-oriented systems analyst, explain how you would move from understanding the business need to identifying potential objects for the proposed system."



A strong answer should discuss:

1. current business problem;


2. business objectives;


3. business needs;


4. stakeholders;


5. requirements elicitation;


6. functional requirements;


7. non-functional requirements;


8. business rules;


9. candidate objects;


10. state and behaviour of the candidate objects.




---

59. References and Further Reading

Core standards and authoritative references

International Organization for Standardization. (2018). ISO/IEC/IEEE 29148:2018 — Systems and software engineering — Life cycle processes — Requirements engineering. ISO. The standard defines requirements engineering processes and information products and remains the current published edition; ISO reports that it was reviewed and confirmed in 2024. 

Object Management Group. (2017). OMG Unified Modeling Language (OMG UML), Version 2.5.1. OMG. The OMG maintains UML 2.5.1 as the formal UML specification. 


Object-oriented concepts

Oracle. Object-Oriented Programming Concepts. Oracle's documentation provides explanations of objects, classes, inheritance, encapsulation and related OO concepts. 

Microsoft. Object-oriented programming (C#). Microsoft Learn, updated 2025. This provides a contemporary explanation of abstraction, encapsulation, inheritance and polymorphism. 


Prescribed texts from the university course outline

Mach, E. (2019). Object Oriented Analysis & Design Cookbook: Introduction to Practical System Modeling.

Reddy, V., & Korra, S. (2018). Object-Oriented Analysis and Design Using UML.

The Art of Service. (2021). Object Oriented Analysis and Design: A Complete Guide.


Recommended texts from the course outline

Wixom, B., & Dennis, A. (2018). Systems Analysis and Design.

Blokdyk, G. (2021). Object-Oriented Analysis and Design Standard Requirements.

Wixom, B., & Dennis, A. (2020). Systems Analysis and Design: An Object-Oriented Approach with UML.
