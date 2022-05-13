N, K = [int(x) for x in input().split(' ')]
A = [int(x) for x in input().split(' ')]
B = [int(x) for x in input().split(' ')]

A = sorted(A)
B = sorted(B, reverse=True)

for i in range(K):
    if A[i] > B[i]:
        K = i
        break
    
print(sum(A[K:] + B[:K]))
