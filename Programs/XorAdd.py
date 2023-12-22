def add(x, y):
    while y:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x


a = int(input("Enter a value:"))
b = int(input("Enter b value:"))
print(add(a, b))


"""
1 - 001 
2 - 010
1 & 2 = 000 - 0
1 ^ 2 = 011 - 3
0 << 1
shifts the carry one position to the left to prepare it for the next addition.
The loop continues until there is no carry left and final result is 'x'

000 - 0
001 - 1
010 - 2
011 - 3
"""