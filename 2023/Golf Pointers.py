# =============================================================================
# Problem 2 — Golf Pointers
# =============================================================================

def solve_golf():
    # 64 compass points, each 5.625 degrees apart, starting at N=0 going clockwise
    # Listed from N clockwise to complete circle:
    compass_64 = [
        "N", "NtE", "NNE", "NNEtE", "NEbN", "NEtN", "NE", "NEtE",
        "NEbE", "ENEtN", "ENE", "ENEtE", "EbN", "EtN", "E", "EtS",
        "EbS", "ESEtN", "ESE", "ESEtS", "SEbE", "SEtE", "SE", "SEtS",
        "SEbS", "SSEtE", "SSE", "SSEtS", "SbE", "StE", "S", "StW",
        "SbW", "SSWtW", "SSW", "SSWtS", "SWbS", "SWtS", "SW", "SWtW",
        "SWbW", "WSWtS", "WSW", "WSWtW", "WbS", "WtS", "W", "WtN",
        "WbN", "WNWtS", "WNW", "WNWtN", "NWbW", "NWtW", "NW", "NWtN",
        "NWbN", "NNWtW", "NNW", "NNWtN", "NbW", "NtW", "N_dup", "N_dup2"
    ]

    # Actually let's build the 64 points properly from the problem description.
    # The 32-point compass (from problem): N, NbE, NNE, NEbN, NE, NEbE, ENE, EbN,
    # E, EbS, ESE, SEbE, SE, SEbS, SSE, SbE, S, SbW, SSW, SWbS, SW, SWbW,
    # WSW, WbS, W, WbN, WNW, NWbW, NW, NWbN, NNW, NbW
    # These are 32 points = 11.25 deg apart.
    # Then 32 more "XtY" points inserted between each pair: 64 total = 5.625 deg apart.
    # From N to E clockwise the 64 points are:
    # N, NtE, NbE, NNEtN, NNE, NNEtE, NEbN, NEtN, NE, NEtE, NEbE, ENEtN,
    # ENE, ENEtE, EbN, EtN, E
    # Wait - the problem explicitly lists them:
    # "From N to E in the clockwise direction the compass points are:
    #  N, NtE, NbE, NNEtN, NNE, NNEtE, NEbN, NEtN, NE, NEtE, NEbE, ENEtN, ENE, ENEtE, EbN, EtN, E"
    # That's 17 points from N to E inclusive = 16 steps * 5.625 = 90 degrees. ✓

    # Build full 64-point list by going around all 8 octants clockwise
    # Each octant has 8 points (N->NE, NE->E, E->SE, SE->S, S->SW, SW->W, W->NW, NW->N)
    # The problem gives N->E as:
    # N, NtE, NbE, NNEtN, NNE, NNEtE, NEbN, NEtN, NE, NEtE, NEbE, ENEtN, ENE, ENEtE, EbN, EtN, E
    # Let's just hardcode all 64 in order (clockwise from N):

    points = [
        # N to NE (indices 0-8)
        "N", "NtE", "NbE", "NNEtN", "NNE", "NNEtE", "NEbN", "NEtN",
        # NE to E (indices 8-16)
        "NE", "NEtE", "NEbE", "ENEtN", "ENE", "ENEtE", "EbN", "EtN",
        # E to SE (indices 16-24)
        "E", "EtS", "EbS", "ESEtE", "ESE", "ESEtS", "SEbE", "SEtE",
        # SE to S (indices 24-32)
        "SE", "SEtS", "SEbS", "SSEtE", "SSE", "SSEtS", "SbE", "StE",
        # S to SW (indices 32-40)
        "S", "StW", "SbW", "SSWtS", "SSW", "SSWtW", "SWbS", "SWtS",
        # SW to W (indices 40-48)
        "SW", "SWtW", "SWbW", "WSWtS", "WSW", "WSWtW", "WbS", "WtS",
        # W to NW (indices 48-56)
        "W", "WtN", "WbN", "WNWtW", "WNW", "WNWtN", "NWbW", "NWtW",
        # NW to N (indices 56-63)
        "NW", "NWtN", "NWbN", "NNWtW", "NNW", "NNWtN", "NbW", "NtW",
    ]
    # Total = 64 points

    n = int(input())
    for i in range(1, n + 1):
        line = input().split()
        degrees = int(line[0])
        direction = line[4]  # "left" or "right"

        # N = 0 degrees (index 0). Each step = 5.625 degrees.
        # Right = clockwise (increasing index), Left = counter-clockwise (decreasing index)
        if direction == "right":
            angle = degrees
        else:
            angle = -degrees  # left = counter-clockwise = negative

        # Find closest point: divide by 5.625 and round to nearest integer
        step = angle / 5.625
        idx = round(step) % 64
        print(f"Case {i}: {points[idx]}")

