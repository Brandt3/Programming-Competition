# BK Alien Math Base 30
"""
convert 2 numbers from base 30 into decimal/nomral and thed add them up
"""

def base30_add(num1, num2):
    # Create mapping: 0-9, A-T (base-30)
    digits = '0123456789ABCDEFGHIJKLMNOPQRST'
    # These will be used for the conversion
    # i is the index of each digit or character
    char_to_val = {ch: i for i, ch in enumerate(digits)}
    val_to_char = {i: ch for i, ch in enumerate(digits)}

    # Pad the shorter number with leading zeros
    max_len = max(len(num1), len(num2))
    num1 = num1.rjust(max_len, '0')
    num2 = num2.rjust(max_len, '0')

    carry = 0
    result = []

    # Add digits from right to left
    # Counting down from 30, 29, ... 0 inlcuding zero
    for i in range(max_len - 1, -1, -1):
        val1 = char_to_val[num1[i]]
        val2 = char_to_val[num2[i]]
        total = val1 + val2 + carry
        # carry the one so it will be added to the  next digit
        carry = total // 30
        result.append(val_to_char[total % 30])

        # So if total = 47, 47 % 30 = 17, and val_to_char[17] = 'H' → we add 'H' to the result.

    if carry > 0:
        result.append(val_to_char[carry])

    # Reverse result since we built it backwards
    return ''.join(reversed(result))

# Read input
n = int(input())
problems = []
for _ in range(n):
    line = input().strip()
    num1, num2 = line.split()
    problems.append((num1, num2))

# Now process and print everything
for i, (num1, num2) in enumerate(problems, 1):
    sum_result = base30_add(num1, num2)
    print(f"Case {i} sum: {sum_result}")
