def findMaxConsecutiveOnes( nums):
        maxi=0
        temp=0
        for i in range(len(nums)):
            if nums[i]==1:
                temp+=1 
            else: 
                maxi=max(maxi,temp)
                temp=0
        return max(maxi,temp)
        
print(findMaxConsecutiveOnes([1,1,0,1,1,1]))