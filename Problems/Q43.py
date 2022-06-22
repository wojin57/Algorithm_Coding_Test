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
parent = [i for i in range(N)]
roads = []
total_cost = 0
minimum_cost = 0

for _ in range(M):
    h1, h2, cost = [int(x) for x in input().split()]
    total_cost += cost
    roads.append((cost, h1, h2))

roads.sort()

for cost, h1, h2 in roads:
    if find_parent(parent, h1) != find_parent(parent, h2):
        union_parent(parent, h1, h2)
        minimum_cost += cost

print(total_cost - minimum_cost)
