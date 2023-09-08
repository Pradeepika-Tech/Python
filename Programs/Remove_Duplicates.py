"""Remove duplicates from the given list: [1, 2, 3, 4, 2, 2, 2, 3, 4, 5]"""


def remove_duplicates(l1):
    s = dict()
    for i in range(len(l1)):
        s[l1[i]] = None
    return list(s)


li = [1, 2, 3, 4, 2, 2, 2, 3, 4, 5]
print(remove_duplicates(li))
