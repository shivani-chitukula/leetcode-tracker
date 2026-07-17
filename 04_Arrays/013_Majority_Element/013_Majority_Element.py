from typing import Counter
def majorityElement(nums):
    n=len(nums)
    # nums.sort()
    # return nums[n//2]

    # counter = Counter(nums)

    # for num, count in counter.items():
    #     if count > (n // 2):
    #         return num

    # return -1

    element=0
    count=0
    for i in range(n):
        if count==0:
            element=nums[i]
        if element==nums[i]:
            count+=1
        else:
            count-=1
        
    return element
print(majorityElement([2,2,1,1,1,2,2]))