def largestOddNumber(num):
    n=len(num)
    for i in range(n-1,-1,-1):
        if int(num[i])%2!=0:
            return num[:i+1]
    return ""

print(largestOddNumber('42061'))