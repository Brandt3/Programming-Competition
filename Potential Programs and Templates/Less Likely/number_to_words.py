# number_to_words.py — convert integer to English words
#
# RANGE: handles 0 to 999,999 (extend the millions block if needed)
# NEGATIVE: prepends "negative"
#
# EDGE CASES THAT TRIP PEOPLE UP:
#   11–19: eleven, twelve... NOT "ten-one", "ten-two"
#   tens:  twenty, thirty, forty (NOT "twoty", "threety")
#   hyphen: twenty-one, forty-five — between tens and ones ONLY
#   zero:  only say "zero" if the number IS zero (not inside larger numbers)
#   100:   "one hundred" — no trailing "zero"
#   1000:  "one thousand" — no "zero hundred"
#
# TWEAK FOR:
#   British English: "one hundred and one" → add "and" before last chunk
#   Larger numbers: add billions block the same way as millions/thousands

ONES = ["","one","two","three","four","five","six","seven","eight","nine",
        "ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen",
        "seventeen","eighteen","nineteen"]
TENS = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def _under_1000(n):
    """Convert 1–999 to words (helper — never called with 0)."""
    parts = []
    if n >= 100:
        parts.append(ONES[n // 100] + " hundred")
        n %= 100
    if n >= 20:
        t = TENS[n // 10]
        o = ONES[n % 10]
        parts.append(t + ("-" + o if o else ""))
    elif n > 0:
        parts.append(ONES[n])
    return " ".join(parts)

def number_to_words(n):
    if n < 0:  return "negative " + number_to_words(-n)
    if n == 0: return "zero"
    parts = []
    if n >= 1_000_000:
        parts.append(_under_1000(n // 1_000_000) + " million")
        n %= 1_000_000
    if n >= 1000:
        parts.append(_under_1000(n // 1000) + " thousand")
        n %= 1000
    if n > 0:
        parts.append(_under_1000(n))
    return " ".join(parts)

def solve():
    n = int(input())
    for i in range(1, n + 1):
        num = int(input())
        print(f"Case {i}: {number_to_words(num)}")
