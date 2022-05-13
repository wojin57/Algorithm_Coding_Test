import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

num_vertices, num_edges = [int(x) for x in input().split(' ')]
start = int(input())
graph = [[] for _ in range(num_vertices + 1)]
distance = [INF] * (num_vertices + 1)

for _ in range(num_edges):
    src, dest, dist = [int(x) for x in input().split(' ')]
    graph[src].append((dest, dist))


def dijkstra_improved(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        cur_dist, cur = heapq.heappop(queue)
        
        if distance[cur] < cur_dist:
            continue

        for dest, dist in graph[cur]:
            new_dist = cur_dist + dist

            if new_dist < distance[dest]:
                distance[dest] = new_dist
                heapq.heappush(queue, (new_dist, dest))


dijkstra_improved(start)

for i in range(1, num_vertices + 1):
    if distance[i] == INF:
        print("INFINITY", end=' ')
    else:
        print(distance[i], end=' ')

print()
