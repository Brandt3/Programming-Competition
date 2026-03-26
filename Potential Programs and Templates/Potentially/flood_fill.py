# flood_fill.py — island counting, largest region, flood fill
#
# All three use the same BFS core — just different things you track/do per cell.
#
# TWEAK FOR:
#   8-connected (diagonals): replace the 4-direction list with all 8 directions
#   Different cell value: change '1' to whatever the problem uses (e.g. '#', 1, True)
#   In-place visited marker: set grid[r][c]='0' instead of using visited array
#                            (saves memory, but modifies input)

from collections import deque

DIRS_4 = [(-1,0),(1,0),(0,-1),(0,1)]                    # up down left right
DIRS_8 = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]  # + diagonals

def bfs_region(grid, visited, sr, sc, target, dirs=DIRS_4):
    """BFS from (sr,sc). Returns list of all cells in the connected region."""
    rows, cols = len(grid), len(grid[0])
    cells = []
    queue = deque([(sr, sc)])
    visited[sr][sc] = True
    while queue:
        r, c = queue.popleft()
        cells.append((r, c))
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0<=nr<rows and 0<=nc<cols and not visited[nr][nc] and grid[nr][nc]==target:
                visited[nr][nc] = True
                queue.append((nr, nc))
    return cells

def count_islands(grid, target='1', dirs=DIRS_4):
    """Count connected regions of target value."""
    rows, cols = len(grid), len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == target and not visited[r][c]:
                bfs_region(grid, visited, r, c, target, dirs)
                count += 1
    return count

def largest_island(grid, target='1', dirs=DIRS_4):
    """Size of the largest connected region of target value."""
    rows, cols = len(grid), len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    best = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == target and not visited[r][c]:
                best = max(best, len(bfs_region(grid, visited, r, c, target, dirs)))
    return best

def flood_fill(grid, sr, sc, new_val, dirs=DIRS_4):
    """Replace all cells connected to (sr,sc) that match its value with new_val."""
    old_val = grid[sr][sc]
    if old_val == new_val: return
    rows, cols = len(grid), len(grid[0])
    queue = deque([(sr, sc)])
    grid[sr][sc] = new_val
    while queue:
        r, c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==old_val:
                grid[nr][nc] = new_val
                queue.append((nr, nc))

def solve():
    rows, cols = map(int, input().split())
    grid = [list(input().strip()) for _ in range(rows)]
    # Uncomment whichever the problem asks:
    print(count_islands(grid))          # number of islands
    # print(largest_island(grid))       # size of largest island
    # sr, sc = map(int, input().split())
    # flood_fill(grid, sr, sc, '2')     # fill from a point
    # for row in grid: print(''.join(row))
