from collections import deque

N, M = [int(x) for x in input().split(' ')]
maps = [[int(x) for x in input()] for _ in range(N)]
forest = [[] for _ in range(N * M)]
neighbor_dist = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def forest_construction(x, y):
    for dist in neighbor_dist:
        nx = x + dist[0]
        ny = y + dist[1]
        
        if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1:
            forest[x * M + y].append(nx * M + ny)


def bfs(graph, start_vertex, count):
    queue = deque([start_vertex])

    while queue:
        vertex = queue.popleft()
        
        if vertex == N * M - 1:
            return maps[N - 1][M - 1]

        for i in graph[vertex]:
            if maps[i // M][i % M] == 1:
                queue.append(i)
                maps[i // M][i % M] = maps[vertex // M][vertex % M] + 1


for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            forest_construction(i, j)


count = bfs(forest, 0, 0)
print(count)
