S = input()
result = []
sum = 0

for ch in S:
    if ch.isalpha():
        result.append(ch)
    else:
        sum += int(ch)

result.sort()

if sum != 0:
    result.append(str(sum))

print(''.join(result))
