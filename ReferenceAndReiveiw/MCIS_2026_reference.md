# MCIS 2026 — Competition Reference Guide

> **VS Code tip:** Press `Ctrl+Shift+V` to open rendered preview alongside this file.  
> The **Outline** panel (Explorer sidebar) lets you jump between sections instantly.

---

## 1. Python Syntax Quick Reference

### Input

```python
n = int(input())                              # single integer
a, b = map(int, input().split())              # two integers, one line
nums = list(map(int, input().split()))        # list of integers, one line
count = int(input())
nums = [int(input()) for _ in range(count)]  # n integers, one per line
grid = [list(map(int, input().split())) for _ in range(rows)]  # 2D grid
parts = line.strip().split(',')              # CSV line
val = float(parts[1]) if parts[1].strip() else None  # blank CSV field → None
```

**EOF (no count given):**
```python
import sys
lines = [l.rstrip() for l in sys.stdin]      # read everything at once
# OR
try:
    while True: lines.append(input())
except EOFError: pass
```

### Output

```python
print(f"Case {i}: {result}")                 # labeled case
print(f"Case {i}: F({n}) = {result}")        # with function notation
print(f"{value:.1f}")                        # float, 1 decimal place
print(" ".join(map(str, nums)))              # list → space-separated string
print(line.ljust(max_len))                   # pad to fixed width
print("text", end="")                        # no trailing newline
print()                                      # blank line
# Sort players: highest score first, alphabetical on tie
ranked = sorted(players, key=lambda p: (-p[1], p[0]))
```

### Lists

```python
evens = [x for x in lst if x % 2 == 0]      # filter
idxs  = [i for i, v in enumerate(lst) if v % 2 == 0]  # matching indices
sorted(lst)                                  # ascending copy
sorted(lst, reverse=True)                    # descending copy
sorted(lst, key=lambda x: abs(x))           # custom key
sorted(players, key=lambda p: (-p[1], p[0])) # multi-key
min(lst, key=lambda e: abs(e - pos))        # nearest to pos
lst[a], lst[b] = lst[b], lst[a]             # swap
flat = [x for row in grid for x in row]     # flatten 2D
```

### Strings

```python
s[::-1]                                      # reverse
s[i:] + s[:i]                               # rotate left by i
''.join(sorted(word))                        # anagram canonical key
''.join(ch * scale for ch in row)           # ASCII art: stretch chars
s.ljust(20)                                  # pad right with spaces
ord('a')  # 97        chr(97)  # 'a'        # char ↔ int
(ord(ch) - ord('a') + n) % 26              # shift letter by n (lowercase)
```

### Dicts and sets

```python
d.get(key, 0)                                # safe get, default 0
freq = {}
for x in lst: freq[x] = freq.get(x, 0) + 1 # count occurrences
groups = {}
for w in words: groups.setdefault(''.join(sorted(w)), []).append(w)
x in my_set                                  # O(1) membership test

# Memoization cache (no imports)
cache = {}
def f(n):
    if n in cache: return cache[n]
    result = ...                             # compute
    cache[n] = result; return result

# 2-variable cache (tuple key)
cache = {}
def f(m, n):
    if (m, n) in cache: return cache[(m, n)]
    ...
    cache[(m, n)] = result; return result
```

### Loops

```python
for i, v in enumerate(lst): pass            # index + value
for a, b in zip(lst1, lst2): pass           # two lists together
for i in range(n-1, -1, -1): pass          # count down n-1 to 0
for i in range(1, n+1): pass               # 1-indexed 1 to n
(x + step) % n                             # wrap around circle of size n
```

### Math

```python
n % m    n // m    n ** 2    abs(x)         # mod, floor div, power, abs
(start - target) % 40                       # clockwise dial distance
(target - start) % 40                       # counter-clockwise
q, r = divmod(17, 5)                        # quotient and remainder together
int(n ** 0.5) + 1                           # integer square root (for sieve)
def gcd(a, b):
    while b: a, b = b, a % b
    return a
```

### Conditions

```python
if lo <= x <= hi: pass                      # chained range check
result = "yes" if condition else "no"       # ternary
all(x > 0 for x in lst)                    # every element satisfies
any(x > 0 for x in lst)                    # at least one satisfies
avg = total / count if count else 0        # safe division
```

---

## 2. File Directory

### Folder: `Less Likely/`

| File | What it solves | Open when you see... |
|------|---------------|----------------------|
| `caesar_cipher.py` | Shift letters by n, ROT-13 | Shift cipher, encoded message, ROT |
| `collatz_sequence.py` | Follow a rule until condition, count steps | "apply rule repeatedly", "how many steps" |
| `edit_distance.py` | Min insert/delete/substitute to transform string A→B | "minimum operations", "transform", "typo" |
| `eof_reading.py` | Read input with no count given | "read until end", no N given |
| `interval_merging.py` | Merge overlapping ranges, total coverage, scheduling | Overlapping intervals, time slots, coverage |
| `lru_cache.py` | Least-recently-used cache simulation | Cache, eviction, page replacement, hits/misses |
| `number_to_words.py` | 1948 → "one thousand nine hundred forty-eight" | Number to English words |
| `run_length_encoding.py` | AAABBC → 3A2BC, decode back | Compress string, run-length, encode/decode |
| `score_rank_output.py` | Sort players by score desc, name asc on tie | Leaderboard, ranking, scores with ties |
| `topological_sort.py` | Order tasks where some must come before others | Prerequisites, dependencies, build order |
| `union_find.py` | Are A and B connected? How many groups? | Connected components, merging groups, friends |

### Folder: `Likely/`

| File | What it solves | Open when you see... |
|------|---------------|----------------------|
| `Ascii art.py` | Scale letters onto a canvas, all layouts | "scaling factor", sign, ASCII art output |
| `Dijkstra Shortest Path.py` | Cheapest path in a weighted graph | Edge weights/costs, shortest route, distances |
| `Using Queue.py` | FIFO queue simulation with time/wait tracking | Customers, arrivals, service times, wait |
| `Using Stack.py` | Balanced brackets, RPN expression evaluator | Brackets `()[]{}`, postfix expression, undo |

### Folder: `Potentially/`

| File | What it solves | Open when you see... |
|------|---------------|----------------------|
| `calendar_arithmetic.py` | Leap years, days between dates, day of week | Day of week, days between, date arithmetic |
| `flood_fill.py` | Count islands, largest region, flood fill a grid | Connected regions, islands, fill color |
| `matrix_transform.py` | Rotate 90°/180°, transpose, spiral order | Rotate grid, transpose, spiral traversal |
| `roman_numerals.py` | Roman→int, int→Roman, validate | Roman numerals, MCMXLVIII |
| `sliding_window.py` | Longest substring no repeat, smallest containing window | Substring, window, no repeat, contains all |
| `statistics_summary.py` | Mean, median, mode with tie handling | Average, median, most frequent, statistics |

### Folder: `Snippets/`  *(small reusable building blocks)*

| File | Contains |
|------|----------|
| `input_reading.py` | Every input pattern: single, multi, grid, CSV, n-per-line |
| `output_formatting.py` | Case labels, padding, join, float format |
| `list_tricks.py` | Filter, find indices, write-back, swap, interleave, count |
| `string_tricks.py` | Rotate, anagram key, scale chars, reverse, shift letter |
| `dict_and_set_tricks.py` | Safe get, count, group-by, invert, cache pattern |
| `math_tricks.py` | Circular arithmetic, dial distance, digit rotate, GCD |
| `loop_tricks.py` | Enumerate, zip, reverse range, 1-indexed, greedy while |
| `sorting_tricks.py` | Custom key, multi-key, nearest element, partition |
| `conditions_and_checks.py` | Range check, ternary, all/any, safe division, validate |
| `grid_tricks.py` | Safe 2D grid, 4-dir + 8-dir neighbors, read board |
| `heap.py` | Max-heap enqueue + dequeue (no imports) |
| `bst.py` | BST as dict, left=2i+1, right=2i+2 |
| `stack_and_queue.py` | List-based stack, deque-based queue |
| `recursion_and_memo.py` | 1-var cache, 2-var tuple key, backtracking skeleton |
| `graph_traversal.py` | BFS shortest path, DFS, adjacency list builder |
| `primes.py` | Sieve, twin, circular, emirp primes |
| `dynamic_programming.py` | 0/1 knapsack (backwards), unbounded (forwards), min-cost |
| `binary_search.py` | Find in sorted list, insert position |
| `subsets.py` | All subsets, subsets of size k |
| `char_and_ord.py` | ord/chr arithmetic, digit ops, base-30 |
| `running_totals.py` | Prefix sums, running avg (skip None), accumulate by key |
| `date_parsing.py` | Parse M/D/YYYY, blank CSV fields, group by year/month |
| `defaultdict_patterns.py` | Frequency, group-by, adjacency list, nested |
| `number_bases.py` | to_base / from_base without imports |
| `swap_and_rotate.py` | Variable swap, list rotate, string rotate, cycle pattern |
| `two_pointer.py` | Two-sum sorted, sliding window max, fill-from-both-ends |
| `combinatorics.py` | All subsets, Farkel dice scoring, n-choose-k |
| `backtracking.py` | Generic skeleton, Kudok-16 style, subset sum |
| `ascii_art_scale.py` | scale_letter() + horizontal make_sign() |
| `dijkstra.py` | *(same as Likely folder but as snippet)* |
| `flood_fill.py` | *(same as Potentially but as snippet)* |

### Folders: `2022/`, `2023/`, `2024/`, `2025/`

Fully solved competition problems. Use to verify your templates work or to study what past problems looked like. Each year's problems are labeled by number.

---

## 3. Pattern Recognition — What to Open

Read the first paragraph of the problem. Match a keyword below, open that file.

| You see in the problem... | Open this file |
|--------------------------|---------------|
| "scaling factor", sign to hang on door, ASCII grid output | `Likely/Ascii art.py` |
| Piecewise function F(n) or H(n) with 2–3 cases | `Snippets/recursion_and_memo.py` |
| Rearrange a list with a named rule / letter shape / legs | `Snippets/sorting_tricks.py` + trace shape on paper |
| Prime numbers, pairs, rotations of digits | `Snippets/primes.py` |
| Insert/delete/enqueue/dequeue, tree operations | `Snippets/heap.py` or `Snippets/bst.py` |
| Weighted edges, cheapest path, road network | `Likely/Dijkstra Shortest Path.py` |
| Customers, arrivals, service time, wait | `Likely/Using Queue.py` |
| Brackets `()[]{}`, postfix / RPN expression | `Likely/Using Stack.py` |
| "Can you make exactly X", minimum operations | `Snippets/dynamic_programming.py` |
| Connected regions, islands, flood fill | `Potentially/flood_fill.py` |
| Overlapping time slots, merge ranges | `Less Likely/interval_merging.py` |
| Rotate grid, transpose, spiral | `Potentially/matrix_transform.py` |
| Roman numerals | `Potentially/roman_numerals.py` |
| Longest substring, window, no repeat | `Potentially/sliding_window.py` |
| Mean / median / mode | `Potentially/statistics_summary.py` |
| Day of week, days between dates | `Potentially/calendar_arithmetic.py` |
| Prerequisites, order of tasks, dependencies | `Less Likely/topological_sort.py` |
| Are A and B connected? Group merging | `Less Likely/union_find.py` |
| Cache, page replacement, eviction | `Less Likely/lru_cache.py` |
| Minimum edits, transform string A → B | `Less Likely/edit_distance.py` |
| Shift cipher, ROT-13, encoded letters | `Less Likely/caesar_cipher.py` |
| Number to English words | `Less Likely/number_to_words.py` |
| Compress string AAABB → 3A2B | `Less Likely/run_length_encoding.py` |
| Follow a rule until condition, count steps | `Less Likely/collatz_sequence.py` |
| Ranking, leaderboard, scores with ties | `Less Likely/score_rank_output.py` |
| Read until end of input, no count N given | `Less Likely/eof_reading.py` |

### Quick triage checklist (first 2 minutes)

- [ ] Is Problem 1 ASCII art? → Yes: open `Ascii art.py`, start immediately
- [ ] Is there a piecewise function definition? → Recursion + cache
- [ ] Is there a letter/shape diagram with numbered cells? → Custom sort — **trace before coding**
- [ ] Does it say "scaling factor"? → ASCII art
- [ ] Does it define F(n) or H(n) with cases? → Recursion
- [ ] Does it say "prime"? → `primes.py`
- [ ] Does it say "graph" / "path" / "intersections"? → BFS or Dijkstra
- [ ] Does it say "insert" / "remove" in order? → Stack or Queue
- [ ] Can you categorize it in 2 min? → If not, **skip and return**

---

## 4. Solving Template-Less / Wildcard Problems

Every year has at least one problem where no template fits. These are **novel simulation problems** — the algorithm is just "do what the problem says." Past examples:

- **2022 Boggle** — custom word search with 8-directional grid DFS
- **2023 Golf Pointers** — 64-point compass with degree-to-name conversion
- **2024 Farkel** — dice scoring where you try every subset
- **2025 Jog in the Woods** — graph traversal with custom intersection rules and edge depletion

### How to recognize one

- The problem describes a game, physical object, or invented system with specific rules
- No standard algorithm name appears anywhere in the problem
- The sample output only makes sense after carefully re-reading the rules
- You feel like "I'd have to build this from scratch" — that's correct, and that's fine

### The reading process

1. **Read the output format first.** Before understanding the algorithm, know exactly what you need to print. Format errors on correct logic = wrong answer.
2. **Read the problem twice.** Once for overall understanding, once to extract the precise rules.
3. **Identify the inputs and outputs.** What comes in, what goes out, what is the transformation between them?
4. **Find the state.** What changes as the simulation runs? (position, counts, a grid, a set of remaining items)
5. **Find the transitions.** What are the rules that change the state at each step?

### How to code it

```python
# General simulation structure:
state = initial_state_from_input()

while not done(state):
    event = next_event(state)        # what happens next
    state = apply_rule(state, event) # update state per problem rules

print(format_output(state))
```

The "rules" become `if/elif` statements that directly mirror the problem text. **Do not try to be clever.** The problem told you what to do — just code it exactly.

### Common traps in novel problems

| Trap | What to watch for |
|------|-------------------|
| **Output format** | Spacing, colons, padding, blank lines between cases — always match the sample exactly |
| **Off-by-one on counts** | "after each letter" vs "between letters" — re-read |
| **Direction of rotation** | CW vs CCW on a dial — draw it out |
| **Inclusive vs exclusive** | Does "stop at N" mean include N or not? |
| **Tie-breaking** | Problems always specify — "alphabetical", "smallest", "all of them" |
| **Edge cases the sample doesn't show** | n=1, empty input, all tied, scale=1 |

### The custom sort trap (most common hard problem)

Letter-shape sorts (M-sort, W-sort, and whatever 2026 brings) look algorithmic but the hard part is **reading the diagram**, not coding. The pattern is always the same:

1. Draw the letter shape on paper
2. Number each cell in the order the inputs fill them
3. Write down: `input index → which leg → which row`
4. That gives you `fill_order`
5. Determine which direction and order you read the legs back out
6. **Only then** open `Snippets/sorting_tricks.py` and fill in the two parameters

Spending 15 minutes tracing correctly is always faster than spending 60 minutes debugging wrong code.

### What to do when you're stuck

1. **Simulate the sample by hand** — work through the sample input step by step on paper and check each step against the sample output
2. **Add print statements** — print intermediate state after each step to find where it diverges
3. **Re-read the problem** — the answer to what's going wrong is almost always in a sentence you glossed over
4. **Move on after 20 minutes** — come back with fresh eyes after solving easier problems

---

*Last updated: MCIS 2026 preparation — covers all problems from 2022–2025 plus predicted new types.*
