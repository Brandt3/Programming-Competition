# ascii_art.py — universal canvas-based ASCII art sign generator
#
# HOW TO USE ON CONTEST DAY:
#   1. Read the problem — identify which layout it uses
#   2. Pick the matching layout function (or write positions manually)
#   3. Change the word(s) passed to make_sign()
#   4. Adjust the output block if a header line is needed
#   That's it — scale_letter, blit, and render never change.
#
# LAYOUT QUICK REFERENCE:
#   horizontal("MSOE", scale)          2022 — letters side by side
#   vertical("AUE", scale)             2024 — letters stacked top to bottom
#   two_col("MICS","LVII", scale)      2025 — two vertical columns side by side
#   three_col("AB","CD","EF", scale)   predicted — three columns
#   diagonal("SCI", scale)             predicted — letters step down-right
#   mixed_hv("MS","OE", scale)         predicted — top row horiz, rest vertical
#   Custom: pass your own list of (row_offset, col_offset, char) to make_sign()

# ─── LETTER TEMPLATES (5x5) ──────────────────────────────────────────────────
LETTERS = {
    'A': ["  A  ", " A A ", "AAAAA", "A   A", "A   A"],
    'B': ["BBBB ", "B   B", "BBBB ", "B   B", "BBBB "],
    'C': ["CCCCC", "C    ", "C    ", "C    ", "CCCCC"],
    'D': ["DDDD ", "D   D", "D   D", "D   D", "DDDD "],
    'E': ["EEEEE", "E    ", "EEEEE", "E    ", "EEEEE"],
    'F': ["FFFFF", "F    ", "FFFF ", "F    ", "F    "],
    'G': ["GGGGG", "G    ", "G  GG", "G   G", "GGGGG"],
    'H': ["H   H", "H   H", "HHHHH", "H   H", "H   H"],
    'I': ["IIIII", "  I  ", "  I  ", "  I  ", "IIIII"],
    'J': ["JJJJJ", "  J  ", "  J  ", "J J  ", "JJJJ "],
    'K': ["K   K", "K  K ", "KKK  ", "K  K ", "K   K"],
    'L': ["L    ", "L    ", "L    ", "L    ", "LLLLL"],
    'M': ["M   M", "MM MM", "M M M", "M   M", "M   M"],
    'N': ["N   N", "NN  N", "N N N", "N  NN", "N   N"],
    'O': ["OOOOO", "O   O", "O   O", "O   O", "OOOOO"],
    'P': ["PPPPP", "P   P", "PPPPP", "P    ", "P    "],
    'Q': ["QQQQQ", "Q   Q", "Q Q Q", "Q  Q ", "QQQQ "],
    'R': ["RRRR ", "R   R", "RRRR ", "R  R ", "R   R"],
    'S': ["SSSSS", "S    ", "SSSSS", "    S", "SSSSS"],
    'T': ["TTTTT", "  T  ", "  T  ", "  T  ", "  T  "],
    'U': ["U   U", "U   U", "U   U", "U   U", "UUUUU"],
    'V': ["V   V", "V   V", "V   V", " V V ", "  V  "],
    'W': ["W   W", "W   W", "W W W", "WW WW", "W   W"],
    'X': ["X   X", " X X ", "  X  ", " X X ", "X   X"],
    'Y': ["Y   Y", " Y Y ", "  Y  ", "  Y  ", "  Y  "],
    'Z': ["ZZZZZ", "   Z ", "  Z  ", " Z   ", "ZZZZZ"],
}

# ─── CORE ENGINE (never needs to change) ─────────────────────────────────────

def scale_letter(rows, scale):
    """Expand a 5-row letter block by scale factor."""
    result = []
    for row in rows:
        scaled = ''.join(ch * scale for ch in row)
        for _ in range(scale):
            result.append(scaled)
    return result

def blit(canvas, block, r0, c0):
    """Stamp a letter block onto the canvas at (r0, c0). Spaces never overwrite."""
    for r, row in enumerate(block):
        for c, ch in enumerate(row):
            if ch != ' ':
                canvas[r0 + r][c0 + c] = ch

def make_sign(positions, scale, pad=True):
    """
    positions: list of (row_offset, col_offset, char)
    pad=True  → all lines ljust to the same width  (most competition problems)
    pad=False → rstrip only
    Returns list of output strings.
    """
    lh = lw = 5 * scale
    # add "+ scale" below if problem wants a blank line after the final letter too
    max_r = max(r + lh for r, c, _ in positions)
    max_c = max(c + lw for r, c, _ in positions)
    canvas = [[' '] * max_c for _ in range(max_r)]
    for r0, c0, ch in positions:
        blit(canvas, scale_letter(LETTERS[ch], scale), r0, c0)
    lines = [''.join(row) for row in canvas]
    if pad:
        w = max(len(l.rstrip()) for l in lines)
        return [l.ljust(w) for l in lines]
    return [l.rstrip() for l in lines]

# ─── LAYOUT FUNCTIONS (swap in whichever one matches the problem) ─────────────

def horizontal(word, scale):
    """Letters side by side with gap=scale between them. (2022, 2023)"""
    lh = lw = g = 5 * scale
    g = scale
    return [(0, i * (lw + g), ch) for i, ch in enumerate(word)]

def vertical(word, scale):
    """Letters stacked top to bottom with gap=scale blank lines after each. (2024)"""
    lh = lw = 5 * scale
    g  = scale
    return [(i * (lh + g), 0, ch) for i, ch in enumerate(word)]

def two_col(left, right, scale):
    """Two words printed as side-by-side vertical columns. (2025)"""
    lh = lw = 5 * scale
    g  = scale
    L = [(i * (lh + g), 0,       ch) for i, ch in enumerate(left)]
    R = [(i * (lh + g), lw + g,  ch) for i, ch in enumerate(right)]
    return L + R

def three_col(col0, col1, col2, scale):
    """Three words as side-by-side vertical columns. (predicted)"""
    lh = lw = 5 * scale
    g  = scale
    C0 = [(i * (lh + g), 0,           ch) for i, ch in enumerate(col0)]
    C1 = [(i * (lh + g), lw + g,      ch) for i, ch in enumerate(col1)]
    C2 = [(i * (lh + g), 2 * (lw + g), ch) for i, ch in enumerate(col2)]
    return C0 + C1 + C2

def diagonal(word, scale):
    """Each letter steps one letter-width+gap right and one letter-height+gap down. (predicted)"""
    lh = lw = 5 * scale
    g  = scale
    return [(i * (lh + g), i * (lw + g), ch) for i, ch in enumerate(word)]

def mixed_hv(horiz_word, vert_word, scale):
    """Top row horizontal, then remaining letters stacked vertically below. (predicted)"""
    lh = lw = 5 * scale
    g  = scale
    H = [(0,          i * (lw + g), ch) for i, ch in enumerate(horiz_word)]
    V = [(lh + g + i * (lh + g), 0, ch) for i, ch in enumerate(vert_word)]
    return H + V

# ─── MAIN — change this block to match the specific problem ──────────────────

def solve():
    n = int(input())
    for _ in range(n):
        scale = int(input())

        # ── PICK ONE layout and set your word(s): ──────────────────────────
        #positions = horizontal("MSOE", scale)
        #positions = vertical("AUE", scale)
        #positions = two_col("MICS", "LVII", scale)
        positions = three_col("AB", "CD", "EF", scale)
        #positions = diagonal("SCI", scale)
        #positions = mixed_hv("MS", "OE", scale)

        # ── OUTPUT ─────────────────────────────────────────────────────────
        # print(f"Scaling Factor {scale}:")   # uncomment if problem asks for header (2025-style)
        for line in make_sign(positions, scale):
            print(line)

solve()