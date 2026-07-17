def sortColors(arr):
        # return arr.sort()

        # cnt0 = 0
        # cnt1 = 0
        # cnt2 = 0
        # for num in arr:
        #     if num == 0:
        #         cnt0 += 1
        #     elif num == 1:
        #         cnt1 += 1
        #     else:
        #         cnt2 += 1
        # for i in range(cnt0):
        #     arr[i] = 0
        # for i in range(cnt0, cnt0 + cnt1):
        #     arr[i] = 1
        # for i in range(cnt0 + cnt1, len(arr)):
        #     arr[i] = 2
        # return arr

        mid=0
        low=0
        high=len(arr)-1
        for i in range(len(arr)):
            if arr[mid]==0:
                arr[low],arr[mid]=arr[mid],arr[low]
                mid+=1
                low+=1
            elif arr[mid]==1:
                mid+=1
            elif arr[mid]==2:
                arr[high],arr[mid]=arr[mid],arr[high]
                high-=1


        return arr
print(sortColors([2,0,2,1,1,0]))