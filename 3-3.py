N, M = [int(x) for x in input().split(' ')]
num_lists = [[int(x) for x in input().split(' ')] for _ in range(N)]
max_min = 0

for list in num_lists:
    local_min = min(list)
    if local_min > max_min:
        max_min = local_min

print(max_min)
