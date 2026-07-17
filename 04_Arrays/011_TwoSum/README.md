# Two Sum

[LeetCode Problem Link](https://leetcode.com/problems/two-sum/)

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice. You can return the answer in any order.

---

## 1. Brute Force Approach

### Intuition
The simplest approach is to check every possible pair of numbers in the array to see if their sum equals the `target`.
- We use two nested loops: the outer loop runs from `i = 0` to `n - 1`, and the inner loop runs from `j = i + 1` to `n - 1`.
- If `nums[i] + nums[j] == target`, we return the indices `[i, j]`.

- **Time Complexity (TC)**: $\mathcal{O}(N^2)$ (where $N$ is the length of `nums`, due to the nested loops checking all pairs)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ (uses constant extra space)

---

## 2. Two-Pass Hash Map Approach

### Intuition
We can reduce the lookup time from $\mathcal{O}(N)$ to $\mathcal{O}(1)$ by using a hash map (dictionary in Python).
- In the first pass, we add each element's value and its index to the hash map.
- In the second pass, we check if each element's complement (`target - nums[i]`) exists in the hash map.
- If the complement exists and its index is not equal to `i` (we cannot use the same element twice), we return the indices `[i, dict[target - nums[i]]]`.

- **Time Complexity (TC)**: $\mathcal{O}(N)$ (we traverse the list containing $N$ elements exactly twice; lookups in the hash map take $\mathcal{O}(1)$ time)
- **Space Complexity (SC)**: $\mathcal{O}(N)$ (the extra space required depends on the number of items stored in the hash map, which stores at most $N$ elements)

---

## 3. One-Pass Hash Map Approach (Optimal)

### Intuition
We can optimize the two-pass approach to a single pass. While we iterate and insert elements into the hash map, we also check if the current element's complement already exists in the map.
- For each element `nums[i]`, we calculate its complement `target - nums[i]`.
- If the complement is already present in our hash map, it means we found a pair that sums up to the target. We return its index and the current index `[dict[complement], i]`.
- If it is not present, we insert the current element `nums[i]` and its index `i` into the map.

- **Time Complexity (TC)**: $\mathcal{O}(N)$ (we traverse the list containing $N$ elements only once; each lookup in the table costs $\mathcal{O}(1)$ time)
- **Space Complexity (SC)**: $\mathcal{O}(N)$ (in the worst case, the hash map will store up to $N$ elements)

---

## Summary Table

| Approach | Time Complexity (TC) | Space Complexity (SC) | Description |
| :--- | :--- | :--- | :--- |
| **Brute Force** | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | Checks every pair of elements. |
| **Two-Pass Hash Map** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | Builds a hash map first, and then searches for complements. |
| **One-Pass Hash Map (Optimal)** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | Searches for the complement while building the hash map. |
