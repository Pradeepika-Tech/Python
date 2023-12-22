def color_sort(input_list):
    n = len(input_list)
    sorted_list = input_list.copy()

    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    return sorted_list


my_list = [2, 0, 1]
result = color_sort(my_list)

print(result)
