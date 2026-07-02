# Maximum Ascending Subarray Sum

[LeetCode Problem Link](https://leetcode.com/problems/maximum-ascending-subarray-sum/)

Find the maximum sum of a contiguous ascending subarray in a given array of positive integers.

---

## Optimal Approach (Single Pass Iteration)
- **Logic**: Iterate through the array starting from the second element. Keep track of two variables:
  - `maxi`: Stores the overall maximum ascending subarray sum found so far.
  - `curr_sum`: Stores the sum of the current active ascending subarray (initialized to the first element).
- **Process**:
  - If the current element is less than or equal to the previous element (`nums[i] <= nums[i-1]`), the ascending sequence is broken. Update `maxi` with the max of `maxi` and `curr_sum`, and reset `curr_sum` to `0`.
  - Add the current element to `curr_sum`.
  - After completing the loop, return the maximum of `maxi` and the remaining `curr_sum`.
- **Time Complexity (TC)**: $\mathcal{O}(N)$ (scans the array exactly once)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ (uses constant auxiliary space)

---

## Summary Table

| Approach | Time Complexity (TC) | Space Complexity (SC) | Description |
| :--- | :--- | :--- | :--- |
| **Optimal Iteration** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Single pass tracking of active ascending sum and overall maximum. |
