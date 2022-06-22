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

    
G = int(input())
P = int(input())
limits = [int(input()) for _ in range(P)]
parent = [i for i in range(G + 1)]

result = 0
for i in range(P):
    root = find_parent(parent, limits[i])
    if root == 0:
        break

    union_parent(parent, root, root - 1)
    result += 1

print(result)
