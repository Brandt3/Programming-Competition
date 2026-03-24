
# BK M ilwaukee Sort 
"""
The program takes these lucky numbers and organizes them in a special 
order based on a pattern. This pattern is like arranging numbers into 
four vertical lines (called "legs") that form the shape of the letter "M".
The first column gets the first set of numbers, the fourth column gets the 
second set, the second column gets the third set, and the third column gets the fourth set.
"""

def m_sort(numbers):
    # Create four empty lists to represent the four legs of the M shape
    first_leg = []
    fourth_leg = []
    second_leg = []
    third_leg = []
    
    # Fill the legs based on the "M" sort order
    for i, num in enumerate(numbers):
        if i % 4 == 0:
            first_leg.append(num)
        elif i % 4 == 1:
            fourth_leg.append(num)
        elif i % 4 == 2:
            second_leg.append(num)
        elif i % 4 == 3:
            third_leg.append(num)
    
    # Combine the legs in the order: first_leg, fourth_leg, second_leg, third_leg
    sorted_numbers = first_leg + fourth_leg + second_leg + third_leg
    return sorted_numbers

def generate_pick_4_numbers(lucky_numbers):
    # Perform the "M" sort
    sorted_numbers = m_sort(lucky_numbers)
    
    # Output Pick-4 numbers for each day (grouped in sets of 4)
    for day in range(31):
        start_index = day * 4
        pick_4 = sorted_numbers[start_index:start_index + 4]
        print(f"{day + 1}: {' '.join(map(str, pick_4))}")

# Sample Input
input_numbers = list(map(int, input().split()))

# Generate and output the Pick-4 numbers
generate_pick_4_numbers(input_numbers)
