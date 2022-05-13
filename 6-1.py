N = int(input())

nums = [int(input()) for _ in range(N)]
nums = sorted(nums, reverse=True)

for num in nums:
    print(num, end=' ')

print()
