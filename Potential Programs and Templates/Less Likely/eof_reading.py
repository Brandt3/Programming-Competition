# eof_reading.py — input patterns when no count is given
#
# USE WHEN: problem says "read until end of input" instead of giving N.
#
# PATTERN 1 — try/except (most reliable)
import sys

def read_all_lines():
    lines = []
    try:
        while True:
            lines.append(input())
    except EOFError:
        pass
    return lines

# PATTERN 2 — sys.stdin (cleaner, reads everything at once)
def read_all_lines_stdin():
    return [line.rstrip('\n') for line in sys.stdin]

# PATTERN 3 — blank line as section terminator (not true EOF)
def read_sections():
    """Read groups of lines separated by blank lines."""
    groups = []
    current = []
    try:
        while True:
            line = input()
            if line.strip():
                current.append(line)
            else:
                if current:
                    groups.append(current)
                    current = []
    except EOFError:
        if current:
            groups.append(current)
    return groups

# PATTERN 4 — read space-separated values across all lines
def read_all_ints():
    nums = []
    try:
        while True:
            nums.extend(map(int, input().split()))
    except EOFError:
        pass
    return nums

# PATTERN 5 — read pairs until a sentinel value
def read_until_sentinel(sentinel="0 0"):
    pairs = []
    while True:
        line = input().strip()
        if line == sentinel:
            break
        pairs.append(list(map(int, line.split())))
    return pairs

# USAGE: replace the solve() body with whichever pattern fits
def solve():
    lines = read_all_lines()
    for line in lines:
        print(line)         # replace with real logic
