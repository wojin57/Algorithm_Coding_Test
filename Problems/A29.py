N, C = [int(x) for x in input().split()]
houses = [int(input) for _ in range(N)]
houses.sort()

start = 1
end = houses[-1] - houses[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    cur = houses[0]
    count = 1

    for i in range(1, N):
        if houses[i] >= cur + mid:
            cur = houses[i]
            count += 1
    
    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
