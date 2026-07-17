def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    # n=len(matrix)
    # ans = [[0]*n for _ in range(n)]
    # for i in range(n):
    #     for j in range(n):
    #         ans[j][n-1-i]=matrix[i][j]
    # return ans
    n=len(matrix)
    #transpose
    for i in range(n-1):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    #reverse
    for i in range(n):
        matrix[i].reverse()
    return matrix

print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))