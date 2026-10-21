# 002. Add Two Numbers

## Problem Link

[LeetCode — Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

## Difficulty

Medium

## Tags

Linked List, Math, Recursion

## Problem Description

Two non-empty singly linked lists represent two non-negative integers. Each node contains one digit, and digits are stored in **reverse order** (least significant digit first). Add the two numbers and return their sum as a linked list in the same order.

### Examples

| l1 | l2 | Output |
|---|---|---|
| `[2,4,3]` | `[5,6,4]` | `[7,0,8]` |
| `[0]` | `[0]` | `[0]` |
| `[9,9]` | `[1]` | `[0,0,1]` |

## Solution Approach

### Approach 1 (v1): Digit-by-Digit Addition with Carry and a Dummy Head (Accepted)

Because digits are reversed, both input heads represent the ones place. We can add the numbers directly, one position at a time, without converting the lists into integers.

1. Initialize `p1 = l1` and `p2 = l2` to traverse the two input lists, plus `carry = 0`.
2. Create `dummy = ListNode(0)` as a placeholder head, and set `current = dummy` to build the answer.
3. Continue while either list still has nodes **or** there is a remaining carry: `while p1 or p2 or carry:`.
4. Read each current digit. If one list is exhausted, treat that digit as `0`.
5. Compute `total = val_1 + val_2 + carry`. The old carry must be included **before** calculating the new carry.
6. Compute `carry = total // 10` and `digit = total % 10`, then advance each input pointer if it exists.
7. Append a fresh node with `current.next = ListNode(digit)` and move the output pointer with `current = current.next`.
8. Return `dummy.next` to skip the placeholder and expose the complete result list.

### Why a Dummy Head?

`dummy = ListNode(0)` allocates a *placeholder node*, not the first result digit. Initially, `current = dummy` points to that placeholder. The first loop iteration connects the real first digit to `dummy.next`.

The placeholder avoids a special case for creating the first output node. Returning `dummy.next` returns a reference to the first real node, from which all subsequent nodes are accessible through `.next`.

### Why Does the Loop Include `or carry`?

The final addition may overflow into a new highest digit. For instance, `[9,9]` (99) plus `[1]` (1) produces `[0,0,1]` (100). After both input pointers reach `None`, `carry = 1` keeps the loop running for one final digit.

### Pointer Movement vs. Appending Nodes

```python
p1 = p1.next                       # Move along an existing input list
current.next = ListNode(digit)    # Create and attach an output node
current = current.next             # Move to the output node just appended
```

Merely accessing `p1.next` does not change `p1`. Likewise, assigning `current = current.next` moves the reference; the preceding `current.next = ...` is what changes the linked-list structure.

### Trace: `[2,4,3] + [5,6,4]`

| Place | Input digits | Incoming carry | Total | Output digit | New carry |
|---|---|---|---|---|---|
| Ones | 2 + 5 | 0 | 7 | 7 | 0 |
| Tens | 4 + 6 | 0 | 10 | 0 | 1 |
| Hundreds | 3 + 4 | 1 | 8 | 8 | 0 |

The output chain is `7 → 0 → 8`, representing the sum `807` in reverse digit order.

## Complexity Analysis

Let `m` and `n` be the numbers of nodes in the input lists.

| Version | Time Complexity | Auxiliary Space | Output Space |
|---|---|---|---|
| v1 | O(max(m, n)) | O(1) | O(max(m, n)) |

We process one pair of digit positions per iteration, possibly followed by a final carry. A constant number of references and numeric variables are used, while the newly allocated result list takes linear space.

## Submission Record

The supplied screenshot shows an accepted Python 3 submission on **October 20, 2026**:

| Version | Test Cases Passed | Runtime | Runtime Beats | Memory | Memory Beats |
|---|---|---|---|---|---|
| v1 | 1569 / 1569 | 2 ms | 72.41% | 19.04 MB | 98.95% |

These are measurements from one LeetCode submission, not asymptotic performance guarantees.

## Edge Cases

- One list is shorter: its missing digits contribute `0`.
- A final carry remains: the condition `or carry` adds the new most significant digit.
- No carry is generated: the loop finishes when both lists are exhausted.
- Inputs `[0]` and `[0]`: output is a single node with value `0`.

## Code Implementation

- [solution_v1.py](solution_v1.py): Original accepted iterative solution using two input pointers, carry, and a dummy head.

## Reflection and Takeaways

A dummy head simplifies the first insertion. Keep the input pointers separate from the output pointer, distinguish **link creation** from **pointer movement**, and use `while p1 or p2 or carry` to cover lists of different lengths and a final carry.
