if __name__ == '__main__':
    N = int(input())
    houses = [int(x) for x in input().split()]
    houses.sort()
    print(houses[(N - 1) // 2])
