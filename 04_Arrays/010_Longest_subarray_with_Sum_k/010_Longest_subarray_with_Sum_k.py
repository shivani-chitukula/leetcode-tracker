def longestSubarraySumK(nums, k):
    L = 0
    R = 0
    tempSum = 0
    maxLen = 0

    while R < len(nums):
        tempSum += nums[R]
        while tempSum > k:
            tempSum -= nums[L]
            L += 1
        if tempSum == k:
            maxLen = max(maxLen, R - L + 1)
        R += 1
    return maxLen

print(longestSubarraySumK([10, 5, 2, 7, 1, 9],15))