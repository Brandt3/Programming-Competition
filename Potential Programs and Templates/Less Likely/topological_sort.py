# topological_sort.py — Kahn's algorithm (BFS-based)
#
# USE FOR: ordering items where some must come before others.
#   Course prerequisites, build order, task scheduling.
#
# HOW IT WORKS:
#   1. Count how many things must come BEFORE each node (in-degree).
#   2. Start with nodes that have nothing before them (in-degree 0).
#   3. Each time you "process" a node, reduce its neighbors' in-degrees.
#   4. When a neighbor hits 0, it's ready — add it to the queue.
#   5. If you can't process all nodes → CYCLE EXISTS (no valid order).
#
# TWEAK FOR:
#   Lexicographically smallest order: sort the initial queue and re-sort on each step
#   Named nodes: build a name→index dict, convert edges, convert result back
#   Just cycle detection: check if len(order) == n

from collections import deque

def topological_sort(n, edges):
    """
    n: number of nodes (0 to n-1)
    edges: list of (u, v) — u must come before v
    Returns sorted order, or None if a cycle exists.
    """
    graph  = [[] for _ in range(n)]
    in_deg = [0] * n
    for u, v in edges:
        graph[u].append(v)
        in_deg[v] += 1
    queue = deque(i for i in range(n) if in_deg[i] == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nb in graph[node]:
            in_deg[nb] -= 1
            if in_deg[nb] == 0:
                queue.append(nb)
    return order if len(order) == n else None    # None = cycle detected

def topological_sort_named(nodes, edges):
    """Same but takes string node names and returns string names."""
    idx   = {name: i for i, name in enumerate(nodes)}
    order = topological_sort(len(nodes), [(idx[u], idx[v]) for u, v in edges])
    return [nodes[i] for i in order] if order is not None else None

def solve():
    n, m = map(int, input().split())           # n courses, m prerequisites
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())       # u before v
        edges.append((u, v))
    order = topological_sort(n, edges)
    if order is None:
        print("No valid order (cycle detected)")
    else:
        print(' '.join(map(str, order)))
