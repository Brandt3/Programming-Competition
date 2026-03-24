# =============================================================================
# Problem 6 — "W"inning Sort
# W has 4 legs filled top-to-bottom in order: leg1, leg2, leg3, leg4
# Read back row-by-row bottom-to-top: leg1[r], leg2[r], leg3[r], leg4[r]
# Each group of 4 = one day's Pick-4 numbers
# =============================================================================

def solve_w_sort():
    numbers = list(map(int, input().split()))
    # 124 numbers -> 4 legs of 31 elements
    legs = [[None]*31 for _ in range(4)]
    fill_order = [0, 3, 1, 2]  # leg1, leg4, leg2, leg3 (same as M-sort)

    for idx, num in enumerate(numbers):
        leg = fill_order[idx % 4]
        row = idx // 4
        legs[leg][row] = num

    # Read bottom-to-top, left-to-right across legs
    output = []
    for row in range(30, -1, -1):
        for leg in range(4):
            output.append(legs[leg][row])

    for day in range(1, 32):
        base = (day-1)*4
        four = output[base:base+4]
        print(f"{day}: {four[0]} {four[1]} {four[2]} {four[3]}")
