from re import U


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
has_cycle = False


for i in range(num_edges):
    a, b = [int(x) for x in input().split()]

    if find_parent(parent, a) == find_parent(parent, b):
        has_cycle = True
        break
    else:
        union_parent(parent, a, b)

if has_cycle:
    print("Cycle occurs")
else:
    print("Cycle doesn't occur")
    