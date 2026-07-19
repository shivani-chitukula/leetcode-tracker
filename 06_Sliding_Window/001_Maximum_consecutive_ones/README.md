# Max Consecutive Ones III

🔗 **LeetCode Link**: [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)

---

## 💡 Intuition & Core Concepts

The problem asks us to find the maximum number of consecutive `1`s we can get if we are allowed to flip at most `k` `0`s to `1`s.

### 1. Reformulating the Problem
Instead of performing actual modification/flipping of array values, we can rephrase the problem:
> **Find the longest contiguous subarray (window) that contains at most `k` zeros.**

If a subarray contains at most `k` zeros, we can flip all of them to `1`s, making the entire subarray consist of consecutive `1`s.

---

## ⚙️ Sliding Window Mechanism (Example: $k = 2$)

To solve this in linear time, we use a **sliding window** with two pointers: `l` (left boundary) and `r` (right boundary). 

If we set **$k = 2$**, our window is allowed to contain **at most 2 zeros** to remain valid. If it contains 3 or more zeros, it becomes invalid, and we must shrink it from the left.

### 📝 Step-by-Step Trace Example
Consider `nums = [1, 0, 0, 1, 0, 1]` with **$k = 2$**:

1. **Initial State**: `l = 0`, `r = 0`, `zeros = 0`, `maxi = 0`.
2. **Expand window (`r = 0`)**: `nums[0] = 1`. 
   - `zeros` count = `0`. (Valid: $0 \le 2$). 
   - Window: `[1]`. 
   - `maxi = max(0, 1 - 0) = 1`.
3. **Expand window (`r = 1`)**: `nums[1] = 0`.
   - `zeros` count = `1`. (Valid: $1 \le 2$). 
   - Window: `[1, 0]`. 
   - `maxi = max(1, 2 - 0) = 2`.
4. **Expand window (`r = 2`)**: `nums[2] = 0`.
   - `zeros` count = `2`. (Valid: $2 \le 2$). 
   - Window: `[1, 0, 0]`. 
   - `maxi = max(2, 3 - 0) = 3`.
5. **Expand window (`r = 3`)**: `nums[3] = 1`.
   - `zeros` count = `2`. (Valid: $2 \le 2$). 
   - Window: `[1, 0, 0, 1]`. 
   - `maxi = max(3, 4 - 0) = 4`.
6. **Expand window (`r = 4`)**: `nums[4] = 0`.
   - `zeros` count = `3`. (**Invalid**: $3 > 2$).
   - Window: `[1, 0, 0, 1, 0]`.
   - **Shrink from left**:
     - `nums[l] (nums[0]) = 1` $\rightarrow$ not a zero, just increment `l` to `1`. `zeros` is still `3`.
     - `nums[l] (nums[1]) = 0` $\rightarrow$ found a zero! Decrement `zeros` to `2` and increment `l` to `2`.
   - Window is valid again: `[0, 1, 0]` (indices 2 to 4).
   - `maxi` remains `4`.
7. **Expand window (`r = 5`)**: `nums[5] = 1`.
   - `zeros` count = `2`. (Valid: $2 \le 2$).
   - Window: `[0, 1, 0, 1]` (indices 2 to 5).
   - `maxi = max(4, 6 - 2) = 4`.

---

## 📊 Complexity Analysis

| Approach | Time Complexity | Space Complexity | Description |
| :--- | :--- | :--- | :--- |
| **Sliding Window** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Both pointers `l` and `r` only move forward. Each element is visited at most twice. Uses constant extra memory. |
