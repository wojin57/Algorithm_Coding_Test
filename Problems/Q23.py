if __name__ == '__main__':
    N = int(input())
    students = [[x for x in input().split()] for _ in range(N)]

    for s in students:
        s[1] = int(s[1])
        s[2] = int(s[2])
        s[3] = int(s[3])

    students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

    for name, *args in students:
        print(name)
