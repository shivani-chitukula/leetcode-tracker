def reverseInteger(x):
    is_negative=x<0
    n=abs(x)
    x=0
    while (n!=0):
        r=n%10
        x=x*10+r
        n=n//10
    if x < -2**31 or x > 2**31 - 1:
        return 0
    return -x if is_negative else x

num = 12348975
print(reverseInteger(num)) 
