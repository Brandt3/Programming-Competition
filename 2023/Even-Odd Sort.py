# =============================================================================
# Problem 3 — Even-Odd Sort
# =============================================================================

def solve_even_odd_sort():
    n = int(input())
    values = [int(input()) for _ in range(n)]

    # Separate indices by parity of VALUE (not index)
    even_indices = [i for i, v in enumerate(values) if v % 2 == 0]
    odd_indices  = [i for i, v in enumerate(values) if v % 2 != 0]

    even_vals = sorted([values[i] for i in even_indices])           # ascending
    odd_vals  = sorted([values[i] for i in odd_indices], reverse=True)  # descending

    result = list(values)
    for i, idx in enumerate(even_indices):
        result[idx] = even_vals[i]
    for i, idx in enumerate(odd_indices):
        result[idx] = odd_vals[i]
    print("\n")
    for v in result:
        print(v)

solve_even_odd_sort()