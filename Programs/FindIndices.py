def find_indices(l1, value):
    indices = []
    for i in range(len(l1)):
        for j in range(i+1, len(l1)):
            if l1[i] + l1[j] == value:
                indices.append((i, j))
    return indices


n = [3, 3]
target = 6
result = find_indices(n, target)
print(result)
