# =============================================================================
# Problem 5 — Combination Lock
# 40 positions (0-39), clockwise = increasing number
# Steps:
#   1. CW 2 full turns + continue CW to first number (c1)
#   2. CCW 1 full turn + continue CCW to second number (c2)
#   3. CW to third number (c3)
# Count total positions traversed (not counting start, counting each stop).
# =============================================================================
# Needs adjustment
def solve_lock():
    def cw_distance(start, target):
        """Clockwise distance from start to target on 40-position dial."""
        if target >= start:
            return target - start
        else:
            return 40 + target - start

    def ccw_distance(start, target):
        """Counter-clockwise distance from start to target."""
        if start >= target:
            return start - target
        else:
            return 40 + start - target

    n_cases = int(input())
    for _ in range(n_cases):
        parts = list(map(int, input().split()))
        start, c1, c2, c3 = parts

        # Validate
        if any(x < 0 or x > 39 for x in [start, c1, c2, c3]):
            print("Error")
            continue

        total = 120

        # Step 1: CW 2 full turns (80 positions) then CW to c1
        total += ccw_distance(start, c1)
        pos = c1

        # Step 2: CCW 1 full turn (40 positions) then CCW to c2
        total += cw_distance(pos, c2)
        pos = c2

        # Step 3: CW to c3
        dist = ccw_distance(pos, c3)
        # If dist is 0 we still go a full turn? No - just stop at c3.
        # But if c3 == c2 we'd traverse 0; the lock would still work.
        total += dist
        pos = c3

        print(total)

solve_lock()