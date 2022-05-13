from copy import deepcopy


def virus(maps, graph, r, c, N, virus_num):
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < N:
            if maps[nr][nc] == 0:
                maps[nr][nc] = virus_num
                graph[virus_num].append((nr, nc))


def bfs(maps, graph_virus, N, S, K, X, Y):
    for _ in range(S):
        for vn in range(1, K + 1):
            virus_round = deepcopy(graph_virus[vn])
            for i, j in virus_round:
                if (i, j) == (X - 1, Y - 1):
                    return
                    
                virus(maps, graph_virus, i, j, N, vn)
                graph_virus[vn].remove((i, j))


if __name__ == '__main__':
    N, K = [int(x) for x in input().split()]
    maps = [[int(x) for x in input().split()] for _ in range(N)]
    S, X, Y = [int(x) for x in input().split()]
    
    graph_virus = [[] for _ in range(K + 1)]
    for i in range(N):
        for j in range(N):
            if maps[i][j] != 0:
                graph_virus[maps[i][j]].append((i, j))
    bfs(maps, graph_virus, N, S, K, X, Y)
    print(maps[X - 1][Y - 1])
    