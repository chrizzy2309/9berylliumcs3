## ACTIVITY 2:
### This activity will help you test your understanding of duck-typing: polymorphism without inheritance.

### —-------------

## Instruction: Do what is asked in each item below:
### __1. Answer the following questions:__
###  a. What is duck typing, as explained in the video?
###   - It is a way to achieve polymorphism in Python without requiring objects to belong to the same inheritance hierarchy. In the video it was explained by "If it looks  like a duck and quacks like a duck it must be a duck" which means that an object can be used as a particular type if it provides attributes and methods that the code needs. In short focuses on what an object can do, rater than on the object's exact class.
###  b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
###   - 

### 2. Create the Python code that:
### a. Creates three classes: Car, Boat, and Drone with a method move().
### move() in the Car class prints "The car drives on the road."
### move() in the Boat class prints "The boat sails on water."
### move() in the Drone class prints "The drone flies in the sky."
### b. Has a function named start_trip(vehicle), with a parameter vehicle, that simply calls the move() method: vehicle.move().
### c. Creates one object of each class.
### d. Calls the start_trip() method for each object.
### 3. How does the code in 2.2 demonstrate polymorphism?
