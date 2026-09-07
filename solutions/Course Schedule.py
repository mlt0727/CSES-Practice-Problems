# https://cses.fi/problemset/task/1679/

from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
adj = defaultdict(list)
for _ in range(m):
    n1, n2 = map(int, input().split())
    adj[n1 - 1].append(n2 - 1)

ways = set()
visited = set()
ans = []
def dfs(node):
    if node in ways:
        return False
    if node in visited:
        return True
    visited.add(node)
    ways.add(node)
    for neighbor in adj[node]:
        if not dfs(neighbor):
            return False
    ways.remove(node)
    ans.append(node + 1)
    return True

for i in range(n):
    if not dfs(i):
        print("IMPOSSIBLE")
        break
else:
    print(*ans[::-1])