# statistics_summary.py — mean, median, mode with tie handling
#
# The fiddly parts:
#   median: odd n → middle element. even n → average of two middle (may be float).
#   mode:   ties are common — problem WILL say what to do. Read carefully.
#           Options: report all, report smallest, report largest, report "no mode"
#
# TWEAK FOR output format:
#   f"{mean(data):.1f}"    → one decimal place
#   int(median(data))      → integer if problem guarantees odd count
#   mode(data)[0]          → smallest mode value
#   mode(data)[-1]         → largest mode value
#   mode(data) if len==1   → single mode only, else "No mode"

def mean(data):
    """Average. Returns float, or None if data is empty."""
    return sum(data) / len(data) if data else None

def median(data):
    """Middle value of sorted data. Returns int if odd count, float if even."""
    if not data: return None
    s = sorted(data)
    n = len(s)
    if n % 2 == 1:
        return s[n // 2]                       # odd: exact middle
    return (s[n//2 - 1] + s[n//2]) / 2        # even: average of two middles

def mode(data):
    """Returns sorted list of all most-frequent values (handles ties)."""
    if not data: return []
    freq = {}
    for x in data: freq[x] = freq.get(x, 0) + 1
    max_freq = max(freq.values())
    return sorted(k for k, v in freq.items() if v == max_freq)

def solve():
    n = int(input())
    data = [int(input()) for _ in range(n)]    # or: list(map(int, input().split()))
    m = mode(data)
    print(f"Mean:   {mean(data):.2f}")
    print(f"Median: {median(data)}")
    # Pick one of these based on what the problem says about ties:
    print(f"Mode:   {' '.join(map(str, m))}")  # all modes, space-separated
    # print(f"Mode: {m[0]}")                   # smallest only
    # print(f"Mode: {m[-1]}")                  # largest only
    # print(f"Mode: {m[0] if len(m)==1 else 'No mode'}")  # tie = no mode
