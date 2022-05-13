def solution(N, stages):
    counts = [0] * (N + 2)
    fail_rates = []
    remaining_counts = len(stages)

    for stage in stages:
        counts[stage] += 1

    for lv, cnt in enumerate(counts[1:-1], 1):
        if remaining_counts == 0:
            fail_rates.append((lv, 0))
        else:
            fail_rates.append((lv, cnt / remaining_counts))
            remaining_counts -= cnt

    fail_rates.sort(key=lambda x: x[1], reverse=True)

    for lv, _ in fail_rates:
        print(lv)

    
if __name__ == '__main__':
    N = int(input())
    stages = [int(x) for x in input().split()]
    solution(N, stages)
