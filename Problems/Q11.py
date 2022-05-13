from collections import deque

class Coordinate:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Snake:
    def __init__(self):
        self.coords = deque()

    def add_coord(self, c):
        self.coords.append(c)

    def is_collide(self, c):
        for coord in self.coords:
            if c == coord:
                return True
        
        return False
    
    def pop_coord(self):
        self.coords.popleft()

    def tail_direction(self):
        return self.coords[0].dir

    def x(self):
        return self.coords[-1].x

    def y(self):
        return self.coords[-1].y

def init_map(maps, apple_loc):
    for row, col in apple_loc:
        maps[row - 1][col - 1] = 1


def snake_move(maps, N, snake, dir, second):
    time = 0
    dx, dy = dir

    for _ in range(second):
        time += 1
        snake_x = snake.x()
        snake_y = snake.y()
        # 1. Out of range
        if not 0 <= snake_x + dx < N or not 0 <= snake_y + dy < N:
            return (time, False)
        
        coord = Coordinate(snake_x + dx, snake_y + dy, (dx, dy))
        # 2. Collision itself
        if snake.is_collide(coord):
            return (time, False)
            
        if maps[snake_x + dx][snake_y + dy] == 1:
            maps[snake_x + dx][snake_y + dy] = 0
        else:
            snake.pop_coord()

        snake.add_coord(coord)

    return (time, True)

N = int(input())
K = int(input())
apple_locations = [(int(x) for x in input().split()) for _ in range(K)]
L = int(input())
direction_changes = [(x for x in input().split()) for _ in range(L)]
direction_changes.append((10100, 'D'))

maps = [[0] * N for _ in range(N)]
init_map(maps, apple_locations)
snake = Snake()
snake.add_coord(Coordinate(0, 0, (0, 1)))
time = 0
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_idx = 0

for second, turn in direction_changes:
    t, cont = snake_move(maps, N, snake, directions[dir_idx], int(second) - time)
    time += t
    if not cont:
        break

    if turn == 'D':
        dir_idx = (dir_idx + 1) % 4
    else:
        dir_idx = (dir_idx - 1) % 4

print(time)