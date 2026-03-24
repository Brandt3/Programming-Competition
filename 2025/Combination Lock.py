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
        return (target - start) % 40

    def ccw_distance(start, target):
        """Counter-clockwise distance from start to target."""
        return (start - target) % 40

    n_cases = int(input())
    for _ in range(n_cases):
        parts = list(map(int, input().split()))
        start, c1, c2, c3 = parts

        # Validate
        if any(x < 0 or x > 39 for x in [start, c1, c2, c3]):
            print("Error")
            continue

        total = 0

        # Step 1: CW 2 full turns (80 positions) then CW to c1
        total += 80 + cw_distance(start, c1)
        pos = c1

        # Step 2: CCW 1 full turn (40 positions) then CCW to c2
        total += 40 + ccw_distance(pos, c2)
        pos = c2

        # Step 3: CW to c3
        dist = cw_distance(pos, c3)
        # If dist is 0 we still go a full turn? No - just stop at c3.
        # But if c3 == c2 we'd traverse 0; the lock would still work.
        total += dist if dist > 0 else 40
        pos = c3

        print(total)

solve_lock()