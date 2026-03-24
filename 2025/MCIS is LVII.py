# =============================================================================
# Problem 1 — MICS is LVII
# "MICS" left column, "LVII" right column, printed side by side.
# Each letter: 5*scale tall, 5*scale wide, scale blank spaces between columns,
# scale blank lines after each letter (including the last).
# =============================================================================

def solve_lvii():
    LETTERS = {
        'M': [
            "M   M",
            "MM MM",
            "M M M",
            "M   M",
            "M   M",
        ],
        'I': [
            "IIIII",
            "  I  ",
            "  I  ",
            "  I  ",
            "IIIII",
        ],
        'C': [
            "CCCCC",
            "C    ",
            "C    ",
            "C    ",
            "CCCCC",
        ],
        'S': [
            "SSSSS",
            "S    ",
            "SSSSS",
            "    S",
            "SSSSS",
        ],
        'L': [
            "L    ",
            "L    ",
            "L    ",
            "L    ",
            "LLLLL",
        ],
        'V': [
            "V   V",
            "V   V",
            "V   V",
            " V V ",
            "  V  ",
        ],
    }

    def scale_letter(rows, scale):
        result = []
        for row in rows:
            scaled = "".join(ch * scale for ch in row)
            for _ in range(scale):
                result.append(scaled)
        return result

    def generate_sign(scale):
        left_word  = "MICS"
        right_word = "LVII"
        letter_w = 5 * scale
        gap = " " * scale
        blank_row = " " * letter_w

        lines = []
        for left_ch, right_ch in zip(left_word, right_word):
            left_rows  = scale_letter(LETTERS[left_ch],  scale)
            right_rows = scale_letter(LETTERS[right_ch], scale)
            for l, r in zip(left_rows, right_rows):
                lines.append(l + gap + r)
            # scale blank lines after each letter pair
            for _ in range(scale):
                lines.append(blank_row + gap + blank_row)

        max_len = max(len(l) for l in lines)
        return [l.ljust(max_len) for l in lines]

    n = int(input())
    for _ in range(n):
        scale = int(input())
        sign = generate_sign(scale)
        print(f"Scaling Factor {scale}:")
        for line in sign:
            print(line)

