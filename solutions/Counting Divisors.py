# https://cses.fi/problemset/task/1713/

primes = []

for x in range(2, 1001):
    for p in primes:
        if p * p > x:
            primes.append(x)
            break
        if x % p == 0:
            break
    else:
        primes.append(x)

n = int(input())

for _ in range(n):
    x = int(input())

    ans = 1

    for p in primes:
        if p * p > x:
            break

        count = 0
        while x % p == 0:
            x //= p
            count += 1

        ans *= (count + 1)

    if x > 1:
        ans *= 2

    print(ans)
