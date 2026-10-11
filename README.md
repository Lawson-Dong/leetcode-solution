# LeetCode Solutions

Personal LeetCode practice by [Lawson Dong](https://github.com/Lawson-Dong), documenting algorithmic reasoning, Python implementations, and learning progress.

## Progress

| Easy | Medium | Hard | Total |
|---|---|---|---|
| 8 | 0 | 0 | 8 |

## Problem Index

| # | Problem | Difficulty | Topics | Approach | Expected Time | Space | Notes | Code |
|---|---|---|---|---|---|---|---|---|
| 001 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Array, Hash Table | One-pass hash table | O(n) | O(n) | [README](easy/001/README.md) | [Python](easy/001/solution_v1.py) |
| 009 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | Easy | Math, String | Explicit reversal (v1); string slicing (v2) | O(n) | O(n) | [README](easy/009/README.md) | [v1](easy/009/solution_v1.py), [v2](easy/009/solution_v2.py) |
| 013 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | Easy | Hash Table, Math, String | Adjacent-symbol comparison | O(n) | O(1) | [README](easy/013/README.md) | [Python](easy/013/solution_v1.py) |
| 014 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | Easy | String, Trie | Vertical scanning | O(nm) | O(1) auxiliary; O(p) output | [README](easy/014/README.md) | [Python](easy/014/solution_v1.py) |
| 020 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | String, Stack | Stack with bracket matching map | O(n) | O(n) | [README](easy/020/README.md) | [Python](easy/020/solution_v1.py) |
| 066 | [Plus One](https://leetcode.com/problems/plus-one/) | Easy | Array, Math | Right-to-left carry (v1); integer conversion (v2) | O(n) for v1 | O(1) auxiliary for v1 | [README](easy/066/README.md) | [v1](easy/066/solution_v1.py), [v2](easy/066/solution_v2.py) |
| 021 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | Linked List, Recursion | Iterative pointer merge | O(m + n) | O(1) | [README](easy/021/README.md) | [Python](easy/021/solution_v1.py) |
| 069 | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) | Easy | Math, Binary Search | Linear search (v1); binary search (v2) | O(log(x + 1)) for v2 | O(1) | [README](easy/069/README.md) | [v1](easy/069/solution_v1.py), [v2](easy/069/solution_v2.py) |

Here, `n` denotes input length: the number of array elements for Two Sum, the number of decimal digits for Palindrome Number, and the number of Roman numeral characters for Roman to Integer, and the number of characters for Valid Parentheses. For Merge Two Sorted Lists, `m` and `n` are the input list lengths. For Longest Common Prefix, `n` is the number of strings, `m` is the length of the first string, and `p` is the returned prefix length.

## Repository Structure

```text
.
├── easy/
│   ├── 001/
│   │   ├── README.md
│   │   └── solution_v1.py
│   ├── 009/
│   │   ├── README.md
│   │   ├── solution_v1.py
│   │   └── solution_v2.py
│   ├── 013/
│   │   ├── README.md
│   │   └── solution_v1.py
│   ├── 014/
│   │   ├── README.md
│   │   └── solution_v1.py
│   ├── 020/
│   │   ├── README.md
│   │   └── solution_v1.py
│   ├── 021/
│   │   ├── README.md
│   │   └── solution_v1.py
│   ├── 066/
│   │   ├── README.md
│   │   ├── solution_v1.py
│   │   └── solution_v2.py
│   └── 069/
│       ├── README.md
│       ├── solution_v1.py
│       └── solution_v2.py
├── medium/
├── hard/
└── LICENSE
```

Problems are grouped by difficulty. Directory names use at least three digits, such as `001`, `009`, and `1000`. Each problem has its own README and one Python file per documented approach.

## Documentation Conventions

Each problem README contains:

- Problem number, title, and LeetCode link.
- Difficulty, tags, and a concise problem description.
- Explanation of each solution and its time and space complexity.
- Links to the corresponding implementations.
- A reflection section reserved for personal notes.

Solutions use Python 3, type hints, descriptive names, and English comments. LeetCode's required method names, such as `twoSum`, are preserved.

When a submitted solution is provided, v1 records its approach. Additional versions document distinct approaches or meaningful optimizations; an already optimal solution does not require a redundant v2.

## Running a Solution

Submit the relevant `solution_v*.py` file in LeetCode's Python 3 editor. Each file defines the standard `Solution` class; files do not include a command-line interface.

## Maintenance

When adding a problem:

1. Create `<difficulty>/<problem-number>/`.
2. Add the problem README and solution files.
3. Check the examples and relevant edge cases.
4. Update the problem index and difficulty counts.
5. Keep personal reflections as placeholders until supplied by the author.

## License

See [LICENSE](LICENSE).
