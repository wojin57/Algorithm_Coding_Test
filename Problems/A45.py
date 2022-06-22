import sys
from collections import deque

def arr_to_str(arr):
    s = ""
    for num in arr:
        s += str(num)
        s += " "
    
    return s


def solution():
    N = int(input())
    indegree = [0] * (N + 1)
    graph = [[False] * (N + 1) for _ in range(N + 1)]
    rank = [int(x) for x in sys.stdin.readline().split()]

    for i in range(N):
        for j in range(i + 1, N):
            graph[rank[i]][rank[j]] = True
            indegree[rank[j]] += 1

    M = int(input())
    for _ in range(M):
        a, b = [int(x) for x in sys.stdin.readline().split()]
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    for _ in range(N):
        if len(q) == 0:
            return("IMPOSSIBLE")

        if len(q) > 1:
            return("?")

        cur = q.popleft()
        result.append(cur)
        for j in range(1, N + 1):
            if graph[cur][j]:
                indegree[j] -= 1
               
                if indegree[j] == 0:
                    q.append(j)
    
    return arr_to_str(result)


if __name__ == '__main__':
    T = int(input())
    results = []

    for _ in range(T):
        results.append(solution())

    for res in results:
        print(res)
