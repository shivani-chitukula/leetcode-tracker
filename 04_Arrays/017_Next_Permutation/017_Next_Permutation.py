
def nextPermutation(nums):
    n = len(nums)

    # Step 1: Find breakpoint
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # Step 2: Find next greater element and swap
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # Step 3: Reverse suffix
    nums[i + 1:] = reversed(nums[i + 1:])
    return nums

print(nextPermutation([1,3,2]))