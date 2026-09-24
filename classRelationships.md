# Class Relationships: Association and Multiplicity

---

## Previous Work
### [Part I - Classes and Objects](https://github.com/chrizzy2309/9berylliumcs3/blob/q1/classObjectUML.md)
### [Part II - Class Attributes and Methods](https://github.com/chrizzy2309/9berylliumcs3/tree/q1/OOPAct2)

---

## Existing Class
### Class: GENSHIN IMPACT CHARACTER LIST EDITOR

### Description: The class is a editable list of characters that you add in genshin impact. The remaining attributes that are still useful are Name, elemental vision, and  weapon type. While all methods from the previous activities are still used these methods are ADD(), REMOVE(), EDIT(), and SHOW().

---

## New Related Class
### Class: Nation
### Description: The NATION have character and those characters have  different information like their name, the weapon type they use, and the elemental vision they have.

---

## Association
### Relationship:
## Nations HAVE Characters

### Explanation: The class Nation is composed of characters which are individuals the class just collects the info and puts it into different nations. Which makes the information easier to show, find, and edit.

---

## Multiplicity

### Multiplicity: NATION ───────── *Character

### Explanation: Because nations contain many characters and aren't limited to one. And the nation class can store different characters. That allows the class to organize the characters under a nation.

---

## UML Class Relationship Diagram
![Class Relationship Diagram](https://github.com/chrizzy2309/9berylliumcs3/blob/q1/images/classRelationshipDiagram.md)

---

## Python Implementation
[View Python Source](classRelationships.py)

---

## Test Run
![Relationship Test Run](https://github.com/chrizzy2309/9berylliumcs3/blob/q1/images/relationshipTestRun.md)

---

## Object Relationship Diagram
![Object Relationship Diagram](https://github.com/chrizzy2309/9berylliumcs3/blob/q1/images/ObjectRelationshipDiagram.md)

---

## Analysis
### What is the association between your two classes?
### - The association between my two classes are Nations Have characters.

### What multiplicity did you choose and why?
### - The multiplicity that I chose is one is too many because a nation contains many characters and the different characters have different 

### How did you implement the relationship in Python?
### - I created a list that stores the characters info then created an add function to add the characters in the list to create an established connection.

### Why did you store an object reference instead of copying its data?
### - I store an object reference because it can enable shared data and a change made at one point immediately updates the data for every other part which uses the same object.


### If your relationship uses many, why is a list appropriate?
### - A list is appropriate because it stores the information so that it's organized and makes finding info easier.
