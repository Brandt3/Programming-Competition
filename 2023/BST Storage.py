# 2023 Problem 4 — BST Storage
# Insert values into a BST stored as an array.
# Root at 0, left child of i = 2i+1, right child = 2i+2.
# Equal values go RIGHT. Answer = max index used + 1.

num_bsts = int(input())
for case in range(1, num_bsts + 1):
    parts = list(map(int, input().split()))
    count, values = parts[0], parts[1:parts[0]+1]
    bst = {}
    def insert(val):
        i = 0
        while i in bst:
            i = 2*i+1 if val < bst[i] else 2*i+2
        bst[i] = val
    for v in values: insert(v)
    print(f"Case {case}: {max(bst.keys()) + 1}")
