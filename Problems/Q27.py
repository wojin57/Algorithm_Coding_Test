def binary_search(arr, x, option):   
    start = 0
    end = len(arr) - 1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] < x:
            start = middle + 1
        elif arr[middle] > x:
            end = middle - 1
        elif option == 0 and middle > 0 and arr[middle - 1] == x:
            end = middle - 1
        elif option == 1 and middle < len(arr) and arr[middle + 1] == x:
            start = middle + 1
        else:
            return middle
        
    return start


N, x = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]

print(binary_search(numbers, x, 1) - binary_search(numbers, x, 0) + 1)
