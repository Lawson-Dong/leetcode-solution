# 001. Two Sum

## 🔗 Problem Link

[LeetCode — Two Sum](https://leetcode.com/problems/two-sum/)

## 🏷️ Difficulty

Easy

## 🏷️ Tags

Array, Hash Table

## 📝 Problem Description

Given an integer array `nums` and an integer `target`, return the indices
of two distinct elements whose sum equals `target`.

Each input has exactly one valid solution. You cannot use the same
element twice, and you may return the indices in either order.

### Examples

| Input | Target | Output |
|---|---|---|
| `[2, 7, 11, 15]` | `9` | `[0, 1]` |
| `[3, 2, 4]` | `6` | `[1, 2]` |
| `[3, 3]` | `6` | `[0, 1]` |

## 💡 Solution Approach

### Approach 1 (v1): One-Pass Hash Table

The submitted solution uses a dictionary to store previously visited
numbers and their indices.

For each number, compute its complement:

`complement = target - current_num`

1. Check whether the complement exists in the dictionary.
2. If it exists, return its stored index and the current index.
3. Otherwise, store the current number and its index.

Check for the complement **before** storing the current number.
This ensures that the returned indices are distinct and correctly
handles duplicates such as `[3, 3]` with a target of `6`.

### Walkthrough

For `nums = [2, 7, 11, 15]` and `target = 9`:

- At index `0`, the number is `2`, and its complement is `7`.
  The dictionary is empty, so store `{2: 0}`.
- At index `1`, the number is `7`, and its complement is `2`.
  The dictionary contains `2` at index `0`, so return `[0, 1]`.

### Why It Works

Before processing each element, the dictionary contains only numbers
from earlier indices.

If the complement is found, the earlier number and the current number
sum to the target and occupy different positions.

For the valid pair, the first element is stored before the second is
processed. Therefore, the pair will be found.

This approach already achieves optimal expected linear time.
No separate optimization version is needed.

## 📊 Complexity Analysis

Let `n` be the length of `nums`.

| Version | Time Complexity | Auxiliary Space |
|---|---|---|
| v1 | O(n) expected | O(n) |

Dictionary lookup and insertion take O(1) on average. The algorithm
visits each element at most once and stores at most `n` entries.

## 💻 Code Implementation

- [solution_v1.py](solution_v1.py): One-pass hash table based on the
  submitted solution, with clearer variable names and comments.

## 🧠 Reflection and Takeaways

<!-- TODO: Add personal reflections and takeaways. -->
