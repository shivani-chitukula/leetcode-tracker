# Reverse Words in a String

Given an input string `s`, reverse the order of the **words**. A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

Return *a string of the words in reverse order concatenated by a single space.*

> [!NOTE]
> `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

---

## 💡 Key Concepts

### 1. String Immutability in Python
In Python, strings are **immutable** sequences of Unicode characters. Once a string is created in memory, its characters cannot be modified in-place.
- **Implication**: Any operations like concatenation (`+`), replacing, or slicing create a brand-new string object in memory.
- **Performance Caution**: Constructing a string word-by-word using loops (e.g., `newstr += word + ' '`) is highly inefficient. It takes $\mathcal{O}(N^2)$ time because a new string copy is allocated and copied at every iteration.
- **Best Practice**: Collect substring tokens in a list (which is mutable) and join them once at the end using `" ".join()`. This runs in linear $\mathcal{O}(N)$ time.

### 2. The `split()` and `join()` Operations

#### `s.split()`
- When called without arguments, Python's `split()` automatically groups consecutive whitespace characters as a single delimiter.
- It discards leading and trailing whitespaces and ignores empty strings from the resulting list.
- **Example**: `"  hello   world  ".split()` returns `['hello', 'world']`.

#### `delimiter.join(iterable)`
- Concatenates the string elements of an iterable (e.g., a list of words) with the `delimiter` string placed between them.
- It is highly optimized in CPython, pre-calculating the exact length of the final string to allocate memory once, resulting in linear $\mathcal{O}(N)$ time.

---

## 🛠️ Approaches

### Approach 1: Split & Join (Pythonic Built-in)
This approach splits the string into a list of words, reverses the list using Python's built-in list reversal, and joins them back with a single space.

```python
def reverseWords(s: str) -> str:
    # 1. Split words (removes extra spaces automatically)
    words = s.split()
    # 2. Reverse the list of words
    words.reverse()
    # 3. Join with a single space
    return " ".join(words)
```

- **Time Complexity**: $\mathcal{O}(N)$ where $N$ is the length of string `s`. Splitting takes $\mathcal{O}(N)$, reversing takes $\mathcal{O}(W)$ (where $W$ is the number of words), and joining takes $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$ to store the list of words in memory.

---

### Approach 2: Split & Two-Pointer Swapping
This approach splits the string into a list of words first, then uses two pointers (`l` at the start and `r` at the end) to swap elements in-place within the list before joining.

```python
def reverseWords(s: str) -> str:
    # 1. Split the string into a list of words
    words = s.split()
    
    # 2. Reversal of the list using two pointers
    l = 0
    r = len(words) - 1
    while l < r:
        words[l], words[r] = words[r], words[l]
        l += 1
        r -= 1
        
    # 3. Join the list back to a string
    return " ".join(words)
```

- **Time Complexity**: $\mathcal{O}(N)$ because we traverse the list of words once to swap them.
- **Space Complexity**: $\mathcal{O}(N)$ since we must allocate space for the list of words due to Python's string immutability.

---

## 📊 Complexity Comparison

| Approach | Time Complexity | Space Complexity | Description |
| :--- | :--- | :--- | :--- |
| **Split & Join** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | Uses highly optimized built-in CPython list reversal. Clean and readable. |
| **Split & Two-Pointer** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | Manually reverses the word list using element swaps. Demonstrates pointer logic. |
