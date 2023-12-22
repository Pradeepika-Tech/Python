def find_denominations(amount):
    denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 1]
    result = {}

    for denomination in denominations:
        count = amount // denomination
        if count > 0:
            result[denomination] = count
            amount %= denomination

    return result


input_amount = 2456
output_denomination = find_denominations(input_amount)

print("input_amount", input_amount)
print("output_amount", end="\n")
for denomination, count in output_denomination.items():
    print(f"{denomination}:{count}", end="\n")
