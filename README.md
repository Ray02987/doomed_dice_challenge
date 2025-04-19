# doomed_dice_challenge

This repository contains my solution to the Doomed Dice Challenge problem.

## Problem Description
The challenge involves two parts:
1. Analyzing the probability distribution of two standard six-sided dice
2. Transforming the dice according to specific constraints while maintaining the same probability distribution

## Solution
The solution uses Python to analyze the original dice and find a transformation that satisfies the  constraints:
- Die A cannot have more than 4 spots on any face
- The probability distribution of sums must remain unchanged

The final transformation:
- Die A: [1, 2, 2, 3, 3, 4]
- Die B: [1, 3, 4, 5, 6, 8]

## Running the Code
To run the solution:
```python
python solution.py
