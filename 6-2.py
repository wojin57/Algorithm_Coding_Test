N = int(input())
grades = [(input().split(' ')) for _ in range(N)]
grades = sorted(grades, key=lambda x:int(x[1]))

for name, _ in grades:
    print(name, end=' ')

print()
