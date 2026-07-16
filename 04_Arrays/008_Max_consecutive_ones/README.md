# Max Consecutive Ones

[LeetCode Problem Link](https://leetcode.com/problems/max-consecutive-ones/description/)

Given a binary array `nums`, return the maximum number of consecutive 1's in the array.

---

## 1. Single Pass Iterative Approach (Linear Scan)
- **Logic**: Maintain a running counter `temp` for the current streak of consecutive 1s and a global maximum `maxi`. Iterate through the array:
  - If the element is `1`, increment `temp`.
  - If the element is `0`, update `maxi` with the maximum of `maxi` and `temp`, and reset `temp` to `0`.
  - After completing the loop, return the maximum of `maxi` and `temp` to account for a streak ending at the last element.
- **Time Complexity (TC)**: $\mathcal{O}(N)$ (where $N$ is the length of the array, since we traverse it exactly once)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ (uses constant extra space for the count variables)

---

## Summary Table

| Approach | Time Complexity (TC) | Space Complexity (SC) | Description |
| :--- | :--- | :--- | :--- |
| **Linear Scan (Optimal)** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Single pass scan tracking running count and maximum count. |
