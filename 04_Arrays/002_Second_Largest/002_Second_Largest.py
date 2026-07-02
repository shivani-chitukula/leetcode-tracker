def secondLargestSmallest(arr):

    # arr.sort()
    # return arr[1],arr[-2]

    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')

    for i in range(len(arr)):
        if arr[i] < small:
            second_small = small
            small = arr[i]
        elif arr[i] < second_small and arr[i] > small:
            second_small = arr[i]

        if arr[i] > large:
            second_large = large
            large = arr[i]
        elif arr[i] > second_large and arr[i] < large:
            second_large = arr[i]

    return second_small,second_large


print(secondLargestSmallest( [1, 2, 4, 7, 7, 5, 8]  ))
