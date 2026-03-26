# lru_cache.py — Least Recently Used cache simulation, no imports
#
# EVICTION RULE: when cache is full and a new key is inserted,
#   remove the key that was accessed LEAST RECENTLY.
#
# IMPLEMENTATION: dict for O(1) lookup + list for access order.
#   Front of list = least recently used (next to evict).
#   Back of list  = most recently used.
#   On every access (get or put): move key to the back.
#   NOTE: list.remove() is O(n) — fine for competition-sized caches.
#
# TWEAK FOR:
#   Hit/miss counting: see hits_and_misses()
#   Page replacement simulation: feed a list of page numbers as accesses
#   Report cache state: print lru.order or lru.cache at any point

class LRUCache:
    def __init__(self, capacity):
        self.cap   = capacity
        self.cache = {}     # key → value
        self.order = []     # front=LRU, back=MRU

    def get(self, key):
        """Return value for key, or -1 if not in cache. Updates recency."""
        if key not in self.cache:
            return -1
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key, value):
        """Insert or update key. Evicts LRU item if at capacity."""
        if key in self.cache:
            self.order.remove(key)           # refresh position
        elif len(self.cache) >= self.cap:
            evict = self.order.pop(0)        # remove least recently used
            del self.cache[evict]
        self.cache[key] = value
        self.order.append(key)

    def hits_and_misses(self, accesses):
        """Simulate read-only accesses. Loads on miss. Returns (hits, misses)."""
        hits = misses = 0
        for key in accesses:
            if self.get(key) == -1:
                self.put(key, key)
                misses += 1
            else:
                hits += 1
        return hits, misses

def solve():
    capacity = int(input())
    lru = LRUCache(capacity)
    n = int(input())
    hits = misses = 0
    for _ in range(n):
        parts = input().split()
        if parts[0] == 'GET':
            result = lru.get(parts[1])
            print(result if result != -1 else "MISS")
        elif parts[0] == 'PUT':
            lru.put(parts[1], parts[2])
    # Or for page replacement:
    # accesses = list(map(int, input().split()))
    # hits, misses = lru.hits_and_misses(accesses)
    # print(f"Hits: {hits}, Misses: {misses}")
