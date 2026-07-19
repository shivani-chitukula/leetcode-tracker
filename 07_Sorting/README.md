# ⚡ Basic Sorting Algorithms

This folder contains implementations and notes for the three fundamental quadratic sorting algorithms: **Selection Sort**, **Bubble Sort**, and **Insertion Sort**. All three are in-place comparison-based algorithms but differ significantly in how they build the sorted sequence.

---

## 💡 Core Intuition Differences

| Algorithm | Primary Action | Conceptual Analogy |
| :--- | :--- | :--- |
| **Selection Sort** | **Select the minimum** from the unsorted part and place it at the beginning. | Scanning a shelf of books to find the shortest one, then swapping it with the first book. |
| **Bubble Sort** | **Bubble up the maximum** to the end of the array by comparing and swapping adjacent elements. | Bubbles rising in water—the largest bubbles (numbers) rise to the top (end of the list) first. |
| **Insertion Sort** | **Insert the next element** into its correct sorted position within the already sorted prefix. | Sorting a hand of playing cards: picking one card at a time and inserting it into the correct position. |

---

## 🔍 Key Differences Explained

### 1. Stability (Does it preserve duplicate order?)
- **Selection Sort (Unstable)**: Swapping the minimum element to the front can jump over identical elements, changing their relative order.
  - *Example*: `[2a, 2b, 1]` $\rightarrow$ `1` is swapped with `2a` $\rightarrow$ `[1, 2b, 2a]`. The relative order of `2a` and `2b` is reversed.
- **Bubble Sort (Stable)**: Only swaps adjacent elements if they are strictly out of order (`nums[j] > nums[j+1]`). Equal elements are never swapped.
- **Insertion Sort (Stable)**: Moves elements backward until it finds an element less than or equal to the target. It does not move the target past equal elements.

### 2. Adaptability (Does it run faster if already sorted?)
- **Selection Sort (Non-Adaptive)**: It **always** scans the entire remaining unsorted segment to find the minimum. It performs $\mathcal{O}(N^2)$ comparisons regardless of whether the input is sorted, reversed, or random.
- **Bubble Sort (Adaptive - Optimized)**: With the early-termination optimization (`did_swap` flag), it can exit after a single pass ($\mathcal{O}(N)$ comparisons) if the array is already sorted.
- **Insertion Sort (Highly Adaptive)**: If the array is already sorted, the inner loop comparison fails immediately on the first check. It only makes 1 comparison per element, resulting in $\mathcal{O}(N)$ comparisons. It is also extremely fast for *nearly sorted* arrays.

---

## 📊 Summary Comparison Table

| Algorithm | Best Case Time | Avg Case Time | Worst Case Time | Space Complexity | Stable? | Adaptive? |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Selection Sort** | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | ❌ No | ❌ No |
| **Bubble Sort** | $\mathcal{O}(N)$ (opt.) | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ |  Yes |  Yes |
| **Insertion Sort** | $\mathcal{O}(N)$ | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ |  Yes |  Yes |

---

## 🏆 Which is best in practice?
Among the three quadratic algorithms, **Insertion Sort is generally the most efficient in practice**:
- It does not perform unnecessary swaps.
- It has very low constant factors.
- It is the algorithm of choice for sorting very small datasets (many high-performance sorting library hybrids, like Timsort or IntroSort, fallback to Insertion Sort when subarray sizes drop below a certain threshold, e.g., 10–64 elements).
