INF = int(1e9)

num_cities, num_edges, city = [int(x) for x in input().split()]
graph = [[INF] * (num_cities + 1) for _ in range(num_cities + 1)]


for idx in range(num_cities + 1):
    graph[idx][idx] = 0

for _ in range(num_edges):
    src, dest, dist = [int(x) for x in input().split()]
    graph[src][dest] = dist

for md in range(num_cities):
    for src in range(num_cities):
        for dest in range(num_cities):
            graph[src][dest] = min(graph[src][dest], graph[src][md] + graph[md][dest])

connect_cities = 0
max_dist = 0
for dest in range(1, num_cities + 1):
    if dest != city and graph[city][dest] != INF:
        connect_cities += 1
        max_dist = max(max_dist, graph[city][dest])

print(connect_cities, max_dist)
