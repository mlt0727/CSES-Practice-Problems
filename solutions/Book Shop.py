# https://cses.fi/problemset/task/1158/

n, x = map(int, input().split())
prices = list(map(int, input().split()))
pages = list(map(int, input().split()))

dp = [0] * (x + 1)
for price, page in zip(prices, pages):
    for c in range(x, price - 1, -1):
        dp[c] = max(dp[c], dp[c - price] + page)

print(dp[x])