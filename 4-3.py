location = input()
x, y = ord(location[0]) - ord('a'), int(location[1]) - 1
moves = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]
count = 0


def is_valid(x, y, move):
    return 0 <= x + move[0] <= 7 and 0 <= y + move[1] <= 7


for move in moves:
    if is_valid(x, y, move):
        count += 1

print(count)
