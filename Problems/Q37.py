import sys

n = int(input())
m = int(input())
INF = int(1e9)

distance = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    distance[i][i] = 0

for _ in range(m):
    src, dest, dist = [int(x) for x in sys.stdin.readline().split()]
    distance[src][dest] = min(distance[src][dest], dist)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for src in range(1, n + 1):
    for dest in range(1, n + 1):
        if distance[src][dest] == INF:
            print(0, end = ' ')
        else:
            print(distance[src][dest], end=' ')

    print()