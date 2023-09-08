"""Expand the string based on the number in front of the character
    Input: "e2n4b2cx"
    Output: "ennbbbbccx"
"""


def expand(st):
    temp = " "
    for i in range(len(st)):
        if st[i].isdigit():
            num = int(st[i])
            for j in range(1, num):
                temp += st[i+1]
        else:
            temp += st[i]
    return temp


s = "e2n4b2cx"
print(expand(s))
