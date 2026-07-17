
def twoSum(nums,target):
    # for i in range(0,len(nums)-1):
    #     for j in range(len(nums)-1,i,-1):
    #         if nums[i]+nums[j]==target:
    #             return [i,j]

    # dict={}
    # for i in range(0,len(nums)):
    #     dict[nums[i]]=i
    # for i in range(0,len(nums)): 
    #     c=target-nums[i]
    #     if c in dict and i!=dict[c]:
    #         return[i,dict[c]]  

    dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in dict:
            return [dict[complement], i]
        dict[num] = i
     
print(twoSum([2,7,11,15],9))