from itertools import permutations


def operate(a, b, op):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    elif op == 3:
        if a < 0:
            return -(-a // b)
        return a // b


def calculate(numbers, ops):
    result = numbers[0]
    for i, op in enumerate(ops):
        result = operate(result, numbers[i + 1], op)

    return result


def operation_mixer(num_ops):
    ops = []
    for i, num in enumerate(num_ops):
        for _ in range(num):
            ops.append(i)

    return set(permutations(ops))


if __name__ == '__main__':
    N = int(input())
    numbers = [int(x) for x in input().split()]
    num_ops = [int(x) for x in input().split()]
    min_result = int(1e9)
    max_result = -int(1e9)

    for ops in operation_mixer(num_ops):
        result = calculate(numbers, ops)
        min_result = min(min_result, result)
        max_result = max(max_result, result)

    print(max_result)
    print(min_result)
