# =============================================================================
# Problem 1 — Golden (AU) Eagle
# AUE printed VERTICALLY, one letter per block, scale blank lines between letters
# =============================================================================
#Slightly off
def solve_aue():
    LETTERS = {
        'A': [
            "  A  ",
            " A A ",
            "AAAAA",
            "A   A",
            "A   A",
        ],
        'U': [
            "U   U",
            "U   U",
            "U   U",
            "U   U",
            "UUUUU",
        ],
        'E': [
            "EEEEE",
            "E    ",
            "EEEEE",
            "E    ",
            "EEEEE",
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
        word = "AUE"
        width = 5 * scale
        blank_line = " " * width
        lines = []
        for i, ch in enumerate(word):
            lines.extend(scale_letter(LETTERS[ch], scale))
            # Add blank lines after each letter (including last)
            for _ in range(scale):
                lines.append(blank_line)
        # Pad all lines to same width (they already are, but be safe)
        max_len = max(len(l) for l in lines)
        return [l.ljust(max_len) for l in lines]

    n = int(input())
    results = []
    for _ in range(n):
        scale = int(input())
        results.append(generate_sign(scale))

    for sign_lines in results:
        for line in sign_lines:
            print(line)

solve_aue()