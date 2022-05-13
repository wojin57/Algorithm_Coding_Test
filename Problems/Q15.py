from collections import deque
import sys


def find_and_print(dist, K):
    found = False
    for i, d in enumerate(dist):
        if d == K:
            found = True
            print(i)

    if not found:
        print(-1)


N, M, K, X = [int(x) for x in sys.stdin.readline().split()]
graph = [[] for _ in range(N + 1)]
dist = [-1] * (N + 1)

for _ in range(M):
    src, dest = [int(x) for x in sys.stdin.readline().split()]
    graph[src].append(dest)

queue = deque([X])
dist[X] = 0

while queue:
    cur = queue.popleft()
    for dest in graph[cur]:
        if dist[dest] == -1:
            dist[dest] = dist[cur] + 1
            queue.append(dest)


find_and_print(dist, K)
