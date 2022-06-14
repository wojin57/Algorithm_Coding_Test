import heapq
import sys

INF = int(1e9)
start = 1
N, M = [int(x) for x in input().split()]
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    v1, v2 = [int(x) for x in sys.stdin.readline().split()]
    graph[v1].append(v2)
    graph[v2].append(v1)

q = []
heapq.heappush(q, (0, start))
distance[start] = 0

while q:
    cur_dist, cur = heapq.heappop(q)
    
    if distance[cur] < cur_dist:
        continue

    for dest in graph[cur]:
        new_dist = cur_dist + 1

        if new_dist < distance[dest]:
            distance[dest] = new_dist
            heapq.heappush(q, (new_dist, dest))

distance.pop(0)
dist_max = max(distance)
barn_num = distance.index(dist_max) + 1
count = distance.count(dist_max)
print(barn_num, dist_max, count)
