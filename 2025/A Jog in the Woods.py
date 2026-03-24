# =============================================================================
# Problem 9 — A Jog in the Woods
# =============================================================================
# Needs adjustment
def solve_jog():
    line1 = input().split()
    n, m = int(line1[0]), int(line1[1])

    coords_raw = list(map(int, input().split()))
    coords = {}
    for i in range(n):
        x, y = coords_raw[2*i], coords_raw[2*i+1]
        coords[i+1] = (x, y)  # 1-indexed

    # adjacency: node -> list of (neighbor, interest_remaining)
    # We need mutable interest counts
    from collections import defaultdict
    edges = {}  # (i,j) with i<j -> current interest count

    adj = defaultdict(list)  # node -> [neighbor nodes]
    for _ in range(m):
        parts = input().split()
        i, j, k = int(parts[0]), int(parts[1]), int(parts[2])
        key = (min(i,j), max(i,j))
        edges[key] = k
        adj[i].append(j)
        adj[j].append(i)

    start_parts = input().split()
    s = int(start_parts[0])
    d = start_parts[1]  # N, S, E, W

    # Determine the first neighbor by direction d from s
    sx, sy = coords[s]
    dir_vec = {'N':(0,1),'S':(0,-1),'E':(1,0),'W':(-1,0)}
    dx, dy = dir_vec[d]

    # Find neighbor in direction d
    def get_neighbor_in_dir(node, direction):
        nx_coord, ny_coord = coords[node]
        ddx, ddy = dir_vec[direction]
        best = None
        best_dist = float('inf')
        for nb in adj[node]:
            nbx, nby = coords[nb]
            vx, vy = nbx - nx_coord, nby - ny_coord
            # Check same direction (same sign, one axis zero)
            if ddx == 0 and ddy != 0:
                if vx == 0 and (vy * ddy > 0):
                    dist = abs(vy)
                    if dist < best_dist:
                        best_dist = dist; best = nb
            elif ddy == 0 and ddx != 0:
                if vy == 0 and (vx * ddx > 0):
                    dist = abs(vx)
                    if dist < best_dist:
                        best_dist = dist; best = nb
        return best

    def use_edge(u, v):
        """Use edge u-v once. Returns False if edge is now exhausted."""
        key = (min(u,v), max(u,v))
        edges[key] -= 1
        if edges[key] <= 0:
            # Remove from adjacency
            adj[u].remove(v)
            adj[v].remove(u)
            del edges[key]

    def get_direction(frm, to):
        """Cardinal direction from frm to to."""
        fx, fy = coords[frm]
        tx, ty = coords[to]
        if tx > fx: return 'E'
        if tx < fx: return 'W'
        if ty > fy: return 'N'
        return 'S'

    def opposite(d):
        return {'N':'S','S':'N','E':'W','W':'E'}[d]

    def branches_at(node, arrival_dir):
        """Get available branches, sorted by their direction, excluding arrival."""
        # All neighbors reachable (edge still exists)
        dirs = []
        for nb in list(adj[node]):
            d_to_nb = get_direction(node, nb)
            if d_to_nb != arrival_dir:
                dirs.append(d_to_nb)
        # Sort cardinal: N, E, S, W (clockwise)
        order = ['N', 'E', 'S', 'W']
        dirs.sort(key=lambda x: order.index(x))
        return dirs

    # Start the jog
    first_nb = get_neighbor_in_dir(s, d)
    if first_nb is None:
        # Dead end immediately
        print(f"{coords[s][0]} {coords[s][1]}")
        return

    use_edge(s, first_nb)
    current = first_nb
    arrival = opposite(d)  # direction we arrived from

    while True:
        available = branches_at(current, arrival)
        if len(available) == 0:
            break
        elif len(available) == 1:
            chosen_dir = available[0]
        elif len(available) == 2:
            chosen_dir = available[0]  # leftmost
        else:  # 3 branches
            chosen_dir = available[1]  # middle

        # Find neighbor in chosen_dir
        next_nb = get_neighbor_in_dir(current, chosen_dir)
        if next_nb is None:
            break

        use_edge(current, next_nb)
        arrival = opposite(chosen_dir)
        current = next_nb

    cx, cy = coords[current]
    print(f"{cx} {cy}")


solve_jog()