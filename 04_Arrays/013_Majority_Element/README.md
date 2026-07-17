# Majority Element

[LeetCode Problem Link](https://leetcode.com/problems/majority-element/)

Given an array `nums` of size `n`, return the *majority element*.

The **majority element** is the element that appears more than $\lfloor n / 2 \rfloor$ times. You may assume that the majority element always exists in the array.

---

## 1. Brute Force / Sorting Approach

### Intuition
If an element appears more than $\lfloor n / 2 \rfloor$ times in the array, it means that when the array is sorted, this element will always occupy the middle index (index $n // 2$).
- No matter where the majority element starts or ends, its length is greater than half of the array, so it is guaranteed to cross the center.

### Algorithm
1. Sort the array `nums` in ascending order.
2. Return the element at index `n // 2`.

- **Time Complexity (TC)**: $\mathcal{O}(N \log N)$ (due to the sorting algorithm)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ or $\mathcal{O}(N)$ (depending on the sorting method used; Python's `sort()` uses Timsort which takes $\mathcal{O}(N)$ space in the worst case)

---

## 2. Better Approach (Hash Map / Frequency Counter)

### Intuition
We can keep track of the occurrences of each element in the array using a Hash Map (or `Counter` in Python).
1. Traverse the array and populate a frequency dictionary.
2. Iterate through the dictionary to find the element whose frequency is strictly greater than $\lfloor n / 2 \rfloor$.

- **Time Complexity (TC)**: $\mathcal{O}(N)$ (we traverse the array once to count frequencies, and then search the map of size at most $N$)
- **Space Complexity (SC)**: $\mathcal{O}(N)$ (to store the frequencies of the elements in the hash map)

---

## 3. Optimal Approach (Boyer-Moore Voting Algorithm)

### Intuition
The Boyer-Moore Voting Algorithm is an optimal, single-pass algorithm that finds the majority element using $\mathcal{O}(1)$ extra space.

Think of it as a battle or election:
* We maintain a candidate (`element`) and a vote counter (`count`).
* As we iterate through the array:
  * If `count` drops to `0`, we pick the current element as our new candidate.
  * If the current element is equal to our candidate, we increment `count` (the candidate gets a supporting vote).
  * If the current element is different, we decrement `count` (an opposing vote cancels out a vote for our candidate).

Because the majority element appears more than $\lfloor n / 2 \rfloor$ times, its votes will outnumber the votes of all other elements combined. Even in the worst-case scenario where all other elements "vote against" the majority element, the majority element will still emerge as the surviving candidate at the end.

### Step-by-Step Visualization

Consider the array: `[2, 2, 1, 1, 1, 2, 2]`

```
Index | Element | Count | Candidate | Explanation
------+---------+-------+-----------+---------------------------------------------------
  0   |    2    |   0   |     -     | Count is 0. Candidate becomes 2. Count = 1.
  1   |    2    |   1   |     2     | Matches candidate. Count increases to 2.
  2   |    1    |   2   |     2     | Different. Count decreases to 1.
  3   |    1    |   1   |     2     | Different. Count decreases to 0.
  4   |    1    |   0   |     2     | Count is 0. Candidate becomes 1. Count = 1.
  5   |    2    |   1   |     1     | Different. Count decreases to 0.
  6   |    2    |   0   |     1     | Count is 0. Candidate becomes 2. Count = 1.
```
At the end, the surviving candidate is `2`.

> [!NOTE]
> This algorithm assumes that a majority element *always* exists. If a majority element is not guaranteed, we must perform a second pass to verify if the candidate's frequency is indeed greater than $\lfloor n / 2 \rfloor$.

### Complexity Analysis
- **Time Complexity (TC)**: $\mathcal{O}(N)$ (single pass over the array)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ (uses only two variables: `element` and `count`)

---

## Summary Table

| Approach | Time Complexity (TC) | Space Complexity (SC) | Description |
| :--- | :--- | :--- | :--- |
| **Sorting** | $\mathcal{O}(N \log N)$ | $\mathcal{O}(1)$ or $\mathcal{O}(N)$ | The majority element will always be at index $n//2$ after sorting. |
| **Hash Map** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | Counts frequencies and returns the element with count $> n//2$. |
| **Boyer-Moore Voting (Optimal)**| $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Uses a candidate and a counter to cancel out non-majority elements. |
