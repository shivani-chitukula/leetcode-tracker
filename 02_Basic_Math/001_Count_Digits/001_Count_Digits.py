def countDigits(n):
    count = 0
    while (n>0):
        n = n//10
        count += 1
    return count


if __name__ == "__main__":
    N = 329823
    print("N:", N)
    digits = countDigits(N)
    print("Number of Digits in N:", digits)
                                