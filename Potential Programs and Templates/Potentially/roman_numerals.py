# roman_numerals.py — parse, validate, and do arithmetic on Roman numerals
#
# to_roman(n)        int → Roman string         (from 2025 solutions)
# from_roman(s)      Roman string → int         (the new direction)
# is_valid_roman(s)  check if s is a valid Roman numeral (round-trip check)
# roman_add(a, b)    add two Roman numerals, return Roman string
#
# from_roman RULE: scan left to right.
#   current < next → SUBTRACT current   (e.g. I before V = 4)
#   otherwise      → ADD current
#
# TWEAK FOR:
#   Roman → int only:        just use from_roman()
#   int → Roman only:        just use to_roman()  (already in math_and_numbers.py)
#   validate:                is_valid_roman() uses round-trip: convert to int, back to Roman, compare
#   arithmetic:              convert both to int, compute, convert result back

VAL_SYM = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),
           (90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]

def to_roman(n):
    result = []
    for val, sym in VAL_SYM:
        while n >= val: result.append(sym); n -= val
    return ''.join(result)

def from_roman(s):
    val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = 0
    for i in range(len(s)):
        curr = val[s[i]]
        nxt  = val[s[i+1]] if i + 1 < len(s) else 0
        if curr < nxt: result -= curr   # subtractive: IX, XL, CM, etc.
        else:          result += curr
    return result

def is_valid_roman(s):
    """Round-trip check: valid only if converting to int and back gives the same string."""
    if not s or not all(c in 'IVXLCDM' for c in s): return False
    n = from_roman(s)
    if n < 1 or n > 3999: return False
    return to_roman(n) == s

def roman_add(a, b):
    """Add two Roman numeral strings. Returns Roman string."""
    return to_roman(from_roman(a) + from_roman(b))

def roman_subtract(a, b):
    """Subtract b from a. Returns Roman string, or None if result < 1."""
    result = from_roman(a) - from_roman(b)
    return to_roman(result) if result >= 1 else None

def solve():
    n = int(input())
    for i in range(1, n + 1):
        s = input().strip()
        # Uncomment whichever the problem asks for:
        print(f"Case {i}: {from_roman(s)}")           # Roman → int
        # print(f"Case {i}: {to_roman(int(s))}")      # int → Roman
        # print(f"Case {i}: {is_valid_roman(s)}")     # validate
