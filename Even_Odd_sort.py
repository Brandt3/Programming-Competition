# BK Even-Odd Sort
"""
Preserve the original "odd/even pattern" of the input.
Sort even numbers in ascending order.
Sort odd numbers in descending order.
Then reconstruct the list so that:

Chat reuasable comapct version for the first half 

def sort_preserve_parity_pattern(nums):
    even = sorted([n for n in nums if n % 2 == 0])
    odd = sorted([n for n in nums if n % 2 != 0], reverse=True)
    sol = []

    even_i = 0
    odd_i = 0

    for n in nums:
        if n % 2 == 0:
            sol.append(even[even_i])
            even_i += 1
        else:
            sol.append(odd[odd_i])
            odd_i += 1
    return sol
"""

count =  int(input())
nums = [int(input()) for n in range(count)]

even = []
odd = []
check = ""

sol = []

for i in nums:
    if i % 2 == 0:
        even.append(i)
        check += '1'
    else:
        odd.append(i)
        check += '0'

# Defalut sort is ascending 
even.sort()
odd.sort(reverse=True)

low = 0
high = 0

for i in range(len(nums)):
    if check[i] == '1':
        sol.append(even[low])
        low += 1
    if check[i] == '0':
        sol.append(odd[high])
        high += 1

for i in sol:
    print(i)

