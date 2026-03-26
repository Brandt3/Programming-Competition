# 2023 Problem 1 — UNI was SCI
# ASCII art printing "SCI" horizontally with a scaling factor.
# Gap between letters = scale spaces. All lines padded to equal length.

LETTERS = {
    'S': ["SSSSS","S    ","SSSSS","    S","SSSSS"],
    'C': ["CCCCC","C    ","C    ","C    ","CCCCC"],
    'I': ["IIIII","  I  ","  I  ","  I  ","IIIII"],
}

def scale_letter(rows, scale):
    result = []
    for row in rows:
        scaled = "".join(ch * scale for ch in row)
        for _ in range(scale):
            result.append(scaled)
    return result

def generate_sign(scale):
    scaled = [scale_letter(LETTERS[ch], scale) for ch in "SCI"]
    gap = " " * scale
    lines = [gap.join(col[r] for col in scaled) for r in range(5 * scale)]
    w = max(len(l) for l in lines)
    return [l.ljust(w) for l in lines]

n = int(input())
results = [generate_sign(int(input())) for _ in range(n)]
for sign in results:
    for line in sign:
        print(line)
