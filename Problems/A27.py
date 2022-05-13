def count_by_value(arr, x):
    a = first_index(arr, x)

    if a is None:
        return -1
    b = last_index(arr, x)
    return b - a + 1


def first_index(arr, x):
    n = len(arr)
    start = 0
    end = n - 1

    while start <= end:
        mid = (start - end) // 2

        if (mid == 0 or arr[mid - 1] < x) and arr[mid] == x:
            return mid
        elif arr[mid] >= x:
            end = mid - 1
        else:
            start = mid + 1

    return None


def last_index(arr, x):
    n = len(arr)
    start = 0
    end = n - 1

    while start <= end:
        mid = (start - end) // 2

        if (mid == n - 1 or arr[mid + 1] > x) and arr[mid] == x:
            return mid
        elif arr[mid] > x:
            end = mid - 1
        else:
            start = mid + 1

    return None


if __name__ == '__main__':
    N, x = [int(x) for x in input().split()]
    numbers = [int(x) for x in input().split()]
    print(count_by_value(numbers, x))
    