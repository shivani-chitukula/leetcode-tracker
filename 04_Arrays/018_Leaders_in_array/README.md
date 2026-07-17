# Leaders in an Array

[GeeksforGeeks Problem Link](https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1)

Given an array of integers `nums`, find all the **leaders** in the array. 

An element is a **leader** if it is strictly greater than all the elements to its right side. The rightmost element is always a leader.

---

## 1. Brute Force Approach

### Intuition
Compare each element with all elements to its right.
- Use two nested loops:
  - The outer loop picks an element `nums[i]`.
  - The inner loop checks all elements from `i + 1` to `n - 1`. If we find any element greater than or equal to `nums[i]`, then `nums[i]` is not a leader.
  - If we reach the end of the inner loop without finding a larger element, `nums[i]` is a leader.

- **Time Complexity (TC)**: $\mathcal{O}(N^2)$ (due to nested loops checking all elements to the right)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ auxiliary space (excluding the output list)

---

## 2. Optimal Approach (Scan from Right to Left)

### Intuition
Instead of scanning forward, we scan the array **backwards** (from right to left) and maintain the maximum element seen so far (`maxi`).

Since an element is a leader only if it is greater than all elements to its right:
1. The last element `nums[n - 1]` has no elements to its right, so it is **always** a leader. We initialize `maxi` with this element.
2. We iterate from index `n - 2` down to `0`.
3. If `nums[i] > maxi`, it means `nums[i]` is greater than all elements to its right. We add it to our leader list and update `maxi` to `nums[i]`.
4. Since we traverse backwards, our leaders will be in reverse order. We reverse the final list before returning it.

### Step-by-Step Execution Example

Input: `nums = [10, 22, 12, 3, 0, 6]`

```
Index (i) | Element | Current maxi | Is nums[i] > maxi? | Leaders List (reversed order)
----------+---------+--------------+--------------------+------------------------------
    5     |    6    |      6       |  Yes (Rightmost)   | [6]
    4     |    0    |      6       |  No (0 <= 6)       | [6]
    3     |    3    |      6       |  No (3 <= 6)       | [6]
    2     |   12    |      12      |  Yes (12 > 6)      | [6, 12]
    1     |   22    |      22      |  Yes (22 > 12)     | [6, 12, 22]
    0     |   10    |      22      |  No (10 <= 22)     | [6, 12, 22]
```

* Reversing the final leaders list `[6, 12, 22]` gives: `[22, 12, 6]`.

- **Time Complexity (TC)**: $\mathcal{O}(N)$ (single pass traversal and reversing a list of size at most $N$)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ auxiliary space (excluding the list used to store the results)

---

## Summary Table

| Approach | Time Complexity (TC) | Space Complexity (SC) | Description |
| :--- | :--- | :--- | :--- |
| **Brute Force** | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | Compares each element with all elements to its right using nested loops. |
| **Right-to-Left Scan (Optimal)** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Traverses backwards keeping track of the maximum element seen so far. |
