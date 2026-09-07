# https://cses.fi/problemset/task/1675/

n, m = map(int, input().split())

edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

parent = list(range(n + 1))
size = [1] * (n + 1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False

    if size[x] < size[y]:
        x, y = y, x

    parent[y] = x
    size[x] += size[y]
    return True

cost = 0
count = 0

for c, a, b in edges:
    if union(a, b):
        cost += c
        count += 1

        if count == n - 1:
            print(cost)
            break
else:
    print("IMPOSSIBLE")