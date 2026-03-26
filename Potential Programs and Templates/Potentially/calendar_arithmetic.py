# calendar_arithmetic.py — leap years, days between dates, day of week
#
# No imports needed — all built from first principles.
#
# LEAP YEAR RULE (easy to get wrong):
#   Divisible by 4       → leap year
#   EXCEPT divisible by 100 → NOT leap
#   EXCEPT divisible by 400 → IS leap
#   2000 ✓  1900 ✗  2024 ✓  2100 ✗
#
# DAY OF WEEK anchor: Jan 1 2001 = Monday (verified).
#   Positive offset = forward. days_between handles negative correctly via % 7.
#
# TWEAK FOR:
#   Different epoch: change days_since_epoch(2001,1,1) anchor
#   Sunday=0 convention: change DAY_NAMES order and anchor offset

DAY_NAMES = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
MONTH_DAYS = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(month, year):
    return 29 if month == 2 and is_leap(year) else MONTH_DAYS[month]

def days_since_epoch(year, month, day, epoch=1):
    """Total days from Jan 1 of epoch year up to and including given date."""
    total = sum(366 if is_leap(y) else 365 for y in range(epoch, year))
    total += sum(days_in_month(m, year) for m in range(1, month))
    return total + day

def days_between(y1, m1, d1, y2, m2, d2):
    """Days from date1 to date2. Positive = date2 is later."""
    return days_since_epoch(y2,m2,d2) - days_since_epoch(y1,m1,d1)

def day_of_week(year, month, day):
    """Returns day name. Anchor: Jan 1 2001 = Monday."""
    anchor = days_since_epoch(2001, 1, 1)
    offset = (days_since_epoch(year, month, day) - anchor) % 7
    return DAY_NAMES[offset]

def solve():
    n = int(input())
    for i in range(1, n + 1):
        parts = input().strip().split()
        # Parse M/D/YYYY or YYYY/M/D depending on problem
        month, day, year = map(int, parts[0].split('/'))
        # Uncomment whichever the problem asks:
        print(f"Case {i}: {day_of_week(year, month, day)}")
        # month2, day2, year2 = map(int, parts[1].split('/'))
        # print(f"Case {i}: {days_between(year,month,day,year2,month2,day2)}")
