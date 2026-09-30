# Advanced Class Relationships

---

## Previous Activities
### - [classAttrib](https://github.com/chrizzy2309/9berylliumcs3/blob/fe20162b253c31d3b9b65b46cce4aa180e3d1bf0/OOPAct2/classAttributesMethods.md)

### - [classRel]( https://github.com/chrizzy2309/9berylliumcs3/blob/65555761a9bd9a5c11ac49ecb0e2fa93e12dd8e5/classRelationships.md )

---

## Existing System Description:
### 1. What classes currently exist in your system?
### Class 1: GENSHIN IMPACT CHARACTERS
### Class 2: NATION

### 2. What problem or limitation exists in your current design?
### &nbsp;- The limitation of the current design is that it can let incorrect info pass by without confirming if the info's right. For example Zibai's info is inputed she is a a geo vision wielder but in the info inputted her vision is shown to be pyro. The system didn't double check it just let it slide.

---

## Inheritance Relationship
### Parent: GenshinImpactCharacters
### Child: MODEL TYPE
### Explanation: ModelType is a child class of GenshinImpactCharacters because it represents a  subset that inherits common traits while introducin new specific behaviors and attributes.

---

## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)

---

## Composition/Aggregation
### Relationship: Aggregation

### Explanation: The relationship between them is treated as aggregation because it has different lifecycle, if the character is removed the ModelType information is still retained  and is shared across many other characters. 

--- 

## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)

---

## Python Implementation
[Source Code](advancedRelationships.py)
--- 

## Test Run
![Test](images/advancedTestRun.png)

---

## Object Diagram
![Objects](images/advancedObjectDiagram.png)

---

## Reflection
### Answers:
### 1. Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class.
### 2. How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
### 3. Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship between the two objects.
### 4. What is the difference between Association from Part III and the advanced relationship you implemented?
### 5. How does your design follow the DRY principle?

### LLM USED: Gemini Built in Google Search
