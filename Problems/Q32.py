height = int(input())
if height == 1:
    pass

dp_sum = [0] * height
for h in range(height):
    row = [int(x) for x in input().split()]
    temp = [0] * height
    temp[0] = dp_sum[0] + row[0]
    for i in range(1, h - 1):
        temp[i] = max(dp_sum[i - 1], dp_sum[i]) + row[i]
    temp[h - 1] = dp_sum[h - 2] + row[h - 1]
    dp_sum = temp
print(max(dp_sum))