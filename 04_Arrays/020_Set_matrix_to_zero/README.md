# Set Matrix Zeroes

[LeetCode Problem Link](https://leetcode.com/problems/set-matrix-zeroes/)

Given an `m x n` integer matrix, if an element is `0`, set its entire row and column to `0`'s. You must do it **in-place**.

---

## 1. Better Approach (Using Reference Arrays)

### Intuition
Instead of modifying the matrix immediately (which would cause a chain reaction of zeros and overwrite other elements before we can read them), we can use extra space to keep track of which rows and columns should be set to zero.

1. Maintain two dummy lists: `row` (of size `m`) and `col` (of size `n`), both initialized to track non-zero states.
2. Traverse the matrix. For every cell `matrix[i][j] == 0`, mark `row[i]` and `col[j]` as `0` (or add their indices to tracking lists).
3. Traverse the matrix a second time. For every cell `matrix[i][j]`, if its row `i` or column `j` was marked, set `matrix[i][j] = 0`.

### Complexity Analysis
- **Time Complexity (TC)**: $\mathcal{O}(M \times N)$ (two full passes of the matrix)
- **Space Complexity (SC)**: $\mathcal{O}(M + N)$ (to store the row and column states)

---

## 2. Optimal Approach (In-Place using First Row/Col as Tracking Arrays)

### Intuition
To achieve $\mathcal{O}(1)$ auxiliary space, we must reuse the matrix itself to store the flags instead of using external arrays. The natural candidates for this are the **first row** and the **first column** of the matrix.

- We can use `matrix[i][0]` to track if row `i` needs to be zeroed.
- We can use `matrix[0][j]` to track if column `j` needs to be zeroed.

For any cell `matrix[i][j] == 0` (excluding the first row and first column for a moment), we set:
- `matrix[i][0] = 0`
- `matrix[0][j] = 0`

---

### The Edge Case with the Shared Variable `var`

The top-left cell `matrix[0][0]` presents a collision issue. It is shared by both the first row (`matrix[0][..]`) and the first column (`matrix[..][0]`). 

If we set `matrix[0][0] = 0`, we won't be able to distinguish whether it represents:
1. The **first row** needs to be zeroed.
2. The **first column** needs to be zeroed.
3. Both need to be zeroed.

#### How to resolve this?
We introduce an auxiliary variable `var` (typically initialized to `1`):
* `matrix[0][0]` will represent the status of the **first row**.
* `var` will represent the status of the **first column**.

#### Flag Marking Rules:
As we iterate through the matrix from top to bottom, left to right:
* If `matrix[i][j] == 0`:
  * If it's not in the first column (`j != 0`), mark its markers: `matrix[i][0] = 0` and `matrix[0][j] = 0`.
  * If it is in the first column (`j == 0`), update the tracker variable `var = 0`.

---

### The Crucial Step: Backwards Update
When modifying the matrix based on the flags, **we must traverse backwards** (from bottom-right to top-left, i.e., from `m-1` down to `0` and `n-1` down to `0`):

#### Why?
If we updated the matrix forward starting from `matrix[0][0]`, we would overwrite the flag indicators in the first row and first column. For example, if we zero out the first row prematurely, we lose the column markers stored in `matrix[0][j]`.

#### Backwards Update Rules:
For each cell `matrix[i][j]`:
1. If the cell is not in the first row or first column (`i != 0` and `j != 0`):
   * Set `matrix[i][j] = 0` if `matrix[i][0] == 0` or `matrix[0][j] == 0`.
2. For the first row (`i == 0`):
   * Set `matrix[i][j] = 0` if `matrix[0][0] == 0`.
3. For the first column (`j == 0`):
   * Set `matrix[i][j] = 0` if `var == 0`.

---

### Complexity Analysis
- **Time Complexity (TC)**: $\mathcal{O}(M \times N)$ (two passes of the matrix)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ (in-place modification using only a single extra variable `var`)

---

## Summary Table

| Approach | Time Complexity (TC) | Space Complexity (SC) | Description |
| :--- | :--- | :--- | :--- |
| **Using Reference Arrays** | $\mathcal{O}(M \times N)$ | $\mathcal{O}(M + N)$ | Uses helper list structures to track zero states for rows and columns. |
| **In-Place (Optimal)** | $\mathcal{O}(M \times N)$ | $\mathcal{O}(1)$ | Reuses the first row/col as dummy trackers, resolving the overlap with `var`. |
