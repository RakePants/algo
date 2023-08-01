import heapq as hq


def dj(s:int, dist:[], edges:[[]]):
    dist[s] = 0
    heap = []
    hq.heappush(heap, [dist[s], s])
    route = []
    while heap:
        begin = hq.heappop(heap)
        v = begin[1]
        route.append(v)
        if dist[v] < begin[0]:
            continue
        for i in range(len(edges[v])):
            to = edges[v][i][0]
            w = edges[v][i][1]
            if dist[to] > dist[v] + w:
                dist[to] = dist[v] + w
                hq.heappush(heap, (dist[to], to))
    return route[:-1]
                

n, s, f = map(int, input().split())
edges = [[] for i in range(n + 1)]
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j] != -1:
            edges[i + 1].append([j + 1, a[j]])
inf = 10 ** 9
dist = [inf] * (n + 1)
route = dj(s, dist, edges)
if dist[f] == inf or not route:
    print('-1')
else:
    print(*route)