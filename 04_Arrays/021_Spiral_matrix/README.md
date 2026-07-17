# Spiral Matrix

[LeetCode Problem Link](https://leetcode.com/problems/spiral-matrix/)

Given an `m x n` matrix, return *all elements of the matrix in spiral order*.

---

## 1. Optimal Approach (Boundary Traversal)

### Intuition
To traverse the matrix in a spiral order, we can view the traversal as peeling off the outer boundaries of the matrix layer by layer. 

We define four pointers representing the boundaries of our current active submatrix:
* `top`: Points to the top-most row (initially `0`).
* `bottom`: Points to the bottom-most row (initially `m - 1`).
* `left`: Points to the left-most column (initially `0`).
* `right`: Points to the right-most column (initially `n - 1`).

In each outer iteration, we traverse the boundary elements of the current submatrix in a clockwise direction:
1. **Left to Right**: Traverse the `top` row from column `left` to `right`. Then, increment `top` by 1.
2. **Top to Bottom**: Traverse the `right` column from row `top` to `bottom`. Then, decrement `right` by 1.
3. **Right to Left**: Traverse the `bottom` row from column `right` to `left`. Then, decrement `bottom` by 1.
4. **Bottom to Top**: Traverse the `left` column from row `bottom` to `top`. Then, increment `left` by 1.

We repeat this process as long as `left <= right` and `top <= bottom`.

---

### Crucial Detail: Why we check `top <= bottom` and `left <= right` again inside the loop

The outer `while` loop checks the condition `while left <= right and top <= bottom:` at the beginning of each layer traversal. However, **within a single iteration**, we modify the boundary pointers:
* After the **Left to Right** step, we do `top += 1`.
* After the **Top to Bottom** step, we do `right -= 1`.

Because of these intermediate changes, the loop boundary state can change *before* we execute steps 3 and 4. This is especially true for non-square matrices (specifically matrices with only a single row or a single column) and when processing the final central layer of a matrix.

#### Case 1: Single Row Matrix (e.g., `[[1, 2, 3, 4]]`)
* **Initial boundaries**: `top = 0`, `bottom = 0`, `left = 0`, `right = 3`.
* **Step 1 (Left to Right)**: Prints `1, 2, 3, 4`. We increment `top += 1` (now `top = 1`).
* **Step 2 (Top to Bottom)**: `top = 1`, `bottom = 0`. The range `for i in range(top, bottom + 1)` doesn't execute. We decrement `right -= 1` (now `right = 2`).
* **Step 3 (Right to Left)**: If we do **NOT** check `if top <= bottom:`, the loop `for i in range(right, left - 1, -1)` (which is `range(2, -1, -1)`) will run. It would print elements from `matrix[bottom][i]` (where `bottom = 0`), resulting in duplicate prints: `3, 2, 1`.
  * **Solution**: Checking `if top <= bottom` (which is `1 <= 0` -> `False`) correctly blocks this loop and prevents duplicate prints.

#### Case 2: Single Column Matrix (e.g., `[[1], [2], [3]]`)
* **Initial boundaries**: `top = 0`, `bottom = 2`, `left = 0`, `right = 0`.
* **Step 1 (Left to Right)**: Prints `1`. We increment `top += 1` (now `top = 1`).
* **Step 2 (Top to Bottom)**: Prints `2, 3`. We decrement `right -= 1` (now `right = -1`).
* **Step 3 (Right to Left)**: `top <= bottom` (`1 <= 2`) is `True`, but the loop range `range(-1, -1, -1)` is empty, so nothing prints. We decrement `bottom -= 1` (now `bottom = 1`).
* **Step 4 (Bottom to Top)**: If we do **NOT** check `if left <= right:`, the loop `for i in range(bottom, top - 1, -1)` (which is `range(1, 0, -1)`) will run. It would print elements from `matrix[i][left]` (where `left = 0`), resulting in a duplicate print of `2`.
  * **Solution**: Checking `if left <= right` (which is `0 <= -1` -> `False`) correctly blocks this loop and prevents duplicate prints.

---

### Complexity Analysis
- **Time Complexity (TC)**: $\mathcal{O}(M \times N)$ (every element of the matrix is visited and printed exactly once)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ auxiliary space (excluding the output list to return the elements)

---

## Summary Table

| Approach | Time Complexity (TC) | Space Complexity (SC) | Description |
| :--- | :--- | :--- | :--- |
| **Boundary Traversal** | $\mathcal{O}(M \times N)$ | $\mathcal{O}(1)$ | Shrinks boundaries `top`, `bottom`, `left`, and `right` clockwise layer-by-layer. |
