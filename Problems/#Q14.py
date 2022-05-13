from collections import deque
from copy import deepcopy


def work(n, weak, d):
    start = weak[0]
    cl = []
    cntcl = []
    weak.remove(start)

    for w in weak:
        if (w - start) % n <= d:
            cl.append(w)
        else:
            break

    weak.reverse()
    for w in weak:
        if (start - w) % n <= d:
            cntcl.append(w)
        else:
            break

    if len(cl) >= len(cntcl):
        return cl
    else:
        return cntcl


def remove_items(weak, items):
    for item in items:
        weak.remove(item)


if __name__ == '__main__':
    n = int(input())
    weak = [int(x) for x in input().split()]
    dist = [int(x) for x in input().split()]
    dist.sort(reverse=True)
    weak = deque(weak)
    answer = len(dist) + 1

    for _ in range(len(weak)):
        weak.append(weak.popleft())
        weak_copy = deepcopy(weak)
        cnt = 0

        for d in dist:
            cnt += 1
            removes = work(n, weak_copy, d)
            remove_items(weak_copy, removes)

            if not weak_copy:
                answer = min(answer, cnt)
                break
    
    if answer == len(dist) + 1:
        answer = -1

    print(answer)
