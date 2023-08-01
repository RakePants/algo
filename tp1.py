n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

one = 0
two = 0

for i in range(n + m):
    if one >= n:
        print(b[two], end=' ')
        two += 1
    elif two >= m:
        print(a[one], end=' ')
        one += 1
    elif a[one] <= b[two]:
        print(a[one], end=' ')
        one += 1
    else:
        print(b[two], end=' ')
        two += 1
