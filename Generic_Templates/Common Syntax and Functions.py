# ============================================================
# ================== INPUT / OUTPUT ===========================
# ============================================================

# single int
n = int(input())

# multiple ints on one line
a, b = map(int, input().split())

# list of ints
nums = list(map(int, input().split()))

# read entire line
line = input()

# read until EOF (useful sometimes)
import sys
data = sys.stdin.read().split()



# ============================================================
# ================== STRINGS ================================
# ============================================================

# iterate through characters
s = "hello"
for ch in s:
    print(ch)

# string length
length = len(s)

# reverse string
rev = s[::-1]

# check substring
if "he" in s:
    print("yes")

# uppercase / lowercase
s = s.upper()
s = s.lower()

# join list into string
lst = ['a', 'b', 'c']
result = "".join(lst)  # "abc"

# split string
words = "a b c".split()   # ['a', 'b', 'c']



# ============================================================
# ================== LISTS ===================================
# ============================================================

my_list = [1, 2, 3]

# add element
my_list.append(4)

# remove element
my_list.remove(2)

# sort list
my_list.sort()

# reverse list
my_list.reverse()

# slicing
sub = my_list[1:3]

# loop with index
for i in range(len(my_list)):
    print(i, my_list[i])

# loop with index (better)
for index, value in enumerate(my_list):
    print(index, value)



# ============================================================
# ================== DICTIONARY ==============================
# ============================================================

# create dictionary
my_dict = {'apple': 1, 'banana': 2}

# add/update value
my_dict['orange'] = 3

# access value
print(my_dict['apple'])

# safe access
val = my_dict.get('grape', 0)

# loop through dictionary
for k, v in my_dict.items():
    print(k, v)

# check if key exists
if 'apple' in my_dict:
    print("exists")



# ============================================================
# ================== SETS ====================================
# ============================================================

# create set
s = set()

# add
s.add(1)

# remove
s.remove(1)

# check existence
if 2 in s:
    print("yes")

# remove duplicates from list
lst = [1, 2, 2, 3]
unique = list(set(lst))



# ============================================================
# ================== COUNTING / FREQUENCY ====================
# ============================================================

# count manually
count = {}
for x in [1, 2, 2, 3]:
    if x not in count:
        count[x] = 0
    count[x] += 1

# using Counter (faster)
from collections import Counter
c = Counter([1, 2, 2, 3])
print(c[2])  # 2



# ============================================================
# ================== SORTING ================================
# ============================================================

# normal sort
lst = [3, 1, 2]
lst.sort()

# sort descending
lst.sort(reverse=True)

# sort by second value in tuple
pairs = [(1, 3), (2, 1)]
pairs.sort(key=lambda x: x[1])

# sort by multiple rules
pairs.sort(key=lambda x: (-x[1], x[0]))



# ============================================================
# ================== GRID / MATRIX ===========================
# ============================================================

# create grid
grid = [[0]*4 for _ in range(4)]

# directions (8-directional)
dirs = [(-1,-1),(-1,0),(-1,1),
        (0,-1),       (0,1),
        (1,-1),(1,0),(1,1)]

# check bounds
r, c = 1, 2
if 0 <= r < 4 and 0 <= c < 4:
    print("inside")



# ============================================================
# ================== DFS (GRID SEARCH) =======================
# ============================================================

visited = [[False]*4 for _ in range(4)]

def dfs(r, c):
    visited[r][c] = True

    for dr, dc in dirs:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < 4 and 0 <= nc < 4:
            if not visited[nr][nc]:
                dfs(nr, nc)



# ============================================================
# ================== RECURSION + MEMO ========================
# ============================================================

memo = {}

def f(n):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    result = f(n-1) + f(n-2)

    memo[n] = result
    return result



# ============================================================
# ================== BASE CONVERSION =========================
# ============================================================

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# map char -> value
val = {}
for i, ch in enumerate(digits):
    val[ch] = i

# base N to base 10
def to_base10(s, base):
    num = 0
    for ch in s:
        num = num * base + val[ch]
    return num

# base 10 to base N
def from_base10(num, base):
    if num == 0:
        return "0"

    result = ""

    while num > 0:
        result = digits[num % base] + result
        num = num // base

    return result



# ============================================================
# ================== PRIME CHECK =============================
# ============================================================

import math

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True



# ============================================================
# ================== STRING BUILDING =========================
# ============================================================

# avoid doing: result += inside loops (slow)

# good way:
res = []
res.append("a")
res.append("b")
final = "".join(res)



# ============================================================
# ================== COMMON TRICKS ===========================
# ============================================================

# swap values
a, b = b, a

# max / min
m = max(1, 2, 3)
m = min(1, 2, 3)

# absolute value
x = abs(-5)

# check even / odd
if x % 2 == 0:
    print("even")

# range loops
for i in range(5):        # 0 to 4
    pass

for i in range(1, 6):     # 1 to 5
    pass

# reverse loop
for i in range(5, 0, -1):
    pass