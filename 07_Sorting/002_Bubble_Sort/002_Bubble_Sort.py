def bubbleSort(nums):
    n=len(nums)
    for i in range(n-1,-1,-1):
        for j in range(i):
            if nums[j+1]<nums[j]:
                nums[j+1],nums[j]=nums[j],nums[j+1]
    return nums
print(bubbleSort([13,46,24,52,20,9]))

