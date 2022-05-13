def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def is_same_team(parent, a, b, results):
    if parent[a] == parent[b]:
        results.append("YES")
    else:
        results.append("NO")


N, M = [int(x) for x in input().split()]
parent = [i for i in range(N + 1)]
results = []

for _ in range(M):
    op, a, b = [int(x) for x in input().split()]

    if op == 0:
        union(parent, a, b)
    else:
        is_same_team(parent, a, b, results)

for result in results:
    print(result)