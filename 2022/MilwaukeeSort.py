# =============================================================================
# Problem 4 — "M"ilwaukee Sort
# =============================================================================

def solve_milwaukee_sort():
    numbers = list(map(int, input().split()))
    # 124 numbers -> 4 legs of 31 elements each
    # Fill input left-to-right into legs top-to-bottom in repeating order:
    #   leg1, leg4, leg2, leg3
    # Then read out row-by-row bottom-to-top as: leg1[r], leg2[r], leg3[r], leg4[r]
    # Each group of 4 in the output = Pick-4 for one day of the month.

    # legs[0]=leg1, legs[1]=leg2, legs[2]=leg3, legs[3]=leg4
    legs = [[None] * 31 for _ in range(4)]
    fill_order = [0, 3, 1, 2]  # leg1, leg4, leg2, leg3

    for idx, num in enumerate(numbers):
        leg = fill_order[idx % 4]
        row = idx // 4
        legs[leg][row] = num

    # Read bottom-to-top (row 30 down to 0), leg order: 1, 2, 3, 4
    output = []
    for row in range(30, -1, -1):
        output.append(legs[0][row])  # leg1
        output.append(legs[1][row])  # leg2
        output.append(legs[2][row])  # leg3
        output.append(legs[3][row])  # leg4

    for day in range(1, 32):
        base = (day - 1) * 4
        four = output[base:base + 4]
        print(f"{day}: {four[0]} {four[1]} {four[2]} {four[3]}")


solve_milwaukee_sort()