# =============================================================================
# Problem 1 — UNI was SCI
# =============================================================================

def solve_sci():
    LETTERS = {
        'S': [
            "SSSSS",
            "S    ",
            "SSSSS",
            "    S",
            "SSSSS",
        ],
        'C': [
            "CCCCC",
            "C    ",
            "C    ",
            "C    ",
            "CCCCC",
        ],
        'I': [
            "IIIII",
            "  I  ",
            "  I  ",
            "  I  ",
            "IIIII",
        ],
    }

    def scale_letter(letter_rows, scale):
        result = []
        for row in letter_rows:
            scaled_row = "".join(ch * scale for ch in row)
            for _ in range(scale):
                result.append(scaled_row)
        return result

    def generate_sign(scale):
        word = "SCI"
        scaled = [scale_letter(LETTERS[ch], scale) for ch in word]
        gap = " " * scale
        height = 5 * scale
        lines = []
        for row_idx in range(height):
            line = gap.join(letter[row_idx] for letter in scaled)
            lines.append(line)
        max_len = max(len(l) for l in lines)
        lines = [l.ljust(max_len) for l in lines]
        return lines

    n = int(input())
    results = []
    for _ in range(n):
        scale = int(input())
        results.append(generate_sign(scale))

    for sign_lines in results:
        for line in sign_lines:
            print(line)

solve_sci()