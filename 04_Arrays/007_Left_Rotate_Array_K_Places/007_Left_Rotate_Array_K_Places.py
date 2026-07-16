def rotate(nums, k):
    n = len(nums)
    k %= n
    nums[:] = nums[k:] + nums[:k]
    return nums

print(rotate([1,2,3,4,5,6,7], 3))

