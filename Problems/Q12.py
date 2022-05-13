def find(result, x, y, option):
    if not result:
        return False

    for build in result:
        if build == [x, y, option]:
            return True
    return False


def is_vaild(result, x, y, option):
    COLUMN, BEAM = 0, 1
    if option == COLUMN:
        if y == 0 or find(result, x - 1, y, BEAM) or find(result, x, y, BEAM) or find(result, x, y - 1, COLUMN):
            return True
    else:
        if find(result, x, y - 1, COLUMN) or find(result, x + 1, y - 1, COLUMN) or (find(result, x - 1, y, BEAM) and find(result, x + 1, y, BEAM)):
            return True
    
    return False


def operating(build, result):
    x, y, a, b = build
    if b == 0:
        stupid_destructing(result, x, y, a)
        # destructing(result, x, y, a)
    else:
        building(result, x, y, a)        


def stupid_destructing(result, x, y, option):
    result.remove([x, y, option])
    
    if not result:
        return

    for xx, yy, op in result:
        if not is_vaild(result, xx, yy, op):
            result.append([x, y, option])
            return
    

def destructing(result, x, y, option):
    COLUMN, BEAM = 0, 1
    result.remove([x, y, option])
    
    if option == COLUMN:
        if find(result, x, y + 1, COLUMN) and not is_vaild(result, x, y + 1, COLUMN):
            result.append([x, y, option])
            return
        
        if find(result, x, y + 1, BEAM) and not is_vaild(result, x, y + 1, BEAM):
            result.append([x, y, option])
            return
        
        if find(result, x - 1, y + 1, BEAM) and not is_vaild(result, x - 1, y + 1, BEAM):
            result.append([x, y, option])
            return
    else:
        if find(result, x, y, COLUMN) and not is_vaild(result, x, y, COLUMN):
            result.append([x, y, option])
            return
    
        if find(result, x + 1, y, COLUMN) and not is_vaild(result, x + 1, y, COLUMN):
            result.append([x, y, option])
            return
    
        if find(result, x - 1, y, BEAM) and not is_vaild(result, x, y, BEAM):
            result.append([x, y, option])
            return
    
        if find(result, x + 1, y, BEAM) and not is_vaild(result, x + 1, y, BEAM):
            result.append([x, y, option])
            return
    
def building(result, x, y, option):
    if is_vaild(result, x, y, option):
        result.append([x, y, option])


if __name__ == '__main__':
    n = int(input())
    ops = int(input())
    build_frame = [[int(x) for x in input().split()] for _ in range(ops)]
    result = []
    for build in build_frame:
        operating(build, result)

    result.sort()
    for build in result:
        for i in build:
            print(i, end=' ')
        print()
