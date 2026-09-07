# Reference solution notes

Attempt the problems independently before reading these notes or the linked code. These notes explain all 10 Python implementations in this repository. They follow the problem order in the preparation PDF. Complexity estimates describe the code as written and assume average constant-time dictionary and set operations.


- [Counting Rooms](#counting-rooms)
- [Factory Machines](#factory-machines)
- [Book Shop](#book-shop)
- [Static Range Sum Queries](#static-range-sum-queries)
- [Course Schedule](#course-schedule)
- [Message Route](#message-route)
- [Counting Divisors](#counting-divisors)
- [Shortest Routes I](#shortest-routes-i)
- [Distinct Values Subarrays II](#distinct-values-subarrays-ii)
- [Road Reparation](#road-reparation)

## Counting Rooms

[Problem](https://cses.fi/problemset/task/1192/) | [Python code](solutions/Counting%20Rooms.py)

Each room is a connected component of floor cells (`.`), connected horizontally or vertically.

1. Scan every cell. When an unvisited floor cell is found, count one new room.
2. Mark that cell as visited by changing it to `#`, and push it onto a stack.
3. Pop a cell and examine its four neighbors. Mark and push each unvisited floor neighbor.
4. When the stack is empty, every cell in that room has been visited. Continue scanning for the next room.

Marking cells when they are pushed prevents duplicate visits. The explicit stack implements depth-first search without recursive calls. Every floor cell reachable from the starting cell is visited, so the scan counts each room exactly once.

For a grid with `rows * cols` cells, time is `O(rows * cols)` and worst-case space is `O(rows * cols)`, including the grid and stack.

## Factory Machines

[Problem](https://cses.fi/problemset/task/1620/) | [Python code](solutions/Factory%20Machines.py)

Use binary search on the time needed to produce at least `t` products.

1. In `m` units of time, a machine taking `machine` units per product makes `m // machine` products. Sum this across all machines.
2. If the total is at least `t`, keep `m` as a possible answer and search earlier times with `r = m`.
3. Otherwise, discard `m` and all earlier times with `l = m + 1`.

Production never decreases as time increases, so this feasibility check is monotonic. When the bounds meet, they identify the earliest feasible time. The code uses `max(machines) * t` as a valid upper bound: even the slowest machine could meet the target alone by then.

**Complexity:** `O(n log U)` time, where `U = max(machines) * t`, and `O(n)` total space for the machine times.

## Book Shop

[Problem](https://cses.fi/problemset/task/1158/) | [Python code](solutions/Book%20Shop.py)

Use one-dimensional dynamic programming for 0/1 knapsack. `dp[c]` stores the most pages obtainable with a budget of at most `c` using the books processed so far.

For each `(price, page)` pair, update `dp[c]` to the better of skipping the book (`dp[c]`) or buying it (`dp[c - price] + page`). Visit budgets from `x` down to `price`.

The descending order is essential: `dp[c - price]` still represents the previous set of books, so the current book is used at most once. An ascending loop could reuse the same book repeatedly. After all books, `dp[x]` is the answer.

**Complexity:** `O(n * x)` time and `O(n + x)` total space, including the price and page arrays; the DP array itself uses `O(x)` space.

## Static Range Sum Queries

[Problem](https://cses.fi/problemset/task/1646/) | [Python code](solutions/Static%20Range%20Sum%20Queries.py)

Precompute prefix sums so each range query needs one subtraction. The code calls the array length `m` and the number of queries `q`.

Set `prefix_sum[0] = 0`. For each position `i`, add the next array value to obtain the sum of the first `i` elements. A query uses one-based, inclusive endpoints `l` and `r`, so its answer is:

```python
prefix_sum[r] - prefix_sum[l - 1]
```

Subtracting the sum before `l` from the sum through `r` leaves exactly the requested range. The leading zero also handles queries starting at position 1 without a special case. This works because the array does not change between queries.

**Complexity:** `O(m + q)` total time, `O(1)` per query after preprocessing, and `O(m)` space.

## Course Schedule

[Problem](https://cses.fi/problemset/task/1679/) | [Python code](solutions/Course%20Schedule.py)

Use recursive DFS to detect directed cycles and build a topological ordering. The code stores course numbers as zero-based indices internally.

- `ways` contains the nodes on the current recursion path. Reaching one again reveals a directed cycle, so the program prints `IMPOSSIBLE`.
- `visited` records nodes already entered. A visited node outside `ways` has finished its DFS and does not need to be processed again.
- After all outgoing neighbors finish, remove the current node from `ways` and append it to `ans`.

The cycle check comes before the visited check so an active node is not mistaken for a finished node. For an edge `a -> b`, DFS finishes `b` before appending `a`, unless `b` was already finished. Reversing the finishing order therefore places each prerequisite before the course that depends on it. Starting DFS from every course also covers disconnected parts of the graph.

**Complexity:** `O(n + m)` time and space, including up to `O(n)` recursive calls. The code raises Python's recursion limit to accommodate deep traversals; recursion still consumes memory.

## Message Route

[Problem](https://cses.fi/problemset/task/1667/) | [Python code](solutions/Message%20Route.py)

Use BFS to find a shortest route from computer 1 to computer `n` in the undirected, unweighted graph.

Start a queue with computer 1. When discovering an unvisited neighbor, mark it visited, add it to the queue, and record the current node as its parent. Marking on discovery prevents duplicate queue entries.

BFS explores nodes in increasing distance from the start, so a node's first recorded parent belongs to a shortest route. If `n` is absent from `parent`, print `IMPOSSIBLE`. Otherwise, follow parent links backward from `n` to `None`, then reverse the collected list. The printed length counts computers in the route, not edges. The implementation finishes the full reachable BFS before reconstructing the route.

**Complexity:** `O(n + m)` time and space, including the adjacency lists, queue, visited set, parent mapping, and reconstructed route.

## Counting Divisors

[Problem](https://cses.fi/problemset/task/1713/) | [Python code](solutions/Counting%20Divisors.py)

Factor each query value into primes. If `x = p1^a1 * p2^a2 * ...`, every divisor chooses an exponent from `0` through `ai` for each prime. The total number of divisors is therefore `(a1 + 1) * (a2 + 1) * ...`.

The code first generates primes up to 1000 by trial division. This covers the square root of the maximum query value, `10^6`, in the linked problem. For each query, divide out each prime repeatedly, count its exponent, and multiply the answer by one more than that exponent.

Stop when `p * p > x`, using the remaining, reduced value of `x`. Any remaining value greater than 1 must then be prime and contributes a factor of 2. For `x = 1`, the answer stays 1.

**Complexity:** Let `M` be the largest permitted value and `P` the number of primes up to `sqrt(M)`. Each query uses `O(P + log M)` time as a safe upper bound, and the stored prime list uses `O(P)` space. Here the prime-generation bound is fixed at 1000, and queries are processed one at a time.

## Shortest Routes I

[Problem](https://cses.fi/problemset/task/1671/) | [Python code](solutions/Shortest%20Routes%20I.py)

Use Dijkstra's algorithm on the directed graph. The linked problem has positive edge weights and guarantees that every city is reachable from city 1.

Initialize `dist[1] = 0` and all other distances to infinity. A min-heap stores `(distance, node)` candidates. Pop the smallest candidate, then try extending its route along every outgoing edge. If a new route improves a neighbor's distance, update `dist` and push the new candidate.

The heap can contain older candidates for the same city. Skip a popped entry when `d > dist[node]`, because a better route has already been found. With nonnegative weights, the smallest current distance cannot be improved by going through a later, more distant node. Finally, print the distances for cities 1 through `n`.

**Complexity:** `O(n + m log(m + 1))` time and `O(n + m)` space for this heap implementation. The heap may retain `O(m)` candidates, including outdated entries.

## Distinct Values Subarrays II

[Problem](https://cses.fi/problemset/task/2428/) | [Python code](solutions/Distinct%20Values%20Subarrays%20II.py)

Count contiguous subarrays containing at most `k` distinct values using a sliding window.

1. Extend the right end of the window and increment that value's frequency.
2. While the window contains more than `k` distinct values, move the left end forward, decreasing frequencies and removing zero-count entries.
3. Once the window is valid, add `r - l + 1` to the answer. These are exactly the valid subarrays ending at index `r`, with starting positions from `l` through `r`.
4. Repeat for each right endpoint.

Removing elements cannot increase the number of distinct values, so every suffix of the valid window is valid. Starting before `l` would include a window already rejected for having too many distinct values. Each subarray is counted once, at its right endpoint.

Both pointers move forward at most `n` times. With average constant-time dictionary operations, time is `O(n)`. The frequency dictionary uses `O(min(n, k + 1))` space, and the full program uses `O(n)` space because it stores the input array.

The existing code names its frequency dictionary `set`; it is a `defaultdict(int)`, not a Python set.

## Road Reparation

[Problem](https://cses.fi/problemset/task/1675/) | [Python code](solutions/Road%20Reparation.py)

Use Kruskal's algorithm to build a minimum spanning tree.

1. Store each road as `(cost, a, b)` and sort the roads by cost.
2. Use a disjoint-set union structure (DSU) to track which cities are already connected. `find` applies path compression, and `union` attaches the smaller component to the larger one.
3. Accept a road only when it connects different components. Add its cost and increment the number of accepted roads.
4. Once `n - 1` roads are accepted, print the total cost. If the roads run out first, print `IMPOSSIBLE`.

Adding an edge within a component would create a cycle. Among edges joining different components, the cheapest available edge is safe to include in a minimum spanning tree. Repeating this choice connects all cities at minimum total cost whenever the graph is connected.

**Complexity:** `O(n + m log m + m * alpha(n))` time and `O(n + m)` space. Sorting dominates the edge processing; `alpha(n)` is the inverse Ackermann function and grows extremely slowly.
