# Rotate Image

[LeetCode Problem Link](https://leetcode.com/problems/rotate-image/)

You are given an `n x n` 2D matrix representing an image, rotate the image by **90 degrees (clockwise)**.

You have to rotate the image **in-place**, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

---

## 1. Brute Force Approach (Using Helper Matrix)

### Intuition
If we observe the transformation from the input matrix to the rotated matrix:
* The first row of the original matrix becomes the last column of the rotated matrix.
* The second row becomes the second-to-last column, and so on.

Mathematically, the element at index `(i, j)` in the original matrix moves to index `(j, n - 1 - i)` in the rotated matrix.

1. Create a dummy/helper matrix `ans` of the same dimensions `n x n`.
2. Traverse the original matrix and place each element `matrix[i][j]` at its new position: `ans[j][n - 1 - i] = matrix[i][j]`.
3. Copy the elements from `ans` back into the original `matrix`.

### Complexity Analysis
- **Time Complexity (TC)**: $\mathcal{O}(N^2)$ (we traverse every element of the $N \times N$ matrix)
- **Space Complexity (SC)**: $\mathcal{O}(N^2)$ (uses a helper matrix of size $N \times N$)

---

## 2. Optimal Approach (In-Place Transpose & Reverse)

### Intuition
To rotate the matrix in-place without using extra space, we can break the 90-degree clockwise rotation into two simple steps:
1. **Transpose the matrix**: Swap rows and columns. This swaps elements along the main diagonal (`matrix[i][j]` is swapped with `matrix[j][i]`).
2. **Reverse each row**: Reverse the elements of each row horizontally.

```
Original Matrix            Transposed Matrix          Rotated Matrix (After Reverse)
 1  2  3                    1  4  7                    7  4  1
 4  5  6         --->       2  5  8         --->       8  5  2
 7  8  9                    3  6  9                    9  6  3
```

---

### Crucial Detail: Transposing Only the Upper Triangle

When performing the transpose step, **we must only swap elements in one-half of the matrix** (either the upper triangle or the lower triangle). 

#### Why?
* A transpose operation swaps `matrix[i][j]` with `matrix[j][i]`.
* If we run both loops fully from `0` to `n - 1` (e.g. `for i in range(0, n)` and `for j in range(0, n)`):
  * When the loop reaches cell `(i, j)` where `i = 0, j = 1`, it swaps `matrix[0][1]` and `matrix[1][0]`.
  * Later, when the loop reaches cell `(j, i)` where `i = 1, j = 0`, it swaps `matrix[1][0]` and `matrix[0][1]` **again**.
  * These double swaps **cancel each other out**, returning every element back to its original position. The matrix remains completely unchanged.
* To prevent this cancellation, we only iterate the inner loop over the **upper triangle** (where `j > i`). By starting the inner loop at index `i + 1` (`for j in range(i + 1, n)`), each pair is swapped exactly once.
* We can optimize the loop boundaries to avoid redundant operations:
  * **Avoid Diagonal Swaps**: Diagonal elements (where `i == j`) do not need to be swapped with themselves. We start the inner loop `j` from `i + 1` instead of `i`.
  * **Avoid Last Row**: For the last row (`i = n - 1`), the only remaining element is on the diagonal. Thus, we can terminate the outer loop `i` at `n - 2` (`for i in range(n - 1)`).

---

### Complexity Analysis
- **Time Complexity (TC)**: $\mathcal{O}(N^2) + \mathcal{O}(N^2) = \mathcal{O}(N^2)$ 
  * Transposing the matrix takes $\mathcal{O}(N^2/2)$ operations.
  * Reversing each of the $N$ rows of size $N$ takes $\mathcal{O}(N \times N/2)$ operations.
- **Space Complexity (SC)**: $\mathcal{O}(1)$ (the operations are done completely in-place using constant auxiliary variables)

---

## Summary Table

| Approach | Time Complexity (TC) | Space Complexity (SC) | Description |
| :--- | :--- | :--- | :--- |
| **Helper Matrix (Brute Force)** | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | Map elements directly to their final positions in a separate helper matrix. |
| **Transpose & Reverse (Optimal)** | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | Transpose the upper triangle in-place, then reverse the elements of each row. |
