# Maximum Subarray

[LeetCode Problem Link](https://leetcode.com/problems/maximum-subarray/)

Given an integer array `nums`, find the subarray with the largest sum, and return *its sum*.

A **subarray** is a contiguous non-empty sequence of elements within an array.

---

## 1. Brute Force Approach

### Intuition
We can check the sum of every possible subarray. 
- Use three nested loops:
  - The first loop selects the starting index `i`.
  - The second loop selects the ending index `j`.
  - The third loop calculates the sum of elements from index `i` to `j`.
- Track the maximum sum found.

- **Time Complexity (TC)**: $\mathcal{O}(N^3)$
- **Space Complexity (SC)**: $\mathcal{O}(1)$

---

## 2. Better Approach (Optimized Brute Force)

### Intuition
We can eliminate the third loop by keeping a running sum. While iterating through the ending index `j` from `i` to `n-1`, we can simply add the current element `nums[j]` to the previous sum.

- **Time Complexity (TC)**: $\mathcal{O}(N^2)$
- **Space Complexity (SC)**: $\mathcal{O}(1)$

---

## 3. Optimal Approach (Kadane's Algorithm)

### Intuition
Kadane's Algorithm is a dynamic programming approach that finds the maximum subarray sum in a single pass.

The core idea is:
* We maintain a running sum `sum1` of the current subarray and a global maximum `maxi`.
* For each element in the array:
  1. Add it to our running sum: `sum1 += nums[i]`.
  2. Update our maximum: `maxi = max(maxi, sum1)`.
  3. **Reset if negative**: If `sum1` becomes less than `0`, we discard the current subarray. Any negative sum will only decrease the sum of any future subarray we add it to. So we reset `sum1 = 0`.

### Step-by-Step Execution Example

Input: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`

```
Index | Element | Running Sum (sum1) | Max Sum (maxi) | Decision / Action
------+---------+--------------------+----------------+----------------------------------------
  0   |   -2    |        -2          |       -2       | sum1 < 0, reset sum1 to 0
  1   |    1    |         1          |        1       | sum1 > maxi, update maxi = 1
  2   |   -3    |        -2          |        1       | sum1 < 0, reset sum1 to 0
  3   |    4    |         4          |        4       | sum1 > maxi, update maxi = 4
  4   |   -1    |         3          |        4       | 
  5   |    2    |         5          |        5       | sum1 > maxi, update maxi = 5
  6   |    1    |         6          |        6       | sum1 > maxi, update maxi = 6 (Max Subarray Found: [4, -1, 2, 1])
  7   |   -5    |         1          |        6       | 
  8   |    4    |         5          |        6       | 
```

### Complexity Analysis
- **Time Complexity (TC)**: $\mathcal{O}(N)$ (single pass through the array)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ (uses constant extra space)

---

## Follow-up: Printing the Maximum Subarray

In interviews, you might be asked to return or print the actual elements of the subarray that yield the maximum sum.

We can achieve this by keeping track of the starting and ending indices of the subarray:
* Whenever `sum1` resets to `0`, we mark the start of a new potential subarray: `start = i + 1` (or `i` for the current index).
* Whenever we update `maxi` with `sum1`, we record the indices: `subarray_start = start`, `subarray_end = i`.



## Summary Table

| Approach | Time Complexity (TC) | Space Complexity (SC) | Description |
| :--- | :--- | :--- | :--- |
| **Brute Force** | $\mathcal{O}(N^3)$ | $\mathcal{O}(1)$ | Checks sum of all possible subarrays by recalculating. |
| **Optimized Brute Force** | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | Uses a running sum to reduce nested loops to two. |
| **Kadane's Algorithm (Optimal)** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Single pass; discards negative subarray sums. |
