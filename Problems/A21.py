from collections import deque


def process(pops, union, r, c, index):
    united = [(r, c)]
    q = deque()
    q.append((r, c))
    union[r][c] = index
    pop_sum = pops[r][c]
    
    while q:
        r, c = q.popleft()

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N and union[nr][nc] == -1:
                if L <= abs(pops[r][c] - pops[nr][nc]) <= R:
                    q.append((nr, nc))
                    union[nr][nc] = index
                    pop_sum += pops[nr][nc]
                    united.append((nr, nc))

    new_pop = pop_sum // len(united)
    for r, c in united:
        pops[r][c] = new_pop


if __name__ == '__main__':
    N, L, R = [int(x) for x in input().split()]
    populations = [[int(x) for x in input().split()] for _ in range(N)]
    moves = 0

    while True:
        union = [[-1] * N for _ in range(N)]
        index = 0
        for i in range(N):
            for j in range(N):
                if union[i][j] == -1:
                    process(populations, union, i, j, index)
                    index += 1

        if index == N * N:
            break

        moves += 1

    print(moves)
