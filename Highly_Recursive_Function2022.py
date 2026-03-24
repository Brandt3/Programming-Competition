# Highly Revursive Function 2022 (confusing)

# Use a dictionary to store computed H(n) values for speed

"""
promt
Youre given a recursive function H(n) with three cases:

If n < -5:
H(n) = H(n+4) + H(n+2)

If -5 ≤ n < 2:
H(n) = n * 2

If n ≥ 2:
H(n) = H(n-8) - H(n-4) + H(n-3)
"""
memo = {}

def H(n):
    if n in memo:
        return memo[n]
    
    if n < -5:
        result = H(n + 4) + H(n + 2)
    elif -5 <= n < 2:
        result = n * 2
    else:  # n >= 2
        result = H(n - 8) - H(n - 4) + H(n - 3)
    
    memo[n] = result
    return result

# Read input
# These two lines are very good for almost any question with input
#  saying number of cases then case enter case enter etc.
num_cases = int(input())
inputs = [int(input()) for _ in range(num_cases)]

# Compute and print results
for i, n in enumerate(inputs, start=1):
    print(f"Case {i}: H ({n}) = {H(n)}")


# Tried to find a universal code for all  the recursive problems this is as clsoe as i could get wiht chat

"""
def general_recursive_function(n, memo, rules):
    if n in memo:
        return memo[n]
    
    for rule in rules:
        cond, action = rule
        if cond(n):
            result = action(n, memo)
            memo[n] = result
            return result

    raise ValueError("No rule matched for n =", n)

    


   Applying This to the F(n) Problem
Now plug in the rules for F(n):

# Define rules as a list of (condition, action)
def build_F_rules():
    return [
        (lambda n: n < -20, lambda n, memo: F(n + 15, memo) + F(n + 10, memo) - F(n + 5, memo)),
        (lambda n: -20 <= n <= -10, lambda n, memo: n * 3),
        (lambda n: n > -10, lambda n, memo: F(n - 7, memo) - F(n - 2, memo)),
    ]



Well make F(n) a wrapper around general_recursive_function:

def F(n, memo):
    return general_recursive_function(n, memo, build_F_rules()) 

    

And here were the prompts 
F(n):
F(n) = F(n+15) + F(n+10) - F(n+5) for all value of n < -20
F(n) = n*3 for all value of -20 ≤ n ≤ -10
F(n) = F(n-7) - F(n-2) for all values of n > -10.

"""
