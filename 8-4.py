N, M = [int(x) for x in input().split(' ')]
units = [int(input()) for _ in range(N)]
min_unit = min(units)
dp = [100000] * (M + 1)
dp[0] = 0

for i in range(min_unit + 1, M + 1):
    for unit in units:
        if i >= unit:
            dp[i] = min(dp[i], dp[i - unit] + 1)

if dp[M] == 100000:
    dp[M] = -1

print(dp[M])


