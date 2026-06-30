# Count Frequency of each element in the array

Problem Link: [takeUforward - Count frequency of each element in the array](https://takeuforward.org/data-structure/count-frequency-of-each-element-in-an-array/)

## Intuition
To count how many times each element appears in a given array, we can use a **Hash Map** (or a Python dictionary). 

1. We initialize an empty dictionary `d` where the keys represent the elements from the array and the values represent their frequencies.
2. We traverse the array element by element. For each element:
   - If it is already in our dictionary, we increment its count by 1.
   - If it is not in the dictionary, we add it with a starting frequency of 1.
3. Python also provides a built-in `Counter` class from the `collections` module which does this automatically and efficiently.

Example: `[10, 10, 5, 5, 6, 9, 66, 5, 5, 10]`
- Traverse and update counts:
  - `10` appears 3 times
  - `5` appears 4 times
  - `6` appears 1 time
  - `9` appears 1 time
  - `66` appears 1 time
- Output: `{10: 3, 5: 4, 6: 1, 9: 1, 66: 1}`

## Complexity
- **Time Complexity:** O(N) where N is the number of elements in the array. We perform a single pass over the array, and dictionary insertions/lookups take O(1) time on average.
- **Space Complexity:** O(N) in the worst case if all elements in the array are unique, as we need to store them in the hash map.
