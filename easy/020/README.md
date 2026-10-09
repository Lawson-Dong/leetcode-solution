# 020. Valid Parentheses

## Problem Link

[LeetCode — Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

## Difficulty

Easy

## Tags

String, Stack

## Problem Description

Given a string containing only `(`, `)`, `[`, `]`, `{`, and `}`,
determine whether every opening bracket is closed by a bracket of the
same type in the correct order.

### Examples

| Input | Output | Explanation |
|---|---|---|
| `"()"` | `True` | The brackets match. |
| `"()[]{}"` | `True` | Each consecutive pair matches. |
| `"([])"` | `True` | Nested brackets close in reverse opening order. |
| `"(]"` | `False` | The bracket types differ. |
| `"([)]"` | `False` | The closing order is incorrect. |
| `"("` | `False` | An opening bracket remains unmatched. |

## Solution Approach

### Approach 1 (v1): Stack with a Closing-to-Opening Map

This version preserves the accepted implementation from the supplied
screenshot.

1. Start with an empty stack.
2. Store each closing bracket's matching opening bracket in `pairs`.
3. Push opening brackets onto the stack.
4. For a closing bracket, return `False` if the stack is empty or its
   top does not match the required opening bracket.
5. Otherwise, pop that matching opening bracket.
6. After scanning the string, return `True` only if the stack is empty.

The stack stores unmatched opening brackets in their original order.
A closing bracket must match the most recently opened unmatched bracket,
which is the top of the stack. This last-in, first-out behavior enforces
correct nesting.

For `"([])"`, the stack evolves as follows:

| Character | Action | Stack After Action |
|---|---|---|
| `(` | Push | `['(']` |
| `[` | Push | `['(', '[']` |
| `]` | Match and pop `[` | `['(']` |
| `)` | Match and pop `(` | `[]` |

For `"([)]"`, `)` encounters `[` at the stack top, so the method
returns `False`.

Python short-circuits `or`: when `not stack` is true, it does not
evaluate `stack[-1]`. This prevents access to an empty stack.
The opening-bracket branch relies on the problem's bracket-only input
constraint.

### Submission Record

The supplied screenshot shows an accepted Python 3 submission on
October 8, 2026:

| Version | Test Cases Passed | Runtime | Runtime Beats | Memory | Memory Beats |
|---|---|---|---|---|---|
| v1 | 103 / 103 | 0 ms | 100.00% | 19.16 MB | 91.62% |

These are measurements from one submission. A reported `0 ms` does not
mean constant-time execution; percentiles can vary between submissions.

## Complexity Analysis

Let `n` be the number of characters in the input string.

| Version | Time Complexity | Auxiliary Space |
|---|---|---|
| v1 | O(n) | O(n) |

- Each character is visited once. Dictionary lookups use a fixed
  three-entry map, while list append and end-pop operations take
  amortized O(1) time.
- The stack may store all `n` characters when every bracket is an
  opening bracket. The matching map requires O(1) space.

## Code Implementation

- [solution_v1.py](solution_v1.py): The submitted stack-based
  implementation, preserving the LeetCode method name and control flow.

## Reflection and Takeaways

*To be added by the author.*
