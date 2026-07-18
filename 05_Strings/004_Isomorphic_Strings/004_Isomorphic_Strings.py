
def isIsomorphic(s, t):
    # d={}
    # n=len(s)
    # for i in range(n):
    #     if s[i] in d:
    #         if t[i]!=d[s[i]]:
    #             return False
    #     else:
    #         for k,v in d.items():
    #             if v==t[i]:
    #                 return False
    #         d[s[i]]=t[i]
    # return True

    s_to_t = {}
    t_to_s = {}


    for c1, c2 in zip(s, t):
        if c1 in s_to_t and s_to_t[c1] != c2:
            return False
        if c2 in t_to_s and t_to_s[c2] != c1:
            return False

        s_to_t[c1] = c2
        t_to_s[c2] = c1

    return True

print(isIsomorphic("badc","baba"))