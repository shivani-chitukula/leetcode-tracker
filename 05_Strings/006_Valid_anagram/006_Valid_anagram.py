def isAnagram(s, t):
    # return sorted(s) == sorted(t)


    if len(s) != len(t):
        return False
    dict1={}
    dict2={}
    for c1,c2 in zip(s,t):
        if c1 in dict1:
            dict1[c1]+=1
        else:
            dict1[c1]=1
        if c2 in dict2:
            dict2[c2]+=1
        else:
            dict2[c2]=1

    # for k,v in dict1.items():
    #     if k not in dict2:
    #         return False
    #     if dict2[k]!=v:
    #         return False
    return dict1==dict2
        

print(isAnagram('anagram','nagaram'))
print(isAnagram('a','ab'))