# Best Time to Buy and Sell Stock

[LeetCode Problem Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

You are given an array `prices` where `prices[i]` is the price of a given stock on the $i^{th}$ day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

---

## 1. Brute Force Approach

### Intuition
The simplest way to solve this is to check every possible pair of buy and sell days.
- We buy on day `i` and sell on day `j` (where `j > i`).
- We calculate the profit for each pair and track the maximum profit.


### Complexity Analysis
- **Time Complexity (TC)**: $\mathcal{O}(N^2)$ (due to two nested loops comparing all possible pairs of days)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ (uses constant extra space)

---

## 2. Optimal Approach (Greedy / One Pass)

### Intuition
Instead of comparing every pair of days, we can traverse the prices array just **once**. 
To maximize profit, we want to:
1. Buy at the lowest possible price.
2. Sell at the highest possible price *after* that buying day.

As we iterate through the list:
- We keep track of the minimum price seen so far (`mini`).
- If the current price is less than `mini`, we update `mini`.
- If the current price is greater, we calculate the potential profit if we sold today: `profit = prices[i] - mini`. We then update our maximum profit (`maxProfit`) if this potential profit is larger.

### Step-by-Step Execution Example

Input: `prices = [7, 1, 5, 3, 6, 4]`

```
Day (i) | Price | Min Price So Far (mini) | Potential Profit (prices[i] - mini) | Max Profit (maxProfit)
--------+-------+-------------------------+-------------------------------------+-----------------------
   0    |   7   |            7            |                  -                  |           0
   1    |   1   |            1            |              1 - 1 = 0              |           0
   2    |   5   |            1            |              5 - 1 = 4              |           4
   3    |   3   |            1            |              3 - 1 = 2              |           4
   4    |   6   |            1            |              6 - 1 = 5              |           5
   5    |   4   |            1            |              4 - 1 = 3              |           5
```

At the end of the iteration, `maxProfit = 5`.

### Complexity Analysis
- **Time Complexity (TC)**: $\mathcal{O}(N)$ (we traverse the array of size $N$ exactly once)
- **Space Complexity (SC)**: $\mathcal{O}(1)$ (uses only two extra variables: `mini` and `maxProfit`)

---

## Summary Table

| Approach | Time Complexity (TC) | Space Complexity (SC) | Description |
| :--- | :--- | :--- | :--- |
| **Brute Force** | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | Compares every possible buying day with every future selling day. |
| **Greedy (Optimal)** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Single pass tracking the minimum price and calculating maximum profit dynamically. |
