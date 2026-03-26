# union_find.py — disjoint sets with path compression and union by rank
#
# USE FOR: grouping, connectivity queries, counting components.
#   "Are A and B connected?"    → connected(parent, a, b)
#   "How many groups are there?" → count_components(parent)
#   "Merge group containing A with group containing B" → union(parent, rank, a, b)
#
# NODES ARE INTEGERS 0..n-1. For string names, build a name→index dict first.
#
# WHY PATH COMPRESSION: after find(x), point x directly to root.
#   Makes every future find(x) O(1). Include it — it matters for large inputs.
#
# union() returns False if x and y are already in the same group.
# Use this to detect redundant edges or count successful merges.

def make_uf(n):
    """Create union-find for n elements indexed 0..n-1."""
    parent = list(range(n))
    rank   = [0] * n
    return parent, rank

def find(parent, x):
    """Find root of x with path compression (halving)."""
    while parent[x] != x:
        parent[x] = parent[parent[x]]   # point to grandparent (compression)
        x = parent[x]
    return x

def union(parent, rank, x, y):
    """Merge groups of x and y. Returns False if already in same group."""
    rx, ry = find(parent, x), find(parent, y)
    if rx == ry: return False
    if rank[rx] < rank[ry]: rx, ry = ry, rx   # attach smaller under larger
    parent[ry] = rx
    if rank[rx] == rank[ry]: rank[rx] += 1
    return True

def connected(parent, x, y):
    return find(parent, x) == find(parent, y)

def count_components(parent):
    return sum(1 for i in range(len(parent)) if find(parent, i) == i)

def solve():
    n, m = map(int, input().split())          # n nodes, m edges/connections
    parent, rank = make_uf(n)
    for _ in range(m):
        u, v = map(int, input().split())
        union(parent, rank, u, v)
    print(count_components(parent))           # or answer queries below
    # q = int(input())
    # for _ in range(q):
    #     u, v = map(int, input().split())
    #     print("YES" if connected(parent, u, v) else "NO")
