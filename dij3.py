import heapq as hq


def dj(s:int, dist:[], edges:[[]]):
    dist[s] = 0
    heap = []
    hq.heappush(heap, [dist[s], s])
    while heap:
        begin = hq.heappop(heap)
        v = begin[1]
        if dist[v] < begin[0]:
            continue
        for i in range(len(edges[v])):
            to = edges[v][i][0]
            w = edges[v][i][1]
            if dist[to] > dist[v] + w:
                dist[to] = dist[v] + w
                hq.heappush(heap, (dist[to], to))
    
    
n, m, s = map(int, input().split())
edges = [[] for i in range(n)]
for i in range(m):
    a = list(map(int, input().split()))
    edges[a[0]].append([a[1], a[2]])
    edges[a[1]].append([a[0], a[2]])
inf = 10 ** 9
dist = [inf] * n
dj(s, dist, edges)
for i in range(n):
    if i == s:
        print(0, end=' ')
    elif dist[i] == inf:
        print(2009000999, end=' ')
    else:
        print(dist[i], end=' ')