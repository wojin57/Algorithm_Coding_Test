import sys

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


def get_distance(c1, c2):
    return abs(c1 - c2)


N = int(input())
coords = {i: [int(x) for x in sys.stdin.readline().split()] for i in range(N)}
parent = [i for i in range(N)]
edges = []

for c in range(3):
    sorted_coords = sorted(coords, key=lambda k: coords.get(k)[c])
    prev = sorted_coords[0]
    for cur in sorted_coords[1:]:
        edges.append((abs(coords.get(prev)[c] - coords.get(cur)[c]), prev, cur))
        prev = cur


edges.sort()
min_cost = 0
for cost, i, j in edges:
    if find_parent(parent, i) != find_parent(parent, j):
        min_cost += cost
        union_parent(parent, i, j)

print(min_cost)
