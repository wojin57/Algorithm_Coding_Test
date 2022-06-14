import heapq
import sys

INF = int(1e9)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
T = int(input())
answers = []

for _ in range(T):
    N = int(input())
    graph = []
    for i in range(N):
        graph.append([int(x) for x in sys.stdin.readline().split()])
    
    distance = [[INF] * N for _ in range(N)]
    r, c = 0, 0
    q = [(graph[r][c], r, c)]
    distance[r][c] = graph[r][c]

    while q:
        dist, r, c = heapq.heappop(q)
        if distance[r][c] < dist:
            continue
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N:
                cost = dist + graph[nr][nc]
                if cost < distance[nr][nc]:
                    distance[nr][nc] = cost
                    heapq.heappush(q, (cost, nr, nc))

    answers.append(distance[N - 1][N - 1])

for i in range(T):
    print(answers[i])