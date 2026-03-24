# =============================================================================
# Problem 5 — Twin-Prime Pairs
# =============================================================================

def solve_twin_primes():
    def sieve(limit):
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, limit + 1, i):
                    is_prime[j] = False
        return is_prime

    a, b = map(int, input().split())
    is_prime = sieve(b)

    for p in range(a, b - 1):
        if is_prime[p] and is_prime[p + 2] and p + 2 <= b:
            print(f"({p}, {p + 2})")


solve_twin_primes()