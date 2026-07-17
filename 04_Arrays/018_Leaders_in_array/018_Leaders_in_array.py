def leaderInArray(nums):
    n=len(nums)
    x=[]
    maxi=nums[-1]
    x.append(nums[-1])
    for i in range(n-2,-1,-1):
        if nums[i]>maxi:
            x.append(nums[i])
            maxi=nums[i]
    
    x.reverse()
    return x

print(leaderInArray([10, 22, 12, 3, 0, 6]))