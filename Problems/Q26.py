N = int(input())
numbers = [int(input()) for _ in range(N)]

if N == 1:
    print(numbers[0])
else:
    numbers.sort()
    comparison = 0
    for i in range(len(numbers) - 1):
        a = numbers[i]
        b = numbers[i + 1]

    print(comparison)
