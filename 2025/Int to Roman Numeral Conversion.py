# =============================================================================
# Problem 2 — Integer to Roman Numeral Conversion
# =============================================================================

def solve_roman():
    val_sym = [
        (1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),
        (100,'C'), (90,'XC'),(50,'L'), (40,'XL'),
        (10,'X'),  (9,'IX'), (5,'V'),  (4,'IV'),
        (1,'I'),
    ]
    n = int(input())
    for _ in range(n):
        num = int(input())
        orig = num
        result = []
        for val, sym in val_sym:
            while num >= val:
                result.append(sym)
                num -= val
        print(f"{orig} is {''.join(result)}")

solve_roman()