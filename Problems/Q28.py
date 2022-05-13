def fixed_point(arr, N):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] < mid:
            start = mid + 1
        elif arr[mid] > mid:
            end = mid - 1
        else:
            return mid

    return -1


if __name__ == '__main__':
    N = int(input())
    numbers = [int(x) for x in input().split()]
    print(fixed_point(numbers, N))
    