INF = int(1e9)

num_vertices = int(input())
num_edges = int(input())

graph = [[INF] * (num_vertices + 1) for _ in range(num_vertices + 1)]

for idx in range(num_vertices + 1):
    graph[idx][idx] = 0

for _ in range(num_edges):
    src, dest, dist = [int(x) for x in input().split(' ')]
    graph[src][dest] = dist

for md in range(1, num_vertices + 1):
    for src in range(1, num_vertices + 1):
        for dest in range(1, num_vertices + 1):
            graph[src][dest] = min(graph[src][dest], graph[src][md] + graph[md][dest])


for src in range(1, num_vertices + 1):
    for dest in range(1, num_vertices + 1):
        if graph[src][dest] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[src][dest], end=' ')
    print()
