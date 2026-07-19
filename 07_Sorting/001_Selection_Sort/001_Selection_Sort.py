def selectionSort(nums):
    n=len(nums)
    for i in range(n-1):
        mini=i
        for j in range(i,n):
            if nums[j]<nums[mini]:
                mini=j
        nums[mini],nums[i]=nums[i],nums[mini]    
    return nums

print(selectionSort([13,46,24,52,20,9]))