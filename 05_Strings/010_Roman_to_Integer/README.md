# Roman to Integer

🔗 **LeetCode Link**: [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

---

## 💡 Intuition & Core Concepts

Roman numerals are written from left to right, usually starting with the largest values and ending with the smallest. However, there are exceptions where subtraction is used:
- If a smaller numeral is placed **before** a larger numeral, it means the smaller value is subtracted from the larger value (e.g., `IV` = $5 - 1 = 4$).
- Otherwise, the values are simply added (e.g., `VI` = $5 + 1 = 6$).

### Roman Symbol Value Mapping
| Symbol | Value |
| :---: | :---: |
| **I** | 1 |
| **V** | 5 |
| **X** | 10 |
| **L** | 50 |
| **C** | 100 |
| **D** | 500 |
| **M** | 1000 |

---

## 🛠️ Approaches

### Approach: Compare Adjacent Values (Implemented)
This approach traverses the Roman numeral string from left to right, comparing each symbol with its adjacent successor to identify subtraction cases.

#### 🔄 Step-by-Step Logic
1. **Dictionary Lookup**: Map each Roman character to its corresponding integer value.
2. **Left-to-Right Traversal**: Initialize a pointer `i = 0` and a running sum `num = 0`.
3. **Compare Neighbors**: While `i < len(s)`:
   - If there is a next character (`i < len(s) - 1`) and its value is **strictly greater** than the current character's value (`d[s[i+1]] > d[s[i]]`):
     - We have a subtraction case (e.g., `IX`, `CD`).
     - Add the difference `d[s[i+1]] - d[s[i]]` to `num`.
     - Skip both characters by advancing the pointer `i` by `2`.
   - Otherwise:
     - We have a standard addition case.
     - Add the value `d[s[i]]` to `num`.
     - Advance the pointer `i` by `1`.
4. **Return Result**: Return the accumulated sum `num`.

#### 📝 Dry Run Trace: `s = "MCMXCIV"` (1994)

| Pointer `i` | Pair Checked | Comparison | Action Taken | Current `num` |
| :---: | :---: | :---: | :---: | :---: |
| `0` | `'M'` (and next `'C'`) | `d['C'] (100) > d['M'] (1000)` is `False` | Add `d['M'] (1000)` $\rightarrow$ Advance by 1 | `1000` |
| `1` | `'C'` (and next `'M'`) | `d['M'] (1000) > d['C'] (100)` is `True` | Add `1000 - 100 = 900` $\rightarrow$ Advance by 2 | `1900` |
| `3` | `'X'` (and next `'C'`) | `d['C'] (100) > d['X'] (10)` is `True` | Add `100 - 10 = 90` $\rightarrow$ Advance by 2 | `1990` |
| `5` | `'I'` (and next `'V'`) | `d['V'] (5) > d['I'] (1)` is `True` | Add `5 - 1 = 4` $\rightarrow$ Advance by 2 | `1994` |

---

## 📊 Complexity Analysis

| Approach | Time Complexity | Space Complexity | Description |
| :--- | :--- | :--- | :--- |
| **Adjacent Comparison** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Single pass execution. The mapping dictionary contains only 7 key-value pairs (constant helper space). |
