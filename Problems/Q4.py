N = int(input())
coins = [int(x) for x in input().split()]
coins.sort()

target = 1
for coin in coins:
    if target < coin:
        break
    target += coin

print(target)
