# Insertion Sort

---

## 💡 Intuition & Core Concepts

The key idea behind **Insertion Sort** is:
> **Build a sorted array one element at a time by picking the next element and inserting it into its correct position within the already sorted prefix.**

Think of it like sorting a hand of playing cards. You pick up one card from the pile, look at the sorted cards in your hand, and slide/insert it into its correct location, shifting larger cards to the right.

### How it Works (Step-by-Step)
We conceptually divide the array into:
1. **Sorted Prefix**: Initially containing only the first element `nums[0..0]`.
2. **Unsorted Suffix**: The remaining elements `nums[1..n-1]`.

For each index `i` (from `0` to `n - 2`):
1. The sorted prefix spans from index `0` to `i`.
2. We take the next element `nums[i + 1]` (at index `j = i + 1`).
3. We move this element backwards through the sorted prefix (`j` counting down from `i + 1` to `1`):
   - Compare `nums[j]` with its left neighbor `nums[j - 1]`.
   - If `nums[j - 1] > nums[j]`, they are in the wrong order $\rightarrow$ swap them.
   - If `nums[j - 1] <= nums[j]`, the element has reached its correct position $\rightarrow$ stop the inner loop immediately.
4. Repeat until the entire array is sorted.

---

## 📝 Dry Run Example
Let's trace Insertion Sort with the input array: `nums = [13, 46, 24, 52, 20, 9]`

### Initial State
```text
[ 13 | 46, 24, 52, 20, 9 ]   (Sorted Prefix: [13] / Unsorted Boundary: i = 0)
```

---

### Pass 0 ($i = 0$)
We insert the next element `46` (index 1) into the sorted prefix `[13]`:
- Compare `(13, 46)` $\rightarrow$ `13 < 46`, order is correct. No swap. Stop.

**Array state below Pass 0:**
```text
[ 13, 46 | 24, 52, 20, 9 ]
  Sorted | Unsorted
```

---

### Pass 1 ($i = 1$)
We insert `24` (index 2) into `[13, 46]`:
- Compare `(46, 24)` $\rightarrow$ swap $\rightarrow$ `[13, 24, 46 | 52, 20, 9]`
- Compare `(13, 24)` $\rightarrow$ order is correct. Stop.

**Array state below Pass 1:**
```text
[ 13, 24, 46 | 52, 20, 9 ]
```

---

### Pass 2 ($i = 2$)
We insert `52` (index 3) into `[13, 24, 46]`:
- Compare `(46, 52)` $\rightarrow$ order is correct. Stop.

**Array state below Pass 2:**
```text
[ 13, 24, 46, 52 | 20, 9 ]
```

---

### Pass 3 ($i = 3$)
We insert `20` (index 4) into `[13, 24, 46, 52]`:
- Compare `(52, 20)` $\rightarrow$ swap $\rightarrow$ `[13, 24, 46, 20, 52 | 9]`
- Compare `(46, 20)` $\rightarrow$ swap $\rightarrow$ `[13, 24, 20, 46, 52 | 9]`
- Compare `(24, 20)` $\rightarrow$ swap $\rightarrow$ `[13, 20, 24, 46, 52 | 9]`
- Compare `(13, 20)` $\rightarrow$ order is correct. Stop.

**Array state below Pass 3:**
```text
[ 13, 20, 24, 46, 52 | 9 ]
```

---

### Pass 4 ($i = 4$)
We insert `9` (index 5) into `[13, 20, 24, 46, 52]`:
- `9` is smaller than all prefix elements. It swaps repeatedly all the way to the beginning.
- Swaps: `(52, 9)`, then `(46, 9)`, then `(24, 9)`, then `(20, 9)`, then `(13, 9)`.

**Array state below Pass 4:**
```text
[ 9, 13, 20, 24, 46, 52 ]
```

**Final Sorted Array:**
`[9, 13, 20, 24, 46, 52]`

---

## ⚡ Optimization: Shifting Instead of Swapping
In standard implementation, we swap adjacent elements to bubble the target value backward. Each swap takes 3 memory writes. 
We can optimize this by saving the target element to a temporary variable (`key`), shifting larger elements to the right, and then inserting the `key` into its final position.

### Optimized Implementation
```python
def insertionSortOptimized(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        
        # Shift elements of nums[0..i-1] that are greater than key
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
            
        nums[j + 1] = key
        
    return nums
```

---

## 📊 Complexity Analysis

| Scenario | Time Complexity | Space Complexity | Description |
| :--- | :---: | :---: | :--- |
| **Best Case** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Occurs when the input array is already sorted. The inner loop checks the first element to the left and terminates instantly. |
| **Average Case** | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | Quadratic comparisons and swaps on average. |
| **Worst Case** | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | Occurs when the input array is sorted in reverse order. Every element must be shifted to the start. |
