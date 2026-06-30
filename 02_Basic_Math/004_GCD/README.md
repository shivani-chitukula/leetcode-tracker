# Find Greatest Common Divisor of Array

LeetCode Link: [Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/)

## Intuition
The problem asks us to find the Greatest Common Divisor (GCD) of the smallest and largest numbers in a given array.

To solve this:
1. First, we identify the minimum and maximum elements in the array.
2. Then, to find the GCD of these two numbers (`a` and `b`), we can check numbers starting from 1 up to the maximum of `a` and `b`. If a number divides both `a` and `b` without a remainder, we track it as our current GCD. The largest such divisor found by the end of the loop is the GCD.

Example : a= 18, b=24

Multiples of 18= `[1, 2, 3, 6, 9, 18] `

Multiples of 24= `[1, 2, 3, 4, 6, 8, 12, 24] `

Greatest among all divisors is 6.

### Optimal Approach Hint
While a linear search loop works, the most efficient way to find the GCD of two numbers is using the **Euclidean Algorithm**. It states that the GCD of two numbers also divides their difference. Recursively, this can be written as `gcd(a, b) = gcd(b, a % b)` until `b` becomes 0. This algorithm runs in logarithmic time instead of linear time.

## Complexity
- **Time Complexity:** 
  - Finding the min and max in the array takes O(N) time, where N is the length of the array.
  - The GCD loop in the current implementation takes O(max(a, b)) time because it iterates up to the maximum of the two numbers.
  - Using the Euclidean Algorithm, the GCD calculation would be optimized to O(log(min(a, b))) time.
- **Space Complexity:** O(1) as we only use a few variables to store the limits and the GCD value.
