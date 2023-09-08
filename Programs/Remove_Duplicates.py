def remove_duplicates(l):
    s = dict()
    for i in range(len(l)):
        s[l[i]] = None
    return list(s)


li = [1, 2, 3, 4, 2, 2, 2, 3, 4, 5]
print(remove_duplicates(li))
