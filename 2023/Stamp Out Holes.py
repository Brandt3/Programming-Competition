# =============================================================================
# Problem 5 — Stamp Out Holes
# =============================================================================

def solve_stamps():
    forever_val = int(input())
    tokens = input().split()

    stamp_values = []
    for t in tokens:
        if t == 'F':
            stamp_values.append(forever_val)
        else:
            stamp_values.append(int(t))

    total = sum(stamp_values)

    # Find all amounts from 1 to total-1 that CANNOT be made
    # Each physical stamp can only be used once -> 0/1 knapsack reachability
    dp = [False] * (total + 1)
    dp[0] = True

    for s in stamp_values:
        for amount in range(total, s - 1, -1):
            if dp[amount - s]:
                dp[amount] = True

    holes = [a for a in range(1, total) if not dp[a]]
    print(f"The number of amounts between 0 and {total} that cannot be made exactly is {len(holes)}.")
    print("The amounts that cannot be made exactly are:")
    for h in holes:
        print(h)

