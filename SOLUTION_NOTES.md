# Reference solution notes

Attempt the problems independently before reading these notes or the linked code. These explanations describe the two existing Python implementations; the other eight files remain empty placeholders.

## Counting Rooms

[Problem](https://cses.fi/problemset/task/1192/) | [Python code](solutions/Counting%20Rooms.py)

Each room is a connected component of floor cells (`.`), connected horizontally or vertically.

1. Scan every cell. When an unvisited floor cell is found, count one new room.
2. Mark that cell as visited by changing it to `#`, and push it onto a stack.
3. Pop a cell and examine its four neighbors. Mark and push each unvisited floor neighbor.
4. When the stack is empty, every cell in that room has been visited. Continue scanning for the next room.

Marking cells when they are pushed prevents duplicate visits. The explicit stack implements depth-first search without recursive calls. Every floor cell reachable from the starting cell is visited, so the scan counts each room exactly once.

For a grid with `rows * cols` cells, time is `O(rows * cols)` and worst-case space is `O(rows * cols)`, including the grid and stack.

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
