input_str = input()
zeros = 0
ones = 0
cur = input_str[0]

for c in input_str:
    if cur != c:
        if cur == "0":
            zeros += 1
        else:
            ones += 1
        cur = c

if input_str[-1] == "0":
    zeros += 1
else:
    ones += 1
    
print(min(zeros, ones))
