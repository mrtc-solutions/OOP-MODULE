BICT 3202 — OBJECT-ORIENTED ANALYSIS AND DESIGN

WEEK 6: OBJECT-ORIENTED ANALYSIS — OBJECT MODELLING II

Programme: BSc in Information Communication and Technology
Year: 3
Course Code: BICT 3202
Week: 6 of 16
Lecture: 2 hours
Tutorial: 1 hour
Practical: 1 hour
Independent Learning: 10 hours

Topics from the official course outline

1. Aggregation


2. Inheritance


3. Polymorphism


4. Grouping




---

1. Where Week 6 Fits in the Module

Let's first make the progression absolutely clear.

In Week 5, students learned how to identify and model:

Classes
Objects
Attributes
Operations
Links
Associations
Multiplicity
Generalization
Specialization

Now in Week 6, we build on those concepts.

The progression is:

WEEK 5
What objects/classes exist?
        ↓
How are they related?
        ↓
Generalization/Specialization
        ↓
WEEK 6
How do objects form whole-part structures?
        ↓
How can characteristics be inherited?
        ↓
How can different objects respond differently?
        ↓
How can related classes be organized?

This is important because aggregation, inheritance and polymorphism are not isolated programming concepts. In OOAD, they help us construct models that represent real systems in a reusable and understandable way.

The formal UML specification defines aggregation as a property of an association end and distinguishes shared aggregation from composite aggregation. 


---

2. Week 6 Learning Outcomes

By the end of this week, students should be able to:

1. Define aggregation.


2. Explain the whole-part relationship.


3. Distinguish ordinary association from aggregation.


4. Distinguish aggregation from composition.


5. Explain shared aggregation.


6. Explain composite aggregation.


7. Represent aggregation using UML notation.


8. Explain inheritance in object-oriented systems.


9. Explain the relationship between inheritance and UML generalization.


10. Identify superclass and subclass.


11. Explain inherited attributes and operations.


12. Distinguish inheritance from association.


13. Explain polymorphism.


14. Demonstrate polymorphism using a real-world example.


15. Explain method overriding in relation to polymorphism.


16. Explain why polymorphism supports extensibility.


17. Explain grouping/classification in object models.


18. Develop a more complete class hierarchy.


19. Use a CASE tool to model aggregation and inheritance.


20. Evaluate whether aggregation, inheritance or polymorphism is appropriate for a given problem.




---

PART A — AGGREGATION

3. What Is Aggregation?

Let's begin with a simple question:

> What does it mean when one object is made up of, or contains, other objects?



Consider a university.

A university has:

Departments

A department has:

Lecturers
Students
Courses

So we could represent:

University
    ◇──── Department

This represents a whole-part relationship.

The university is the whole.

The department is a part.

This type of relationship can be modelled using aggregation.


---

4. Aggregation in Simple English

Aggregation can be explained as:

> A relationship in which one object represents a whole or collection that is related to other objects representing its parts.



For example:

Library ◇──── Book

means:

> A Library contains/has Books.



Another example:

Department ◇──── Lecturer

means:

> A Department has Lecturers.




---

5. The UML Aggregation Symbol

Aggregation is represented using a hollow diamond.

Department ◇──────── Lecturer

The diamond is placed on the whole side.

Therefore:

Department ◇──────── Lecturer
     ↑                    ↑
   Whole                 Part

Remember:

> Hollow diamond = aggregation



This is different from the filled diamond used for composition, which we will discuss shortly.


---

6. Aggregation vs Ordinary Association

This distinction is extremely important.

Consider:

Student ───────── Course

This is an association.

It means:

> A Student is related to a Course.



Now consider:

Department ◇──────── Lecturer

This represents a whole-part relationship.

It means:

> A Department is an aggregate involving Lecturers.



So:

Relationship	Meaning

Association	General relationship
Aggregation	Whole-part relationship
Composition	Strong whole-part relationship



---

7. Real-Life Example: Football Team

Imagine a football team.

FootballTeam ◇──── Player

The team consists of players.

But a player can potentially exist independently of a particular team.

For example:

Manchester United
       ◇
       |
    Player

If the player leaves the club, the player does not cease to exist.

Therefore, this is a useful conceptual example of weak/shared whole-part aggregation.


---

8. Another Example: Classroom

Consider:

Classroom ◇──── Student

A classroom contains students.

But if the classroom is closed or renamed, the students still exist.

Therefore:

Classroom
    ◇
    |
 Student

can represent a whole-part relationship where the parts have independent existence.


---

9. Aggregation Does NOT Mean "The Part Dies When the Whole Dies"

This is one of the easiest ways to distinguish aggregation from composition.

Suppose:

Department ◇──── Lecturer

If the department is reorganized or removed:

> Does the lecturer cease to exist?



No.

The lecturer can be assigned to another department.

Therefore, the lecturer has an independent existence.


---

10. Composition

Now we need to introduce a closely related concept.

Composition is a stronger form of whole-part relationship.

UML identifies composite aggregation as the form where the composite object has responsibility for the existence and storage of the composed parts; a part can be included in at most one composite at a time. 

It is represented using a filled/black diamond.

House ◆──────── Room

Here:

House = Whole
Room  = Part


---

11. Aggregation vs Composition

This must be very clear.

Aggregation

Department ◇──── Lecturer

The Lecturer can exist independently.

Composition

House ◆──── Room

The Room is treated as a strongly owned part of that particular House.

So:

◇ = weak/shared whole-part
◆ = strong/composite whole-part


---

12. Simple Analogy

Think of a football club and player.

Club ◇──── Player

The player can leave the club and join another.

That's the idea of a weaker whole-part relationship.

Now think about a house and its rooms:

House ◆──── Room

In a system model, the room is strongly owned as a part of that house.

That's composition.


---

13. Why Does This Matter?

Because the relationship tells us something about the lifecycle and ownership of objects.

Compare:

Team ◇──── Player

and:

Order ◆──── OrderLine

If an order is deleted, its order lines normally have no independent meaning within the system.

Therefore:

Order ◆──── OrderLine

is a much stronger whole-part relationship.


---

14. Aggregation Example: University

Let's model a university.

University ◇──── Department

A university has departments.

A department can be represented as part of the university.

Then:

Department ◇──── Lecturer

A department has lecturers.

We could therefore have:

University
    ◇
    |
Department
    ◇
    |
Lecturer

However, students must not blindly add diamonds everywhere.

The relationship must be justified by the requirements.


---

15. Aggregation and Multiplicity

Aggregation can also use multiplicity.

For example:

University 1 ◇──────── 1..* Department

This can be read as:

> One university has one or more departments.



Another:

Department 1 ◇──────── 0..* Lecturer

This can mean:

> One department may have zero or many lecturers.




---

16. Important Warning

Do not assume:

> "Contains" automatically means aggregation.



For example:

> A customer has an address.



This does not automatically mean:

Customer ◇──── Address

The analyst must understand the domain and lifecycle.

The goal is not to use every possible UML symbol.

The goal is:

> To choose the relationship that best represents the requirements.




---

PART B — INHERITANCE

17. What Is Inheritance?

Inheritance is a mechanism through which a more specific class can acquire characteristics and behaviour from a more general class.

For example:

Vehicle
                    △
                    |
          ┌─────────┴─────────┐
          ↓                   ↓
        Car              Motorcycle

A Car inherits characteristics of Vehicle.

A Motorcycle also inherits characteristics of Vehicle.

In UML, this relationship is represented through generalization. The UML specification states that an instance of the specific classifier is also an instance of the general classifier and that the specific classifier inherits features of the general classifier. 


---

18. Generalization vs Inheritance

Students often ask:

> "Are generalization and inheritance the same?"



They are closely related but we should be precise.

UML terminology

The relationship in the model is called:

> Generalization



Object-oriented programming terminology

The implementation mechanism is commonly called:

> Inheritance



So:

UML → Generalization
Programming → Inheritance

A UML generalization relationship can be implemented using inheritance in an object-oriented programming language.


---

19. Example: Employee

Suppose an organization has:

Employee

There are:

Manager
Lecturer
Accountant
Technician

These are all types of employees.

Therefore:

Employee
                       △
                       |
       ┌───────────────┼───────────────┐
       ↓               ↓               ↓
    Manager         Lecturer       Accountant


---

20. What Does the Child Inherit?

Suppose Employee has:

Employee
-------------------------
employeeID
name
email
-------------------------
login()
logout()

Then:

Manager
-------------------------
department
approveLeave()

A Manager can conceptually have:

employeeID
name
email
department

login()
logout()
approveLeave()

The Manager does not need to duplicate the common features in its own class declaration.


---

21. Why Use Inheritance?

Inheritance can support:

1. Reuse

Common characteristics are defined once.

2. Consistency

Shared behaviour can be managed in one general class.

3. Specialization

Subclasses can add their own characteristics.

4. Polymorphism

Inheritance can support substitutability and polymorphic behaviour.

5. Maintainability

Changing a shared feature can be managed centrally, depending on the design.


---

22. Inheritance Example

Consider:

Animal

with:

name
age
eat()

Then:

Dog
Cat
Bird

can inherit common characteristics.

Animal
                       △
                       |
          ┌────────────┼────────────┐
          ↓            ↓            ↓
         Dog          Cat          Bird

But each can have specialized behaviour.

Dog → bark()
Cat → meow()
Bird → fly()


---

23. The "Is-A" Rule Again

Inheritance should generally make sense as an is-a relationship.

Dog is an Animal.

Good.

Car is a Vehicle.

Good.

Student is a User.

Potentially good.

But:

Car is an Engine.

No.

Student is a Course.

No.

The latter relationships should not be modelled using inheritance.


---

24. Inheritance vs Aggregation

This is one of the most common examination questions.

Inheritance

Represents:

> IS-A



Car ─────▷ Vehicle

A car is a vehicle.

Aggregation

Represents:

> HAS-A / WHOLE-PART



Car ◇──── Engine

A car has an engine.

So remember:

IS-A  → Generalization/Inheritance

HAS-A / PART-OF → Aggregation/Composition


---

25. Example: University

Suppose:

User

has:

userID
name
email
login()
logout()

Then:

User
                      △
                      |
            ┌─────────┴─────────┐
            ↓                   ↓
         Student             Lecturer

Student adds:

programme
yearOfStudy
registerCourse()

Lecturer adds:

department
academicRank
assignGrade()

This is inheritance/generalization.


---

PART C — POLYMORPHISM

26. What Is Polymorphism?

Now we reach one of the most important concepts in object-oriented design.

The word polymorphism comes from Greek roots meaning roughly:

> many forms.



In object-oriented systems, polymorphism allows the same operation/message to be associated with different implementations or behaviours depending on the object receiving it.

In simple terms:

> Different objects can respond differently to the same request.




---

27. Real-World Example

Imagine you tell:

> "Make a sound!"



Different animals respond differently.

Dog → bark
Cat → meow
Cow → moo
Bird → chirp

The request is conceptually the same:

makeSound()

but the behaviour differs.

Animal
------------------
makeSound()
      △
      |
 ┌────┼────┐
 ↓    ↓    ↓
Dog  Cat  Cow

Dog.makeSound() → bark
Cat.makeSound() → meow
Cow.makeSound() → moo

That is the basic idea of polymorphism.


---

28. Why Is This Powerful?

Suppose a system needs to work with different types of payment.

We could have:

Payment

with:

processPayment()

Then:

Payment
                △
                |
       ┌────────┼────────┐
       ↓        ↓        ↓
     Card     Mobile    Bank
   Payment    Money    Transfer

Each class can implement:

processPayment()

differently.

So the system can issue the general request:

processPayment()

without needing to treat every payment type as completely unrelated.


---

29. Polymorphism in Simple Terms

Think:

> One operation name, different behaviour.



For example:

draw()

For:

Circle
Rectangle
Triangle

The operation is:

draw()

But each shape draws itself differently.


---

30. Polymorphism and Inheritance

These concepts often work together.

For example:

Shape
                      △
                      |
             ┌────────┴────────┐
             ↓                 ↓
          Circle           Rectangle

Shape defines:

draw()

Circle provides its own implementation:

draw() → draw a circle

Rectangle provides:

draw() → draw a rectangle

The same operation:

draw()

has different behaviour.


---

31. Method Overriding

In programming, this idea is commonly implemented through method overriding.

Suppose the general class defines:

Animal
----------------
makeSound()

The subclasses provide specialized versions:

Dog
----------------
makeSound()

Cat
----------------
makeSound()

The subclass version overrides or provides a specialized implementation of the inherited operation.


---

32. A Very Simple Programming Example

Students familiar with Java may understand this:

Animal a;

a = new Dog();
a.makeSound();

The result could be:

Bark

If:

a = new Cat();
a.makeSound();

the result could be:

Meow

The variable can refer to an Animal, but the actual object's implementation determines the behaviour.

That is the power of polymorphism.


---

33. Polymorphism Without Programming Syntax

Since this is OOAD, students should first understand the modelling idea.

We can simply model:

Payment
                      △
                      |
           ┌──────────┼──────────┐
           ↓          ↓          ↓
         Card       Mobile      Bank
        Payment      Money     Transfer
           |          |          |
           └──────────┼──────────┘
                      |
               processPayment()

The model tells us:

> Different payment types support the same conceptual operation but may perform it differently.




---

34. Another Example: Notification System

Imagine a system that sends notifications.

General class:

Notification
--------------------
send()

Specialized classes:

EmailNotification
SMSNotification
PushNotification

Each implements:

send()

differently.

Notification
                     △
                     |
          ┌──────────┼───────────┐
          ↓          ↓           ↓
        Email        SMS         Push
          |           |           |
          └───────────┼───────────┘
                      ↓
                     send()

This is an excellent modern example because applications frequently support multiple communication channels.


---

35. Why Polymorphism Helps Software Design

Polymorphism can allow systems to be designed around common abstractions.

For example, instead of writing completely separate logic for:

Email
SMS
Push

the system can work with:

Notification

and allow each subtype to determine how send() works.

This supports extensibility.

Suppose we later introduce:

WhatsAppNotification

We can potentially add another specialization without changing every part of the system that simply needs to request:

send()

The actual implementation depends on the new object.


---

PART D — GROUPING

36. What Does Grouping Mean in Object Modelling?

As systems become larger, diagrams can become difficult to understand.

Imagine an enterprise system with:

60 classes

Putting all 60 classes into one diagram would be confusing.

Therefore, related elements can be organized into meaningful groups/packages.

In UML, packages provide a mechanism for organizing model elements.

Think of a package as a folder.


---

37. Real-World Analogy

Your computer might contain:

University System
│
├── Student Management
├── Finance
├── Human Resources
├── Library
└── Accommodation

Each area can contain related classes.

For example:

Student Management
│
├── Student
├── Programme
├── Course
├── Registration
└── Result

This is much easier to manage than one giant diagram.


---

38. Grouping Related Classes

For a hospital:

Hospital System
│
├── Patient Management
│   ├── Patient
│   ├── Appointment
│   └── MedicalRecord
│
├── Staff Management
│   ├── Doctor
│   ├── Nurse
│   └── Administrator
│
└── Billing
    ├── Invoice
    ├── Payment
    └── Insurance

Grouping makes the model easier to understand.


---

39. Why Grouping Matters

Grouping can help with:

organization;

readability;

modularity;

maintenance;

team development;

navigation through large models;

separation of related concerns.


It becomes increasingly important when students begin designing larger systems.


---

40. Complete Example: Online Shopping System

Let's bring all four Week 6 concepts together.

Suppose we are developing an online shopping system.

We might have:

Customer
Order
OrderItem
Product
Payment
Delivery


---

Aggregation/Composition

An Order contains OrderItems:

Order ◆──── OrderItem

An OrderItem is strongly associated with a particular Order.


---

Inheritance

Payment may be generalized:

Payment
                    △
                    |
          ┌─────────┼─────────┐
          ↓         ↓         ↓
        Card      Mobile     Bank
       Payment     Money    Transfer


---

Polymorphism

All payment types may support:

processPayment()

but each performs it differently.


---

Grouping

We could organize the system:

Online Shopping
│
├── Customer Management
│
├── Order Management
│
├── Product Management
│
├── Payment Management
│
└── Delivery Management

Now students can see how all four concepts fit together.


---

41. Another Complete Example: University System

Let's build a larger model.

User
                      △
             ┌────────┴────────┐
             ↓                 ↓
          Student           Lecturer
             |                 |
             |                 |
             └───────┐ ┌───────┘
                     ↓ ↓
                   Course

Then:

Department ◇──── Lecturer

and:

Student ─── Registration ─── Course

Then perhaps:

Course ◆──── CourseMaterial

if course materials are treated as strongly owned parts.


---

42. Putting Polymorphism Into the University System

Suppose the university supports different assessment types:

Assessment

with:

calculateMark()

Specialized forms:

Assignment
Exam
Quiz
Project

Then:

Assessment
                 
