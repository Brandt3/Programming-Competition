# 2023 Problem 5 — Stamp Out Holes
# Find all amounts 1..total-1 that CANNOT be made using the stamps.
# Each physical stamp used at most once → 0/1 knapsack (inner loop BACKWARDS).
# 'F' tokens = Forever stamp = use the given forever value.

forever_val = int(input())
tokens = input().split()
stamps = [forever_val if t == 'F' else int(t) for t in tokens]
total = sum(stamps)

dp = [False] * (total + 1)
dp[0] = True
for s in stamps:
    for amt in range(total, s - 1, -1):
        if dp[amt - s]: dp[amt] = True

holes = [a for a in range(1, total) if not dp[a]]
print(f"The number of amounts between 0 and {total} that cannot be made exactly is {len(holes)}.")
print("The amounts that cannot be made exactly are:")
for h in holes: print(h)
