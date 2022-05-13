from copy import deepcopy


def virus(maps, r, c, N, M):
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < M:
            if maps[nr][nc] == 0:
                maps[nr][nc] = 2
                virus(maps, nr, nc, N, M)

def count_safe_zone(maps, N, M):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                cnt += 1
    
    return cnt


def dfs(maps, N, M, count):
    global result

    if count == 3:
        copy_maps = deepcopy(maps)

        for i in range(N):
            for j in range(M):
                if copy_maps[i][j] == 2:
                    virus(copy_maps, i, j, N, M)

        result = max(result, count_safe_zone(copy_maps, N, M))
        return

    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                maps[i][j] = 1
                count += 1
                dfs(maps, N, M, count)
                maps[i][j] = 0
                count -= 1


if __name__ == '__main__':
    N, M = [int(x) for x in input().split()]
    maps = [[int(x) for x in input().split()] for _ in range(N)]
    result = 0
    dfs(maps, N, M, 0)
    print(result)
