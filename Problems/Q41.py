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


def check_route(parent):
    route = {int(x) for x in input().split()}
    par = find_parent(parent, route.pop())
    for city in route:
        if find_parent(parent, city) != par:
            print("NO")
            return

    print("YES")


N, M = [int(x) for x in input().split()]
parent = [i for i in range(N + 1)]

for i in range(1, N + 1):
    adj_list = [int(x) for x in input().split()]
    for j in range(N):
        if adj_list[j] == 1:
            union_parent(parent, i, j + 1)

check_route(parent)