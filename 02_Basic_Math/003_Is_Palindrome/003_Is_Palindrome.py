def isPalindrome(x):
        if x<0:
            return False
        n=x
        reverse=0
        while(n!=0):
            r=n%10
            reverse=reverse*10+r
            n=n//10
        return x==reverse

x = 12321
print(isPalindrome(x)) 