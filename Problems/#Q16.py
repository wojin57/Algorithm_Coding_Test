from itertools import combinations
from copy import deepcopy


def find(maps, N, M, option):
    found = []

    for i in range(N):
        for j in range(M):
            if maps[i][j] == option:
                found.append((i, j))

    return found


def safe_search(maps, N, M, r, c):
    if not (0 <= r < N and 0 <= c < M):
        return -1

    return maps[r][c]


def simulate(maps, N, M, add_walls):
    copy_maps = deepcopy(maps)

    for r, c in add_walls:
        copy_maps[r][c] == 1

    
    return len(find(copy_maps, N, M, 0))


N, M = [int(x) for x in input().split()]
maps = [[int(x) for x in input().split()] for _ in range(N)]
zeros = []

for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            zeros.append((i, j))

graph = []

max_safe = 0
for comb in combinations(zeros, 3):
    max_safe = max(max_safe, simulate(maps, N, M, comb))

print(max_safe)