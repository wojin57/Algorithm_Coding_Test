from collections import deque

N, M = [int(x) for x in input().split(' ')]
maps = [[int(x) for x in input()] for _ in range(N)]
forest = [[] for _ in range(N * M)]
neighbor_dist = [(-1, 0), (1, 0), (0, -1), (0, 1)]
count = 0


def forest_construction(x, y):
    for dist in neighbor_dist:
        nx = x + dist[0]
        ny = y + dist[1]
        
        if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 0:
            forest[x * M + y].append(nx * M + ny)
            

def bfs(graph, start_vertex):
    queue = deque([start_vertex])

    while queue:
        vertex = queue.popleft()
        
        for i in graph[vertex]:
            if maps[i // M][i % M] == 0:
                queue.append(i)
                maps[i // M][i % M] = 1


for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            forest_construction(i, j)


for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            bfs(forest, i * M + j)
            count += 1

print(count)
