N = input()
nums = [int(x) for x in N]
len = len(N) // 2

if sum(nums[:len]) == sum(nums[len:]):
    print("LUCKY")
else:
    print("READY")
