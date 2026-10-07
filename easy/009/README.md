# 009. Palindrome Number

## Problem Link

[LeetCode — Palindrome Number](https://leetcode.com/problems/palindrome-number/)

## Difficulty

Easy

## Tags

Math, String

## Problem Description

Given an integer `x`, return `True` if its decimal representation reads
the same forward and backward; otherwise, return `False`.

The input is a signed 32-bit integer: `-2**31 <= x <= 2**31 - 1`.

### Examples

| Input | Output | Explanation |
|---|---|---|
| `121` | `True` | The digits are identical in both directions. |
| `-121` | `False` | Reversing the representation moves the minus sign. |
| `10` | `False` | A nonzero number ending in zero cannot be a palindrome. |
| `0` | `True` | A single digit is a palindrome. |

## Solution Approach

### Approach 1 (v1): Explicit Digit Reversal

This version records the original submitted approach.

1. Reject negative numbers and nonzero numbers ending in zero.
2. Convert `x` to a string, then to a list of digit characters.
3. Iterate over the list in reverse order and append each character
   to a new list.
4. Join the reversed characters into a string.
5. Convert that string back to an integer and compare it with `x`.

For `121`, the reversed characters produce `"121"`, which becomes
the integer `121`. The comparison returns `True`.

The trailing-zero check rejects an impossible case early: a nonzero
number ending in zero cannot begin with zero. It is optional for
correctness in both versions. For example, reversing `10` produces
`"01"`, which becomes `1`; the final comparison would still be false.
The exception for `0` preserves its valid palindrome status.

### Approach 2 (v2): String Slicing

This version records the shorter solution shown in the screenshots.

1. Apply the same early rejection checks.
2. Convert `x` to a string.
3. Compare it directly with its reverse, `x_str[::-1]`.

In Python, a slice with a step of `-1` creates a reversed copy of the
string. String equality compares the characters in order, so equality
holds exactly when the number is a palindrome.

**Optimization:** Remove the two character lists, the explicit append
loop, the join operation, and conversion back to an integer.
Both versions still have the same asymptotic time and space complexity.

The trailing-zero check is optional for direct string comparison,
but is retained to match the submitted solution and reject the case early.

### Submission Record

The supplied screenshots show these accepted Python 3 submissions:

| Version | Test Cases Passed | Runtime | Memory |
|---|---|---|---|
| v1 | 11,513 / 11,513 | 15 ms | 19.24 MB |
| v2 | 11,513 / 11,513 | 0 ms | 19.36 MB |

These are measurements from individual submissions. A reported
`0 ms` does not mean constant-time execution, and runtime percentiles
are not a substitute for complexity analysis.

## Complexity Analysis

Let `n` be the number of decimal digits in the input.

| Version | Time Complexity | Auxiliary Space |
|---|---|---|
| v1 | O(n) | O(n) |
| v2 | O(n) | O(n) |

- **v1:** String conversion, list construction, reversal, joining,
  integer parsing, and comparison take O(n) time overall under the
  bounded integer constraints. The strings and lists require O(n) space.
- **v2:** String conversion, reversed slicing, and comparison take O(n)
  time. The original string and reversed copy require O(n) space.

Both versions use strings. The no-string follow-up would require
a separate arithmetic approach.

## Code Implementation

- [solution_v1.py](solution_v1.py): Explicit digit reversal based on
  the original submission, with clearer comments and a direct Boolean return.
- [solution_v2.py](solution_v2.py): Optimized string-slicing implementation
  based on the later submission.

## Reflection and Takeaways

In my v2 submission, the reported runtime beat 100% of submissions,
while memory usage beat only 19.07%. This prompted me to think about
the **time–space trade-off** in computer science.

- The solution creates a string with `str(x)` and a reversed copy
  with `[::-1]`. These allocations require O(n) auxiliary space,
  where n is the number of digits.
- String slicing replaces the explicit reversal loop with a built-in
  operation and removes several intermediate conversions, making
  the implementation simpler and potentially faster in practice.
- An arithmetic approach could avoid these string allocations and
  use O(1) auxiliary space under the fixed-width integer model.

However, the submission percentiles alone do not establish a
time–space trade-off between v1 and v2. Both versions use O(n) space,
and v1 also creates intermediate lists and strings. Individual
benchmark results can vary.

In many applications, spending a modest amount of memory to reduce
response time is a worthwhile choice. The decision should depend
on input size, memory limits, and measured performance. My takeaway
is to balance speed, memory usage, and readability rather than
optimize for a single benchmark percentile.
