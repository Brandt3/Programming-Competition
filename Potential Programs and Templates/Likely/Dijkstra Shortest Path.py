# dijkstra.py — weighted shortest path, no imports needed
#
# WHEN TO USE: graph has edges with different costs/weights and you need
# the cheapest path. If all edges cost the same, use BFS instead (simpler).
#
# INPUT PATTERN (typical):
#   n m          ← n nodes, m edges
#   u v w        ← edge from u to v with weight w (repeat m times)
#   start end    ← find shortest path from start to end
#
# TWEAK FOR:
#   Directed graph   → only add edge one way (remove the second graph line)
#   Path itself      → use dijkstra_with_path() instead
#   All destinations → just print dist after dijkstra(graph, start)

def dijkstra(graph, start):
    """Returns dist dict: dist[node] = cheapest cost from start."""
    dist = {start: 0}
    heap = [(0, start)]                        # (cost, node) — manual priority queue
    while heap:
        heap.sort()                            # sort in place — no heapq needed
        cost, u = heap.pop(0)
        if cost > dist.get(u, float('inf')):
            continue                           # stale entry, skip
        for v, w in graph.get(u, []):
            new_cost = cost + w
            if new_cost < dist.get(v, float('inf')):
                dist[v] = new_cost
                heap.append((new_cost, v))
    return dist

def dijkstra_with_path(graph, start, end):
    """Returns (cost, path) where path is list of nodes start → ... → end."""
    dist = {start: 0}
    prev = {start: None}
    heap = [(0, start)]
    while heap:
        heap.sort()
        cost, u = heap.pop(0)
        if cost > dist.get(u, float('inf')): continue
        if u == end: break
        for v, w in graph.get(u, []):
            new_cost = cost + w
            if new_cost < dist.get(v, float('inf')):
                dist[v] = new_cost
                prev[v] = u
                heap.append((new_cost, v))
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = prev.get(node)
    return dist.get(end, float('inf')), list(reversed(path))

def solve():
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        u, v, w = input().split()
        w = int(w)
        graph.setdefault(u, []).append((v, w))
        graph.setdefault(v, []).append((u, w))  # remove for directed graph
    start, end = input().split()
    cost, path = dijkstra_with_path(graph, start, end)
    if cost == float('inf'):
        print("No path")
    else:
        print(f"Cost: {cost}")
        print(f"Path: {' -> '.join(path)}")

solve()