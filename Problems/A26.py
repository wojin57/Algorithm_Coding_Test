import heapq

N = int(input())
numbers = [int(input()) for _ in range(N)]
heap = []
result = 0

for num in numbers:
    heapq.heappush(heap, num)

while len(heap) > 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    sum = first + second
    result += sum
    heapq.heappush(heap, sum)

print(result)
