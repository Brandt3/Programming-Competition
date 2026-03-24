# =============================================================================
# Problem 3 — Happy Hunting (greedy nearest-egg in 1D)
# =============================================================================

def solve_hunting():
    num_hunts = int(input())
    for case in range(1, num_hunts + 1):
        parts = list(map(int, input().split()))
        pos = parts[0]
        n   = parts[1]
        eggs = parts[2:2+n]

        order = []
        remaining = list(eggs)
        while remaining:
            # Find closest egg (ties broken by problem guarantee: "Two eggs will
            # never be the same distance away")
            closest = min(remaining, key=lambda e: abs(e - pos))
            order.append(closest)
            remaining.remove(closest)
            pos = closest

        print(f"Case {case}: {' '.join(map(str, order))}")

