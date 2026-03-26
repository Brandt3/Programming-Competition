# 2023 Problem 2 — Golf Pointers
# Convert an angle (0-90°, left or right) to the nearest of 64 compass points.
# 64 points spaced 5.625° apart clockwise from N.
# Right = clockwise (+), Left = counter-clockwise (-). Round to nearest index.

POINTS = [
    "N","NtE","NbE","NNEtN","NNE","NNEtE","NEbN","NEtN",
    "NE","NEtE","NEbE","ENEtN","ENE","ENEtE","EbN","EtN",
    "E","EtS","EbS","ESEtE","ESE","ESEtS","SEbE","SEtE",
    "SE","SEtS","SEbS","SSEtE","SSE","SSEtS","SbE","StE",
    "S","StW","SbW","SSWtS","SSW","SSWtW","SWbS","SWtS",
    "SW","SWtW","SWbW","WSWtS","WSW","WSWtW","WbS","WtS",
    "W","WtN","WbN","WNWtW","WNW","WNWtN","NWbW","NWtW",
    "NW","NWtN","NWbN","NNWtW","NNW","NNWtN","NbW","NtW",
]

n = int(input())
for i in range(1, n + 1):
    parts = input().split()
    degrees = int(parts[0])
    direction = parts[4]
    angle = degrees if direction == "right" else -degrees
    idx = round(angle / 5.625) % 64
    print(f"Case {i}: {POINTS[idx]}")
