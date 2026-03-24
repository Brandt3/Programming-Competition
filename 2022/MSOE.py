# =============================================================================
# Problem 1 — MSOE
# =============================================================================

def solve_msoe():
    # Each letter is defined on a 5x5 grid (1 = filled, 0 = blank)
    LETTERS = {
        'M': [
            "M   M",
            "MM MM",
            "M M M",
            "M   M",
            "M   M",
        ],
        'S': [
            "SSSSS",
            "S    ",
            "SSSSS",
            "    S",
            "SSSSS",
        ],
        'O': [
            "OOOOO",
            "O   O",
            "O   O",
            "O   O",
            "OOOOO",
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
        """Scale a letter's rows by the given factor."""
        result = []
        for row in letter_rows:
            scaled_row = "".join(ch * scale for ch in row)
            for _ in range(scale):
                result.append(scaled_row)
        return result

    def generate_sign(scale):
        word = "MSOE"
        scaled = [scale_letter(LETTERS[ch], scale) for ch in word]
        gap = " " * scale
        height = 5 * scale
        lines = []
        for row_idx in range(height):
            line = gap.join(letter[row_idx] for letter in scaled)
            lines.append(line)
        # Pad all lines to the same length
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

solve_msoe()