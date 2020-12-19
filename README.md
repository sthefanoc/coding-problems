# Coding problems solved using Python

This is a repository filled with coding problems from [DailyCodingProblem](https://www.dailycodingproblem.com/) and [LeetCode](https://leetcode.com/).

Below, the list of solved problems.

| Source               | Company  | Difficulty | Problem                                                | Status   | Solution                                              |
| -------------------- | -------- | ---------- | ------------------------------------------------------ | -------- | ----------------------------------------------------- |
| _DailyCodingProblem_ | `Google` | EASY       | **[#001: Two numbers on list add to k](#Problem-001)** | _SOLVED_ | [SOLUTION](DailyCodingProblem/2020-12-18-solution.py) |
| _DailyCodingProblem_ | `Uber`   | HARD       | **[#002: Dynamic product array](#Problem-002)**        | _SOLVED_ | [SOLUTION](DailyCodingProblem/2020-12-19-solution.py) |
| _DailyCodingProblem_ | `Google` | MEDIUM     | **[#003: Binary Tree Serializing](#Problem-003)**      | _SOLVED_ | SOLUTION                                              |

# DAILY CODING PROBLEM

---

## Problem 001

### Two numbers on list add to k

_Date: 2020-12-17_<br/>
_Asked by **Google**_<br/>
**[Easy]**

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

_Bonus:_ Can you do this in one pass?

**Status:** SOLVED.
[SOLUTION](DailyCodingProblem/2020-12-18-solution.py).

---

## Problem 002

### Dynamic product array

_Date: 2020-12-18_<br/>
_Asked by **Uber**_<br/>
**[Hard]**

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

_Follow-up:_ what if you can't use division?

**Status:** SOLVED.
[SOLUTION](DailyCodingProblem/2020-12-19-solution.py).

---

## Problem 003

### Binary Tree Serializing

_Date: 2020-12-19_<br/>
_Asked by **Google**_<br/>
**[Medium]**

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```

**Status:** UNSOLVED.
SOLUTION.

---
