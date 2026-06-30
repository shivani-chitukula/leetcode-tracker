def findGCD(a,b):
    maxi=max(a,b)
    gcd=1
    if a == 0 : return b
    elif b == 0 : return a
    elif a == b : return a

    for i in range(1,maxi+1):
        if a%i==0 and b%i==0:
            gcd=max(i,gcd)
    return gcd

gcd=findGCD(18,24)
print(gcd)
