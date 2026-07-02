# Check if Array Is Sorted and Rotated

[LeetCode Problem Link](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/)

Determine if the array was originally sorted in non-decreasing order and then rotated some number of positions (including zero).

---

## Optimal Approach (Counting Break Points)
- **Logic**: A sorted and rotated array can have at **most one** point where the sequence decreases (a "break point"), including the transition from the last element back to the first element (circular wrap-around).
- **Process**:
  - Traverse the array and count how many times `nums[i] < nums[i-1]`.
  - Compare the last element with the first element (`nums[-1]` and `nums[0]`). If `nums[0] < nums[-1]`, count it as an additional break point.
  - If the total count of break points is less than or equal to `1`, the array is sorted and rotated. Otherwise, it is not.
- **Time Complexity (TC)**: $\mathcal{O}(N)$ (single pass scan of the array)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ (uses constant extra space)

---

## Summary Table

| Approach | Time Complexity (TC) | Space Complexity (SC) | Description |
| :--- | :--- | :--- | :--- |
| **Optimal Count** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Count transitions where elements decrease, including the circular wrap-around. At most 1 break is allowed. |
