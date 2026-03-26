# score_rank_output.py — sort players by score, handle ties
#
# APPEARS IN: any multi-player problem (Boggle 2022, Word Jumble 2025)
#
# SORT TRICK: sorted(players, key=lambda p: (-p[1], p[0]))
#   -score  → highest score first (negate to flip ascending sort)
#   name    → alphabetical on tie (already ascending)
#   One sort call handles both keys.
#
# TWO RANK STYLES — read the problem carefully:
#   Standard: tied players share the lowest rank, next rank skips
#             1, 1, 3, 4  (two tied for 1st, next is 3rd)
#   Dense:    tied players share rank, next rank is +1
#             1, 1, 2, 3  (two tied for 1st, next is 2nd)

def rank_players(players):
    """Standard ranking: gaps after ties. Returns [(rank, name, score)]."""
    ranked = sorted(players, key=lambda p: (-p[1], p[0]))
    result = []
    rank = 1
    for i, (name, score) in enumerate(ranked):
        if i > 0 and score < ranked[i-1][1]:
            rank = i + 1                   # jump past tied positions
        result.append((rank, name, score))
    return result

def dense_rank_players(players):
    """Dense ranking: no gaps after ties. Returns [(rank, name, score)]."""
    ranked = sorted(players, key=lambda p: (-p[1], p[0]))
    result = []
    rank = 1
    for i, (name, score) in enumerate(ranked):
        if i > 0 and score < ranked[i-1][1]:
            rank += 1                      # always just +1, no gap
        result.append((rank, name, score))
    return result

def solve():
    n = int(input())
    players = []
    for _ in range(n):
        parts = input().split()
        name, score = parts[0], int(parts[1])
        players.append((name, score))
    # Uncomment whichever rank style the problem uses:
    for rank, name, score in rank_players(players):
        print(f"{name} {score}")           # no rank number (2022/2025 style)
    # for rank, name, score in rank_players(players):
    #     print(f"{rank} {name} {score}")  # with rank number
