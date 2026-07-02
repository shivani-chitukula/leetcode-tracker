# Largest Element in an Array

Find the largest element in a given array.

---

## 1. Sorting Approach
Sort the array in ascending order and return the last element.
```python
def largest(arr):
    arr.sort()
    return arr[-1]
```
- **Time Complexity (TC)**: $\mathcal{O}(N \log N)$ (due to sorting)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ or $\mathcal{O}(N)$ (depending on the sorting algorithm implementation)

---

## 2. Iterative Approach (Linear Scan)
Loop through the array, keeping track of the maximum element seen so far.
```python
def largest(arr):
    maxi = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > maxi:
            maxi = arr[i]
    return maxi
```
- **Time Complexity (TC)**: $\mathcal{O}(N)$ (requires a single pass through the array)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ (uses constant extra space)

---

## 3. Built-in `max()` Function
Use Python's highly optimized built-in `max()` function.
```python
def largest(arr):
    return max(arr)
```
- **Time Complexity (TC)**: $\mathcal{O}(N)$ (scans the array once)
- **Space Complexity (SC)**: $\mathcal{O}(1)$

---

## Summary Table

| Approach | Time Complexity (TC) | Space Complexity (SC) | Remarks |
| :--- | :--- | :--- | :--- |
| **Sorting** | $\mathcal{O}(N \log N)$ | $\mathcal{O}(1)$ / $\mathcal{O}(N)$ | Sub-optimal due to sorting overhead |
| **Iterative** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Optimal, standard algorithm |
| **Built-in `max()`** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Optimal, clean & Pythonic |
