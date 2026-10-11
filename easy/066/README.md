# 066. Plus One

## Problem Link

[LeetCode — Plus One](https://leetcode.com/problems/plus-one/)

## Difficulty

Easy

## Tags

Array, Math

## Problem Description

A nonnegative integer is represented as an array of decimal digits, ordered from most significant to least significant. Add one and return the resulting array of digits. The input has no leading zeroes.

### Examples

| Input | Output |
|---|---|
| `[1,2,3]` | `[1,2,4]` |
| `[1,2,9,9]` | `[1,3,0,0]` |
| `[9,9,9]` | `[1,0,0,0]` |

## Solution Approach

### Approach 1 (v1): Right-to-left carry propagation

This file preserves the author's accepted implementation, including its explicit second `if` statement.

1. Iterate from the least significant digit to the most significant.
2. If the current digit is not 9, increase it by one and immediately `return digits`. Returning exits the entire function and ends the carry propagation.
3. If it is 9, change it to 0 and move left, implicitly carrying one.
4. If every digit was 9, the loop finishes with all zeroes; return `[1] + digits` to represent the new leading digit.

The second `if digits[i] == 9` can be omitted because reaching it means the earlier branch did not return; the explicit version is retained for learning purposes.

**Complexity:** O(n) time in the worst case and O(1) auxiliary space, excluding the newly allocated result for the all-nines case.

### Approach 2 (v2): Convert, increment, convert back

1. `map(str, digits)` converts each digit to a string.
2. `"".join(...)` joins the digit strings with no separator.
3. `int(...)` creates the corresponding Python integer; add one.
4. `list(map(int, str(num)))` converts the incremented integer back into individual digits.

**Complexity:** The conversions require at least O(n) work and O(n) additional storage. Arbitrary-precision integer conversion and arithmetic costs can depend on n. Python 3.11+ may impose a default decimal digit string conversion limit (normally 4300 digits), so this approach is less robust for extremely large input than v1.

### Submission Record (October 10, 2026)

Both versions passed **114 / 114** test cases in the supplied screenshots.

| Version | Runtime | Runtime beats | Memory | Memory beats |
|---|---|---|---|---|
| v1 | 0 ms | 100.00% | 19.30 MB | 19.99% |
| v2 | 0 ms | 100.00% | 19.17 MB | 88.46% |

LeetCode measurements vary between runs; `0 ms` does not imply constant-time performance.

## Code Implementation

- [solution_v1.py](solution_v1.py) — accepted right-to-left carry algorithm.
- [solution_v2.py](solution_v2.py) — accepted integer conversion algorithm.

## Reflection and Takeaways

A fixed solution that checks only the final or penultimate digit fails on a longer run of 9s. A backward loop generalizes the carry to any number of digits. `return` inside the loop exits the function, so the first non-9 digit is incremented exactly once. `[1] + digits` creates a new list rather than mutating `digits`. The conversion alternative illustrates `map`, `join`, `str`, and `int` but delegates carry to Python's integer arithmetic.
