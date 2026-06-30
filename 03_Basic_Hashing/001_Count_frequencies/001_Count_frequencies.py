from collections import Counter

def countFrequency(arr):
    d={}

    for i in arr:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1

    return d

print(countFrequency([10,10,5,5,6,9,66,5,5,10]))
#Output: {10: 3, 5: 4, 6: 1, 9: 1, 66: 1}

#with counter
fruit_counts = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print(fruit_counts)
# Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

char_counts = Counter("mississippi")
print(char_counts)
# Output: Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
