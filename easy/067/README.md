# 067. Add Binary

## Problem Link

[LeetCode — Add Binary](https://leetcode.com/problems/add-binary/)

## Difficulty

Easy

## Tags

Math, String, Bit Manipulation, Simulation

## Problem Description

Given two binary strings `a` and `b`, return their sum as a binary string. Each string contains only `0` and `1`, has length from 1 to 10,000, and has no leading zeroes except for the string `"0"` itself.

### Examples

| a | b | Output |
|---|---|---|
| `"11"` | `"1"` | `"100"` |
| `"1010"` | `"1011"` | `"10101"` |

## Solution Approach

My idea was to convert the binary strings to integers, add them, and convert the result back to a binary string.

1. `int(a, 2)` and `int(b, 2)` interpret the strings in base 2.
2. Add the two integer values.
3. `bin(add_ab)` converts the sum to a binary string with a `0b` prefix.
4. `[2:]` removes the prefix to produce the format required by LeetCode.

For example: `"1010"` → 10, `"1011"` → 11, then 10 + 11 = 21 → `"0b10101"` → `"10101"`.

An integer is a numeric value; decimal and binary are ways of representing that value. The intermediate values are Python integers, not decimal strings.

**Complexity:** O(m + n) time and O(m + n) space for binary conversion, arbitrary-precision addition, and output construction, where m and n are the input lengths. The built-in operations still process the input bits.

Python supports arbitrary-precision integers. Base-2 conversion is not subject to Python's decimal string conversion digit limit.

## Code Implementation

[solution_v1.py](solution_v1.py) — the author's accepted conversion approach.

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a = int(a, 2)
        num_b = int(b, 2)

        add_ab = num_a + num_b

        return bin(add_ab)[2:]
```

### Submission Record (October 11, 2026)

The supplied screenshot shows **Accepted — 296 / 296 test cases passed**.

| Runtime | Runtime beats | Memory | Memory beats |
|---|---|---|---|
| 0 ms | 100.00% | 19.46 MB | 17.73% |

Measurements vary between runs; 0 ms does not imply constant-time performance.

## Reflection and Takeaways

### 1. What does bin() do?

`bin()` is a Python built-in function that converts an integer into a binary **string**.

```python
bin(10)       # '0b1010'
bin(5)        # '0b101'
bin(21)       # '0b10101'
bin(0)        # '0b0'
type(bin(10)) # <class 'str'>
```

The returned string includes the `0b` prefix.

### 2. What is a prefix?

A prefix is a marker placed at the beginning of a representation. These prefixes identify the number base:

| Prefix | Base | Python integer literal | Decimal value |
|---|---|---|---|
| `0b` | Binary (base 2) | `0b1010` | 10 |
| `0o` | Octal (base 8) | `0o12` | 10 |
| `0x` | Hexadecimal (base 16) | `0xA` | 10 |

The prefix identifies the base; it is not one of the digits contributing to the value. All three literals above represent the same integer.

```python
0b1010 == 0o12 == 0xA == 10  # True

bin(10)  # '0b1010'
oct(10)  # '0o12'
hex(10)  # '0xa'
```

The functions return strings, whereas unquoted literals such as `0b1010` evaluate to integers.

### 3. Why use [2:]?

String indices start at 0. In `"0b1010"`, index 0 is `"0"`, index 1 is `"b"`, and index 2 is the first binary digit.

`[2:]` takes the substring from index 2 through the end:

```python
bin(10)       # '0b1010'
bin(10)[2:]   # '1010'
bin(0)[2:]    # '0'
```

LeetCode expects `"1010"`, so the `0b` prefix must be removed. This slicing works here because the inputs and their sum are nonnegative. For a negative number, `bin(-10)` returns `'-0b1010'`, so `[2:]` would not remove the full prefix correctly.

### 4. int() and bin() work in opposite directions

| Expression | Operation | Result type |
|---|---|---|
| `int("1010", 2)` | Interpret a binary string as an integer | `int` |
| `bin(10)` | Represent an integer as a binary string with a prefix | `str` |
| `bin(10)[2:]` | Remove the prefix from that binary string | `str` |

The second argument of `int()` specifies the base of the input string.

The same approach can be written in one line:

```python
return bin(int(a, 2) + int(b, 2))[2:]
```

The expanded version makes the conversion and addition steps easier to inspect.
