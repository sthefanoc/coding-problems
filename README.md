# Coding problems solved using Python

This is a repository filled with coding problems from [DailyCodingProblem](https://www.dailycodingproblem.com/) and [LeetCode](https://leetcode.com/).

## Problems List

| Source               | Company       | Difficulty | Problem                                                | Status     | Solution                                                  |
| -------------------- | ------------- | ---------- | ------------------------------------------------------ | ---------- | --------------------------------------------------------- |
| _DailyCodingProblem_ | `Google`      | EASY       | **[#001: Two numbers on list add to k](#Problem-001)** | _SOLVED_   | [SOLUTION](DailyCodingProblem/2020-12-17-solution.py)     |
| _DailyCodingProblem_ | `Uber`        | HARD       | **[#002: Dynamic product array](#Problem-002)**        | _SOLVED_   | [SOLUTION](DailyCodingProblem/2020-12-18-solution.py)     |
| _DailyCodingProblem_ | `Google`      | MEDIUM     | **[#003: Binary Tree Serializing](#Problem-003)**      | _UNSOLVED_ | ~~SOLUTION~~                                              |
| _DailyCodingProblem_ | `Stripe`      | HARD       | **[#004: Fist Missing Positive](#Problem-004)**        | _SOLVED_   | [SOLUTION](DailyCodingProblem/2020-12-20-solution.py)     |
| _DailyCodingProblem_ | `Jane Street` | MEDIUM     | **[#005: Nested functions return](#Problem-005)**      | _UNSOLVED_ | ~~[SOLUTION](DailyCodingProblem/2020-12-21-solution.py)~~ |
| _DailyCodingProblem_ | `Google`      | HARD       | **[#006: XOR Linked List](#Problem-006)**              | _UNSOLVED_ | ~~[SOLUTION](DailyCodingProblem/2020-12-22-solution.py)~~ |

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
[SOLUTION](DailyCodingProblem/2020-12-17-solution.py).

_[back to list](#Problems-List)_

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
[SOLUTION](DailyCodingProblem/2020-12-18-solution.py).

_[back to list](#Problems-List)_

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
~~SOLUTION.~~

_[back to list](#Problems-List)_

---

## Problem 004

### First Missing Positive

_Date: 2020-12-20_<br/>
_Asked by **Stripe**_<br/>
**[Hard]**

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

**Status:** SOLVED.
[SOLUTION](DailyCodingProblem/2020-12-20-solution.py).

_[back to list](#Problems-List)_

---

## Problem 005

### Nested functions return

_Date: 2020-12-21_<br/>
_Asked by **Jane Street**_<br/>
**[Medium]**

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

```python
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```

Implement car and cdr.

**Status:** UNSOLVED.
~~[SOLUTION.](DailyCodingProblem/2020-12-21-solution.py)~~

_[back to list](#Problems-List)_

---

## Problem 006

### XOR Linked List

_Date: 2020-12-22_<br/>
_Asked by **Google**_<br/>
**[Hard]**

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

**Status:** UNSOLVED.
~~[SOLUTION.](DailyCodingProblem/2020-12-22-solution.py)~~

_[back to list](#Problems-List)_

---
