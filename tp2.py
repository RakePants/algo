n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
cnt = 0

for j in range(len(b)):
    while (i < n) and (a[i] <= b[j]):
        if a[i] < b[i]:
            i += 1
        cnt += 1
        
    print(cnt, end=' ')