# Largest Odd Number in String

🔗 **LeetCode Link**: [1903. Largest Odd Number in String](https://leetcode.com/problems/largest-odd-number-in-string/)

Given a string `num` representing a large integer, return *the largest-valued odd integer (as a string) that is a non-empty substring of `num`, or an empty string `""` if no odd integer exists.*

---

## 💡 Intuition & Core Concepts

### 1. What Makes a Number Odd?
In the decimal (base-10) system, the parity (even or odd) of any integer is determined **solely by its last (rightmost) digit**.
- If the last digit is `1, 3, 5, 7, or 9`, the entire number is **odd**.
- If the last digit is `0, 2, 4, 6, or 8`, the entire number is **even**.
- *Why?* Any integer can be represented as $10 \times k + d$, where $d$ is the unit digit. Since $10 \times k$ is always divisible by 2 (even), the parity of the entire number depends entirely on the parity of $d$.

### 2. How Do We Maximize the Substring?
To find the **largest-valued** odd substring:
1. **Length Dominates Value**: For positive integers, a number with more digits is always larger than a number with fewer digits (e.g., $42061 > 2061$).
2. **Keep the Prefix**: To maximize the value of any substring ending at a specific index `i`, we must extend it as far left as possible. Therefore, the optimal substring will always start at the very beginning of the string (index `0`).
3. **Right-to-Left Search**: Since we want the longest possible prefix ending with an odd digit, we should scan the string from **right to left** (from `len(num) - 1` down to `0`).
4. **First Match is the Best Match**: The first odd digit we encounter from the right will mark the end of the largest odd prefix substring. We can immediately slice the string and return `num[:i+1]`.

---

## 🛠️ Implementation

### Greedy Right-to-Left Scan
Refer to [002_Largest_Odd_Number_String.py](file:///c:/Users/chitukula%20shivani/Desktop/leetcode-tracker/05_Strings/002_Largest_Odd_Number_String/002_Largest_Odd_Number_String.py) for the complete implementation.

### Dry Run Example: `num = "42061"`
- `i = 4`: `num[4]` is `'1'`. `int('1') % 2 != 0` is `True`.
- Since `'1'` is odd, we immediately return the prefix `num[:4+1]` which is `"42061"`.

---

## 📊 Complexity Analysis

- **Time Complexity**: $\mathcal{O}(N)$ where $N$ is the length of the string `num`. In the worst case (e.g., all even digits or no odd digits), we traverse the entire string once. String slicing `num[:i+1]` also takes $\mathcal{O}(N)$ time.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space (excluding the space for the returned substring) as we only use index variables.
