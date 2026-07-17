def rearrangeArray(nums):
    n=len(nums)
    # pos=[]
    # neg=[]
    # for num in nums:
    #     if num<0:
    #         neg.append(num)
    #     else:
    #         pos.append(num)
    # for i in range(n):
    #     if i%2==0:
    #         nums[i]=pos[i//2]
    #     else:
    #         nums[i]=neg[i//2]
    # return nums

    result=[0]*n
    posIdx=0
    negIdx=1
    for i in range(n):
        if nums[i]>0:
            result[posIdx]=nums[i]
            posIdx+=2
        else:
            result[negIdx]=nums[i]
            negIdx+=2
    return result

def rearrangeArrayUnequal(nums):
    n=len(nums)
    pos=[]
    neg=[]
    for num in nums:
        if num<0:
            neg.append(num)
        else:
            pos.append(num)
    
    if len(pos)>len(neg):
        for i in range(len(neg)):
            nums[2*i]=pos[i]
            nums[2*i+1]=neg[i]
        index=2*len(neg)
        for i in range(len(neg),len(pos)):
            nums[index]=pos[i]
            index+=1
    else:
        for i in range(len(pos)):
            nums[2*i]=pos[i]
            nums[2*i+1]=neg[i]
        index=2*len(pos)
        for i in range(len(pos),len(neg)):
            nums[index]=neg[i]
            index+=1
    return nums

# Testing equal positives and negatives
print("Equal:",rearrangeArray([3,1,-2,-5,2,-4]))

# Testing unequal positives and negatives
print("Unequal:",rearrangeArrayUnequal([3,1,-2,-5,2,-4,1,1,1]))
