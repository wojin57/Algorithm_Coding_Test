import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    queue = []
    for i, time in enumerate(food_times, 1):
        heapq.heappush(queue, (time, i))

    time_spent = 0
    prev_spent = 0
    remaining_foods = len(food_times)

    while time_spent + ((queue[0][0] - prev_spent) * remaining_foods) <= k:
        cur_time = heapq.heappop(queue)[0]
        time_spent += (cur_time - prev_spent) * remaining_foods
        remaining_foods -= 1
        prev_spent = cur_time

    result = sorted(queue, key=lambda x: x[1])
    return result[(k - time_spent) % remaining_foods][1]


if __name__ == '__main__':
    food_times = [int(x) for x in input().split()]
    k = int(input())
    print(solution(food_times, k))
