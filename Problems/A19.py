def dfs(idx, cur_value, N, numbers, num_ops):
    global min_result, max_result
    
    if idx == N:
        min_result = min(min_result, cur_value)
        max_result = max(max_result, cur_value)
    else:
        if num_ops[0] > 0:
            num_ops[0] -= 1
            dfs(idx + 1, cur_value + numbers[idx], N, numbers, num_ops)
            num_ops[0] += 1
        if num_ops[1] > 0:
            num_ops[1] -= 1
            dfs(idx + 1, cur_value - numbers[idx], N, numbers, num_ops)
            num_ops[1] += 1
        if num_ops[2] > 0:
            num_ops[2] -= 1
            dfs(idx + 1, cur_value * numbers[idx], N, numbers, num_ops)
            num_ops[2] += 1
        if num_ops[3] > 0:
            num_ops[3] -= 1
            dfs(idx + 1, int(cur_value / numbers[idx]), N, numbers, num_ops)
            num_ops[3] += 1


if __name__ == '__main__':
    N = int(input())
    numbers = [int(x) for x in input().split()]
    num_ops = [int(x) for x in input().split()]
    min_result = int(1e9)
    max_result = -int(1e9)

    dfs(1, numbers[0], N, numbers, num_ops)
    print(max_result)
    print(min_result)
