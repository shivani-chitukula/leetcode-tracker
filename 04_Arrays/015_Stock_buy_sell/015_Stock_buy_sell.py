def maxProfit(prices):
    n=len(prices)
    maxi=0
    # for i in range(n-1):
    #     for j in range(i+1,n):
    #         maxi=max(maxi,prices[j]-prices[i])
    # return maxi

    mini=prices[0]
    maxProfit=0
    for i in range(1,n):
        maxProfit=max(prices[i]-mini,maxProfit)
        if prices[i]<mini:
            mini=prices[i]
    return maxProfit

print(maxProfit([7,1,5,3,6,4]))