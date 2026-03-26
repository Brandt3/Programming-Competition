# 2023 Problem 6 — Highly Recursive Function F(n)
# F(n) = F(n+15) + F(n+10) - F(n+5)   for n < -20
# F(n) = n * 3                          for -20 <= n <= -10
# F(n) = F(n-7) - F(n-2)               for n > -10
# Memoization dict prevents exponential blowup.

_cache = {}
def F(n):
    if n in _cache: return _cache[n]
    if n < -20:          result = F(n+15) + F(n+10) - F(n+5)
    elif -20 <= n <= -10: result = n * 3
    else:                result = F(n-7) - F(n-2)
    _cache[n] = result
    return result

count = int(input())
for i in range(1, count + 1):
    n = int(input())
    print(f"Case {i}: F({n}) = {F(n)}")
