# =============================================================================
# Problem 8 — Steganography
# =============================================================================
 
def solve_steg():
    CODE = {0: ' ', 27: '.', 28: '?', 29: '\n'}
    for i in range(1, 27):
        CODE[i] = chr(ord('A') + i - 1)
 
    n = int(input())
    output = []
    for _ in range(n):
        val = int(input())
        code = val % 30
        ch = CODE.get(code, '')
        if ch == '\n':
            output.append('\n')
        else:
            output.append(ch)
 
    # Print without adding extra newlines
    print(''.join(output), end='')
    if output and output[-1] != '\n':
        print()