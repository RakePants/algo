n, k = map(int, input().split())
a = list(map(int, input().split()))
qs = list(map(int, input().split()))

def bin(a, q):
    l = 0
    r = len(a) - 1
    while l <= r:
        mid = (l + r) // 2

        if a[mid] < q:
            l = mid + 1
        else:
            r = mid - 1

    return r + 2

for q in qs:
    if q <= a[-1]:
        print(bin(a, q))
    else:
        print(n + 1)
