n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0
first = {}
second = {}

for i in range(n):
    if a[i] not in first.keys():
        first[a[i]] = 1
    else:
        first[a[i]] += 1
for j in range(m):
    if b[j] not in second.keys():
        second[b[j]] = 1
    else:
        second[b[j]] += 1
    
for k, v in first.items():
    if k in second.keys():
        cnt += first[k] * second[k]
    
print(cnt)