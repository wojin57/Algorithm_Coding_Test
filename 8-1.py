dp = [0] * 30001

def solution(n):
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
    
        for div in [2, 3, 5]:
            if i % div == 0:
                dp[i] = min(dp[i], dp[i // div] + 1)
    
    return dp[n]
    

X = int(input())
print(solution(X))
