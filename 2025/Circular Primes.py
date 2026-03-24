# =============================================================================
# Problem 7 — Circular Primes
# =============================================================================

def solve_circular_primes():
    a, b = map(int, input().split())

    # Sieve up to b
    sieve_limit = b
    is_prime = [True] * (sieve_limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(sieve_limit**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, sieve_limit+1, i):
                is_prime[j] = False

    def rotations(n):
        s = str(n)
        return [int(s[i:] + s[:i]) for i in range(len(s))]

    def is_circular_prime(n):
        for r in rotations(n):
            if r > sieve_limit or not is_prime[r]:
                return False
        return True

    for n in range(a, b+1):
        if is_prime[n] and is_circular_prime(n):
            print(n)
