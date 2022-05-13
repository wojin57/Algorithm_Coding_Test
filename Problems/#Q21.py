def check(pops, N, L, R):
    visited = [False] * (N * N)

    for i in range(N):
        for j in range(N):
            sum = pops[i][j]
            count = 1
            for di, dj in [(0, 1), (1, 0)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    diff = pops[i][j] - pops[ni][nj]
                    if L <= abs(diff) <= R:
                        sum += pops[ni][nj]
                        count += 1


if __name__ == '__main__':
    N, L, R = [int(x) for x in input().split()]
    populations = [[int(x) for x in input().split()] for _ in range(N)]

    moves = 0

    while check(populations, N, L, R):
        moves += 1

    print(moves)
