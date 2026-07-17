# Next Permutation

[LeetCode Problem Link](https://leetcode.com/problems/next-permutation/)

A **permutation** of an array of integers is an arrangement of its members into a sequence or linear order.

* For example, for `arr = [1,2,3]`, the following are all the permutations of `arr`: `[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]`.

The **next permutation** of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one list according to their lexicographical order, then the **next permutation** of that array is the permutation that follows it in the sorted list.

If such an arrangement is not possible (i.e., the array is sorted in descending order), the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

The replacement must be **in-place** and use only constant extra memory.

---

## 1. Brute Force Approach

### Intuition
The most basic way to solve this is to generate all possible permutations of the given array.
1. Find all permutations of the array and sort them lexicographically.
2. Search for the input array in the list of sorted permutations.
3. Identify the permutation that appears immediately after it.
4. If the input array is the last permutation in the sorted list (the descending array), wrap around and return the first permutation (the sorted ascending array).

### Complexity Analysis
- **Time Complexity (TC)**: $\mathcal{O}(N! \times N)$ (generating all permutations of size $N$ takes factorial time)
- **Space Complexity (SC)**: $\mathcal{O}(N! \times N)$ (needed to store all the generated permutations)

---

## 2. Optimal Approach (Single-Pass Algorithm)

This is the optimal approach which solves the problem in a single pass of the array. It utilizes mathematical logic to find the next lexicographically greater permutation directly.

### Detailed Breakdown of the Three Steps

#### Step 1: Find the Breakpoint (First `while` Loop)
* **What it does**: We start from the second-to-last element (`n - 2`) and scan the array backwards (from right to left) to find the first index `i` where the element is smaller than its next element: `nums[i] < nums[i + 1]`.
* **Why we do it**: 
  * If we look at the array from right to left, a sequence of increasing numbers (e.g., `5 -> 4 -> 3 -> 2`) is in its maximum possible sorted order (descending from left to right). We cannot create a larger permutation using just these numbers.
  * To make the number larger, we must find the first position from the right that breaks this descending sequence. That position `i` is our "breakpoint". This is the point where we can swap in a larger element to increase the permutation value.

#### Step 2: Find the Next Greater Element and Swap (Second `while` Loop)
* **What it does**: If a breakpoint index `i` is found (meaning the array is not entirely in descending order), we look for the smallest element to the right of `i` that is strictly greater than `nums[i]`. We find this by scanning backwards from the end of the array (`n - 1`) using index `j` until we find `nums[j] > nums[i]`. Once found, we swap `nums[i]` and `nums[j]`.
* **Why we do it**:
  * We need to replace the element at the breakpoint `nums[i]` with the next larger number available to its right to step up to the next lexicographical permutation.
  * Since the suffix `nums[i + 1 ... n - 1]` is sorted in descending order (from left to right), scanning backwards from right to left guarantees that the first element we encounter that is greater than `nums[i]` is the smallest possible number that is still larger than `nums[i]`. This minimizes the increase in value.

#### Step 3: Reverse the Suffix
* **What it does**: We reverse all the elements to the right of the breakpoint `i` (from index `i + 1` to the end of the array).
* **Why we do it**:
  * After swapping `nums[i]` and `nums[j]`, the suffix `nums[i + 1 ... n - 1]` remains sorted in descending order.
  * To get the *immediate* next permutation, we want the suffix to be as small as possible. The smallest possible suffix is one sorted in ascending order.
  * Since the suffix is currently in descending order, reversing it in-place transforms it into ascending order in $\mathcal{O}(N)$ time, avoiding the cost of a full sorting algorithm.

> [!NOTE]
> If no breakpoint is found in Step 1 (i.e. `i < 0`), it means the entire array is sorted in descending order (e.g. `[3, 2, 1]`). In this case, we skip Step 2 and directly proceed to Step 3, which reverses the entire array to sorted ascending order (`[1, 2, 3]`), satisfying the wrap-around requirement.

---

### Step-by-Step Execution Example

Input: `nums = [2, 1, 5, 4, 3, 0]`

1. **Step 1 (Find Breakpoint)**:
   * Scan backwards: `0 < 3` (yes), `3 < 4` (yes), `4 < 5` (yes), `5 < 1` (no!).
   * The breakpoint is at index `i = 1` where `nums[1] = 1`.

2. **Step 2 (Find Next Greater Element to Swap)**:
   * Scan backwards from the end to find the first element greater than `nums[i] = 1`.
   * `nums[5] = 0` (no), `nums[4] = 3` (yes, `3 > 1`).
   * Swap `nums[1]` (1) and `nums[4]` (3).
   * Array becomes: `[2, 3, 5, 4, 1, 0]`.

3. **Step 3 (Reverse Suffix)**:
   * Suffix to reverse starts at index `i + 1 = 2` (elements: `[5, 4, 1, 0]`).
   * Reversing `[5, 4, 1, 0]` gives `[0, 1, 4, 5]`.
   * Final array becomes: `[2, 3, 0, 1, 4, 5]`.

---

### Complexity Analysis
- **Time Complexity (TC)**: $\mathcal{O}(N)$ (in the worst case, we do a constant number of linear scans: one scan from right to left to find the breakpoint, one scan to find the swap element, and one reversal of the suffix)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ (all operations are performed in-place using constant extra memory)

---

## Summary Table

| Approach | Time Complexity (TC) | Space Complexity (SC) | Description |
| :--- | :--- | :--- | :--- |
| **Brute Force** | $\mathcal{O}(N! \times N)$ | $\mathcal{O}(N! \times N)$ | Generates all permutations, sorts them, and searches for the next configuration. |
| **Optimal (Single-Pass)** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Scans from the right to find the breakpoint, swaps with the next larger suffix element, and reverses the suffix. |
