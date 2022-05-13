from collections import deque


def bfs(graph, start_vertex, visited):
    queue = deque([start_vertex])
    visited[start_vertex] = True

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        for i in graph[vertex]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    print()


graph =  [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
