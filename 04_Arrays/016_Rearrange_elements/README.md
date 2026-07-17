# Rearrange Array Elements by Sign

[LeetCode Problem Link](https://leetcode.com/problems/rearrange-array-elements-by-sign/)

You are given a **0-indexed** integer array `nums` of **even** length containing an equal number of positive and negative integers.

You should **rearrange** the elements of `nums` such that the modified array follows the given conditions:
1. Every consecutive pair of integers have **opposite signs**.
2. For all integers with the same sign, the **order** in which they were present in `nums` is **preserved** (i.e., they must maintain their relative order).
3. The rearranged array begins with a positive integer.

Return *the modified array after rearranging the elements*.

---

## 1. Brute Force Approach (Two-Pass)

### Intuition
Since we need to separate the positive and negative numbers and place them at alternating positions, the most direct approach is:
1. Create two auxiliary lists: one for positive integers and one for negative integers.
2. Traverse the input array and filter the numbers into their respective lists.
3. Traverse the original array again (or build a new one), placing the positive numbers at even indices (`0, 2, 4, ...`) and the negative numbers at odd indices (`1, 3, 5, ...`).

### Complexity Analysis
- **Time Complexity (TC)**: $\mathcal{O}(N) + \mathcal{O}(N) = \mathcal{O}(N)$ (one pass to separate the elements, and a second pass to merge them back)
- **Space Complexity (SC)**: $\mathcal{O}(N)$ (to store the auxiliary lists for positive and negative numbers, each of size $N/2$)

---

## 2. Optimal Approach (Single-Pass with Two Pointers)

### Intuition
Instead of making two passes and storing elements in separate lists before merging them, we can do it in a **single pass** using two pointers.

We initialize a result array of the same size as `nums`.
- We maintain a `posIdx` pointer starting at `0` (for even positions).
- We maintain a `negIdx` pointer starting at `1` (for odd positions).

As we iterate through the input array `nums` exactly once:
- If the current element is positive, we place it directly at `result[posIdx]` and increment `posIdx` by `2`.
- If the current element is negative, we place it directly at `result[negIdx]` and increment `negIdx` by `2`.

This allows us to place every element in its correct destination immediately without separate intermediate list creation.

### Step-by-Step Execution Example

Input: `nums = [3, 1, -2, -5, 2, -4]`

* Initialize: `result = [0, 0, 0, 0, 0, 0]`, `posIdx = 0`, `negIdx = 1`

```
Step | Element | Sign     | Action                                     | Pointers State               | Result Array
-----+---------+----------+--------------------------------------------+------------------------------+--------------------------
  1  |    3    | Positive | Place at result[posIdx], posIdx += 2       | posIdx = 2, negIdx = 1       | [3, 0, 0, 0, 0, 0]
  2  |    1    | Positive | Place at result[posIdx], posIdx += 2       | posIdx = 4, negIdx = 1       | [3, 0, 1, 0, 0, 0]
  3  |   -2    | Negative | Place at result[negIdx], negIdx += 2       | posIdx = 4, negIdx = 3       | [3, -2, 1, 0, 0, 0]
  4  |   -5    | Negative | Place at result[negIdx], negIdx += 2       | posIdx = 4, negIdx = 5       | [3, -2, 1, -5, 0, 0]
  5  |    2    | Positive | Place at result[posIdx], posIdx += 2       | posIdx = 6, negIdx = 5       | [3, -2, 1, -5, 2, 0]
  6  |   -4    | Negative | Place at result[negIdx], negIdx += 2       | posIdx = 6, negIdx = 7       | [3, -2, 1, -5, 2, -4]
```

### Complexity Analysis
- **Time Complexity (TC)**: $\mathcal{O}(N)$ (we traverse the input array exactly once)
- **Space Complexity (SC)**: $\mathcal{O}(N)$ (to store the returned output array; no extra temporary list/auxiliary storage is used)

---

## Summary Table

| Approach | Time Complexity (TC) | Space Complexity (SC) | Description |
| :--- | :--- | :--- | :--- |
| **Two-Pass (Brute Force)** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | Segregates positives and negatives into two lists, then merges them back. |
| **Two Pointers (Optimal)** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | Fills the result array in a single pass using separate even and odd index pointers. |

---

## Follow-up: What if there are unequal numbers of positives and negatives?

### Will the current approaches work?
**No, they will fail.**
1. **Two-Pass Approach**: It assumes `pos` and `neg` each have exactly `n // 2` elements. If they are unequal, once we finish processing the shorter list, accessing `pos[i//2]` or `neg[i//2]` will throw an `IndexError: list index out of range`.
2. **Two-Pointer Approach**: Since one sign is more frequent than `n // 2`, its index pointer (`posIdx` or `negIdx`) will exceed the bounds of the array size `n`, throwing an `IndexError`.

### How to handle this variation?
If there are unequal counts, the rule is usually to place them in alternating positions as long as we have both positive and negative numbers. Once we run out of one type, we simply append all the remaining elements of the other type at the end.

#### Modified Algorithm:
1. Segregate positives and negatives into two lists, `pos` and `neg`.
2. Maintain three pointers: `p = 0` (for `pos`), `n = 0` (for `neg`), and `i = 0` (for placing in the output).
3. While `p < len(pos)` and `n < len(neg)`:
   - If `i` is even, place `pos[p]` and increment `p` and `i`.
   - If `i` is odd, place `neg[n]` and increment `n` and `i`.
4. If there are remaining elements in `pos`, copy them directly to the end of the output.
5. If there are remaining elements in `neg`, copy them directly to the end of the output.

- **Time Complexity (TC)**: $\mathcal{O}(N)$
- **Space Complexity (SC)**: $\mathcal{O}(N)$

