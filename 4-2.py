N = int(input())

count_normal = (6 + 10 - 1) * 60 * 2 - (6 + 10 - 1) ** 2
count_threes = 60 * 60
three_occurs = (N + 7) // 10

count = count_normal * (N + 1 - three_occurs) + count_threes * three_occurs
print(count)
