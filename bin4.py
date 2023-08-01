n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

def bin(a, k):
    l = 0
    r = 10 ** 8
    
    while (r - l) >= 10 ** (-6):
        mid = (l + r) / 2

        if sum(int((x + 0.0) / mid) for x in a) < k:
            r = mid
        else:
            l = mid

    return l

print(bin(a, k))
