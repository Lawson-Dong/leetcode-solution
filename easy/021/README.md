# 021. Merge Two Sorted Lists

## Problem Link

[LeetCode — Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

## Difficulty

Easy

## Tags

Linked List, Recursion

## Problem Description

Given the heads of two non-decreasing sorted singly linked lists, merge them into one sorted list by linking together the existing nodes. Return the head of the merged list.

### Examples

| list1 | list2 | Merged |
|---|---|---|
| `[1,2,4]` | `[1,3,4]` | `[1,1,2,3,4,4]` |
| `[]` | `[]` | `[]` |
| `[]` | `[0]` | `[0]` |

## Solution Approach

### Approach 1 (v1): Iterative Merge with Head and Three Moving Pointers

This version preserves the author's accepted solution and original English comments.

1. If either input head is `None`, return the other head.
2. Compare the initial node values and store the smaller head as `head`, the start of the merged list.
3. Initialize `p` at `head`. Pointers `p1` and `p2` track the unprocessed portions of the two input lists.
4. While both input pointers are non-null, connect the smaller current node to `p.next`, advance its input pointer, and then advance `p`.
5. When one list is exhausted, attach the remaining linked nodes from the other list directly.
6. Return `head`.

The key distinction is between **rewiring** a node (`p.next = p1` or `p.next = p2`) and **moving** a variable (`p = p.next`). Because a node already links to its successors, attaching the remaining head attaches the entire suffix.

The algorithm reuses original nodes instead of allocating new list nodes.

### Submission Record

The supplied screenshot shows an accepted Python submission on October 9, 2026:

| Version | Test Cases Passed | Runtime | Runtime Beats | Memory | Memory Beats |
|---|---|---|---|---|---|
| v1 | 208 / 208 | 0 ms | 100.00% | 19.28 MB | 73.98% |

These figures describe one submission and can vary across runs. A reported `0 ms` is a timer measurement, not constant-time complexity.

## Complexity Analysis

Let `m` and `n` be the lengths of the two input lists.

| Version | Time Complexity | Auxiliary Space |
|---|---|---|
| v1 | O(m + n) | O(1) |

Each iteration consumes one node from one of the lists, so at most `m + n` nodes are processed. The algorithm uses a fixed number of node references and reuses the existing links.

## Code Implementation

- [solution_v1.py](solution_v1.py): The original accepted iterative solution.

## Reflection and Takeaways

The difference between a node reference and its stored value matters: `list1` refers to the head node, while `list1.val` is just the data in that node. Keeping `head` fixed preserves the entry to the merged list; moving `p` extends its processed prefix. Input pointers advance independently so that each next candidate remains accessible.
