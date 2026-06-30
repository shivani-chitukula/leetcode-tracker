# Check if a number is Armstrong Number

Problem Link: [takeUforward - Check if a number is Armstrong Number or not](https://takeuforward.org/maths/check-if-a-number-is-armstrong-number-or-not/)

## Intuition
An Armstrong number (or Narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

1. First, any negative number cannot be an Armstrong number, so we return `False` immediately.
2. We determine the total number of digits `n` in the input integer by converting it to a string and taking its length.
3. We then extract each digit of the number from right to left using the modulo operator (`% 10`), raise it to the power of `n`, and add it to our running sum.
4. We divide the number by `10` (`// 10`) in each step to remove the last digit until the number becomes `0`.
5. Finally, we check if the computed sum matches the original input.

## Complexity
- **Time Complexity:** O($\log_{10}(N)$) where N is the input integer. Counting the digits and extracting them one-by-one both take time proportional to the number of digits in N.
- **Space Complexity:** O(1) as we only use a few extra variables for the computation.
