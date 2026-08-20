# Computational Thinking Exercise
## [Smart School Canteen Queue]
---
#**Name:** Chris Deniel 

#**Section:** 9 - Beryllium

#**Last Name:** Baldoza

#**Date:** August 20, 2026

---

## Step 1: Identify the Big Problem
### Main Problem

The PSHS Canteen's process is extremely slow because of the manual processes, including order preparation,
the cashier operation, and the system for tracking the food running out.
---
## Step 2: Identify the Sub-Problems
1. Slow ordering process
2. No proper tracking of food running out
3. Manual and error frequent cashier calculations
4. Long lines during peak hours
---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| Slow ordering process | Decomposition | Build a menu in python using using functions to separate menu browsing, item selection, and check out  |
| No proper tracking of food running out | Abstraction | Develop a program to that creates a list of stock levels and trigger a automatic visual response when count hits zero. |
| Manual and error frequent cashier calculations | Pattern recognition | Write a program that calculates subtotal and change due automatically |

---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
The sub-problem I selected is "No proper tracking of food running out".

---
### Pseudocode

START 

1. Create a list of stock.
2. Create a function to sell an item.
3. Check if the item is in stock.
4. Check if the item is in subtract the sold amount from the total stock.
5. Show an out of stock message if the stock hits zero.
6. Show a low stock message if three or fewer items are remaining.
7. Show an error message if the item does not exist.
8. Create a function to show the current inventory.
9. Print every item and its remaining stock count.
    
END
