def setZeroes(matrix):
    m=len(matrix)
    n=len(matrix[0])
    l=[]
    l1=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                l.append(i)
                l1.append(j)
    
    for i in l:
        for j in range(n):
            matrix[i][j]=0
    for j in l1:
        for i in range(m):
            matrix[i][j]=0
    return matrix

#Optimal
def setZeroes(matrix):
    m=len(matrix)
    n=len(matrix[0])
    #col is matrix[0][1,2,3,4..]
    #row is matrix[0,1,2,3][0]
    var=1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0 and j!=0:
                matrix[i][0]=0
                matrix[0][j]=0

            if j==0 and matrix[i][j]==0:
                var=0       
    for i in range(len(matrix)-1,-1,-1):
        for j in range(len(matrix[0])-1,-1,-1):

            if (matrix[i][0]==0 or matrix[0][j]==0) and (i!=0 and j!=0):
                matrix[i][j]=0

            if matrix[i][0]==0 and i==0 :
                matrix[i][j]=0

            if var==0 and j==0:
                matrix[i][j]=0
    return matrix

print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))