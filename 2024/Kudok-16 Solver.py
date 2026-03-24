# =============================================================================
# Problem 2 — Kudok-16 Solver
# =============================================================================
#Needs testing
def solve_kudok():
    num_puzzles = int(input())
    for _ in range(num_puzzles):
        col_sums = list(map(int, input().split()))  # 4 column sums
        grid = []
        row_sums = []
        for _ in range(4):
            parts = input().split()
            row_sums.append(int(parts[0]))
            row = [None if x == '?' else int(x) for x in parts[1:]]
            grid.append(row)

        # Collect which numbers are already placed
        used = set()
        blanks = []  # (row, col) positions that are '?'
        for r in range(4):
            for c in range(4):
                if grid[r][c] is not None:
                    used.add(grid[r][c])
                else:
                    blanks.append((r, c))

        available = [x for x in range(1, 17) if x not in used]

        # Backtracking solver
        def is_valid():
            # Check partial row/col constraints
            for r in range(4):
                row_vals = [grid[r][c] for c in range(4) if grid[r][c] is not None]
                if len(set(row_vals)) != len(row_vals):
                    return False
                if len(row_vals) == 4 and sum(row_vals) != row_sums[r]:
                    return False
                if sum(row_vals) > row_sums[r]:
                    return False
            for c in range(4):
                col_vals = [grid[r][c] for r in range(4) if grid[r][c] is not None]
                if len(set(col_vals)) != len(col_vals):
                    return False
                if len(col_vals) == 4 and sum(col_vals) != col_sums[c]:
                    return False
                if sum(col_vals) > col_sums[c]:
                    return False
            return True

        def solve(idx, avail):
            if idx == len(blanks):
                return is_valid()
            r, c = blanks[idx]
            for i, val in enumerate(avail):
                grid[r][c] = val
                rest = avail[:i] + avail[i+1:]
                if is_valid():
                    if solve(idx + 1, rest):
                        return True
            grid[r][c] = None
            return False

        solve(0, available)

        # Print solution
        print(f"   {' '.join(map(str, col_sums))}")
        for r in range(4):
            row_str = ' '.join(str(grid[r][c]) for c in range(4))
            print(f"{row_sums[r]} {row_str}")
        print()

solve_kudok()