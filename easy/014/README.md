# 014. Longest Common Prefix

## Problem Link

[LeetCode — Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

## Difficulty

Easy

## Tags

String, Trie

## Problem Description

Given a list of strings, return the longest prefix shared by every string.
Return `""` when no nonempty common prefix exists.

### Examples

| Input | Output | Explanation |
|---|---|---|
| `["flower", "flow", "flight"]` | `"fl"` | Every string begins with "fl". |
| `["dog", "racecar", "car"]` | `""` | The first characters already differ. |
| `["ab", "a"]` | `"a"` | The shorter string limits the common prefix. |
| `["", "abc"]` | `""` | An empty string has no nonempty prefix. |

## Solution Approach

### Approach 1 (v1): Vertical Scanning

This version records the accepted implementation in the supplied screenshot.

1. Return an empty string if the input list is empty.
2. Use the first string as the reference.
3. At each character position `i`, compare the reference character with
   the character at the same position in every other string.
4. If another string has ended or its character differs, return
   `strs[0][:i]`.
5. If all positions in the reference string match, return that string.

Before checking position `i`, every earlier position has matched across
all strings. Therefore, a mismatch or an ended string proves that the
prefix cannot extend beyond `i`.

Python evaluates `or` from left to right and short-circuits. The length
check `i >= len(strs[j])` therefore prevents an out-of-range character
access in `strs[j][i]`.

For `["flower", "flow", "flight"]`, positions 0 and 1 match. At position 2,
"o" differs from "i", so the method returns `"fl"`.

### Submission Record

The supplied screenshot shows an accepted Python 3 submission on
October 8, 2026:

| Version | Test Cases Passed | Runtime | Runtime Beats | Memory | Memory Beats |
|---|---|---|---|---|---|
| v1 | 126 / 126 | 0 ms | 100.00% | 19.21 MB | 73.80% |

These are measurements from one submission. A reported `0 ms` does not
mean constant-time execution; percentiles can vary between submissions.

## Complexity Analysis

Let `n` be the number of strings, `m` the length of the first string,
and `p` the length of the returned common prefix.

| Version | Time Complexity | Auxiliary Space | Output Space |
|---|---|---|---|
| v1 | O(nm) | O(1) | O(p) when slicing |

- At most `m` character positions are checked across `n - 1` other strings.
  The method usually stops earlier at the first mismatch or ended string.
- Only indices and a reference character are stored during scanning.
- A sliced result can allocate O(p) space and take O(p) time. Returning
  the original first string reuses that string rather than copying it.

## Code Implementation

- [solution_v1.py](solution_v1.py): Vertical scanning, preserving the
  submitted algorithm and LeetCode method name.

## Reflection and Takeaways

*To be added by the author.*
