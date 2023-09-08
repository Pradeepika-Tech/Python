def expand(s):
    temp = " "
    for i in range(len(s)):
        if s[i].isdigit():
            num = int(s[i])
            for j in range(1, num):
                temp += s[i+1]
        else:
            temp += s[i]
    return temp


s = "e2n4b2cx"
print(expand(s))
