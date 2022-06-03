N = int(input())
times = []
prices = []
profits = [0] * (N + 1)

for _ in range(N):
    time, price = [int(x) for x in input().split()]
    times.append(time)
    prices.append(price)
    
for day in range(N - 1, -1, -1):
    if day + times[day] < N:
        profits[day] = prices[day] + max(profits[(day + times[day]):])
    elif day + times[day] == N:
        profits[day] = prices[day]

print(max(profits))
