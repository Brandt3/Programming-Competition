# =============================================================================
# Problem 3 — It Boggles the Mind
# =============================================================================
# Maybe ignore this one, not sure if works
def solve_boggle():
    def get_neighbors(r, c):
        neighbors = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < 4 and 0 <= nc < 4:
                    neighbors.append((nr, nc))
        return neighbors

    def can_form_word(board, word):
        """Check if word can be formed on the board using DFS."""
        word = word.upper()
        # Tokenize board (handle 'QU')
        tokens = []
        for row in board:
            tokens.append(row)  # row is already a list of tokens

        def dfs(pos, token_idx, visited):
            if token_idx == len(word_tokens):
                return True
            r, c = pos
            for nr, nc in get_neighbors(r, c):
                if (nr, nc) not in visited:
                    if tokens[nr][nc] == word_tokens[token_idx]:
                        visited.add((nr, nc))
                        if dfs((nr, nc), token_idx + 1, visited):
                            return True
                        visited.remove((nr, nc))
            return False

        # Convert word to tokens (QU handling)
        word_tokens = []
        i = 0
        while i < len(word):
            if word[i:i+2] == 'QU':
                word_tokens.append('QU')
                i += 2
            else:
                word_tokens.append(word[i])
                i += 1

        # Try starting from each cell
        for r in range(4):
            for c in range(4):
                if tokens[r][c] == word_tokens[0]:
                    if len(word_tokens) == 1:
                        return True
                    visited = {(r, c)}
                    if dfs((r, c), 1, visited):
                        return True
        return False

    def word_score(word):
        length = len(word)
        if length <= 4:
            return 1
        elif length == 5:
            return 2
        elif length == 6:
            return 3
        elif length == 7:
            return 5
        else:
            return 11

    n = int(input())
    players = []
    for _ in range(n):
        line = input().split()
        name = line[0]
        words = [w.upper() for w in line[1:]]
        players.append((name, words))

    board = []
    for _ in range(4):
        row = input().split()
        board.append(row)

    num_dict_words = int(input())
    dictionary = set()
    for _ in range(num_dict_words):
        dictionary.add(input().strip().upper())

    # Remove duplicates across players (words that appear in 2+ players' lists)
    from collections import Counter
    all_words = []
    for _, words in players:
        all_words.extend(words)
    word_counts = Counter(all_words)
    duplicate_words = {w for w, cnt in word_counts.items() if cnt > 1}

    # Score each player
    scores = {}
    for name, words in players:
        score = 0
        for word in words:
            if word in duplicate_words:
                continue
            if len(word) < 3:
                continue
            if word not in dictionary:
                continue
            if can_form_word(board, word):
                score += word_score(word)
        scores[name] = score

    # Sort by score descending, then alphabetically
    ranked = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
    for name, score in ranked:
        print(f"{name} {score}")

solve_boggle()