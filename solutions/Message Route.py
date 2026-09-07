# https://cses.fi/problemset/task/1667/

from collections import defaultdict, deque

n, m = map(int, input().split())
adj = defaultdict(list)
for _ in range(m):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)

q = deque()
visited = set()
q.append(1)
visited.add(1)

parent = {1: None}

while q:
    node = q.popleft()

    for neighbor in adj[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            q.append(neighbor)
            parent[neighbor] = node

if n not in parent:
    print("IMPOSSIBLE")
else:
    ans = []
    while n is not None:
        ans.append(n)
        n = parent[n]
    print(len(ans))
    print(*ans[::-1])