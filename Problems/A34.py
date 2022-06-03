N = int(input())
levels = [int(x) for x in input().split()]
dp = [1] * N  # length of dec. subseq. with last element levels[i]

for i in range(1, N):
    for j in range(i):
        if levels[i] < levels[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(dp[i])