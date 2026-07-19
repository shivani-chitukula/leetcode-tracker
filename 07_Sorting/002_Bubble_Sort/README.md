# Bubble Sort

---

## 💡 Intuition & Core Concepts

The key idea behind **Bubble Sort** is:
> **Push the maximum element of the unsorted segment to the end of that segment in each pass by repeatedly swapping adjacent elements if they are in the wrong order.**

Because the largest elements "bubble up" to the end of the array, the algorithm is named Bubble Sort.

### How it Works (Step-by-Step)
We conceptually divide the array into:
1. **Unsorted Partition**: Initially the entire array.
2. **Sorted Partition**: At the end of the array (initially empty).

In each outer loop pass $i$ (counting backwards from `n - 1` to `0`):
1. The unsorted partition spans from index `0` to `i`.
2. We run an inner loop with pointer `j` from index `0` to `i - 1`.
3. For each adjacent pair `nums[j]` and `nums[j + 1]`:
   - If `nums[j] > nums[j + 1]`, they are in the wrong order $\rightarrow$ swap them.
4. By the end of this inner loop, the maximum element in `nums[0..i]` has bubbled up to index `i`.
5. We shrink the unsorted partition boundary by decrementing $i$ and repeat.

---

## 📝 Dry Run Example
Let's trace Bubble Sort with the input array: `nums = [13, 46, 24, 52, 20, 9]`

### Initial State
```text
[ 13, 46, 24, 52, 20, 9 ]   (Unsorted Boundary: i = 5)
```

---

### Pass 0 ($i = 5$)
We compare adjacent pairs from index `0` to `4`:
- Compare `(13, 46)` $\rightarrow$ order is correct, no swap.
- Compare `(46, 24)` $\rightarrow$ swap $\rightarrow$ `[13, 24, 46, 52, 20, 9]`
- Compare `(46, 52)` $\rightarrow$ order is correct, no swap.
- Compare `(52, 20)` $\rightarrow$ swap $\rightarrow$ `[13, 24, 46, 20, 52, 9]`
- Compare `(52, 9)` $\rightarrow$ swap $\rightarrow$ `[13, 24, 46, 20, 9, 52]`

**Array state below Pass 0:**
```text
[ 13, 24, 46, 20, 9 | 52 ]
  Unsorted Portion   | Sorted (52 is placed)
```

---

### Pass 1 ($i = 4$)
We compare adjacent pairs from index `0` to `3`:
- Compare `(13, 24)` $\rightarrow$ no swap.
- Compare `(24, 46)` $\rightarrow$ no swap.
- Compare `(46, 20)` $\rightarrow$ swap $\rightarrow$ `[13, 24, 20, 46, 9, 52]`
- Compare `(46, 9)` $\rightarrow$ swap $\rightarrow$ `[13, 24, 20, 9, 46, 52]`

**Array state below Pass 1:**
```text
[ 13, 24, 20, 9 | 46, 52 ]
  Unsorted part | Sorted
```

---

### Pass 2 ($i = 3$)
We compare adjacent pairs from index `0` to `2`:
- Compare `(13, 24)` $\rightarrow$ no swap.
- Compare `(24, 20)` $\rightarrow$ swap $\rightarrow$ `[13, 20, 24, 9, 46, 52]`
- Compare `(24, 9)` $\rightarrow$ swap $\rightarrow$ `[13, 20, 9, 24, 46, 52]`

**Array state below Pass 2:**
```text
[ 13, 20, 9 | 24, 46, 52 ]
```

---

### Pass 3 ($i = 2$)
We compare adjacent pairs from index `0` to `1`:
- Compare `(13, 20)` $\rightarrow$ no swap.
- Compare `(20, 9)` $\rightarrow$ swap $\rightarrow$ `[13, 9, 20, 24, 46, 52]`

**Array state below Pass 3:**
```text
[ 13, 9 | 20, 24, 46, 52 ]
```

---

### Pass 4 ($i = 1$)
We compare the pair at index `0`:
- Compare `(13, 9)` $\rightarrow$ swap $\rightarrow$ `[9, 13, 20, 24, 46, 52]`

**Array state below Pass 4:**
```text
[ 9 | 13, 20, 24, 46, 52 ]
```

**Final Sorted Array:**
`[9, 13, 20, 24, 46, 52]`

---

## ⚡ Optimization: Early Termination
If the array is already sorted, standard Bubble Sort will still perform all comparisons, resulting in $\mathcal{O}(N^2)$ operations. We can optimize it by tracking if any swap occurred during a pass. If no swaps are made during an entire inner loop, the array is sorted, and we can terminate early.

### Optimized Implementation
```python
def bubbleSortOptimized(nums):
    n = len(nums)
    for i in range(n - 1, -1, -1):
        did_swap = False
        for j in range(i):
            if nums[j + 1] < nums[j]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
                did_swap = True
        
        # If no elements were swapped, array is already sorted
        if not did_swap:
            break
            
    return nums
```

---

## 📊 Complexity Analysis

| Scenario | Time Complexity | Space Complexity | Description |
| :--- | :---: | :---: | :--- |
| **Best Case (Optimized)** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Occurs when the input array is already sorted. The algorithm detects this after 1 pass (with $N-1$ comparisons) and exits. |
| **Average Case** | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | Quadratic comparisons and swaps on average. |
| **Worst Case** | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | Occurs when the input array is sorted in reverse order, requiring swaps at every step. |
