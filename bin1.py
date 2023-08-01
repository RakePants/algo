n, k = map(int, input().split())
a = list(map(int, input().split()))
qs = list(map(int, input().split()))

def bin(a, q):
    l = 0
    r = len(a) - 1
    ans = 0
    while l <= r:
        mid = (l + r) // 2

        if a[mid] == q:
            return "YES"
        elif a[mid] < q:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    return "NO"

for q in qs:
    print(bin(a, q))
