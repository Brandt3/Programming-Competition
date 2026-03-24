# =============================================================================
# Problem 4 — Word Jumble
# =============================================================================

def solve_jumble():
    from collections import defaultdict

    n = int(input())
    scrambled = [input().strip() for _ in range(n)]

    d = int(input())
    # Build anagram index: sorted_letters -> [words]
    anagram_map = defaultdict(list)
    for _ in range(d):
        word = input().strip()
        key = ''.join(sorted(word))
        anagram_map[key].append(word)

    for s in scrambled:
        key = ''.join(sorted(s))
        matches = anagram_map.get(key, [])
        # Filter to same length as scrambled word
        matches = [w for w in matches if len(w) == len(s)]
        matches.sort()
        if matches:
            print(f"{s}: {' '.join(matches)}")
        else:
            print(f"{s}: no match in dictionary")

