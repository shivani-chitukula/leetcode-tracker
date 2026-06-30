def isArmstrong(num):
    if num < 0:
        return False
    sum=0
    n=len(str(num))
    temp=num
    while(temp>0):
        x=temp%10
        sum+=x**n
        temp=temp//10
    
    return num==sum

print(isArmstrong(153)) #true. 1^3+5^3+3^3= 1+125+27=153
print(isArmstrong(1634)) # true:1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634

