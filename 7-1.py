import sys


def binary_search(lst, target, start, end):
    while start <= end:
        middle = (start + end) // 2
        if lst[middle] < target:
            start = middle + 1
        elif lst[middle] == target:
            return "yes"
        else:
            end = middle - 1
    return "no"


N = int(input())
parts_stocks = [int(x) for x in sys.stdin.readline().rstrip().split(' ')]
M = int(input())
parts_checks = [int(x) for x in sys.stdin.readline().rstrip().split(' ')]

parts_stosks = sorted(parts_stocks)
for check in parts_checks:
    print(binary_search(parts_stocks, check, 0, N - 1), end=' ')

print()
