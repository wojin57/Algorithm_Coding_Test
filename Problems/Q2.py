input_str = input()
result = 0

for c in input_str:
    num = int(c)
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
