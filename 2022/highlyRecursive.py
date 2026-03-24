# =============================================================================
# Problem 2 — Highly Recursive Function
# =============================================================================

def solve_recursive():
    _cache = {}
    def H(n):
        if n in _cache:
            return _cache[n]
        if n < -5:
            result = H(n + 4) + H(n + 2)
        elif -5 <= n < 2:
            result = n * 2
        else:  # n >= 2
            result = H(n - 8) - H(n - 4) + H(n - 3)
        _cache[n] = result
        return result
 
    count = int(input())
    for i in range(1, count + 1):
        n = int(input())
        print(f"Case {i}: H({n}) = {H(n)}")

solve_recursive()