# =============================================================================
# Problem 3 — Monthly Weather Summaries
# =============================================================================

def solve_weather():
    n = int(input())
    # month_data[year][month] = {'highs': [...], 'lows': [...]}
    from collections import defaultdict
    data = defaultdict(lambda: defaultdict(lambda: {'highs': [], 'lows': []}))

    month_names = {3: 'March', 4: 'April'}

    for _ in range(n):
        line = input().strip()
        parts = line.split(',')
        date_str = parts[0]
        tmax_str = parts[1] if len(parts) > 1 else ''
        tmin_str = parts[2] if len(parts) > 2 else ''

        month, day, year = map(int, date_str.split('/'))
        if month not in (3, 4):
            continue

        if tmax_str.strip():
            data[year][month]['highs'].append(float(tmax_str))
        if tmin_str.strip():
            data[year][month]['lows'].append(float(tmin_str))

    # Output chronologically
    for year in sorted(data.keys()):
        for month in sorted(data[year].keys()):
            highs = data[year][month]['highs']
            lows  = data[year][month]['lows']
            avg_high = sum(highs) / len(highs) if highs else None
            avg_low  = sum(lows)  / len(lows)  if lows  else None
            if avg_high is not None and avg_low is not None:
                print(f"{month_names[month]} {year}: Average daily high temperature "
                      f"{avg_high:.1f} and Average daily low temperature {avg_low:.1f}")

