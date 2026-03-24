# =============================================================================
# Problem 6 — Alien Math (Base-30 Addition)
# =============================================================================

def solve_alien_math():
    DIGITS = "0123456789ABCDEFGHIJKLMNOPQRST"
    char_to_val = {ch: i for i, ch in enumerate(DIGITS)}

    def base30_add(a, b):
        a = a[::-1]
        b = b[::-1]
        result = []
        carry = 0
        for i in range(max(len(a), len(b))):
            va = char_to_val[a[i]] if i < len(a) else 0
            vb = char_to_val[b[i]] if i < len(b) else 0
            total = va + vb + carry
            carry = total // 30
            result.append(DIGITS[total % 30])
        if carry:
            result.append(DIGITS[carry])
        return "".join(reversed(result))

    n = int(input())
    for i in range(1, n + 1):
        a, b = input().split()
        total = base30_add(a, b)
        print(f"Case {i} sum: {total}")


solve_alien_math()
