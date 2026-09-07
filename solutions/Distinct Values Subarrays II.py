from collections import defaultdict

n, k = map(int, input().split())
nums = list(map(int, input().split()))

set = defaultdict(int)

l, r = 0, 0
ans = 0
while r < n:
    set[nums[r]] += 1
    while len(set) > k:
        set[nums[l]] -= 1
        if set[nums[l]] == 0:
            del set[nums[l]]
        l += 1
    ans += r - l + 1
    r += 1
print(ans)

