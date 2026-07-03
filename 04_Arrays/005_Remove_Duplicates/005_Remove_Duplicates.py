def removeDuplicates(nums):
        L=0
        for R in range(1,len(nums)):
            if nums[R]!=nums[L]:
                L+=1
                nums[L]=nums[R]
                
        return L+1,nums

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))