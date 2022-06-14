def find_shortest_path():
    N = int(input())
    cost = [[int(x) for x in input().split()] for _ in range(N)]
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    INF = int(1e9)
    graph = [[INF] * (N * N) for _ in range(N * N)]
    
    for row in range(N):
        for col in range(N):
            graph[row * N + col][row * N + col] = cost[row][col]
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < N and 0 <= nc < N:
                    graph[row * N + col][nr * N + nc] = cost[nr][nc]


    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    
    return graph[0][N * N - 1]


T = int(input())
answers = []
for _ in range(T):
    answers.append(find_shortest_path())

for i in range(T):
    print(answers[i])
