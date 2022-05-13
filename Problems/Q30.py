def count_query(words_by_length, query):
    len_query = len(query)
    count = 0

    for word in words_by_length[len_query]:
        if len(word) != len_query:
            continue


def binary_search(arr, x, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < x:
            start = mid + 1
        elif arr[mid] > x:
            end = mid - 1
        else:
            return mid


if __name__ == '__main__':
    words = [x for x in input().split()]
    queries = [x for x in input().split()]
    words_by_length = {}
    results = []
    
    for word in words:
        word_len = len(word)
        words_by_length.get(word_len, []).append(word)

    for query in queries:
        results.append(count_query(words_by_length, query))

    print(results)
