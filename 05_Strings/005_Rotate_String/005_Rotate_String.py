
def rotateString(s,goal):
    # for i in range(len(s)):
    #     temp=s[0]
    #     s=s[1:]+temp
    #     if s==goal:
    #         return True
    # return False

    if len(s) != len(goal):
        return False
    return goal in s + s

print(rotateString('abcde','cdeab'))