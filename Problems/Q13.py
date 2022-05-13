from itertools import combinations

def distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def house_chicken_distance(maps, chickens, r, c):
    dist = 100
    for r_c, c_c in chickens:
        dist = min(dist, distance(r, c, r_c, c_c))

    return dist


def city_chicken_distance(maps, chickens, houses):
    dist = 0

    for i, j in houses:
        dist += house_chicken_distance(maps, chickens, i, j)

    return dist


N, M = [int(x) for x in input().split()]
maps = [[int(x) for x in input().split()] for _ in range(N)]
chickens = []
houses = []
min_chicken_dist = int(1e9)

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            houses.append((i, j))
        if maps[i][j] == 2:
            chickens.append((i, j))

for comb in combinations(chickens, M):
    min_chicken_dist = min(min_chicken_dist, city_chicken_distance(maps, comb, houses))

print(min_chicken_dist)
