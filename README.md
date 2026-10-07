# LeetCode Solutions

Personal LeetCode practice by [Lawson Dong](https://github.com/Lawson-Dong), documenting algorithmic reasoning, Python implementations, and learning progress.

## Progress

| Easy | Medium | Hard | Total |
|---|---|---|---|
| 1 | 0 | 0 | 1 |

## Problem Index

| # | Problem | Difficulty | Topics | Approach | Expected Time | Space | Notes | Code |
|---|---|---|---|---|---|---|---|---|
| 001 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Array, Hash Table | One-pass hash table | O(n) | O(n) | [README](easy/001/README.md) | [Python](easy/001/solution_v1.py) |

## Repository Structure

```text
.
├── easy/
│   └── 001/
│       ├── README.md
│       └── solution_v1.py
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
