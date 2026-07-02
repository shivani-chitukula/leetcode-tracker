def check(nums):
    breaks=0
    
    for i in range(1,len(nums)):
        if nums[i]<nums[i-1]:
            breaks+=1
    if nums[0] <nums[-1]:
                breaks+=1    
    return breaks<=1   

print(check([3,4,5,1,2,1]))