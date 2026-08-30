BICT 3202 — OBJECT-ORIENTED ANALYSIS AND DESIGN

WEEK 7: OBJECT-ORIENTED ANALYSIS — DYNAMIC MODELLING

Programme: BSc in Information Communication and Technology
Year: 3
Course Code: BICT 3202
Week: 7 of 16
Lectures: 2 hours
Tutorial: 1 hour
Practical: 1 hour
Independent Learning: 10 hours


---

1. Where Week 7 Fits in the Course

Yes — Week 7 follows Week 6 exactly according to the sequence in the course outline.

So far, students have progressed through:

WEEK 1
Business Needs
        ↓
WEEK 2
Principles of Object Modelling
        ↓
WEEK 3
Modelling Language / UML
        ↓
WEEK 4
Object-Oriented Analysis — Object Modelling I
        ↓
WEEK 5
Object-Oriented Analysis — Object Modelling I continued
        ↓
WEEK 6
Object-Oriented Analysis — Object Modelling II
Aggregation
Inheritance
Polymorphism
Grouping
        ↓
WEEK 7
OBJECT-ORIENTED ANALYSIS — DYNAMIC MODELLING

The important change in Week 7 is this:

> Previous weeks mainly asked: "What things exist in the system and how are they structurally related?"



Week 7 asks:

> "What happens to those things over time, and how do they respond to events?"



That distinction is fundamental to object-oriented modelling.

The OMG UML specification separates UML into structural and behavioural semantic areas. State machines, activities and interactions are among the behavioural modelling constructs, while classes, classifiers and packages belong to structural modelling. 


---

2. Week 7 Topics from the Official Course Outline

This week's official topics are:

1. Event


2. State


3. Operations


4. Concurrency


5. Relation of Structure and Dynamic Models


6. CASE Tools Support



We will therefore cover all six rather than simply teaching "state diagrams."


---

3. Week 7 Learning Outcomes

By the end of this week, students should be able to:

1. Define dynamic modelling.


2. Explain why dynamic behaviour must be modelled in an object-oriented system.


3. Define an event.


4. Identify different types of events.


5. Define a state.


6. Distinguish a state from an event.


7. Explain state transitions.


8. Identify initial and final states.


9. Explain guards and transition conditions.


10. Explain entry, exit and activity behaviour.


11. Define an operation.


12. Distinguish an operation from an event.


13. Explain how operations can cause changes in an object's state.


14. Construct a UML state-machine diagram.


15. Explain concurrency.


16. Distinguish sequential behaviour from concurrent behaviour.


17. Model concurrent states.


18. Explain the relationship between class/structural models and dynamic models.


19. Identify which class or object a dynamic model describes.


20. Use a CASE tool to create and inspect dynamic models.




---

PART A — WHAT IS DYNAMIC MODELLING?

4. What Does "Dynamic" Mean?

The word dynamic means:

> Something that changes over time.



Think about a student registration system.

A student might initially be:

Not Registered

Then:

Student submits registration
        ↓
Registration Pending
        ↓
Payment confirmed
        ↓
Registered

The student has moved from one condition to another.

That changing behaviour is what dynamic modelling helps us describe.


---

5. Structural vs Dynamic Modelling

This distinction should be made extremely clear to students.

Structural modelling asks:

> What exists?



For example:

Student
Course
Lecturer
Registration
Payment

and:

Student ─── registers ─── Course

This describes the structure.


---

Dynamic modelling asks:

> What happens?



For example:

Student selects course
        ↓
Registration submitted
        ↓
Payment made
        ↓
Registration confirmed

This describes behaviour over time.


---

Simple comparison

Structural modelling	Dynamic modelling

What exists?	What happens?
Classes	Events
Attributes	States
Associations	Transitions
Operations	Behaviour
Static relationships	Changes over time


UML's formal specification explicitly describes behavioural semantics in terms of behaviour and state changes built upon the structural model. 


---

6. A Simple Analogy for Students

Imagine a car.

A structural model might tell us:

Car
----------------
registrationNo
model
colour
----------------
start()
stop()
accelerate()
brake()

That tells us what a Car is.

But it doesn't tell us what happens when someone starts it.

Dynamic modelling could show:

Off
 ↓
Start button pressed
 ↓
Starting
 ↓
Running

Then:

Running
 ↓
Brake pressed
 ↓
Stopped

So:

> Structural model = the car's design/parts.



> Dynamic model = how the car behaves as events occur.




---

PART B — EVENTS

7. What Is an Event?

An event is something that occurs and can cause a change in behaviour or state.

In simple English:

> An event is something that happens to which the system can respond.



Examples:

User clicks Login
Customer places Order
ATM card inserted
Payment received
Temperature exceeds limit
Student submits assignment

These are all events.


---

8. Real-Life Example of Events

Consider an ATM.

Possible events include:

Card inserted
PIN entered
Withdrawal requested
Cash dispensed
Card removed

The ATM responds differently depending on what happens.

For example:

Idle
  |
  | Card inserted
  ↓
Card Inserted
  |
  | PIN entered
  ↓
Authenticating

The words:

Card inserted
PIN entered

represent events.


---

9. Events Are Not States

This is a common student mistake.

Event

Something that happens.

Example:

> Customer clicks "Pay".



State

A condition that exists for some period of time.

Example:

> Payment Pending.



So:

EVENT:
Customer clicks Pay
        ↓
STATE:
Payment Pending

Remember:

> Event = something happens.



> State = something is/exists.




---

10. Examples of Events

User-generated events

Click Login
Submit Form
Press Cancel
Select Product
Upload File

System-generated events

Timer expires
Backup completed
Session timeout

External events

Payment gateway sends confirmation
Bank sends transaction response
Sensor detects movement

Data-related events

Payment received
Stock reaches zero
Account balance falls below threshold


---

11. Event and Transition

An event can trigger a transition.

For example:

[Locked]
    |
    | Correct PIN
    ↓
[Unlocked]

Here:

Locked       = state
Correct PIN  = event/trigger
Unlocked     = state

The event causes the object to move from one state to another.


---

PART C — STATES

12. What Is a State?

A state represents a condition or situation in which an object exists during some period of its behaviour.

For example, an order can be:

Pending
Paid
Processing
Shipped
Delivered
Cancelled

These are states of an Order.


---

13. Order Example

Imagine ordering a phone online.

The order might follow:

Payment received
Pending ───────────────────────→ Paid
                                  |
                                  | Warehouse starts processing
                                  ↓
                              Processing
                                  |
                                  | Item dispatched
                                  ↓
                               Shipped
                                  |
                                  | Courier delivers
                                  ↓
                              Delivered

The order changes state as events occur.


---

14. UML State Diagram

A simplified state-machine diagram can look like:

●
        |
        ↓
   [Pending]
        |
        | payment received
        ↓
     [Paid]
        |
        | process order
        ↓
 [Processing]
        |
        | dispatch
        ↓
   [Shipped]
        |
        | delivered
        ↓
  [Delivered]
        |
        ↓
        ◎

Where:

● = initial pseudostate
◎ = final state
[State] = state
arrow = transition
text on arrow = trigger/event


---

15. Initial State

The black filled circle:

●

represents the starting point of a state machine.

For example:

●
↓
Pending

This means:

> The object begins its lifecycle in the Pending state.




---

16. Final State

A final state is represented by a circle with an inner filled circle:

◎

For example:

Delivered
    |
    ↓
    ◎

This represents the end of the relevant state-machine behaviour.


---

17. State Transition

A transition describes movement from one state to another.

For example:

Pending ─────payment received────→ Paid

Here:

Pending = source state
Paid = target state
payment received = trigger/event

The UML specification defines state-machine execution in terms of transitions between active state configurations in response to event occurrences matching transition triggers. 


---

18. Guards

Sometimes an event alone isn't enough.

The system may need a condition.

For example:

Payment Submitted
        |
        | payment received [amount >= total]
        ↓
      Paid

The part:

[amount >= total]

is a guard condition.

It means:

> The transition can happen only if this condition is true.




---

19. Example: ATM Withdrawal

Suppose:

Card Inserted
       ↓
PIN Verified
       |
       | Withdraw requested
       ↓
Withdrawal Requested

Now there are two possible outcomes:

Withdrawal Requested
       |
       | [balance sufficient]
       ↓
Cash Dispensed

or:

Withdrawal Requested
       |
       | [balance insufficient]
       ↓
Insufficient Funds

The conditions in brackets are guards.


---

20. Multiple Transitions from One State

One state can have several possible transitions.

For example:

┌─── [payment successful] ──→ Paid
                |
Payment Pending ┤
                |
                └─── [payment failed] ─────→ Payment Failed

The system chooses the appropriate path based on the event and condition.


---

21. Entry Behaviour

A state can have behaviour that occurs when the state is entered.

For example:

[Payment Confirmed]
entry / sendConfirmationEmail()

Meaning:

> When the object enters Payment Confirmed, send a confirmation email.




---

22. Exit Behaviour

A state can also have behaviour that occurs when it leaves.

For example:

[Payment Confirmed]
exit / updateTransactionLog()

Meaning:

> When the object leaves this state, update the transaction log.




---

23. Do Activity

A state can also have behaviour that occurs while the object remains in the state.

For example:

[Processing]
do / processOrder()

This is different from an instantaneous transition trigger.

The UML specification recognizes entry, exit and do-activity behaviours associated with states. 


---

24. Complete State Example

Consider an online payment.

●
                   |
                   ↓
              [Pending]
                   |
                   | submitPayment()
                   ↓
             [Processing]
             /           \
            /             \
 [payment successful]   [payment failed]
          ↓                   ↓
       [Paid]              [Failed]
          |                   |
          ↓                   ↓
          ◎                   ◎

Students should be able to read this as a story:

> The payment begins in Pending. The customer submits payment. The system enters Processing. If payment succeeds, the payment becomes Paid. If payment fails, it becomes Failed.



That is dynamic modelling.


---

PART D — OPERATIONS

25. What Is an Operation?

An operation is a service or behaviour that an object/class provides.

In a class model, we might have:

Order
-----------------------
orderID
total
status
-----------------------
calculateTotal()
submitOrder()
cancelOrder()

The operations describe what the object can do.


---

26. Operation vs Event

Students often confuse these.

Operation

Something the object can perform or provide.

Example:

calculateTotal()

Event

Something that occurs and can trigger behaviour.

Example:

PaymentReceived

So:

Event → something happens

Operation → behaviour/service that can be invoked


---

27. Operation Causing State Change

Consider an ATM.

ATM
---------------------
insertCard()
enterPIN()
withdrawCash()
ejectCard()

When the user invokes:

insertCard()

the ATM can move:

Idle
 ↓
Card Inserted

When:

ejectCard()

occurs:

Card Inserted
 ↓
Idle

Thus, operations can participate in the object's dynamic behaviour.


---

28. Operation in a State Transition

A transition can be represented conceptually as:

Pending
   |
   | submitOrder()
   ↓
Processing

Here:

submitOrder()

can represent an operation/message that causes the transition.

Students should understand that UML's behavioural semantics provide mechanisms for modelling event-driven behaviour, while actions represent fine-grained behaviour. 


---

PART E — CONCURRENCY

29. What Is Concurrency?

This is one of the more difficult Week 7 concepts.

Concurrency means that multiple activities or behaviours can be occurring during the same period rather than strictly one after another.

Think about ordering food using a mobile application.

After placing an order:

Restaurant prepares food
        +
Driver is assigned
        +
Payment is processed

These activities may overlap.

They don't necessarily have to happen strictly like:

Prepare food
     ↓
Assign driver
     ↓
Process payment

Instead, some activities can occur concurrently.


---

30. Sequential vs Concurrent Behaviour

Sequential

One thing happens after another:

A
↓
B
↓
C

Example:

Enter PIN
↓
Validate PIN
↓
Display account


---

Concurrent

Two or more activities can occur in parallel:

┌──→ A ──→┐
Start ──┤          ├──→ Finish
        └──→ B ──→┘

For example:

Order Placed
      |
      ├──── Process Payment
      |
      └──── Prepare Order

Both may proceed independently.


---

31. Real-Life Example: Airport

When a passenger checks in:

Check-in
   |
   ├── Security Screening
   |
   └── Baggage Processing

Security screening and baggage processing can happen concurrently.

Eventually:

Security complete
       +
Baggage processed
       ↓
Ready for Boarding


---

32. UML Concurrent Regions

A UML composite state can contain concurrent regions.

Conceptually:

[Order Processing]
              /              \
             /                \
            ↓                  ↓
     [Payment]             [Delivery]
        |                      |
     Processing             Preparing
        |                      |
       Paid                  Dispatched
            \                /
             \              /
              ↓            ↓
              [Completed]

The two regions can execute concurrently.

The UML specification's behavioural model includes state machines and supports composite states with behavioural structure; the broader UML behavioural semantics are explicitly event-driven/discrete. 


---

33. Why Concurrency Matters

Modern systems frequently perform multiple activities simultaneously.

Examples:

Banking

Update account
+
Send notification
+
Record audit log

E-commerce

Process payment
+
Update inventory
+
Send order confirmation

Social media

Save post
+
Update feed
+
Send notification

Mobile application

Download data
+
Display interface
+
Monitor notifications

Therefore, analysts need to understand behaviour that is not purely sequential.


---

PART F — RELATIONSHIP BETWEEN STRUCTURAL AND DYNAMIC MODELS

34. Why Do We Need Both?

Imagine we create a class:

Order
-----------------------
orderID
status
total
-----------------------
submit()
cancel()
pay()
ship()

This tells us the structure.

But it doesn't fully tell us:

> What sequence of behaviour is allowed?



For example:

Can an order go directly from:

Pending → Shipped

without payment?

Probably not.

The dynamic model can make such rules visible.


---

35. Structural Model

The structural model might say:

Customer ───── places ───── Order

and:

Order ◆──── OrderItem

This tells us what exists and how things are related.


---

36. Dynamic Model

The dynamic model might say:

Pending
   |
   | PaymentReceived
   ↓
Paid
   |
   | WarehouseDispatch
   ↓
Shipped
   |
   | DeliveryConfirmed
   ↓
Delivered

Now we know how the Order behaves.


---

37. The Two Models Complement Each Other

Think of it this way:

STRUCTURAL MODEL
"What is the system made of?"
             +
DYNAMIC MODEL
"How does the system behave?"
             ↓
COMPLETE UNDERSTANDING

Neither model should be viewed as automatically replacing the other.


---

38. Example: ATM System

Structural model

ATM
-----------------
location
status
-----------------
insertCard()
validatePIN()
withdraw()
ejectCard()

Customer ─── uses ─── ATM

Dynamic model

Idle
 ↓
Card Inserted
 ↓
PIN Verification
 ↓
Authenticated
 ↓
Transaction
 ↓
Card Ejected
 ↓
Idle

Now we understand both:

WHAT EXISTS

and:

HOW IT BEHAVES


---

39. Why Dynamic Models Can Reveal Problems

Suppose an analyst models:

Order

with:

cancelOrder()

But the dynamic model reveals:

Delivered
   |
   | cancelOrder()
   ↓
Cancelled

That may not make business sense.

A delivered order probably shouldn't be cancellable.

So the dynamic model can expose requirements problems.

Perhaps the correct rule is:

Pending ───── cancel ───→ Cancelled
Paid ───────── cancel ───→ Cancelled
Processing ─── cancel ───→ Cancelled
Shipped ────── cancel ───→ Return Process
Delivered ──── cancel ───→ Return Process

This is an important reason analysts model behaviour.


---

PART G — CASE TOOL SUPPORT

40. What Is a CASE Tool?

CASE stands for:

> Computer-Aided Software Engineering.



A CASE tool provides software support for analysis, modelling, design and/or development activities.

For OOAD, CASE tools can help analysts create:

class diagrams;

state-machine diagrams;

activity diagrams;

sequence diagrams;

use-case diagrams;

package diagrams;

other UML artefacts.



---

41. Why Use a CASE Tool?

Imagine drawing this manually:

30 classes
15 associations
10 states
20 transitions

Then the lecturer says:

> "Change Customer to User."



Manually updating everything can become difficult.

A CASE tool can make model editing much easier.


---

42. Examples of CASE/UML Tools

Examples students may encounter include:

Enterprise Architect;

Visual Paradigm;

IBM Rational tools;

StarUML;

PlantUML;

diagrams.net/draw.io for diagramming.


For this module, the course outline specifically mentions:

> CASE Tool: Select Enterprise Demonstration



and earlier references Enterprise.

Therefore, students should receive practical exposure to the selected CASE environment used by the university/lecturer.


---

43. What Students Should Do in the CASE Tool

Students should be able to:

1. Create a project.


2. Create a UML model.


3. Create a state-machine diagram.


4. Add an initial state.


5. Add states.


6. Add transitions.


7. Add event/trigger labels.


8. Add guard conditions.


9. Add entry/exit behaviour where appropriate.


10. Add final states.


11. Save the model.


12. Modify the model when requirements change.




---

PART H — COMPLETE EXAMPLE

44. Hospital Patient Dynamic Model

Let's model a patient appointment.

Possible states:

Appointment Requested
Confirmed
Checked In
Waiting
With Doctor
Completed
Cancelled

Possible events:

requestAppointment
confirmAppointment
patientArrives
doctorCallsPatient
consultationComplete
cancelAppointment


---

45. State Diagram

●
                         |
                         ↓
              [Appointment Requested]
                         |
                         | confirmAppointment
                         ↓
                    [Confirmed]
                     /         \
                    /           \
       patientArrives          cancelAppointment
                  ↓                    ↓
             [Checked In]        [Cancelled]
                  |
                  | joinQueue
                  ↓
               [Waiting]
                  |
                  | doctorCallsPatient
                  ↓
             [With Doctor]
                  |
                  | consultationComplete
                  ↓
              [Completed]
                  |
                  ↓
                  ◎


---

46. Reading the Diagram as a Story

This is something I strongly recommend you make students do.

Don't just ask them to draw arrows.

Ask:

> "Tell me what this diagram says in English."



A student should be able to say:

> An appointment begins in the Appointment Requested state. When the appointment is confirmed, it moves to Confirmed. When the patient arrives, it moves to Checked In. The patient then waits until the doctor calls them. The appointment enters With Doctor. When the consultation finishes, the appointment becomes Completed. Alternatively, the appointment can be cancelled before completion.



If they cannot explain the diagram in words, they probably don't understand the model.


---

47. Add Guards

Suppose the hospital requires confirmation.

We could model:

Requested
    |
    | confirmAppointment [doctor available]
    ↓
Confirmed

But:

Requested
    |
    | confirmAppointment [doctor unavailable]
    ↓
Waitlisted

Now the model represents business rules.


---

48. Add Operations

Our Appointment class might be:

Appointment
--------------------------------
appointmentID
date
time
status
--------------------------------
request()
confirm()
cancel()
checkIn()
complete()

The dynamic model explains when these behaviours are allowed.

For example:

Requested
   |
   | confirm()
   ↓
Confirmed

but:

Completed
   |
   | confirm()
   ↓
???

There should probably be no such transition.


---

PART I — STATE VS CLASS VS OBJECT

49. Another Important Distinction

Students sometimes confuse:

Class
Object
State
Event

Let's separate them.

Class

A blueprint/type.

Order

Object

A specific instance.

order1024

State

The condition of that object.

Paid

Event

Something that happens.

PaymentReceived

So:

Class:
Order

Object:
order1024

Current State:
Paid

Event:
ShipmentDispatched

Then:

Paid
  |
  | ShipmentDispatched
  ↓
Shipped

This distinction is extremely important.


---

50. State Belongs to an Object

For example:

Order #1001 → Paid
Order #1002 → Pending
Order #1003 → Shipped

All three are objects of the same class:

Order

but they can be in different states.

Therefore:

> A state describes the current condition of an object during its lifecycle.




---

PART J — STATE MACHINE VS FLOWCHART

51. Are They the Same?

No.

Students often say:

> "A state diagram is just a flowchart."



That is not accurate.

A flowchart primarily represents procedural flow.

A state machine focuses on:

> The states of an entity and the transitions between those states in response to events.



For example:

Flowchart thinking

Calculate total
↓
Check payment
↓
Print receipt

State-machine thinking

Pending
   |
PaymentReceived
   ↓
Paid
   |
Dispatched
   ↓
Shipped

The second focuses on the lifecycle/state of the object.


---

52. When Should We Use Dynamic Modelling?

Dynamic modelling is especially useful when an object:

has several meaningful states;

changes state during its lifecycle;

responds to events;

has business rules governing transitions;

interacts with external events;

has concurrent behaviour;

has complex workflows.


Examples:

Order
BankAccount
ATM
TrafficLight
PatientAppointment
LoanApplication
Booking
InsuranceClaim
StudentRegistration


---

PART K — TRAFFIC LIGHT EXAMPLE

53. A Very Simple State Machine

Consider a traffic light.

States:

Red
Yellow
Green

Events/timers cause transitions.

●
        |
        ↓
      [Red]
        |
        | timer expires
        ↓
     [Green]
        |
        | timer expires
        ↓
     [Yellow]
        |
        | timer expires
        ↓
      [Red]

This is an excellent example for beginners because the states are obvious.


---

54. Adding Concurrency

Now imagine a modern traffic intersection.

One traffic light controls:

North/South

while another controls:

East/West

Their behaviour must coordinate.

Conceptually:

Intersection
      |
      ├── North/South Controller
      |
      └── East/West Controller

The system may have concurrent state-machine regions whose transitions must be coordinated safely.

This shows why concurrency becomes important in real systems.


---

PART L — WEEK 7 PRACTICAL

55. Practical Exercise: Online Shopping Order

Students should create a UML state-machine diagram for:

> Online Shopping Order



Required states

New
Pending Payment
Paid
Processing
Shipped
Delivered
Cancelled
Returned

Required events

placeOrder
makePayment
paymentConfirmed
dispatchOrder
deliverOrder
cancelOrder
requestReturn
approveReturn


---

56. Suggested Student Model

●
                           |
                           ↓
                         [New]
                           |
                           | placeOrder
                           ↓
                    [Pending Payment]
                           |
                           | paymentConfirmed
                           ↓
                         [Paid]
                           |
                           | processOrder
                           ↓
                      [Processing]
                       /          \
                      /            \
              dispatchOrder      cancelOrder
                    ↓                ↓
                [Shipped]       [Cancelled]
                    |
                    | deliverOrder
                    ↓
                [Delivered]
                    |
                    | requestReturn
                    ↓
                [Returned]
                    |
                    ↓
                    ◎

Students should add guards where appropriate.

For example:

requestReturn [within return period]


---

57. Practical Extension

Add:

entry / sendNotification()

to:

Paid

and:

entry / notifyCustomer()

to:

Shipped

Then ask students:

> What happens when the object enters each state?



This tests whether they understand entry behaviour rather than merely copying symbols.


---

PART M — TUTORIAL QUESTIONS

58. Tutorial Activity 1

Scenario

A bank account can be:

Active
Blocked
Closed

The following events occur:

login
wrongPIN
blockAccount
unblockAccount
closeAccount

Ask students to:

1. Identify the states.


2. Identify the events.


3. Draw the state machine.


4. Add suitable guards.


5. Identify which transitions should not be allowed.




---

59. Tutorial Activity 2

Ask:

> What is the difference between an event and a state?



Expected answer:

> An event is something that occurs and may trigger behaviour, while a state represents a condition in which an object exists for some period.




---

60. Tutorial Activity 3

Ask:

> Why is a class diagram alone insufficient for modelling a complex Order object?



Expected answer:

> Because the class diagram shows the Order's structural characteristics and relationships but does not adequately describe the sequence of states and events through which the Order passes during its lifecycle.




---

PART N — COMMON STUDENT MISTAKES

61. Mistake 1: Treating an Event as a State

Wrong:

[PaymentReceived]

if "PaymentReceived" is being used as an instantaneous event.

Better:

Pending
   |
   | PaymentReceived
   ↓
Paid


---

62. Mistake 2: Confusing an Operation with a State

Wrong:

[ProcessPayment]

if processPayment() is actually an operation.

Better:

[Pending]
    |
    | processPayment()
    ↓
[Processing]


---

63. Mistake 3: Forgetting the Object Being Modelled

A state-machine diagram should have a clear context.

For example:

> Order State Machine



rather than producing a collection of random states.

Ask:

> "Whose state are we describing?"



Possible answers:

Order
Payment
StudentRegistration
ATM
PatientAppointment


---

64. Mistake 4: Creating Impossible Transitions

For example:

Delivered → Paid

may make no sense for a particular system.

Students must use domain requirements, not simply draw arrows between every state.


---

65. Mistake 5: Creating a State for Every Small Action

Not every action is a state.

For example:

Click Button

is normally an event.

Whereas:

Processing

can be a meaningful state.


---

PART O — EXAMINATION-STYLE QUESTIONS

66. Question 1 — Definitions

Define:

a. Dynamic modelling
b. Event
c. State
d. Transition
e. Guard condition
f. Operation
g. Concurrency

[14 marks]


---

67. Question 2 — Difference

Explain the difference between:

a. Event and state
b. Operation and event
c. Structural model and dynamic model
d. Sequential and concurrent behaviour

[16 marks]


---

68. Question 3 — State Machine

A university student registration can move through:

Not Registered
Registration Pending
Payment Pending
Registered
Cancelled

Events include:

submitRegistration
makePayment
paymentConfirmed
cancelRegistration

Required:

Draw an appropriate UML state-machine diagram.

[15 marks]


---

69. Question 4 — Analysis

Explain why dynamic modelling is important when analysing:

> An online banking system



Your answer should include at least four examples of objects whose states change over time.

[10 marks]


---

70. Question 5 — Concurrency

A food delivery application performs the following after an order is placed:

payment processing;

restaurant order preparation;

driver assignment;

customer notification.


Explain which activities could potentially occur concurrently and why.

[10 marks]


---

PART P — WEEK 7 INDEPENDENT LEARNING

Students should use their 10 independent-learning hours as follows.

Activity 1 — State machine

Create a state machine for:

> ATM withdrawal



Minimum:

7 states;

6 events;

2 guards;

initial state;

final state.



---

Activity 2 — Dynamic analysis

Choose one:

hospital appointment;

university registration;

bank account;

online shopping;

hotel booking.


Identify:

10 events
10 states
5 operations
5 possible transitions
3 guard conditions


---

Activity 3 — Structural + Dynamic Model

For the same system, create:

1. a class diagram; and


2. a state-machine diagram.



Then write 500–700 words explaining how the two models complement each other.


---

Activity 4 — CASE Tool

Recreate your model using the selected CASE tool.

Students should submit:

1. Class diagram
2. State-machine diagram
3. Written explanation
4. CASE-tool project/model


---

PART Q — QUICK REVISION TABLE

Concept	Simple meaning	Example

Dynamic modelling	Modelling behaviour/change over time	Order lifecycle
Event	Something that happens	Payment received
State	Condition of an object	Paid
Transition	Movement between states	Pending → Paid
Guard	Condition controlling transition	[payment valid]
Operation	Behaviour/service provided by an object	cancelOrder()
Initial state	Starting point	●
Final state	End point	◎
Entry behaviour	Action when entering state	sendEmail()
Exit behaviour	Action when leaving state	logExit()
Concurrency	Activities occurring in parallel/overlapping	Payment + order preparation
Structural model	What exists	Classes and relationships
Dynamic model	What happens	States and transitions
CASE tool	Software supporting modelling	Enterprise Architect



---

71. The Most Important Conceptual Picture for Week 7

I would encourage students to remember this:

OBJECT
                      |
                      ↓
             has a CURRENT STATE
                      |
                      ↓
                ┌───────────┐
                │  Pending  │
                └───────────┘
                      |
                  EVENT OCCURS
                      |
                      ↓
                ┌───────────┐
                │    Paid   │
                └───────────┘
                      |
                  EVENT OCCURS
                      |
                      ↓
                ┌───────────┐
                │  Shipped  │
                └───────────┘

The fundamental story is:

> An object exists → it is in a state → an event occurs → a transition happens → the object enters another state.



That is the heart of dynamic modelling.


---

72. Week 7 Summary

By the end of Week 7, students should understand that OOAD is not only about identifying classes.

We need to understand how those objects behave.

The complete picture is:

STRUCTURAL MODELLING
        ↓
What objects/classes exist?
        ↓
What attributes do they have?
        ↓
How are they related?
        ↓
        +
DYNAMIC MODELLING
        ↓
What states can objects have?
        ↓
What events occur?
        ↓
What operations can be performed?
        ↓
What transitions happen?
        ↓
What conditions control transitions?
        ↓
Can activities occur concurrently?
        ↓
COMPLETE OBJECT-ORIENTED MODEL

The official UML specification describes state machines as behavioural modelling constructs and defines behaviour in terms of event-driven changes between states/configurations. 

The four questions students should ask

Whenever they encounter a dynamic-modelling problem, ask:

1. What object am I modelling?

Order?
Payment?
ATM?
Student registration?

2. What states can that object be in?

Pending?
Paid?
Cancelled?
Completed?

3. What events cause it to change?

PaymentReceived
CancelRequested
DeliveryConfirmed

4. What conditions determine which transition occurs?

[payment successful]
[balance sufficient]
[within return period]

If students can answer those four questions, they are already thinking like object-oriented analysts.


---

References

Authoritative UML Reference

Object Management Group (OMG). (2017). OMG Unified Modeling Language (OMG UML), Version 2.5.1. OMG. The OMG specification remains the formal reference for UML 2.5.1 and includes the structural and behavioural semantic foundations used in this week's material. 

[Official OMG UML 2.5.1 Specification](https://www.omg.org/spec/UML/2.5.1/?utm_source=chatgpt.com)

Additional UML/State-Machine Reference

Object Management Group. OMG UML 2.5.1 — State Machines and Behavioural Semantics. The specification covers states, transitions, events, behaviours and related state-machine concepts. 

Prescribed texts from the module outline

Mach, E. (2019). Object Oriented Analysis & Design Cookbook: Introduction to Practical System Modeling.

Reddy, V., & Korra, S. (2018). Object-Oriented Analysis and Design Using UML.

The Art of Service. (2021). Object Oriented Analysis and Design: A Complete Guide.


Recommended texts

Wixom, B., & Dennis, A. (2018). Systems Analysis and Design.

Blokdyk, G. (2021). Object-Oriented Analysis and Design Standard Requirements.

Wixom, B., & Dennis, A. (2020). Systems Analysis and Design: An Object-Oriented Approach with UML.


Next: Week 8 — Object-Oriented Analysis: Behavioural Modelling, covering Use Cases, Use Case Diagrams, Interaction Diagrams, Sequence Diagrams, Collaboration/Communication Diagrams, Activity Diagrams, and Full Analysis Documentation.
