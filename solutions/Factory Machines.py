# https://cses.fi/problemset/task/1620/

n, t = map(int, input().split())
machines = list(map(int, input().split()))
l, r = 1, max(machines) * t
while l < r:
    m = (l + r) // 2
    if sum(m // machine for machine in machines) >= t:
        r = m
    else:
        l = m + 1
print(l)