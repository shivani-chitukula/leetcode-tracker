# Selection Sort

---

## 💡 Intuition & Core Concepts

The key idea behind **Selection Sort** is very simple:
> **Find the minimum element in the unsorted portion of the array and swap it with the first element of that unsorted portion.**

By repeating this process, we move the minimum values to the beginning of the list one-by-one, gradually building a sorted list from left to right.

### How it Works (Step-by-Step)
We divide the array conceptually into two partitions:
1. **Sorted Partition**: At the beginning of the array (initially empty).
2. **Unsorted Partition**: The remaining part of the array (initially the entire array).

In each pass $i$ (from index `0` to `n - 2`):
1. Assume the first element of the unsorted portion is the minimum: `mini = i`.
2. Scan the rest of the unsorted portion (from index `i` to `n - 1`) to find the actual minimum element's index.
3. If we find a smaller element, update `mini` to this index.
4. Swap the minimum element found at `mini` with the element at index `i`.
5. This index `i` is now part of the sorted partition. Expand the sorted boundary and repeat.

---

## 📝 Dry Run Example
Let's trace Selection Sort with the input array: `nums = [13, 46, 24, 52, 20, 9]`

### Initial State
```text
[ 13, 46, 24, 52, 20, 9 ]
  L                     R  (Unsorted Part: Index 0 to 5)
```

---

### Pass 0 ($i = 0$)
1. **Unsorted segment**: `[13, 46, 24, 52, 20, 9]`
2. Assume minimum is `13` (index 0). Scan remaining to find the actual minimum.
3. The smallest element is `9` (index 5).
4. Swap `9` (index 5) with `13` (index 0).

**Array state below Pass 0:**
```text
[ 9 | 46, 24, 52, 20, 13 ]
  S   L                R   (Sorted: [9] / Unsorted: Index 1 to 5)
```

---

### Pass 1 ($i = 1$)
1. **Unsorted segment**: `[46, 24, 52, 20, 13]`
2. Assume minimum is `46` (index 1). Scan remaining to find the actual minimum.
3. The smallest element is `13` (index 5).
4. Swap `13` (index 5) with `46` (index 1).

**Array state below Pass 1:**
```text
[ 9, 13 | 24, 52, 20, 46 ]
  Sorted   L            R  (Sorted: [9, 13] / Unsorted: Index 2 to 5)
```

---

### Pass 2 ($i = 2$)
1. **Unsorted segment**: `[24, 52, 20, 46]`
2. Assume minimum is `24` (index 2). Scan remaining to find the actual minimum.
3. The smallest element is `20` (index 4).
4. Swap `20` (index 4) with `24` (index 2).

**Array state below Pass 2:**
```text
[ 9, 13, 20 | 52, 24, 46 ]
  Sorted      L        R   (Sorted: [9, 13, 20] / Unsorted: Index 3 to 5)
```

---

### Pass 3 ($i = 3$)
1. **Unsorted segment**: `[52, 24, 46]`
2. Assume minimum is `52` (index 3). Scan remaining to find the actual minimum.
3. The smallest element is `24` (index 4).
4. Swap `24` (index 4) with `52` (index 3).

**Array state below Pass 3:**
```text
[ 9, 13, 20, 24 | 52, 46 ]
  Sorted          L    R   (Sorted: [9, 13, 20, 24] / Unsorted: Index 4 to 5)
```

---

### Pass 4 ($i = 4$)
1. **Unsorted segment**: `[52, 46]`
2. Assume minimum is `52` (index 4). Scan remaining to find the actual minimum.
3. The smallest element is `46` (index 5).
4. Swap `46` (index 5) with `52` (index 4).

**Array state below Pass 4:**
```text
[ 9, 13, 20, 24, 46 | 52 ]
  Sorted              L/R  (Sorted: [9, 13, 20, 24, 46] / Unsorted: Index 5)
```
*Note: Since there is only one element remaining in the unsorted partition, it is automatically sorted.*

**Final Sorted Array:**
`[9, 13, 20, 24, 46, 52]`

---

## 📊 Complexity Analysis

| Scenario | Time Complexity | Space Complexity | Description |
| :--- | :---: | :---: | :--- |
| **Best Case** | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | Even if the array is already sorted, it still scans the unsorted segment to find minimums. |
| **Average Case** | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | Average number of comparisons remains quadratic. |
| **Worst Case** | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | Worst-case comparisons are quadratic. |
