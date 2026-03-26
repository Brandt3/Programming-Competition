# MCIS 2026 — Problem Skeletons
# Fill in each solve() as problems are revealed on contest day.
#
# PREDICTED ORDER (based on 2022-2025 patterns):
#   P1  Easy   ASCII art — always Problem 1, always the host school acronym
#   P2  Easy   Warmup — greedy, simple string, Roman parse, encoding
#   P3  Easy   Easy-medium — simulation, math, or date/calendar
#   P4  Medium Medium — cipher, statistics, or data structure
#   P5  Medium Medium — prime variant, sliding window, or matrix
#   P6  Hard   Custom sort — new letter shape, TRACE DIAGRAM BEFORE CODING
#   P7  Medium Data structure — queue, stack, heap, or tree simulation
#   P8  Medium Highly recursive F(n) — skipped 2025, very likely returns
#   P9  Hard   Hard graph/simulation — novel rules, no template fits
#   P10 Hard   If a 10th problem: DP, backtracking, or second graph
#
# CONTEST DAY WORKFLOW:
#   1. Skim ALL problems first (5 min). Note Easy / Medium / Hard.
#   2. Start P1 immediately — ASCII art is free points.
#   3. Do all Easy problems before touching Hard ones.
#   4. Stuck for 20+ min? Move on — come back later.
#   5. Last 10 min: STOP new code. Check output formats.

import sys

# =============================================================================
# Problem 1 — ASCII Art  [EASY — ~15-20 min]
# Change: word/acronym, layout (horizontal/vertical/2-col/diagonal)
# File:   Likely/Ascii art.py  — swap layout function and set word
# =============================================================================

def solve_p1():
    # Copy from Likely/Ascii art.py and set the right layout + word
    pass


# =============================================================================
# Problem 2 — [EASY — ~15-20 min]
# Likely: Roman numeral parse, greedy nearest, word jumble, simple encoding
# Files:  Potentially/roman_numerals.py, Snippets/searching_and_greedy.py
# =============================================================================

def solve_p2():
    pass


# =============================================================================
# Problem 3 — [EASY/MEDIUM — ~20-30 min]
# Likely: simulation, date arithmetic, run-length encoding, stats
# Files:  Potentially/calendar_arithmetic.py, Potentially/statistics_summary.py
#         Less Likely/run_length_encoding.py
# =============================================================================

def solve_p3():
    pass


# =============================================================================
# Problem 4 — [MEDIUM — ~30-40 min]
# Likely: cipher, data structure, matrix transform, flood fill
# Files:  Likely/Using Stack.py, Potentially/matrix_transform.py
#         Potentially/flood_fill.py, Snippets/data_structures.py
# =============================================================================

def solve_p4():
    pass


# =============================================================================
# Problem 5 — [MEDIUM — ~30-40 min]
# Likely: prime variant, sliding window, interval merging, BST/heap
# Files:  Snippets/primes.py, Potentially/sliding_window.py
#         Less Likely/interval_merging.py, Snippets/heap.py
# =============================================================================

def solve_p5():
    pass


# =============================================================================
# Problem 6 — Custom Sort  [HARD — ~45-60 min]
# 95% certain this appears. New letter shape every year (M, Even-Odd, Valley, W).
# PROCESS: (1) draw the shape  (2) trace fill order  (3) trace read-back order
#          (4) ONLY THEN open Snippets/sorting_tricks.py and fill in the two parameters
# Do NOT start coding until you have fill_order and read direction written down.
# =============================================================================

def solve_p6():
    # fill_order = [?, ?, ?, ?]   ← derive from the diagram
    # read bottom-to-top or top-to-bottom? ← derive from the diagram
    numbers = list(map(int, input().split()))
    legs = [[None]*31 for _ in range(4)]
    fill_order = [0, 3, 1, 2]   # CHANGE THIS after tracing

    for idx, num in enumerate(numbers):
        legs[fill_order[idx % 4]][idx // 4] = num

    output = []
    for row in range(30, -1, -1):   # CHANGE direction if needed
        for leg in range(4):         # CHANGE leg order if needed
            output.append(legs[leg][row])

    for day in range(1, 32):
        b = (day-1)*4
        print(f"{day}: {output[b]} {output[b+1]} {output[b+2]} {output[b+3]}")


# =============================================================================
# Problem 7 — Data Structure Simulation  [MEDIUM — ~30-40 min]
# Likely: queue simulation, stack expression, heap operations, graph BFS
# Files:  Likely/Using Queue.py, Likely/Using Stack.py
#         Snippets/heap.py, Snippets/graph_traversal.py
# =============================================================================

def solve_p7():
    pass


# =============================================================================
# Problem 8 — Highly Recursive F(n)  [MEDIUM — ~20-30 min]
# Skipped 2025 after 3 straight years — very likely returns.
# Could be 1-var, 2-var, or 3 cases. ALWAYS add cache dict first.
# File:   Snippets/recursion_and_memo.py
# =============================================================================

def solve_p8():
    _cache = {}
    def F(n):
        if n in _cache: return _cache[n]
        if False:        result = 0   # REPLACE: case 1 condition and formula
        elif False:      result = n   # REPLACE: case 2 (base case — direct formula)
        else:            result = 0   # REPLACE: case 3 formula
        _cache[n] = result
        return result

    count = int(input())
    for i in range(1, count + 1):
        n = int(input())
        print(f"Case {i}: F({n}) = {F(n)}")


# =============================================================================
# Problem 9 — Hard Graph / Novel Simulation  [HARD — ~60 min]
# Novel rules every year — no template fits perfectly.
# PROCESS: (1) read twice  (2) identify STATE and TRANSITIONS
#          (3) code exactly what the problem says, no cleverness
# File:   Snippets/graph_traversal.py for BFS/DFS primitives
# =============================================================================

def solve_p9():
    pass


# =============================================================================
# Problem 10 — Hard Problem  [HARD — ~60 min]  (if it exists)
# Likely: DP, backtracking, or a second graph/simulation problem
# Files:  Snippets/dynamic_programming.py, Snippets/backtracking.py
#         Less Likely/topological_sort.py, Likely/Dijkstra Shortest Path.py
# =============================================================================

def solve_p10():
    pass


# =============================================================================
# Dispatcher — uncomment the problem you're running
# =============================================================================

if __name__ == "__main__":
    # solve_p1()
    # solve_p2()
    # solve_p3()
    # solve_p4()
    # solve_p5()
    # solve_p6()
    # solve_p7()
    # solve_p8()
    # solve_p9()
    # solve_p10()
    pass