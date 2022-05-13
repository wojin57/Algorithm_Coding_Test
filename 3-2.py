N, M, K = [int(x) for x in input().split(' ')]
nums = [int(x) for x in input().split(' ')]
max, sec_max = 1, 0

for num in nums:
    if num > max:
        sec_max = max
        max = num
    elif num > sec_max:
        sec_max = num

print(M // K, max, sec_max)
print((M // K) * sec_max + (M - M // K) * max)
