# Print all Divisors of a given Number

Problem Link: [takeUforward - Print all Divisors of a given Number](https://takeuforward.org/data-structure/print-all-divisors-of-a-given-number/)

## Intuition
A divisor of an integer `N` is any positive integer that divides `N` without leaving a remainder. 

To find all divisors of a number:
1. We can check all integers starting from `1` up to `N // 2`. If `N` is divisible by the integer `i` (i.e., `N % i == 0`), then `i` is a divisor, and we add it to our list.
2. Finally, we append the number `N` itself to the list since any number is divisible by itself.

Example: num = 36
- Checking numbers from 1 to 18:
  - 36 is divisible by 1, 2, 3, 4, 6, 9, 12, 18.
- Appending the number itself: 36.
- All divisors: `[1, 2, 3, 4, 6, 9, 12, 18, 36]`.

### Optimal Approach Hint
Instead of checking all numbers up to `N // 2`, we can run the loop only up to `sqrt(N)`. If a number `i` divides `N`, then both `i` and `N // i` are divisors. This optimization reduces the search range significantly.

## Complexity
- **Time Complexity:** O(N) where N is the input integer. The loop runs from 1 to `N // 2`.
  - *With the optimal approach, it can be reduced to O(sqrt(N)).*
- **Space Complexity:** O(D) where D is the number of divisors of N (to store the list of divisors).
