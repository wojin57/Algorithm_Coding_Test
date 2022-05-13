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


num_vertices, num_edges = [int(x) for x in input().split()]
parent = [i for i in range(num_vertices + 1)]
edges = []
min_costs = 0

for _ in range(num_edges):
    a, b, cost = [int(x) for x in input().split()]
    edges.append((cost, a, b))

edges.sort()

for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        min_costs += cost

print(min_costs)
