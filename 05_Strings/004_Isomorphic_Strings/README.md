# Isomorphic Strings

🔗 **LeetCode Link**: [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)

Given two strings `s` and `t`, determine if they are isomorphic. 

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`. All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

---

## 💡 Intuition & Core Concepts

### 1. What is Isomorphism?
For two strings to be isomorphic, there must be a **one-to-one mapping (bijection)** between the characters of `s` and `t` at each position.
- Every character $c_1$ in `s` must map to exactly one character $c_2$ in `t`.
- Every character $c_2$ in `t` must map to exactly one character $c_1$ in `s`.

### 2. Why a Single Map is Not Enough
If we only use a single mapping (e.g., `s` to `t`), we might map different characters in `s` to the same character in `t`.
- **Example**: `s = "badc"`, `t = "baba"`
  - `'b'` $\rightarrow$ `'b'`
  - `'a'` $\rightarrow$ `'a'`
  - `'d'` $\rightarrow$ `'b'` (Invalid! `'b'` in `t` is already mapped to by `'b'` in `s`)
  - `'c'` $\rightarrow$ `'a'` (Invalid! `'a'` in `t` is already mapped to by `'a'` in `s`)
- If we only check `s_to_t`, a naive check would miss the fact that multiple characters from `s` mapped to the same target character in `t`. 
- To establish a bijection, we either need **two hash maps** (cross-referencing each other) or a **hash map + a set** of already mapped values.

---

## 🛠️ Approaches

### Approach 1: Single Hash Map with Value Scan (Naive)
This approach uses a single dictionary `d` to keep track of the mapping from `s` to `t`.
- **Logic**: For each index `i`, if `s[i]` is not yet in the map, we check if `t[i]` has already been assigned to another character. We do this by scanning all values currently in `d` (`for k, v in d.items()`). If `t[i]` is already mapped, we return `False`. Otherwise, we set `d[s[i]] = t[i]`.
- **Time Complexity**: $\mathcal{O}(N \cdot K)$, where $N$ is the string length and $K$ is the number of unique characters. Scanning the dictionary values takes $\mathcal{O}(K)$ time at each step.
- **Space Complexity**: $\mathcal{O}(K)$ to store the mapping.

---

### Approach 2: Two Hash Maps / Bidirectional Mapping (Optimized & Implemented)
This approach avoids the linear search over dictionary values by maintaining two separate dictionaries: `s_to_t` and `t_to_s`.

#### 💡 Intuition
By storing the mapping in both directions, we can verify that no two characters map to the same target character using simple dictionary key lookups, which take $\mathcal{O}(1)$ time on average.

#### ⚙️ The `zip(s, t)` function
- `zip(s, t)` creates an iterator of tuples where the $i$-th tuple contains the $i$-th element from each of the input strings.
- **Example**: `zip("badc", "baba")` yields `('b', 'b')`, `('a', 'a')`, `('d', 'b')`, `('c', 'a')`.
- This allows us to traverse both strings in parallel clean, Pythonic syntax without manual index variables (like `i`).

#### 🔄 Step-by-Step Logic
For each pair `(c1, c2)` in `zip(s, t)`:
1. If `c1` already exists in `s_to_t` but points to a character other than `c2`, we have a conflict $\rightarrow$ return `False`.
2. If `c2` already exists in `t_to_s` but points to a character other than `c1`, we have a conflict $\rightarrow$ return `False`.
3. If neither check fails, store the mapping in both maps: `s_to_t[c1] = c2` and `t_to_s[c2] = c1`.

- **Time Complexity**: $\mathcal{O}(N)$ because we iterate through the strings once, and hash map lookups and insertions are $\mathcal{O}(1)$ on average.
- **Space Complexity**: $\mathcal{O}(K)$ where $K$ is the unique character set size. Since the character set is bounded (e.g. 256 for ASCII), this is practically $\mathcal{O}(1)$.

---

## 📊 Complexity Comparison

| Approach | Time Complexity | Space Complexity | Description |
| :--- | :--- | :--- | :--- |
| **1. Single Map (Value Scan)** | $\mathcal{O}(N \cdot K)$ | $\mathcal{O}(K)$ | Slow because of the $\mathcal{O}(K)$ scan of dictionary values to prevent duplicate mapping. |
| **2. Two Maps (zip)** | $\mathcal{O}(N)$ | $\mathcal{O}(K)$ | Fast and clean. Uses bidirectional maps to verify bijection in $\mathcal{O}(1)$ lookup time. |
