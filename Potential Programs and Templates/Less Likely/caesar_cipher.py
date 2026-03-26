# caesar_cipher.py — Caesar shift and ROT-13
#
# RULE: shift every letter by n positions, wrap around at Z/z.
#       Non-letters (spaces, punctuation, digits) pass through unchanged.
#       Case is preserved.
#
# ROT-13: shift=13. Special property: encoding == decoding (its own inverse).
# DECODE: caesar(text, -shift)  OR  caesar(text, 26 - shift)
#
# NOTE: shift_letter() already exists in string_tricks.py.
#       This file adds the full-string application and ROT-13 convenience.
#
# TWEAK FOR:
#   Different alphabet size: change 26 to your alphabet size
#   ROT-47: operates on ASCII 33-126 (printable chars), shift=47, wrap at 94

def caesar(text, shift):
    """Shift every letter by shift. Negative shift = decode."""
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def rot13(text):
    return caesar(text, 13)

def solve():
    shift = int(input())
    n = int(input())
    for i in range(1, n + 1):
        line = input()
        # Uncomment whichever the problem asks:
        print(f"Case {i}: {caesar(line, shift)}")      # encode
        # print(f"Case {i}: {caesar(line, -shift)}")   # decode
        # print(f"Case {i}: {rot13(line)}")             # ROT-13
