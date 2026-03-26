# stack_problems.py — balanced brackets and RPN evaluator
#
# BALANCED BRACKETS — is the string valid?
#   Push opening brackets. On closing bracket, check top matches.
#   Valid if stack is empty at the end.
#   TRICKY: closing bracket on empty stack = invalid immediately.
#
# RPN EVALUATOR — evaluate a postfix expression
#   Push numbers. On operator, pop TWO values, compute, push result.
#   TRICKY: second popped = LEFT operand. Matters for - and /.
#   e.g. "6 2 /" → pop 2 (right), pop 6 (left) → 6/2 = 3, NOT 2/6

def is_balanced(s):
    """Returns True if all brackets in s are correctly matched and nested."""
    stack = []
    match = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != match[ch]:
                return False
            stack.pop()
    return len(stack) == 0

def eval_rpn(tokens):
    """
    tokens: list of strings e.g. ['3', '4', '+', '2', '*']
    Returns numeric result. Uses integer division for /.
    """
    stack = []
    for tok in tokens:
        if tok in '+-*/':
            b = stack.pop()            # right operand (popped second)
            a = stack.pop()            # left operand  (popped first)
            if   tok == '+': stack.append(a + b)
            elif tok == '-': stack.append(a - b)
            elif tok == '*': stack.append(a * b)
            elif tok == '/': stack.append(int(a / b))
        else:
            stack.append(int(tok))
    return stack[0]

def solve_brackets():
    n = int(input())
    for i in range(1, n + 1):
        s = input().strip()
        print(f"Case {i}: {'valid' if is_balanced(s) else 'invalid'}")

def solve_rpn():
    n = int(input())
    for i in range(1, n + 1):
        tokens = input().split()
        print(f"Case {i}: {eval_rpn(tokens)}")