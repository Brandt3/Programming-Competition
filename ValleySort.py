# BK Valley Sort Alternate placing them from front to back into a new array:

"""
Take a number of inputs and then sort them as a "valley" 
greatest on the right second greatest on the left etc.
"""


def valley_sort(numbers):
    numbers.sort(reverse=True)  # Step 1: Sort in descending order
    result = [0] * len(numbers)  # Placeholder list
    
    left = 0
    right = len(numbers) - 1
    
    # Alternating between left and right side based off the i value and using that as the index
    for i, num in enumerate(numbers):
        if i % 2 == 0:
            result[left] = num
            left += 1
        else:
            result[right] = num
            right -= 1
            
    return result

# Read input
count = int(input())
nums = [int(input()) for _ in range(count)]

# Apply valley sort
sorted_nums = valley_sort(nums)

# Output
print(count)
for num in sorted_nums:
    print(num)