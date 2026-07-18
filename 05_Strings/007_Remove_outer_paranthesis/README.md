# Remove Outermost Parentheses

🔗 **LeetCode Link**: [1021. Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/)

---

## 💡 Intuition & Core Concepts

### 1. Primitive Parentheses Strings
A valid parentheses string is **primitive** if it is non-empty and cannot be split into smaller non-empty valid parentheses strings.
- **Example**: `s = "(()())(())"` can be decomposed into two primitive parts:
  - `(()())` $\rightarrow$ Outer parentheses surround `()()`
  - `(())` $\rightarrow$ Outer parentheses surround `()`
- The goal is to identify each primitive block, strip the outermost `'('` (at the start of the block) and `')'` (at the end of the block), and concatenate the inner parts.

### 2. Identifying Primitive Boundaries
A primitive block always starts with an open parenthesis `'('` and ends when the parentheses are fully balanced for the first time.
- By tracking the balance (e.g., using a counter that changes on `'('` and `')'`), we know a primitive block has ended the moment the counter returns to `0`.

---

## 🛠️ Approaches

### Approach 1: Two-Pointer Primitive Boundary Scan (Implemented)
This approach uses two pointers (`l` and `r`) to track the start and end of each primitive block.

#### 🔄 Step-by-Step Logic
1. We maintain a `count` balance tracker (e.g., decrement on `'('` and increment on `')'`).
2. We increment the right pointer `r` as we process characters.
3. When `count` returns to `0`, we have identified a complete primitive block spanning from index `l` to `r - 1`.
4. We slice the inner contents `s[l + 1 : r - 1]` (which strips the outermost parentheses at `l` and `r - 1`) and append it to our result.
5. We set `l = r` to mark the start of the next primitive block and repeat.

- **Time Complexity**: $\mathcal{O}(N)$ where $N$ is the length of `s`. We traverse the string once, and slicing portions takes time proportional to their lengths.
- **Space Complexity**: $\mathcal{O}(N)$ to store the output string.

---

### Approach 2: Opened Count Tracker (Alternative / Cleaner Single-Pass)
This approach processes the string character by character in a single pass without slicing or two pointers, by keeping track of the depth of open parentheses.

#### 💡 Intuition
- An open parenthesis `'('` belongs to the inner content if and only if there is already at least one open parenthesis ahead of it (i.e., `opened > 0`).
- A close parenthesis `')'` belongs to the inner content if and only if it closes a parenthesis that is not the outermost one (i.e., `opened > 1` before decrementing, or `opened > 0` after decrementing).

#### Implementation
```python
def removeOuterParentheses(s: str) -> str:
    res = []
    opened = 0
    for char in s:
        if char == '(':
            if opened > 0:
                res.append(char)
            opened += 1
        elif char == ')':
            opened -= 1
            if opened > 0:
                res.append(char)
    return "".join(res)
```

- **Time Complexity**: $\mathcal{O}(N)$ because we iterate through the string exactly once.
- **Space Complexity**: $\mathcal{O}(N)$ to store the list of characters before joining them.

---

## 📊 Complexity Comparison

| Approach | Time Complexity | Space Complexity | Description |
| :--- | :--- | :--- | :--- |
| **1. Two-Pointer Scan** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | Identifies blocks explicitly using `l` and `r` boundaries, slicing the inner portions. |
| **2. Opened Count Tracker** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | Simpler logic, avoids string slicing and uses character-by-character filtering. |
