def largest(arr):

    # arr.sort()
    # return arr[-1]

    maxi=arr[0]
    for i in range(1,len(arr)):
        if maxi<arr[i]:
            maxi=arr[i]
    return maxi

    # return max(arr)

print(largest([1,4,2,3,8,6,5,44,3,77,800,12]))