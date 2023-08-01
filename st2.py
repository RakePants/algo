from math import gcd

def build(v:int, tl:int, tr:int, tree:[], a:[]):
    if tl == tr:
        tree[v] = a[tl]
        return
    tm = (tl + tr) >> 1
    build(v * 2, tl, tm, tree, a)
    build(v * 2 + 1, tm + 1, tr ,tree, a)
    tree[v] = gcd(tree[v * 2], tree[v * 2 + 1])
    
def get(v:int, tl:int, tr:int, l:int, r:int, tree:[]):
    if l > r:
        return 0
    if tl == l and tr == r:
        return tree[v]
    tm = (tl + tr) >> 1
    resLeft = get(v * 2, tl, tm, l, min(r, tm), tree)
    resRight = get(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, tree)
    return gcd(resLeft, resRight)
 
def update(v:int, tl:int, tr:int, pos:int, val:int, tree:[]):
    if tl == tr:
        tree[v] = val
        return
    tm = (tl + tr) >> 1
    if pos <= tm:
        update(v * 2, tl, tm, pos, val, tree)
    else:
        update(v * 2 + 1, tm + 1, tr, pos, val, tree)
    tree[v] = gcd(tree[v * 2], tree[v * 2 + 1])
 

N = 100000
tree = [0] * (4 * N)
n = int(input())
a = list(map(int, input().split()))
m = int(input())
build(1, 0, n - 1, tree, a)
for it in range(m):
    type, x, y = input().split()
    
    if type == 'u':
        x, y = int(x) - 1, int(y)
        update(1, 0, n - 1, x, y, tree)
    else:
        x, y = int(x) - 1, int(y) - 1
        print(get(1, 0, n - 1, x, y, tree))

'''
5
2 8 4 16 12
1
g 1 5
'''