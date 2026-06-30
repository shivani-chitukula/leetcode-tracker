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

print(isArmstrong(153))

