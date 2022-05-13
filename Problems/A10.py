def rotate_clockwise(matrix, n):
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[j][n - 1 - i] = matrix[i][j]

    return result


def is_matched(new_lock, N):
    for i in range(N, N * 2):
        for j in range(N, N * 2):
            if new_lock[i][j] != 1:
                return False

    return True


def checking(key, lock, N, M):
    new_lock = [[0] * (3 * N) for _ in range(3 * N)]

    for i in range(N):
        for j in range(N):
            new_lock[i + N][j + N] = lock[i][j]


    for rotation in range(4):
        key = rotate_clockwise(key, M)

        for x in range(N * 2):
            for y in range(N * 2):
                for i in range(M):
                    for j in range(M):
                        new_lock[x + i][y + j] += key[i][j]

                if is_matched(new_lock, N):
                    return True

                for i in range(M):
                    for j in range(M):
                        new_lock[x + i][y + j] -= key[i][j]

    return False


if __name__ == '__main__':
    N, M = [int(x) for x in input().split()]
    key = [[int(x) for x in input().split()] for _ in range(M)]
    lock = [[int(x) for x in input().split()] for _ in range(N)]
    answer = checking(key, lock, N, M)
    print(answer)
