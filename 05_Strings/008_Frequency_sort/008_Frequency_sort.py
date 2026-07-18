from collections import Counter
def frequencySort(s):
    d=Counter(s)
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    # print(sorted_dict)
    newStr=''
    for k,v in sorted_dict.items():
        newStr+=k*v
    return newStr
print(frequencySort("cccaaa"))
print(frequencySort("tree"))