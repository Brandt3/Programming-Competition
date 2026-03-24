# =============================================================================
# Problem 4 — BST Storage
# =============================================================================

def solve_bst_storage():
    num_bsts = int(input())
    for case in range(1, num_bsts + 1):
        parts = list(map(int, input().split()))
        count = parts[0]
        values = parts[1:count + 1]

        # BST stored in array: root at 0, left child of i at 2i+1, right child at 2i+2
        # We simulate insertion and track the maximum index used
        bst = {}  # index -> value

        def insert(val):
            idx = 0
            while idx in bst:
                if val < bst[idx]:
                    idx = 2 * idx + 1
                else:
                    idx = 2 * idx + 2
            bst[idx] = val

        for v in values:
            insert(v)

        max_idx = max(bst.keys())
        print(f"Case {case}: {max_idx + 1}")

