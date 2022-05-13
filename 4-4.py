N, M = [int(x) for x in input().split(' ')]
x, y, direction = [int(x) for x in input().split(' ')]
maps = [[int(x) for x in input().split(' ')] for list in range(N)]
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
count = 1
turn_count = 0


def is_new(x, y, move):
    return maps[x + move[0]][y + move[1]] == 0


maps[x][y] = 2
while True:
    direction = (direction + 3) % 4

    if is_new(x, y, moves[direction]):
       x += moves[direction][0] 
       y += moves[direction][1]
       maps[x][y] = 2
       count += 1
       turn_count = 0
    else:
        turn_count += 1

    if turn_count == 4:
        x -= moves[direction][0]
        y -= moves[direction][1]
        if maps[x][y] == 1:
            break
        turn_count = 0

print(count)
