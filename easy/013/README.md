# 013. Roman to Integer

## Problem Link

[LeetCode — Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

## Difficulty

Easy

## Tags

Hash Table, Math, String

## Problem Description

Convert a valid Roman numeral string `s` to an integer.

| Symbol | Value |
|---|---|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

Symbols are normally added. In the subtractive pairs `IV`, `IX`,
`XL`, `XC`, `CD`, and `CM`, the smaller symbol is subtracted
from the larger symbol that follows it.

The input is guaranteed to be a valid Roman numeral representing
an integer from 1 to 3999, with `1 <= len(s) <= 15`.

### Examples

| Input | Output | Explanation |
|---|---|---|
| `"III"` | `3` | 1 + 1 + 1 |
| `"LVIII"` | `58` | 50 + 5 + 1 + 1 + 1 |
| `"MCMXCIV"` | `1994` | 1000 + 900 + 90 + 4 |

## Solution Approach

### Approach 1 (v1): Compare Adjacent Symbols

This version records the submitted approach shown in the screenshot.

1. Store the seven symbol values in a dictionary.
2. Scan every symbol except the last one.
3. If the current value is smaller than the next value, subtract it.
4. Otherwise, add the current value.
5. Add the final symbol separately and return the total.

For `"MCMXCIV"`, the contributions are
`1000 - 100 + 1000 - 10 + 100 - 1 + 5 = 1994`.

The loop stops before the final character so that `s[i + 1]` stays
within bounds. Adding the last symbol separately also handles a
single-character input: the loop runs zero times.

### Submission Record

The supplied screenshot shows an accepted Python 3 submission on
October 7, 2026.

| Version | Test Cases Passed | Runtime | Runtime Beats | Memory | Memory Beats |
|---|---|---|---|---|---|
| v1 | 3,999 / 3,999 | 6 ms | 46.56% | 19.26 MB | 59.61% |

These measurements describe the individual submission shown in the screenshot.

## Complexity Analysis

Let `n` be the number of characters in `s`.

| Version | Time Complexity | Auxiliary Space |
|---|---|---|
| v1 | O(n) | O(1) |

Each character is processed once with constant-time dictionary lookups.
The dictionary always contains seven entries, and the remaining variables
use constant space.

## Code Implementation

- [solution_v1.py](solution_v1.py): Adjacent-symbol comparison based on the
  submitted solution, with formatting and English comments.

## Validation

Checked all 3,999 canonical Roman numerals representing integers from
1 to 3999, including single symbols and every subtractive pair.

## Reflection and Takeaways

Reserved for personal notes.
