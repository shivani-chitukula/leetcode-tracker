
def reverseWords(s):
    # a=s.split(' ')
    # a.reverse()
    # newstr=''
    # for word in a:
    #     if word=='':
    #         continue
    #     else:
    #         newstr+=word+' '
    
    # return newstr[:-1]
    words = s.split()
    # words.reverse()
    # return " ".join(words)
    l=0
    r=len(words)-1
    while l<r:
        words[l],words[r]=words[r],words[l]
        l+=1
        r-=1
    return " ".join(words)

print(reverseWords("a good   example"))