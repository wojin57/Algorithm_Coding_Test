import sys

input = sys.stdin.readline
INF = int(1e9)

num_vertices, num_edges = [int(x) for x in input().split(' ')]
start = int(input())
graph = [[] for _ in range(num_vertices + 1)]
visited = [False] * (num_vertices + 1)
distance = [INF] * (num_vertices + 1)

for _ in range(num_edges):
    src, dest, dist = [int(x) for x in input().split(' ')]
    graph[src].append((dest, dist))


def get_smallest_node():
    min_dist = INF
    index = 0
    for i in range(1, num_vertices + 1):
        if distance[i] < min_dist and not visited[i]:
            min_dist = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for dest, dist in graph[start]:
        distance[dest] = dist

    for i in range(num_vertices - 1):
        cur = get_smallest_node()
        visited[cur] = True

        for dest, dist in graph[cur]:
            cur_dist = distance[cur] + dist

            if cur_dist < distance[dest]:
                distance[dest] = cur_dist


dijkstra(start)

for i in range(1, num_vertices + 1):
    if distance[i] == INF:
        print("INFINITY", end=' ')
    
    else:
        print(distance[i], end=' ')

print()
