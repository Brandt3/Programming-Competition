# 2023 Problem 3 — Even-Odd Sort
# Rearrange so even-value positions stay even (sorted ascending)
# and odd-value positions stay odd (sorted descending).
# KEY: parity is of the VALUE, not the index.

n = int(input())
vals = [int(input()) for _ in range(n)]

even_idx = [i for i, v in enumerate(vals) if v % 2 == 0]
odd_idx  = [i for i, v in enumerate(vals) if v % 2 != 0]
even_sorted = sorted(vals[i] for i in even_idx)
odd_sorted  = sorted((vals[i] for i in odd_idx), reverse=True)

result = list(vals)
for i, idx in enumerate(even_idx): result[idx] = even_sorted[i]
for i, idx in enumerate(odd_idx):  result[idx] = odd_sorted[i]
for v in result: print(v)
