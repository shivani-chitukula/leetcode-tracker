def insertionSort(nums):
    n=len(nums)
    for i in range(n-1):
        for j in range(i+1,0,-1):
            if nums[j-1]>nums[j]:
                nums[j-1],nums[j]=nums[j],nums[j-1]


    return nums

print(insertionSort([13,46,24,52,20,9]))