n, k = map(int, input().split())
a = list(map(int, input().split()))
qs = list(map(int, input().split()))

def bin(a, q):
    l = 0
    r = len(a)
    while (r - l) > 1:
        mid = (l + r) // 2

        if a[mid] <= q:
            l = mid
        else:
            r = mid

    return l + 1

for q in qs:
    if q >= a[0]:
        print(bin(a, q))
    else:
        print(0)
