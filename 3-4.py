from math import remainder


N, K = [int(x) for x in input().split(' ')]
count = 0

while N > 1:
    if (remainder := N % K) != 0:
        N -= remainder
        count += remainder
    else:
        N /= K
        count += 1

print(count)
