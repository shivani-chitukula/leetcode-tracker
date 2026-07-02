
def maxAscendingSum(nums):
    maxi=0
    curr_sum =nums[0]
    
    for i in range(1,len(nums)):
        if nums[i]<=nums[i-1]:
            maxi=max(maxi,curr_sum)
            curr_sum =0
        curr_sum +=nums[i]
    return max(maxi,curr_sum)

print(maxAscendingSum([10,20,30,5,10,50]))