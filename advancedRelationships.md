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
[Inheritance](https://github.com/chrizzy2309/9berylliumcs3/blob/q1/images/inheritanceDiagram.md)

---

## Composition/Aggregation
### Relationship: Aggregation

### Explanation: The relationship between them is treated as aggregation because it has different lifecycle, if the character is removed the ModelType information is still retained  and is shared across many other characters. 

--- 

## Advanced UML Diagram
![Advanced UML](https://github.com/chrizzy2309/9berylliumcs3/blob/q1/images/AdvanceUMLDiagram.md)

---

## Python Implementation

### [Source Code ](https://github.com/chrizzy2309/9berylliumcs3/blob/q1/advancedRelationships.py)
--- 

## Test Run
[Test](https://github.com/chrizzy2309/9berylliumcs3/blob/q1/images/TestRunAR.md)

---

## Object Diagram
![Objects](https://github.com/chrizzy2309/9berylliumcs3/blob/q1/images/Screenshot%202026-10-01%20102212.png)

---

## Reflection
### Answers:
### 1. Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class.
### - I picked aggregation because a model type is a special asset component that can exist independently of a specific character. A model type is a type of character asset because it defines the 3D visual geometry and rendering data assigned to represent that character. 

### 2. How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
### - Inheritance reduces the code by allowing to inherit and retain the past code and reuse it without revision. All of the attributes were reused and one was added model_type. All the methods were inherited with no additions.

### 3. Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship between the two objects.
### It's aggregation because model type is a independent asset if the character is deleted the information is still retained.

### 4. What is the difference between Association from Part III and the advanced relationship you implemented?
### The difference between the two is in part three the information from the parent class is retained.

### 5. How does your design follow the DRY principle?
### My design follows the DRY principle because instead repeatedly changing the code for different situations it inherits the information is retained to avoid repetitions.
 
### LLM USED: Gemini Built in Google Search
