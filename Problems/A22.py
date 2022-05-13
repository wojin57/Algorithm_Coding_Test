from collections import deque


def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    
    # Step 1. move directly
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        npos1_x, npos1_y, npos2_x, npos2_y = pos1_x + dx, pos1_y + dy, pos2_x + dx, pos2_y + dy
        if board[npos1_x][npos1_y] == 0 and board[npos2_x][npos2_y] == 0:
            next_pos.append({(npos1_x,npos1_y), (npos2_x, npos2_y)})

    # Step 2. spin
    if pos1_x == pos2_x:    # robot stands horizontally
        for i in [-1, 1]:
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    else:   # robot stands vertically
        for i in [-1, 1]:
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})

    return next_pos
    

def solution(board, N):
    new_board = [[1] * (N + 2) for _ in range(N + 2)]

    for i in range(N):
        for j in range(N):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)

    while q:
        pos, time = q.popleft()

        if (N, N) in pos:
            return time

        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, time + 1))
                visited.append(next_pos)

    return 0



if __name__ == '__main__':
    N = int(input())
    board = [[int(x) for x in input().split()] for _ in range(N)]
    print(solution(board, N))