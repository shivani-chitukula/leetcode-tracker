# Longest Palindromic Substring

🔗 **LeetCode Link**: [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

---

## 💡 Intuition & Core Concepts

A palindrome reads the same backward as forward (e.g., `"aba"`, `"racecar"`, `"abba"`). Every palindromic substring has a **center**.

### 1. Types of Centers
There are two possibilities for a palindrome's center:
1. **Odd-Length Palindromes**: Have a single character as the center (e.g., `"aba"`, center is `'b'`).
2. **Even-Length Palindromes**: Have a boundary between two characters as the center (e.g., `"abba"`, center is between the two `'b'`s).

---

## 🛠️ Approaches

### Approach 1: Expand Around Center (Implemented)
Instead of checking every substring, we can treat each position in the string as a potential center and expand outwards to check for palindromes.

#### 🔄 Step-by-Step Logic
For each index `i` from `0` to `len(s) - 1`:
1. **Odd-Length Palindromes**: Initialize pointers `l = i` and `r = i`. Expand outward (`l -= 1`, `r += 1`) while the characters match (`s[l] == s[r]`) and pointers stay within boundaries.
2. **Even-Length Palindromes**: Initialize pointers `l = i` and `r = i + 1`. Expand outward while the characters match.
3. **Update Result**: Track the maximum length of palindromic substring found, and slice `s[l:r+1]` to save the longest match.

- **Time Complexity**: $\mathcal{O}(N^2)$ where $N$ is the length of `s`. We have $2N - 1$ centers (one for each character, and one for each boundary between characters), and for each center, expanding can take up to $\mathcal{O}(N)$ time.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space, since we only use pointers and integer variable values to search (excluding the space required to return the output string).

#### 📝 Dry Run Trace: `s = "babad"`

| Index `i` | Palindrome Type | Center Check | Max Palindrome Found | Notes |
| :---: | :---: | :---: | :---: | :--- |
| `0` | Odd | `s[0:1]` = `"b"` | `"b"` | Initial state |
| `1` | Odd | `s[1:2]` = `"a"` $\rightarrow$ Expand to `s[0:3]` = `"bab"` | `"bab"` | Outer characters `'b'` match |
| `1` | Even | `s[1:3]` = `"ab"` | `"bab"` | `'a'` and `'b'` mismatch |
| `2` | Odd | `s[2:3]` = `"b"` $\rightarrow$ Expand to `s[1:4]` = `"aba"` | `"bab"` (or `"aba"`) | Outer characters `'a'` match |
| `2` | Even | `s[2:4]` = `"ba"` | `"bab"` | Mismatch |

---

### Approach 2: Dynamic Programming (Alternative)
- **Logic**: We define a table `dp[i][j]` which is `True` if `s[i..j]` is a palindrome.
  - **Base cases**: `dp[i][i] = True` (all single characters), and `dp[i][i+1] = (s[i] == s[i+1])` (adjacent equal characters).
  - **Transition**: `dp[i][j] = (s[i] == s[j] and dp[i+1][j-1])`.
- **Time Complexity**: $\mathcal{O}(N^2)$
- **Space Complexity**: $\mathcal{O}(N^2)$ to store the DP table.

---


## 📊 Complexity Comparison

| Approach | Time Complexity | Space Complexity | Description |
| :--- | :--- | :--- | :--- |
| **Expand Around Center** | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | Highly efficient space-wise. Avoids state allocation. |
| **Dynamic Programming** | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | Simple logic, but consumes significant memory. |

