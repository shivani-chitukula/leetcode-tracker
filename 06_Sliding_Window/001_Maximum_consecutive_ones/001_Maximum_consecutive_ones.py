def longestOnes(nums,k):
    maxi = 0
    n = len(nums)
    l=0
    r=0
    zeros=0

    while r < n:
        if nums[r] == 0:
            zeros += 1
        while zeros>k:
            if nums[l]==0:
                zeros-=1
            l+=1
        r+=1

        if zeros<=k:
            maxi=max(maxi,r-l)
    return maxi
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
    