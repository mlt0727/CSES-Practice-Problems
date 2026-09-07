# https://cses.fi/problemset/task/1671/

from collections import defaultdict
import heapq

n, m = map(int, input().split())
adj = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))

dist = [float("inf")] * (n + 1)
dist[1] = 0

heap = [(0, 1)]

while heap:
    d, node = heapq.heappop(heap)
    if d > dist[node]:
        continue

    for neighbor, weight in adj[node]:
        new_dist = d + weight
        if new_dist < dist[neighbor]:
            dist[neighbor] = new_dist
            heapq.heappush(heap, (new_dist, neighbor))

print(*dist[1:])