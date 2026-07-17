def spiralOrder(matrix):
    nums=[]
    top,left=0,0
    right=len(matrix[0])-1
    bottom=len(matrix)-1
    while left<=right and top<=bottom:
        for i in range(left, right+1):
            nums.append(matrix[top][i])
        top+=1
        for i in range(top,bottom+1):
            nums.append(matrix[i][right])
        right-=1
        if top <= bottom:
            for i in range(right,left-1,-1):
                nums.append(matrix[bottom][i])
            bottom-=1
        if left <= right:
            for i in range(bottom, top-1,-1):
                nums.append(matrix[i][left])
            left+=1
    return nums

print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    