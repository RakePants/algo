INF = float('inf')

n = int(input())
a = [[0] * n for _ in range(n)]

for i in range(n):
    a[i] = [int(x) if int(x) != -1 else INF for x in input().split()]


for k in range(n):
    for i in range(n):
        for j in range(n):
            if a[i][j] > a[i][k] + a[k][j]:
                a[i][j] = a[i][k] + a[k][j]

k = 0
for i in range(n):
    for j in range(n):
        if a[i][j] < INF and a[i][j] > k:
            k = a[i][j]

print(k)
