# Second Largest and Second Smallest Element

Find the second largest and second smallest elements in a given array.

---

## 1. Sorting Approach
- **Logic**: Convert the array to a set to remove duplicates, sort the unique elements in ascending order, and return the second element from the start (index 1) and the second element from the end (index -2).
- **Time Complexity (TC)**: $\mathcal{O}(N \log N)$ (due to sorting the unique values)
- **Space Complexity (SC)**: $\mathcal{O}(N)$ (to store the unique values in memory)

---

## 2. Optimal Approach (Single Pass Linear Scan)
- **Logic**: Traverse the array in a single loop. Maintain four tracking variables (`small`, `second_small`, `large`, `second_large`).
  - For each element, update the smallest/second smallest boundaries.
  - Independently, update the largest/second largest boundaries.
- **Time Complexity (TC)**: $\mathcal{O}(N)$ (single pass scan of the array)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ (uses constant auxiliary space)

---

## Summary Table

| Approach | Time Complexity (TC) | Space Complexity (SC) | Description |
| :--- | :--- | :--- | :--- |
| **Sorting** | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ | Remove duplicates, sort, and select index. |
| **Optimal Scan** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Single pass scan tracking boundary variables. |
