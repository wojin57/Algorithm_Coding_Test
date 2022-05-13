import heapq

INF = int(1e9)
num_vertices, num_edges = [int(x) for x in input().split()]
graph = [[] for _ in range(num_vertices + 1)]
distance = [INF] * (num_vertices + 1)

for _ in range(num_edges):
    src, dest = [int(x) for x in input().split(' ')]
    graph[src].append(dest)
    
dest, stop = [int(x) for x in input().split()]

def dijkstra_improved(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        cur_dist, cur = heapq.heappop(queue)
        if distance[cur] < cur_dist:
            continue

        for dest in graph[cur]:
            new_dist = cur_dist + 1

            if new_dist < distance[dest]:
                distance[dest] = new_dist
                heapq.heappush(queue, (new_dist, dest))

dijkstra_improved(1)
dist = distance[stop]
dijkstra_improved(stop)
dist += distance[dest]

if dist >= INF:
    dist = -1

print(dist)