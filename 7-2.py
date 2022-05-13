import sys

N, M = [int(x) for x in input().split(' ')]
heights = [int(x) for x in sys.stdin.readline().rstrip().split(' ')]

start = 0
end = max(heights)
middle = (start + end) // 2

while start <= end:
    middle = (start + end) // 2
    total = 0
    for height in heights:
        if height > middle:
            total += (height - middle)

    if total > M:
        start = middle + 1
    elif total == M:
        break
    else:
        end = middle - 1

print(middle)
