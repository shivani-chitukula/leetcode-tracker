# Sort Characters By Frequency

🔗 **LeetCode Link**: [451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)

---

## 💡 Intuition & Core Concepts

The goal is to sort a string `s` in decreasing order based on the frequency of its characters. 
- **Example**: `s = "tree"`
  - `'e'` appears 2 times.
  - `'t'` appears 1 time.
  - `'r'` appears 1 time.
  - A valid sorted output is `"eetr"` or `"eert"`.
  
To solve this, we must:
1. Count the occurrences of each character.
2. Group and order the characters based on their count in descending order.
3. Build the final string by replicating each character according to its count.

---

## 🛠️ Approaches

### Approach 1: Frequency Map & Sorting (Implemented)
This approach counts character frequencies and then sorts the characters based on their counts.

#### 🔄 Step-by-Step Logic
1. **Count Frequencies**: Use a frequency map (like Python's `collections.Counter`) to count the occurrences of each character.
2. **Sort by Frequency**: Sort the map's elements based on their count values in descending order.
3. **Reconstruct String**: Iterate through the sorted character-frequency pairs, repeat each character by its frequency (`char * frequency`), and concatenate them to build the output string.

- **Time Complexity**: $\mathcal{O}(N + K \log K)$ where $N$ is the length of string `s` and $K$ is the number of unique characters. Counting frequencies takes $\mathcal{O}(N)$, sorting the unique character keys takes $\mathcal{O}(K \log K)$, and reconstructing the string takes $\mathcal{O}(N)$. Since $K \le 256$ for standard ASCII character sets, sorting is effectively $\mathcal{O}(1)$, resulting in an overall time complexity of $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N + K)$ to store the frequency dictionary and the result string.


---

## 📊 Complexity Analysis

| Approach | Time Complexity | Space Complexity | Description |
| :--- | :--- | :--- | :--- |
| **Frequency Map & Sort** | $\mathcal{O}(N + K \log K)$ | $\mathcal{O}(N + K)$ | Simple and intuitive. Extremely fast when the count of unique characters $K$ is small. |
