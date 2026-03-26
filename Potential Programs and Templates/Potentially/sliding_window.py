# sliding_window.py — variable and fixed window patterns
#
# PATTERN: two pointers (left, right). Expand right each step.
#          Shrink left when the window violates the constraint.
#
# TRICKY PART: knowing WHEN to shrink left — it depends on the constraint:
#   No repeats     → shrink when seen[ch] is already in window
#   Contains all   → shrink while all target chars are still covered
#   Fixed size     → shrink when window > k (just subtract leftmost)
#
# TWEAK FOR:
#   Return length only: remove the best_start tracking, just track best_len
#   Return the string:  use s[best_start : best_start + best_len]
#   Case-insensitive:   s = s.lower() before processing

def longest_no_repeat(s):
    """Length of longest substring with no repeating characters."""
    seen = {}           # char → most recent index
    best = left = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1     # jump left past the previous occurrence
        seen[ch] = right
        best = max(best, right - left + 1)
    return best

def longest_no_repeat_str(s):
    """Returns the actual longest substring (not just length)."""
    seen = {}
    best_start = best_len = left = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        if right - left + 1 > best_len:
            best_len = right - left + 1
            best_start = left
    return s[best_start : best_start + best_len]

def smallest_window_containing(s, target):
    """Smallest substring of s that contains every character in target."""
    if not target or not s: return ""
    need = {}
    for ch in target: need[ch] = need.get(ch, 0) + 1
    have = {}; satisfied = 0; required = len(need)
    best = (float('inf'), 0, 0); left = 0
    for right, ch in enumerate(s):
        have[ch] = have.get(ch, 0) + 1
        if ch in need and have[ch] == need[ch]: satisfied += 1
        while satisfied == required:
            if right - left + 1 < best[0]: best = (right - left + 1, left, right)
            lch = s[left]; have[lch] -= 1
            if lch in need and have[lch] < need[lch]: satisfied -= 1
            left += 1
    return s[best[1]:best[2]+1] if best[0] != float('inf') else ""

def max_sum_subarray(nums, k):
    """Maximum sum of any contiguous subarray of exactly size k."""
    w = sum(nums[:k]); best = w
    for i in range(k, len(nums)):
        w += nums[i] - nums[i-k]; best = max(best, w)
    return best

def solve():
    n = int(input())
    for i in range(1, n + 1):
        s = input().strip()
        # Uncomment whichever the problem asks:
        print(f"Case {i}: {longest_no_repeat(s)}")
        # print(f"Case {i}: {longest_no_repeat_str(s)}")
        # target = input().strip()
        # print(f"Case {i}: {smallest_window_containing(s, target)}")
