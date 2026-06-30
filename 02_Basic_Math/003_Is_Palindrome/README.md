# Palindrome Number

LeetCode Link: [Palindrome Number](https://leetcode.com/problems/palindrome-number/)

## Intuition
A number is a palindrome if it reads the same backward as forward. 

First, any negative number cannot be a palindrome because of the minus sign at the beginning (for example, -121 reversed is 121-, which does not match). 

For non-negative numbers, we can reverse the entire number by extracting its digits one by one (using `% 10` to get the last digit and `// 10` to remove it). Once we have the fully reversed number, we simply check if it is equal to the original input.

## Complexity
- **Time Complexity:** O(log10(N)) where N is the input integer. We divide the number by 10 in each iteration of the loop, which means we perform a constant number of operations for each digit.
- **Space Complexity:** O(1) as we only use a few variables to store the reversed value and intermediate results.
