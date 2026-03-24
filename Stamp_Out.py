# BK Stamp Out Holes (Bit Confusing to understand)
"""
We are trying to figure out what postage amounts can't be 
made using a handful of stamps, where each stamp can only be used once.
"""

def parse_stamp_values(line, forever_value):
    values = []
    for token in line.split():
        if token == 'F' or token.startswith('F'):
            values.append(forever_value)
        else:
            values.append(int(token))
    return values

def find_unreachable_postage(forever_value, stamp_line):
    stamps = parse_stamp_values(stamp_line, forever_value)
    total = sum(stamps)
    
    # DP array: can_make[x] = True if sum x is achievable
    can_make = [False] * (total + 1) #Place holder index is the value aswell 
                                    # Tells us if we can use that value for addition later on
    can_make[0] = True  # You can always make 0

    for stamp in stamps:
        for i in range(total, stamp - 1, -1):
            if can_make[i - stamp]:
                can_make[i] = True

    # Gather results
    unreachable = [i for i in range(1, total) if not can_make[i]] #If it's false we want it
    print(f"The number of amounts between 0 and {total} that cannot be made exactly is {len(unreachable)}.")
    print("The amounts that cannot be made exactly are:")
    for amount in unreachable:
        print(amount)

# Example usage
forever_value = int(input())
stamp_line = input()
find_unreachable_postage(forever_value, stamp_line)

