# edit_distance.py — minimum operations to transform one string into another
#
# OPERATIONS: insert, delete, substitute (each costs 1).
# RESULT: dp[len(s1)][len(s2)] after filling the table.
#
# TABLE INTUITION:
#   dp[i][j] = edit distance between s1[:i] and s2[:j]
#   dp[i][0] = i  (delete all i chars of s1)
#   dp[0][j] = j  (insert all j chars of s2)
#   If chars match: free — copy from diagonal (dp[i-1][j-1])
#   If not: 1 + cheapest of delete / insert / substitute
#
# TWEAK FOR:
#   No substitution (insert+delete only): remove the dp[i-1][j-1] option
#   Different costs: change the 1+ to whatever cost the problem specifies
#   Just check if distance <= k: can exit early once any row exceeds k

def edit_distance(s1, s2):
    """Minimum insert/delete/substitute operations to transform s1 into s2."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i          # delete all of s1
    for j in range(n + 1): dp[0][j] = j          # insert all of s2
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]          # chars match — no cost
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],                   # delete from s1
                    dp[i][j-1],                   # insert into s1
                    dp[i-1][j-1]                  # substitute
                )
    return dp[m][n]

def edit_distance_insert_delete_only(s1, s2):
    """Edit distance using only insertions and deletions (substitution = 2 ops)."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1]
            else: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

def solve():
    n = int(input())
    for i in range(1, n + 1):
        s1 = input().strip()
        s2 = input().strip()
        print(f"Case {i}: {edit_distance(s1, s2)}")
