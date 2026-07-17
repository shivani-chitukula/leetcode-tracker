# Longest Subarray With Sum K

[GeeksforGeeks Problem Link](https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1)

Given an array `nums` and an integer `k`, find the length of the longest contiguous subarray whose elements sum to `k`.

---

## 1. Sliding Window / Two-Pointer Approach (Optimal for Positives & Zeros)

### Intuition
If the array contains only **non-negative** elements, we can utilize a sliding window. The sum of elements in a window is monotonically increasing with its size.
- Expand the window to the right by moving pointer `R` and adding the elements to `tempSum`.
- If `tempSum` exceeds `k`, the sum is too large. Since there are no negative numbers, adding more elements will only increase the sum. Thus, we shrink the window from the left by moving pointer `L` and subtracting `nums[L]` until the sum is less than or equal to `k`.
- Whenever `tempSum == k`, we calculate the window size (`R - L + 1`) and update the maximum length found so far.

- **Time Complexity (TC)**: $\mathcal{O}(N)$ (where $N$ is the number of elements; each element is visited at most twice: once by `R` and once by `L`)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ (uses constant extra space)

> [!IMPORTANT]
> The Sliding Window approach is only valid when the array elements are non-negative. If the array contains negative numbers, shrinking the window from the left is not guaranteed to reduce the sum, rendering this approach incorrect.

---

## 2. Hashing / Prefix Sum Approach (Optimal for Positives, Negatives & Zeros)

### Intuition
If the array contains **negative** numbers, we cannot use the sliding window approach because the prefix sum is no longer monotonic. Instead, we use a Hash Map to store the first occurrence of each prefix sum.
- Let the prefix sum up to index `i` be `x`.
- If there exists a subarray with sum `k` ending at index `i`, then the prefix sum up to the start of this subarray must be `x - k`.
- Therefore, at each step, we calculate the running `prefix_sum` and check if `prefix_sum - k` exists in our hash map.
- If it exists, it means the elements between the stored index and the current index sum to `k`. We update the maximum length.
- If the current `prefix_sum` is not already in the hash map, we store it along with its index. We only store the *first* occurrence to maximize the subarray length.

- **Time Complexity (TC)**: $\mathcal{O}(N)$ (single pass traversal, map lookups are $\mathcal{O}(1)$ on average)
- **Space Complexity (SC)**: $\mathcal{O}(N)$ (to store prefix sums in the hash map)

---

## Summary Table

| Approach | Constraints | Time Complexity (TC) | Space Complexity (SC) | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Sliding Window (Optimal)** | Non-negative numbers only | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Uses two pointers to dynamically adjust window size. |
| **Hashing (Optimal)** | Positives, Negatives, and Zeros | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | Tracks running prefix sums and checks for target differences in a map. |
