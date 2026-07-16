# Left Rotate Array by K Places

[LeetCode Problem Link (Right Rotate)](https://leetcode.com/problems/rotate-array/description/)

Rotate a given array to the left by `k` steps.

---

## 1. Slicing Approach (Pythonic)
- **Logic**: Slice the array from index `k` to the end, and concatenate it with the slice from the start to index `k`. Assign the result back to `nums[:]` to modify the array in-place.
- **Time Complexity (TC)**: $\mathcal{O}(N)$ (creating list slices and copying them back takes linear time)
- **Space Complexity (SC)**: $\mathcal{O}(N)$ (creates temporary sublists of combined size $N$ in memory)

---

## 2. Reversal Algorithm (Optimal - In-Place)
- **Logic**: To achieve a left rotation in-place without using extra space, we can reverse specific subsegments of the array:
  1. Reverse the first `k` elements: `nums[0:k]`
  2. Reverse the remaining `n - k` elements: `nums[k:n]`
  3. Reverse the entire array: `nums[0:n]`
- **Time Complexity (TC)**: $\mathcal{O}(N)$ (each element is visited a constant number of times during reversal)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ (modifies the array completely in-place)

---

## Summary Table

| Approach | Time Complexity (TC) | Space Complexity (SC) | Description |
| :--- | :--- | :--- | :--- |
| **Slicing Approach** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | Pythonic slice and concatenation, simple but uses extra space. |
| **Reversal Algorithm (Optimal)** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Three-step reversal to rotate the array completely in-place. |
