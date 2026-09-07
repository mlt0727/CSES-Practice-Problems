# https://cses.fi/problemset/task/1646/

m, q = map(int, input().split())

prefix_sum = [0] * (m + 1)
nums = list(map(int, input().split()))
for i in range(1, m + 1):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

for _ in range(q):
    l, r = map(int, input().split())
    print(prefix_sum[r] - prefix_sum[l - 1])