
def longestConsecutive(nums):
    # nums.sort()
    # count = 1
    # maxCount = 1
    # if len(nums)==0:
    #     return 0
    # for i in range(1, len(nums)):
    #     if nums[i] == nums[i-1]:
    #         continue
    #     elif nums[i]-nums[i-1]==  1:
    #         count += 1
    #     else:
    #         maxCount = max(maxCount, count)
    #         count = 1
    # maxCount = max(maxCount, count)
    # return maxCount

    setA=set(nums)
    count=0
    for num in setA:
        if num-1 not in setA:
            curLen=1
            while num+curLen in setA:
                curLen+=1
            count=max(count, curLen)
    return count

print(longestConsecutive([1,0,1,2]))