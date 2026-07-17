def maxSubArray(nums):
        sum1=0
        maxi=float('-inf')
        for i in range(len(nums)):
            sum1+=nums[i]
            maxi=max(maxi,sum1)
            if sum1<0:
                sum1=0
        return maxi
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

def printMaxSubArray(nums):
    sum1 = 0
    maxi = float('-inf')
    start = 0
    sub_start, sub_end = -1, -1
    
    for i in range(len(nums)):
        if sum1 == 0:
            start = i          
        sum1+=nums[i]        
        if sum1 > maxi:
            maxi = sum1
            sub_start = start
            sub_end = i
            
        if sum1 < 0:
            sum1 = 0
            
    print("Maximum Subarray is:", nums[sub_start : sub_end + 1])
    # return maxi

printMaxSubArray([-2,1,-3,4,-1,2,1,-5,4])