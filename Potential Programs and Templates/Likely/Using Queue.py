# queue_simulation.py — FIFO queue with time-based simulation
#
# USE FOR: customers/jobs arriving over time, served in order, track wait times.
# KEY DISTINCTION: pure FIFO = this file. Priority-based = use heap.py instead.
#
# TRICKY PARTS:
#   - Simulate TIME, not just steps. Advance the clock to next event.
#   - Multi-server: each server has its own "free at" timestamp.
#   - Wait time = time_service_starts - time_arrived (can be 0).
#   - If customer arrives when server is free: wait = 0, starts immediately.
#
# TWEAK FOR:
#   - Single server: n_servers=1 (default)
#   - Multiple servers: n_servers=k
#   - Named entities: store (arrival, duration, name) tuples
#   - Output: swap in whatever the problem asks (total wait, max wait, order served)

from collections import deque

def simulate_queue(arrivals, n_servers=1):
    """
    arrivals: list of (arrival_time, service_duration, name)
              does NOT need to be pre-sorted
    Returns: list of (name, wait_time) in the order each was served.
    """
    arrivals = sorted(arrivals, key=lambda x: x[0])
    queue          = deque()
    server_free_at = [0] * n_servers
    results        = []
    clock          = 0
    idx            = 0

    while idx < len(arrivals) or queue:
        # Enqueue everyone who has arrived by now
        while idx < len(arrivals) and arrivals[idx][0] <= clock:
            queue.append(arrivals[idx])
            idx += 1

        # Assign waiting customers to free servers
        free = [i for i, t in enumerate(server_free_at) if t <= clock]
        while free and queue:
            server = free.pop(0)
            arrival_time, duration, name = queue.popleft()
            wait = clock - arrival_time
            server_free_at[server] = clock + duration
            results.append((name, wait))

        # Advance clock to next event if nothing left to do right now
        if (not queue or not [i for i,t in enumerate(server_free_at) if t<=clock]):
            next_times = []
            if idx < len(arrivals):
                next_times.append(arrivals[idx][0])
            next_times += [t for t in server_free_at if t > clock]
            if next_times:
                clock = min(next_times)

    return results

def solve():
    n_servers = int(input())                   # number of servers (or 1 if fixed)
    n = int(input())                           # number of customers/jobs
    arrivals = []
    for _ in range(n):
        parts = input().split()
        name         = parts[0]
        arrival_time = int(parts[1])
        duration     = int(parts[2])
        arrivals.append((arrival_time, duration, name))
    results = simulate_queue(arrivals, n_servers)
    for name, wait in results:
        print(f"{name} waited {wait}")

solve()