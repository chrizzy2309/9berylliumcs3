# Class Attributes and Methods
---

## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)

---

## Design Revision
No major changes were needed from my original design.

---

## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| Name | String | Public | Because there is no direct danger from sharing this info publicly. |
| Nation/Area | String | Private | Because they can easily identified if the nation they live in said. |
| Elemental Vision | String | Public | Because the elements of teyvat are equal with each other the thing that factors in is the experience of the person. |
| Weapon | String | Public | Because the weapons are basically useless against fights with other people visions are more commonly used against other vision holders. |

---

## Updated UML Class Diagram
[Class Diagram](https://github.com/chrizzy2309/9berylliumcs3/blob/q1/images/UpdatedUMLClassDiagram.md)

---

## Python Implementation

[View Python Source](classImplementation.py)

---

## Test Run
[Test Run](https://github.com/chrizzy2309/9berylliumcs3/blob/q1/images/testrun.md)

---

## Object Diagram
[Object Diagram](https://github.com/chrizzy2309/9berylliumcs3/blob/q1/images/objectDiagram.md)

---

## Analysis
### Why did you make your chosen attribute private?
#### - I made Nation private because it is sensitive information about the character.

### Which method changes the state of your object?
#### - The method that changes the state of object is edit method because it changes the information of the object

### How did your two objects demonstrate that instances are independent?
#### - The two objects are independent because when I changed the weapon used by character79 the weapon used by character110 didn't change.

### What is the difference between your class diagram and your object diagram?
#### - The class diagram is a blueprint while the object diagram has values.
