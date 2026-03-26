# collatz_sequence.py — follow a rule until a condition, count steps
#
# CLASSIC COLLATZ:
#   if n is even: n = n // 2
#   if n is odd:  n = 3*n + 1
#   stop at 1
#
# GENERIC PATTERN: apply rule repeatedly until stop(n) is True.
#   Use this for any "follow the rule" problem — just swap in the rule.
#   Cycle detection included: returns -1 if the sequence revisits a value.
#
# CACHE: if the problem asks for many starting values, cache intermediate
#   results so you don't recompute the same suffixes repeatedly.

def collatz_steps(n):
    """Steps and full sequence for Collatz starting at n."""
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3*n + 1
        seq.append(n)
    return len(seq) - 1, seq

def follow_until(n, rule, stop, max_steps=100000):
    """
    Apply rule(n) repeatedly until stop(n) is True.
    Returns step count, or -1 if a cycle is detected or max_steps exceeded.
    """
    visited = {n}
    steps = 0
    while not stop(n):
        n = rule(n)
        steps += 1
        if steps > max_steps or n in visited:
            return -1               # cycle or runaway — adjust max_steps if needed
        visited.add(n)
    return steps

# Cached version for multiple queries on the same sequence family
_cache = {}
def collatz_steps_cached(n):
    if n in _cache: return _cache[n]
    if n == 1:
        _cache[1] = 0
        return 0
    if n % 2 == 0: result = 1 + collatz_steps_cached(n // 2)
    else:          result = 1 + collatz_steps_cached(3*n + 1)
    _cache[n] = result
    return result

def solve():
    n = int(input())
    for i in range(1, n + 1):
        start = int(input())
        steps, seq = collatz_steps(start)
        print(f"Case {i}: {steps} steps")
        # print(f"Case {i}: {' '.join(map(str, seq))}")  # full sequence
