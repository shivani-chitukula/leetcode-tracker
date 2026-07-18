# Longest Substring Without Repeating Characters

🔗 **LeetCode Link**: [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

## 💡 Intuition & Core Concepts

The goal is to find the length of the longest substring (a contiguous sequence of characters) that does not contain any duplicate characters.

### 1. Sliding Window Technique
To do this efficiently, we can use a **sliding window** defined by two pointers: `i` (left boundary) and `j` (right boundary).
- The window `[i, j]` represents the substring currently under examination.
- We expand the window by moving `j` to the right.
- If we encounter a character that is already inside the window, we must shrink the window from the left (by moving `i` to the right) until the duplicate is removed.

---

## 🛠️ Approaches

### Approach 1: Sliding Window with Set (Implemented)
This approach uses a Hash Set to track the unique characters currently inside the sliding window.

#### 🔄 Step-by-Step Logic
1. **Initialize trackers**: Create an empty set `temp`, left pointer `i = 0`, and `maxlen = 0`.
2. **Expand window**: Move the right pointer `j` from `0` to `len(s) - 1`.
3. **Handle duplicates**: If `s[j]` is already in `temp`:
   - Keep removing `s[i]` from the set and increment `i` until `s[j]` is no longer in `temp`.
4. **Update window state**: Add `s[j]` to `temp` and compute the window size `j - i + 1`. Update `maxlen = max(maxlen, j - i + 1)`.
5. **Return result**: `maxlen`.

- **Time Complexity**: $\mathcal{O}(N)$ where $N$ is the length of string `s`. Although there is a nested loop, each character is added to the set once and removed at most once. Hence, the pointers `i` and `j` make at most $2N$ steps in total.
- **Space Complexity**: $\mathcal{O}(\min(N, M))$ where $M$ is the size of the character set (alphabet size). The set will store at most the unique characters in the string.


---

## 📊 Complexity Analysis

| Approach | Time Complexity | Space Complexity | Description |
| :--- | :--- | :--- | :--- |
| **Sliding Window (Set)** | $\mathcal{O}(N)$ | $\mathcal{O}(\min(N, M))$ | Uses a set to track duplicates. Window shrinks character-by-character. |
