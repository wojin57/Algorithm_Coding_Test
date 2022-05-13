def get_coords(matrix, n, target):
    result = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == target:
                result.append((i, j))
    
    return result


def rotate_clockwise(coords, n):
    new_coords = []

    for x, y in coords:
        new_coords.append((y, n - 1 - x))
    
    return new_coords


def move(key_coords, N, dx, dy):
    result = []
    
    if key_coords is None:
        return result

    for x, y in key_coords:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < N:
            result.append((nx, ny))

    return result


def is_matched(key_coords, lock_coords):
    key_coords.sort()
    lock_coords.sort()

    return key_coords == lock_coords


def checking(key_coords, lock_coords, N, M):
    for _ in range(4):
        for dx in range(-M + 1, N):
            for dy in range(-M + 1, N):
                moved_key_coords = move(key_coords, N, dx, dy)
                
                if is_matched(moved_key_coords, lock_coords):
                    return True

        key_coords = rotate_clockwise(key_coords, M)
    
    return False


if __name__ == '__main__':
    N, M = [int(x) for x in input().split()]
    key = [[int(x) for x in input().split()] for _ in range(M)]
    lock = [[int(x) for x in input().split()] for _ in range(N)]
    key_coords = get_coords(key, M, 1)
    lock_coords = get_coords(lock, N, 0)
    answer = checking(key_coords, lock_coords, N, M)
    print(answer)
