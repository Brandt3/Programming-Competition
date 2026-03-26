# matrix_transform.py — rotate, transpose, spiral traversal
#
# All functions return a NEW grid — original is not modified.
#
# ROTATION DIRECTION — read the problem carefully:
#   "rotate clockwise"         → rotate_90_cw
#   "rotate counter-clockwise" → rotate_90_ccw
#   "rotate 180°"              → rotate_180
#   Apply twice for 180°:      rotate_90_cw(rotate_90_cw(grid))  also works
#
# SPIRAL — uses 4 boundary pointers that shrink inward each layer.
#   Works for non-square grids and single row/column edge cases.

def rotate_90_cw(grid):
    """Rotate 90° clockwise: top→right, right→bottom, bottom→left, left→top."""
    n, m = len(grid), len(grid[0])
    return [[grid[n-1-r][c] for r in range(n)] for c in range(m)]

def rotate_90_ccw(grid):
    """Rotate 90° counter-clockwise."""
    n, m = len(grid), len(grid[0])
    return [[grid[r][m-1-c] for c in range(m)] for r in range(n)][::-1]

def rotate_180(grid):
    """Rotate 180°: reverse row order then reverse each row."""
    return [row[::-1] for row in reversed(grid)]

def transpose(grid):
    """Flip across main diagonal: new[c][r] = old[r][c]."""
    return [[grid[r][c] for r in range(len(grid))] for c in range(len(grid[0]))]

def spiral_order(grid):
    """Return all elements in clockwise spiral order (outside → inside)."""
    result = []
    top, bot = 0, len(grid)-1
    left, right = 0, len(grid[0])-1
    while top <= bot and left <= right:
        for c in range(left, right+1):           result.append(grid[top][c])  # →
        for r in range(top+1, bot+1):            result.append(grid[r][right]) # ↓
        if top < bot:
            for c in range(right-1, left-1, -1): result.append(grid[bot][c])  # ←
        if left < right:
            for r in range(bot-1, top, -1):      result.append(grid[r][left]) # ↑
        top+=1; bot-=1; left+=1; right-=1
    return result

def solve():
    rows, cols = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(rows)]
    # Uncomment whichever the problem asks:
    result = rotate_90_cw(grid)
    # result = rotate_90_ccw(grid)
    # result = rotate_180(grid)
    # result = transpose(grid)
    for row in result:
        print(' '.join(map(str, row)))
    # For spiral: print(' '.join(map(str, spiral_order(grid))))
