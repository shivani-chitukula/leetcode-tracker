# Count Digits

Problem Link: [takeUforward - Count Digits in a Number](https://takeuforward.org/data-structure/count-digits-in-a-number/)

## Intuition
To count the total number of digits in an integer, we can repeatedly divide the number by 10 using integer division (`// 10`) until it becomes 0. Each division removes the last digit from the number, and we increment a counter by 1 for each step.

## Complexity
- **Time Complexity:** O(log10(N)) where N is the input integer. Since we divide N by 10 in every step, the loop runs once for each digit of the number.
- **Space Complexity:** O(1) as we only use a single counter variable.

