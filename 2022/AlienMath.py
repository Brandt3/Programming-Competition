# =============================================================================
# Problem 6 — Alien Math (Base-30 Addition)
# =============================================================================

# Readable version
def to_base10(s):
    digits = "0123456789ABCDEFGHIJKLMNOPQRST"

    # build value map
    val = {}
    for i, ch in enumerate(digits):
        val[ch] = i

    num = 0
    for ch in s:
        num = num * 30 + val[ch]

    return num


def to_base30(num):
    digits = "0123456789ABCDEFGHIJKLMNOPQRST"

    if num == 0:
        return "0"

    result = ""

    while num > 0:
        remainder = num % 30
        result = digits[remainder] + result
        num = num // 30

    return result


# main program
count = int(input())

for case in range(1, count + 1):
    num1, num2 = input().split()

    value1 = to_base10(num1)
    value2 = to_base10(num2)

    total = value1 + value2

    answer = to_base30(total)

    print(f"Case {case} sum: {answer}")



# Less code

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
