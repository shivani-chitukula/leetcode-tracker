def maxDepth(s):
    tempCount=0
    maxCount=0
    for i in range(len(s)):
        if s[i]=='(':
            tempCount+=1
        if s[i]==')':
            tempCount-=1
        maxCount=max(maxCount,tempCount)
    return maxCount
        
print(maxDepth("(1)+((2))+(((3)))"))