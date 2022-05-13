def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x]) 

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

for i in range(1, num_vertices + 1):
    parent[i] = i

for i in range(num_edges):
    a, b = [int(x) for x in input().split()]
    union_parent(parent, a, b)

print("Sets for each element: ", end='')
for i in range(1, num_vertices + 1):
    print(find_parent(parent, i), end=' ')

print()

print("Parent table: ", end='')
for i in range(1, num_vertices + 1):
    print(parent[i], end=' ')

print()
