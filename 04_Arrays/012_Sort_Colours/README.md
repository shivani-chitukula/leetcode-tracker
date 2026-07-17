# Sort Colors

[LeetCode Problem Link](https://leetcode.com/problems/sort-colors/)

Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

---

## 1. Brute Force Approach (Sorting)

### Intuition
The most straightforward way is to use a standard sorting algorithm (like QuickSort or MergeSort) or the built-in language sorting function to sort the array.
- This will sort the numbers in ascending order (`0`s, then `1`s, then `2`s).

- **Time Complexity (TC)**: $\mathcal{O}(N \log N)$ (due to sorting)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ or $\mathcal{O}(N)$ (depending on the sorting implementation)

---

## 2. Better Approach (Counting Sort)

### Intuition
Since we only have three unique elements (`0`, `1`, and `2`), we can count their frequencies and then overwrite the original array.
1. Traverse the array and keep a count of the number of `0`s, `1`s, and `2`s.
2. In a second pass, overwrite the array:
   - Fill the first `cnt0` elements with `0`.
   - Fill the next `cnt1` elements with `1`.
   - Fill the remaining elements with `2`.

- **Time Complexity (TC)**: $\mathcal{O}(N) + \mathcal{O}(N) = \mathcal{O}(N)$ (since we traverse the array twice)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ (uses only three counter variables)

---

## 3. Optimal Approach (Dutch National Flag Algorithm)

### Intuition
The Dutch National Flag (DNF) algorithm allows us to sort the array in a **single pass** with $\mathcal{O}(1)$ extra space.

The algorithm uses three pointers: `low`, `mid`, and `high` to partition the array into four virtual sections:
- `nums[0 ... low-1]`: Contains only `0`s.
- `nums[low ... mid-1]`: Contains only `1`s.
- `nums[mid ... high]`: Unprocessed/unsorted elements.
- `nums[high+1 ... n-1]`: Contains only `2`s.

```mermaid
text
+-----------------------+-----------------------+-----------------------+-----------------------+
|        All 0s         |        All 1s         |      Unprocessed      |        All 2s         |
+-----------------------+-----------------------+-----------------------+-----------------------+
0                     low-1   low             mid-1   mid            high   high+1                 n-1
```

### Steps & Pointer Movements
Initially, all elements are unprocessed. So we set:
- `low = 0`
- `mid = 0`
- `high = n - 1` (where `n` is the size of the array)

We traverse the array by checking `nums[mid]` until `mid <= high`:

1. **If `nums[mid] == 0`**:
   - Swap `nums[low]` and `nums[mid]`.
   - Since the element swapped from `nums[low]` is guaranteed to be `1` (because `mid` has already processed it), we can safely move both pointers forward:
     - `low += 1`
     - `mid += 1`

2. **If `nums[mid] == 1`**:
   - The element is already in its correct segment.
   - Simply move the `mid` pointer forward:
     - `mid += 1`

3. **If `nums[mid] == 2`**:
   - Swap `nums[mid]` and `nums[high]`.
   - Since we placed a `2` at its correct position at the end, we decrement the `high` pointer:
     - `high -= 1`
   - **Important**: We do **NOT** increment `mid`. The swapped element that came from `high` to `mid` is unprocessed and unknown. We must evaluate it in the next iteration.

### Complexity Analysis
- **Time Complexity (TC)**: $\mathcal{O}(N)$ (we only traverse the array once; in each step, either `mid` increases or `high` decreases)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ (sorting is done in-place without any extra memory)

---

## Summary Table

| Approach | Time Complexity (TC) | Space Complexity (SC) | Description |
| :--- | :--- | :--- | :--- |
| **Brute Force** | $\mathcal{O}(N \log N)$ | $\mathcal{O}(1)$ | Uses library sort or standard sorting. |
| **Counting Sort (Better)** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Two-pass approach: count frequencies and overwrite. |
| **Dutch National Flag (Optimal)**| $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Single-pass approach using three pointers. |
