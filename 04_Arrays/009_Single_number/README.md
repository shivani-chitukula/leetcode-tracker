# Single Number

[LeetCode Problem Link](https://leetcode.com/problems/single-number/)

Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

---

## 1. Hashing Approach (Frequency Map)
- **Logic**: Maintain a frequency map (using `Counter` or a dictionary) to keep track of the occurrences of each element. Iterate through the frequency map to find the element that appears exactly once.
- **Time Complexity (TC)**: $\mathcal{O}(N)$ (one pass to count frequencies, and another pass to find the single element)
- **Space Complexity (SC)**: $\mathcal{O}(N)$ (to store up to $N/2 + 1$ unique elements in the map)

---

## 2. Bit Manipulation Approach (XOR - Optimal)
- **Logic**: Use the bitwise XOR operator ($\oplus$). 
  - **XOR Properties**:
    - **XOR of a number with itself is 0**: $x \oplus x = 0$ (identical bits cancel out).
    - **XOR of a number with 0 is the number itself**: $x \oplus 0 = x$.
  - By XORing all numbers in the array together, the numbers appearing twice cancel out, leaving only the single number.
  $$\text{result} = a \oplus b \oplus a \oplus b \oplus c = (a \oplus a) \oplus (b \oplus b) \oplus c = 0 \oplus 0 \oplus c = c$$

  ### XOR Truth Table (Binary)
  | Bit A | Bit B | A ⊕ B | Description |
  | :---: | :---: | :---: | :--- |
  | 0 | 0 | **0** | Same inputs cancel out to 0 |
  | 0 | 1 | **1** | Different inputs result in 1 |
  | 1 | 0 | **1** | Different inputs result in 1 |
  | 1 | 1 | **0** | Same inputs cancel out to 0 |

- **Time Complexity (TC)**: $\mathcal{O}(N)$ (single pass scan of the array)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ (uses constant auxiliary space)

---

## Summary Table

| Approach | Time Complexity (TC) | Space Complexity (SC) | Description |
| :--- | :--- | :--- | :--- |
| **Hashing** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | Store counts in a dictionary/map; requires extra memory. |
| **Bit Manipulation (Optimal)** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | XOR all numbers to cancel out duplicates; matches the $\mathcal{O}(1)$ space requirement. |
