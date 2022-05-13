def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = [int(x) for x in input().split()]
parent = [i for i in range(N + 1)]
edges = []
min_cost = 0
maximum = 0

for _ in range(M):
    a, b, cost = [int(x) for x in input().split()]
    edges.append((cost, a, b))

edges.sort()

for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        min_cost += cost
        if cost > maximum:
            maximum = cost

min_cost -= maximum
print(min_cost)
