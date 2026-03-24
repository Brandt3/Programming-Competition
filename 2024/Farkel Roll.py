# =============================================================================
# Problem 4 — Farkel Roll
# Find the maximum score for a set of dice (1-6 dice values)
# =============================================================================

def solve_farkel():
    from itertools import combinations

    def score_dice(dice):
        """Score a specific set of dice as a single scoring combination."""
        if not dice:
            return 0
        counts = [0] * 7
        for d in dice:
            counts[d] += 1

        n = len(dice)
        sorted_dice = sorted(dice)

        # Straight 1-6
        if n == 6 and sorted_dice == [1, 2, 3, 4, 5, 6]:
            return 1500

        # Three pairs
        pairs = sum(1 for i in range(1, 7) if counts[i] == 2)
        if n == 6 and pairs == 3:
            return 1500

        # Two triplets
        triplets = sum(1 for i in range(1, 7) if counts[i] == 3)
        if n == 6 and triplets == 2:
            return 2500

        # 6 of a kind
        for i in range(1, 7):
            if counts[i] == 6:
                return 3000

        # 5 of a kind
        for i in range(1, 7):
            if counts[i] == 5:
                return 2000

        # 4 of a kind
        for i in range(1, 7):
            if counts[i] == 4:
                return 1000

        # 3 of a kind
        for i in range(1, 7):
            if counts[i] == 3:
                if i == 1:
                    return 300
                return i * 100

        # Individual ones and fives only
        total = 0
        for i in range(1, 7):
            if i == 1:
                total += counts[1] * 100
            elif i == 5:
                total += counts[5] * 50
            elif counts[i] > 0:
                return 0  # Other dice without forming 3-of-a-kind = Farkel
        return total

    def max_score(dice):
        """Find the maximum score achievable from a roll."""
        n = len(dice)
        best = 0
        # Try all non-empty subsets
        for size in range(1, n + 1):
            for subset in combinations(range(n), size):
                subset_dice = [dice[i] for i in subset]
                s = score_dice(subset_dice)
                if s > best:
                    best = s
        return best

    num_rolls = int(input())
    for _ in range(num_rolls):
        dice = list(map(int, input().split()))
        sorted_dice = sorted(dice)
        score = max_score(dice)
        dice_str = ' '.join(map(str, sorted_dice))
        print(f"{dice_str} scores {score}")

