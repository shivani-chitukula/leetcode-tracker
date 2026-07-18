# Rotate String

Given two strings `s` and `goal`, return `True` *if and only if `s` can become `goal` after some number of shifts on `s`*.

A **shift** on `s` consists of moving the leftmost character of `s` to the rightmost position.
- For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

---

## 💡 Intuition & Core Concepts

### 1. The Rotate Property
Any rotation of a string `s` can be viewed as dividing `s` into two parts at some pivot index:
- Let `s = A + B`, where `A` represents the prefix of `s` that is shifted to the end, and `B` represents the remaining suffix.
- When we rotate `s`, the prefix `A` moves to the end, resulting in the rotated string: `B + A`.
- Therefore, `goal` is a valid rotation of `s` if and only if there exists a split such that `goal == B + A`.

---

### 2. The Shift Universe (All Possible Rotations)
A string of length $N$ can be shifted at most $N$ times before it cycles back to its original state. This means there are exactly $N$ possible rotated versions of `s`.

Let's trace all possible shifts for `s = "abcde"` ($N = 5$) and see where they appear inside `s + s` (`"abcdeabcde"`):

| Shift ($k$) | Shifted Prefix ($A$) | Remaining Suffix ($B$) | Resulting String ($B + A$) | Location in `s + s` (`"abcdeabcde"`) |
| :---: | :---: | :---: | :---: | :--- |
| **0** | `""` | `"abcde"` | `"abcde"` | **`[abcde]`**`abcde` (Index 0) |
| **1** | `"a"` | `"bcde"` | `"bcdea"` | `a`**`[bcdea]`**`bcde` (Index 1) |
| **2** | `"ab"` | `"cde"` | `"cdeab"` | `ab`**`[cdeab]`**`cde` (Index 2) |
| **3** | `"abc"` | `"de"` | `"deabc"` | `abc`**`[deabc]`**`de` (Index 3) |
| **4** | `"abcd"` | `"e"` | `"eabcd"` | `abcd`**`[eabcd]`**`e` (Index 4) |

Since the search space of all valid rotations is completely covered by the substrings of `s + s`, checking if `goal` is a substring of `s + s` will always determine if it is a valid rotation.

---

### 3. General Algebraic Proof
We can generalize this behavior mathematically. Let any shift of `s` partition the string into two halves:
- Let `s = A + B`, where `A` is the prefix of length $k$ that gets shifted, and `B` is the remaining suffix.
- The rotated version of `s` (the `goal`) is represented as `B + A`.

When we concatenate `s` with itself, we get:
$$\text{s} + \text{s} = (A + B) + (A + B) = A + \mathbf{(B + A)} + B$$

The target rotated string $\mathbf{(B + A)}$ is embedded inside the concatenated string.

#### Requirements for the Substring Check:
1. **Length Check**: The strings `s` and `goal` must have the same length (`len(s) == len(goal)`). If we omit this check, a shorter string that happens to be a substring of `s + s` would incorrectly return `True` (e.g., if `s = "abc"` and `goal = "ab"`, `goal in s + s` is `True` but `"ab"` is not a rotation of `"abc"`).
2. **Substring Check**: `goal` must be a substring of `s + s`.

---

## 🛠️ Approaches

### Approach 1: Simulation (Linear Shifts)
- **Logic**: We can simulate the shift process step-by-step. In each step, we pop the first character of `s` and append it to the end. We repeat this $N$ times (where $N = \text{len}(s)$). If at any point the shifted string matches `goal`, we return `True`. If no match is found after $N$ shifts, we return `False`.
- **Time Complexity**: $\mathcal{O}(N^2)$ because we do $N$ shifts, and each string slice/concatenation takes $\mathcal{O}(N)$ time.
- **Space Complexity**: $\mathcal{O}(N)$ to store the temporary shifted string.

---

### Approach 2: Concatenation & Substring Search (Optimized & Implemented)
- **Logic**: Check if `len(s) == len(goal)`. If so, search for `goal` inside the concatenated string `s + s`.
- **Time Complexity**: $\mathcal{O}(N)$ on average. In Python, the `in` operator for string substring search uses an optimized Boyer-Moore-Horspool algorithm under the hood, running in linear time.
- **Space Complexity**: $\mathcal{O}(N)$ to construct the concatenated string `s + s`.

---

## 📊 Complexity Comparison

| Approach | Time Complexity | Space Complexity | Description |
| :--- | :--- | :--- | :--- |
| **1. Simulation** | $\mathcal{O}(N^2)$ | $\mathcal{O}(N)$ | Brute-force approach that simulates each character shift individually. |
| **2. Concatenation (`s + s`)** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | Elegant mathematical approach leveraging the substring property of rotations. |
