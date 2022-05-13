N = int(input())
fears = [int(x) for x in input().split(' ')]
fears.sort()
result = 0
count = 0

for fear in fears:
    count += 1
    if count >= fear:
        result += 1
        count = 0

print(result)
