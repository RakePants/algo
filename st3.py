def build(v:int, tl:int, tr:int, tree:[], a:[]):
    if tr == tl:
        tree[v] = a[tl]
        return
    tm = (tl + tr) >> 1
    build(v * 2 + 1, tl, tm, tree, a)
    build(v * 2 + 2, tm + 1, tr, tree, a)
    tree[v] = max(tree[v * 2 + 1], tree[v * 2 + 2])
    
def get(v:int, tl:int, tr:int, l:int, tree:[], x):
    if tree[v] < x:
        return -1
    if tr < l:
        return -1
    if tr == tl:
        return tl
    tm = (tl + tr) >> 1
    res = get(v * 2 + 1, tl, tm, l, tree, x)
    if res == -1:
        res = get(v * 2 + 2, tm + 1, tr, l, tree, x)
    return res

 
def update(v:int, tl:int, tr:int, pos:int, val:int, tree:[]):
    if tr == tl:
        tree[v] = val
        return 
    tm = (tl + tr) >> 1
    if pos <= tm:
        update(v * 2 + 1, tl, tm, pos, val, tree)
    else:
        update(v * 2 + 2, tm + 1, tr, pos, val, tree)
    tree[v] = max(tree[v * 2 + 1], tree[v * 2 + 2])
 
def solve():
    
    N = 100000
    tree = [0] * (4 * N)
    
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    build(0, 0, n - 1, tree, a)
    for it in range(m):
        type, x, y = map(int, input().split())
        if type == 1:
            update(0, 0, n - 1, x, y, tree)
        else:
            print(get(0, 0, n - 1, y, tree, x))


def main():
    #t = int(input())
    #for i in range(t):
    #  solve()
    solve()
if __name__ == '__main__':
  main()