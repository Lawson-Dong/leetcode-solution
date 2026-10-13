# 083. Remove Duplicates from Sorted List

## Problem Link

[LeetCode — Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

## Difficulty

Easy

## Tags

Linked List

## Problem Description

Given the head of a **sorted** singly linked list, remove duplicate values so that each value occurs once. Return the head of the resulting sorted list.

### Examples

| Input | Output |
|---|---|
| `[1,1,2]` | `[1,2]` |
| `[1,1,2,3,3]` | `[1,2,3]` |
| `[]` | `[]` |

## Solution Approach

### Approach 1 (v1): In-Place Pointer Traversal (Accepted)

Because the input list is sorted, all equal values appear in adjacent nodes. One moving reference, `pointer`, is enough.

1. Initialize `pointer = head`.
2. While both the current node and the next node exist, compare their `.val` fields.
3. If equal, remove the next node from the chain with `pointer.next = pointer.next.next`. **Do not advance `pointer`**, because there might be another duplicate immediately after it.
4. If different, advance with `pointer = pointer.next`.
5. Return the original `head` reference, which still points to the updated list.

### Why `while pointer and pointer.next`?

A comparison uses `pointer.next.val`, so both nodes must exist. Python's `and` short-circuits: if `pointer` is `None`, `pointer.next` is never evaluated.

This condition is equivalent here to:

```python
while pointer is not None and pointer.next is not None:
```

### Pointer Movement vs. Link Modification

These two operations have different effects:

```python
pointer = pointer.next           # Move the reference to the next node
pointer.next = pointer.next.next # Bypass the next node in the linked list
```

A linked list is **not** a Python `list`: its nodes are reached using `.next`, rather than `head[i]`. In Python, `pointer` is technically an object reference, commonly called a *pointer* in linked-list algorithms.

### Trace: `[1,1,1,2]`

| Step | Current pointer | Action | Remaining chain |
|---|---|---|---|
| Start | First `1` | Compare `1 == 1` | `1 → 1 → 1 → 2` |
| 1 | First `1` | Bypass the second `1`; stay on current | `1 → 1 → 2` |
| 2 | First `1` | Bypass the next `1`; stay on current | `1 → 2` |
| 3 | First `1` | Values differ; move to `2` | `1 → 2` |
| End | `2` | `pointer.next` is `None`; stop | `1 → 2` |

## Complexity Analysis

Let `n` be the number of nodes.

- **Time:** O(n). Each iteration removes a node or moves the pointer forward.
- **Auxiliary space:** O(1). The solution rewires existing nodes without allocating a second list.

## Submission Record

The provided screenshot shows an accepted Python 3 submission on **October 13, 2026**:

| Version | Test Cases Passed | Runtime | Runtime Beats | Memory | Memory Beats |
|---|---|---|---|---|---|
| v1 | 168 / 168 | 0 ms | 100.00% | 19.20 MB | 72.06% |

These are platform measurements for a single run; 0 ms does not imply constant-time complexity.

## Edge Cases

- `head = None`: the loop is skipped and `None` is returned.
- One node: no next node exists, so it is returned unchanged.
- All nodes equal: duplicates are repeatedly bypassed until one remains.
- All values distinct: the pointer simply walks to the tail.

## Code Implementation

- [solution_v1.py](solution_v1.py): Original accepted in-place pointer solution.

## Reflection and Takeaways

The central lesson is to distinguish a **node's value** (`.val`), its **link to the next node** (`.next`), and the **pointer/reference variable** itself. Bypassing a node changes the structure of the list; advancing a pointer only changes which node the variable refers to. Keep the original head for the return value.
