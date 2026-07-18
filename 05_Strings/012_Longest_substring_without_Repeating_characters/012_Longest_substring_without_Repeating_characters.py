def lengthOfLongestSubstring(s):
    temp=set()
    i=0
    maxlen=0
    for j in range(len(s)):
        while s[j] in temp:
            temp.remove(s[i])
            i=i+1
    
        temp.add(s[j]) 
        maxlen=max(maxlen,j-i+1)
    return maxlen

print(lengthOfLongestSubstring("abcabcbb"))