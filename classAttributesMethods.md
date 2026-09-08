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
![Class Diagram](<img width="1294" height="2000" alt="Baldoza_Floating In A Pool" src="https://github.com/user-attachments/assets/07ca9e56-df6a-4ab4-a1dd-3c864c6907d0" />)

---

## Python Implementation

[View Python Source](classImplementation.py)

---

## Test Run
![Test Run](images/classTestRun.png)

---

## Object Diagram
![Object Diagram](images/objectDiagram.png)

---

## Analysis
### Why did you make your chosen attribute private?
#### - 
### Which method changes the state of your object?

### How did your two objects demonstrate that instances are independent?

### What is the difference between your class diagram and your object diagram?
