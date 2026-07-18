# Maximum Nesting Depth of the Parentheses

🔗 **LeetCode Link**: [1614. Maximum Nesting Depth of the Parentheses](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/)

---

## 💡 Intuition & Core Concepts

A valid parentheses string (VPS) can contain numbers, operators, and nested parentheses. The **nesting depth** represents the maximum number of nested parentheses surrounding any character in the string.

### 1. The Core Concept
- The maximum nesting depth is equivalent to the **maximum number of open parentheses `'('` that remain unmatched** at any point during a single left-to-right sweep of the string.
- Since the input is guaranteed to be a Valid Parentheses String (VPS), we do not need to worry about validation or boundary check errors (unbalanced parenthesis).

---

## 🛠️ Approaches

### Approach: Single-Pass Counting (Implemented)
This approach sweeps the string from left to right and tracks the active open parentheses depth.

#### 🔄 Step-by-Step Logic
1. **Initialize Trackers**: Maintain `tempCount` (current depth of open parentheses) and `maxCount` (maximum depth recorded so far), both starting at `0`.
2. **Scan the String**: Iterate character by character through the string:
   - If we encounter `'('`: We are entering a new nesting level $\rightarrow$ increment `tempCount` by `1`.
   - If we encounter `')'`: We are closing an open parenthesis, leaving a nesting level $\rightarrow$ decrement `tempCount` by `1`.
3. **Record Maximum**: At each step, update `maxCount = max(maxCount, tempCount)`.
4. **Return Results**: After traversing the entire string, return `maxCount`.

#### 📝 Dry Run Trace: `s = "(1)+((2))+(((3)))"`

| Character | Action | `tempCount` | `maxCount` | Note |
| :---: | :---: | :---: | :---: | :--- |
| `(` | Increment | 1 | 1 | Depth increases |
| `1` | Ignore | 1 | 1 | Non-parenthesis char |
| `)` | Decrement | 0 | 1 | Depth decreases |
| `+` | Ignore | 0 | 1 | Non-parenthesis char |
| `(` | Increment | 1 | 1 | Depth increases |
| `(` | Increment | 2 | 2 | Depth increases |
| `2` | Ignore | 2 | 2 | Non-parenthesis char |
| `)` | Decrement | 1 | 2 | Depth decreases |
| `)` | Decrement | 0 | 2 | Depth decreases |
| `+` | Ignore | 0 | 2 | Non-parenthesis char |
| `(` | Increment | 1 | 2 | Depth increases |
| `(` | Increment | 2 | 2 | Depth increases |
| `(` | Increment | 3 | 3 | **Peak Depth Reached** |
| `3` | Ignore | 3 | 3 | Non-parenthesis char |
| `)` | Decrement | 2 | 3 | Depth decreases |
| `)` | Decrement | 1 | 3 | Depth decreases |
| `)` | Decrement | 0 | 3 | Depth decreases |

---

## 📊 Complexity Analysis

| Approach | Time Complexity | Space Complexity | Description |
| :--- | :--- | :--- | :--- |
| **Single-Pass Counting** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Highly optimized one-pass sweep with constant helper space. |
