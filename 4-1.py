N = int(input())
x, y = 1, 1
moves = [x for x in input().split(' ')]

for move in moves:
    if move == 'L' and y != 1:
        y -= 1
    elif move == 'R' and y != N:
        y += 1
    elif move == 'U' and x != 1:
        x -= 1
    elif move == 'D' and x != N:
        x += 1

print(x, y)
