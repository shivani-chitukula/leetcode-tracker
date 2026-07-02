# Largest Element in an Array

Find the largest element in a given array.

---

## 1. Sorting Approach
- **Logic**: Sort the array in ascending order and return the last element (at index -1).
- **Time Complexity (TC)**: $\mathcal{O}(N \log N)$ (due to sorting)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ or $\mathcal{O}(N)$ (depending on the sorting algorithm implementation details)

---

## 2. Iterative Approach (Linear Scan)
- **Logic**: Maintain a `maxi` variable, iterate through the array once, and update `maxi` whenever a larger element is found.
- **Time Complexity (TC)**: $\mathcal{O}(N)$ (traverses the array exactly once)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ (uses constant extra space)

---

## 3. Built-in Function
- **Logic**: Use the built-in `max()` library utility.
- **Time Complexity (TC)**: $\mathcal{O}(N)$ (scans the array once)
- **Space Complexity (SC)**: $\mathcal{O}(1)$

---

## Summary Table

| Approach | Time Complexity (TC) | Space Complexity (SC) | Description |
| :--- | :--- | :--- | :--- |
| **Sorting** | $\mathcal{O}(N \log N)$ | $\mathcal{O}(1)$ / $\mathcal{O}(N)$ | Sub-optimal due to sorting overhead |
| **Linear Scan** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Optimal, custom traversal |
| **Built-in `max()`** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Optimal, clean & Pythonic |
