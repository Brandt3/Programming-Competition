# run_length_encoding.py — encode and decode RLE strings
#
# ENCODE: AAABBC → '3A2BC'  (omit_one=True, default)
#         AAABBC → '3A2B1C' (omit_one=False)
# DECODE: '3A2BC' → 'AAABBC'  handles multi-digit counts like '12A'
#
# TRICKY PARTS:
#   Multi-digit counts: '12A' = twelve A's, NOT one A then '2'
#   omit_one: check what the problem shows for single-char runs
#   Decode parses ALL leading digits as the count, then takes one char
#
# TWEAK FOR:
#   Numbers in the string: only works if string contains only letters
#   Different delimiter: e.g. 'A/3' instead of '3A'

def rle_encode(s, omit_one=True):
    """Encode a string using run-length encoding."""
    if not s: return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            prefix = "" if (omit_one and count == 1) else str(count)
            result.append(prefix + s[i-1])
            count = 1
    prefix = "" if (omit_one and count == 1) else str(count)
    result.append(prefix + s[-1])
    return "".join(result)

def rle_decode(s):
    """Decode a run-length encoded string. Handles multi-digit counts."""
    result = []
    i = 0
    while i < len(s):
        count_str = ""
        while i < len(s) and s[i].isdigit():
            count_str += s[i]
            i += 1
        if i < len(s):
            count = int(count_str) if count_str else 1
            result.append(s[i] * count)
            i += 1
    return "".join(result)

def solve():
    n = int(input())
    for i in range(1, n + 1):
        s = input().strip()
        # Uncomment whichever direction the problem asks:
        print(f"Case {i}: {rle_encode(s)}")
        # print(f"Case {i}: {rle_decode(s)}")
