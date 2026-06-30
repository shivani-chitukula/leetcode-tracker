# Reverse Integer

LeetCode Link: [Reverse Integer](https://leetcode.com/problems/reverse-integer/)

## Intuition
To reverse the digits of an integer, we can extract the last digit of the number using the remainder operator (`% 10`), add it to our reversed result, and then remove that last digit from the number using integer division (`// 10`). 

Since the input can be negative, we can keep track of the sign, reverse the absolute value of the number, and then apply the sign back to the final result.

Finally, the problem requires that if the reversed number goes outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, we must return 0.

## Complexity
- **Time Complexity:** O(log10(N)) where N is the input integer. This is because we divide the number by 10 in each step, meaning the loop runs once for each digit in the number.
- **Space Complexity:** O(1) as we only use a few variables to store the intermediate states.
