def is_balanced(input_str):
    str_map = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in input_str:
        if char in str_map.values():
            stack.append(char)
        elif char in str_map.keys():
            if not stack or stack.pop() != str_map[char]:
                return "Unbalanced"
        else:
            pass
    return "Balanced"


result1 = is_balanced("(}{}][][))")
result2 = is_balanced("()")

print(result1)
print(result2)
