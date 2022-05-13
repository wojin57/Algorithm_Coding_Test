from collections import deque
import copy

N = int(input())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
time = [0] * (N + 1)

for i in range(1, N + 1):
    input_data = [int(x) for x in input().split()]
    time[i] = input_data[0]
    indegree[i] = len(input_data) - 2
    for pre in input_data[1:-1]:
        graph[pre].append(i)
    

def topology_sort():
    result = copy.deepcopy(time)
    queue = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        cur = queue.popleft()
        for dest in graph[cur]:
            result[dest] = max(result[dest], result[cur] + time[dest])
            indegree[dest] -= 1

            if indegree[dest] == 0:
                queue.append(dest)
    
    for i in range(1, N + 1):
        print(result[i])


topology_sort()
