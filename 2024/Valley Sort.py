# =============================================================================
# Problem 6 — Valley Sort
# First half descending, second half ascending (valley shape)
# =============================================================================

def solve_valley_sort():
    n = int(input())
    values = [int(input()) for _ in range(n)]

    sorted_vals = sorted(values, reverse=True)  # largest to smallest

    # Interleave: place in positions 0, n-1, 1, n-2, 2, n-3, ...
    # This gives descending first half, ascending second half
    result = [0] * n
    left = 0
    right = n - 1
    for i, val in enumerate(sorted_vals):
        if i % 2 == 0:
            result[left] = val
            left += 1
        else:
            result[right] = val
            right -= 1
    print("\n",n)
    for v in result:
        print(v)

solve_valley_sort()