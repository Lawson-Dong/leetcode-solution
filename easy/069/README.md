# 69. Sqrt(x)

- **Difficulty:** Easy
- **Topics:** Math, Binary Search
- **Problem:** [LeetCode 69 — Sqrt(x)](https://leetcode.com/problems/sqrtx/)
- **Goal:** Given a non-negative integer `x`, return `floor(sqrt(x))` without using a built-in square-root or exponent operation.

## Approach 1: Linear Search

Start at `n = 0` and increment it while `n * n < x`. When the loop stops, `n` is the smallest integer whose square is at least `x`. Return `n` if it is an exact square root; otherwise return `n - 1`.

- **Time:** O(sqrt(x))
- **Extra space:** O(1)
- **Code:** [solution_v1.py](solution_v1.py)

A boundary-aware variation keeps `n` valid throughout the loop:

```python
n = 0
while (n + 1) * (n + 1) <= x:
    n += 1
return n
```

## Approach 2: Binary Search (Accepted)

[solution_v2.py](solution_v2.py)

**The pointers `left` and `right` define the current search interval `[left, right]`. This is a closed interval: both endpoints are included.**

At each iteration, calculate `mid = (left + right) // 2`.

- If `mid * mid == x`, return `mid` immediately.
- If `mid * mid < x`, discard `mid` and all smaller candidates: `left = mid + 1`.
- If `mid * mid > x`, discard `mid` and all larger candidates: `right = mid - 1`.

Using `+ 1` and `- 1` excludes the already-checked midpoint and guarantees progress for this inclusive-interval template.

### Example: x = 8

| Iteration | left (before) | right (before) | mid | Comparison | Update |
|---|---:|---:|---:|---|---|
| 1 | 0 | 8 | 4 | 16 > 8 | right = 3 |
| 2 | 0 | 3 | 1 | 1 < 8 | left = 2 |
| 3 | 2 | 3 | 2 | 4 < 8 | left = 3 |
| 4 | 3 | 3 | 3 | 9 > 8 | right = 2 |

The final state is `left = 3`, `right = 2`. The condition `left <= right` is false, so the loop terminates.

### Why return right?

**If an exact square root is found, `return mid` ends the function immediately. Otherwise, the loop terminates only when the search boundaries cross, with `left = right + 1`.**

At that point, `right` is the **largest integer whose square does not exceed `x`**, whereas `left` is the smallest integer whose square exceeds `x`:

```text
right * right <= x < left * left
```

Thus **`return right` is exactly the square root rounded down**. For `x = 8`, `right = 2`.

- **Time:** O(log(x + 1))
- **Extra space:** O(1)
- **LeetCode result:** Accepted, 1019/1019 tests (user's submission).

## Edge Cases

- `x = 0` returns `0`.
- `x = 1` returns `1`.
- `x = 4` returns `2` by the exact-match branch.
- `x = 8` returns `2` after the boundaries cross.

## Reflection

The main insight is that binary search repeatedly narrows an **inclusive search interval**, not just a pair of arbitrary pointers. The final `right` is an answer boundary when `x` is not a perfect square.
