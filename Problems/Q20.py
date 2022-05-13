from itertools import combinations


def add_obstacles(maps, combs):
    for i, j in combs:
        maps[i][j] = 'O'


def delete_obstacles(maps, combs):
    for i, j in combs:
        maps[i][j] = 'X'


def detect(maps, teachers, N):
    for t in teachers:
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            x, y = t
            x += dx
            y += dy

            while 0 <= x < N and 0 <= y < N:
                if maps[x][y] == 'S':
                    return True
                elif maps[x][y] == 'O':
                    break

                x += dx
                y += dy

    return False


if __name__ == '__main__':
    N = int(input())
    maps = [[x for x in input().split()] for _ in range(N)]
    empty = []
    teachers = []
    result = "NO"

    for i in range(N):
        for j in range(N):
            if maps[i][j] == 'X':
                empty.append((i, j))
            elif maps[i][j] == 'T':
                teachers.append((i, j))

    for comb in combinations(empty, 3):
        add_obstacles(maps, comb)
        if detect(maps, teachers, N):
            delete_obstacles(maps, comb)
            continue

        result = "YES"
        break
        
    print(result)
