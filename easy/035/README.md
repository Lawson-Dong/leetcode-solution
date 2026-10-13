# 35. Search Insert Position

- **Difficulty:** Easy
- **Topics:** Array, Binary Search
- **Problem:** [LeetCode 35 — Search Insert Position](https://leetcode.com/problems/search-insert-position/)
- **Goal:** In a sorted array of distinct integers, return the index of `target` if present; otherwise return the index where it should be inserted to preserve ascending order.
- **Code:** [solution_v1.py](solution_v1.py) — accepted submission.

## Approach: Binary Search on a Closed Interval

The search interval is **`[left, right]`**, so both endpoints are included.

1. Start with `left = 0` and `right = len(nums) - 1`.
2. Compute `mid = (left + right) // 2`.
3. If `nums[mid] < target`, discard the midpoint and everything to its left: `left = mid + 1`.
4. If `nums[mid] == target`, return `mid`.
5. If `nums[mid] > target`, discard the midpoint and everything to its right: `right = mid - 1`.
6. If the value was not found, the boundaries eventually cross; return `left`.

The author's submitted version uses three separate `if` statements. They are correct here because the comparisons with the same `nums[mid]` are mutually exclusive. An `if / elif / else` chain would also work.

**Why `return left`?** At termination (`left > right`), `left` points immediately after all elements known to be smaller than `target`. It is therefore the insertion position, possibly `len(nums)` if the target is larger than every element.

## Learning Note: Check Boundaries With Concrete Examples

**A practical way to understand and debug an algorithm is to trace a small input step by step**, writing down `left`, `right`, `mid`, the comparison, and the updated boundary. Examples are especially useful for discovering **off-by-one errors** and invalid indexing. They help test behavior, although a few examples alone do not prove correctness for every input.

### Example A — Target absent, inserted in the middle

`nums = [1, 3, 5, 6]`, `target = 2`

| Iteration | left | right | mid | nums[mid] | Update |
|---|---:|---:|---:|---:|---|
| 1 | 0 | 3 | 1 | 3 | `3 > 2` → `right = 0` |
| 2 | 0 | 0 | 0 | 1 | `1 < 2` → `left = 1` |

Now `left = 1` and `right = 0`, so the loop stops. Return **1**, the insertion position between 1 and 3.

### Example B — Target smaller than every element

`nums = [1, 3, 5, 6]`, `target = 0`

| Iteration | left | right | mid | nums[mid] | Update |
|---|---:|---:|---:|---:|---|
| 1 | 0 | 3 | 1 | 3 | `right = 0` |
| 2 | 0 | 0 | 0 | 1 | `right = -1` |

`left = 0`, `right = -1`. Return **0**; the insertion position is at the beginning. Notice that `right = -1` does **not** access `nums[-1]`: the loop has already ended.

### Example C — Target larger than every element

`nums = [1, 3, 5, 6]`, `target = 7`

| Iteration | left | right | mid | nums[mid] | Update |
|---|---:|---:|---:|---:|---|
| 1 | 0 | 3 | 1 | 3 | `left = 2` |
| 2 | 2 | 3 | 2 | 5 | `left = 3` |
| 3 | 3 | 3 | 3 | 6 | `left = 4` |

`left = 4`, `right = 3`. Return **4 = len(nums)**, the insertion position after the last element. The algorithm never accesses `nums[4]` because it exits the loop first.

### More boundary checks

| nums | target | Expected index | Checks |
|---|---:|---:|---|
| `[1, 3, 5, 6]` | 5 | 2 | Existing value |
| `[1, 3, 5, 6]` | 2 | 1 | Missing value in the middle |
| `[1, 3, 5, 6]` | 0 | 0 | Insert before the first element |
| `[1, 3, 5, 6]` | 7 | 4 | Insert after the last element |
| `[1]` | 1 | 0 | One-element array, exact match |
| `[1]` | 0 | 0 | One-element array, before |
| `[1]` | 2 | 1 | One-element array, after |

The problem guarantees a nonempty array, but this particular implementation also returns `0` for `nums = []` without indexing into it.

### Common mistakes revealed by examples

- **Wrong right endpoint:** With `while left <= right`, initialize `right = len(nums) - 1`, not `len(nums)`; otherwise `mid` may become an invalid index.
- **Forgetting `+1` or `-1`:** The midpoint has already been checked. Keeping it in a closed search interval can cause an infinite loop.
- **Returning `right` instead of `left`:** Once the pointers cross, `right` is immediately *before* the insertion position.
- **Using `nums.index(target)`:** It works only for an existing value and has `O(n)` worst-case time, whereas the problem requires `O(log n)`.

## Complexity

- **Time:** `O(log n)`, because the search interval shrinks by approximately half each iteration.
- **Extra space:** `O(1)`, because only a fixed number of variables are used.

## Submission Record (October 12, 2026)

The supplied screenshot shows **Accepted — 68/68 test cases passed**, runtime **0 ms (beats 100.00%)**, and memory **19.96 MB (beats 45.05%)**. Runtime and percentile values vary between submissions; the asymptotic complexity remains `O(log n)`.

## Reflection

For problem solving, I find **example-driven boundary checks** particularly useful: trace the variables on typical inputs, then deliberately test the smallest inputs and both ends of the array. This makes the meaning of `return left` concrete and exposes off-by-one mistakes before relying on a formal argument.
