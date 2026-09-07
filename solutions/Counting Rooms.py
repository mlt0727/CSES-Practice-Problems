# https://cses.fi/problemset/task/1192/
rows, cols = map(int, input().split())
grid = [list(input()) for _ in range(rows)]

ans = 0

for r in range(rows):
    for c in range(cols):

        if grid[r][c] == ".":
            ans += 1
            grid[r][c] = "#"

            stack = [(r, c)]

            while stack:
                x, y = stack.pop()

                if x > 0 and grid[x - 1][y] == ".":
                    grid[x - 1][y] = "#"
                    stack.append((x - 1, y))

                if x + 1 < rows and grid[x + 1][y] == ".":
                    grid[x + 1][y] = "#"
                    stack.append((x + 1, y))

                if y > 0 and grid[x][y - 1] == ".":
                    grid[x][y - 1] = "#"
                    stack.append((x, y - 1))

                if y + 1 < cols and grid[x][y + 1] == ".":
                    grid[x][y + 1] = "#"
                    stack.append((x, y + 1))

print(ans)