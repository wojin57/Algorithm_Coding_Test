from bisect import bisect_left, bisect_right


def count_by_range(arr, left, right):
    right_index = bisect_right(arr, right)
    left_index = bisect_left(arr, left)
    return right_index - left_index


def solution(ws, queries):
    answer = []
    words = [[] for _ in range(10001)]
    rwords = [[] for _ in range(10001)]

    for word in ws:
        len_word = len(word)
        words[len_word].append(word)
        rwords[len_word].append(word[::-1])

    for wds in words:
        wds.sort()
    
    for wds in rwords:
        wds.sort()

    for q in queries:
        if q[0] != '?':
            res = count_by_range(words[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            q = q[::-1]
            res = count_by_range(rwords[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        answer.append(res)

    return answer
    

if __name__ == '__main__':
    words = [x for x in input().split()]
    queries = [x for x in input().split()]
    print(solution(words, queries))
