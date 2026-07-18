# Valid Anagram

Given two strings `s` and `t`, return `true` *if `t` is an anagram of `s`, and `false` otherwise.*

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

---

## 💡 Intuition & Core Concepts

### 1. What Makes an Anagram?
For string `t` to be an anagram of `s`, two conditions must be met:
1. **Identical Lengths**: Both strings must contain the exact same number of characters. If their lengths differ, it is impossible for them to be anagrams.
2. **Identical Frequencies**: Every unique character must appear the exact same number of times in both strings.

### 2. Python Specifics: `sorted()` vs `.sort()` for Strings
- **Strings are Immutable**: In Python, strings are immutable, meaning their characters cannot be modified in-place. As a result, strings do not have a `.sort()` method. Calling `s.sort()` will throw an `AttributeError`.
- **The `sorted()` Function**: To sort a string, we must use Python's built-in `sorted(s)` function. It treats the string as an iterable and **generates a brand-new list** containing the sorted characters (e.g., `sorted("anagram")` returns `['a', 'a', 'a', 'g', 'm', 'n', 'r']`).
- **Memory Cost**: Because a new list is constructed, this operation has an $\mathcal{O}(N)$ space complexity.

---

## 🛠️ Approaches

### Approach 1: Sorting (Alternative)
- **Logic**: If two strings are anagrams, sorting their characters alphabetically will produce identical sorted lists.
- **Time Complexity**: $\mathcal{O}(N \log N)$ where $N$ is the length of the strings, due to the sorting step.
- **Space Complexity**: $\mathcal{O}(N)$ in Python, as `sorted()` creates a new list of sorted characters.

---

### Approach 2: Frequency Count with Hash Maps (Implemented)
Instead of sorting, we can count character occurrences using hash maps (dictionaries) to achieve linear time complexity.

#### ⚙️ Optimizations & Logic Flow
1. **Length Guard Check**: We first verify if `len(s) == len(t)`. If not, we immediately return `False`.
2. **Parallel Traversal with `zip()`**: Because we verified the lengths are identical, we can use `zip(s, t)` to loop through characters of both strings concurrently. During this single pass, we build the frequency dictionaries `dict1` and `dict2`.
3. **Dictionary Comparison**: We compare the two dictionaries directly (`dict1 == dict2`). In Python, this check evaluates whether both dictionaries have the same keys and identical values.

- **Time Complexity**: $\mathcal{O}(N)$ where $N$ is the length of the strings. Traversing the strings takes $\mathcal{O}(N)$ time, and dictionary comparison takes $\mathcal{O}(K)$ time where $K \le N$ is the unique character count.
- **Space Complexity**: $\mathcal{O}(K)$ where $K$ is the size of the unique character set. Since the problem typically bounds the character set (e.g., 26 lowercase English letters), the space complexity is effectively $\mathcal{O}(1)$.

---

## 📊 Complexity Comparison

| Approach | Time Complexity | Space Complexity | Description |
| :--- | :--- | :--- | :--- |
| **1. Sorting** | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ | Simple one-liner, but slower due to sorting overhead. |
| **2. Frequency Count** | $\mathcal{O}(N)$ | $\mathcal{O}(K) \approx \mathcal{O}(1)$ | Optimal linear time approach using two hash maps. |
