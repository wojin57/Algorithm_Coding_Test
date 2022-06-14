N, M = [int(x) for x in input().split()]
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    worse, better = [int(x) for x in input().split()]
    graph[better][worse] = 1
    graph[worse][better] = -1


for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][k] == graph[k][j] and graph[i][k] != 0:
                graph[i][j] = graph[i][k]

count = N
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i != j and graph[i][j] == 0:
            count -= 1
            break

print(count)