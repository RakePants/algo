n = int(input())
d = []
for i in range(n):
    a = list(map(int, input().split()))
    d.append(a)
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
for i in range(n):
    print(" ".join(map(str, d[i])))