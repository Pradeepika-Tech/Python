"""
input: Learning Python is very easy
output: Easy Very Is Python Learning
"""


def reverse_string(n):
    li = n.split()
    final_string = []
    i = len(li)-1
    while i >= 0:
        final_string.append(li[i])
        i -= 1
    output = ' '.join(li)
    print(output)


s = "Learning Python is very easy"
reverse_string(s)
