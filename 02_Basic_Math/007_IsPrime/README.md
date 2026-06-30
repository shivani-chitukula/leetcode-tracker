# Check if a number is Prime or not

Problem Link: [takeUforward - Check if a number is Prime or not](https://takeuforward.org/data-structure/check-if-a-number-is-prime-or-not/)

## Intuition
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

To check if a number `N` is prime:
1. Any number less than or equal to `1` is not prime, so we return `False` immediately.
2. We iterate through all integers starting from `2` up to `N // 2` (or `num // 2 + 1` in Python's range).
3. If `N` is divisible by any integer `i` in this range (i.e., `N % i == 0`), it has a divisor other than 1 and itself, so it is not prime (`False`).
4. If the loop completes without finding any divisors, the number is prime (`True`).

### Optimal Approach Hint
Instead of checking all numbers up to `N // 2`, we only need to search up to `sqrt(N)`. If a number `N` has a divisor greater than `sqrt(N)`, it must also have a matching divisor smaller than `sqrt(N)`. Thus, we can optimize the loop to check from `2` up to `sqrt(N)`, which reduces the time complexity.

## Complexity
- **Time Complexity:** O(N) where N is the input integer. The loop runs up to `N // 2` times.
  - *With the optimal approach, it can be reduced to O(sqrt(N)).*
- **Space Complexity:** O(1) as we only use a single loop counter variable.
