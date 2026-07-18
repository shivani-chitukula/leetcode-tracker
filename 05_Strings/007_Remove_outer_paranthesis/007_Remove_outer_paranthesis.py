
def removeOuterParentheses(s):
    l,r=0,0
    count=0
    newStr=''
    while l<=r and r<len(s):
        if s[r]=='(':
            count-=1
            r+=1
        if s[r]==')':
            count+=1
            r+=1
        
        if count==0:
            newStr=newStr+s[l+1:r-1]
            l=r

    return newStr

print(removeOuterParentheses("(()())(())(()(()))"))