from collections import Counter

def singleNumber(nums):
    frequency = Counter(nums)

    # frequency={}

    # for num in nums:
    #     if num in frequency:
    #         frequency[num] += 1
    #     else:
    #         frequency[num] = 1
    # for key,value in frequency.items():
    #     if value==1:
    #         return key

    XOR=0
    for i in range(len(nums)):
        XOR=XOR^nums[i]
    return XOR


print(singleNumber([4,1,2,1,2]))


