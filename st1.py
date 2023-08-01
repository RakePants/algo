def combine(a, b):
    if a[0] < b[0]:
        return a
    if b[0] < a[0]:
        return b
    return [a[0], a[1] + b[1]]

def build(v:int, tl:int, tr:int, tree:[], a:[]):
    if tl == tr:
        tree[v] = [a[tl], 1]
        return
    tm = (tl + tr) >> 1
    build(v * 2, tl, tm, tree, a)
    build(v * 2 + 1, tm + 1, tr ,tree, a)
    tree[v] = combine(tree[v * 2], tree[v * 2 + 1])
    
def get(v:int, tl:int, tr:int, l:int, r:int, tree:[]):
    if l > r:
        INF = 1000000000
        return (INF, 0)
    if tl == l and tr == r:
        return tree[v]
    tm = (tl + tr) >> 1
    return combine(get(v * 2, tl, tm, l, min(r, tm), tree), get(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, tree))

 
def update(v:int, tl:int, tr:int, pos:int, val:int, tree:[]):
    if tl == tr:
        tree[v] = [val, 1]
    else:
        tm = (tl + tr) >> 1
        if pos <= tm:
            update(v * 2, tl, tm, pos, val, tree)
        else:
            update(v * 2 + 1, tm + 1, tr, pos, val, tree)
        tree[v] = combine(tree[v * 2], tree[v * 2 + 1])
 

N = 100000
tree = [0, 0] * (4 * N)
n, m = map(int, input().split())
a = list(map(int, input().split()))
build(1, 0, n - 1, tree, a)
for it in range(m):
    type, x, y = map(int, input().split())
    if type == 1:
        update(1, 0, n - 1, x, y, tree)
    else:
        a, b = get(1, 0, n - 1, x, y - 1, tree)
        print(a, b)
