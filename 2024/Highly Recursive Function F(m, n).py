# =============================================================================
# Problem 8 — Highly Recursive Function F(m, n)
# =============================================================================
 
def solve_recursive_fmn():
    _cache = {}
    def F(m, n):
        if (m, n) in _cache:
            return _cache[(m, n)]
        if n <= 10:
            result = m + n
        elif m >= n:  # m >= n and n > 10
            result = 10
        else:          # m < n and n > 10
            result = F(m+1, n-2) + F(m+3, n) - F(m+4, n-1)
        _cache[(m, n)] = result
        return result
 
    count = int(input())
    for i in range(1, count + 1):
        m, n = map(int, input().split())
        print(f"Case {i}: F({m},{n}) = {F(m, n)}")
 

