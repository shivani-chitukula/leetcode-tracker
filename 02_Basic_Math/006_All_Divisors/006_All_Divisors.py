def divisors(num):
    arr=[]

    for i  in range(1,num//2+1):
        if num%i==0:
            arr.append(i)
    arr.append(num)
 
    return arr


print(divisors(36)) #output: [1, 2, 3, 4, 6, 9, 12, 18, 36]
print(divisors(12)) #output: [1, 2, 3, 4, 6, 12]