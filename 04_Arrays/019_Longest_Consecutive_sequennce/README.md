# Longest Consecutive Sequence

[LeetCode Problem Link](https://leetcode.com/problems/longest-consecutive-sequence/)

Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*

You must write an algorithm that runs in **$\mathcal{O}(n)$ time**.

---

## 1. Better Approach (Sorting)

### Intuition
If we sort the array, consecutive numbers will lie adjacent to each other.
1. Sort the array in ascending order.
2. Initialize `count` to 1 and `maxCount` to 1 (handling empty array edge cases first, which returns 0).
3. Iterate through the array starting from the second element:
   - If the current element is equal to the previous element, skip it (duplicates do not break the sequence but also do not increase its length).
   - If the current element is exactly 1 greater than the previous element (`nums[i] - nums[i-1] == 1`), increment `count`.
   - Otherwise, update `maxCount` with `max(maxCount, count)` and reset `count` to 1.
4. At the end of the loop, perform one final check to update `maxCount`.

### Complexity Analysis
- **Time Complexity (TC)**: $\mathcal{O}(N \log N)$ (due to sorting the array)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ or $\mathcal{O}(N)$ (depending on the sorting method/algorithm implemented)

---

## 2. Optimal Approach (Hash Set / Intelligent Scan)

### Intuition
To achieve $\mathcal{O}(N)$ time complexity, we need a fast way to check if consecutive numbers exist. Inserting all elements into a Hash Set allows us to check for the existence of any number in $\mathcal{O}(1)$ average time.

If we simply searched for the next consecutive numbers for *every* element, we would end up repeating work and risk an $\mathcal{O}(N^2)$ runtime. To optimize this, **we only want to start counting a sequence from its very beginning (the minimum element of that sequence).**

#### How do we identify the start of a sequence?
* For any number `num`, if `num - 1` is present in the set, then `num` is **not** the start of a sequence (since a sequence starting at `num - 1` or earlier already contains it). We skip it.
* If `num - 1` is **not** present in the set, it means `num` is the absolute starting point of a new consecutive sequence. Only then do we start checking for `num + 1`, `num + 2`, `num + 3`, etc.

### Step-by-Step Algorithm
1. Store all elements of the array in a Hash Set `setA`. This eliminates duplicates and gives $\mathcal{O}(1)$ lookups.
2. Iterate through the elements of the set:
   - For each element `num`, check if `num - 1` is in `setA`.
   - If `num - 1` is **not** in `setA`:
     - Initialize `curLen = 1`.
     - While `num + curLen` exists in `setA`, increment `curLen`.
     - Update the maximum length found so far: `count = max(count, curLen)`.
3. Return the maximum consecutive sequence length `count`.

### Visual Walkthrough

Input: `nums = [100, 4, 200, 1, 3, 2]`
Hash Set `setA = {100, 4, 200, 1, 3, 2}`

* **`num = 100`**: Is `99` in set? No. We start sequence: `100`. Next `101` in set? No. `curLen = 1`.
* **`num = 4`**: Is `3` in set? Yes. We skip `4` (since it will be covered by the sequence starting at `1`).
* **`num = 200`**: Is `199` in set? No. We start sequence: `200`. Next `201` in set? No. `curLen = 1`.
* **`num = 1`**: Is `0` in set? No. We start sequence: `1`. 
  - Next `2` in set? Yes.
  - Next `3` in set? Yes.
  - Next `4` in set? Yes.
  - Next `5` in set? No.
  - `curLen = 4`. Update `count = 4`.
* **`num = 3`**: Is `2` in set? Yes. Skip.
* **`num = 2`**: Is `1` in set? Yes. Skip.

Longest consecutive length is `4`.

### Why is this $\mathcal{O}(N)$ if there is a nested `while` loop?
Although there is a `while` loop inside the `for` loop, each element is visited at most **twice**:
1. Once during the outer iteration over the set.
2. At most once inside the inner `while` loop (since the `while` loop only triggers for the starting element of a sequence). Each consecutive number chain is built exactly once.
Thus, total operations are roughly $2N$, which is linear.

- **Time Complexity (TC)**: $\mathcal{O}(N)$ (to build the set and traverse the elements)
- **Space Complexity (SC)**: $\mathcal{O}(N)$ (to store the elements in the Hash Set)

---

## Summary Table

| Approach | Time Complexity (TC) | Space Complexity (SC) | Description |
| :--- | :--- | :--- | :--- |
| **Sorting** | $\mathcal{O}(N \log N)$ | $\mathcal{O}(1)$ | Sorts the array and counts adjacent elements incrementing by 1. |
| **Hash Set (Optimal)** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | Uses a set for $\mathcal{O}(1)$ lookup, only counting sequences from their starting elements. |
