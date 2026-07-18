# Longest Common Prefix

🔗 **LeetCode Link**: [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`.

---

## 🛠️ Approaches

### Approach 1: Vertical Scanning (Implemented)
This approach compares characters of the strings column by column (vertically), starting from the first character (index `0`).

#### 💡 Intuition
Instead of comparing the first string with the second, then the result with the third (Horizontal Scanning), we compare the characters at index `i` across all strings simultaneously. 
- We iterate through each character of the first string `strs[0]`.
- For each character at index `i`, we check if it matches the character at index `i` of all other strings.
- If we hit a string that is shorter than `i` or has a mismatching character, we immediately return the prefix up to `i` (`strs[0][:i]`).


- **Time Complexity**: $\mathcal{O}(S)$ in the worst case, where $S$ is the sum of all characters in all strings. In the best case, it terminates after $\mathcal{O}(N)$ comparisons if the first character doesn't match.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space, since we do not use any extra memory other than the returned slice.

---

### Approach 2: Sorting (Alternative)
This approach sorts the list of strings first and then compares only the first and last strings.

#### 💡 Intuition
Sorting the strings alphabetically guarantees that the first string and the last string in the sorted list are the **most different** from each other. 
- Any common prefix shared by all strings must be shared by the alphabetically first and last strings.
- Therefore, we only need to compare the first string (`strs[0]`) and the last string (`strs[-1]`) of the sorted list.

#### Implementation
```python
def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""
        
    strs.sort()
    first, last = strs[0], strs[-1]
    i = 0
    
    # Compare character by character
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
        
    return first[:i]
```

- **Time Complexity**: $\mathcal{O}(N \cdot M \log N)$ where $N$ is the number of strings and $M$ is the maximum length of a string, due to the sorting step.
- **Space Complexity**: $\mathcal{O}(N \cdot M)$ or $\mathcal{O}(1)$ depending on the space complexity of the sorting algorithm.

---

## 📊 Complexity Comparison

| Approach | Time Complexity | Space Complexity | Best-use Case |
| :--- | :--- | :--- | :--- |
| **Vertical Scanning** | $\mathcal{O}(S)$ (Worst) / $\mathcal{O}(1)$ (Best) | $\mathcal{O}(1)$ | Highly efficient for early mismatches or short prefixes. |
| **Sorting** | $\mathcal{O}(N \cdot M \log N)$ | $\mathcal{O}(1)$ or $\mathcal{O}(N \cdot M)$ | Clean code, works well when $N$ is small. |
