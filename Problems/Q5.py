N, M = [int(x) for x in input().split()]
input_data = [int(x) for x in input().split()] 
count_weights = [0] * (M + 1)

for weight in input_data:
    count_weights[weight] += 1

combs = 0

for i in range(1, M + 1):
    combs += (count_weights[i] * (N - count_weights[i]))
    N -= count_weights[i]

print(combs)
