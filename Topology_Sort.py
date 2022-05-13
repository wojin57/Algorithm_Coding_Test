from collections import deque

num_vertices, num_edges = [int(x) for x in input().split()]
indegree = [0] * (num_vertices + 1)
graph = [[] for _ in range(num_vertices + 1)]

for _ in range(num_edges):
    src, dest = [int(x) for x in input().split()]
    graph[src].append(dest)
    indegree[dest] += 1


def topology_sort(graph, indegree):
    result = []
    queue = deque()

    for i in range(1, num_vertices + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        cur = queue.popleft()
        result.append(cur)

        for dest in graph[cur]:
            indegree[dest] -= 1
            if indegree[dest] == 0:
                queue.append(dest)

    for i in result:
        print(i, end=' ')
    
    print()


topology_sort(graph, indegree)
