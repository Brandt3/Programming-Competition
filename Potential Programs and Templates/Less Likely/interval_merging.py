# interval_merging.py — merge overlapping intervals and related problems
#
# CRITICAL: always sort by start time first — everything breaks without it.
#
# OVERLAP CONDITION: start <= prev_end  (not <, so touching intervals merge)
# MERGE END: max(prev_end, curr_end)    (not just curr_end — curr may be contained)
#
# TWEAK FOR:
#   Touching intervals should NOT merge: change <= to <
#   Tuples instead of lists: use (start, end) and build new tuples
#   Named intervals: store extra fields alongside start/end

def merge_intervals(intervals):
    """Merge all overlapping intervals. Input: list of [start, end]."""
    if not intervals: return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:                    # overlaps or touches
            merged[-1][1] = max(merged[-1][1], end)  # extend if needed
        else:
            merged.append([start, end])
    return merged

def total_coverage(intervals):
    """Total number of distinct integer points covered."""
    merged = merge_intervals([list(i) for i in intervals])
    return sum(end - start for start, end in merged)

def can_attend_all(intervals):
    """True if no two intervals overlap (touching is allowed)."""
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:      # strict < = touching ok
            return False
    return True

def insert_interval(intervals, new_interval):
    """Insert new_interval into a list and merge. List need not be sorted."""
    return merge_intervals(intervals + [new_interval])

def solve():
    n = int(input())
    intervals = []
    for _ in range(n):
        start, end = map(int, input().split())
        intervals.append([start, end])
    result = merge_intervals(intervals)
    print(len(result))
    for start, end in result:
        print(f"{start} {end}")
