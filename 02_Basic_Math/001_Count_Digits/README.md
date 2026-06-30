# Count Digits

Problem Links:
- [GeeksforGeeks - Count Digits](https://www.geeksforgeeks.org/problems/count-digits5716/1) (Count digits that evenly divide the number)

## Intuition
To count the total number of digits in an integer, we can repeatedly divide the number by 10 using integer division (`// 10`) until it becomes 0. Each division removes the last digit from the number, and we increment a counter by 1 for each step.

Note: In the GeeksforGeeks/Coding Ninjas version of the problem, you are asked to count only the individual digits that evenly divide the original number. To do that, you would need to save the original number, extract each digit using `% 10`, check if the digit divides the original number with a remainder of 0, and then proceed with `// 10`.

## Complexity
- **Time Complexity:** O(log10(N)) where N is the input integer. Since we divide N by 10 in every step, the loop runs exactly once for each digit of the number.
- **Space Complexity:** O(1) as we only use a single counter variable.
